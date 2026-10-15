# daemonarchy-desktop

Daemonarchy's own layer over the [Omarchy](https://omarchy.org) desktop on FreeBSD: its look, and the FreeBSD tools it adds to the Omarchy menu. The FreeBSD port [`x11-wm/daemonarchy`](https://github.com/jordanhubbard/freebsd-ports/tree/omarchy/x11-wm/daemonarchy) installs it, along with the applications a full Omarchy install ships. The installer image that puts it all on a disk is [jordanhubbard/daemonarchy](https://github.com/jordanhubbard/daemonarchy).

## Contents

- **Artwork**, original to Daemonarchy: `wallpaper.svg` (rendered to the default wallpaper), `wordmark.svg` (the login screen's logo), `mark.svg` (the horned "A", also the application icon), `about.txt` (the About screen's art) and `screensaver.txt`.
- **Login theme**: `metadata.desktop` and `20-daemonarchy-theme.conf`, an SDDM theme that reuses Omarchy's with the Daemonarchy wordmark.
- **System > FreeBSD** in the Omarchy menu (`omarchy-menu.jsonc`, merged as a vendor menu) and the commands behind it:
  - `daemonarchy-be`: boot environments (bectl)
  - `daemonarchy-home-snapshots`: hourly and daily ZFS snapshots of home directories, run from `daemonarchy.cron`
  - `daemonarchy-jail`: jails
  - `daemonarchy-vm`: bhyve virtual machines, through vm-bhyve
  - `daemonarchy-dtrace`: ready-made DTrace views
  - `daemonarchy-dev-setup`: get the sources and run the desktop from a checkout
  - `daemonarchy-cudalab`: live CUDA studio on NVIDIA, opened from System > FreeBSD

Files carry `%%PREFIX%%` and `%%LOCALBASE%%` placeholders, which the port fills in.

Releases use [semantic versioning](https://semver.org) and match the Daemonarchy release they belong to.

Daemonarchy is not affiliated with or endorsed by Omarchy, the FreeBSD Project, or The FreeBSD Foundation. FreeBSD is a registered trademark of The FreeBSD Foundation.
