# LinkedIn Touch Drafter

Draft a LinkedIn touch from a supplied shared context only. Draft only.

## Category
- GTM — Outreach & Sequences
- Tool kind: `template`

## Tool
- `linkedin_touch_drafter` — Draft a LinkedIn touch from a supplied shared context only. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: shared_context, specific_observation, useful_resource, open_question"
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
    "shared_context": "[supplied: shared context]",
    "specific_observation": "[supplied: specific observation]",
    "useful_resource": "[supplied: useful resource]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: shared context, specific observation, useful resource, open question
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
