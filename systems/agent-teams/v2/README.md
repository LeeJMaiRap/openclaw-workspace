# Agent-Teams v2

## Purpose

Agent-Teams v2 extends v1 from controlled local pilots toward broader real-project readiness.

v2 does not remove v1 guardrails. It adds stronger gates for dependencies, toolchains, browser evidence, security, performance, multi-agent execution, and production/deploy work.

## v1 Baseline

```text
v1 status: validated for controlled local pilots
v1 tag: agent-teams-v1
v1 report: systems/agent-teams/reports/agent-teams-v1-report.md
v1 overview: systems/agent-teams/reports/agent-teams-overview-report.md
```

## v2 Entry Rule

All v2 work must preserve:

```text
PM Agent remains Orchestrator-only
No silent installs/downloads
No deploy/cloud/DNS/billing/secrets without explicit approval
No browser/screenshot/a11y/visual claim without executable launch evidence
No security/performance claim without specialist evidence
Claims must match verification level and evidence
```

## Roadmap

See:

```text
systems/agent-teams/v2/roadmap.md
systems/agent-teams/v2/dependency-governance/plan.md
systems/agent-teams/v2/dependency-governance/acceptance-criteria.md
```

## Track 1 — Dependency / Toolchain Governance

Phase 51 started Track 1 with a governance plan.

Phase 52 adds reusable dependency approval packet templates:

```text
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-packet-index.md
systems/agent-teams/v2/dependency-governance/templates/dependency-approval-request-template.md
systems/agent-teams/v2/dependency-governance/templates/dependency-risk-review-template.md
systems/agent-teams/v2/dependency-governance/templates/install-provenance-log-template.md
systems/agent-teams/v2/dependency-governance/toolchain-preflight-matrix.md
systems/agent-teams/v2/dependency-governance/lockfile-provenance-policy.md
systems/agent-teams/v2/dependency-governance/starter-runbook-wiring.md
systems/agent-teams/v2/dependency-governance/examples/phase-56-dry-run-dependency-approval/README.md
```

Phase 56 completes Track 1 at docs/simulated level with a dry-run dependency approval simulation. Scope remains docs-only until explicit approval for any install/download.

## Track 2 — Project Type Packs

Phase 57 starts Track 2 with a project type packs plan.

```text
systems/agent-teams/v2/project-type-packs/plan.md
systems/agent-teams/v2/project-type-packs/acceptance-criteria.md
```

Candidate packs: CLI/local-file, HTTP API, Static UI, Fullstack local, Docs-only/project-management.


Phase 65 completes Track 2 at docs/simulated level with a CLI/local-file pack selection dry run.

```text
systems/agent-teams/v2/project-type-packs/examples/phase-65-pack-selection-dry-run/README.md
```

## Track 3 — Security / Performance Evidence Gates

Phase 66 starts Track 3 with a security/performance evidence gates plan.

```text
systems/agent-teams/v2/security-performance-gates/plan.md
systems/agent-teams/v2/security-performance-gates/acceptance-criteria.md
```

Track 3 blocks security/performance claims unless matching specialist evidence, benchmark output, risk severity, and PM acceptance boundaries exist.

## Track 4 — Browser / UI Evidence Recovery

Phase 74 starts Track 4 with a Browser / UI Evidence Recovery plan.

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/plan.md
systems/agent-teams/v2/browser-ui-evidence-recovery/acceptance-criteria.md
```

Track 4 preserves current browser blocker rules: no real browser, screenshot, a11y, or visual claim without executable launch evidence and required artifacts. Browser installs/downloads still require explicit approval through Track 1 governance.

Track 4 is complete at docs/simulated level after Phase 81.

```text
systems/agent-teams/v2/browser-ui-evidence-recovery/track-4-closure-readiness-review.md
```

Real browser proof remains blocked until supported executable and launch/artifact evidence exist.

## Track 5 — Multi-Agent Execution Quality

Phase 82 starts Track 5 with planning for cross-agent evidence indexing, parallel wave readiness, ownership conflict escalation, handoff quality, and PM acceptance visibility.

```text
systems/agent-teams/v2/multi-agent-execution-quality/plan.md
systems/agent-teams/v2/multi-agent-execution-quality/acceptance-criteria.md
```

