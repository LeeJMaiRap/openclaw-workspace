# Agent-Teams v1 Local Project Checklist

## Launch Runbook

- [ ] Read `systems/agent-teams/runbooks/new-local-project-launch-runbook.md`.
- [ ] Confirm project fits v1 local-only launch scope.
- [ ] Confirm Wave 2 implementation will wait for user approval.
- [ ] Record stop gates and approval needs.

## Starter Packet Setup

- [ ] Copy `systems/agent-teams/templates/v1-local-project-starter/` into the new project folder.
- [ ] Rename placeholders such as `<project-name>`, `<feature-name>`, `<date>`, and `<owner>`.
- [ ] Complete `reports/starter-dry-run-checklist.md`.
- [ ] Run placeholder cleanup check against filled Wave 1 docs.
- [ ] Keep `app/.gitkeep` as placeholder until implementation is approved.
- [ ] Treat starter packet content as scaffolding, not completed evidence.
- [ ] Read `systems/agent-teams/runbooks/v1-local-project-operating-guide.md` before Wave 1.

## Intake

- [ ] Project name.
- [ ] Local-only goal.
- [ ] User-visible outcome.
- [ ] In scope.
- [ ] Out of scope.
- [ ] Verification Level target.
- [ ] Approval gates.
- [ ] Rollback point.

## Wave 1 — Planning

Starter files:

```text
planning/intake-form.md
planning/requirements.md
planning/acceptance-criteria.md
planning/architecture.md
planning/ownership-map.md
contracts/feature-contract.md
task-packets/wave-1-planning-task.md
reports/starter-dry-run-checklist.md
```

- [ ] Requirements written.
- [ ] Acceptance criteria written.
- [ ] UX flow/copy written if UI exists.
- [ ] Architecture written.
- [ ] API/feature contract written.
- [ ] Ownership map written.
- [ ] Preflight needs listed.
- [ ] Filled Wave 1 docs have no generic starter placeholders.
- [ ] No app code created unless explicitly scoped.

## Wave 2 — Implementation

Do not start Wave 2 until user explicitly approves after Wave 1 review.

Starter files:

```text
task-packets/wave-2-implementation-task.md
reports/implementation-report.md
app/.gitkeep placeholder
```

- [ ] Preflight run and logged.
- [ ] Implementation stays in owned paths.
- [ ] Contract unchanged or approved change recorded.
- [ ] Dependency policy followed.
- [ ] Build/syntax check run and logged.
- [ ] Implementation report written.
- [ ] No install/download/deploy unless approved.

## Wave 3 — Integration / QA

Starter files:

```text
task-packets/wave-3-integration-task.md
reports/integration-report.md
```

- [ ] Local integration tests written.
- [ ] Happy path covered.
- [ ] Negative/error cases covered.
- [ ] UI/HTML path covered if UI exists.
- [ ] Escaping/security-relevant local checks covered if user input exists.
- [ ] Test command run and logged.
- [ ] Build/syntax command run and logged.
- [ ] QA report written.
- [ ] Code review written.
- [ ] Challenge review written.
- [ ] Handoff written.

## Wave 4 — Acceptance

Starter files:

```text
task-packets/wave-4-acceptance-task.md
reports/pm-acceptance-report.md
reports/requirements-traceability-matrix.md
reports/cutover-decision.md
reports/retrospective.md
reports/final-verification-report.md
```

- [ ] PM acceptance report written.
- [ ] Requirements traceability matrix written.
- [ ] Cutover decision written.
- [ ] Retrospective written.
- [ ] Supported claims listed.
- [ ] Unsupported claims listed.
- [ ] Known blockers listed.
- [ ] Next step recommended.

## Claim Boundary Checklist

- [ ] No production-ready claim without production evidence.
- [ ] No deploy claim without deploy evidence.
- [ ] No secure claim without security evidence.
- [ ] No performant claim without performance evidence.
- [ ] No accessible claim without accessibility evidence.
- [ ] No real browser/screenshot/visual claim without browser launch and output evidence.

## Git Checklist

- [ ] `git diff --check` passes.
- [ ] Only scoped files staged.
- [ ] Runtime memory files not staged unless requested.
- [ ] PM daily reports not staged unless requested.
- [ ] Commit message names phase/wave.
- [ ] Push completed.
