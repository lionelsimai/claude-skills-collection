#!/usr/bin/env python3
"""Collection tests. Runs with plain python3 (unittest, stdlib only):

    python3 tests/test_collection.py [repo_root]

No pytest required, though pytest can also collect this file.
"""
import json
import os
import sys
import unittest

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from build_catalog import parse_frontmatter  # noqa: E402
import validate as validator  # noqa: E402

NEW_SKILLS = [
    "icp-and-offer-research", "lead-list-building", "personalised-cold-email",
    "sponsor-and-partner-outreach", "reply-triage-and-booking",
    "follow-up-and-learning-loop", "agent-findability-audit",
    "automation-agency", "whatsapp-ai-agent", "voice-ai-receptionist",
    "agent-plugin-builder", "agent-setup-service", "ai-avatar-critique",
    "video-replica", "objection-to-content", "design-md", "project-manager",
    "sponsor-audience-claims", "career-opportunities",
    "invoice-and-reconciliation-integrity",
]


class TestFrontmatterParser(unittest.TestCase):
    def test_plain(self):
        name, desc, cat = parse_frontmatter("---\nname: x\ndescription: Does a thing.\ncategory: GTM\n---\n# X\n")
        self.assertEqual((name, desc, cat), ("x", "Does a thing.", "GTM"))

    def test_block_scalar_strips_triggers(self):
        name, desc, _ = parse_frontmatter("---\nname: y\ndescription: |\n  Does a thing.\n  \n  TRIGGERS - Use when:\n  - foo\n---\n")
        self.assertEqual(desc, "Does a thing.")

    def test_no_frontmatter(self):
        self.assertEqual(parse_frontmatter("# No frontmatter\n"), (None, None, None))


class TestNewSkills(unittest.TestCase):
    def test_new_skills_exist_and_comply(self):
        for slug in NEW_SKILLS:
            path = os.path.join(ROOT, "skills", slug, "SKILL.md")
            self.assertTrue(os.path.isfile(path), f"missing {path}")
            with open(path, errors="ignore") as fh:
                text = fh.read()
            name, desc, _ = parse_frontmatter(text)
            self.assertTrue(name and desc, f"{slug}: frontmatter incomplete")
            low = text.lower()
            self.assertIn("when to use", low, f"{slug}: no When to use section")
            self.assertIn("guardrail", low, f"{slug}: no guardrails section")
            self.assertTrue("example" in low or "output" in low, f"{slug}: no example/output section")
            for banned in ("~/workspace", "/home/", "9,500"):
                self.assertNotIn(banned, text, f"{slug}: unsanitised content '{banned}'")


class TestManifests(unittest.TestCase):
    def test_marketplace_paths_exist(self):
        self.assertEqual(validator.check_marketplaces(ROOT), [])

    def test_catalog_matches_folders(self):
        if os.path.isfile(os.path.join(ROOT, "catalog.json")):
            self.assertEqual(validator.check_catalog(ROOT), [])

    def test_root_marketplace_lists_three_plugins(self):
        path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
        if not os.path.isfile(path):
            self.skipTest("root marketplace not present in this tree")
        with open(path) as fh:
            names = {p["name"] for p in json.load(fh)["plugins"]}
        self.assertEqual(names, {"resume-optimizer", "auto-gtm-agent", "gtm-community-plugins"})


if __name__ == "__main__":
    unittest.main(argv=[sys.argv[0]], verbosity=2)
