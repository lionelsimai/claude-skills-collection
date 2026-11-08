# Partner Outreach Drafter

Draft partner outreach from supplied audience facts only. Draft only.

## Category
- GTM — Sponsors & Partners
- Tool kind: `template`

## Tool
- `partner_outreach_drafter` — Draft partner outreach from supplied audience facts only. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: shared_audience, entry_offer, proof_supplied_by_user, meeting_ask"
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
    "shared_audience": "[supplied: shared audience]",
    "entry_offer": "[supplied: entry offer]",
    "proof_supplied_by_user": "[supplied: proof supplied by user]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: shared audience, entry offer, proof supplied by user, meeting ask
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
