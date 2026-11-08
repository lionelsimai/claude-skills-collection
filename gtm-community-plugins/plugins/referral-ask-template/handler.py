"""Handler for Referral Ask Template (referral-ask-template). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "context",
    "reason for asking",
    "specific person type",
    "easy yes path",
    "thank you note"
  ],
  "slug": "referral-ask-template",
  "name": "Referral Ask Template"
}
def run(args):
    return run_engine(CONFIG, args or {})
