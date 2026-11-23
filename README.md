# ai-skills

A collection of reusable [Claude Code](https://claude.com/claude-code) skills.

## Skills

| Skill | What it does |
|---|---|
| [`cv-audit`](cv-audit/) | Audits a CV/résumé like a company screen (ATS parse check, 10-second recruiter scan, scorecard), gives a 0-100 score and a ranked fix list, and rewrites the CV on approval. Aimed at Polish students/interns and juniors in IT and business. |

## Install

Copy a skill folder into your skills directory:

```bash
# all projects
cp -R cv-audit ~/.claude/skills/

# one project
cp -R cv-audit <project>/.claude/skills/
```

Claude Code picks the skill up automatically when a request matches its `description`.

## Layout

Each skill is a folder with a `SKILL.md` (required), plus optional `references/`, `scripts/` and `evals/`.

## Contributing

Issues and pull requests are welcome. Keep skills free of personal data.
