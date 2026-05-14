# Daily Report Cron Runbook

## Purpose
Run the PM Agent 19:00 daily reporting flow via OpenClaw cron.

## Trigger
OpenClaw cron runs an agent turn in an isolated session.

## Event Contract
When the 19:00 cron job runs, the agent should execute this flow in order:
1. Generate or update the framework daily report when framework reporting is relevant.
2. Scan `projects/active/` for projects with `project.yaml` and `status: active`.
3. Skip projects with `status: on-hold`, `stopped`, or `archived`.
4. Generate project daily reports only for eligible active projects.
5. Surface source conflicts in report output instead of silently reconciling them.
6. Export the framework daily report Markdown to PDF.
7. Send the resulting PDF to Telegram with a short caption.

## Source Of Truth
Primary spec:
`systems/pm-agent/reports/plans/cron-flow-19h00-spec-2026-05-14.md`

## Current Default
- Schedule target: 19:00
- Timezone currently configured in cron job: Asia/Ho_Chi_Minh
- Delivery: Telegram announce with framework report PDF
- Recommended enablement: monitor first real scheduled run to confirm PDF generation + delivery remain stable

## Notes
This runbook defines execution intent for the scheduler binding. The cron job message should remain compact but explicit enough to preserve the PDF export + Telegram delivery behavior.
