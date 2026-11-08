# Resume Optimizer — an open-source AI skill

Give your AI agent a resume and a job opening, and it returns a polished,
tailored resume that applicant tracking systems (ATS) can parse and
recruiters can find — without inventing a single fact.

Built and maintained by [Lionel Sim](https://www.linkedin.com/in/lionelshen)
(The AI Capitol), founder of OpenBuilder. MIT licensed — free to use,
fork and build on.

## What it does

1. **Reads the resume** you upload (PDF, DOCX, TXT or pasted text)
2. **Reads the job opening** from a link — or pasted job description when
   the job board blocks fetching (LinkedIn and Indeed often do; the skill
   says so instead of faking it)
3. **Scores the resume** against the posting: keyword coverage, section
   checks, format red flags — before and after
4. **Sorts every gap honestly** into three buckets: present but buried,
   rephraseable, genuinely missing. Only the first two ever get written in
5. **Rewrites** the summary and bullets with strong verbs and real,
   sourced numbers, rebuilds the skills section in the posting's own
   vocabulary, and formats everything ATS-safe: single column, standard
   headings, no tables or graphics
6. **Delivers** the tailored resume, the before/after score, the gap
   list and a submission checklist

## The honesty rule

Most "AI resume" tools stuff keywords and inflate claims. This one is
built around the opposite rule: **no fabricated employers, titles, dates,
tools or metrics — ever.** Numbers come from the original resume or the
candidate's own confirmation. Where a metric is missing, the rewrite
leaves a visible `[add metric: …]` slot for the candidate to fill in.

## Install

This is a [Claude Skill](https://www.anthropic.com/news/skills) in the
standard `SKILL.md` format, and works with any agent runtime that reads
skill folders.

```bash
git clone https://github.com/lionelsimai/resume-optimizer.git
cp -r resume-optimizer ~/.claude/skills/
```

Also published in the
[claude-skills-collection](https://github.com/lionelsimai/claude-skills-collection/tree/main/resume-optimizer)
under the same MIT licence.

Then ask your agent:

> Here is my resume and the link to the job I want. Optimise my resume
> for this opening.

## No agent? Use the prompt

[PROMPT.md](PROMPT.md) is the same workflow as one paste-ready prompt —
copy it into ChatGPT, Claude or Gemini, add your resume and the job
description, and it runs the full process: score, honest gap list,
rewrite, before/after.

## Cite or adapt this

- **Cite it:** this repo carries a `CITATION.cff`, so GitHub shows a
  "Cite this repository" option on the repo page (About panel).
- **Adapt it:** fork it, change the references and scorer synonyms for
  your industry, and ship your version. The MIT licence allows use,
  copying, modification and even commercial use — the one condition is
  keeping the copyright and licence notice with it.

## Try the scorer without an agent

The bundled scorer is plain Python 3 (standard library only):

```bash
python3 scripts/resume_optimizer.py keywords --job examples/sample-job.txt
python3 scripts/resume_optimizer.py score \
  --resume examples/sample-resume.txt --job examples/sample-job.txt
```

Run the tests:

```bash
python3 tests/test_resume_optimizer.py
```

## What's inside

| Path | What it is |
|---|---|
| `SKILL.md` | The skill itself: workflow, guardrails, delivery format |
| `PROMPT.md` | The no-install version: one paste-ready prompt for any AI chat |
| `scripts/resume_optimizer.py` | Keyword extraction + ATS scoring with synonym and must-have awareness (stdlib only) |
| `references/ats-playbook.md` | How ATS parsers work and the formatting rules that survive them |
| `references/keyword-method.md` | Extracting and placing keywords honestly — the three buckets |
| `references/rewrite-rules.md` | Summary and bullet formulas, action-verb bank, quantification rules |
| `templates/` | Tailored-resume skeleton + delivery-report format |
| `examples/` | Sample resume, sample job post, scorer report, before/after excerpt |
| `tests/` | Tests for the scorer |
| `CITATION.cff` | Formal citation metadata for the repo |
| `CHANGELOG.md` | What changed, version by version |

## Prefer a website instead?

A free public web version — upload a resume, paste a job link, get the
tailored result in your browser (files are processed client-side, nothing
is uploaded to a server):
https://resume-ai-agent-lionel-s-projects-8f911d78.vercel.app

## Contributing

Issues and pull requests welcome. The bar for contributions: keep the
honesty rule intact, keep the scripts dependency-free, and add a test
for any scoring change.

## Licence

MIT — see [LICENSE](LICENSE).
