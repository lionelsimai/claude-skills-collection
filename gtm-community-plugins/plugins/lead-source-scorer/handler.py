"""Handler for Lead Source Scorer (lead-source-scorer). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "conversion rate",
    "cost per lead",
    "data completeness",
    "reply rate",
    "unsubscribe rate"
  ],
  "slug": "lead-source-scorer",
  "name": "Lead Source Scorer"
}
def run(args):
    return run_engine(CONFIG, args or {})
