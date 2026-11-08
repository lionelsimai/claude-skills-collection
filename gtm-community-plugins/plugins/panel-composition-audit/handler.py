"""Handler for Panel Composition Audit (panel-composition-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "topic balance",
    "seniority mix",
    "company mix",
    "perspective mix",
    "moderator assigned"
  ],
  "slug": "panel-composition-audit",
  "name": "Panel Composition Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})
