"""Tests for scripts/resume_optimizer.py — run: python3 -m pytest tests/ -q
or plain: python3 tests/test_resume_optimizer.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from resume_optimizer import extract_keywords, score_resume  # noqa: E402

JOB = """
Growth Marketing Manager. Own paid media campaigns and lifecycle email
marketing in HubSpot. Analyse data in Google Analytics and Excel.
Run A/B testing. Stakeholder management across cross-functional teams.
Requirements: 4+ years growth marketing, HubSpot, Google Analytics,
paid media, A/B testing, data analysis.
"""

RESUME = """
Jane Lim
jane.lim@email.com
Summary
Growth marketing specialist with 5 years in B2C SaaS.
Experience
Growth Marketing Manager, AppCo, 2021 - Present
- Ran paid media campaigns and lifecycle email marketing in HubSpot
- Analysed campaign data in Excel; presented KPI dashboards
Education
Bachelor of Business, 2018
Skills
HubSpot, Excel, paid media, email marketing
"""


def test_keywords_surface_job_terms():
    kws = dict(extract_keywords(JOB, top=30))
    assert "hubspot" in kws
    assert "paid media" in kws
    assert "a/b testing" in kws


def test_score_finds_sections_and_coverage():
    result = score_resume(RESUME, JOB)
    assert result["sections"]["summary"] is True
    assert result["sections"]["experience"] is True
    assert result["sections"]["education"] is True
    assert result["sections"]["skills"] is True
    assert result["sections"]["contact"] is True
    assert result["keyword_coverage_pct"] > 30
    missing = {m["keyword"] for m in result["missing_keywords"]}
    assert "google analytics" in missing  # genuinely absent from resume


def test_score_flags_thin_resume():
    result = score_resume("John Doe\njohn@email.com\nDid some work.", JOB)
    assert result["overall_score"] < 40
    assert any("short" in f for f in result["format_flags"])


def test_synonyms_count_as_matches():
    job = ("Frontend Developer. Requirements: JavaScript, Amazon Web "
           "Services, Microsoft Excel. Build user interfaces.")
    resume = ("Sam Koh\nsam@email.com\nSummary\nFrontend developer.\n"
              "Experience\nDeveloper, WebCo, 2020 - Present\n"
              "- Built UI in JS, deployed on AWS, tracked data in Excel\n"
              "Education\nBSc, 2019\nSkills\nJS, AWS, Excel")
    result = score_resume(resume, job)
    missing = {m["keyword"] for m in result["missing_keywords"]}
    assert "javascript" not in missing
    assert result["must_have_coverage_pct"] is not None
    assert result["must_have_coverage_pct"] >= 50


def test_no_substring_false_positives():
    # "excellence" must not surface "excel"; "seasoned" must not surface "seo".
    job = ("Operations Lead. We value operational excellence and a seasoned "
           "team. Lead regional operations across markets.")
    kws = dict(extract_keywords(job, top=30))
    assert "excel" not in kws
    resume = "Sam\nsam@x.com\nSummary\nOps lead.\nExperience\nLed operations.\nEducation\nBSc\nSkills\nOperations"
    result = score_resume(resume, job)
    missing = {m["keyword"] for m in result["missing_keywords"]}
    assert "excel" not in missing


def test_punctuation_tokens_normalised():
    # "functions." and "anz." in a posting are the words functions / anz,
    # not separate keywords, and must match a resume that uses them plainly.
    job = ("Strategy Lead for SEA & ANZ. Build scalable processes across "
           "business lines and functions. Drive execution across ANZ.")
    kws = dict(extract_keywords(job, top=30))
    assert "functions." not in kws and "anz." not in kws
    resume = ("Sam\nsam@x.com\nSummary\nStrategy lead.\nExperience\n"
              "Built processes across functions in ANZ.\nEducation\nBSc\n"
              "Skills\nStrategy, functions")
    result = score_resume(resume, job)
    missing = {m["keyword"] for m in result["missing_keywords"]}
    assert "functions" not in missing and "anz" not in missing


def test_plural_variants_match():
    job = ("Operations Manager. Requirements: operations, reporting "
           "frameworks, stakeholder management. Operations operations.")
    resume = ("Sam\nsam@x.com\nSummary\nManager.\nExperience\n"
              "Owned operation and a reporting framework.\nEducation\nBSc\n"
              "Skills\nOperation, reporting framework")
    result = score_resume(resume, job)
    missing = {m["keyword"] for m in result["missing_keywords"]}
    assert "operations" not in missing


def test_bigram_components_suppressed():
    job = ("Lead for South East Asia. Grow South East Asia markets. "
           "South East Asia is the priority region.")
    kws = dict(extract_keywords(job, top=30))
    if "south east" in kws:
        assert "south" not in kws and "east" not in kws


if __name__ == "__main__":
    test_keywords_surface_job_terms()
    test_score_finds_sections_and_coverage()
    test_score_flags_thin_resume()
    test_synonyms_count_as_matches()
    test_no_substring_false_positives()
    test_punctuation_tokens_normalised()
    test_plural_variants_match()
    test_bigram_components_suppressed()
    print("All tests passed.")
