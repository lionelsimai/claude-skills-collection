---
name: whatsapp-ai-agent
description: "Build and sell WhatsApp AI sales agents for SMEs: instant replies, qualification, booking and follow-up. Use when the user mentions a WhatsApp chatbot, WhatsApp AI agent, or WhatsApp sales automation."
category: AI & Automation
license: MIT
version: 1.0.0
---

# WhatsApp AI Agent

## Purpose

Turn a business's WhatsApp into a 24/7 sales agent: answers enquiries in under a minute, qualifies leads, books appointments, follows up quotes, reactivates past customers. In markets like Singapore, WhatsApp IS the sales channel — this is the highest-leverage agent you can sell to an SME.

## Workflow

1. **Infrastructure first.** The WhatsApp Business App is fine for solo operators. Any business handling 20+ enquiries/day needs the WhatsApp Business API: multi-agent inbox, templates, broadcasts, the verified tick. Route via a BSP (Wati, Interakt, 360dialog, or a white-label platform) — never hack the app with unofficial bridges; they get numbers banned.
2. **Map the conversation.** Enquiry → qualify (budget, timeline, need) → answer from the business's real info (price list, catalogue, availability) → book/quote → human handoff for the close. Plus three always-on sequences: quote follow-up, abandoned-enquiry nudge, past-customer reactivation broadcast.
3. **Train on their truth.** Feed the agent the real price list, service list, hours, and policies. Anything not in the knowledge base → "let me check with the team" — never a guess.
4. **Sell the reply speed.** The pitch is one line: every enquiry answered in under a minute, 24/7, no lead waits till morning. Demo it live on their own number.
5. **Pricing.** Setup fee + monthly retainer. Reference economics: white-label operators charge ~$199/mo per client against ~$30/mo platform cost; premium builds command $1,000+ setup. Retainer covers prompt tuning, the broadcast calendar, and monthly conversation review.
6. **Compliance.** Consent before any marketing message; easy opt-out in every broadcast ("Reply STOP to unsubscribe"); never reuse a number given for billing to send promos without fresh consent.

Full operator prompts (conversation map, knowledge-base template, broadcast calendar, demo script) in `references/prompts.md`.

## Output Contract

- `conversation-map.md` — flows: enquiry, qualification, booking, follow-up, reactivation, handoff
- `knowledge-base.md` — the business's real info, in the agent's source format
- `broadcast-calendar.md` — monthly retention/reactivation messages
- `proposal.md` — speed-to-lead ROI framing and pricing

## Operating Rules

1. Be transparent it's an automated assistant; always offer a human escape hatch.
2. Approval-first on anything involving money, discounts, or promises made to customers.
3. Official API only. No grey-area bridges.
4. Review real conversations weekly in month one; every correction becomes a knowledge-base update.
5. Retention beats acquisition: the reactivation sequence (past customers, timed to when they're happiest) usually outperforms new-lead spend.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.

## Worked example

Example request: "Use the WhatsApp AI Agent skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
