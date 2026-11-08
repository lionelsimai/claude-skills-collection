# Newsletter Section Builder

Build a newsletter section from supplied facts only. Draft only.

## Category
- GTM — Content & Thought Leadership
- Tool kind: `template`

## Tool
- `newsletter_section_builder` — Build a newsletter section from supplied facts only. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: headline, what_happened, why_it_matters, what_to_do, link"
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
    "headline": "[supplied: headline]",
    "what_happened": "[supplied: what happened]",
    "why_it_matters": "[supplied: why it matters]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: headline, what happened, why it matters, what to do, link
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
