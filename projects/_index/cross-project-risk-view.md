# Cross-Project Risk View

Sau cleanup 2026-05-26, workspace chính chưa có nhiều project để phân tích risk xuyên project.

## Current Observation

- Không có project folder active trong cây chính.
- PM Agent framework vẫn còn đầy đủ tại `systems/pm-agent/`.
- Risk view hiện chỉ là placeholder cho các project mới sau này.

## Risk Patterns Cần Theo Dõi Khi Có Project Mới

### 1. Source-of-truth drift
Artifact khác nhau lệch nhau về status/progress.

### 2. Done giả / verification yếu
Task bị đánh dấu done khi chưa có evidence hoặc acceptance rõ.

### 3. Active nhưng thực tế đã dừng
Metadata/path/status không còn phản ánh công việc thật.

### 4. Actor attribution yếu
Không rõ human/main agent/subagent nào làm gì.

## Next Step

Khi có project active mới:
1. Cập nhật registry.
2. Chạy PM Agent reporting theo project lifecycle.
3. Ghi risk pattern thực tế vào file này.

Last updated: 2026-05-26T02:25:00Z
