# Feedback Response Drafter

Draft a response to feedback from supplied actions. Draft only.

## Category
- Community — Feedback & NPS
- Tool kind: `template`

## Tool
- `feedback_response_drafter` — Draft a response to feedback from supplied actions. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: thank_them, specific_point, what_will_change_supplied_by_user, timeline"
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
    "thank_them": "[supplied: thank them]",
    "specific_point": "[supplied: specific point]",
    "what_will_change_supplied_by_user": "[supplied: what will change supplied by user]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: thank them, specific point, what will change supplied by user, timeline
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
