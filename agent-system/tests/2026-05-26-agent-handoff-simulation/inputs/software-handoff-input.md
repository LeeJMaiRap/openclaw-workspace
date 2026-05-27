# Software Handoff Simulation Input

## Scenario

User asks: "Build MVP internal task board for one-person team. Need requirements, plan, UI/API split, and QA readiness. No implementation yet."

## Constraints

- PM Agent source of truth remains `systems/pm-agent`.
- `agent-system/agents/software/pm-agent` is adapter only.
- Do not modify `systems/pm-agent`.
- Specialist handoff is proposed extension only.
- No dependency install, no deployment, no external service.
- Verification Level: Paper.

## Expected Handoff

```text
Existing PM Agent rules
  -> PM Adapter check
  -> Product Agent PRD
  -> Frontend Agent UI spec
  -> Backend Agent API spec
  -> QA Agent artifact review
  -> PM Adapter acceptance summary
```

## Pass Criteria

- PM Adapter cites existing PM Agent rules.
- Each agent stays in role.
- QA can mark PASS/BLOCKED.
- No runtime claim beyond Paper.
- No modification to `systems/pm-agent`.
