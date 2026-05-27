# Audit: awesome-llm-apps

## Source

https://github.com/Shubhamsaboo/awesome-llm-apps

## Purpose

LLM app templates plus `awesome_agent_skills` with general-purpose roles: planner, researcher, coder, writer, analyst.

## Inspected Skills

- `project-planner/SKILL.md`
- `fullstack-developer/SKILL.md`
- `code-reviewer/SKILL.md`
- `debugger/SKILL.md`
- `content-creator/SKILL.md`
- `data-analyst/SKILL.md`

## Useful Candidates

- project-planner → `software/project-planning`
- fullstack-developer → `software/frontend-react`, `software/backend-api`
- code-reviewer + debugger → `software/qa-verification`
- content-creator → `affiliate/content-copywriting`, `affiliate/short-video-script`
- data-analyst → `affiliate/performance-analysis`

## Candidate Agents

- PM Agent
- Product Agent
- Frontend Agent
- Backend Agent
- QA Agent
- Content Copy Agent
- Performance Analyst Agent

## Keep

- Clear trigger descriptions.
- Structured output formats.
- Project planning flow: success criteria, deliverables, task breakdown, dependencies, risks.
- Full-stack flow: React/Next.js, API design, validation, security basics, file structure.
- QA/review flow: security → performance → correctness → maintainability → tests.
- Debug flow: problem, environment, hypotheses, investigation, root cause, fix, prevention.
- Content flow: audience, hook, value, scannability, CTA, platform-specific format.
- Data flow: SQL/pandas/statistics, comments, findings interpretation.

## Reject or Modify

- Do not copy agent persona claims directly (`You are...`) into OpenClaw skills.
- Do not auto-install dependencies from examples.
- Do not treat examples as mandatory stack choices.
- Convert broad fullstack skill into narrower frontend/backend skills.
- Add OpenClaw safety rules and evidence requirements.
- Affiliate content must not auto-post or make unsupported claims.

## Dependencies

- None required for skill usage.
- Optional project dependencies only when implementation task explicitly needs them.

## License

- Source README/SKILL frontmatter reports MIT for inspected skills.

## Risk

- Low for planning/content/data instructions.
- Medium for code examples if copied blindly or dependencies installed without review.

## Decision

Adapt inspected skills into 6 foundation skills first. Status: reviewed-for-adaptation.

## Next Step

Test with two small workflows:

1. software mini app planning/build/review flow;
2. affiliate 7-day campaign plan + content + metric sheet.

## Phase 4 Affiliate Strategy Notes

Inspected `strategy-advisor` and `decision-helper`. Keep situational analysis, option generation, decision criteria, recommendation, roadmap, success metrics, decision matrix, ICE/SWOT. Adapt for affiliate with safety gates.

Decision: adapt `affiliate/affiliate-strategy` to reviewed Paper-level strategy skill for Business PM Agent.
