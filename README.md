# 🎮 Batocera Web Services — Netflix-Inspired Theme

Give your Batocera setup a fresh, modern look with **Batocera Web Services**, a sleek Netflix-inspired web interface designed to make browsing and launching your games feel more like a streaming service.

<img width="1919" height="1034" alt="image" src="https://github.com/user-attachments/assets/a183e432-8aca-47cb-8faf-162f19de297d" />

## 🎮 Features

* 🌑 Modern dark interface with a Netflix-inspired design
* 🖼️ Clean game cards with artwork, titles, genres and release information
* ▶️ Launch games directly from the web interface
* ℹ️ Game information popup with descriptions and artwork
* 🎬 Integrated game video previews
* ▶️ Video previews displayed directly over the game artwork
* 📱 Responsive design for desktop, tablet and mobile devices
* ⚡ Smooth scrolling and optimized loading for large game libraries

## 🎬 Game Video Previews

If a game has a video available, a **play button** appears directly on the game artwork.

Clicking the button plays the video **on top of the artwork**, using the same 16:9 area.

Games without an available video will simply display their artwork without a play button.

---

# 🛠️ Installation

## 1. Back up the original files

Before installing, it is recommended to make a backup of the original Batocera files:

```text
/usr/share/emulationstation/resources/services/index.html
/usr/share/emulationstation/resources/services/logo-tri.png
```

## 2. Replace the files

Copy the files from this theme/repository to your Batocera system:

```text
index.html
→ /usr/share/emulationstation/resources/services/index.html
```

```text
logo.png
→ /usr/share/emulationstation/resources/services/logo-tri.png
```

Make sure **both files are replaced**.

## 3. Save the changes

Connect to your Batocera system via **SSH** and run:

```bash
batocera-save-overlay
```

This saves the changes to the Batocera overlay so they remain after a reboot or system update.

## 4. Restart Batocera

After saving the overlay, reboot Batocera or restart the relevant service to see the new theme.

That's it! 🎉

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

Once opened, you should see the new **Batocera Web Services — Netflix-Inspired Theme**. 🎬🎮


---

# ⚠️ Important

Make sure **both files are replaced**.

Replacing only one of the files may cause the theme or some of its features to not work correctly.

It is also recommended to keep a backup of your original files before installing the theme.

---

# ❤️ Free to Use

This theme is completely **free to use and share**.

Feel free to customize it, improve it and make it your own.

If you enjoy the theme, sharing it with other Batocera users is always appreciated!

## 🎮 Enjoy your games!
