# Security Policy

## Reporting a vulnerability

Report security issues through GitHub Issues on this repository, or via
the contact page at https://theaicapitol.com if the issue is sensitive.
Please do not include secrets, credentials or personal data in a public
issue.

## What this collection is — and is not

- Skills are instruction files (`SKILL.md`). They contain no credentials
  and must never ask a user to paste a secret into a skill file.
- Plugins in this collection run locally and are Python 3 standard
  library only unless a plugin README says otherwise. Review any plugin
  before running it, exactly as you would any downloaded code.
- The REST servers shipped by plugins bind locally by default. Put your
  own authentication and TLS in front before exposing one publicly.
  Resumes and lead lists are personal data.

## Guardrails built into the skills

- **No fabrication.** Skills must not invent metrics, clients, audience
  numbers or experience. Claims come from sources the user provides.
- **Draft-only by default.** Outreach, publishing and sending skills
  produce drafts for human approval. Nothing in this collection
  authorises auto-sending.
- **Human approval for consequential actions.** Pricing, contracts,
  payments and external sends always escalate to a human.
- **No secrets in skills.** If you find a credential, token or personal
  identifier in any file here, report it as a security issue so it can
  be removed and rotated.
