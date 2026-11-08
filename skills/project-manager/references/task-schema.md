# Task / project schema

`.`:

```json
{
  "slug": "hermes-lab",
  "name": "Hermes Lab",
  "goal": "Landing page + workshop funnel driving workshop signups",
  "deadline": "2026-11-30",
  "status": "active",          // active | archived
  "created": "2026-10-02",
  "owner": "you",
  "notes": ["2026-10-02: decided to ship landing first, funnel second"],
  "tasks": [
    {
      "id": "t1",
      "title": "Draft landing hero copy",
      "status": "todo",        // todo | doing | blocked | done
      "priority": "P1",        // P0 | P1 | P2 | P3
      "due": "2026-10-05",
      "owner": "",
      "created": "2026-10-02",
      "updated": "2026-10-02",
      "notes": []
    }
  ],
  "_seq": 1
}
```

- `id` is auto-assigned (`t1`, `t2`, ...) and never reused within a project.
- `_seq` is the internal counter; edit JSON by hand only when the CLI can't express what you need.
- Task notes are timestamped strings: `"2026-10-02 (blocked): Waiting on venue confirmation"`.
- Project-level notes hold decisions and context; task notes hold per-task history.
