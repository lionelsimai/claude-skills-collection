---
name: code-reviewer
description: |
  Review code for bugs, performance, security, and best practices.
  TRIGGERS - Use when user wants code review, bug checking, or code quality analysis.
---

# Code Reviewer

## Review Checklist
For every code review, check:

1. **Correctness**: Does it work as intended?
2. **Bugs**: Edge cases, off-by-one, null handling
3. **Security**: Input validation, injection, auth
4. **Performance**: N+1 queries, unnecessary loops, memory
5. **Readability**: Clear naming, comments, structure
6. **Best practices**: DRY, SOLID, patterns
7. **Error handling**: Try/catch, fallbacks, logging
8. **Tests**: Coverage, edge cases, meaningful assertions

## Output Format

```markdown
# Code Review: [File/PR Name]

## Summary
[Overall assessment — 1-2 sentences]
**Rating**: 🟢 Approve / 🟡 Approve with suggestions / 🔴 Request changes

## Critical Issues 🔴
[Must fix before merge]

## Suggestions 🟡
[Recommended improvements]

## Nitpicks 🔵
[Optional style/preference items]

## What's Good 🟢
[Positive feedback — always include this]
```
