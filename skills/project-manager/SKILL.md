---
name: project-manager
description: "Manage projects end to end: intake, prioritise, track status across parallel builds, and produce standup and weekly-review summaries. Use when the user asks to manage, track or drive a project, plan the week, or asks for a status or standup update."
category: Operations
license: MIT
version: 1.0.0
---

# Project Manager

## Purpose
Keep the user's many parallel builds (workshops, partnerships, community programs, product experiments, job-hunt threads) organized: one place for every project, its goal, its tasks, and its current state. Own task intake, prioritization, and status reporting. Keep builds running in their own threads — this skill coordinates and reports; it never does unrelated work on the side.

Inspired by [finna/project-manager-skill](https://github.com/finna/project-manager-skill); rebuilt here in original form for a multi-project builder workflow.

## Tooling
- CLI: `bin/pm` (python3 stdlib only). Run as `. <cmd>`, or add the skill's `bin/` to PATH for the session.
- Data: one JSON file per project in `.`. Override with `PM_PROJECTS_DIR` (used by tests). Schema in `references/task-schema.md`.

## Workflow

### 1. Intake
When the user names a new project or a task, capture it before anything else:
- `pm init "Project Name" --goal "..." --deadline YYYY-MM-DD` (creates the project file)
- `pm task add <project> "Task title" --priority P0|P1|P2|P3 --due YYYY-MM-DD`

### 2. Prioritize
- Default every task to P2. P0 = blocked revenue or hard deadline this week; P1 = moves a live deal or event; P3 = nice-to-have.
- If he gives a deadline, record it. Flag overdue items in status and reviews — never silently drop them.
- One project may have many tasks; across projects, keep the total P0 count small. If P0s pile up, surface that explicitly.

### 3. Track
- `pm task start|done|block|unblock <project> <task-id> --note "..."` — move tasks through `todo → doing → done`, with `blocked` as a side state. Notes are timestamped and kept.
- `pm note <project> "text" [--task tN]` — decisions, context, anything worth remembering about the project.
- `pm status <project>` — render the markdown status summary (goal, deadline, grouped tasks, recent notes). `--out file.md` writes it to a file.

### 4. Report
- **Standup:** `pm standup` — done since yesterday, next up, blocked, across all active projects. Good as a morning brief.
- **Weekly review:** `pm review` — shipped / in-flight / blocked / overdue per project for the trailing 7 days.
- `pm list` — active projects with done counts; `--status all` or `archived` to see the rest; `pm archive <project>` when finished or killed.

## Output Contract
- `pm status` / `pm standup` / `pm review` print markdown to stdout — reuse it directly in the chat reply or as a document.
- When reporting to the user: lead with blockers and overdue items, then what's next. Keep it short; he reads bullets, not essays.
- A status answer never starts new work, sends messages, or spends money. Say so if he asks.

## Operating Rules
- Project facts live in `.`, never in this skill's directory and never in memory files.
- Keep `implemented` distinct from `done-and-verified`: a task is `done` only when its outcome is actually confirmed, not when a draft exists.
- Silence is not approval. If a milestone needs a decision that changes scope, deadline, or money, ask.
- Killed projects get archived, not deleted — the record stays for the weekly review.

## When to use

Use this skill when the task described in the purpose above is in front of you, before improvising your own process.

## Guardrails and quality checks

- Apply the rules in this skill throughout. Never fabricate facts or numbers, keep external actions draft-only until a human approves them, and state anything you could not verify.

## Worked example

Example request: "Use the Project Manager skill: [the user describes their situation, inputs and goal]." Worked output: follow the workflow step by step, produce the output format defined above, run the quality checks, and list any unverified item instead of guessing it.
