# Reply Intent Classifier

Classify an email reply by intent so hot replies move first.

## Category
- GTM — Reply & Meeting
- Tool kind: `classify`

## Tool
- `reply_intent_classifier` — Classify an email reply by intent so hot replies move first.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

## Example call
```json
{
  "text": "This is about interested and needs review."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `classify`
- `result` — the classify result, built only from the inputs and this plugin's items: interested, meeting request, objection, not now, not relevant, unsubscribe, pricing question
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
