---
name: survey-analyzer
description: |
  Analyze survey results and generate actionable insights.
  TRIGGERS - Use when user wants to analyze survey data, questionnaire results, or feedback forms.
---

# Survey Analyzer

## Overview
Analyzes survey responses to extract patterns, insights, and actionable recommendations.

## Workflow

### Step 1: Receive the Data
Accept survey data in any format (CSV, JSON, pasted text, or described verbally).

### Step 2: Analyze

1. **Response overview**: Total responses, completion rate, date range
2. **Quantitative analysis**: Averages, distributions, correlations
3. **Qualitative analysis**: Theme extraction from open-ended responses
4. **Segment analysis**: Differences between groups
5. **Trend identification**: Patterns and outliers

### Step 3: Generate Report

## Output Format

```markdown
# Survey Analysis: [Survey Name]

## Overview
- **Total responses**: [N]
- **Completion rate**: [X%]
- **Date range**: [dates]
- **Key finding**: [One-sentence headline result]

## Executive Summary
[3-5 sentences covering the most important findings]

## Key Metrics

| Question/Metric | Result | Benchmark | Status |
|----------------|--------|-----------|--------|
| [Metric 1] | [value] | [if known] | 🟢/🟡/🔴 |

## Detailed Findings

### Finding 1: [Title]
**Data**: [what the numbers show]
**Insight**: [what it means]
**Action**: [what to do about it]

[Repeat for top findings]

## Open-Ended Response Themes
| Theme | Frequency | Sentiment | Sample Quote |
|-------|-----------|-----------|-------------|
| [Theme] | [X mentions] | Positive/Negative | "[quote]" |

## Recommendations
1. [Action item with priority]
2. [Action item with priority]
3. [Action item with priority]

## Methodology Notes
[How analysis was conducted, limitations]
```

## Quality Checklist
- [ ] Key finding stated upfront
- [ ] Quantitative and qualitative data combined
- [ ] Recommendations are specific and actionable
- [ ] Visualizations suggested for key data
- [ ] Limitations acknowledged
