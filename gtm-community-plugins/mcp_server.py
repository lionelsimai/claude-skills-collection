#!/usr/bin/env python3
"""Shared MCP server for all 120 GTM + Community plugins. Stdlib only.
Transport: MCP over stdio (newline-delimited JSON-RPC 2.0).
Run: python3 mcp_server.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from core.registry import get_registry
NAME, VERSION = "lionel-gtm-community-plugins", "1.0.0"
def reply(i, result=None, error=None):
    m={"jsonrpc":"2.0","id":i}
    m["error" if error else "result"]=error if error else result
    sys.stdout.write(json.dumps(m)+"\n"); sys.stdout.flush()
def main():
    reg=get_registry()
    for line in sys.stdin:
        line=line.strip()
        if not line: continue
        try: req=json.loads(line)
        except json.JSONDecodeError: continue
        method, rid = req.get("method",""), req.get("id")
        if rid is None: continue
        try:
            if method=="initialize": reply(rid, {"protocolVersion":"2024-11-05","capabilities":{"tools":{}},"serverInfo":{"name":NAME,"version":VERSION}})
            elif method=="ping": reply(rid, {})
            elif method=="tools/list": reply(rid, {"tools": reg.list_tools()})
            elif method=="tools/call":
                p=req.get("params") or {}; r=reg.call(p.get("name",""), p.get("arguments") or {})
                reply(rid, {"content":[{"type":"text","text":json.dumps(r,indent=2)}],"structuredContent":r,"isError":False})
            else: reply(rid, error={"code":-32601,"message":f"Method not found: {method}"})
        except Exception as e: reply(rid, {"content":[{"type":"text","text":f"Error: {e}"}],"isError":True})
    return 0
if __name__=="__main__": sys.exit(main())
