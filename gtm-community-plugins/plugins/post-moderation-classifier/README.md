# Post Moderation Classifier

Classify a community post for moderation routing. Flags only, never auto-removes.

## Category
- Community — Moderation & Safety
- Tool kind: `classify`

## Tool
- `post_moderation_classifier` — Classify a community post for moderation routing. Flags only, never auto-removes.

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
  "text": "This is about welcome and needs review."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `classify`
- `result` — the classify result, built only from the inputs and this plugin's items: welcome, self promotion, spam, abuse, off topic, needs help
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
