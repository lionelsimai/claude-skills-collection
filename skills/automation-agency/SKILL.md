---
name: automation-agency
description: "Sell and deliver outcome-based automation retainers on n8n or Make. Use when the user asks to sell automations to businesses, package workflow retainers, or says 'automation agency' or 'n8n workflows to sell'."
category: AI & Automation
license: MIT
version: 1.0.0
---

# Automation Agency

## Purpose

Sell specific automated outcomes to small businesses on a setup-fee + monthly-retainer model, built on n8n (self-hosted, free) or Make. Never sell "AI strategy" — sell a named pain with a price and a number.

## Workflow

1. **Pick one demoable workflow.** Build it end-to-end for a fictional-but-realistic client first — that's your portfolio piece. Do the process manually twice before automating it; never encode chaos.
2. **Three starter offers** (each: one-time build + monthly retainer):
   - **Lead-capture automation** — form → CRM → instant Slack/WhatsApp alert → AI qualification. The pitch: "no lead waits."
   - **Invoice & expense sorting** — email attachments → folders → ledger rows. The pitch: hours back for the bookkeeper weekly.
   - **Support triage** — inbox → label → drafted reply for human approval. Never auto-send on a client's behalf.
3. **Two-call sales process.** Discovery call: "If we had to deliver value in seven days, what one manual task should we automate?" Scope only that. Solutions call: scoped plan, fixed price, proposal + payment link sent the same day. Price with ROI framing: hours saved × hourly rate × automation %.
4. **Build with guardrails.** Every workflow gets retries, error handling, and a dead-letter path. Money and legal actions never go unsupervised: draft, notify, human approves.
5. **Retainer = maintenance + expansion.** Monitoring, API-change fixes, a monthly report of hours saved, and one new workflow candidate per quarter.

Full offer scripts, workflow specs, and templates in `references/prompts.md`.

## Output Contract

- `offer-one-pager.md` — the three offers with ROI framing and pricing
- `workflow-spec.md` — per workflow: trigger, steps, integrations, error handling, human handoff points
- `discovery-script.md` + `proposal-template.md`
- `monthly-report.md` — hours saved, errors caught, next automation candidate

## Operating Rules

1. Manual twice, then automate. No exceptions.
2. No error handling = no delivery. Retries + dead-letter path on every external call.
3. Draft-first on anything customer-facing; auto-send nothing involving money, legal, or reputation.
4. Never promise ROI you haven't measured. "Save 10 hrs/week" is defensible if measured; "guaranteed income" is a lie that earns refunds.
5. Pricing ladder: fixed-price first project to de-risk → monthly retainers for stability → value-based only once ROI is proven.
6. By client five you're cloning validated workflows; delivery time should collapse — price the outcome, not your hours.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.

## Worked example

Example request: "Use the Automation Agency skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
