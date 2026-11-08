# No-show Recovery Drafter

Draft a no-show recovery message from supplied facts. Draft only.

## Category
- GTM — Reply & Meeting
- Tool kind: `template`

## Tool
- `no_show_recovery_drafter` — Draft a no-show recovery message from supplied facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: grace_opening, no_blame, two_new_options, value_recap"
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
    "grace_opening": "[supplied: grace opening]",
    "no_blame": "[supplied: no blame]",
    "two_new_options": "[supplied: two new options]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: grace opening, no blame, two new options, value recap
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
