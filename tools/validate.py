#!/usr/bin/env python3
"""Validate the claude-skills-collection tree. Stdlib only.

    python3 tools/validate.py [repo_root]

Errors (exit 1): broken JSON in any plugin.json / marketplace.json /
catalog.json, a marketplace plugin path that does not exist, a root
catalog.json whose counts do not match the folders on disk, or a broken
relative link in the root README.md.

Warnings (exit stays 0): SKILL.md files without valid name+description
frontmatter. The collection carries a small number of legacy files like
this; they are reported as a compliance statistic, not rewritten.
New contributions must be 100% compliant - see QUALITY.md.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_catalog import parse_frontmatter  # noqa: E402


def find_json_manifests(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__", "node_modules")]
        for fn in filenames:
            if fn in ("plugin.json", "marketplace.json", "catalog.json", "ai-plugin.json"):
                yield os.path.join(dirpath, fn)


def check_skills(root):
    skills_dir = os.path.join(root, "skills")
    total = ok = 0
    defects = []
    if not os.path.isdir(skills_dir):
        return total, ok, defects
    for slug in sorted(os.listdir(skills_dir)):
        path = os.path.join(skills_dir, slug, "SKILL.md")
        if not os.path.isfile(path):
            continue
        total += 1
        with open(path, errors="ignore") as fh:
            name, desc, _ = parse_frontmatter(fh.read())
        if name and desc:
            ok += 1
        else:
            defects.append(slug)
    return total, ok, defects


def check_marketplaces(root):
    errors = []
    for path in find_json_manifests(root):
        if os.path.basename(path) != "marketplace.json":
            continue
        with open(path) as fh:
            data = json.load(fh)
        base = os.path.dirname(os.path.dirname(path)) if os.path.basename(os.path.dirname(path)) == ".claude-plugin" else os.path.dirname(path)
        for plugin in data.get("plugins", []):
            src = plugin.get("source", "")
            if src.startswith("./"):
                target = os.path.normpath(os.path.join(base, src))
                if not os.path.exists(target):
                    errors.append(f"{path}: plugin '{plugin.get('name')}' source '{src}' does not exist")
    return errors


def check_catalog(root):
    errors = []
    path = os.path.join(root, "catalog.json")
    if not os.path.isfile(path):
        return errors
    with open(path) as fh:
        data = json.load(fh)
    skills_dir = os.path.join(root, "skills")
    actual = sum(1 for s in os.listdir(skills_dir) if os.path.isfile(os.path.join(skills_dir, s, "SKILL.md"))) if os.path.isdir(skills_dir) else 0
    listed = len(data.get("skills", []))
    if listed != actual:
        errors.append(f"catalog.json lists {listed} skills but skills/ holds {actual}")
    counts = data.get("counts", {})
    if counts.get("skills_in_skills_dir") not in (None, actual):
        errors.append(f"catalog counts.skills_in_skills_dir={counts.get('skills_in_skills_dir')} != {actual}")
    for entry in data.get("skills", []) + data.get("plugins", []) + data.get("templates", []):
        if not os.path.exists(os.path.join(root, entry.get("path", ""))):
            errors.append(f"catalog entry '{entry.get('slug')}' path '{entry.get('path')}' does not exist")
    return errors


def check_readme_links(root):
    errors = []
    path = os.path.join(root, "README.md")
    if not os.path.isfile(path):
        return errors
    with open(path, errors="ignore") as fh:
        text = fh.read()
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not os.path.exists(os.path.join(root, target)):
            errors.append(f"README.md links to missing path '{target}'")
    return errors


def validate(root):
    root = os.path.abspath(root)
    errors, warnings = [], []
    for path in find_json_manifests(root):
        try:
            with open(path) as fh:
                json.load(fh)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{os.path.relpath(path, root)}: invalid JSON ({exc})")
    total, ok, defects = check_skills(root)
    for slug in defects:
        warnings.append(f"skills/{slug}/SKILL.md: missing name/description frontmatter (legacy)")
    errors += check_marketplaces(root)
    errors += check_catalog(root)
    errors += check_readme_links(root)
    stats = {"skills_total": total, "skills_compliant": ok, "skills_noncompliant": total - ok}
    return errors, warnings, stats


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    errors, warnings, stats = validate(root)
    print(f"skills: {stats['skills_compliant']}/{stats['skills_total']} with valid name+description frontmatter")
    for w in warnings:
        print(f"WARNING: {w}")
    for e in errors:
        print(f"ERROR: {e}")
    print(f"result: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
