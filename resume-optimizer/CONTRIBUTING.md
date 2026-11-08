# Contributing

Issues and pull requests are welcome. Three rules keep this project
what it is:

1. **The honesty rule is not negotiable.** No change may make the
   workflow, the scorer or the examples fabricate, inflate or stuff
   keywords. If a change helps a resume claim something the candidate
   cannot defend in an interview, it will not be merged.
2. **Scripts stay dependency-free.** `scripts/` runs on the Python 3
   standard library alone, on any machine, offline.
3. **Every scoring change ships with a test.** Run
   `python3 tests/test_resume_optimizer.py` (or `pytest tests/`) before
   opening a pull request — CI runs the same suite on Python 3.9–3.12,
   plus a check that the root skill files and the
   `skills/resume-optimizer/` plugin copy stay in sync.

If you regenerate `examples/sample-report.md`, paste the scorer's
actual output — the examples must never claim numbers the tool did
not produce.
