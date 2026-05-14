# Lessons Learned: Hệ thống quản lý công việc nội bộ

## What Went Well
1. **Chuỗi tài liệu PM được tạo đồng bộ** - Từ clarification đến dashboard đều bám cùng một logic dự án.
2. **WBS và task board làm lộ điểm nghẽn sớm** - Blocker API contract được nhìn ra rõ trước khi lan rộng.
3. **Scope control hoạt động tốt** - Dashboard đã được giảm scope kịp thời để bảo vệ MVP.

## What Could Be Improved
1. **API contract cần chốt sớm hơn** - Việc chốt muộn làm frontend bị block.
2. **Cần chi tiết hơn phần phân quyền và validation từ đầu** - Nếu không sẽ dễ rework ở execution.
3. **Ước lượng phase handoff còn hơi lạc quan** - Variance +2 ngày cho thấy cần buffer rõ hơn.

## Key Insights
- Insight 1: Workflow PM Agent có thể đi xuyên suốt từ input đến monitoring mà vẫn nhất quán.
- Insight 2: Các skill execution phát huy giá trị rõ nhất khi có dữ liệu sống từ task board và issue log.
- Insight 3: Scope reduction đúng lúc là một quyết định PM quan trọng để giữ MVP khả thi.

## Recommendations
1. For similar projects in future: Chốt API contract trước khi mở frontend core.
2. For PM Agent improvements: Thêm checklist xác nhận contract/validation trước execution.
3. For team process improvements: Luôn có buffer nhỏ giữa backend handoff và frontend start.

## Metrics Summary
- **Estimation accuracy:** Chưa đủ dữ liệu cuối kỳ, hiện lệch nhẹ
- **On-time delivery:** Chưa kết thúc, đang at risk nhẹ
- **Budget variance:** +2h forecast
- **Defect escape rate:** Thấp ở thời điểm hiện tại
- **Team satisfaction:** Chưa có dữ liệu

## Knowledge Transfer
- **Documentation location:** `projects/pm-agent-e2e-demo/`
- **Key contacts:** Owner, PM Agent, Backend dev, Frontend dev
- **Related projects:** `projects/web-ban-hang/`
- **Lessons learned repository:** `projects/pm-agent-e2e-demo/lessons-learned.md`

## Action Items
- [ ] Thêm checklist chốt API contract vào workflow
- [ ] Thêm checklist validation form sớm trong phase frontend
- [ ] Rà lại template handoff giữa backend và frontend
