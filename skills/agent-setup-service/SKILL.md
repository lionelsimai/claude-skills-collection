---
name: agent-setup-service
description: "Run an always-on AI agent setup service for owner-led businesses, with rulebooks and a client setup pack. Use when the user asks to set up AI agents for a business, chase invoices with AI, or auto-reply to leads."
category: AI & Automation
license: MIT
version: 1.0.0
---

# Dots Setup Service

## Purpose

Deliver a done-for-you always-on AI agent setup for owner-led service businesses (trades: aircon servicing, plumbing, electrical, cleaning, landscaping). Charge a setup fee once, then a monthly retainer to keep it tuned. The agent's standing jobs: chase overdue invoices, reply to new leads fast, follow up on quotes.

## Workflow

1. **Mock business rehearsal.** Before touching a real client, build a mock business in the target trade + city: price sheet from public sources, business profile, mock invoices and customer emails. Run the invoice and lead workflows against the mocks first.
2. **Price sheet.** The base artifact — every price the agent ever quotes traces to it. Real local ranges with a source per row. Label referral/lead-gen sites as such; when sources disagree, show both ranges and flag it. If no real price exists for a job, leave it off — never estimate.
3. **Invoice-chase rulebook.** Staged: friendly reminder → firmer reminder → flag for the owner's phone call. Holds (never chase): disputed, marked paid, promised payment date not yet due. Promise date passed → chase again and mention the missed promise. Every reminder asks for the payment date in case they already paid. Anything not matching a rule → hold and explain why.
4. **Lead-reply rules.** Under 80 words. Job on the price sheet → one price range + two available times. Not on sheet → offer a visit, never a guessed price. Vague enquiry → one clarifying question. Urgent (leak etc.) → safe first steps before anything else. No disclaimers. Never redirect to another business. Ignore spam/sales pitches. Unsure → draft and flag for the owner.
5. **Sell it with a demo recording.** Order the recording the way owners care: invoices first (money already owed), then lead replies, then price sheet. Send by DM, or on a postcard with a QR code to the video.
6. **Automate outreach.** Pull every business of one trade in one city (e.g. from Google Maps). Audit each site: try to find a price and the next open appointment the way a customer would; log exactly where it gets stuck (form, 404, bot check). Build a demo page per business (name/logo, what the audit found, prerecorded demo video, example replies for their real services, checkout link). Mail a postcard (site + audit result on front, one line + QR on back) via a print API. Show the user the first 10 before anything is mailed.
7. **Client setup pack.** From the client's onboarding form answers, build a shared folder: business profile doc (services, prices, hours, area), invoice rulebook, lead-reply rulebook, custom rules written word-for-word, and one "paste this first" message that tells the client's agent to read the folder and start its standing jobs. Missing/unclear answer → list it, never fill it in.

Full operator prompts for each stage live in `references/prompts.md`.

## Output Contract

- `price-sheet.md` — jobs, low/high ranges, source per row, referral-site labels
- `business-profile.md` — services, what the business does/doesn't do, emergency policy, hours, area
- `invoice-rulebook.md` + `lead-reply-rulebook.md` — the staged rules
- `custom-rules.md` — approval rules word-for-word
- `outreach/` — audit sheet, demo pages, postcard copy
- `setup-pack/` — the client's folder contents, ready to share

## Operating Rules

1. **Approval-first defaults.** Every outbound message, payment action, or record change stays behind owner approval until the owner explicitly loosens it. Start: read everything, draft anything, send nothing.
2. **Never send without the user confirming.** Drafts only, unless the user has approved a specific send.
3. **Read-only audits.** Never fill in a form, enter a zip code, or book anything during audits or outreach.
4. **Client accounts are theirs.** The business owner creates their own agent and connects their own accounts (inside their own login); you prepare everything around that step.
5. **Surface the platform cost.** The client also needs their own agent subscription (e.g. ChatGPT Pro at $100/mo for dots) — put this in every proposal, never bury it.
6. **The monthly retainer is real work.** Prices change, services start/stop, tone drifts — review the month's drafts, fix misses, update rules and the price sheet.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.
