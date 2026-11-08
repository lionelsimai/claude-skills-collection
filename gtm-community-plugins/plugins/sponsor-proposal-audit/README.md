# Sponsor Proposal Audit

Audit a sponsor proposal for missing commercial elements. Audience numbers must be supplied, never invented.

## Category
- GTM — Sponsors & Partners
- Tool kind: `audit`

## Tool
- `sponsor_proposal_audit` — Audit a sponsor proposal for missing commercial elements. Audience numbers must be supplied, never invented.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

## Example call
```json
{
  "text": "audience evidence deliverables pricing are covered in this document."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `audit`
- `result` — the audit result, built only from the inputs and this plugin's items: audience evidence, deliverables, pricing, dates, terms, call to action
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
