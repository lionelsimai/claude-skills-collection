---
name: voice-ai-receptionist
description: "Sell and deliver AI voice receptionists: missed-call recovery, booking and lead qualification. Use when the user mentions an AI receptionist, voice agent for a business, missed-call recovery, or AI phone agent."
category: AI & Automation
license: MIT
version: 1.0.0
---

# Voice AI Receptionist

## Purpose

Sell a 24/7 AI phone agent to businesses that lose money on missed calls — clinics, dental, salons, aircon/HVAC servicing, plumbing, law firms, real estate. You are not selling AI. You are selling missed-call recovery as revenue infrastructure.

## Workflow

1. **Pick one industry.** Dental, med spa, salon, aircon servicing, vet, chiropractic — one, not all. Specialists close; generalists starve.
2. **Build one demo deployment** for a fake client in that industry. Record the test calls. This recording is your proof.
3. **Ghost pilot.** For each real target, build a private 60-second demo call using only public info from their website. Generic demos don't sell.
4. **Sell the leak, not the tech.** Discovery: quantify their actual missed-call volume from their phone/CRM data. Pitch relief: "every after-hours call gets answered, qualified, and booked — you wake up to the summary."
5. **Deploy.** Two models: white-label reseller platform ($500–$2,000/mo per client, you handle the relationship) or custom build on Vapi/Retell/Bland ($1,000–$5,000 setup + $300–$800/mo). Voice cost runs ~$0.05–$0.12/minute.
6. **Retainer = operations.** The monthly fee pays for call monitoring, transcript review, script updates, and guardrails — not a one-time bot install. Every missed FAQ from a real call goes into the script the same week.

Full operator prompts (demo script, ghost pilot, discovery, objection handling) in `references/prompts.md`.

## Output Contract

- `call-flows.md` — greeting, qualification, booking, fallback flows for the industry
- `ghost-pilot.md` — per-target demo plan
- `discovery-questions.md` — questions that quantify the missed-call leak
- `proposal.md` — ROI framing (missed calls × average job value), pricing, 30-day cancellation terms

## Operating Rules

1. Never lead with "AI" — lead with the leak and the money.
2. Human fallback on every call flow. "Let me connect you to the team" — no dead ends, ever.
3. Record and transcribe every call; review transcripts weekly in month one.
4. One industry at a time.
5. Check local call-recording consent rules before deploying (e.g. two-party consent jurisdictions).
6. First 3 clients: offer a 7-day free trial with real call data — it outsells any pitch deck.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.

## Worked example

Example request: "Use the Voice AI Receptionist skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
