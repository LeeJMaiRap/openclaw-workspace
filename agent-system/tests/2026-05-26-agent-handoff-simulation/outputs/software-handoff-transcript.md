# Software Handoff Transcript Simulation

Verification Level: Paper

No runtime commands, installs, deployment, or edits to `systems/pm-agent`.

---

## 1. Existing PM Agent Rule Check

Canonical PM Agent source:

```text
systems/pm-agent/
```

Rules applied:

- `architecture/SYSTEM-PROMPT.md`: PM Agent manages project through docs, task board, evidence, reports.
- `architecture/WORKFLOW.md`: initiation -> planning -> execution loop -> monitoring -> closure.
- `runtime/policies/verification-level-policy.md`: Paper evidence only proves artifact quality, not working implementation.
- `runtime/policies/approval-policy.md`: scope/plan/change/closure approvals must be logged.
- `templates/task-packet-template.md`: needed before broad/technical/delegated implementation.
- `templates/task-report-template.md`: needed after completion/blocker.

Decision:

```text
Proceed with Paper-level handoff simulation only.
Do not claim tested/working/integrated.
```

---

## 2. PM Agent Adapter Intake

Input:

> Build MVP internal task board for one-person team. Need requirements, plan, UI/API split, and QA readiness. No implementation yet.

Adapter interpretation:

- This is not an implementation task yet.
- Existing PM Agent lifecycle would start with initiation/planning artifacts.
- Specialist handoff is simulated extension only.

Initial status:

```text
Status: Planning Simulation
Verification Level: Paper
External Action: none
Systems PM Agent modified: no
```

Handoff to Product Agent:

```text
Create PRD/MVP scope/user stories/acceptance criteria.
Do not define final implementation stack beyond constraint notes.
```

---

## 3. Product Agent Output Summary

Role respected: Product Agent defines what/why, not implementation details.

PRD summary:

- Product: Tiny internal task board.
- User: one-person team.
- MVP: create/list/update/filter tasks.
- Non-goals: auth, multi-user, deployment, notifications.
- Acceptance criteria:
  - create task with required title;
  - list tasks;
  - update status todo/doing/done;
  - filter by status;
  - reject invalid/empty title.

Handoff to PM Adapter:

```text
Requirements ready at Paper level.
Needs PM planning and specialist spec split.
```

---

## 4. PM Agent Adapter Planning Summary

Using `software/project-planning` as extension aid.

Milestones:

| # | Milestone | Owner | Evidence |
|---|---|---|---|
| 1 | Requirements ready | Product Agent | PRD section |
| 2 | UI/API specs ready | Frontend + Backend Agents | Spec sections |
| 3 | QA review ready | QA Agent | QA report |
| 4 | PM acceptance summary | PM Adapter | Handoff summary |

Task packet requirement for future implementation:

```text
Required before any code changes.
Verification Level must be Local or higher for implementation claim.
Preflight required for Local/Integration/Production.
```

Handoff to Frontend Agent:

```text
Create UI/component/state spec. No code implementation.
```

Handoff to Backend Agent:

```text
Create API contract/spec. No code implementation.
```

---

## 5. Frontend Agent Output Summary

Role respected: Frontend Agent owns UI spec only.

Proposed UI components:

- `TaskForm`
- `TaskFilters`
- `TaskList`
- `TaskCard`

States:

- empty list;
- empty filtered result;
- validation error;
- normal list;
- status changed.

Frontend boundary:

```text
No API contract changes without Backend/PM agreement.
No dependency install.
No working UI claim.
```

Handoff to QA:

```text
Review UI artifact readiness at Paper level.
```

---

## 6. Backend Agent Output Summary

Role respected: Backend Agent owns API/data contract only.

Proposed endpoints:

- `GET /api/tasks?status=todo|doing|done`
- `POST /api/tasks`
- `PATCH /api/tasks/:id/status`

Error contract:

| Status | Code | Meaning |
|---|---|---|
| 400 | VALIDATION_ERROR | Invalid input |
| 404 | TASK_NOT_FOUND | Task id not found |
| 500 | INTERNAL_ERROR | Unexpected failure |

Backend boundary:

```text
No API key/payment/external write.
No storage decision forced.
No working API claim.
```

Handoff to QA:

```text
Review API artifact readiness at Paper level.
```

---

## 7. QA Agent Review

Role respected: QA can block acceptance.

## Critical Issues

None for Paper-level artifact simulation.

## High Priority Issues

1. Persistence decision unresolved.
   - Options: in-memory, localStorage, file, database.
   - Impact: implementation architecture changes.
   - Status: Blocking for implementation, not blocking for planning artifact.

2. No task packet for implementation yet.
   - Required by existing PM Agent rules before code changes.

## Acceptance Status

```text
PASS: Paper-level planning/handoff artifact readiness.
BLOCKED: implementation readiness until persistence decision + task packet + preflight exist.
```

Evidence:

- Input: `inputs/software-handoff-input.md`
- Output: `outputs/software-handoff-transcript.md`
- No runtime test/command.

---

## 8. PM Adapter Acceptance Summary

PM Adapter accepts only this claim:

```text
Paper-level handoff simulation completed.
```

PM Adapter rejects these claims:

```text
tested
working
integrated
production-ready
```

Next action before implementation:

1. Ask Doanh to choose persistence approach.
2. Create PM Agent task packet using `systems/pm-agent/templates/task-packet-template.md`.
3. Define Verification Level: Local.
4. Run preflight before code changes.

Systems PM Agent untouched:

```text
yes
```
