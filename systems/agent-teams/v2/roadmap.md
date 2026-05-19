# Agent-Teams v2 Roadmap

## Theme

Move from controlled local pilots toward real-project readiness while keeping v1 evidence discipline.

## Track Order

```text
1. Dependency / Toolchain Governance
2. Project Type Packs
3. Security / Performance Evidence Gates
4. Browser / UI Evidence Recovery
5. Multi-Agent Execution Quality
6. Production / Deploy Gates
```

## Track 1 — Dependency / Toolchain Governance

Goal:

```text
Make installs/downloads explicit, reviewable, repeatable, and evidence-backed.
```

Planned phases:

```text
Phase 51: v2 dependency governance plan — complete
Phase 52: dependency approval packet templates — complete
Phase 53: toolchain preflight matrix — complete
Phase 54: lockfile + provenance policy
Phase 55: starter/runbook wiring
Phase 56: dry-run dependency approval simulation
```

Exit criteria:

```text
PM can approve/reject dependencies from a standardized packet.
Workers cannot silently install dependencies.
Install command, risk, lockfile impact, provenance, and fallback are documented.
Templates exist for request, risk review, and install provenance logging.
Toolchain preflight matrix defines detect commands, approval requirements, fallbacks, and claim boundaries.
```

## Track 2 — Project Type Packs

Goal:

```text
Provide starter add-ons for common project types.
```

Candidate packs:

```text
CLI/local-file pack
HTTP API pack
Static UI pack
Fullstack local pack
Docs-only/project-management pack
```

## Track 3 — Security / Performance Evidence Gates

Goal:

```text
Allow security/performance claims only through dedicated evidence matrices.
```

Outputs:

```text
security minimum evidence matrix
performance benchmark evidence matrix
risk severity rubric
risk acceptance form
security/performance task packets v2
```

## Track 4 — Browser / UI Evidence Recovery

Goal:

```text
Restore real browser proof once executable support exists.
```

Current blocker:

```text
Playwright Chromium install failed on ubuntu26.04-x64.
No browser executable launch evidence exists.
```

## Track 5 — Multi-Agent Execution Quality

Goal:

```text
Improve coordination, ownership clarity, handoff quality, and evidence indexing.
```

Outputs:

```text
cross-agent evidence index
parallel wave readiness v2
ownership conflict escalation v2
handoff quality rubric
PM acceptance dashboard template
```

## Track 6 — Production / Deploy Gates

Goal:

```text
Support production-like work only after explicit approval and stronger gates.
```

Outputs:

```text
deploy approval packet
environment/secrets policy
rollback/backout template
release checklist
post-deploy verification template
production claim policy
```

## Non-Negotiables

```text
No silent installs.
No deploy/cloud/DNS/billing/secrets without explicit approval.
No browser/screenshot/a11y/visual claim without executable launch evidence.
No security/performance claim without specialist evidence.
PM Agent remains Orchestrator-only.
Claims must match verification level and evidence.
```
