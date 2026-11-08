---
name: agent-plugin-builder
description: "Design a small quote-and-booking plugin that AI agents can call, with get_quote and book_slot style tools. Use when the user asks to build a plugin for agents, a quote plugin, a booking plugin, or an agent-callable API."
category: AI & Automation
license: MIT
version: 1.0.0
---

# Dots Plugin Builder

## Purpose

Build a product, not a service: a small plugin with two actions — `get_quote` and `book_slot` — that an AI agent calls when a user asks for a price or a booking. Monetize per lead or per booked job, paid by the user or by the business receiving the job.

## Workflow

1. **Pick one job, one trade, one city.** Something people ask for constantly, where prices fall in a clear range (e.g. aircon servicing in Singapore, drain cleaning, garage door repair).
2. **Build the price table** from public prices: job, size/type where it matters, low/high price, source per row. Label referral sites as such. One city at first — prices vary a lot by area.
3. **Build the app.** Two actions: `get_quote` (returns a price range + source for the job) and `book_slot` (returns and holds an open time). The plugin's **description text matters as much as the code** — it must say clearly what the plugin is for, which trade and area it covers, and what it sends back, so an agent knows exactly when to call it.
4. **Connect in developer mode and test.** Add it to your own account before anyone else can use it. Test the messy way people actually ask ("my ac is blowing warm air", "how much to fix an ac in phoenix", "can someone come out tomorrow") — all should land at the same quote and booking. Also test a job NOT in the table, and a booking attempt.
5. **Expand.** One new job or one new city at a time — each is just new rows in the table.

Full build prompt in `references/prompts.md`.

## Output Contract

- `price-table.csv` — job, size/type, low, high, source, city
- `plugin-spec.md` — the two actions, request/response schemas, and the agent-facing descriptions
- `test-matrix.md` — messy phrasings tried, results, fixes

## Operating Rules

1. **Never return a price that isn't in the table.** Job not in the table → return no price and offer a visit instead.
2. **Booking slots must be real.** They come from the calendar/booking tool of a business that agreed to take the jobs — never fabricated.
3. **Description-first.** Write the agent-facing description before the code; re-test with messy phrasings after every change.
4. **If the platform's plugin-calling docs are unclear, say so** instead of guessing how agents invoke plugins.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.

## Worked example

Example request: "Use the Agent Plugin Builder skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
