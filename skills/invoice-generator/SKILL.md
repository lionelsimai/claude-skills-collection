---
name: invoice-generator
description: |
  Create professional invoices for freelancers and service providers.
  TRIGGERS - Use when user wants to create an invoice, billing document, or payment request.
---

# Invoice Generator

## Output Format

```markdown
# INVOICE

**Invoice #**: [INV-0001]
**Date**: [Issue date]
**Due Date**: [Payment due date]

## From
[Your business name]
[Address]
[Email]

## Bill To
[Client name]
[Company]
[Address]

## Services

| Description | Quantity | Rate | Amount |
|------------|---------|------|--------|
| [Service 1] | [qty/hrs] | $[rate] | $[total] |
| [Service 2] | [qty/hrs] | $[rate] | $[total] |

| | |
|--|--|
| **Subtotal** | $[X] |
| **Tax ([X%])** | $[X] |
| **Total Due** | **$[X]** |

## Payment Methods
[Bank transfer / PayPal / Stripe / etc.]

## Notes
[Payment terms, late fees, thank you message]
```
