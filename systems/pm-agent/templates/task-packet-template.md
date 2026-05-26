# Task Packet Template

Use this template before executing a broad, technical, risky, or evidence-sensitive task.

## Task Identity

- **Task ID:**
- **Title:**
- **Project:**
- **Phase:**
- **Actor / Owner:** human:... / agent:main / worker:... / unknown
- **Requested by:**
- **Date:**

## Objective

What must be accomplished?

## Context

Relevant files, decisions, constraints, prior work, and assumptions.

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

Stop and ask user if:
- scope expands;
- destructive action is needed;
- secret/cloud/DNS/billing/deploy action is needed;
- required tool/dependency is missing and no fallback is approved;
- evidence cannot meet requested Verification Level.

## Expected Output

- Files changed:
- Report required:
- Evidence location:
- Next recommended action:
