# Batocera Web Services — Netflix-Inspired Theme

Give your Batocera setup a fresh, modern look with this **Batocera Web Services Theme**, a sleek Netflix-inspired web interface designed to make browsing and launching your games feel more like a streaming service.

<img width="1280" height="672" alt="New Project" src="https://github.com/user-attachments/assets/7fea1739-ff28-4bdf-a5ee-c3eef08eb95a" />

## Features

* Modern dark interface with a Netflix-inspired design
* Clean game cards with artwork, titles, genres and release information
* Launch games directly from the web interface
* Game information popup with descriptions and artwork
* Integrated game video previews
* Video previews displayed directly over the game artwork
* Responsive design for desktop, tablet and mobile devices
* Smooth scrolling and optimized loading for large game libraries

---

## What's New in v2.0!

-  **Splash Screen:** 3 seconds Netflix style Splash Screen.
-  **Home Screen with Console Lists:** A brand-new homepage displaying all your gaming consoles and system lists with smooth horizontal scrolling.
-  **Global Live Search:** Added an instant search bar to search for any game by title across all your consoles at once.
-  **Consolidated Pop-Up Modal:** Cleaned up the game cards! All detailed game information, descriptions, video previews, badges, manuals, and the **Play button** have been moved directly into the interactive detail pop-up modal.

---

## What's New in 3.0!

- Add to iOS home screen with custom icon and full screen support
- Dice button for a random game, right in the search bar
- Slideshow with random games on the home screen, swipeable and clickable to launch that game
- Bottom console menu is now swipeable, not just tap-the-arrows
- Refresh button now refreshes the page and the game list — a full reset
- Bug fixes

---

## What's New in 4.0!

- **Favorites** - a star on the cover of any favorited game, and a toggle in each game's info popup (needs the companion service, see below)
- **`batocerapower.py` + `batocerapower`** - an optional companion service that adds abilities Batocera's built-in web server doesn't have (reboot, shutdown, restarting EmulationStation, toggling favorites). `index.html` detects on its own whether this service is installed - if it isn't, those specific buttons just stay hidden and everything else works normally.
- **`kodi.sh`** - a one-line launcher script that makes the Kodi button work, by using Batocera's existing `ports` system rather than the companion service. Optional, only needed if you want the Kodi button.

## Game Video Previews

If a game has a video available, a **play button** appears directly on the game artwork.

Clicking the button plays the video **on top of the artwork**, using the same 16:9 area.

Games without an available video will simply display their artwork without a play button.

## Demo Video:

https://www.youtube.com/watch?v=Hv72GlUHEc0

---

# Installation

## 1. Back up the original files

Before installing, it is recommended to make a backup of the original Batocera files:

```text
/usr/share/emulationstation/resources/services/index.html
/usr/share/emulationstation/resources/services/logo-tri.png
```

## 2. Replace the files

Copy the files from this theme/repository to your Batocera system:

```text
/usr/share/emulationstation/resources/services/index.html
/usr/share/emulationstation/resources/services/logo-tri.png
/usr/share/emulationstation/resources/services/logo-ios.png
```

Make sure **all files are replaced**.

## 3. Save the changes

Connect to your Batocera system via **SSH** and run:

```bash
batocera-save-overlay
```

This saves the changes to the Batocera overlay so they remain after a reboot.

## 4. Restart Batocera

After saving the overlay, reboot Batocera or restart the relevant service to see the new theme.

That's it!

Your **Batocera Web Services** page should now use the new Netflix-inspired design.

## 5. Open the Web Interface

Open the Batocera Web Services interface in your browser:

**Using the Batocera hostname:**

```text
http://batocera:1234
```

Or, if the hostname does not work, use the **IP address of your Batocera system**:

```text
http://YOUR-BATOCERA-IP:1234
```

For example:

```text
http://192.168.1.100:1234
```

You can find the IP address of your Batocera system under:

**Main Menu → Network Settings**

Once opened, you should see the new **Batocera Web Services — Netflix-Inspired Theme**. 

---

## Installing the companion service (optional, for Restart/Shutdown/Restart ES/Favorites)

Only do this if you want Restart/Shutdown/Restart EmulationStation/
Favorites to work. Without it, the web page still works fine - those
specific buttons just won't appear. (Kodi is separate - see below.)

**1. Connect via SSH** (see above).

**2. Copy the files into place:**
- `batocerapower.py` → `/userdata/system/batocerapower.py`
- `batocerapower` → `/userdata/system/services/batocerapower`

Either via scp:
```
scp batocerapower.py root@batocera:/userdata/system/batocerapower.py
scp batocerapower root@batocera:/userdata/system/services/batocerapower
```
or, just as easily, drop them into the matching folders over
Batocera's network share (`system` and `system/services`) - same
location either way.

**3. Make it executable and enable it** (back in the SSH session, one
line at a time, then Enter - don't paste all three as one line):
```
chmod +x /userdata/system/services/batocerapower
batocera-services enable batocerapower
batocera-services start batocerapower
```
`enable` makes sure it also starts automatically after every reboot.
This step needs SSH/terminal access - it can't be done through the
file share.

Unlike the web page, files under `/userdata/system` already live on
the persistent partition, so **no `batocera-save-overlay` needed**
here - it survives reboots and updates on its own.

**4. Test it.** From a browser on another device on the same network:
```
http://batocera:1235/ping
```
Should say `ok`. Reload `index.html` in your browser afterward -
Restart/Shutdown/Restart EmulationStation should now appear in the
Options menu, and the favorite star should appear among a game's info
badges in its popup.

### Uninstalling
```
batocera-services stop batocerapower
batocera-services disable batocerapower
rm /userdata/system/services/batocerapower
rm /userdata/system/batocerapower.py
```
The web page's Restart/Shutdown/Restart EmulationStation/Favorite
buttons will simply go back to being hidden - nothing else is
affected, and Kodi (if set up) keeps working regardless.

---

## Installing the Kodi launcher (optional, for the Kodi button)

**1. Copy `kodi.sh` into Batocera's ports folder:**
```
scp kodi.sh root@batocera:/userdata/roms/ports/kodi.sh
```
or drop it into the `ports` folder over Batocera's network share.

**2. Make it executable:**
```
chmod +x /userdata/roms/ports/kodi.sh
```

**3. Refresh your game lists** so Batocera picks up the new entry -
either restart EmulationStation, or use Refresh in the web page's
Options menu, then reload the page.

That's it - no companion service needed. `index.html` automatically
detects `kodi.sh` in the ports list, and the Kodi button in the
Options menu appears and uses it.

**Optional: hide it from your ports game list.** `kodi.sh` will show
up as a regular ports "game" unless you hide it. In EmulationStation
itself, select it and toggle "hidden" the same way you would for any
other game - the web page already respects that flag, so it stays out
of the browsable game list while the Kodi button keeps working.

### Uninstalling
```
rm /userdata/roms/ports/kodi.sh
```
The Kodi button in the Options menu will simply go back to being
hidden.

---

## How favorites work

Favorited games are stored the same way Batocera itself stores them:
a `<favorite>true</favorite>` tag inside that console's
`gamelist.xml`. Un-favoriting removes the tag entirely, rather than
setting it to `false` - matching exactly how Batocera's own files look
for a game that was never favorited.

**EmulationStation only reads `gamelist.xml` at startup** and keeps it
in memory after that, so a favorite toggled from the web page won't
show up live inside EmulationStation on the actual TV/screen until ES
re-reads the file. Use **Refresh** in the Options menu (or restart ES,
or just wait for your next normal ES restart) to sync it up.

Avoid toggling a favorite for a game at the *exact* moment Batocera
might also be writing to that same `gamelist.xml` (e.g. right as you
launch or close that specific game) - there's a small, generally
harmless risk of a write conflict, same as any external tool editing
gamelist files outside of ES.

---

## Security

The companion service (`batocerapower`, port 1235) has **no
authentication** - anyone who can reach that port can reboot/shut
down your machine or edit your game metadata. This is fine on a
trusted home network, but:

- Never expose this port to the internet
- Don't run it on a network you don't fully trust (e.g. public wifi,
  shared student housing, etc.)

The web page itself (`index.html`) only talks to Batocera's own,
already-existing web server and, if installed, the companion service
above - it doesn't send anything anywhere else.

---

## Troubleshooting

**Restart/Shutdown/Restart EmulationStation don't show up in the
Options menu.**
The companion service either isn't installed, isn't running, or isn't
reachable. Test `http://batocera:1235/ping` from a browser on the same
network - if that doesn't say `ok`, re-check the installation steps
above and confirm the service is running with:
```
batocera-services status batocerapower
```

**The Kodi button doesn't show up.**
`index.html` couldn't find a `kodi.sh` entry in the `ports` system.
Double check it's at `/userdata/roms/ports/kodi.sh`, is executable,
and that you refreshed the game lists (Refresh in the Options menu,
or restart EmulationStation) after adding it.

**Kodi goes black and bounces straight back to EmulationStation.**
This used to happen with an earlier version of this project that
launched Kodi through `batocera-es-swissknife --kodi` from the
companion service - that command needs a graphical session that a
background service doesn't have. The current version launches
`kodi.sh` through Batocera's own game-launch mechanism instead (see
"The Kodi launcher" above), which doesn't have this problem since it
uses the exact same, already-working pipeline as launching any other
game. If you're still seeing this, make sure you're on the current
`index.html` and that `kodi.sh` really does just contain:
```
#!/bin/bash
kodi
```

**A favorite toggle doesn't show up in EmulationStation on the TV.**
Expected - see "How favorites work" above. Trigger a Refresh or
restart ES to sync it.

**My changes to `index.html` disappeared after a Batocera update.**
Expected - system updates can reset `/usr/share/...`. Re-copy
`index.html` and run `batocera-save-overlay` again.


---

# Important

Make sure **both files are replaced**.

Replacing only one of the files may cause the theme or some of its features to not work correctly.

It is also recommended to keep a backup of your original files before installing the theme.

---

# Free to Use

This theme is completely **free to use and share**.

Feel free to customize it, improve it and make it your own.

If you enjoy the theme, sharing it with other Batocera users is always appreciated!

## Enjoy your games!
