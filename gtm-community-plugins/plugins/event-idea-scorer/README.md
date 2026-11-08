# Event Idea Scorer

Score an event idea before committing a venue.

## Category
- Community — Events
- Tool kind: `score`

## Tool
- `event_idea_scorer` — Score an event idea before committing a venue.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "metrics": {
      "type": "object",
      "description": "Scores 0-100 keyed by: member_demand, speaker_availability, cost, sponsor_fit, format_novelty"
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
    "member_demand": 70,
    "speaker_availability": 70,
    "cost": 70,
    "sponsor_fit": 70,
    "format_novelty": 70
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `score`
- `result` — the score result, built only from the inputs and this plugin's items: member demand, speaker availability, cost, sponsor fit, format novelty
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
