---
name: ai-workflow-builder
description: |
  Design AI automation workflows with clear inputs, outputs, tools, and implementation steps.
  
  TRIGGERS - Use this skill when:
  - User wants to design an AI automation workflow
  - User mentions automating a business process with AI
  - User wants to map out an AI-powered system
  - User asks how to automate something using AI tools
  - User mentions n8n, Make, Zapier, or any automation platform
---

# AI Workflow Builder

## Overview

Designs complete AI automation workflows from business process to implementation plan. Maps out triggers, steps, AI components, integrations, and expected outcomes.

## Workflow

### Step 1: Understand the Process

Ask the user:
1. **What process** do you want to automate?
2. **Current state**: How is it done manually today?
3. **Volume**: How often does this happen? (daily, weekly, per client)
4. **Time spent**: How long does the manual process take?
5. **Tools involved**: What software/platforms are already in use?
6. **Desired outcome**: What does "automated" look like?

### Step 2: Map the Current Workflow

Document the as-is process:
```
TRIGGER → Step 1 → Step 2 → ... → OUTPUT
```

Identify:
- **Manual steps** (candidate for automation)
- **Decision points** (needs AI judgment or rules)
- **Data sources** (where information comes from)
- **Handoff points** (where humans need to review)
- **Bottlenecks** (where delays happen)

### Step 3: Design the AI Workflow

For each step, determine:

| Step | Manual Task | AI Solution | Tool/Platform | Human Review? |
|------|------------|-------------|---------------|--------------|
| 1 | ... | ... | ... | Yes/No |
| 2 | ... | ... | ... | Yes/No |

**AI Component Selection Guide:**

| Task Type | Recommended AI Approach |
|-----------|----------------------|
| Text generation | LLM (Claude, GPT) |
| Data extraction | LLM with structured output |
| Classification | LLM or fine-tuned classifier |
| Image processing | Vision AI (Claude, GPT-4V) |
| Voice/transcription | Whisper, Deepgram |
| Data lookup | RAG or API integration |
| Decision making | Rule engine + LLM fallback |
| Scheduling | Calendar API + automation |

### Step 4: Select Automation Platform

| Platform | Best For | Complexity |
|----------|----------|-----------|
| **Zapier** | Simple 2-5 step workflows | Low |
| **Make (Integromat)** | Visual complex workflows | Medium |
| **n8n** | Self-hosted, developer-friendly | Medium-High |
| **Custom code** | Full control, unique logic | High |
| **LangChain/CrewAI** | Multi-agent AI workflows | High |

### Step 5: Build the Architecture

Create the workflow diagram:

```
[TRIGGER]
    ↓
[STEP 1: Input Processing]
    → Tool: [platform/API]
    → AI: [model + prompt purpose]
    → Output: [what this step produces]
    ↓
[STEP 2: AI Processing]
    → Tool: [platform/API]
    → AI: [model + prompt purpose]
    → Output: [what this step produces]
    ↓
[DECISION: Human Review Needed?]
    → YES → [Notify human via Slack/email] → Wait for approval → Continue
    → NO → Continue
    ↓
[STEP 3: Action/Output]
    → Tool: [destination platform]
    → Action: [what happens]
    ↓
[COMPLETE: Log result]
```

### Step 6: Write the Prompts

For each AI step, create:
1. **System prompt** — role and context
2. **Input template** — dynamic variables from previous steps
3. **Output format** — structured JSON or specific format
4. **Fallback** — what happens if AI fails

### Step 7: Implementation Plan

Provide:
1. **Phase 1** (Week 1): Set up accounts, connect tools
2. **Phase 2** (Week 2): Build core automation flow
3. **Phase 3** (Week 3): Add AI components and test
4. **Phase 4** (Week 4): Monitor, refine, go live

## Output Format

```markdown
# AI Workflow: [Process Name]

## Summary
- **Process**: [what's being automated]
- **Time saved**: [X hours/week]
- **Tools**: [platforms used]
- **AI models**: [which AI and for what]

## Current vs Automated

| | Manual | Automated |
|--|--------|-----------|
| Time per task | Xm | Xm |
| Tasks/day | X | X |
| Error rate | X% | X% |
| Monthly cost | $X | $X |

## Workflow Architecture

[Visual flow diagram using text/arrows]

## Step-by-Step Breakdown

### Step 1: [Name]
- **Trigger**: [what kicks this off]
- **Input**: [data coming in]
- **Process**: [what happens]
- **AI prompt**: [if applicable]
- **Output**: [what's produced]
- **Tool**: [platform/integration]

[Repeat for each step]

## Prompts & Templates

### [AI Step Name] — System Prompt
```
[Full prompt text]
```

### [AI Step Name] — Input Template
```
[Template with {{variables}}]
```

## Implementation Plan
[Phased rollout]

## Monitoring & Maintenance
- KPIs to track
- Common failure points
- Escalation triggers
```

## Quality Checklist

- [ ] Every manual step has an automated equivalent
- [ ] Human review points identified for critical decisions
- [ ] AI prompts are specific with structured outputs
- [ ] Fallback/error handling defined for each step
- [ ] ROI estimate included (time/money saved)
- [ ] Implementation is phased and realistic
