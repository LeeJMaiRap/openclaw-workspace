#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import subprocess


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding='utf-8') if path.exists() else ''


def extract_field(pattern: str, text: str, default: str = 'unknown') -> str:
    m = re.search(pattern, text, re.MULTILINE)
    return m.group(1).strip() if m else default


def parse_task_summary(task_board: str) -> dict[str, str]:
    result: dict[str, str] = {}
    patterns = {
        'total': [r'\*\*Total tasks:\*\*\s*(\d+)'],
        'completed': [r'\*\*Completed:\*\*\s*(\d+)'],
        'in_progress': [r'\*\*In Progress:\*\*\s*(\d+)', r'\*\*In progress:\*\*\s*(\d+)'],
        'blocked': [r'\*\*Blocked:\*\*\s*(\d+)'],
        'pct': [r'\*\*Completion %:\*\*\s*(\d+)%'],
        'phase': [r'\*\*Current phase:\*\*\s*(.+)']
    }
    for key, plist in patterns.items():
        value = 'unknown'
        for pattern in plist:
            m = re.search(pattern, task_board, re.MULTILINE)
            if m:
                value = next((g for g in m.groups() if g), 'unknown')
                break
        result[key] = value
    return result


def parse_project_yaml(text: str) -> dict[str, str]:
    return {
        'project_id': extract_field(r'^project_id:\s*(.+)$', text),
        'name': extract_field(r'^name:\s*(.+)$', text),
        'status': extract_field(r'^status:\s*(.+)$', text),
        'owner': extract_field(r'^owner:\s*(.+)$', text),
        'yaml_total': extract_field(r'^\s*total_tasks:\s*(.+)$', text),
        'yaml_completed': extract_field(r'^\s*completed_tasks:\s*(.+)$', text),
        'yaml_pct': extract_field(r'^\s*completion_percentage:\s*(.+)$', text),
    }


def list_git_commits(repo_root: pathlib.Path, scope: str) -> list[str]:
    try:
        out = subprocess.run(
            ['git', '-C', str(repo_root), 'log', '--oneline', '-n', '6', '--', scope],
            capture_output=True,
            text=True,
            check=False,
        )
        return [line.strip() for line in out.stdout.splitlines() if line.strip()]
    except Exception:
        return []


def parse_approvals(approvals_dir: pathlib.Path) -> list[str]:
    if not approvals_dir.exists():
        return []
    items: list[str] = []
    for path in sorted(approvals_dir.glob('*.md')):
        text = read_text(path)
        status = extract_field(r'^- \*\*Status:\*\*\s*(.+)$', text, default='unknown')
        approver_actor = extract_field(r'^- \*\*Approver actor:\*\*\s*(.+)$', text, default='unknown')
        requested_actor = extract_field(r'^- \*\*Requested actor:\*\*\s*(.+)$', text, default='unknown')
        items.append(f"{path.name} ({status}, requested actor: {requested_actor}, approver actor: {approver_actor})")
    return items


def parse_decisions(decisions_dir: pathlib.Path) -> list[str]:
    if not decisions_dir.exists():
        return []
    text = read_text(decisions_dir / 'decision-log.md')
    entries = []
    chunks = re.split(r'(?=^##\s+)', text, flags=re.MULTILINE)
    for chunk in chunks:
        title_match = re.search(r'^##\s+(.+)$', chunk, re.MULTILINE)
        if not title_match:
            continue
        actor = extract_field(r'^- \*\*Made actor:\*\*\s*(.+)$', chunk, default='unknown')
        entries.append(f"{title_match.group(1).strip()} (made actor: {actor})")
    return entries


def parse_handoff_actors(handoffs_dir: pathlib.Path) -> list[str]:
    if not handoffs_dir.exists():
        return []
    items: list[str] = []
    for path in sorted(handoffs_dir.glob('*.md')):
        if path.name.startswith('template-') or path.name.lower() == 'readme.md':
            continue
        text = read_text(path)
        if 'Assigned to actor' not in text and 'Result actor' not in text:
            continue
        assigned = extract_field(r'^- \*\*Assigned to actor:\*\*\s*(.+)$', text, default='unknown')
        result_actor = extract_field(r'^- \*\*Result actor:\*\*\s*(.+)$', text, default='unknown')
        items.append(f"{path.name} (assigned to: {assigned}, result: {result_actor})")
    return items


def detect_metric_conflicts(project: dict[str, str], summary: dict[str, str]) -> list[str]:
    conflicts: list[str] = []
    if project['yaml_total'] != 'unknown' and summary['total'] != 'unknown' and project['yaml_total'] != summary['total']:
        conflicts.append(f"total_tasks conflict: project.yaml={project['yaml_total']} vs task-board.md={summary['total']}")
    if project['yaml_completed'] != 'unknown' and summary['completed'] != 'unknown' and project['yaml_completed'] != summary['completed']:
        conflicts.append(f"completed_tasks conflict: project.yaml={project['yaml_completed']} vs task-board.md={summary['completed']}")
    if project['yaml_pct'] != 'unknown' and summary['pct'] != 'unknown' and project['yaml_pct'] != summary['pct']:
        conflicts.append(f"completion_percentage conflict: project.yaml={project['yaml_pct']}% vs task-board.md={summary['pct']}%")
    return conflicts


def detect_project_summary(project: dict[str, str], final_report: str) -> str:
    status = project['status'].lower()
    if status in {'stopped', 'on-hold', 'archived'}:
        return f"Dự án hiện ở trạng thái {project['status']}. Report này chỉ nên được hiểu là snapshot trạng thái/handoff, không phải báo cáo tiến độ active bình thường."
    if 'demo-ready' in final_report.lower():
        return 'Dự án đã đạt mức demo-ready nhưng chưa production-ready. Daily report nên tập trung vào trạng thái hiện tại, gap còn lại và lý do nếu không tiếp tục active work.'
    return 'Đây là daily snapshot cho project đang active. Báo cáo nên phản ánh tiến độ, thay đổi và next actions dựa trên source-of-truth hiện có.'


def build_project_report(project: dict[str, str], summary: dict[str, str], approvals: list[str], decisions: list[str], handoffs: list[str], commits: list[str], conflicts: list[str], report_date: str, final_report: str) -> str:
    now = dt.datetime.now(dt.UTC).strftime('%H:%M UTC')
    pct = summary['pct'] if summary['pct'] != 'unknown' else '0'
    human_summary = f"Owner chính: {project['owner']}" if project['owner'] != 'unknown' else 'Chưa xác định tự động từ project metadata.'
    approvals_text = '\n'.join([f'- {x}' for x in approvals]) if approvals else '- None'
    decisions_text = '\n'.join([f'- {x}' for x in decisions[:5]]) if decisions else '- None'
    handoff_text = '\n'.join([f'- {x}' for x in handoffs[:5]]) if handoffs else '- None'
    conflict_text = '\n'.join([f'- {x}' for x in conflicts]) if conflicts else '- No source conflict detected between checked fields'
    refs = '\n'.join([f'- `{c}`' for c in commits]) if commits else '- No recent git commits detected for this scope'
    return f'''# Daily Project Report - {project['name']}

- **Date:** {report_date}
- **Generated at:** {now}
- **Project ID:** {project['project_id']}
- **Project Status:** {project['status']}
- **Report Type:** Daily Snapshot

## Summary
{detect_project_summary(project, final_report)}

## Changes Today
1. Report được sinh từ source-of-truth hiện có của project
   - **Actor:** agent:main
   - **Source:** project files + git scope summary

## Task Progress Snapshot
- **Total tasks:** {summary['total']}
- **Completed:** {summary['completed']}
- **In progress:** {summary['in_progress']}
- **Blocked:** {summary['blocked']}
- **Completion %:** {pct}%
- **Current focus:** {summary['phase']}

## Source Conflicts Detected
{conflict_text}

## Issues / Risks Needing Attention
- Actor attribution vẫn phụ thuộc vào chất lượng field actor trong project artifacts.
- Nếu project không còn active, daily reporting nên dừng mặc định và chỉ dùng theo yêu cầu đặc biệt.

## Decisions / Approvals Today
### Approvals
{approvals_text}

### Decisions
{decisions_text}

## Handoff / Execution Signals
{handoff_text}

## Actor Attribution Summary
- **Human activity:** {human_summary}
- **Main agent activity:** Sinh daily snapshot từ source-of-truth hiện tại.
- **Subagent activity:** Suy ra từ handoff/session evidence nếu có; hiện tại: {'có handoff evidence rõ' if handoffs else 'chưa có handoff evidence rõ'}.
- **Unknown / unverifiable:** Các thay đổi không có actor field hoặc session evidence rõ.

## Next Actions (Next Day)
1. Nếu project vẫn active, tiếp tục cập nhật actor field trong task/change/handoff artifacts
   - **Owner:** PM Agent
   - **Priority:** High

2. Nếu project đã stopped/on-hold, chuyển daily reporting sang chế độ by-request only
   - **Owner:** PM Agent
   - **Priority:** High

3. Nếu có source conflict, cần chốt source-of-truth ưu tiên hoặc sửa artifact bị lệch
   - **Owner:** PM Agent
   - **Priority:** High

## Evidence / References
- `project.yaml`
- `03-execution/task-board.md`
- `03-execution/change-log.md`
- `03-execution/issue-log.md`
- `04-monitoring/status-dashboard.md`
- `05-closure/final-report.md`
- `approvals/`
- `decisions/`
- `handoffs/`

## Git Scope Snapshot
{refs}
'''


def parse_framework_status(text: str) -> dict[str, str]:
    stage_match = re.search(r'### Giai đoạn hiện tại\n\*\*(.+?)\*\*', text, re.MULTILINE | re.DOTALL)
    return {
        'stage': stage_match.group(1).strip() if stage_match else 'unknown',
        'framework_completion': extract_field(r'^- \*\*Mức hoàn thành framework và validation:\*\*\s*(.+)$', text),
        'production_completion': extract_field(r'^- \*\*Mức hoàn thiện production-grade:\*\*\s*(.+)$', text),
    }


def build_framework_report(root: pathlib.Path, report_date: str) -> str:
    now = dt.datetime.now(dt.UTC).strftime('%H:%M UTC')
    status_text = read_text(root / 'systems' / 'pm-agent' / 'STATUS.md')
    parsed = parse_framework_status(status_text)
    skill_count = len(list((root / 'systems' / 'pm-agent' / 'skills').glob('**/SKILL.md')))
    runtime_count = sum(1 for p in (root / 'systems' / 'pm-agent' / 'runtime').glob('**/*') if p.is_file())
    eval_count = sum(1 for p in (root / 'systems' / 'pm-agent' / 'eval').glob('**/*') if p.is_file())
    commits = list_git_commits(root, 'systems/pm-agent')
    refs = '\n'.join([f'- `{c}`' for c in commits]) if commits else '- No recent git commits detected for framework scope'
    return f'''# Daily Project Report - PM Agent Framework

- **Date:** {report_date}
- **Generated at:** {now}
- **Project ID:** pm-agent-framework
- **Project Status:** active
- **Report Type:** Daily Snapshot

## Summary
PM Agent framework đang ở giai đoạn `{parsed['stage']}`. Report này dùng framework-report mode để snapshot thay đổi hệ, không dùng logic project business thông thường.

## Changes Today
1. Framework daily reporting được xử lý theo mode riêng cho `systems/pm-agent/`
   - **Actor:** agent:main
   - **Source:** framework source-of-truth

## Capability / Readiness Snapshot
- **Skill count:** {skill_count}
- **Runtime files:** {runtime_count}
- **Eval files:** {eval_count}
- **Framework + validation completion:** {parsed['framework_completion']}
- **Production-grade completion:** {parsed['production_completion']}

## Issues / Risks Needing Attention
- Framework report đã tách mode rõ, nhưng actor attribution tự động vẫn cần hardening thêm.
- Production-grade completion vẫn chưa hoàn tất; còn thiếu regression/stale/acceptance layers.

## Decisions / Approvals Today
- Framework report mode được chuẩn hóa để tránh lẫn với project-level reporting.

## Actor Attribution Summary
- **Human activity:** Theo chat/workflow context của owner khi có quyết định rõ.
- **Main agent activity:** Phân tích, cập nhật docs/policies/skills và sinh report framework.
- **Subagent activity:** Chỉ ghi khi có evidence rõ từ session/handoff.
- **Unknown / unverifiable:** Không bịa actor khi thiếu bằng chứng.

## Next Actions (Next Day)
1. Đọc thêm git/handoff/change signals để tăng chất lượng actor attribution
   - **Owner:** PM Agent
   - **Priority:** High

2. Tiếp tục hardening production-readiness layers còn thiếu
   - **Owner:** PM Agent
   - **Priority:** High

## Evidence / References
- `systems/pm-agent/STATUS.md`
- `systems/pm-agent/runtime/`
- `systems/pm-agent/eval/`
- `systems/pm-agent/skills/`

## Git Scope Snapshot
{refs}
'''


def main() -> int:
    ap = argparse.ArgumentParser(description='Generate daily report for PM Agent project or framework.')
    ap.add_argument('target_path', help='Project root path or workspace root for framework mode')
    ap.add_argument('--date', default=dt.datetime.now(dt.UTC).strftime('%Y-%m-%d'))
    ap.add_argument('--mode', choices=['project', 'framework'], default='project')
    args = ap.parse_args()

    target = pathlib.Path(args.target_path)
    if args.mode == 'framework':
        report = build_framework_report(target, args.date)
        out_dir = target / 'systems' / 'pm-agent' / 'reports' / 'daily'
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f'{args.date}.md'
    else:
        project_yaml = read_text(target / 'project.yaml')
        task_board = read_text(target / '03-execution' / 'task-board.md')
        final_report = read_text(target / '05-closure' / 'final-report.md')
        project = parse_project_yaml(project_yaml)
        summary = parse_task_summary(task_board)
        approvals = parse_approvals(target / 'approvals')
        decisions = parse_decisions(target / 'decisions')
        handoffs = parse_handoff_actors(target / 'handoffs')
        conflicts = detect_metric_conflicts(project, summary)
        repo_root = target
        while repo_root != repo_root.parent and not (repo_root / '.git').exists():
            repo_root = repo_root.parent
        scope = str(target.relative_to(repo_root)) if (repo_root / '.git').exists() else str(target)
        commits = list_git_commits(repo_root, scope)
        report = build_project_report(project, summary, approvals, decisions, handoffs, commits, conflicts, args.date, final_report)
        out_dir = target / 'reports' / 'daily'
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / f'{args.date}.md'

    out_path.write_text(report, encoding='utf-8')
    print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
