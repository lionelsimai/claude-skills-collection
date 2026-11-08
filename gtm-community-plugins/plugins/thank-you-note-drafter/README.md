# Thank-you Note Drafter

Draft a thank-you note from supplied facts. Draft only.

## Category
- Community — Speakers & Sponsors
- Tool kind: `template`

## Tool
- `thank_you_note_drafter` — Draft a thank-you note from supplied facts. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: specific_contribution, audience_impact_supplied_by_user, photo_or_recording_link, future_invite"
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
    "specific_contribution": "[supplied: specific contribution]",
    "audience_impact_supplied_by_user": "[supplied: audience impact supplied by user]",
    "photo_or_recording_link": "[supplied: photo or recording link]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: specific contribution, audience impact supplied by user, photo or recording link, future invite
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
