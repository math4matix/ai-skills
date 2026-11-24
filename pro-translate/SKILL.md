---
name: pro-translate
description: Professionally translate career documents (CV/résumé, cover letter, recruiting email, LinkedIn text) between Polish and British English, so they read as written natively, and save the result as a new .docx with the original layout kept. Includes ATS/recruiter adaptation to UK conventions and a list of flagged decisions. Use whenever the user asks to translate, "przetłumacz", or localise a CV or job-application document, attaches a .docx/.pdf CV for translation, or says "translate my CV into English", even if they never say "professional". Skip for literary, legal, technical-manual or general-purpose translation, and for auditing a CV (use cv-audit).
---

# Professional translation of career documents (PL <-> UK English)

Goal: a document a UK recruiter would believe was written in English by the candidate, with the original's facts untouched.

## Defaults (confirmed with the user; change only if told)
- Scope: professional documents, both directions PL <-> EN. Target English is **British** (-ise, DD/MM/YYYY or "Mar 2024", "CV", "programme", "organisation").
- Style: **natural**, not literal. Rewrite Polish calques and noun-heavy phrasing into action-verb bullets ("Built", "Led", "Reduced"). Keep tense consistent: past for finished roles, present for the current one.
- Names: on first occurrence, original + translation, e.g. `Politechnika Warszawska (Warsaw University of Technology)`; company names, product names and technologies stay unchanged. Job titles: translate to the nearest UK equivalent, original in brackets only if the title is non-obvious.
- Unclear or untranslatable items (grades, degrees, abbreviations, Polish institutions): choose the best rendering, keep going, and list it in the flag list. Never stop to ask mid-translation.
- Output: a **new .docx** next to the original (never overwrite it), same layout, plus the flag list in chat.
- Extras: ATS/recruiter adaptation to UK norms (below).

## Steps
1. **Read the whole source first.** For .docx extract text with the `docx` skill or `python-docx`/`unzip` of `word/document.xml`; for .pdf use the `pdf` skill. If the file is scanned/unreadable, say so and ask for a text version.
2. **Translate** following the rules below. Do not add, drop or "improve" facts, numbers, dates or technologies. Do not invent metrics.
3. **Rebuild the .docx** by editing the original's text in place, run by run, so fonts, spacing, columns, bullets and links survive. If a run split makes that impractical, replace per paragraph and copy the first run's formatting. Save as `<original name>_EN.docx` (or `_PL.docx`). Do not edit the original.
4. **Check the result**: convert to PDF or render if a tool is available and confirm it still fits the same page count (a CV that spills to an extra page is a defect: tighten wording first, never shrink fonts below 10 pt). Search the output for leftover Polish characters (ąćęłńóśźż) outside proper names.
5. **Report**: path of the new file, then the flag list (below). Keep it short.

## Translation rules
- Polish -> English CV conventions: no "Responsible for"; start bullets with a past-tense verb; one idea per bullet; keep metrics as given (convert `1 200 zł` to `PLN 1,200`, decimal comma to point, `tys.` to `k`).
- Section headings: Profil/Podsumowanie -> Profile; Doświadczenie zawodowe -> Work Experience; Wykształcenie -> Education; Umiejętności -> Skills; Języki -> Languages; Zainteresowania -> Interests; Projekty -> Projects; Certyfikaty -> Certifications; Praktyki/staż -> Internship.
- Education: licencjat -> Bachelor's degree (BSc/BA by field), inżynier -> BEng, magister -> Master's (MSc/MA), studia I/II stopnia -> first/second-cycle studies; Polish grades (np. 4,5) are kept with scale noted, e.g. `4.5/5.0`, and flagged.
- Languages: use CEFR levels (B2, C1) when the source gives them; translate "biegły/komunikatywny" to the closest CEFR level and flag it.
- Dates and phone: `03.2024 - obecnie` -> `Mar 2024 - Present`; phone with `+48`.
- English -> Polish: mirror the logic; formal but not stiff, use rzeczowniki odczasownikowe sparingly, keep tech terms in English when that is how Polish recruiters write them (backend, pull request).

## ATS / recruiter adaptation (UK)
Apply, and mention what was changed:
- Remove or suggest removing: photo, date of birth, PESEL, marital status, home address beyond city, and the Polish GDPR consent clause ("Wyrażam zgodę na przetwarzanie danych...") unless the target employer is Polish. Removal of facts is a suggestion in the flag list; do it in the file only if the user said so.
- Keep a plain single-column text-first layout; no text in images or tables for core content.
- Use standard English headings (above) and the keywords of the target role if the user supplied a job ad; never insert skills the candidate did not list.

## Flag list format (end of reply)
A short table: `Original | Rendered as | Why / what to confirm`. Include: grades/degrees, ambiguous titles, language-level mappings, removed/suggested-removed items, and any wording that changed meaning slightly. If there are none, say "No flags".

## Privacy
Document contents are personal data. Process locally, do not send them to external services, and do not quote them back beyond what the report needs.
