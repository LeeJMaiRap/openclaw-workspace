# PM Agent Production Readiness Checklist

## Runtime Foundation
- [x] Workspace structure tách rõ zones
- [x] PM Agent có runtime/ riêng
- [x] PM Agent có eval/ riêng
- [x] Có project metadata schema
- [x] Có decision policy
- [x] Có approval policy
- [x] Có actor tracking policy
- [x] Có state schema
- [x] Có lifecycle registry
- [x] Có runbooks cơ bản

## Project Operations
- [x] Có project.yaml cho project active
- [x] Có decisions/ cho project active
- [x] Có approvals/ cho project active
- [x] Có handoffs/ cho project active
- [x] Có evidence/ cho project active
- [x] Có final-report.md cho closure flow
- [~] Có daily reporting foundation (skill + sample output đã có, cron thật chưa bật)

## Quality & Governance
- [~] Có eval scenarios thực tế ở mức nền (hiện có `scope-change`, `worker-failure`)
- [x] Có regression test pack
- [x] Có acceptance verification checklist
- [x] Có stale-project detection rule
- [x] Có rollback playbook cho project issue

## Multi-project Scalability
- [x] Có projects registry
- [x] Có active projects dashboard
- [ ] Có archived projects dashboard
- [ ] Có portfolio dashboard
- [ ] Có cross-project risk view

## Readiness Notes
- `[x]` = đã có và dùng được
- `[~]` = đã có foundation / partial, nhưng chưa hoàn chỉnh production-grade
- `[ ]` = chưa có hoặc chưa đủ dùng thực tế

## Current Gaps To Close
1. Actor attribution mới có policy + artifact fields, chưa đủ mạnh ở mức auto-audit hoàn chỉnh.
2. Daily reporting mới ở mức foundation; chưa có cron 19:00 thật và chưa có stopped/on-hold handling hoàn chỉnh.
3. Regression/eval pack còn mỏng, chưa đủ bảo vệ chất lượng sau các đợt update lớn.
4. Chưa có acceptance verification / stale-project detection / rollback playbook.
5. Chưa có lớp nhìn xuyên nhiều project như archived dashboard / portfolio dashboard / cross-project risk view.

## Overall Assessment
**Current state:** Production-readiness foundation established and project governance baseline is now in place. PM Agent đủ tốt cho pilot/internal use có kiểm soát, nhưng vẫn cần thêm hardening trước khi coi là production-grade hoàn chỉnh.
