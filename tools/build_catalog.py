#!/usr/bin/env python3
"""Generate catalog.json and skills/INDEX.md from the collection tree.

Stdlib only. Run from anywhere:
    python3 tools/build_catalog.py [repo_root]

Reads every skills/<slug>/SKILL.md frontmatter, plus the plugin folders
(auto-gtm-agent, resume-optimizer, gtm-community-plugins, skill-template),
and writes catalog.json at the repo root and skills/INDEX.md.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict

VERSION = "2.0.0"


def parse_frontmatter(text):
    """Return (name, description, category) from YAML-ish frontmatter.

    Handles plain scalars and block scalars (| or >) for description.
    This is a deliberately small parser for this collection's format,
    not a general YAML parser.
    """
    if not text.startswith("---"):
        return None, None, None
    end = text.find("\n---", 3)
    if end == -1:
        return None, None, None
    block = text[3:end]
    fields = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", lines[i])
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val in ("|", ">", "|-", ">-"):
                buf = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or lines[i] == ""):
                    buf.append(lines[i].strip())
                    i += 1
                fields[key] = " ".join(x for x in buf if x).strip()
                continue
            fields[key] = val.strip('"').strip("'")
        i += 1
    desc = fields.get("description")
    if desc:
        # Block descriptions in this collection carry a TRIGGERS section;
        # keep the catalogue entry to the first sentence block.
        desc = re.split(r"\s+TRIGGERS\s*-", desc)[0].strip()
    return fields.get("name"), desc, fields.get("category")


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    skills_dir = os.path.join(root, "skills")
    entries = []
    by_letter = defaultdict(list)
    for slug in sorted(os.listdir(skills_dir)):
        skill_md = os.path.join(skills_dir, slug, "SKILL.md")
        if not os.path.isfile(skill_md):
            continue
        with open(skill_md, errors="ignore") as fh:
            name, desc, category = parse_frontmatter(fh.read())
        entries.append({
            "slug": slug,
            "name": name or slug,
            "type": "skill",
            "category": category or "",
            "description": desc or "",
            "path": f"skills/{slug}",
            "version": "",
        })
        by_letter[slug[0].upper()].append((slug, desc or ""))

    plugins = []
    gtm_catalog = os.path.join(root, "gtm-community-plugins", "catalog.json")
    gtm_count = 0
    if os.path.isfile(gtm_catalog):
        with open(gtm_catalog) as fh:
            gtm_count = json.load(fh).get("count", 120)
    plugins.append({
        "slug": "gtm-community-plugins", "name": "GTM Community Plugins",
        "type": "suite", "category": "Sales & Marketing",
        "description": f"Suite of {gtm_count} GTM and community plugins (60 GTM + 60 Community) with MCP server, REST API and per-plugin folders. See gtm-community-plugins/catalog.json for the full per-plugin registry.",
        "path": "gtm-community-plugins", "version": "1.0.0", "count": gtm_count,
    })
    plugins.append({
        "slug": "resume-optimizer", "name": "Resume Optimizer",
        "type": "plugin", "category": "Personal Development",
        "description": "Tailor a resume to a job opening: ATS scoring, honest gap analysis, rewrite. v2.0.0 adds an MCP server and REST API with 4 tools.",
        "path": "resume-optimizer", "version": "2.0.0",
    })
    plugins.append({
        "slug": "auto-gtm-agent", "name": "Auto-GTM Agent",
        "type": "plugin", "category": "Sales & Marketing",
        "description": "Human-approved outbound GTM pipeline as a Python CLI with an actions manifest (plugin.json). No MCP server; see auto-gtm-agent/PLUGIN.md.",
        "path": "auto-gtm-agent", "version": "0.1.0",
    })
    template = {
        "slug": "skill-template", "name": "Skill Template", "type": "template",
        "category": "", "description": "The standard SKILL.md template every skill in this collection follows.",
        "path": "skill-template", "version": "",
    }
    catalog = {
        "name": "claude-skills-collection",
        "version": VERSION,
        "author": "Lionel Sim",
        "license": "MIT",
        "counts": {
            "skills_in_skills_dir": len(entries),
            "plugins_individual": 2,
            "plugins_in_gtm_suite": gtm_count,
            "plugins_total": gtm_count + 2,
        },
        "skills": entries,
        "plugins": plugins,
        "templates": [template],
    }
    with open(os.path.join(root, "catalog.json"), "w") as fh:
        json.dump(catalog, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    letter_counts = Counter({k: len(v) for k, v in by_letter.items()})
    lines = [
        "# Skills Index",
        "",
        f"All {len(entries)} skills under `skills/`, A-Z. One line per skill: slug and short description.",
        "Generated by `tools/build_catalog.py` - do not edit by hand.",
        "",
        "## Counts by first letter",
        "",
        "| Letter | Skills | Letter | Skills | Letter | Skills |",
        "|---|---|---|---|---|---|",
    ]
    letters = sorted(letter_counts)
    for i in range(0, len(letters), 3):
        row = letters[i:i + 3]
        cells = []
        for letter in row:
            cells += [letter, str(letter_counts[letter])]
        while len(cells) < 6:
            cells += ["", ""]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    for letter in letters:
        lines.append(f"## {letter}")
        lines.append("")
        for slug, desc in by_letter[letter]:
            short = desc.split(". ")[0].rstrip(".")
            if len(short) > 140:
                short = short[:137] + "..."
            lines.append(f"- [{slug}]({slug}/SKILL.md)" + (f" - {short}" if short else ""))
        lines.append("")
    with open(os.path.join(skills_dir, "INDEX.md"), "w") as fh:
        fh.write("\n".join(lines))
    print(f"skills={len(entries)} plugins_total={gtm_count + 2} catalog=catalog.json index=skills/INDEX.md")


if __name__ == "__main__":
    main()
