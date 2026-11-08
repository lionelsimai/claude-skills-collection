# Case Study Audit

Audit a case study for permission and evidence elements. Results must be supplied.

## Category
- GTM — Content & Thought Leadership
- Tool kind: `audit`

## Tool
- `case_study_audit` — Audit a case study for permission and evidence elements. Results must be supplied.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string"
    }
  },
  "required": [
    "text"
  ]
}
```

## Example call
```json
{
  "text": "client permission problem approach are covered in this document."
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `audit`
- `result` — the audit result, built only from the inputs and this plugin's items: client permission, problem, approach, measured result, quote, dates
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
