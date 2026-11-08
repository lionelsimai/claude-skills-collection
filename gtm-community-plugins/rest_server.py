#!/usr/bin/env python3
"""Shared REST server for all 120 plugins. Stdlib only.
GET /health, GET /catalog, GET /openapi.json, GET /.well-known/ai-plugin.json
POST /tools/{tool_name}  with a JSON body matching that tool's sample_input.
Run: python3 rest_server.py [--port 8787]"""
import argparse, json, os, sys
from http.server import BaseHTTPRequestHandler, HTTPServer
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,HERE)
from core.registry import get_registry
def load(n):
    with open(os.path.join(HERE,n)) as f: return f.read()
class H(BaseHTTPRequestHandler):
    def log_message(self,*a): pass
    def sendj(self,code,obj):
        d=obj if isinstance(obj,bytes) else (obj.encode() if isinstance(obj,str) else json.dumps(obj).encode())
        self.send_response(code); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(d))); self.end_headers(); self.wfile.write(d)
    def do_GET(self):
        if self.path=="/health": self.sendj(200,{"status":"ok","name":"lionel-gtm-community-plugins","version":"1.0.0","tools":len(get_registry().tools)})
        elif self.path=="/catalog": self.sendj(200, load("catalog.json"))
        elif self.path=="/openapi.json": self.sendj(200, load("openapi.json"))
        elif self.path==" /.well-known/ai-plugin.json" or self.path=="/.well-known/ai-plugin.json": self.sendj(200, load("ai-plugin.json"))
        else: self.sendj(404,{"error":"not found"})
    def do_POST(self):
        if not self.path.startswith("/tools/"): self.sendj(404,{"error":"not found"}); return
        try:
            n=int(self.headers.get("Content-Length") or 0); args=json.loads(self.rfile.read(n) or b"{}")
            self.sendj(200, get_registry().call(self.path[len("/tools/"):], args))
        except Exception as e: self.sendj(400,{"error":str(e)})
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--port",type=int,default=8787); ap.add_argument("--host",default="127.0.0.1"); a=ap.parse_args()
    HTTPServer((a.host,a.port),H).serve_forever()
