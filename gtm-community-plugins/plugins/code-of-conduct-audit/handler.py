"""Handler for Code of Conduct Audit (code-of-conduct-audit). Config-driven; logic lives in core/engines.py."""
import os,sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),"..",".."))
from core.engines import run_engine
CONFIG={
  "kind": "audit",
  "items": [
    "expected behaviour",
    "unacceptable behaviour",
    "reporting route",
    "consequences",
    "appeals process"
  ],
  "slug": "code-of-conduct-audit",
  "name": "Code of Conduct Audit"
}
def run(args):
    return run_engine(CONFIG, args or {})
