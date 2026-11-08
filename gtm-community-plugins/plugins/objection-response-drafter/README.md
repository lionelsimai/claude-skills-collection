# Objection Response Drafter

Draft an objection reply from supplied evidence only. Draft only, human approval required.

## Category
- GTM — Reply & Meeting
- Tool kind: `template`

## Tool
- `objection_response_drafter` — Draft an objection reply from supplied evidence only. Draft only, human approval required.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: acknowledge_objection, supplied_evidence, reframe, low-risk_next_step"
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
    "acknowledge_objection": "[supplied: acknowledge objection]",
    "supplied_evidence": "[supplied: supplied evidence]",
    "reframe": "[supplied: reframe]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: acknowledge objection, supplied evidence, reframe, low-risk next step
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
