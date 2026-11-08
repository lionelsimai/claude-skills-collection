"""Handler for Post Moderation Classifier (post-moderation-classifier). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "classify",
  "items": [
    "welcome",
    "self promotion",
    "spam",
    "abuse",
    "off topic",
    "needs help"
  ],
  "slug": "post-moderation-classifier",
  "name": "Post Moderation Classifier"
}
def run(args):
    return run_engine(CONFIG, args or {})
