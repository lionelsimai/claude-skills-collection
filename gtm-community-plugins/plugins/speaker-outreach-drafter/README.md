# Speaker Outreach Drafter

Draft speaker outreach from supplied event facts. Draft only.

## Category
- Community — Speakers & Sponsors
- Tool kind: `template`

## Tool
- `speaker_outreach_drafter` — Draft speaker outreach from supplied event facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: event_context, audience_supplied_by_user, topic_fit, logistics, next_step"
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
    "event_context": "[supplied: event context]",
    "audience_supplied_by_user": "[supplied: audience supplied by user]",
    "topic_fit": "[supplied: topic fit]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: event context, audience supplied by user, topic fit, logistics, next step
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
