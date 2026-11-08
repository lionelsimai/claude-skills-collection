"""Handler for No-show Recovery Drafter (no-show-recovery-drafter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "grace opening",
    "no blame",
    "two new options",
    "value recap"
  ],
  "slug": "no-show-recovery-drafter",
  "name": "No-show Recovery Drafter"
}
def run(args):
    return run_engine(CONFIG, args or {})
