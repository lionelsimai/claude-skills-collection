# TAM SAM SOM Calculator

Calculate TAM, SAM and SOM from supplied account counts and values only.

## Category
- GTM — ICP & Market Research
- Tool kind: `analyze`

## Tool
- `tam_sam_som_calculator` — Calculate TAM, SAM and SOM from supplied account counts and values only.

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
    "total_accounts": 100,
    "serviceable_accounts": 90,
    "obtainable_accounts": 80,
    "average_contract_value": 70,
    "win_rate": 60
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `analyze`
- `result` — the analyze result, built only from the inputs and this plugin's items: total accounts, serviceable accounts, obtainable accounts, average contract value, win rate
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
