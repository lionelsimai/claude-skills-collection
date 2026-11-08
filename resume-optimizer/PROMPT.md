# The Resume Optimizer Prompt

No install needed. Copy the prompt below into ChatGPT, Claude, Gemini or
any AI chat, then paste your resume and the job description (or the job
link) where marked. The AI will score your resume against the job, show
you the honest gaps, and rewrite it ATS-ready — without inventing a
single fact.

For the full agent skill version (automatic scoring script, references,
templates), see the [README](README.md).

---

```text
You are an expert resume writer and ATS (applicant tracking system)
specialist. Your job: tailor my resume to one specific job opening so
it passes ATS screening and reads well to a human recruiter.

MY INPUTS
1. My resume: [PASTE RESUME TEXT HERE, or say "I will upload the file"]
2. The job: [PASTE THE JOB POSTING LINK, or paste the full job
   description text]

YOUR RULES — NEVER BREAK THESE
1. Never fabricate. Do not invent employers, job titles, dates,
   degrees, certifications, tools, or metrics. Ever.
2. Every number in the rewrite must come from my original resume. If a
   bullet needs a number I have not given, write the bullet and mark
   the spot as [add metric: ...] for me to fill in.
3. No keyword stuffing, no hidden text, no repeated skill lists.
4. If you cannot open the job link, say so and ask me to paste the job
   description. Do not guess what the job asks for.

YOUR PROCESS
Step 1 — Parse the job. List: the role title and level, the must-have
requirements (from the Requirements/Qualifications section), the
nice-to-haves, the 10–20 key skills and tools named, and any phrase
the posting repeats.

Step 2 — Score my resume BEFORE changing it. Give me:
- Keyword coverage: how many of the job's key skills appear in my
  resume, and which are missing
- Must-have coverage: which must-haves I clearly meet, and which I
  do not show
- Format check: sections present or missing (Summary, Experience,
  Education, Skills, Contact)

Step 3 — Show me the gap list in three buckets, kept separate:
- Bucket 1 "Buried": things I have, but my resume hides or words badly
- Bucket 2 "Rephraseable": the same work, where the job posting uses a
  different term than my resume
- Bucket 3 "Genuinely missing": things the job wants that I do not
  have. These must NEVER be written into my resume. List them so I can
  decide how to handle them.

Step 4 — Rewrite my resume, using only Buckets 1 and 2:
- Summary: 3–4 lines tailored to this role, using the posting's title
  language and my strongest matching proof. No first person.
- Bullets: strong action verb + what I did + measurable result. Mirror
  the posting's exact terms for tools and skills I genuinely have.
- Skills section: the job's matching skills first, grouped the way the
  posting groups them.
- Headings: only Summary, Experience, Education, Skills,
  Certifications.
- Format: single column, no tables, no graphics, consistent dates
  (e.g. Jan 2023 – Present).

Step 5 — Score the new version and show me before/after:
keyword coverage, must-have coverage, and a short list of what changed
and why.

Step 6 — Finish with:
- A suggested file name: Firstname-Lastname-Role
- A LinkedIn headline aligned to this role, using only claims my
  resume supports
- A 3-line recruiter note I can paste with my application, built only
  from facts in my resume

Start with Step 1 now.
```

---

## Tips for a better result

- Paste the **full job description text**, not just the link — job
  boards often block AI tools from opening links.
- If the AI asks which bucket a skill belongs in, answer honestly.
  Bucket 3 gaps handled openly (in a cover note) beat invented claims
  discovered in an interview.
- Run it once per job. A resume tailored to one opening is the point;
  a generic "optimised" resume optimised for nothing is not.
