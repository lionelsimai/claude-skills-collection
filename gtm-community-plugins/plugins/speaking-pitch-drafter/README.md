# Speaking Pitch Drafter

Draft a speaking pitch from supplied bio and topic only. Draft only.

## Category
- GTM — Content & Thought Leadership
- Tool kind: `template`

## Tool
- `speaking_pitch_drafter` — Draft a speaking pitch from supplied bio and topic only. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: event_fit, topic, three_takeaways, speaker_bio_supplied_by_user, format"
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
    "event_fit": "[supplied: event fit]",
    "topic": "[supplied: topic]",
    "three_takeaways": "[supplied: three takeaways]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: event fit, topic, three takeaways, speaker bio supplied by user, format
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
