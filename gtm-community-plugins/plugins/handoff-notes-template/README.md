# Handoff Notes Template

Render a sales handoff note from supplied facts only.

## Category
- GTM — Pipeline & CRM
- Tool kind: `template`

## Tool
- `handoff_notes_template` — Render a sales handoff note from supplied facts only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: deal_context, key_contacts, commitments_made, risks, immediate_next_step"
    }
  },
  "required": [
    "facts"
  ]
}
```

## Example call
```json
{
  "facts": {
    "deal_context": "[supplied: deal context]",
    "key_contacts": "[supplied: key contacts]",
    "commitments_made": "[supplied: commitments made]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: deal context, key contacts, commitments made, risks, immediate next step
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
