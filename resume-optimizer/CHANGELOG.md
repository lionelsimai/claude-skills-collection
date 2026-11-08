# Changelog

## 1.3.0 — 2026-11-08

- Scorer correctness fixes, each found by running the tool on a real
  application and each now covered by a regression test:
  - Phrase matching is word-boundary aware — "excel" no longer matches
    inside "excellence", "seo" no longer matches inside "seasoned".
  - Tokeniser strips sentence punctuation — "functions." and "anz."
    are the words functions / anz, not phantom keywords that get
    reported missing when they are present.
  - Plural variants match both ways ("operations" <-> "operation").
  - Generic JD filler ("key", "own", boilerplate) added to the
    stopword list so it stops crowding real skills out of the top 30.
  - Single words that only appear inside a kept multi-word keyword
    ("south" / "east" next to "south east") are suppressed.
- Added `templates/cover-note.md` — the SKILL.md workflow already told
  users to address genuine gaps in a cover note; it now ships the
  template for it.
- Added CI (`.github/workflows/tests.yml`): the test suite on
  Python 3.9-3.12, a scorer smoke test, and a sync check between the
  root skill files and the `skills/resume-optimizer/` plugin copy.
- Added `CONTRIBUTING.md` stating the contribution bar.
- Test suite doubled (4 -> 8 tests).

## 1.2.0 — 2026-11-08

- Distribution: the repo is now also a Claude Code plugin marketplace
  (`.claude-plugin/`), so Claude Code users install with two commands
  and invoke the skill as `/resume-optimizer:resume-optimizer`.
  The skill itself ships inside `skills/resume-optimizer/` for the
  plugin; the root copy remains for clone-and-copy installs and for
  Codex (`$skill-installer` or `~/.agents/skills`).
- README: install routes for Claude Code (plugin + manual) and Codex.

## 1.1.0 — 2026-11-08

- Scorer: synonym awareness (e.g. JS ↔ JavaScript, AWS ↔ Amazon Web
  Services) so true matches are not missed over spelling.
- Scorer: must-have coverage — keywords from the posting's
  Requirements/Qualifications section are tracked and weighted
  separately in the overall score.
- Added `CITATION.cff` so the repo can be formally cited (GitHub shows
  a "Cite this repository" option).
- Added `templates/` — the tailored-resume skeleton and the delivery
  report every run should produce.
- SKILL.md: JD parsing now splits must-have vs nice-to-have, and the
  delivery step adds LinkedIn headline alignment and a 3-line recruiter
  note built only from the resume's own claims.

## 1.0.0 — 2026-11-08

- Initial release: SKILL.md workflow with the three-bucket honesty
  rule, stdlib-only keyword/scoring script, ATS/keyword/rewrite
  references, examples and tests. MIT licensed.
