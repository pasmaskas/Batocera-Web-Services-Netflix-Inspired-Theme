#!/usr/bin/env python3
"""
Small, simple HTTP server that runs on Batocera itself.
Listens on port 1235 and adds a few things Batocera's own built-in web
server (port 1234) cannot do:
  - a safe reboot/shutdown
  - restarting EmulationStation only
  - toggling a game's favorite status

(Launching Kodi is handled differently - directly through Batocera's own
/launch endpoint on port 1234, the same way any other game is launched.
See filterOutKodiLauncher() in index.html. It doesn't need this service
at all, since a background service like this one has no graphical
session of its own, and Kodi needs one to open on - EmulationStation's
own launch pipeline already has that.)

Restart/Reboot/Shutdown use 'batocera-es-swissknife', Batocera's own
official helper script, so EmulationStation and any running emulator
get stopped cleanly first (same path used by the ES pause menu). This
avoids the userdata corruption that can happen with a raw
'reboot'/'poweroff' call while ES is mid-write to a gamelist.

NO authentication:
Only run this on a trusted home network. Never expose your Batocera
directly to the internet while this service is active - anyone who
can reach this URL can reboot/shut down your machine, or edit your
game metadata.
"""
import http.server
import subprocess
import os
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, parse_qs

PORT = 1235
ROMS_BASE = "/userdata/roms"


def _normalize_gamelist_path(p, system_dir):
    """Resolves a gamelist.xml path (often relative, like './game.sh')
    to an absolute path, so it can be compared reliably against the
    path the browser sends us (which usually comes straight from
    Batocera's own /systems/<name>/games API)."""
    if not p:
        return p
    if p.startswith("./"):
        p = os.path.join(system_dir, p[2:])
    elif not p.startswith("/"):
        p = os.path.join(system_dir, p)
    return os.path.normpath(p)


def _resolve_system_dir(system, rom_path):
    """Figures out which system folder (and therefore which
    gamelist.xml) a game actually lives in.

    Normally that's just ROMS_BASE/<system>. But some Batocera setups
    group several real systems together under one shared EmulationStation
    menu entry (e.g. several separate ports folders like duke3d, doom,
    mohawk grouped into a single 'Ports' menu) - in that case the
    system name the browser reports (the group's name, e.g. 'ports')
    doesn't match the folder the game's gamelist.xml is actually in.
    The game's own absolute path does, though, so we prefer that
    whenever it points inside ROMS_BASE."""
    if rom_path and rom_path.startswith(ROMS_BASE + os.sep):
        rest = rom_path[len(ROMS_BASE) + 1:]
        real_system = rest.split(os.sep, 1)[0]
        if real_system:
            return os.path.join(ROMS_BASE, real_system)
    return os.path.join(ROMS_BASE, system)


def toggle_favorite(system, rom_path, value):
    """Adds/removes the <favorite> tag for the given game in that
    system's gamelist.xml, matching how Batocera itself stores it:
    favorited games get <favorite>true</favorite>, non-favorited games
    have no <favorite> tag at all (not even an explicit 'false').

    Matches games by full (normalized) path first, since some systems
    - ports especially - have many entries whose launcher script shares
    the exact same filename in different folders (e.g. every port
    having its own 'start.sh'), which filename-only matching would get
    wrong or miss entirely. Falls back to filename-only matching for
    any older/unusual gamelist layout where the exact path doesn't
    line up."""
    system_dir = _resolve_system_dir(system, rom_path)
    gamelist_path = os.path.join(system_dir, "gamelist.xml")
    if not os.path.isfile(gamelist_path):
        return False, "gamelist.xml not found (looked in '%s')" % gamelist_path

    tree = ET.parse(gamelist_path)
    root = tree.getroot()
    target_path = _normalize_gamelist_path(rom_path, system_dir)
    target_name = os.path.basename(rom_path)

    found = None
    for game in root.findall("game"):
        p = game.findtext("path", "")
        if _normalize_gamelist_path(p, system_dir) == target_path:
            found = game
            break

    if found is None:
        for game in root.findall("game"):
            p = game.findtext("path", "")
            if os.path.basename(p) == target_name:
                found = game
                break

    if found is None:
        return False, "game not found in gamelist.xml"

    fav_el = found.find("favorite")
    if value:
        if fav_el is None:
            fav_el = ET.SubElement(found, "favorite")
        fav_el.text = "true"
    else:
        if fav_el is not None:
            found.remove(fav_el)

    tree.write(gamelist_path, encoding="utf-8", xml_declaration=True)
    return True, "ok"


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path == "/reboot":
            self._respond("Rebooting...")
            subprocess.Popen(["batocera-es-swissknife", "--reboot"])
        elif parsed.path == "/shutdown":
            self._respond("Shutting down...")
            subprocess.Popen(["batocera-es-swissknife", "--shutdown"])
        elif parsed.path == "/restart-es":
            self._respond("Restarting EmulationStation...")
            subprocess.Popen(["batocera-es-swissknife", "--restart"])
        elif parsed.path == "/favorite":
            qs = parse_qs(parsed.query)
            system = qs.get("system", [""])[0]
            path = qs.get("path", [""])[0]
            value = qs.get("value", ["true"])[0] == "true"
            if not system or not path:
                self._respond("Missing system or path parameter", status=400)
                return
            ok, msg = toggle_favorite(system, path, value)
            self._respond(msg, status=200 if ok else 404)
        elif parsed.path == "/ping":
            self._respond("ok")
        else:
            self.send_response(404)
            self.end_headers()

    def _respond(self, msg, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(msg.encode())

    def log_message(self, format, *args):
        pass  # keep the system log quiet


if __name__ == "__main__":
    server = http.server.HTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()
