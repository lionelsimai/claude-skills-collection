# Auto-GTM Agent

## Run the pipeline in order

- Start with the config file for the business. Read the sender, offer ladder, banned words and allowed proof list before doing anything else.

- Validate the config first with `python3 -m autogtm validate` using the CLI in `src/`. Fix every issue it reports except a missing booking link, which you flag to the user and treat as an escalation blocker.

- Learn the offer only from sources the user approves, such as their presentation deck or pricing page. Never invent proof points, attendance numbers or client names, and only use claims on the config allow list.

## Score and draft

- Import leads from a CSV the user supplies or a source they name. Dedupe by email, drop invalid and suppressed addresses, and report what was dropped and why.

- Score every lead with `python3 -m autogtm score --leads <file>`. Work tier A first, then tier B, and skip tier C unless the user says otherwise.

- Research one true and checkable personal signal per lead before drafting, such as a launch, a hire, a funding round or an office opening. Put it in the signal column.

- Draft with `python3 -m autogtm draft --leads <file> --out drafts.json`. Accept that a lead with no signal is blocked, and research it instead of sending a generic email.

- Show the user the first batch of drafts and wait for approval before any sending step. Every draft carries the status draft_needs_approval for this reason.

## Handle replies and learn

- Triage every reply with `python3 -m autogtm triage --text "<reply>"`. Send the booking link only for a plain hot reply when a booking link is set in the config.

- Forward pricing, contract, legal, procurement and security replies to the user with a draft reply. Never auto answer them.

- Suppress any contact who asks to unsubscribe or says they are not interested. Never follow up with them.

- Review campaign results with `python3 -m autogtm learn --results <file>`. Scale segments under the scale cost per hot lead, pause segments over the pause cost after the minimum send volume, and report the verdict with the numbers behind it.

## Guardrails

- Never send from the user primary domain. A sending step, when the user adds one, uses a separate warmed domain and an explicit approval flag.

- Keep one segment and one offer per campaign. Do not mix offers in a single email.

- Keep daily volume and spend inside the cap in the config. Stop and report when the cap is hit.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with the custom connector setup skill, or build a custom connector.
