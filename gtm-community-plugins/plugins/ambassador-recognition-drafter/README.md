# Ambassador Recognition Drafter

Draft ambassador recognition from supplied facts. Draft only.

## Category
- Community — Ambassadors
- Tool kind: `template`

## Tool
- `ambassador_recognition_drafter` — Draft ambassador recognition from supplied facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: name_supplied_by_user, specific_contribution, impact_supplied_by_user, public_thank_you"
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
    "name_supplied_by_user": "[supplied: name supplied by user]",
    "specific_contribution": "[supplied: specific contribution]",
    "impact_supplied_by_user": "[supplied: impact supplied by user]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: name supplied by user, specific contribution, impact supplied by user, public thank you
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
