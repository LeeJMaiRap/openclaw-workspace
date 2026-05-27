# Agent Skills JSON Schema

Status: draft
Date: 2026-05-27 UTC

## Purpose

Define expected shape for each agent profile's `skills.json` mapping.

Schema file:

```text
agent-system/schemas/agent-skills.schema.json
```

Consistency checker:

```text
agent-system/tools/check-consistency.py
```

## Normal Specialist Profile

Most specialist agents use:

```json
{
  "agent": "Frontend Agent",
  "slug": "frontend-agent",
  "status": "draft",
  "domain": "software",
  "primary_skills": [
    "../../../skills-library/adapted/software/frontend-react/SKILL.md"
  ],
  "supporting_skills": [],
  "handoff_targets": [],
  "safety": {},
  "handoff_protocol": {
    "protocol": "../../../docs/specialist-handoff-protocol.md",
    "task_packet_template": "../../../templates/specialist-task-packet.md",
    "task_report_template": "../../../templates/specialist-task-report.md",
    "canonical_pm_agent": "../../../systems/pm-agent",
    "requires_task_packet": true,
    "requires_task_report": true,
    "respect_verification_levels": true,
    "respect_role_boundaries": true
  }
}
```

Required for normal profiles:

- `agent`
- `slug`
- `status`
- `domain`
- `primary_skills`
- `handoff_protocol` for specialist handoffs

## PM Adapter Profile

PM Adapter is special because canonical PM Agent remains in:

```text
systems/pm-agent/
```

PM Adapter may use:

```json
{
  "agent": "PM Agent Adapter Profile",
  "canonical_agent": "systems/pm-agent",
  "canonical_identity": "Lệ",
  "status": "adapter-draft",
  "domain": "software",
  "source_of_truth": [],
  "extension_skills": {
    "primary": [],
    "supporting": []
  },
  "proposed_handoff_targets": [],
  "safety": {}
}
```

Required for adapter-style profile:

- `agent`
- `status`
- `domain`
- `extension_skills.primary`

## Path Rules

All paths inside `skills.json` are relative to the agent profile folder.

Examples:

```text
../../../skills-library/adapted/software/frontend-react/SKILL.md
../../../docs/specialist-handoff-protocol.md
../../../templates/specialist-task-packet.md
../../../templates/specialist-task-report.md
```

The consistency checker resolves these paths and fails when target files are missing.

## Safety Rules

Use booleans in `safety` for important guardrails:

```json
{
  "external_actions_require_approval": true,
  "respect_role_boundaries": true,
  "report_blockers_explicitly": true
}
```

Business/affiliate agents should include relevant no-external-action flags:

```json
{
  "draft_only": true,
  "no_posting": true,
  "no_messaging": true,
  "no_ads": true,
  "no_payment_or_api_keys": true,
  "no_fake_claims": true
}
```

## Validation

Run:

```text
python3 agent-system/tools/check-consistency.py
```

Expected current result:

```text
failures: 0
warnings: 0
RESULT: PASS
```

## Notes

This schema is intentionally permissive with `additionalProperties: true` so agent-specific metadata can evolve without breaking old profiles.

The checker enforces practical repo consistency beyond schema shape:

- referenced paths exist;
- agent files exist;
- tests have reports;
- stale future markers do not remain in active docs/profiles;
- Paper-level artifacts avoid likely overclaims.
