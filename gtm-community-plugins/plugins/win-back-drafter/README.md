# Win-back Drafter

Draft a win-back message from supplied updates. Draft only.

## Category
- Community — Retention & Churn
- Tool kind: `template`

## Tool
- `win_back_drafter` — Draft a win-back message from supplied updates. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: acknowledge_absence, what_is_new_supplied_by_user, personal_invite, no_pressure_close"
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
    "acknowledge_absence": "[supplied: acknowledge absence]",
    "what_is_new_supplied_by_user": "[supplied: what is new supplied by user]",
    "personal_invite": "[supplied: personal invite]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: acknowledge absence, what is new supplied by user, personal invite, no pressure close
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
