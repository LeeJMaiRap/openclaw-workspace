# Project Plan: Hệ thống quản lý công việc nội bộ

## 1. Phases
### Phase 1: Setup & Backend Foundation
- **Duration:** 1 tuần
- **Deliverables:** Backend auth + task API
- **Milestones:** Backend usable

### Phase 2: Frontend Core
- **Duration:** 2 tuần
- **Deliverables:** Task UI và state flow
- **Milestones:** Task flow chạy end-to-end

### Phase 3: Collaboration & Dashboard
- **Duration:** 1 tuần
- **Deliverables:** Comment + dashboard cơ bản
- **Milestones:** MVP feature complete

### Phase 4: Testing & Deployment
- **Duration:** 2 tuần
- **Deliverables:** Stable MVP + deploy
- **Milestones:** Internal rollout

**Total:** 6 tuần

## 2. Work Breakdown Structure (WBS)
1. Backend foundation
   1.1 Auth
   1.2 Task CRUD
2. Frontend core
   2.1 Task list
   2.2 Create/edit form
   2.3 Status flow
3. Collaboration & dashboard
   3.1 Comment
   3.2 Dashboard
4. Testing & deployment
   4.1 QA
   4.2 Deploy

## 3. Dependencies
- Auth -> Task CRUD
- Task CRUD -> Frontend Task UI
- Task UI -> Dashboard
- All core features -> QA -> Deploy

## 4. Resource Allocation
| Task | Assigned To | Estimated Hours | Notes |
|------|-------------|-----------------|-------|
| Backend foundation | Backend dev | 32h | API + auth |
| Frontend core | Frontend dev | 48h | Main UI |
| QA | Tester part-time | 16h | Validation + smoke test |

## 5. Communication Plan
- Daily sync ngắn
- Weekly review mỗi thứ 6
- PM update mỗi đầu tuần

## 6. Risk Mitigation
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Scope tăng | Medium | High | Khóa MVP |
| Validation sót | Medium | Medium | Test sớm |
| Feedback chậm | Medium | Medium | Review lịch cố định |

## 7. Success Criteria
- ✅ MVP dùng được nội bộ
- ✅ Task flow ổn định
- ✅ Dashboard cơ bản hoạt động
- ✅ Hoàn thành trong 6 tuần
