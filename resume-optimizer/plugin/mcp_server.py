#!/usr/bin/env python3
"""Lionel Resume Optimizer — MCP plugin server (Python 3, stdlib only).

This is the *plugin* counterpart to the Resume Optimizer *skill*:
- The skill (SKILL.md) teaches an agent the workflow and honesty rules.
- This plugin gives an agent callable tools that actually do the
  deterministic work: ATS scoring, keyword extraction, gap analysis
  and format checking. The rewrite itself stays with the calling
  agent, under the skill's no-fabrication rule.

Transport: MCP over stdio (newline-delimited JSON-RPC 2.0).
No dependencies, no network, no data leaves the machine.

Tools:
  score_resume      {resume_text, job_text, top?}      -> ATS score report
  extract_keywords  {job_text, top?}                   -> ranked keywords
  gap_analysis      {resume_text, job_text, top?}      -> matched / missing /
                                                          must-have missing
  check_format      {resume_text}                      -> sections, word
                                                          count, format flags

Run:  python3 mcp_server.py
"""

import json
import os
import sys

# Load the scorer: prefer the repo's canonical scripts/ copy, fall back
# to the vendored copy bundled in this plugin folder so the plugin also
# works when copied out on its own.
_HERE = os.path.dirname(os.path.abspath(__file__))
for _candidate in (os.path.join(_HERE, "..", "scripts"), _HERE):
    if os.path.isdir(_candidate) and _candidate not in sys.path:
        sys.path.insert(0, _candidate)

try:
    from resume_optimizer import score_resume as _score, extract_keywords as _kw
    import resume_optimizer as _core
except ImportError:  # vendored copy name
    from resume_optimizer_core import score_resume as _score, extract_keywords as _kw
    import resume_optimizer_core as _core

SERVER_NAME = "lionel-resume-optimizer"
SERVER_VERSION = "2.0.0"
PROTOCOL_VERSION = "2024-11-05"

TOOLS = [
    {
        "name": "score_resume",
        "description": (
            "Score a resume against a job description: overall ATS readiness "
            "(0-100), keyword coverage, must-have coverage from the posting's "
            "Requirements section, section checks and format red flags. "
            "Deterministic — never invents anything. Run before and after a "
            "rewrite to show the before/after score."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "resume_text": {"type": "string", "description": "Full plain-text resume"},
                "job_text": {"type": "string", "description": "Full plain-text job description"},
                "top": {"type": "integer", "description": "Keywords to check (default 30)"},
            },
            "required": ["resume_text", "job_text"],
        },
    },
    {
        "name": "extract_keywords",
        "description": (
            "Extract the ranked keywords and skills a job description actually "
            "names, with mention counts. Use to parse a posting before tailoring."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "job_text": {"type": "string", "description": "Full plain-text job description"},
                "top": {"type": "integer", "description": "Max keywords (default 30)"},
            },
            "required": ["job_text"],
        },
    },
    {
        "name": "gap_analysis",
        "description": (
            "Compare a resume to a job description and return matched keywords, "
            "missing keywords and missing must-haves. The calling agent must "
            "then sort missing items honestly into the skill's three buckets: "
            "present-but-buried, rephraseable, genuinely missing. Genuinely "
            "missing items must never be written into the resume."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "resume_text": {"type": "string"},
                "job_text": {"type": "string"},
                "top": {"type": "integer", "description": "Keywords to check (default 30)"},
            },
            "required": ["resume_text", "job_text"],
        },
    },
    {
        "name": "check_format",
        "description": (
            "Check a resume on its own (no job needed): which standard ATS "
            "sections are present, word count, and format red flags such as "
            "fake multi-column spacing or pointer phrases parsers drop."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "resume_text": {"type": "string"},
            },
            "required": ["resume_text"],
        },
    },
]


def _check_format(resume_text):
    import re
    lower = resume_text.lower()
    sections = {
        name: re.search(pattern, lower) is not None
        for name, pattern in _core.SECTION_PATTERNS.items()
    }
    flags = [msg for pattern, msg in _core.FORMAT_RED_FLAGS
             if re.search(pattern, resume_text, re.IGNORECASE)]
    aligned = [ln for ln in resume_text.splitlines()
               if len(re.findall(r" {3,}", ln)) >= 2]
    if len(aligned) >= 3:
        flags.append("Several lines use wide space runs to fake columns — "
                     "multi-column layouts are read out of order by parsers.")
    word_count = len(resume_text.split())
    if word_count < 200:
        flags.append(f"Resume is short ({word_count} words) — thin content scores poorly.")
    if word_count > 1200:
        flags.append(f"Resume is long ({word_count} words) — most ATS/recruiter passes favour 400–800.")
    return {
        "sections": sections,
        "section_score_pct": round(100 * sum(sections.values()) / len(sections)),
        "format_flags": flags,
        "word_count": word_count,
    }


def call_tool(name, args):
    top = int(args.get("top") or 30)
    if name == "score_resume":
        return _score(args["resume_text"], args["job_text"], top=top)
    if name == "extract_keywords":
        return {"keywords": [{"keyword": kw, "job_mentions": c}
                              for kw, c in _kw(args["job_text"], top=top)]}
    if name == "gap_analysis":
        r = _score(args["resume_text"], args["job_text"], top=top)
        return {
            "overall_score": r["overall_score"],
            "keyword_coverage_pct": r["keyword_coverage_pct"],
            "matched_keywords": r["matched_keywords"],
            "missing_keywords": r["missing_keywords"],
            "must_have_coverage_pct": r["must_have_coverage_pct"],
            "must_have_missing": r["must_have_missing"],
            "honesty_rule": (
                "Sort missing_keywords into: (1) present but buried, "
                "(2) rephraseable — same work, posting's words, "
                "(3) genuinely missing. Only buckets 1-2 may be written "
                "into a rewrite. Never fabricate experience or metrics."
            ),
        }
    if name == "check_format":
        return _check_format(args["resume_text"])
    raise ValueError(f"Unknown tool: {name}")


def _reply(req_id, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": req_id}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        method, req_id = req.get("method", ""), req.get("id")
        if req_id is None:  # notification
            continue
        try:
            if method == "initialize":
                _reply(req_id, {
                    "protocolVersion": PROTOCOL_VERSION,
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                })
            elif method == "ping":
                _reply(req_id, {})
            elif method == "tools/list":
                _reply(req_id, {"tools": TOOLS})
            elif method == "tools/call":
                params = req.get("params") or {}
                result = call_tool(params.get("name", ""), params.get("arguments") or {})
                _reply(req_id, {
                    "content": [{"type": "text", "text": json.dumps(result, indent=2)}],
                    "structuredContent": result,
                    "isError": False,
                })
            else:
                _reply(req_id, error={"code": -32601, "message": f"Method not found: {method}"})
        except Exception as exc:  # keep the server alive on a bad call
            _reply(req_id, {
                "content": [{"type": "text", "text": f"Error: {exc}"}],
                "isError": True,
            })
    return 0


if __name__ == "__main__":
    sys.exit(main())
