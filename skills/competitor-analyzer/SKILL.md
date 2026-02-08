---
name: competitor-analyzer
description: |
  Analyze competitors across positioning, pricing, content strategy, strengths, and weaknesses.
  
  TRIGGERS - Use this skill when:
  - User wants to analyze a competitor or set of competitors
  - User asks "what are my competitors doing"
  - User wants competitive intelligence or market positioning analysis
  - User mentions competitor research, competitive landscape, or SWOT
---

# Competitor Analyzer

## Overview

Deep-dive competitor analysis that covers positioning, pricing, messaging, content strategy, and identifies gaps and opportunities. Outputs an actionable competitive intelligence report.

## Workflow

### Step 1: Define the Landscape
Ask the user:
1. **Your business**: What do you sell and to whom?
2. **Competitors**: List 2-5 competitors (names, URLs)
3. **Focus areas**: What matters most? (pricing, messaging, features, content, market position)

If the user provides competitor URLs, use web search to gather current data.

### Step 2: Analyze Each Competitor

For each competitor, evaluate:

**Positioning & Messaging**
- Headline/tagline — what promise do they lead with?
- Primary value proposition
- Target audience (who are they speaking to?)
- Brand voice and tone
- Key differentiators they claim

**Product & Pricing**
- Product/service tiers
- Pricing model (one-time, subscription, usage-based)
- Entry price vs premium price
- Free tier or trial availability
- Feature comparison

**Content & Marketing Strategy**
- Primary content channels (blog, YouTube, podcast, social)
- Content frequency and quality
- Lead magnets / free resources
- Email marketing approach
- Social media presence and engagement
- Paid advertising (if visible)

**Strengths & Weaknesses**
- What they do well
- Where they fall short
- Customer complaints (from reviews if available)
- Gaps in their offering

### Step 3: Generate Comparative Analysis

Create a side-by-side comparison matrix:

| Dimension | Competitor A | Competitor B | Competitor C | YOUR POSITION |
|-----------|-------------|-------------|-------------|---------------|
| Target Market | | | | |
| Price Range | | | | |
| Key Promise | | | | |
| Content Strategy | | | | |
| Unique Angle | | | | |

### Step 4: Identify Opportunities

Based on the analysis, provide:

1. **Positioning gaps** — what no competitor is saying that you could own
2. **Pricing opportunities** — where the market is over/under-served
3. **Content gaps** — topics/channels competitors are ignoring
4. **Messaging angles** — unique value props you could claim
5. **Quick wins** — things you could do this week to differentiate

### Step 5: Strategic Recommendations

Provide 3-5 specific, actionable recommendations ranked by impact and effort.

## Output Format

```markdown
# Competitive Analysis: [Your Business] vs [Competitors]

## Executive Summary
[2-3 sentence overview of key findings]

## Competitor Profiles
### [Competitor 1]
- **Positioning**: ...
- **Pricing**: ...
- **Strengths**: ...
- **Weaknesses**: ...

[Repeat for each competitor]

## Comparison Matrix
[Side-by-side table]

## Opportunities Identified
1. ...
2. ...

## Strategic Recommendations
1. [High impact, low effort] ...
2. [High impact, medium effort] ...
3. ...

## Your Competitive Advantage
[Summary of how to position against these competitors]
```

## Quality Checklist

- [ ] Each competitor analyzed on same dimensions
- [ ] Evidence-based (links/sources where possible)
- [ ] Actionable recommendations (not just observations)
- [ ] Opportunities mapped to user's specific business
- [ ] Comparison matrix included for quick reference
