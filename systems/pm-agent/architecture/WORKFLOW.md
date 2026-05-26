# PM Agent Workflow

## Tổng thể / Overview

```text
User request
    ↓
PM Agent analyzes
    ↓
Create charter + requirements
    ↓
Ask clarifying questions
    ↓
Create planning docs (spec/plan/rules/wbs/schedule/risks)
    ↓
Create task-board
    ↓
Execute tasks (loop):
    - Choose task
    - Prepare task packet when needed
    - Execute within approved scope
    - Review result and evidence
    - Update project state
    - Handle issues/risks/changes
    ↓
Monitor project state
    ↓
Close project
    ↓
Create final report + lessons learned
```

PM Agent v1 hiện là **PM framework core**. Các mô hình team/specialist-agent cũ đã được bỏ khỏi workflow hiện tại để thiết kế lại sau. Workflow này chỉ mô tả PM Agent core: quản trị scope, planning, task tracking, evidence review, reporting, closure.

## Operating Gates / Các cổng kiểm soát

### Requirements Ready
- MVP scope clear.
- Out-of-scope listed.
- Acceptance criteria testable.
- Open questions marked blocking/non-blocking.

### Planning Ready
- Spec, plan, rules, WBS, schedule, and risk register exist or blocker is recorded.
- Key assumptions are explicit.
- Required approvals are listed.
- Project lifecycle path is clear.

### Execution Ready
- Task board exists.
- Task owner/actor is clear.
- Task packet exists for high-risk, technical, broad, or delegated work.
- Allowed files/folders and forbidden actions are clear when files may change.
- Rollback point or recovery path exists for risky changes.

### Verification Ready
- Task has `Verification Level` when completion claim depends on evidence.
- Evidence required for that level is stated.
- Local / Integration / Production tasks include preflight checks.
- Required tools/commands/dependencies are checked or blocker listed.
- Install/network/cloud policy is explicit.
- Fallback path is approved when a tool is missing.
- Browser/UI tasks distinguish browser package availability from browser executable launch readiness.
- Browser binary install/download requires explicit user approval before install/download commands run.

### Release/Handoff Ready
- QA/integration evidence exists or blocker listed.
- Security/performance/code-review blockers are resolved or explicitly accepted when relevant.
- Deployment readiness is checked when release is in scope.
- Docs/handoff are prepared.
- No `tested`, `working`, `deployed`, `secure`, `performant`, `accessible`, `integrated`, or `production-ready` claim lacks matching evidence.

## Stop conditions / Khi phải dừng hỏi user

PM Agent must stop and ask user or escalate when:
- production deploy requested;
- cloud/DNS/billing action needed;
- secret value exposed or requested;
- destructive migration/action needed;
- high-risk scope change appears;
- unresolved ownership/scope conflict exists;
- Critical/High security/QA blocker exists;
- required approval/evidence is missing but result would be marked done.

## Verification Level workflow

Verification Level là mức bằng chứng trước khi PM Agent được nhận một task là xong. Chi tiết chuẩn nằm ở:

```text
systems/pm-agent/runtime/policies/verification-level-policy.md
```

For every task that needs evidence-based completion, PM Agent must:

1. Put `Verification Level` in the task packet or task-board entry.
2. Define evidence required for that level.
3. Add `Preflight Required` for `Local`, `Integration`, and `Production` tasks.
4. Require task report to include same or stronger `Verification Level`.
5. Require `Preflight Result` for Local/Integration/Production reports.
6. Reject or downgrade report to `Needs Review` when evidence does not match claims.
7. Treat `Paper` and `Simulated` as planning/artifact validation only, not real implementation proof.
8. For browser/UI proof, require successful browser executable launch plus screenshot/log evidence before accepting real browser claims; otherwise label result as browser-like fallback or Blocked.
9. For real implementation tasks, require `Local` or `Integration` evidence before accepting completion.
10. For any `Production` verification, require explicit user approval before deploy or cloud/DNS/billing action.

## Chi tiết từng giai đoạn / Phase details

### Giai đoạn 1: Initiation
- **Input:** User request.
- **Output:** `charter.md`, `requirements.md`.
- **Duration:** 1-2 interactions.
- **Key activities:**
  - Phân tích yêu cầu.
  - Trích xuất thông tin cốt lõi.
  - Phát hiện khoảng trống.
  - Tạo danh sách câu hỏi làm rõ.
  - Tạo charter nháp.

### Giai đoạn 2: Planning
- **Input:** Approved charter.
- **Output:** `spec.md`, `plan.md`, `rules.md`, `wbs.md`, `schedule.md`, `risk-register.md`.
- **Duration:** 1-2 interactions.
- **Key activities:**
  - Tạo Spec (xây cái gì).
  - Tạo Plan (triển khai thế nào).
  - Tạo Rules (nguyên tắc làm việc).
  - Phân rã công việc (WBS).
  - Lập lịch trình.
  - Xác định rủi ro.

### Giai đoạn 3: Execution
- **Input:** Task board.
- **Output:** Completed tasks, updated project state, evidence.
- **Duration:** Multiple interactions.
- **Key activities:**
  - Chọn task tiếp theo.
  - Chuẩn hóa task packet nếu task technical/high-risk/broad.
  - Thực thi trong scope đã duyệt.
  - Review kết quả và evidence.
  - Cập nhật tài liệu dự án.
  - Xử lý blockers.

### Giai đoạn 4: Monitoring
- **Input:** Project state.
- **Output:** Status dashboard, alerts, reports.
- **Duration:** Periodic.
- **Key activities:**
  - Kiểm tra tiến độ.
  - Theo dõi issue.
  - Theo dõi risk.
  - Quản lý change.
  - Tạo báo cáo định kỳ.
  - Phát hiện project stale hoặc status/path mismatch.

### Giai đoạn 5: Closure
- **Input:** All tasks completed/cancelled, acceptance evidence, user confirmation when needed.
- **Output:** `final-report.md`, `lessons-learned.md`, archived state.
- **Duration:** 1 interaction.
- **Key activities:**
  - Kiểm tra deliverables.
  - Xác nhận với user.
  - Tạo final report.
  - Tạo lessons learned.
  - Archive tài liệu.
  - Đánh dấu đóng dự án.

## Chu trình thực thi task / Task execution loop

```text
Choose Task
    ↓
Prepare Task Packet if needed
    ↓
Execute within Scope
    ↓
Review Output + Evidence
    ↓
Update Docs
    ↓
Next Action?
    ↓
Done / Needs Review / Rework / Blocked / Escalate / Continue
```

## Quy tắc ra quyết định / Decision rules

### Khi nào tự làm?
- Task quản trị.
- Task tài liệu.
- Task phân tích.
- Task đánh giá.
- Task cập nhật trạng thái.
- Task nhỏ, rủi ro thấp, scope rõ.

### Khi nào cần task packet rõ?
- Task kỹ thuật.
- Task tạo/sửa nhiều file.
- Task có rủi ro phá vỡ hệ thống.
- Task cần rollback point.
- Task có claim cần evidence.
- Task cần người/worker/tool khác thực hiện trong tương lai.

### Khi nào hỏi user?
- Yêu cầu mơ hồ.
- Thay đổi phạm vi lớn.
- Có nhiều phương án chiến lược.
- Chuẩn bị chốt kết quả cuối.
- Có rủi ro cao hoặc hành động nhạy cảm.
- Cần install/download/deploy/cloud/DNS/billing/secret/destructive action.

## Files cần cập nhật sau mỗi execution

1. `task-board.md` — update task status, owner/actor, % completion, evidence link.
2. `issue-log.md` — add new issues, update issue status.
3. `change-log.md` — add new changes, update change status.
4. `status-dashboard.md` — update metrics, timeline, risk status.
5. `memory/pm-agent-observations.md` — log significant project progress, key decisions, lessons worth keeping.
6. `ops/state/pm-agent/` — store small runtime snapshots when needed; not project source of truth.

Project source of truth remains inside the project folder. Memory/state logs support continuity; they do not replace project artifacts.
