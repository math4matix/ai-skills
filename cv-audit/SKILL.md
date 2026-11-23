---
name: cv-audit
description: Audit a CV/résumé the way companies screen applicants (ATS parse check, 10-second recruiter scan, structured scorecard), then produce a 0-100 score, a ranked fix list and, on approval, a rewritten CV. Built for Polish students/interns (praktyki) and juniors in IT and business/finance, candidate's side. Use whenever the user asks to audit, check, review, score, improve or rewrite their CV, or says "sprawdź / oceń / popraw moje CV", attaches a CV (.pdf/.docx) or pastes one, even if they never say "audit". Skip for cover letters, LinkedIn-only profiles and hiring-side ranking of many candidates.
---

# CV audit (screening-grade, candidate side)

Companies do not read a CV first; they filter it. The sequence is: (1) a parser/ATS must read it, (2) knockout criteria remove non-fits, (3) a recruiter spends ~10 seconds deciding "read on or not", (4) only then is it scored against a scorecard. This skill runs the CV through the same sequence, so the candidate finds out where they would be dropped and why.

The score is an estimate from a public-practice rubric, not any company's real score. Say so once in the report.

## Privacy
CV text stays local. Do not web-search, fetch URLs from the CV, or send its contents anywhere. For links, only check that they are well-formed and say what a recruiter would expect behind them.

## Workflow

1. **Get the CV.** For .pdf/.docx run `uv run --with pypdf python <skill>/scripts/extract_text.py <file>` (this is what a parser sees; also try the Read tool to see layout). Pasted text: use as is. If extraction is empty, the PDF is image-only: report that as a fatal ATS failure.
2. **Ask at most two things if missing:** target role/type (e.g. "praktyki, tester QA") and whether a job ad exists. If the user gives no answer, audit against a generic junior-IT/business internship and say so. If an ad exists, extract must-have vs nice-to-have keywords and add a keyword-match table.
3. **Run the stages below.** Detect the CV's language; write the whole report in it (Polish CV → Polish report). Read `references/rubric.md` for scoring anchors and `references/pl-norms.md` for Polish conventions before scoring.
4. **Report** in the format below. Every finding quotes the CV text it is about; a finding without a quote is a guess, so drop it.
5. **Ask follow-ups, then wait.** List the facts needed to fix the weak bullets (numbers, scope, role, tools, links). Offer the rewrite after the user answers.
6. **Rewrite on request.** Use only facts from the CV or the user's answers; unknown numbers become `[liczba]` placeholders. Output in the input's format (.docx in → .docx out; PDF or pasted → .docx; use the docx skill), one page, single column, standard headings. Re-score the rewrite and show before/after.

## Stages (in this order)

- **A. Knockouts (pass/fail, no points).** Readable text layer; name + email + phone; one page; language matches the role; availability dates stated for internships; no obvious contradictions. Any fail goes at the top of the report because it can end the application before scoring.
- **B. ATS parse simulation.** From the extracted text: are section headings standard (Wykształcenie, Doświadczenie, Umiejętności)? Reading order intact? Dates parseable? Anything lost (tables, columns, icons, text in images)? Are keywords spelled the way job ads spell them (e.g. "JavaScript", "SQL", "Git")?
- **C. 10-second scan.** State what a recruiter takes away from the top third: who, what role, strongest proof. If the strongest proof is not visible there, that is the top fix.
- **D. Scorecard** (points in `references/rubric.md`): Content 40, Structure 20, ATS 20, Language 20. Score each sub-criterion with the anchor text, and cite evidence.
- **E. Adjustments** (total at most -15, itemised): Polish legal/format norms, red flags (gaps, vague or unverifiable claims, inconsistency), links & contact quality, visual design.
- **F. Verdict.** 85-100 advance to personal review; 70-84 borderline, fix before sending; below 70 likely filtered. Report the single biggest reason for the verdict.

## Report format

```
# CV audit: <name>, target: <role>
Verdict: <band> · Score: <N>/100  (Content x/40 · Structure x/20 · ATS x/20 · Language x/20 · Adjustments -y)
Knockouts: <pass/fail list>
10-second scan: <what a recruiter sees>
## Top 5 fixes (ranked by points gained)
1. <fix> — "<quote>" — +N pts
## Findings by category   (quote → problem → fix)
## Adjustments           (line items with points)
## Strengths to keep
## Questions I need answered to rewrite
```

Tone: direct but constructive. Say plainly what a recruiter would think, and pair every criticism with the concrete fix. Do not pad with generic advice; if a criterion is fine, say "OK" and move on.

## Hard rules (and why)
- Never invent facts, numbers, employers, or skills. A fabricated bullet gets exposed at interview and the candidate pays for it.
- Do not mention or request protected data (age, marital status, nationality) as an improvement; flag excess personal data as a problem.
- Keep the candidate's real achievements prominent; do not flatten them to fit a template.
