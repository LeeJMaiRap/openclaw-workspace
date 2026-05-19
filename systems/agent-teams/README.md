# Agent-Teams

Agent-Teams is the workspace system for coordinating multiple specialist agents under one PM Orchestrator.

## Goal

Build a practical multi-agent system for real software projects, not only exam/demo projects.

The PM Agent acts as **Orchestrator only**. Specialist agents own specialist work such as requirements, architecture, API contract, frontend, backend, QA, integration, security, performance, DevOps, documentation, and challenge review.

## Directory Map

```text
systems/agent-teams/
├── README.md
├── architecture/   # team design and operating model
├── runtime/        # live protocols used by orchestrator/agents
├── templates/      # task/report/contract templates
├── agents/         # agent specs and prompts
├── skills/         # adapted OpenClaw-native skills
└── references/     # source summaries from external repos/skills
```

## Build Order

1. Phase 0: workspace structure and architecture docs
2. Phase 1: runtime protocols
3. Phase 2: templates
4. Phase 3: reference knowledge summaries
5. Phase 4: PM Orchestrator spec
6. Phase 5: foundation agents
7. Phase 6: execution agents
8. Phase 7: review/production agents
9. Phase 8: OpenClaw demo flow
10. Phase 9: PM Agent refactor, only after approval

## Current Rule

Do not create execution agents or refactor PM Agent until the matching phase is explicitly approved.
