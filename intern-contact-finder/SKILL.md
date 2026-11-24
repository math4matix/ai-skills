---
name: intern-contact-finder
description: Find the right people to contact at a company for an internship or entry-level role - hiring managers, team leads, recruiters - with LinkedIn URLs and likely work emails, ranked by confidence, saved to a CSV, with optional outreach drafts from the user's CV. Works for any field and country (defaults to tech). Use when the user gives a company name and wants to write to a real person instead of a generic info@/jobs@ address, or says "find contacts at <company>" / "znajdź kontakt".
---

# Intern Contact Finder

Goal: for ONE company per run, return 3-6 ranked people the user could email about an internship in the user's field. Ask once for field and target country if not stated (default: IT/software/data; use the user's country).

## Rules
- Use only public sources (web search, company site, public LinkedIn result snippets via search, GitHub, conference pages, Apollo API). Do NOT log in to or scrape LinkedIn directly.
- Never invent an email. Every email gets a `confidence` (verified / pattern-guess / found-public) and a `source`.
- Never send anything. Output is research only.
- Pass only the company name and job titles to external services (search, Apollo), nothing about the user (name, email, CV). The CV is used locally to write drafts only.

## Steps
1. **Input**: company name. If ambiguous (several companies, or local vs. foreign entity), ask once which one. Ask nothing else unless needed.
2. **Domain**: find the official website domain (WebSearch).
3. **Candidate people** (target in this order of priority):
   1. The hiring-side lead of the user's field, e.g. for tech: Engineering Manager / Team Lead / Head of Engineering / Head of Data / CTO (small firms: founder/CEO); for other fields the equivalent department head
   2. Tech recruiter / Talent Acquisition / HR Business Partner (secondary, label as "recruiter")
   3. Alumni-type peers (junior devs, former interns) only if the user asks.
   Include titles in the local language of the target country (e.g. Polish: kierownik zespołu, lider zespołu, dyrektor IT, rekruter IT, specjalista ds. rekrutacji).
   - If `APOLLO_API_KEY` env var is set: use Apollo People API Search (`POST https://api.apollo.io/api/v1/mixed_people/search`, header `x-api-key`, params `q_organization_domains_list[]`, `person_titles[]`, `person_locations[]=<target country>`). Search does not consume credits; email reveal (enrichment) does, so only enrich the top 3. If the API returns a plan/permission error, tell the user and fall back.
   - Otherwise / as a supplement: WebSearch queries like `site:linkedin.com/in "<company>" "engineering manager" <country>`, `"<company>" "tech lead" OR "head of engineering"`, company team/about page, company engineering blog, GitHub org members, conference speaker pages.
4. **Email**:
   - Look for emails already published (team page, blog author pages, GitHub commits on public repos, press releases).
   - Else infer the company's pattern from any one known real address (first.last@, f.last@, firstlast@) and mark `pattern-guess`.
   - If Apollo is available, prefer its revealed email and mark `apollo`.
   - Strip diacritics from names for the address (e.g. Polish ł->l, ą->a, ę->e, ó->o, ś->s, ź/ż->z, ć->c, ń->n).
5. **Rank** by: role relevance to interns (team lead > recruiter > exec in big firms; exec > all in firms under ~50 people), location matches target country, evidence strength.
6. **Output**:
   - Table in chat: name, title, LinkedIn URL, email, confidence, source, why-this-person.
   - Append rows to `./contacts.csv` (create with header if missing): `date,company,domain,name,title,linkedin,email,email_confidence,source,rank,notes,draft` (quote the draft field). Do not duplicate existing name+company rows.
   - End with a one-line suggestion for who to contact first and a note on which emails are guesses.

## CV input and message drafts
Extra input: a CV path (.pdf/.docx/.md) or pasted text. Ask for it once if not given; reuse it for later runs in the session. If no CV, skip drafting and say so.
1. Read the CV; extract: name, field, 2-3 strongest projects/skills, languages, availability/dates if stated. Use only facts in the CV, never invent experience.
2. For each contact in the final table, write ONE draft matched to the channel:
   - **Email** (if an email exists): subject + body, 90-120 words.
   - **LinkedIn DM / connection note** (if only a profile): max 300 characters.
   - **Facebook Messenger**: only if the user asks for it or the contact's public page is clearly the professional channel; otherwise prefer LinkedIn/email and say why (it feels intrusive to cold-contact on a personal social account).
3. Tailor by role: to a team lead, lead with one relevant skill/project matched to the team's stack (look at the company's job posts, blog or GitHub); to a recruiter, lead with availability, field and what you're looking for.
4. Language: The language of the company's country, formal register, no emoji (Polish example: "Dzień dobry Panie/Pani ...", "CV w załączniku"); English otherwise. Mention the CV attachment.
5. Structure: who I am (1 line) -> why this company/team (1 specific line, from real research) -> one concrete proof from the CV -> clear small ask (a short call or pointing me to the right person) -> thanks.
6. Output drafts under each contact in chat and add a `draft` column to `contacts.csv`. Mark placeholders like `[X]` for anything unknown; never send.

## Apollo setup guide (give this when the user asks or no key is set)
1. Create a free account at apollo.io with a company-style or personal email.
2. Settings > Integrations > API (or "API Keys") > Create new key. Enable the People Search and Enrichment endpoints if asked.
3. Put it in the shell profile: `export APOLLO_API_KEY="..."` then restart the terminal/Claude Code. Never paste the key into chat or commit it.
4. Test: `curl -s -X POST https://api.apollo.io/api/v1/mixed_people/search -H "x-api-key: $APOLLO_API_KEY" -H "Content-Type: application/json" -d '{"q_organization_domains_list":["example.com"],"per_page":1}'`
5. Caveat: free plans have a small monthly credit allowance for emails, and API access to some endpoints can be restricted on free plans. If a call is refused, the skill still works with web search + pattern inference.

## Caveats to tell the user
- Pattern-guessed emails can bounce; suggest sending the first one from a normal address and watching for bounces.
- Cold email to a work address is generally fine for a one-to-one personal internship inquiry in many countries (e.g. Poland), but check local rules, keep it short, personal and offer an easy opt-out.
