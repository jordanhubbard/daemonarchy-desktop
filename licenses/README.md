# Licenses in daemonarchy-desktop

This repository is part of the Daemonarchy project (see `../LICENSE` and the repository map in HACKING.md of https://github.com/jordanhubbard/daemonarchy). Daemonarchy-original work here is under BSD-2-Clause. Before this change the whole repository carried an MIT `LICENSE`; the Daemonarchy-original files were relicensed on the operator's instruction, and the one file that may follow Omarchy's menu entries keeps MIT.

Daemonarchy-original work carries the license terms only, with no copyright notice. Third-party and upstream-derived components keep the upstream notices, which are retained as their licenses require.

This list makes no claim that the licenses of transitive dependencies are represented. It lists the components of this repository and the licenses verified for them, with the evidence for each. Packages that the `x11-wm/daemonarchy` port pulls in from upstream (Omarchy, Chromium, OctoPkg and the rest) carry their own license metadata, which is not reproduced here.

## Table

| Component or path | License | File under licenses/ | Upstream notice and evidence |
|---|---|---|---|
| `wallpaper.svg`, `wordmark.svg`, `mark.svg`, `about.txt`, `screensaver.txt` | BSD-2-Clause | `BSD-2-Clause.txt` | Daemonarchy-original artwork. Evidence: README.md calls it original; git history shows one author (Jordan Hubbard / jkh); the SVGs contain no `<text>` or font reference and no embedded third-party image. |
| `daemonarchy-be`, `daemonarchy-cudalab`, `daemonarchy-dev-setup`, `daemonarchy-dtrace`, `daemonarchy-home-snapshots`, `daemonarchy-jail`, `daemonarchy-vm`, `daemonarchy.cron` | BSD-2-Clause | `BSD-2-Clause.txt` | Daemonarchy-original commands. Evidence: no same-named file in Omarchy; one author in git history; no third-party header. |
| `metadata.desktop`, `20-daemonarchy-theme.conf`, `README.md` | BSD-2-Clause | `BSD-2-Clause.txt` | Configuration naming the Daemonarchy theme. The SDDM theme itself is Omarchy's and is not in this repository. |
| `omarchy-menu.jsonc` | MIT, UNDETERMINED: needs owner review | `MIT.txt` | Its `install.package` and `remove.package` entries and its key scheme follow Omarchy's menu, and the file previously carried the repository's MIT license, so the current license is left in place. If Omarchy-derived text is present the notice is `Copyright (c) David Heinemeier Hansson` (Omarchy's own `LICENSE`). The Daemonarchy additions (`system.freebsd.*`) are original. |
| Anything not listed above | BSD-2-Clause if it has no license header of its own | `BSD-2-Clause.txt` | A file with its own license header or SPDX tag is under that license; otherwise it is Daemonarchy-original work. |

## Texts and their sources

- `BSD-2-Clause.txt`: the SPDX BSD-2-Clause text from spdx/license-list-data (commit 31846481de7ea17d92f2f46fad76abe58b2e9bb0, `text/BSD-2-Clause.txt`), with the template line `Copyright (c) <year> <owner>` removed on the operator's instruction, because no copyright holder is named for Daemonarchy-original work. The rest is unchanged.
- `MIT.txt`: byte-for-byte the `LICENSE` file of Omarchy (https://github.com/omacom/omarchy, formerly basecamp/omarchy), checked identical to the file at that repository's head on 2026-10-31. It carries Omarchy's notice line. The previous `Copyright (c) 2026 Jordan Hubbard` MIT line of this repository is removed.
