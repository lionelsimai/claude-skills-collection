# Contributing to Claude Skills Collection

PRs welcome. The bar is [QUALITY.md](QUALITY.md) — read it first. In
short: no skill or plugin is merged until it is validated, and no claim
in it is fabricated.

## Adding a skill

1. Create `skills/<your-skill-slug>/SKILL.md` (flat layout, kebab-case
   slug). Start from [skill-template/SKILL.md](skill-template/SKILL.md).
2. Frontmatter must carry `name`, a trigger-rich `description` (what it
   does plus the phrases that should trigger it), `category` (use an
   existing category from the catalog where one fits), `license` and
   `version`.
3. The body must include: a When to use section, a step-by-step
   workflow, guardrails and quality checks, and at least one worked
   example or a defined output format.
4. Sanitise: no personal names, private data, home-directory paths or
   one person's private constraints. Generalise so any user can run it.
5. Regenerate the registry and index:
   `python3 tools/build_catalog.py`
6. Validate and test (both must pass, and your files must add no
   warnings):
   `python3 tools/validate.py`
   `python3 tests/test_collection.py`

## Adding a plugin

1. Put the plugin in its own top-level folder with a README that has
   install and usage snippets you have actually run.
2. Ship a valid manifest. Claim an MCP server only if the package
   really provides one; document CLI or REST contracts honestly
   (see `auto-gtm-agent/PLUGIN.md` for the pattern).
3. Code is Python 3 standard library only unless a dependency is named,
   justified and pinned in the plugin README.
4. Add smoke tests for callable tools.
5. Add the plugin to the root `.claude-plugin/marketplace.json` if it
   is Claude Code installable, and to the table in `plugins/README.md`.
6. Run the same regenerate / validate / test steps as for a skill.

## Improving an existing skill

- Test the skill with 3+ different prompts, note what works and what
  does not, and include those notes in your PR.
- Do not silently change a skill's guardrails. Call guardrail changes
  out explicitly in the PR description.

## Questions?

Open an issue, or reach out via https://theaicapitol.com
