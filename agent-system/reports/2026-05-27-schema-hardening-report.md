# Schema Hardening Report

Date: 2026-05-27 UTC

## Result

PASS.

## Files Added / Updated

```text
agent-system/schemas/agent-skills.schema.json
agent-system/docs/skills-json-schema.md
agent-system/tools/check-consistency.py
```

## Purpose

Formalize expected `skills.json` shape for agent profiles and extend the consistency checker to validate schema presence and profile shape.

## Schema Coverage

Schema supports two profile styles:

1. Normal specialist profile:
   - `agent`
   - `slug`
   - `status`
   - `domain`
   - `primary_skills`
   - optional `supporting_skills`
   - optional `handoff_targets`
   - optional `safety`
   - optional `handoff_protocol`

2. PM Adapter profile:
   - `agent`
   - `canonical_agent`
   - `canonical_identity`
   - `status`
   - `domain`
   - `source_of_truth`
   - `extension_skills.primary`
   - optional `extension_skills.supporting`
   - optional `proposed_handoff_targets`
   - optional `safety`

## Checker Updates

`agent-system/tools/check-consistency.py` now checks:

- `agent-system/schemas/agent-skills.schema.json` exists and parses as JSON.
- Schema has core keys: `$schema`, `title`, `type`, `properties`, `oneOf`.
- Each `skills.json` contains exactly one of:
  - `primary_skills`
  - `extension_skills`
- Normal specialist profiles include `slug`.
- Adapter profile may use `extension_skills` and `canonical_agent`.
- Previous path, handoff, test, stale marker, and Paper-overclaim checks still run.

## Command

```text
python3 agent-system/tools/check-consistency.py
```

## Output

```text
agent-system consistency check
root: /root/.openclaw/workspace/agent-system
agents: 11
tests: 9
failures: 0
warnings: 0
RESULT: PASS
```

## Notes

Full JSON Schema validation is intentionally not dependent on external packages. The checker performs practical in-repo shape validation without requiring `jsonschema` installation.

## Recommended Next Step

Create live read-only validation plan before any live marketplace/web research or campaign movement beyond Paper level.
