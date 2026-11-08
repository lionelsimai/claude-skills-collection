# Post-event Follow-up Drafter

Draft post-event follow-up from supplied highlights. Draft only.

## Category
- Community — Events
- Tool kind: `template`

## Tool
- `post_event_follow_up_drafter` — Draft post-event follow-up from supplied highlights. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: thank_you, highlight_supplied_by_user, recording_link, feedback_ask, next_event"
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
    "thank_you": "[supplied: thank you]",
    "highlight_supplied_by_user": "[supplied: highlight supplied by user]",
    "recording_link": "[supplied: recording link]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: thank you, highlight supplied by user, recording link, feedback ask, next event
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
