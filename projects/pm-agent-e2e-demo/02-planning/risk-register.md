# Risk Register: Hệ thống quản lý công việc nội bộ

## Risk Matrix
```
High   |        | R-001 |       |
Medium | R-002  | R-003 |       |
Low    |        |       |       |
       Low    Medium   High
            Impact
```

## Risk List
| ID | Risk | Probability | Impact | Score | Mitigation | Owner | Status |
|----|------|-------------|--------|-------|------------|-------|--------|
| R-001 | Scope dashboard làm trễ MVP | High | Medium | 6 | Khóa dashboard ở mức cơ bản | PM Agent | Open |
| R-002 | Tester part-time phản hồi chậm | Medium | Low | 2 | Lên lịch review cố định | PM Agent | Open |
| R-003 | Thiếu validation hoặc phân quyền gây rework | Medium | Medium | 4 | Test sớm các luồng quan trọng | Team | Open |

## Mitigation Plans
### R-001: Scope dashboard làm trễ MVP
- **Plan:** Chỉ giữ dashboard mức tổng hợp đơn giản
- **Trigger:** Nếu frontend core chậm tiến độ
- **Action:** Dời analytics nâng cao sang phase sau
- **Owner:** PM Agent
- **Status:** Open

## Risk Monitoring
- **Review frequency:** Weekly
- **Escalation criteria:** Score >= 6
- **Owner:** PM Agent
