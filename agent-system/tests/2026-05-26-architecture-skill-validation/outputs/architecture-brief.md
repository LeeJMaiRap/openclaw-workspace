# Architecture Brief: Tiny Internal Task Board MVP

## Context

A one-person internal task board needs local/demo-ready planning for create/list/update/filter tasks. Implementation not requested yet.

## Goals

- Keep architecture small and reversible.
- Separate UI, task domain model, API contract, and storage decision.
- Make future implementation easy for Frontend/Backend/QA agents.
- Avoid production claims.

## Non-goals

- No auth.
- No multi-user collaboration.
- No deployment.
- No notifications.
- No external integrations.

## Assumptions

- MVP can begin as frontend-only local state or localStorage.
- API contract is useful for future backend but not mandatory for first demo.
- Persistence decision remains open.

## Constraints

- Next.js + TypeScript style preferred.
- No dependency install.
- Verification Level: Paper.

## Recommended Architecture

Use modular monolith / single Next.js app shape for MVP:

```text
User
  -> Task Board UI
  -> Task domain module
  -> optional API route layer
  -> storage adapter: in-memory/localStorage now, DB later
```

Recommended first implementation path:

```text
Phase A: frontend-only local state prototype
Phase B: localStorage persistence if refresh persistence needed
Phase C: API + database only if multi-session/multi-device needed
```

## System Context

```text
human user
  -> browser UI
  -> Next.js page/components
  -> task service/domain functions
  -> storage adapter
```

## Module Boundaries

| Module | Owns | Does Not Own | Notes |
|---|---|---|---|
| UI components | form, filters, list, card, visual states | persistence rules | Frontend Agent |
| Task domain | task type, status transition, validation rules | rendering | Architect/Backend shared contract |
| API layer | request/response/error contract | UI layout | Backend Agent if backend phase approved |
| Storage adapter | local state/localStorage/DB implementation | product scope | decision pending |
| QA specs | acceptance checks, regression cases | feature scope | QA Agent |

## Data Model

```ts
type TaskStatus = 'todo' | 'doing' | 'done';
type TaskPriority = 'low' | 'medium' | 'high';

type Task = {
  id: string;
  title: string;
  description?: string;
  status: TaskStatus;
  priority: TaskPriority;
  createdAt: string;
  updatedAt: string;
};
```

Validation:

- `title` required.
- `status` must be todo/doing/done.
- `priority` must be low/medium/high.

## API / Contract Notes

If backend API is approved later:

| Method | Path | Purpose |
|---|---|---|
| GET | `/api/tasks?status=` | list/filter tasks |
| POST | `/api/tasks` | create task |
| PATCH | `/api/tasks/:id/status` | update status |

Errors:

| Status | Code | Meaning |
|---|---|---|
| 400 | VALIDATION_ERROR | invalid input |
| 404 | TASK_NOT_FOUND | missing task |
| 500 | INTERNAL_ERROR | unexpected failure |

## Quality Attributes

| Attribute | Requirement | Design Response | Evidence Needed |
|---|---|---|---|
| Simplicity | small MVP | frontend-first, storage adapter | code review after implementation |
| Maintainability | clear boundaries | typed Task model + modules | lint/typecheck later |
| Reliability | no invalid status/title | validation rules | unit/manual tests later |
| Performance | tiny data set | client filtering acceptable | not needed until data grows |
| Security | no auth, local demo | no external exposure | production review if deployed |

## ADRs

### ADR-001: Use modular monolith / single app shape

- Status: Proposed
- Context: MVP small, local demo acceptable.
- Decision: Use one Next.js-style app with separated UI/domain/storage modules.
- Alternatives: separate frontend/backend repos; full DB-first API.
- Consequences: faster MVP, easier refactor later, not production-ready by default.

### ADR-002: Defer durable backend persistence

- Status: Proposed
- Context: persistence requirement unresolved.
- Decision: Start with local state/localStorage path; define API contract for later.
- Alternatives: DB immediately.
- Consequences: avoids overbuild; refresh/multi-device persistence remains limited until later phase.

## Risks and Mitigations

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| Persistence expectation unclear | High | ask Doanh before implementation | PM Adapter |
| API over-engineering | Medium | frontend-first phase | Architect Agent |
| Scope creep into PM platform | High | keep non-goals explicit | PM Adapter |
| Unsupported working claim | High | keep Verification Level Paper | QA Agent |

## Specialist Handoff

### Frontend Agent

- Build `TaskForm`, `TaskFilters`, `TaskList`, `TaskCard` only after task packet.
- Use Task type and validation rules.
- Handle empty/error/normal states.

### Backend Agent

- Do not implement backend unless persistence/API phase approved.
- If approved, use API contract above and validation at boundary.

### QA Agent

- Paper review now.
- Local verification later requires actual implementation and command/manual evidence.
- Block any `working/tested` claim until evidence exists.

## Verification

- Verification Level: Paper
- Evidence Provided: this architecture brief
- Evidence Missing: no implementation, no commands, no local runtime proof

## Open Questions

1. Should tasks persist after page refresh?
2. Should first implementation be frontend-only or API-backed?
3. Should UI be list or kanban board?
