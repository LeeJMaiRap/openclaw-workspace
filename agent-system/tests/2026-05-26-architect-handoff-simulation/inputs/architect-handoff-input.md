# Architect Handoff Simulation Input

## Scenario

User wants a tiny internal task board MVP. Need to verify new Architect Agent fits between Product and implementation specialists.

## Constraints

- Existing PM Agent in `systems/pm-agent` remains canonical.
- PM Adapter only bridges handoff.
- Verification Level: Paper.
- No implementation.
- No install/deploy/cloud/secrets.

## Expected Flow

```text
PM Adapter
  -> Product Agent: PRD/MVP scope
  -> Architect Agent: architecture brief/ADRs/boundaries
  -> Frontend Agent: UI spec based on architecture
  -> Backend Agent: API/data spec based on architecture
  -> QA Agent: artifact review and blocker status
  -> PM Adapter: acceptance summary
```

## Pass Criteria

- Architect Agent does not replace Product/Frontend/Backend/QA.
- Architect adds module boundaries and ADRs.
- Frontend/Backend use architecture as constraint.
- QA can block implementation readiness.
- PM Adapter does not claim working/tested.
