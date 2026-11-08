# Panel Composition Audit

Audit a panel line-up for balance elements.

## Category
- Community — Speakers & Sponsors
- Tool kind: `audit`

## Tool
- `panel_composition_audit` — Audit a panel line-up for balance elements.

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
  "text": "topic balance seniority mix company mix are covered in this document."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `audit`
- `result` — the audit result, built only from the inputs and this plugin's items: topic balance, seniority mix, company mix, perspective mix, moderator assigned
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
