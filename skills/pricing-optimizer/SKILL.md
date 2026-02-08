---
name: pricing-optimizer
description: |
  Analyze and optimize product/service pricing strategies.
  TRIGGERS - Use when user wants to set prices, optimize pricing, or create pricing tiers.
---

# Pricing Optimizer

## Overview
Analyzes market positioning and creates optimized pricing strategies with tiers, anchoring, and packaging.

## Workflow

### Step 1: Understand the Context
1. **Product/service**: What are you pricing?
2. **Current price**: (if existing)
3. **Competitors**: What do alternatives cost?
4. **Costs**: What does it cost you to deliver?
5. **Value delivered**: What's the ROI for the customer?
6. **Target customer**: Who's buying and what's their budget?

### Step 2: Analyze Pricing Models

| Model | Best For | Pros | Cons |
|-------|----------|------|------|
| **One-time** | Products, templates | Simple, high AOV | No recurring revenue |
| **Subscription** | SaaS, ongoing services | Predictable revenue | Churn risk |
| **Tiered** | Different segments | Captures more market | Complex to manage |
| **Usage-based** | API, volume services | Scales with value | Unpredictable revenue |
| **Value-based** | Consulting, high-ticket | Highest margins | Harder to sell |
| **Freemium** | Growth-focused | Low friction | Conversion challenge |

### Step 3: Design the Pricing

## Output Format

```markdown
# Pricing Strategy: [Product/Service]

## Pricing Analysis

### Market Position
- **Budget options**: $[X] ([competitors])
- **Mid-market**: $[X] ([competitors])
- **Premium**: $[X] ([competitors])
- **Your position**: [where you fit and why]

### Value Analysis
- **Customer ROI**: [what they get back]
- **Value/price ratio**: [justify the price]
- **Price sensitivity**: [how price-sensitive is your market?]

## Recommended Pricing

### Tier 1: [Name] — $[Price]
**Target**: [who this is for]
**Includes**:
- [Feature/deliverable]
- [Feature/deliverable]
**Positioning**: [why this tier exists]

### Tier 2: [Name] — $[Price] ⭐ MOST POPULAR
**Target**: [who this is for]
**Includes**:
- Everything in Tier 1, plus:
- [Additional feature]
- [Additional feature]
**Positioning**: [why this is the sweet spot]

### Tier 3: [Name] — $[Price]
**Target**: [who this is for]
**Includes**:
- Everything in Tier 2, plus:
- [Premium feature]
- [Premium feature]
**Positioning**: [anchoring and premium appeal]

## Pricing Psychology Applied
- **Anchoring**: [how tiers anchor perception]
- **Decoy effect**: [which tier drives the target choice]
- **Charm pricing**: [psychological pricing tactics]
- **Bundling**: [what's bundled for perceived value]

## Revenue Projection
| Tier | Expected Mix | Monthly Revenue | Annual Revenue |
|------|-------------|----------------|---------------|
| Tier 1 | [X%] | $[X] | $[X] |
| Tier 2 | [X%] | $[X] | $[X] |
| Tier 3 | [X%] | $[X] | $[X] |
| **Total** | | **$[X]** | **$[X]** |

## Testing Plan
1. [How to validate pricing]
2. [A/B test approach]
3. [When to review and adjust]
```

## Quality Checklist
- [ ] Competitor pricing researched
- [ ] Value-based justification included
- [ ] 3 tiers with clear differentiation
- [ ] Pricing psychology applied
- [ ] Revenue projection realistic
- [ ] Testing plan included
