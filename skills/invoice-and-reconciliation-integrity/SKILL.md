---
name: invoice-and-reconciliation-integrity
description: "Prevent invoice and reconciliation errors: never reuse invoice numbers, count every amount once, net refunds, and tie totals to printed statement totals. Use when the user prepares invoices, reconciles accounts, or checks bookkeeping totals. Complements general bookkeeping skills."
category: Finance
license: MIT
version: 1.0.0
---

# Invoice and Reconciliation Integrity

This skill merges two integrity amendments for bookkeeping work. It complements general bookkeeping and invoicing skills: apply it on top of them whenever invoices are issued or accounts are reconciled.

## Part 1 — Invoice integrity

# Invoice Version and Render Integrity

This amendment adds to Bookkeeping and Invoicing when you create or revise an invoice as a PDF or as a draft in a mail or accounting app. The base skill still governs reconciliation, amounts and collection.

## Give each final invoice one number

- Assign a fresh invoice number whenever the total, the scope, the recipient or the currency changes. Never reuse a number that an earlier draft or sent invoice already carries with different content.

- Before you create a combined invoice, list every line that an earlier invoice already covers. Show that overlap to the user before anything is sent, because sending both versions bills the same work twice.

- Mark every superseded draft as superseded in its file name or subject line, and tell the user plainly when a superseded draft still exists somewhere you cannot delete. Never leave a superseded draft looking ready to send without naming that risk.

- Read the finished invoice back to yourself before you call it ready. Check the number, the total, the currency, the lines covered, the recipient and whether payment terms appear or are absent, exactly as the user asked.

## Verify fixes in the rendered page

- After any edit to an invoice PDF, inspect the rendered page itself before you say the edit is done. Extracted text can confirm wording, but it cannot show table rules, alignment or spacing.

- Scan the rendered page for the exact thing the user asked you to change, such as a separator line between rows, a removed terms block or a shifted column. Claim the fix only when the rendered page shows it.

- When a first fix does not hold, remove the whole class of the problem rather than nudging one instance, then scan the rendered page again. Say what the scan showed, not only that you edited the source.

- State clearly when you cannot render or inspect the page. An unverified edit is a draft, not a finished invoice.

## When to use

Use this skill when the task matches its description above and you need a repeatable, checked workflow rather than an improvised answer.

## Guardrails and quality checks

- Never fabricate facts, numbers, clients or results. Use only sources the user provides or verifies.
- Keep drafts as drafts until a human approves any external send, payment or commitment.
- Check the final output against the workflow above before delivering it, and state anything you could not verify.

## Output format and example

Deliver the result in the structure the workflow defines. Example request: "Use the Invoice and Reconciliation Integrity skill for my situation: [describe the business, audience and goal]." Example output: a completed, checked deliverable following every step above, with open questions listed at the end rather than guessed.
