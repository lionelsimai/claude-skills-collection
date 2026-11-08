#!/usr/bin/env python3
"""Registry: loads every plugins/*/plugin.json + handler.py and exposes
all tools to the shared MCP and REST servers. Add a plugin folder and
it is automatically registered — no server code changes."""
import importlib.util, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT not in sys.path: sys.path.insert(0, ROOT)
from core.engines import run_engine  # noqa: E402

def _load_handler(path):
    spec = importlib.util.spec_from_file_location(f"handler_{os.path.basename(os.path.dirname(path))}", path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

class Registry:
    def __init__(self, root=ROOT):
        self.plugins, self.tools = {}, {}
        pdir = os.path.join(root, "plugins")
        for slug in sorted(os.listdir(pdir)):
            pj = os.path.join(pdir, slug, "plugin.json")
            if not os.path.isfile(pj): continue
            meta = json.load(open(pj))
            handler = _load_handler(os.path.join(pdir, slug, "handler.py"))
            self.plugins[slug] = {"meta": meta, "handler": handler}
            for t in meta["tools"]:
                self.tools[t["name"]] = {"meta": t, "plugin": slug, "run": handler.run}
    def list_tools(self):
        return [{"name": n, "description": e["meta"]["description"],
                 "inputSchema": e["meta"]["inputSchema"]} for n, e in sorted(self.tools.items())]
    def call(self, name, args):
        if name not in self.tools: raise ValueError(f"Unknown tool: {name}")
        return self.tools[name]["run"](args or {})

REGISTRY = None
def get_registry():
    global REGISTRY
    if REGISTRY is None: REGISTRY = Registry()
    return REGISTRY
