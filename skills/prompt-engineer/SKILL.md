---
name: prompt-engineer
description: |
  Create optimized, production-ready prompts for any AI model or use case.
  
  TRIGGERS - Use this skill when:
  - User wants to create or improve AI prompts
  - User mentions prompt engineering, prompt writing, or system prompts
  - User wants to optimize prompts for better AI outputs
  - User asks for help with ChatGPT, Claude, or other AI model prompts
---

# Prompt Engineer

## Overview

Creates structured, optimized prompts that get consistent, high-quality outputs from any AI model. Covers system prompts, user prompts, chain-of-thought, few-shot examples, and output formatting.

## Workflow

### Step 1: Understand the Use Case

Ask the user:
1. **What should the AI do?** (specific task)
2. **What model?** (Claude, GPT-4, Llama, etc.)
3. **Where will it run?** (chatbot, automation, API, manual use)
4. **What does good output look like?** (example if available)
5. **What does bad output look like?** (common failures to avoid)

### Step 2: Choose the Prompt Architecture

| Architecture | When to Use |
|-------------|-------------|
| **Single prompt** | Simple, one-shot tasks |
| **System + User prompt** | Chatbots, consistent behavior |
| **Chain of thought** | Complex reasoning, analysis |
| **Few-shot** | When format/style must be exact |
| **Multi-step chain** | Complex workflows, agents |

### Step 3: Build the Prompt

**Core Components:**

```
1. ROLE — Who is the AI?
2. CONTEXT — What background does it need?
3. TASK — What exactly should it do?
4. FORMAT — How should output be structured?
5. CONSTRAINTS — What to avoid or limit?
6. EXAMPLES — What does good output look like?
```

**Prompt Template:**

```
You are a [ROLE] with expertise in [DOMAIN].

## Context
[Background information the AI needs to know]

## Task
[Exactly what the AI should do — be specific]

## Input
[What the user/system will provide]
{{variable_name}}

## Output Format
[Exact structure expected]
- Format: [JSON/markdown/plain text]
- Length: [word count or structure]
- Tone: [professional/casual/technical]

## Rules
- [Constraint 1]
- [Constraint 2]
- [What to NEVER do]

## Examples

### Input:
[Example input]

### Expected Output:
[Example output]

### Input:
[Second example — different case]

### Expected Output:
[Second example output]
```

### Step 4: Optimize

Apply these optimization techniques:

1. **Be specific**: "Write 3 bullet points" > "Write some points"
2. **Use positive instructions**: "Include metrics" > "Don't forget metrics"
3. **Add guardrails**: "If unsure, say 'I need more information about X'"
4. **Structure with XML/markdown**: Use headers and tags for clarity
5. **Test edge cases**: What happens with weird input?
6. **Add fallback instructions**: What to do when input is incomplete

### Step 5: Test & Iterate

Provide 3 test inputs:
1. **Happy path** — typical, well-formed input
2. **Edge case** — unusual or minimal input
3. **Adversarial** — tricky input that might break it

## Output Format

```markdown
# Prompt: [Use Case Name]

## Model: [recommended model]
## Architecture: [single/system+user/chain/few-shot]

---

## System Prompt
```
[Full system prompt]
```

## User Prompt Template
```
[User prompt with {{variables}}]
```

## Variables
| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| {{var1}} | string | ... | ... |

## Test Cases

### Test 1: Happy Path
**Input**: [test input]
**Expected behavior**: [what should happen]

### Test 2: Edge Case
**Input**: [edge case input]
**Expected behavior**: [what should happen]

### Test 3: Adversarial
**Input**: [tricky input]
**Expected behavior**: [what should happen]

## Integration Notes
- [How to use in Zapier/Make/n8n]
- [API call example if applicable]
- [Token/cost estimate per call]
```

## Quality Checklist

- [ ] Role is specific (not generic "helpful assistant")
- [ ] Task is unambiguous (one interpretation only)
- [ ] Output format is explicitly defined
- [ ] At least 2 examples included
- [ ] Edge cases handled with fallback instructions
- [ ] Variables are clearly marked with {{brackets}}
- [ ] Tested with 3 different inputs
