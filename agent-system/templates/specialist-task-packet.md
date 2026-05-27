# Specialist Task Packet

Derived from canonical PM Agent template:

```text
systems/pm-agent/templates/task-packet-template.md
```

## Task Identity

- **Task ID:**
- **Title:**
- **Project:**
- **Phase:**
- **Assigned by:** agent:main / human:Doanh / unknown
- **Assigned to:** Product Agent / Frontend Agent / Backend Agent / QA Agent / Content Copy Agent / Performance Analyst Agent / other
- **Requested by:**
- **Date:**

## Canonical PM References

- **PM Source:** `systems/pm-agent/`
- **Workflow:** `systems/pm-agent/architecture/WORKFLOW.md`
- **Verification Policy:** `systems/pm-agent/runtime/policies/verification-level-policy.md`
- **Approval Policy:** `systems/pm-agent/runtime/policies/approval-policy.md`
- **Actor Policy:** `systems/pm-agent/runtime/policies/actor-tracking-policy.md`

## Objective

What must specialist accomplish?

## Context

Relevant files, decisions, constraints, prior work, assumptions, and upstream handoff notes.

## Role Boundary

Specialist must do:

```text
- ...
```

Specialist must not do:

```text
- ...
```

## Scope

### Allowed files/folders

```text
- path/to/allowed
```

### Forbidden actions

```text
- no production deploy
- no secret exposure
- no destructive migration
- no dependency install without approval
- no external posting/messaging/ads/payment/API write without approval
```

## Requirements

- Functional requirements:
- Non-functional requirements:
- Acceptance criteria:

## Verification

- **Verification Level:** Paper / Simulated / Local / Integration / Production
- **Evidence Required:** command output / test result / screenshot / API output / log path / checklist / blocker
- **Preflight Required:** yes/no
- **Preflight Checks:**
  - required tools/commands:
  - dependencies:
  - network/install policy:
  - credentials/secrets policy:

## Rollback / Recovery

- **Rollback point:**
- **Recovery steps:**
- **Files to restore if failed:**

## Stop Conditions

Stop and escalate if:

- scope expands;
- forbidden action becomes necessary;
- required tool/dependency is missing and no fallback is approved;
- evidence cannot meet requested Verification Level;
- role boundary conflict appears;
- PM source-of-truth conflict appears.

## Expected Output

- Files changed:
- Report required:
- Evidence location:
- Next recommended action:
