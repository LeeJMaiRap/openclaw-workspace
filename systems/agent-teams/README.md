# Agent-Teams

Agent-Teams is the workspace system for coordinating multiple specialist agents under one PM Orchestrator.

## Goal

Build a practical multi-agent system for real software projects, not only exam/demo projects.

The PM Agent acts as **Orchestrator only**. Specialist agents own specialist work such as requirements, architecture, API contract, frontend, backend, QA, integration, security, performance, DevOps, documentation, and challenge review.

## Quick Start — New Local Project

Use this path when starting a new controlled local project:

1. Read `runbooks/v1-local-project-operating-guide.md`.
2. Copy `runbooks/v1-local-project-checklist.md` into the project planning folder or use it as the phase checklist.
3. Run Wave 1 first: requirements, acceptance criteria, UX/architecture, API/feature contract, ownership map.
4. Run Wave 2 only after Wave 1 is accepted: implementation in owned paths only.
5. Run Wave 3: local integration tests, QA, code review, challenge review, handoff.
6. Run Wave 4: PM acceptance, traceability matrix, cutover decision, retrospective.

Default guardrails:

```text
local-only
contract-first
preflight before Local/Integration/Production
no silent dependency install
no deploy/cloud/DNS/billing/secrets without explicit approval
no real browser/screenshot/a11y/visual claim without executable launch evidence
```

## Primary v1 Runbooks

- `runbooks/v1-local-project-operating-guide.md` — canonical v1 flow for controlled local projects.
- `runbooks/v1-local-project-checklist.md` — checklist for intake, Waves 1-4, claim boundaries, and git hygiene.

## Directory Map

```text
systems/agent-teams/
├── README.md
├── architecture/   # team design and operating model
├── runtime/        # live protocols used by orchestrator/agents
├── templates/      # task/report/contract templates
├── agents/         # agent specs and prompts
├── skills/         # adapted OpenClaw-native skills
├── runbooks/       # reusable operating guides and checklists
├── examples/       # demos, pilots, validation reports
└── references/     # source summaries from external repos/skills
```

## Build Order

1. Phase 0: workspace structure and architecture docs
2. Phase 1: runtime protocols
3. Phase 2: templates
4. Phase 3: reference knowledge summaries
5. Phase 4: PM Orchestrator spec
6. Phase 5: foundation agents
7. Phase 6: execution agents
8. Phase 7: review/production agents
9. Phase 8: OpenClaw demo flow
10. Phase 9: PM Agent alignment
11. Phase 10-30: pilot runbooks, preflight/browser/readiness hardening
12. Phase 31-35: accepted `mini-issue-tracker-v1` clean-slate local pilot
13. Phase 36: v1 local project operating guide
14. Phase 37: README/index quick-start wiring

## Current Rule

For new real work, start from the v1 local project runbooks and keep PM Agent as orchestrator-only. Do not claim Production, real browser, screenshot, accessibility, visual regression, security, or performance proof unless matching evidence exists.
