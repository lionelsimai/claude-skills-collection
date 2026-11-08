# Segment Learning Logger

Log a segment learning in a fixed format from supplied results.

## Category
- GTM — Analytics & Learning
- Tool kind: `template`

## Tool
- `segment_learning_logger` — Log a segment learning in a fixed format from supplied results.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: segment, result, evidence, decision_scale_or_pause, next_test"
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
    "segment": "[supplied: segment]",
    "result": "[supplied: result]",
    "evidence": "[supplied: evidence]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: segment, result, evidence, decision scale or pause, next test
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
