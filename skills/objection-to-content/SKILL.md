---
name: objection-to-content
description: "Turn sales objections into content ideas and drafts that answer them honestly. Use when the user shares an objection, pushback or 'too expensive' style reply and wants content from it."
category: Content Creation
license: MIT
version: 1.0.0
---

# Objection-to-Content Agent

Turn prospect objections into a middle-of-funnel (MOF) content plan using
SooWei Goh's framework: objections are the best ideas — name the limiting
belief under each objection, and create content that breaks the belief
first (neutral state) before any offer content.

## When to use

Trigger on: 'objection agent', 'objections into content', 'turn objections
into posts', 'MOF content from objections', 'belief-breaking content', or
when the user hands over a list of objections from calls/DMs/emails.

## How

Repo: . (objection_agent.py, README.md, tests).

1. Collect objections into a .txt (one per line) or .csv (`objection`
   column). Sources: his own call notes, DM/email replies, the Auto-GTM
   Agent's reply triage output.
2. Run: `python3 objection_agent.py <input> --proof <proof.txt> --out plan.md`
   The proof file is allow-listed, verified proof points only, one per
   line. Without it, briefs are marked PROOF NEEDED — never invent proof,
   numbers, testimonials or client results.
3. Present the plan to the user: theme, limiting belief, reframe, briefs.
4. Drafting the actual posts/carousels/videos happens in chat, only for
   briefs the user approves. Nothing is posted or sent by the agent.

## Rules

- Eight belief themes: price, timing, trust, diy, approval, capacity,
  competitor, need. Unmapped objections are flagged UNCLASSIFIED for a
  human read — do not force them into a theme.
- MOF briefs carry a soft CTA only (invite a reply/question). No pitching
  in belief-breaking content.
- Paste-ready copy for the user follows his format rules (plain text, no
  markdown decoration).

## Guardrails and quality checks

- Never fabricate facts, numbers, clients or results. Use only sources the user provides or verifies.
- Keep drafts as drafts until a human approves any external send, payment or commitment.
- Check the final output against the workflow above before delivering it, and state anything you could not verify.

## Worked example

Example request: "Use the Objection to Content skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
