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
```

Scope remains docs-only until explicit approval for any install/download.
