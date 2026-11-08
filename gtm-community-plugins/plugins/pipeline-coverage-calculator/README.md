# Pipeline Coverage Calculator

Calculate pipeline coverage from supplied pipeline and target.

## Category
- GTM — Pipeline & CRM
- Tool kind: `analyze`

## Tool
- `pipeline_coverage_calculator` — Calculate pipeline coverage from supplied pipeline and target.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "counts": {
      "type": "object"
    },
    "amounts": {
      "type": "object"
    },
    "series": {
      "type": "array",
      "items": {
        "type": "number"
      }
    }
  },
  "required": []
}
```

## Example call
```json
{
  "counts": {
    "open_pipeline": 100,
    "target": 90,
    "coverage_ratio": 80,
    "weighted_pipeline": 70,
    "gap": 60
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `analyze`
- `result` — the analyze result, built only from the inputs and this plugin's items: open pipeline, target, coverage ratio, weighted pipeline, gap
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
