# Agent-Teams v1 Local Project Checklist

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

- [ ] Requirements written.
- [ ] Acceptance criteria written.
- [ ] UX flow/copy written if UI exists.
- [ ] Architecture written.
- [ ] API/feature contract written.
- [ ] Ownership map written.
- [ ] Preflight needs listed.
- [ ] No app code created unless explicitly scoped.

## Wave 2 — Implementation

- [ ] Preflight run and logged.
- [ ] Implementation stays in owned paths.
- [ ] Contract unchanged or approved change recorded.
- [ ] Dependency policy followed.
- [ ] Build/syntax check run and logged.
- [ ] Implementation report written.
- [ ] No install/download/deploy unless approved.

## Wave 3 — Integration / QA

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
