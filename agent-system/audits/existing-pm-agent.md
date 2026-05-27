# Audit: Existing PM Agent in `systems/pm-agent`

## Source of Truth

`systems/pm-agent/` is the canonical PM Agent framework. It must remain unchanged unless Doanh explicitly approves.

Primary files inspected:

- `systems/pm-agent/README.md`
- `systems/pm-agent/STATUS.md`
- `systems/pm-agent/architecture/SYSTEM-PROMPT.md`
- `systems/pm-agent/architecture/WORKFLOW.md`
- `systems/pm-agent/runtime/policies/approval-policy.md`
- `systems/pm-agent/runtime/policies/verification-level-policy.md`
- `systems/pm-agent/skills/README.md`
- `agent-system/agents/software/pm-agent/AGENT.md` draft profile

## Existing PM Agent Summary

PM Agent (Lệ) is a mature PM framework on OpenClaw. It manages projects through documents, task boards, policies, evidence, approvals, reports, and closure.

Core responsibilities:

1. Receive project requests.
2. Analyze and normalize requirements.
3. Create PM artifacts.
4. Split tasks and track task board.
5. Review evidence before accepting done claims.
6. Monitor progress, risk, issue, and change.
7. Produce final report and lessons learned.

## Current Status

From `STATUS.md`:

- PM Agent is in framework core hardening after workspace cleanup.
- Core readiness: ~85-90%.
- Controlled pilot readiness: ~80-85%.
- Production-grade readiness: not complete.
- Old team/specialist-agent branch was removed from active workflow.
- Rebuilt team/delegation system is future design.

## Non-negotiable Rules from Existing PM Agent

- Do not mix PM Agent framework state with managed project state.
- Project source of truth lives in `projects/active/[project-name]/`.
- PM Agent must use verification levels before accepting claims.
- Do not claim `tested`, `working`, `secure`, `performant`, `accessible`, `integrated`, `deployed`, or `production-ready` without matching evidence.
- Paper/Simulated evidence cannot prove runtime working status.
- Local/Integration/Production tasks need preflight.
- Deploy/cloud/DNS/billing/secret/destructive actions require human approval.
- Browser binary install/download requires explicit approval.
- Task packet required for broad, technical, risky, delegated, or evidence-sensitive tasks.
- Task report required after completion/blocker.
- QA/security Critical/High blocker must stop/escalate.

## Existing Workflow

```text
User request
  -> PM Agent analyzes
  -> charter + requirements
  -> clarification if needed
  -> planning docs: spec/plan/rules/wbs/schedule/risks
  -> task-board
  -> execution loop:
       choose task
       prepare task packet when needed
       execute within approved scope
       review evidence
       update project state
       handle issues/risks/changes
  -> monitor
  -> closure
  -> final report + lessons learned
```

## Comparison: Existing PM Agent vs Draft Profile

| Area | Existing PM Agent | Draft `agent-system` PM Profile | Decision |
|---|---|---|---|
| Identity | Lệ, mature PM framework | Generic PM Agent | Use existing identity/reference |
| Scope | Full PM lifecycle | Software delivery orchestrator | Keep existing broader lifecycle; add software-team bridge only as extension |
| Team delegation | Old specialist branch removed; future design | Direct handoff to Product/Frontend/Backend/QA | Mark draft handoff as proposed extension, not canonical active workflow |
| Evidence | Strong verification-level policy | Generic evidence checklist | Replace with existing verification policy references |
| Approval | Formal approval policy | Basic approval mention | Reference existing approval policy |
| Task packet/report | Formal templates | Not explicit enough | Add task packet/report requirements |
| Source of truth | `systems/pm-agent` and `projects/active/...` | `agent-system/...` | Existing PM Agent remains source of truth |
| Runtime readiness | Controlled pilot ready, not production | Draft profile | Draft must be adapter only |

## Keep from Existing PM Agent

- Identity/name: Lệ.
- Full lifecycle workflow.
- Verification Level Policy.
- Approval Policy.
- Task packet/report templates.
- Project source-of-truth structure.
- Separation between framework status and project status.
- Stop conditions.
- Controlled automation with human gates.

## Keep from Draft Profile

- Clear future specialist handoff targets:
  - Product Agent
  - Frontend Agent
  - Backend Agent
  - QA Agent
- Clear reminder that PM Agent should orchestrate instead of doing specialist implementation.
- Skills mapping to project-planning/product-requirements/qa-verification as extension references.

## Conflicts

1. Draft implies specialist handoff flow is active.
   - Existing PM Agent says old team/specialist branch is removed and rebuilt team/delegation is future design.
   - Resolution: mark specialist handoff as proposed extension/adapter only.

2. Draft is too narrow as software delivery PM only.
   - Existing PM Agent handles full project framework.
   - Resolution: draft profile should become `PM Agent Adapter for agent-system`, not replacement.

3. Draft lacks formal verification/approval details.
   - Resolution: reference existing PM Agent policies directly.

## Controlled Merge / Adapt Plan

Do not modify `systems/pm-agent`.

Adapt only:

- `agent-system/agents/software/pm-agent/AGENT.md`
- `agent-system/agents/software/pm-agent/skills.json`
- `agent-system/agents/software/pm-agent/README.md`
- docs/audit references inside `agent-system/`

New role for draft profile:

```text
PM Agent Adapter Profile
```

Meaning:

- It points to existing PM Agent as canonical source.
- It maps reviewed `agent-system` skills as optional extension aids.
- It does not replace Lệ.
- It does not activate specialist delegation by itself.
- It supports future team/delegation rebuild after approval.

## Recommendation

Proceed with controlled adaptation of draft PM profile into an adapter that references `systems/pm-agent` source-of-truth and preserves original PM Agent unchanged.
