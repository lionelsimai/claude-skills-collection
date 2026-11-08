"""Handler for Benchmark Gap Audit (benchmark-gap-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "active rate",
    "response time",
    "event show rate",
    "nps",
    "retention rate"
  ],
  "slug": "benchmark-gap-audit",
  "name": "Benchmark Gap Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})
