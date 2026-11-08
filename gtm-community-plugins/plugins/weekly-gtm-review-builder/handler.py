"""Handler for Weekly GTM Review Builder (weekly-gtm-review-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "headline metric",
    "wins",
    "losses",
    "lessons",
    "one priority"
  ],
  "slug": "weekly-gtm-review-builder",
  "name": "Weekly GTM Review Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})
