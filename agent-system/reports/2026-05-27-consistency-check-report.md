# Consistency Check Report

Date: 2026-05-27 UTC

## Result

PASS.

## Tool

```text
agent-system/tools/check-consistency.py
```

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

## Checks Covered

- Required root docs/templates exist.
- Every agent folder has:
  - `AGENT.md`
  - `README.md`
  - `skills.json`
- All `skills.json` files parse as valid JSON.
- Required JSON keys exist.
- `primary_skills` / `supporting_skills` paths exist.
- PM Adapter `extension_skills` paths exist.
- Specialist `handoff_protocol` paths exist.
- Every test folder has:
  - `README.md`
  - `test-report.md`
- No stale future markers for activated Market Research / Product Hunter agents in active docs/agent profiles.
- Paper-level test artifacts scanned for likely overclaim wording.

## Notes

Initial script run found expected tuning issues:

- PM Adapter uses `extension_skills` and canonical PM source-of-truth fields instead of normal specialist `primary_skills` schema.
- Stale marker scan initially included historical hardening report examples.
- Paper overclaim scan initially flagged negative/prohibited examples such as “do not claim working”.

Script was adjusted to:

- support PM Adapter schema;
- scan stale markers only in active docs/agent profiles;
- ignore negative/prohibited wording contexts;
- ignore fenced code blocks/headings for Paper overclaim scan.

Final run passed with zero failures and zero warnings.

## Recommended Next Step

Create `agent-system/docs/activation-guide.md` so PM Agent / Business PM can decide when and how to use each specialist agent.
