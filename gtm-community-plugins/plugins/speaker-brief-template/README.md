# Speaker Brief Template

Render a speaker brief from supplied event facts only.

## Category
- Community — Events
- Tool kind: `template`

## Tool
- `speaker_brief_template` — Render a speaker brief from supplied event facts only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: event_context, audience, talk_slot, format, av_needs, deadline"
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
    "audience": "[supplied: audience]",
    "talk_slot": "[supplied: talk slot]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: event context, audience, talk slot, format, av needs, deadline
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
