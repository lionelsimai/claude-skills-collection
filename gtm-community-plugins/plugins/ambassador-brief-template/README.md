# Ambassador Brief Template

Render an ambassador brief from supplied campaign facts.

## Category
- Community — Ambassadors
- Tool kind: `template`

## Tool
- `ambassador_brief_template` — Render an ambassador brief from supplied campaign facts.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: campaign_goal, key_message_supplied_by_user, assets, do_and_do_not, deadline"
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
    "campaign_goal": "[supplied: campaign goal]",
    "key_message_supplied_by_user": "[supplied: key message supplied by user]",
    "assets": "[supplied: assets]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: campaign goal, key message supplied by user, assets, do and do not, deadline
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
