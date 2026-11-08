# Proposal Structure Builder

Build a proposal skeleton from supplied scope and pricing only. No invented proof.

## Category
- GTM — Proposals & Pricing
- Tool kind: `template`

## Tool
- `proposal_structure_builder` — Build a proposal skeleton from supplied scope and pricing only. No invented proof.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: problem, outcomes, scope, deliverables, timeline, investment, terms"
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
    "problem": "[supplied: problem]",
    "outcomes": "[supplied: outcomes]",
    "scope": "[supplied: scope]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: problem, outcomes, scope, deliverables, timeline, investment, terms
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
