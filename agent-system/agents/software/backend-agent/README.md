# Backend Agent

Status: draft profile

This profile belongs to Phase 1 agent-system mapping.

## Purpose

Owns API contracts, validation, service logic, auth/permission boundaries, data model implications, and backend tests.

## Skill Map

See `skills.json`.

## Typical Flow

1. Receive input from human, PM, or upstream agent.
2. Load primary skill instructions.
3. Produce assigned output only.
4. Send blockers/handoff notes to next owner.

## Cleanup / Evolution

This profile can be edited or replaced after validation runs in `agent-system/tests/`.
