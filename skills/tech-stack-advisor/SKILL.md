---
name: tech-stack-advisor
description: |
  Recommend technology stacks and tools for specific business needs.
  TRIGGERS - Use when user wants tech recommendations, tool comparisons, or stack architecture.
---

# Tech Stack Advisor

## Output Format

```markdown
# Tech Stack Recommendation: [Use Case]

## Requirements Analysis
| Need | Priority | Notes |
|------|----------|-------|
| [need] | Must have / Nice to have | [context] |

## Recommended Stack

### [Category 1: e.g., CRM]
**Recommended**: [Tool] — $[price]/mo
**Why**: [reasoning]
**Alternatives**: [Tool B] ($X), [Tool C] ($X)

### [Category 2: e.g., Email]
[Same structure]

## Integration Map
```
[Tool A] ←→ [Tool B] (via [connector])
[Tool B] → [Tool C] (via [API/Zapier])
```

## Cost Summary
| Tool | Monthly | Annual | Notes |
|------|---------|--------|-------|
| [tool] | $X | $X | [tier] |
| **Total** | **$X** | **$X** | |

## Migration Plan
[If replacing existing tools]

## Setup Timeline
[Phased implementation]
```
