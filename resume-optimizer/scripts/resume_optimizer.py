#!/usr/bin/env python3
"""Resume Optimizer helper tools (Python 3, standard library only).

Subcommands:
  keywords --job job.txt [--top 30]
      Extract ranked candidate keywords/skills from a job description.
  score --resume resume.txt --job job.txt [--json]
      Score a resume against a job description: keyword coverage,
      section checks and format red flags.

This script does deterministic text analysis only. The tailoring itself
(rewrite, gap judgement, honesty checks) is the agent's job — see SKILL.md.
"""

import argparse
import json
import re
import sys
from collections import Counter

# --------------------------------------------------------------------------
# Keyword extraction
# --------------------------------------------------------------------------

STOPWORDS = {
    "a", "an", "the", "and", "or", "of", "to", "in", "for", "with", "on",
    "at", "by", "as", "is", "are", "be", "will", "you", "we", "our", "your",
    "their", "this", "that", "it", "its", "from", "who", "what", "when",
    "work", "working", "team", "teams", "role", "job", "company", "business",
    "experience", "years", "year", "ability", "skills", "skill", "strong",
    "including", "across", "within", "using", "use", "used", "ensure",
    "support", "help", "join", "looking", "ideal", "candidate", "required",
    "requirements", "responsibilities", "qualifications", "preferred",
    "plus", "etc", "day", "new", "all", "other", "more", "about", "into",
    "over", "per", "such", "than", "then", "them", "they", "have", "has",
    "had", "can", "should", "must", "also", "well", "able", "drive",
}

# Multi-word terms worth more than single words when scoring.
PHRASE_PATTERNS = [
    r"machine learning", r"data analysis", r"data visualisation",
    r"data visualization", r"project management", r"stakeholder management",
    r"customer success", r"product management", r"user experience",
    r"a/b testing", r"ab testing", r"ci/cd", r"rest api", r"restful api",
    r"power bi", r"google analytics", r"search engine optimisation",
    r"search engine optimization", r"content strategy", r"brand strategy",
    r"social media", r"email marketing", r"paid media", r"budget management",
    r"team leadership", r"cross[- ]functional", r"agile", r"scrum",
    r"sql", r"python", r"excel", r"tableau", r"salesforce", r"hubspot",
    r"figma", r"javascript", r"typescript", r"react", r"node\.?js",
    r"aws", r"azure", r"gcp", r"kubernetes", r"docker", r"seo", r"sem",
    r"crm", r"saas", r"b2b", r"b2c", r"kpi", r"roi",
]


def tokenize(text):
    return re.findall(r"[a-zA-Z][a-zA-Z0-9+#.\-]*", text.lower())


def extract_keywords(job_text, top=30):
    """Return a ranked list of (keyword, count) from job description text."""
    lower = job_text.lower()
    counts = Counter()

    for pattern in PHRASE_PATTERNS:
        hits = re.findall(pattern, lower)
        if hits:
            counts[re.sub(r"[- ]", " ", hits[0])] += len(hits) * 2

    for token in tokenize(job_text):
        if token in STOPWORDS or len(token) < 3:
            continue
        if token.isdigit():
            continue
        counts[token] += 1

    # Bigrams of capitalised / repeated content words add signal.
    words = tokenize(job_text)
    for a, b in zip(words, words[1:]):
        if a not in STOPWORDS and b not in STOPWORDS and len(a) > 2 and len(b) > 2:
            counts[f"{a} {b}"] += 1

    ranked = [(kw, c) for kw, c in counts.most_common(top * 2) if c >= 2]
    return ranked[:top]


# --------------------------------------------------------------------------
# Scoring
# --------------------------------------------------------------------------

SECTION_PATTERNS = {
    "summary": r"\b(summary|profile|about me|objective)\b",
    "experience": r"\b(experience|employment|work history|career history)\b",
    "education": r"\b(education|qualifications|academic)\b",
    "skills": r"\b(skills|competencies|expertise|technical skills)\b",
    "contact": r"[\w.+-]+@[\w-]+\.[\w.]+",
}

FORMAT_RED_FLAGS = [
    (r"_{4,}|={4,}", "Long underscore/equal runs suggest drawn lines or text-box art."),
    (r"\b(click here|see attached|portfolio link)\b",
     "Pointer phrases ('see attached') hide content from parsers — spell content out."),
]


# Equivalent terms: a match on any member counts as a match for all.
SYNONYM_GROUPS = [
    {"javascript", "js"},
    {"typescript", "ts"},
    {"amazon web services", "aws"},
    {"google cloud platform", "gcp"},
    {"machine learning", "ml"},
    {"artificial intelligence", "ai"},
    {"user experience", "ux"},
    {"search engine optimization", "seo"},
    {"customer relationship management", "crm"},
    {"microsoft excel", "excel"},
    {"power bi", "powerbi"},
    {"node.js", "nodejs", "node"},
    {"bachelor's degree", "bachelors degree", "bachelor degree", "degree"},
]

SYNONYMS = {}
for _group in SYNONYM_GROUPS:
    for _term in _group:
        SYNONYMS[_term] = _group


def contains_keyword(text_lower, keyword):
    variants = SYNONYMS.get(keyword, {keyword})
    for variant in variants:
        pattern = r"\b" + re.escape(variant).replace(r"\ ", r"[\s\-]") + r"\b"
        if re.search(pattern, text_lower):
            return True
    return False


def requirements_segment(job_text):
    """Return the Requirements/Qualifications portion of a posting, if any."""
    match = re.search(
        r"(requirements|qualifications|what you.ll bring|must have|must-haves)",
        job_text, re.IGNORECASE)
    if not match:
        return ""
    tail = job_text[match.start():]
    # Stop at the next obvious top-level section heading, if present.
    stop = re.search(r"\n(about (the|us)|benefits|perks|how to apply|"
                     r"application|equal opportunity)\b", tail[50:],
                     re.IGNORECASE)
    if stop:
        tail = tail[:stop.start() + 50]
    return tail


def score_resume(resume_text, job_text, top=30):
    keywords = extract_keywords(job_text, top=top)
    resume_lower = resume_text.lower()

    matched, missing = [], []
    for kw, count in keywords:
        (matched if contains_keyword(resume_lower, kw) else missing).append(
            {"keyword": kw, "job_mentions": count})

    coverage = round(100 * len(matched) / len(keywords)) if keywords else 0

    segment = requirements_segment(job_text)
    must_keywords = extract_keywords(segment, top=15) if segment else []
    must_missing = [{"keyword": kw, "job_mentions": count}
                    for kw, count in must_keywords
                    if not contains_keyword(resume_lower, kw)]
    must_coverage = (round(100 * (len(must_keywords) - len(must_missing))
                           / len(must_keywords)) if must_keywords else None)

    sections = {}
    for name, pattern in SECTION_PATTERNS.items():
        sections[name] = re.search(pattern, resume_lower) is not None

    flags = [msg for pattern, msg in FORMAT_RED_FLAGS
             if re.search(pattern, resume_text, re.IGNORECASE)]

    aligned_lines = [ln for ln in resume_text.splitlines()
                     if len(re.findall(r" {3,}", ln)) >= 2]
    if len(aligned_lines) >= 3:
        flags.append("Several lines use wide space runs to fake columns — "
                     "multi-column layouts are read out of order by parsers.")

    word_count = len(resume_text.split())
    if word_count < 200:
        flags.append(f"Resume is short ({word_count} words) — thin content scores poorly.")
    if word_count > 1200:
        flags.append(f"Resume is long ({word_count} words) — most ATS/recruiter passes favour 400–800.")

    section_score = round(100 * sum(sections.values()) / len(sections))
    if must_coverage is None:
        overall = round(0.7 * coverage + 0.3 * section_score)
    else:
        overall = round(0.5 * coverage + 0.2 * must_coverage
                        + 0.3 * section_score)

    return {
        "overall_score": overall,
        "keyword_coverage_pct": coverage,
        "keywords_checked": len(keywords),
        "matched_keywords": matched,
        "missing_keywords": missing,
        "must_have_coverage_pct": must_coverage,
        "must_have_missing": must_missing,
        "sections": sections,
        "format_flags": flags,
        "word_count": word_count,
    }


def print_score(result):
    print(f"Overall ATS readiness: {result['overall_score']}/100")
    print(f"Keyword coverage:      {result['keyword_coverage_pct']}% "
          f"({len(result['matched_keywords'])}/{result['keywords_checked']} keywords)")
    if result["must_have_coverage_pct"] is not None:
        print(f"Must-have coverage:    {result['must_have_coverage_pct']}% "
              f"(from the posting's Requirements section)")
        for item in result["must_have_missing"]:
            print(f"  ! missing must-have: {item['keyword']}")
    print(f"Word count:            {result['word_count']}")
    print("\nSections found:")
    for name, found in result["sections"].items():
        print(f"  {'[x]' if found else '[ ]'} {name}")
    if result["missing_keywords"]:
        print("\nMissing keywords (check the gap list before adding any):")
        for item in result["missing_keywords"]:
            print(f"  - {item['keyword']} (job mentions: {item['job_mentions']})")
    if result["format_flags"]:
        print("\nFormat flags:")
        for flag in result["format_flags"]:
            print(f"  ! {flag}")
    print("\nReminder: only add a missing keyword where the candidate "
          "genuinely has that skill. See SKILL.md, step 5.")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def read_file(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def main(argv=None):
    parser = argparse.ArgumentParser(description="Resume Optimizer helper tools")
    sub = parser.add_subparsers(dest="command", required=True)

    p_kw = sub.add_parser("keywords", help="Extract keywords from a job description")
    p_kw.add_argument("--job", required=True)
    p_kw.add_argument("--top", type=int, default=30)

    p_sc = sub.add_parser("score", help="Score a resume against a job description")
    p_sc.add_argument("--resume", required=True)
    p_sc.add_argument("--job", required=True)
    p_sc.add_argument("--top", type=int, default=30)
    p_sc.add_argument("--json", action="store_true")

    args = parser.parse_args(argv)

    if args.command == "keywords":
        job_text = read_file(args.job)
        for kw, count in extract_keywords(job_text, top=args.top):
            print(f"{count:>3}  {kw}")
        return 0

    if args.command == "score":
        result = score_resume(read_file(args.resume), read_file(args.job), top=args.top)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print_score(result)
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
