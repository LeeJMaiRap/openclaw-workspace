# PM Agent Production Readiness Checklist

## Runtime Foundation
- [x] Workspace structure tách rõ zones
- [x] PM Agent có runtime/ riêng
- [x] PM Agent có eval/ riêng
- [x] Có project metadata schema
- [x] Có decision policy
- [x] Có approval policy
- [x] Có state schema
- [x] Có lifecycle registry
- [x] Có runbooks cơ bản

## Project Operations
- [x] Có project.yaml cho project active
- [ ] Có decisions/ cho project active
- [ ] Có approvals/ cho project active
- [ ] Có handoffs/ cho project active
- [ ] Có evidence/ cho project active
- [ ] Có final-report.md cho closure flow

## Quality & Governance
- [ ] Có eval scenarios thực tế
- [ ] Có regression test pack
- [ ] Có acceptance verification checklist
- [ ] Có stale-project detection rule
- [ ] Có rollback playbook cho project issue

## Multi-project Scalability
- [x] Có projects registry
- [x] Có active projects dashboard
- [ ] Có archived projects dashboard
- [ ] Có portfolio dashboard
- [ ] Có cross-project risk view

## Overall Assessment
**Current state:** Production-readiness foundation established, but project-level governance folders still missing.
