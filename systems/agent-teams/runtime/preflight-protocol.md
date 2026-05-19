# Preflight Protocol

## Purpose

Catch missing tools, dependencies, permissions, and environment assumptions before real implementation work starts.

Phase 14 found a concrete gap: `npm run build` expected `tsc`, but TypeScript was not installed. Preflight prevents that class of failure from reaching implementation acceptance.

## When Required

Preflight is required before any delegated task with Verification Level:

```text
Local
Integration
Production
```

Preflight is optional for:

```text
Paper
Simulated
```

## PM Orchestrator Responsibilities

Before assigning real implementation work, PM Orchestrator must require a preflight block in the task packet.

PM Orchestrator must verify:

```text
- required commands are named
- required versions are stated when relevant
- dependency install policy is clear
- network policy is clear
- approval needs are clear
- fallback path exists if a tool is missing
```

## Worker Responsibilities

Before editing implementation files, worker must run preflight checks and report result.

Worker must not silently install dependencies, change stack, or bypass missing tools. If a tool is missing, worker must either:

```text
- use an approved dependency-free fallback inside scope, or
- return Blocked / Needs Review with exact missing tool and proposed fix
```

## Required Preflight Fields

Task packet should include:

```md
## Preflight Required

- `<command/tool/version check>`
- `<dependency availability check>`
- `<network/install policy>`
- `<fallback if missing>`
```

Agent report should include:

```md
## Preflight Result

```text
<check>
<result>
```
```

## Standard Checks

For Node/JS tasks:

```text
node -v
npm -v
npm run <script> --if-present
command -v <tool>
```

For test/build tasks:

```text
list package scripts
verify tool command exists
run dry/syntax check if available
```

For browser/UI tasks:

```text
browser tool availability
screenshot path policy
route to inspect
```

For API tasks:

```text
server start command
port/env assumptions
curl or request tool availability
```

## Dependency / Network Policy

Default policy:

```text
- no dependency install unless task explicitly allows it
- no paid service setup
- no cloud/DNS/billing
- no real secrets
- if dependency missing, stop or use documented fallback
```

## Preflight Gate

Pass when:

```text
- all required tools exist, or approved fallback is selected
- required commands are runnable or blockers are documented
- dependency/network policy is followed
- evidence is captured in report
```

Fail / Needs Review when:

```text
- required tool missing and no approved fallback
- install/cloud/secret/deploy needed without approval
- command fails before implementation and root cause is unknown
- worker changes stack without PM/user approval
```

## Evidence Requirements

Preflight evidence can be:

```text
- command output
- version output
- package script listing
- explicit blocker with exact missing command/tool
- documented fallback decision
```

## Example

```text
Check: command -v tsc
Result: missing
Decision: Do not install dependencies. Switch to dependency-free JS + node --check because task allowed no-install fallback.
Status: PASS with fallback
```
