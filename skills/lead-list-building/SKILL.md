---
name: lead-list-building
description: "Build and clean a lead list from allowed sources only. Use when the user asks to build a lead list, clean or dedupe leads, apply a suppression list, or says 'lead list', 'prospect list', or 'clean my leads'."
category: Sales & Marketing
license: MIT
version: 1.0.0
---

# Lead List Building

## Build from allowed sources only

- Build the list from sources the user has a right to contact, such as their own event registrations, inbound enquiries, a CRM export, or a licensed data provider.

- Never scrape a source the user has no right to use, and never buy a list of unknown origin.

- Record the source of every lead in its own column, so any lead can be traced back later.

## Clean the list

- Dedupe by email address. Keep the most complete record and report how many duplicates were dropped.

- Drop invalid email addresses and report them. Never guess a corrected address.

- Apply the suppression list before anything else runs. A suppressed contact never re-enters a campaign by accident.

- Keep only the fields the campaign needs: name, email, title, company, region, size, industry, source and signal.

## Enrich with signals

- Add one true and checkable personal signal per lead, such as a launch, a funding round, a senior hire or a new office.

- Mark leads with no signal as not ready. They go back to research, not into a generic blast.

## Present the result

- Return the clean list, the counts at each cleaning step, and the share of leads that carry a usable signal.

## When to use

Use this skill when the task matches its description above and you need a repeatable, checked workflow rather than an improvised answer.

## Guardrails and quality checks

- Never fabricate facts, numbers, clients or results. Use only sources the user provides or verifies.
- Keep drafts as drafts until a human approves any external send, payment or commitment.
- Check the final output against the workflow above before delivering it, and state anything you could not verify.

## Output format and example

Deliver the result in the structure the workflow defines. Example request: "Use the Lead List Building skill for my situation: [describe the business, audience and goal]." Example output: a completed, checked deliverable following every step above, with open questions listed at the end rather than guessed.
