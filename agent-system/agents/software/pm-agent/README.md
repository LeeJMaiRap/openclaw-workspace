# PM Agent Adapter Profile

Status: adapter-draft

## Important

Canonical PM Agent already exists and remains unchanged:

```text
systems/pm-agent/
```

This folder is only an adapter/profile inside `agent-system` so future team/delegation design can reference PM Agent safely.

## What changed here

Original draft profile was narrowed from “new PM Agent” to “adapter profile”.

It now:

- points to `systems/pm-agent` as source of truth;
- preserves PM Agent identity Lệ;
- references existing workflow, policies, templates;
- marks specialist handoff as proposed extension only;
- keeps reviewed `agent-system` skills as optional aids.

## Audit

See:

```text
agent-system/audits/existing-pm-agent.md
```

## Do Not

- Do not overwrite `systems/pm-agent`.
- Do not treat this adapter as canonical PM Agent.
- Do not activate specialist delegation without approved design.
