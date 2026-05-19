# PM Agent Skills

Bộ skill lõi cho PM Agent, chia thành 4 nhóm chức năng.

## Cấu trúc

- `input-normalization/` - Chuẩn hóa đầu vào thô
- `document-generation/` - Sinh tài liệu PM chuẩn
- `project-operations/` - Vận hành và cập nhật dự án
- `infrastructure/` - Hạ tầng và xuất bản

## Danh sách skill

Xem từng thư mục con để biết chi tiết.

## Agent-Teams Specialist Skills

PM Agent skills in this folder are PM/core operations: input normalization, document generation, project operations, infrastructure/reporting.

For multi-role technical projects, PM Agent should route specialist work to Agent-Teams instead of doing it directly.

References:

```text
systems/agent-teams/agents/**
systems/agent-teams/skills/**
systems/agent-teams/runtime/**
systems/agent-teams/examples/orchestrator-demo-runbook.md
```

Routing rule:

```text
PM/core work -> systems/pm-agent/skills/**
Specialist execution/review work -> systems/agent-teams/agents/** + systems/agent-teams/skills/**
```

PM Agent remains PM Orchestrator / Team Lead. It owns delegation, gates, acceptance, reporting, and user approvals. It should not directly own frontend/backend/QA/security/performance/devops/docs specialist deliverables unless explicitly assigned as fallback.

Contract-first rule:

```text
Do not start parallel Frontend/Backend work until requirements, architecture direction, API contract, and ownership map exist.
```
