---
name: agent-findability-audit
description: "Audit whether AI agents can find a business's prices and next open appointment without forms. Use when the user asks for an agent readability audit, AI agent SEO, or says 'can agents find my business' or 'agent findability audit'."
category: AI & Automation
license: MIT
version: 1.0.0
---

# Agent Findability Audit

## Purpose

As people delegate search to AI agents, the businesses an agent can read and book win the jobs; the ones it can't lose them silently. Sell the audit + the fix + a monthly retainer to keep prices and times current.

## Workflow

1. **Take the list.** Trade + city + N businesses (e.g. 10 aircon servicing companies in Singapore), usually pulled from Google Maps.
2. **Audit each site** the way a customer would: find a price or price range for the target job, and the next open appointment time. Never fill in a form, enter a zip code, or book anything. Log every step and exactly where it got stuck: form in the way, broken/404 page, bot check, no price listed, or fully blocked.
3. **Score sheet.** Per business: price found? time found? where stuck? This log is the sales hook — most sites get stuck somewhere.
4. **Sell the fix.** Send the business its own audit log next to a fixed one-pager: real prices/ranges as plain text, next open times visible without a form, booking in a few simple steps, Google listing with hours/services/prices filled in. Re-run the audit on the fixed page as proof the agent now finds both.
5. **Monthly retainer.** Keep the prices and times current.

Full audit prompt in `references/prompts.md`.

## Output Contract

- `audit-sheet.csv` — business, price found (y/n), time found (y/n), stuck point, notes
- `findings.md` — patterns across the batch (e.g. "8/10 hide prices behind a quote form")
- `fixed-page-draft.md` — the one-page fix for a client, agent-readable by construction

## Operating Rules

1. **Read-only, always.** No forms, no zip codes, no bookings, no accounts created.
2. **Log "blocked" honestly.** If a page can't be reached or a bot check stops you, log it as blocked — never guess what's on it.
3. **"Agent-readable" means plain text on the page** — no clicks, no forms, no gates required to see the price or the time.
4. **The fix is usually a single page**, not a new website.
5. A lot of this overlaps with plain human usability — that's what makes it an easy yes for the owner.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.

## Worked example

Example request: "Use the Agent Findability Audit skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
