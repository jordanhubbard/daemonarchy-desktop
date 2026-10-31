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
  - Cudalab menu integration is withheld pending version-specific native Linuxulator qualification.

Files carry `%%PREFIX%%` and `%%LOCALBASE%%` placeholders, which the port fills in.

The package actions under **Install > Packages** and **Remove > Packages**
open OctoPkg as the desktop user. OctoPkg browses the configured FreeBSD and
Daemonarchy package repositories and requests administrator authentication
for changes. Chromium and OctoPkg are core desktop dependencies.

Use `daemonarchy --help` for the desktop command center. Its implementation
lives in omarchy-freebsd; the internal `omarchy-*` commands remain compatible
with the upstream desktop.

Releases use [semantic versioning](https://semver.org) and match the Daemonarchy release they belong to.

Daemonarchy is not affiliated with or endorsed by Omarchy, the FreeBSD Project, or The FreeBSD Foundation. FreeBSD is a registered trademark of The FreeBSD Foundation.

## Release Engineers

- `jordanhubbard`

## Versioning and releases

This repository's version follows the Daemonarchy product version (`literate.project.json` `version`),
and a release is tagged `vX.Y.Z` (the prefix the port `x11-wm/daemonarchy` already uses in
`DISTVERSIONPREFIX`) at the commit the product release selects. The port pins that exact commit in
`GH_TAGNAME`, so a change here reaches users only after a pin bump in daemonarchy-ports and a new package
in the feed. The last tag before this convention is `v1.1.1`; tags `v1.2.0` to `v1.4.1` were not made
(the port pinned commits), so the first tag under this convention is the product's next release.
`tests/check.py` is the release gate: it checks the shell tools, the menu, the SVG artwork and the desktop
entry without installing anything.
