"""Handler for Detractor Recovery Checklist (detractor-recovery-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "acknowledge within 48h",
    "understand issue",
    "offer fix",
    "follow up",
    "log learning"
  ],
  "slug": "detractor-recovery-checklist",
  "name": "Detractor Recovery Checklist"
}
def run(args):
    return run_engine(CONFIG, args or {})
