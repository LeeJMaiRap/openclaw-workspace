# Daily Report Cron Runbook

## Purpose
Run the PM Agent 19:00 daily reporting flow via OpenClaw cron.

## Trigger
OpenClaw cron emits a system event to the main session.

## Event Contract
If the system event text contains:
`PM_AGENT_DAILY_REPORT_19H00`

then the agent should execute this flow in order:
1. Generate or update the framework daily report when framework reporting is relevant.
2. Scan `projects/active/` for projects with `project.yaml` and `status: active`.
3. Skip projects with `status: on-hold`, `stopped`, or `archived`.
4. Generate project daily reports only for eligible active projects.
5. Surface source conflicts in report output instead of silently reconciling them.
6. Default notify policy: write files only, no chat delivery unless explicitly requested.

## Source Of Truth
Primary spec:
`systems/pm-agent/reports/plans/cron-flow-19h00-spec-2026-05-14.md`

## Current Default
- Schedule target: 19:00
- Timezone currently configured in cron job: UTC
- Delivery: none
- Recommended enablement: only after confirming active-project set and owner preference for framework daily snapshots

## Notes
This runbook defines execution intent for the scheduler binding. The cron job itself should stay simple and only carry the event contract string.
