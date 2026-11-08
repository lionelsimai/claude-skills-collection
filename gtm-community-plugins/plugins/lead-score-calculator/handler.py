"""Handler for Lead Score Calculator (lead-score-calculator). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "score",
  "items": [
    "firmographic fit",
    "engagement recency",
    "page intent",
    "role seniority",
    "company growth"
  ],
  "slug": "lead-score-calculator",
  "name": "Lead Score Calculator"
}
def run(args):
    return run_engine(CONFIG, args or {})
