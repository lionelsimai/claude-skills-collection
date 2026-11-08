"""Handler for Community Guidelines Checklist (community-guidelines-checklist). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "checklist",
  "items": [
    "guidelines pinned",
    "reporting route",
    "moderator rota",
    "response sla",
    "appeals process"
  ],
  "slug": "community-guidelines-checklist",
  "name": "Community Guidelines Checklist"
}
def run(args):
    return run_engine(CONFIG, args or {})
