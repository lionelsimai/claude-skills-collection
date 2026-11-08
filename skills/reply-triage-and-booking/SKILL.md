---
name: reply-triage-and-booking
description: "Classify outreach replies and act safely by class, escalating pricing and contract replies to a human. Use when the user asks to triage replies, handle responses, or says 'reply triage', 'classify replies', or 'book meetings from replies'."
category: Sales & Marketing
license: MIT
version: 1.0.0
---

# Reply Triage and Booking

## Classify every reply first

- Sort each reply into one class: hot, hot but escalate, negative, out of office, or warm and unclear.

- Treat a reply as hot when it moves the deal forward, such as asking for pricing, asking to involve a colleague, or proposing a time.

- Treat out-of-office replies as a timing note. Retry after the return date, never immediately.

## Act by class

- For a plain hot reply, send the booking link from the business config and offer two or three times. If no booking link is set, ask the user for one instead of guessing.

- For any reply that touches pricing, contracts, legal, procurement or security, forward it to the user with a draft reply. Never auto answer it, even when the reply also sounds hot.

- For a negative reply or an unsubscribe, suppress the contact at once and never follow up.

- For a warm and unclear reply, forward it to the user. Do not improvise a pitch in the thread.

## Report the triage

- Return the counts per class and the name of every hot lead, so the user sees the pipeline, not a summary number alone.

## When to use

Use this skill when the task matches its description above and you need a repeatable, checked workflow rather than an improvised answer.

## Guardrails and quality checks

- Never fabricate facts, numbers, clients or results. Use only sources the user provides or verifies.
- Keep drafts as drafts until a human approves any external send, payment or commitment.
- Check the final output against the workflow above before delivering it, and state anything you could not verify.

## Output format and example

Deliver the result in the structure the workflow defines. Example request: "Use the Reply Triage and Booking skill for my situation: [describe the business, audience and goal]." Example output: a completed, checked deliverable following every step above, with open questions listed at the end rather than guessed.
