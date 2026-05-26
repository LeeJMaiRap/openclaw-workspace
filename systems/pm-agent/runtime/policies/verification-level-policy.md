# Verification Level Policy

## Purpose / Mục đích

Verification Level xác định mức bằng chứng cần có trước khi PM Agent được nhận một task, deliverable, hoặc project state là xong.

Policy này ngăn claim quá mức như `tested`, `working`, `deployed`, `secure`, `performant`, `accessible`, `integrated`, hoặc `production-ready` khi chưa có evidence tương ứng.

## Levels / Các mức xác minh

| Level | Meaning | Minimum evidence | Allowed claim | Not allowed claim |
|---|---|---|---|---|
| Paper | Review trên tài liệu/logic, không chạy runtime | doc diff, checklist, reasoning notes | drafted, reviewed conceptually | tested, working, deployed |
| Simulated | Dry-run, mock, hoặc mô phỏng, chưa chứng minh runtime thật | simulated output, mock result, dry-run notes | simulated, expected behavior | real working, integration tested |
| Local | Chạy thật trong môi trường local/dev | command output, test result, local log, screenshot nếu UI | local tested, local working | production-ready, deployed |
| Integration | Nhiều phần đã tích hợp và được kiểm chứng cùng nhau | integration test output, API/UI flow evidence, service logs | integration tested | production-ready nếu chưa deploy/approve |
| Production | Môi trường production/staging approved được xác minh | approval record, deploy log, health check, monitoring evidence | deployed, production verified | any production claim without approval/evidence |

## Required fields

Task packet hoặc task-board entry phải ghi:

```text
Verification Level:
Evidence Required:
Preflight Required: yes/no
Stop Conditions:
Rollback Notes:
```

Task report phải ghi:

```text
Verification Level Achieved:
Evidence Provided:
Preflight Result: required for Local/Integration/Production
Blockers:
Residual Risks:
```

## Preflight rule

`Local`, `Integration`, và `Production` tasks phải có preflight trước khi bắt đầu implementation hoặc verification.

Preflight phải kiểm tra:
- required commands/tools/versions;
- dependency availability;
- install/network policy;
- credentials/secrets policy;
- fallback path hoặc blocker nếu tool thiếu;
- rollback/recovery path nếu thay đổi rủi ro.

Nếu preflight fail và không có fallback được duyệt, task status phải là `Blocked` hoặc `Needs Review`.

## Browser/UI evidence rule

Browser/UI proof phải phân biệt:
- browser package available;
- browser executable available;
- browser launch successful;
- screenshot/log/accessibility output thật.

Không được nhận claim `screenshot`, `real browser tested`, `browser runtime verified`, `visual regression passed`, hoặc `accessibility scan passed` nếu chỉ có fallback kiểu local HTTP fetch + HTML assertions. Fallback phải ghi rõ là lower-evidence fallback.

Browser binary install/download cần user approval trước khi chạy lệnh như:

```text
npx playwright install
npx playwright install chromium
npm install playwright
npm install puppeteer
apt install chromium
apt-get install chromium
```

## Claim downgrade rule

Nếu evidence không khớp claim:

- `Done` → `Needs Review`
- `Working` → `Paper/Simulated only`
- `Tested` → `Untested or lower evidence`
- `Production-ready` → `Not production-ready`
- `Deployed` → `Blocked` nếu thiếu approval/deploy evidence

PM Agent phải nói rõ lý do downgrade và evidence còn thiếu.

## Approval rule

User approval bắt buộc trước khi:
- deploy production;
- cloud/DNS/billing action;
- dùng secret thật;
- destructive migration/action;
- install/download browser binary hoặc dependency lớn nếu policy chưa duyệt;
- accept Critical/High blocker as risk.

Production preflight không thay thế user approval.

## Source of truth

- Project evidence nằm trong project artifacts: task-board, issue-log, change-log, status-dashboard, reports, evidence folder.
- PM Agent observation nằm ở `memory/pm-agent-observations.md` khi là bài học/decision đáng nhớ.
- Runtime snapshot nhỏ nằm ở `ops/state/pm-agent/` khi cần.
