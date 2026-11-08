# New Member Intro Classifier

Classify a member introduction by member type for routing to relevant channels.

## Category
- Community — Member Onboarding
- Tool kind: `classify`

## Tool
- `new_member_intro_classifier` — Classify a member introduction by member type for routing to relevant channels.

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
  "text": "This is about builder and needs review."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `classify`
- `result` — the classify result, built only from the inputs and this plugin's items: builder, founder, operator, student, job seeker, investor, other
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
