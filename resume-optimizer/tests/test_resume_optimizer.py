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


if __name__ == "__main__":
    test_keywords_surface_job_terms()
    test_score_finds_sections_and_coverage()
    test_score_flags_thin_resume()
    print("All tests passed.")
