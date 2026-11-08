# Discussion Prompt Drafter

Draft a discussion prompt from a supplied topic. Draft only.

## Category
- Community — Engagement
- Tool kind: `template`

## Tool
- `discussion_prompt_drafter` — Draft a discussion prompt from a supplied topic. Draft only.

## Inputs
```json
{
  "type": "object",
  "properties": {
    "facts": {
      "type": "object",
      "description": "Supplied facts only, keys include: topic_hook, context, question, example_starter, call_to_respond"
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
    "topic_hook": "[supplied: topic hook]",
    "context": "[supplied: context]",
    "question": "[supplied: question]"
  }
}
```

## Outputs
- `plugin` and `tool` — identifiers
- `kind` — `template`
- `result` — the template result, built only from the inputs and this plugin's items: topic hook, context, question, example starter, call to respond
- `guardrails` — present on every result

## Guardrails
- No fabrication: use supplied facts only, mark anything missing as `[missing: ...]`
- Drafts only where the tool drafts — human approval required, no auto-send, no auto-post, no auto-remove
- No real people, client names or metrics in examples — fictional sample data only

## Licence
- MIT — Lionel Sim, Founder The AI Capitol + OpenBuilder (8,000+ builders, 80+ events, ~15,000 signups), Singapore
