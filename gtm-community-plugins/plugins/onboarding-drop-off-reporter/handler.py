"""Handler for Onboarding Drop-off Reporter (onboarding-drop-off-reporter). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "analyze",
  "items": [
    "joined",
    "profile completed",
    "introduced",
    "attended first event",
    "active at day 30"
  ],
  "slug": "onboarding-drop-off-reporter",
  "name": "Onboarding Drop-off Reporter"
}
def run(args):
    return run_engine(CONFIG, args or {})
