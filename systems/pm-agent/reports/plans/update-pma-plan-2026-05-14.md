# PM Agent Update Plan - 2026-05-14

- **Scope:** Đợt nâng cấp production-readiness cho chính `systems/pm-agent/`
- **Owner:** Anh Doanh + PM Agent
- **Status:** Draft for review
- **Purpose:** Biến PM Agent từ framework đã validate sang hệ có thể đưa vào sử dụng thực tế ổn định hơn.

## Vì sao file này lưu ở đây?

**Path:** `systems/pm-agent/reports/plans/update-pma-plan-2026-05-14.md`

### Lý do chọn vị trí này
1. Đây là **kế hoạch nâng cấp cho chính PM Agent framework**
2. Không phải project nghiệp vụ trong `projects/`
3. Không phải tri thức tham khảo tĩnh trong `knowledge/`
4. Không phải memory cá nhân trong `agent-core/`
5. `systems/pm-agent/reports/plans/` phù hợp cho các kế hoạch vận hành / nâng cấp / đợt cải tiến của framework

---

# Checklist tổng thể đợt update

## Mục tiêu đợt này
- tăng production-readiness của PM Agent
- làm report hằng ngày đáng tin hơn
- tăng khả năng audit “ai làm gì”
- chuẩn hóa vận hành cho project thực tế
- giảm khoảng cách giữa framework hiện tại và production use

## Mức ưu tiên đề xuất

### Phase 1 - Bắt buộc trước
- [ ] Chuẩn hóa **actor tracking convention**
- [ ] Gắn actor vào các artifact vận hành chính
- [ ] Cập nhật `production-readiness-checklist.md` cho khớp thực tế
- [ ] Chuẩn hóa cấu trúc daily reporting cho framework và project

### Phase 2 - Tự động hóa vận hành
- [ ] Thiết kế cron/report flow 19:00
- [ ] Chuẩn hóa nguồn dữ liệu cho `daily-project-report-generator`
- [ ] Bổ sung stale/no-change handling cho daily report
- [ ] Quy định output policy cho daily report

### Phase 3 - Hardening cho production
- [ ] Tạo acceptance verification rules
- [ ] Tạo stale-project detection rules
- [ ] Bổ sung regression/eval pack
- [ ] Bổ sung archived/portfolio dashboard foundation

---

# Kế hoạch chi tiết

## Phase 1 — Actor tracking + trạng thái thật

### 1.1. Tạo chuẩn actor tracking
**Mục tiêu:** Mọi thay đổi quan trọng phải biết ai làm.

**Checklist:**
- [ ] Định nghĩa actor format chuẩn:
  - `human:[name]`
  - `agent:main`
  - `subagent:[label-or-session]`
  - `unknown`
- [ ] Tạo file policy cho actor tracking
- [ ] Chỉ rõ nguồn actor ưu tiên:
  1. explicit actor trong docs
  2. handoff
  3. change log / decision log
  4. git author
  5. unknown
- [ ] Quy định khi nào **không được bịa actor**

**Output mong muốn:**
- policy file cho actor tracking trong `systems/pm-agent/runtime/policies/`

---

### 1.2. Gắn actor vào artifact chính
**Mục tiêu:** Report sau này có dữ liệu thật để tổng hợp.

**Checklist:**
- [ ] Cập nhật quy ước cho:
  - task board
  - change log
  - issue log
  - handoffs
  - decisions
  - approvals
- [ ] Tạo mẫu handoff có trường actor rõ ràng
- [ ] Tạo quy ước change entry có actor rõ ràng
- [ ] Tạo quy ước issue update có actor rõ ràng

**Output mong muốn:**
- update template / guideline / sample output trong PM Agent

---

### 1.3. Sửa readiness checklist cho đúng thực tế
**Mục tiêu:** PM Agent tự đánh giá đúng trạng thái hiện tại.

**Checklist:**
- [ ] Đối chiếu checklist hiện tại với cấu trúc thực tế
- [ ] Mark lại các mục đã có nhưng đang ghi thiếu
- [ ] Tách rõ:
  - foundation đã xong
  - partial
  - chưa làm
- [ ] Thêm ghi chú blocker thực tế

**Output mong muốn:**
- `systems/pm-agent/eval/checklists/production-readiness-checklist.md` phản ánh đúng trạng thái thật

---

## Phase 2 — Daily report 19:00

### 2.1. Hardening skill `daily-project-report-generator`
**Mục tiêu:** Skill không chỉ sinh khung mà bắt đầu đọc dữ liệu thật tốt hơn.

**Checklist:**
- [ ] Đọc thêm từ:
  - git log
  - handoffs
  - decisions
  - approvals
  - change log
- [ ] Bổ sung actor attribution logic
- [ ] Bổ sung no-change mode
- [ ] Bổ sung stopped/on-hold project handling
- [ ] Bổ sung framework-report mode cho `systems/pm-agent/`

**Output mong muốn:**
- skill daily report usable hơn cho thực tế

---

### 2.2. Thiết kế cron flow 19:00
**Mục tiêu:** Mỗi ngày có thể tự sinh report đúng giờ.

**Checklist:**
- [ ] Chọn cơ chế chạy:
  - OpenClaw cron
  - hoặc system cron
- [ ] Xác định project selector rule:
  - active only?
  - exclude stopped/on-hold?
- [ ] Xác định naming rule cho report
- [ ] Xác định fail behavior:
  - nếu thiếu dữ liệu thì sao
  - nếu không có thay đổi thì sao
- [ ] Xác định notify policy:
  - chỉ ghi file
  - hay báo luôn cho anh

**Output mong muốn:**
- spec cron flow 19:00
- có thể triển khai sau khi anh duyệt

---

## Phase 3 — Hardening production

### 3.1. Acceptance verification
**Mục tiêu:** Tránh task “done giả”.

**Checklist:**
- [ ] Định nghĩa thế nào là done
- [ ] Định nghĩa evidence tối thiểu
- [ ] Định nghĩa khi nào được close issue
- [ ] Định nghĩa khi nào được close project

---

### 3.2. Stale-project detection
**Mục tiêu:** Không để project chết mềm mà không biết.

**Checklist:**
- [ ] Xác định ngưỡng stale theo thời gian
- [ ] Xác định stale task / stale approval / stale project
- [ ] Định nghĩa cách escalate

---

### 3.3. Regression / eval pack
**Mục tiêu:** Sau mỗi đợt chỉnh skill/runtime không bị tụt chất lượng.

**Checklist:**
- [ ] Tạo scenario:
  - vague requirement
  - scope change
  - worker failure
  - missing approval
  - stale project
  - false done
- [ ] Tạo expected behaviors
- [ ] Tạo checklist pass/fail

---

# Thứ tự triển khai em đề xuất

## Bắt đầu ngay sau khi anh duyệt file này
1. **Actor tracking policy**
2. **Gắn actor vào artifact/templates**
3. **Sửa readiness checklist**
4. **Nâng cấp daily report skill**
5. **Thiết kế cron 19:00**
6. **Acceptance verification**
7. **Stale-project detection**
8. **Regression/eval pack**

---

# Tiêu chí hoàn thành đợt update

Đợt update này được xem là đạt khi:
- [ ] PM Agent có actor tracking policy rõ ràng
- [ ] Daily report có thể phản ánh actor tốt hơn
- [ ] Readiness checklist khớp với trạng thái thật
- [ ] Có spec rõ cho cron 19:00
- [ ] Có rule cơ bản để tránh done giả
- [ ] Có rule phát hiện project stale
- [ ] Có bộ eval nền cho các lỗi workflow chính

---

# Ghi chú

## Chưa làm ngay trong bước này
- chưa triển khai Discord integration
- chưa bật cron thật
- chưa mở rộng portfolio dashboard đầy đủ

## Sau khi anh duyệt
Em sẽ bám đúng checklist này để nâng cấp PM Agent theo từng phase, ưu tiên từ trên xuống.
