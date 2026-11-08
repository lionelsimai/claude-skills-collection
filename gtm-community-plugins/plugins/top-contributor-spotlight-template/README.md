# Top Contributor Spotlight Template

Render a contributor spotlight from supplied facts only.

## Category
- Community — Engagement
- Tool kind: `template`

## Tool
- `top_contributor_spotlight_template` — Render a contributor spotlight from supplied facts only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: member_name_supplied_by_user, contribution, quote_supplied_by_user, thank_you"
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
    "member_name_supplied_by_user": "[supplied: member name supplied by user]",
    "contribution": "[supplied: contribution]",
    "quote_supplied_by_user": "[supplied: quote supplied by user]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: member name supplied by user, contribution, quote supplied by user, thank you
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
