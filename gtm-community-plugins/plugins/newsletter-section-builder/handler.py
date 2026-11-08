"""Handler for Newsletter Section Builder (newsletter-section-builder). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "template",
  "items": [
    "headline",
    "what happened",
    "why it matters",
    "what to do",
    "link"
  ],
  "slug": "newsletter-section-builder",
  "name": "Newsletter Section Builder"
}
def run(args):
    return run_engine(CONFIG, args or {})
