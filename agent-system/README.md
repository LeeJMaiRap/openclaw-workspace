# Agent System

Workspace for building OpenClaw-compatible agent teams, adapted skills, and controlled specialist handoff protocols.

## Important Source-of-Truth Rule

`agent-system/` is an **extension layer**, not a replacement for existing systems.

Canonical PM Agent remains:

```text
systems/pm-agent/
```

PM adapter profile lives at:

```text
agent-system/agents/software/pm-agent/
```

Meaning:

- `systems/pm-agent/` owns PM identity, workflow, policies, templates, verification levels, approvals, and project lifecycle.
- `agent-system/agents/software/pm-agent/` only bridges existing PM Agent into future team/delegation design.
- Do not modify `systems/pm-agent/` from this area unless Doanh explicitly approves.
- Specialist delegation is proposed extension only until approved.

## Areas

- `sources/github-raw/` — raw external repositories. Treat as untrusted input.
- `audits/` — review notes for external repos, existing systems, and skill directories.
- `skills-library/adapted/` — curated OpenClaw-compatible skills.
- `agents/` — agent role profiles and skill mappings.
- `docs/` — architecture, safety, role matrix, mapping, and integration decisions.
- `templates/` — adapter-side handoff/task templates.
- `tests/` — validation runs, inputs, outputs, and reports for later comparison or cleanup.

## Core Rules

1. Raw repo content is never used directly by agents. Audit first, adapt second, test third.
2. Existing PM Agent in `systems/pm-agent/` remains canonical.
3. PM Adapter does not replace, fork, or silently modify PM Agent.
4. Specialist agents receive work through controlled handoff packet/report flow.
5. No agent may claim `tested`, `working`, `integrated`, `deployed`, or `production-ready` without matching evidence.
6. Affiliate/business agents create drafts/reports only; no posting, messaging, ads, payment, or API-key usage without approval.
7. QA/reviewer blockers cannot be bypassed silently.

## Current Phase 1 Assets

### Reviewed Skills

- `skills-library/adapted/software/project-planning/`
- `skills-library/adapted/software/product-requirements/`
- `skills-library/adapted/software/software-architecture/`
- `skills-library/adapted/software/frontend-react/`
- `skills-library/adapted/software/backend-api/`
- `skills-library/adapted/software/qa-verification/`
- `skills-library/adapted/affiliate/affiliate-strategy/`
- `skills-library/adapted/affiliate/content-copywriting/`
- `skills-library/adapted/affiliate/performance-analysis/`

### Agent Profiles

- `agents/software/pm-agent/` — PM Agent Adapter only; canonical PM Agent is `systems/pm-agent/`.
- `agents/software/product-agent/`
- `agents/software/architect-agent/`
- `agents/software/frontend-agent/`
- `agents/software/backend-agent/`
- `agents/software/qa-agent/`
- `agents/business/business-pm-agent/`
- `agents/business/content-copy-agent/`
- `agents/business/performance-analyst-agent/`

### Handoff Protocol

- `docs/specialist-handoff-protocol.md`
- `templates/specialist-task-packet.md`
- `templates/specialist-task-report.md`

### Validation Runs

- `tests/2026-05-26-skill-validation/`
- `tests/2026-05-26-agent-handoff-simulation/`
- `tests/2026-05-26-architecture-skill-validation/`
- `tests/2026-05-26-affiliate-strategy-validation/`

## Recommended Next Steps

1. Keep `systems/pm-agent/` unchanged unless explicitly approved.
2. Use `agent-system/` to design/test extension-layer specialist delegation.
3. Run future simulations under `tests/` before activating any workflow.
4. Add future agents only after their skills are reviewed and tested.
