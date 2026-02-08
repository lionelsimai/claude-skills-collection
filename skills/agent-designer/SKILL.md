---
name: agent-designer
description: |
  Design multi-step AI agent architectures with tools, memory, and orchestration.
  TRIGGERS - Use when user wants to design AI agents, multi-agent systems, or autonomous AI workflows.
---

# AI Agent Designer

## Overview
Designs AI agent architectures — single agents or multi-agent systems — with clear roles, tools, memory, and orchestration patterns.

## Workflow

### Step 1: Define the Agent
1. **Objective**: What should the agent accomplish?
2. **Scope**: What's in and out of bounds?
3. **Tools needed**: What APIs/services should it access?
4. **Autonomy level**: Fully autonomous, human-in-the-loop, or supervised?
5. **Platform**: LangChain, CrewAI, AutoGen, custom, or conceptual?

### Step 2: Choose the Architecture

| Pattern | When to Use |
|---------|-------------|
| **Single agent + tools** | One task, multiple steps |
| **Sequential chain** | Linear workflow, each step feeds the next |
| **Router agent** | Different tasks need different specialists |
| **Parallel agents** | Independent tasks that can run simultaneously |
| **Hierarchical** | Manager delegates to worker agents |
| **Collaborative** | Agents discuss and refine outputs |

### Step 3: Design the System

For each agent:
```markdown
## Agent: [Name]

### Role
[One sentence — what this agent does]

### System Prompt
```
[Full system prompt]
```

### Tools Available
| Tool | Purpose | Input | Output |
|------|---------|-------|--------|
| [tool] | [why] | [format] | [format] |

### Memory
- **Short-term**: [conversation context]
- **Long-term**: [persistent storage approach]
- **Shared**: [what other agents can access]

### Decision Logic
- IF [condition] → [action]
- IF [condition] → [escalate to human]
- IF [error] → [fallback]

### Output
[What this agent produces and where it goes]
```

## Output Format

```markdown
# AI Agent System: [Name]

## Architecture Overview
**Pattern**: [architecture type]
**Agents**: [count]
**Orchestration**: [how they coordinate]

## System Diagram
```
[Text-based architecture diagram]
```

## Agent Specifications

### Agent 1: [Name]
[Full specification per template above]

### Agent 2: [Name]
[Full specification]

## Orchestration Logic
[How agents communicate and coordinate]

## Error Handling
[What happens when things go wrong]

## Human Touchpoints
[Where and when humans intervene]

## Implementation Guide
- **Platform**: [recommendation]
- **Models**: [which LLMs for which agents]
- **Estimated cost**: [per-run cost estimate]
- **Setup steps**: [how to build it]
```

## Quality Checklist
- [ ] Each agent has a clear, single responsibility
- [ ] Tools defined with input/output formats
- [ ] Orchestration logic handles all paths
- [ ] Error handling and fallbacks defined
- [ ] Human oversight points identified
- [ ] Cost estimate included
