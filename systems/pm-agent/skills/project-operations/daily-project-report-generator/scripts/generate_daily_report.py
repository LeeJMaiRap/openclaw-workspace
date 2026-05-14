#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re


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
    }


def build_report(project: dict[str, str], summary: dict[str, str], report_date: str) -> str:
    now = dt.datetime.now(dt.UTC).strftime('%H:%M UTC')
    pct = summary['pct'] if summary['pct'] != 'unknown' else '0'
    return f'''# Daily Project Report - {project['name']}

- **Date:** {report_date}
- **Generated at:** {now}
- **Project ID:** {project['project_id']}
- **Project Status:** {project['status']}
- **Report Type:** Daily Snapshot

## Summary
Hôm nay chưa có bộ actor tracking hoàn chỉnh để xác nhận toàn bộ thay đổi tự động theo người thực hiện. Report này là khung daily snapshot đầu tiên để PM Agent bắt đầu vận hành cơ chế báo cáo hằng ngày.

## Changes Today
1. Daily reporting skill được khởi tạo và sẵn sàng tích hợp vào workflow PM Agent
   - **Actor:** agent:main
   - **Source:** skill/runtime setup

## Task Progress Snapshot
- **Total tasks:** {summary['total']}
- **Completed:** {summary['completed']}
- **In progress:** {summary['in_progress']}
- **Blocked:** {summary['blocked']}
- **Completion %:** {pct}%
- **Current focus:** {summary['phase']}

## Issues / Risks Needing Attention
- Actor attribution chưa đủ mạnh để audit chính xác mọi thay đổi theo ngày.
- Cần tích hợp cron chạy 19:00 và rule cập nhật actor trong project docs.

## Decisions / Approvals Today
- Khởi tạo daily reporting foundation cho PM Agent.

## Actor Attribution Summary
- **Human activity:** Chưa xác định tự động trong bản khởi tạo.
- **Main agent activity:** Tạo skill, template, script và report khung.
- **Subagent activity:** Không có dữ liệu binding trong report khởi tạo.
- **Unknown / unverifiable:** Các thay đổi cũ hơn không được map tự động theo ngày trong bản đầu.

## Next Actions (Next Day)
1. Tích hợp cron chạy 19:00 mỗi ngày
   - **Owner:** PM Agent
   - **Priority:** High

2. Thêm actor field vào handoff / task / change updates
   - **Owner:** PM Agent
   - **Priority:** High

## Evidence / References
- `project.yaml`
- `03-execution/task-board.md`
- `03-execution/change-log.md`
- `03-execution/issue-log.md`
- `04-monitoring/status-dashboard.md`
'''


def main() -> int:
    ap = argparse.ArgumentParser(description='Generate daily project report scaffold for PM Agent project.')
    ap.add_argument('project_path', help='Path to project root')
    ap.add_argument('--date', default=dt.datetime.now(dt.UTC).strftime('%Y-%m-%d'))
    args = ap.parse_args()

    project_path = pathlib.Path(args.project_path)
    project_yaml = read_text(project_path / 'project.yaml')
    task_board = read_text(project_path / '03-execution' / 'task-board.md')

    project = parse_project_yaml(project_yaml)
    summary = parse_task_summary(task_board)
    report = build_report(project, summary, args.date)

    out_dir = project_path / 'reports' / 'daily'
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f'{args.date}.md'
    out_path.write_text(report, encoding='utf-8')
    print(out_path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
