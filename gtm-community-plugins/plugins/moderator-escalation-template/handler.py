"""Handler for Moderator Escalation Template (moderator-escalation-template). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "incident summary",
    "evidence supplied by moderator",
    "rule reference",
    "action taken",
    "appeal note"
  ],
  "slug": "moderator-escalation-template",
  "name": "Moderator Escalation Template"
}
def run(args):
    return run_engine(CONFIG, args or {})
