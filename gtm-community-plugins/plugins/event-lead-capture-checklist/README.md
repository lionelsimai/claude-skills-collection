# Event Lead Capture Checklist

Check an event lead-capture setup before doors open.

## Category
- GTM — Lead Generation
- Tool kind: `checklist`

## Tool
- `event_lead_capture_checklist` — Check an event lead-capture setup before doors open.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "completed": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Completed items from: consent wording, badge scan process, qualifying question, offer hook, follow-up owner, same-day upload"
    }
  },
  "required": [
    "completed"
  ]
}
```

## Example call
```json
{
  "completed": [
    "consent wording",
    "badge scan process"
  ]
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `checklist`
- `result` — the checklist result, built only from the inputs and this plugin's items: consent wording, badge scan process, qualifying question, offer hook, follow-up owner, same-day upload
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
