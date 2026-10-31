# Active work

Work for this repository. The product-wide queue is
[daemonarchy docs/roadmap/active-work.md](https://github.com/jordanhubbard/daemonarchy/blob/main/docs/roadmap/active-work.md);
an item here is the part of a product item that lands in this repository. Checkboxes are execution
status, not test receipts. The release-goal ledger is [release-goals.json](release-goals.json).

### [ ] DESKTOP-001 — Ship the desktop launchers and menu entries in this package

- **Release target:** 1.5.0
- **Product item:** DESKTOP-001 in the daemonarchy queue (opened 2026-10-31; nothing here is claimed done).
- **Direction:** Receive the Cudalab, Wine and Steam launchers, desktop files, icons and menu entries that
  the installer overlay carries today, so users get fixes through `pkg upgrade` of `x11-wm/daemonarchy`
  without a new ISO.
- **Evidence:**
  - [ ] The launchers, entries and icons are installed from this repository by the port; the installer's
    overlay copies are removed; the tests move here (`tests/check.py` grows to cover them).
