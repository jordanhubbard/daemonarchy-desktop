#!/usr/bin/env python3
"""Static checks for the Daemonarchy desktop layer; no install, no network.

Shell tools parse (`sh -n`), the menu is JSON with comments, SVG artwork is well-formed XML,
and the SDDM theme files have the keys SDDM reads.
"""

import json
from pathlib import Path
import re
import subprocess
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
TOOLS = sorted(p for p in ROOT.glob("daemonarchy-*") if p.is_file())


class Checks(unittest.TestCase):
    def test_tools_exist_and_parse(self):
        self.assertTrue(TOOLS)
        for tool in TOOLS:
            first = tool.read_text().splitlines()[0]
            shell = "bash" if "bash" in first else "sh"
            with self.subTest(tool.name):
                self.assertTrue(first.startswith("#!"), "missing interpreter line")
                done = subprocess.run([shell, "-n", str(tool)], capture_output=True, text=True)
                self.assertEqual(done.returncode, 0, done.stderr)

    def test_menu_is_json_with_comments(self):
        text = (ROOT / "omarchy-menu.jsonc").read_text()
        text = re.sub(r"^\s*//.*$", "", text, flags=re.MULTILINE)
        text = re.sub(r",(\s*[}\]])", r"\1", text)  # Omarchy's vendor menus allow trailing commas
        menu = json.loads(text)
        self.assertTrue(menu)
        for key, entry in menu.items():
            with self.subTest(key):
                self.assertIn("label", entry)
                self.assertTrue(entry.get("action") or entry.get("description"), "a leaf needs an action or a group a description")

    def test_menu_commands_ship_here_or_are_named(self):
        text = (ROOT / "omarchy-menu.jsonc").read_text()
        for name in re.findall(r"daemonarchy-[a-z-]+", text):
            with self.subTest(name):
                self.assertTrue((ROOT / name).exists() or name == "daemonarchy-pkg",
                                name + " is neither shipped here nor a known external command")

    def test_svg_is_well_formed(self):
        for svg in sorted(ROOT.glob("*.svg")):
            with self.subTest(svg.name):
                self.assertTrue(ET.parse(svg).getroot().tag.endswith("svg"))

    def test_sddm_theme_files(self):
        self.assertIn("[Theme]", (ROOT / "20-daemonarchy-theme.conf").read_text())
        self.assertIn("[SddmGreeterTheme]", (ROOT / "metadata.desktop").read_text())


if __name__ == "__main__":
    unittest.main()
