# Buddy Match Scorer

Score a buddy pairing for a new member from supplied attributes.

## Category
- Community — Member Onboarding
- Tool kind: `score`

## Tool
- `buddy_match_scorer` — Score a buddy pairing for a new member from supplied attributes.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: shared_interests, location, experience_gap_fit, availability, language"
    }
  },
  "required": [
    "metrics"
  ]
}
```

## Example call
```json
{
  "metrics": {
    "shared_interests": 70,
    "location": 70,
    "experience_gap_fit": 70,
    "availability": 70,
    "language": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: shared interests, location, experience gap fit, availability, language
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
