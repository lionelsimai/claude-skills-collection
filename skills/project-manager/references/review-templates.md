# Review templates

## Standup (daily)

```markdown
# Standup — <date> (since <since>)
## Done
- <project>: <task> (<id>)
## Next up
- <project>: <task> (<id>)
## Blocked
- <project>: <task> (<id>)
```

## Weekly review

```markdown
# Weekly review — week ending <date> (since <since>)
## <Project name> (<slug>)
Goal: <goal>
- Shipped this week: N
  - <task> (<id>)
- In flight / blocked: N
  - <id> [status] <task> (due ...)
- Overdue: N
  - <id> [status] <task> (due ...)
```

## Status summary (single project)

```markdown
# <Project name>
Goal: <goal>
Deadline: <deadline>
Status: <status>
Tasks: N (x todo, y doing, z blocked, w done)

## TODO / DOING / BLOCKED / DONE
- <id> [status] (priority) <task> due <date> @owner

## Notes
- <note>
```

## Friday three (how to report to the user)

1. What's blocked or overdue (with what's needed to unblock).
2. What shipped this week (one line per item).
3. What matters next week (the 3 highest-priority moves).

Lead with #1. Keep the whole thing under ~15 lines for chat; expand only in a document when asked.
