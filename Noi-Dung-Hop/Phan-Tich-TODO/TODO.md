# TODO

## Ghi chú tiếp tục từ phân tích cuộc họp

### Thông tin liên kết cuộc họp
- **Ngày họp:** 2026-04-25
- **Ngày tạo TODO:** 2026-05-05
- **File ghi chú cuộc họp liên quan:** `../Ghi-Chu-Cuoc-Hop/2026-04-25-Ghi-Chu-Cuoc-Hop.md`

### Mục tiêu
Lưu lại các phân tích và quyết định tạm thời của anh sau khi đọc phần phân tích cuộc họp. Sau khi hoàn thành Phần 6, sẽ áp dụng các nội dung phù hợp vào OpenClaw / hệ thống PM Agent.

### Kết luận đã chốt từ Phần 1 và 2
- Claude-mem đang hoạt động khá ổn nên không cần chỉnh sửa gì.
- Cần thiết kế quy tắc để Agent sử dụng Obsidian chuẩn xác.
- Cần cẩn thận thiết kế việc mount thư mục để OpenClaw thao tác với Obsidian.
- Cần phân tích và phân chia vai trò hợp lý giữa Claude-mem và Obsidian.
- Cần thiết kế luồng hoạt động phù hợp cho Claude-mem và Obsidian khi lưu thông tin.

---

## Kế hoạch triển khai tổng thể sau khi đã rà soát và gộp ý trùng

### Bước 0 - Hướng dẫn liên kết OpenClaw/Lệ với Telegram để anh và em có thể chat qua Telegram
**Mục tiêu:** tạo kênh giao tiếp thực tế đầu tiên giữa anh và em thông qua Telegram trước khi đi sâu vào các bước nâng cấp khác.

#### Việc cần làm
- Kiểm tra OpenClaw hiện có hỗ trợ/cấu hình Telegram tới đâu.
- Hướng dẫn anh tạo Telegram Bot và lấy bot token.
- Cấu hình Telegram cho OpenClaw.
- Kiểm tra anh có thể nhắn tin với Lệ qua Telegram thành công.
- Xác định đây là kênh chat chính dùng để tiếp tục phát triển PM Agent.

#### Kết quả mong muốn
- Anh và em có thể chat ổn định qua Telegram.
- Có nền giao tiếp thật để thử các bước tiếp theo.

---

### Bước 1 - Chốt nền bộ nhớ và kho tri thức
**Mục tiêu:** làm rõ vai trò của Claude-mem và Obsidian trước khi phát triển tính năng mới.

#### Việc cần làm
- Thiết kế quy tắc để Agent sử dụng Obsidian chuẩn xác.
- Phân chia vai trò giữa Claude-mem và Obsidian:
  - Claude-mem: nhớ ngữ cảnh, thông tin quan trọng, truy hồi khi cần.
  - Obsidian: lưu note, tài liệu, decision log, project knowledge.
- Thiết kế luồng lưu thông tin:
  - thông tin nào lưu vào Claude-mem
  - thông tin nào lưu vào Obsidian
  - thông tin nào chỉ xử lý tạm thời
- Xác định cấu trúc note/project trong Obsidian.

#### Kết quả mong muốn
- Có quy tắc rõ để tránh lưu sai chỗ, lưu trùng hoặc ghi chú lộn xộn.

---

### Ghi chú cập nhật roadmap
- **Bước 1 đã hoàn thành.**
- **Output của Bước 1** là 2 file hiện có trong nhóm nội dung này:
  - `../Ghi-Chu-Cuoc-Hop/2026-04-25-Ghi-Chu-Cuoc-Hop.md`
  - `./TODO.md`
- **Bước 2** sẽ bắt đầu từ việc **thiết kế hạ tầng thực tế**.

### Bước 2 - Thiết kế hạ tầng Obsidian + Docker + GitHub
**Mục tiêu:** tạo nền hạ tầng ổn định để OpenClaw có thể thao tác dữ liệu và source code an toàn, lâu dài.

**Trạng thái hiện tại:** **tạm đủ dùng để chuyển sang Bước 3**.

#### Ghi chú thiết kế
- Note thiết kế hạ tầng thực tế đã tạo tại: `./BUOC-2-THIET-KE-HA-TANG-THUC-TE.md`
- Checklist triển khai thực tế đã tạo tại: `./BUOC-2-CHECKLIST-TRIEN-KHAI-HA-TANG.md`
- Quyết định tạm chốt: dùng mô hình **host-first storage + mounted access + GitHub for repos**.
- Không để Obsidian vault, source code hoặc skill quan trọng chỉ sống bên trong container.

#### Việc cần làm
- Thiết kế cách mount thư mục Obsidian từ ổ D vào Docker/WSL.
- Kiểm tra quyền đọc/ghi của OpenClaw với thư mục Obsidian.
- Xác định cách liên kết source code với GitHub để tránh code bị “kẹt” trong container.
- Chốt mô hình làm việc với source code:
  - code ở host và mount vào container
  - hoặc clone/pull từ GitHub theo quy trình rõ ràng
- Đảm bảo có thể commit/pull/push thuận tiện.

#### Kết quả mong muốn
- OpenClaw thao tác được với Obsidian.
- Source code và skill có thể quản lý ổn định bằng Git/GitHub.

#### Trạng thái hiện tại của Bước 2
- Đã chốt vault Obsidian thật:
  - Tên vault: `OpenClaw-Vault`
  - Đường dẫn Windows: `D:\OpenClaw\Obsidian\OpenClaw-Vault`
  - Đường dẫn WSL: `/mnt/d/OpenClaw/Obsidian/OpenClaw-Vault`
- Đã xác minh WSL nhìn thấy vault và đọc được `.obsidian`, `Welcome.md`.
- Đã xác minh container hiện tại **chưa có mount nào** và **chưa nhìn thấy vault Obsidian**.
- **Tạm thời bỏ qua phần mount Obsidian vào container** theo quyết định hiện tại.
- Đã chốt và tạo thư mục repo/source code trên host:
  - Windows: `D:\OpenClaw\Repos`
  - WSL: `/mnt/d/OpenClaw/Repos`
- Đã copy workspace từ container ra host:
  - Windows: `D:\OpenClaw\Repos\openclaw-workspace`
  - WSL: `/mnt/d/OpenClaw/Repos/openclaw-workspace`
- Đã kiểm tra Git trên repo host:
  - ban đầu nhiều file bị `M` do file mode khi copy sang ổ D
  - đã dùng `core.filemode false`
  - hiện chỉ còn các thay đổi thật cần xét commit
- Đã gắn GitHub remote và push thành công:
  - Repo: `https://github.com/LeeJMaiRap/openclaw-workspace`
  - Branch: `main`
  - Commit: `799fa40` - `Move workspace to host and update PM Agent roadmap`
- Đã tạo note quy trình đồng bộ tạm thời khi container còn tách khỏi host:
  - `./QUY-TRINH-DONG-BO-CONTAINER-TACH-HOST.md`
- **Kết luận:** Bước 2 hiện đã **tạm đủ dùng** để chuyển sang **Bước 3 - thiết kế nhóm skill lõi cho PM Agent**.

---

### Bước 3 - Thiết kế nhóm skill lõi cho PM Agent
**Mục tiêu:** chia năng lực của agent thành các skill nhỏ, rõ đầu vào - đầu ra.

#### Trạng thái hiện tại (cập nhật 2026-05-11)

**Đã hoàn thành:**
- Đã xóa toàn bộ skill/spec/demo cũ để làm lại từ đầu
- Đã rà soát lại hệ tài liệu PM thực tế từ `docs/pm-agent/`
- Đã thiết kế lại taxonomy skill theo 4 nhóm chức năng
- Đã chốt danh sách 17 skill lõi chính thức
- Đã tạo cấu trúc thư mục thật trong `skills/pm-agent/`

**Cấu trúc skill mới:**
```
skills/pm-agent/
├── input-normalization/        (3 skill)
├── document-generation/        (8 skill)
├── project-operations/         (5 skill)
└── infrastructure/             (1 skill)
```

**Danh sách 17 skill đã chốt:**

*Nhóm A - Chuẩn hóa đầu vào (3):*
1. requirement-clarifier
2. meeting-notes-normalizer
3. action-items-extractor

*Nhóm B - Sinh tài liệu PM (8):*
4. project-charter-generator
5. requirements-document-generator
6. project-spec-generator
7. project-plan-generator
8. rules-generator
9. wbs-generator
10. schedule-generator
11. risk-register-generator

*Nhóm C - Vận hành dự án (5):*
12. task-board-builder
13. issue-log-updater
14. change-log-updater
15. status-dashboard-updater
16. lessons-learned-writer

*Nhóm D - Hạ tầng (1):*
17. markdown-to-pdf

**Đã hoàn thành tiếp:**
- Đã viết đầy đủ spec + template + ví dụ cho toàn bộ 17/17 skill
- Đã hoàn thành trọn 4 nhóm skill:
  - `input-normalization` (3/3)
  - `document-generation` (8/8)
  - `project-operations` (5/5)
  - `infrastructure` (1/1)
- Đã bổ sung script thật cho skill `markdown-to-pdf` tại:
  - `skills/pm-agent/infrastructure/markdown-to-pdf/scripts/md_to_pdf.py`

**Trạng thái chốt:**
- **Bước 3 đã hoàn thành về mặt thiết kế hệ skill lõi.**

**Tiếp theo:**
- Test thử 1 workflow PM Agent thật từ input → tài liệu → task board → dashboard → PDF
- Rà lại những skill nào cần tinh chỉnh sau test thực tế
- Chuyển sang giai đoạn áp dụng/tích hợp thực chiến

#### Nguyên tắc thiết kế skill mới
- Xuất phát từ artefact PM thật, không phải từ tên skill "hay hay"
- Mỗi skill phải rõ: input → xử lý → output
- Ưu tiên skill chuẩn hóa đầu vào trước (vì input sai thì output sai)
- Skill sinh tài liệu phải bám sát cấu trúc `projects/[project-name]/`
- Skill vận hành phải cập nhật được trạng thái dự án sống
- Skill hạ tầng chỉ build khi thật sự cần

#### Kết quả mong muốn
- Có bộ skill lõi hoạt động thật, không chỉ là demo
- Mỗi skill có spec rõ ràng, template chuẩn, ví dụ thật
- Skill phục vụ workflow PM, không phải tool lẻ tẻ

---

### Bước 4 - Chọn skill đầu tiên để làm thử
**Mục tiêu:** không làm dàn trải, chỉ chọn 1 skill dễ kiểm chứng nhất để xây đầu tiên.

#### Ứng viên ưu tiên
- `Meeting Notes -> Summary + Action Items`
- `Meeting Notes -> Meeting Minutes`

#### Vì sao ưu tiên
- Đầu vào rõ ràng.
- Dễ test với dữ liệu thật.
- Gần nhu cầu PM thực tế.
- Dễ gắn với Obsidian và workflow tài liệu.

#### Kết quả mong muốn
- Có một skill đầu tiên chạy được thật, tạo nền cho các skill sau.

---

### Bước 5 - Thiết kế hệ thống tài liệu PM
**Mục tiêu:** chuẩn hóa cách tạo tài liệu trước khi nghĩ đến PDF.

#### Tài liệu nên ưu tiên trước
- Meeting Minutes / Biên bản họp
- PRD draft
- BRD draft
- Action Items / checklist sau họp
- Weekly Status Report

#### Đầu vào cho skill tài liệu
- Ghi chú họp thô
- Đoạn chat mô tả yêu cầu
- Brief dự án ngắn
- Note nghiệp vụ / yêu cầu khách hàng
- Nội dung đã lưu trong Obsidian

#### Luồng tạo tài liệu đề xuất
- Nhận đầu vào thô
- Phân loại loại tài liệu
- Áp template / khung nội dung
- Sinh bản nháp Markdown
- Cho anh xem / chỉnh
- Nếu cần thì mới xuất PDF

#### Quy tắc đầu ra
- Ưu tiên **Markdown** trước
- PDF là bước sau cùng
- Có thể giữ:
  - `.md` = bản gốc làm việc
  - `.pdf` = bản trình bày / chia sẻ

#### Kết quả mong muốn
- Có hệ thống tạo tài liệu PM rõ ràng, không làm PDF quá sớm.

---

### Bước 6 - Tích hợp Telegram làm kênh giao tiếp chính
**Mục tiêu:** biến OpenClaw/PM Agent thành công cụ dùng được hằng ngày qua chat.

#### Giai đoạn 1 - Telegram text
- Tạo Telegram Bot và lấy bot token.
- Kết nối Telegram với OpenClaw để nhận/gửi text.
- Kiểm tra anh có thể chat với Lệ qua Telegram ổn định.
- Xác định mỗi user Telegram map với session nào trong OpenClaw.

#### Giai đoạn 2 - Chuẩn hóa luồng chat
- Xác định cách xử lý text, file, ảnh và voice.
- Thiết kế format phản hồi phù hợp với Telegram.
- Xác định tin nhắn nào cần lưu vào memory / Obsidian.

#### Kết quả mong muốn
- Mốc đầu tiên: `Nhắn Telegram -> OpenClaw trả lời ổn định`.

---

### Bước 7 - Bổ sung voice cho Telegram
**Mục tiêu:** tăng sự tiện lợi sau khi Telegram text đã chạy ổn.

#### Voice-to-text
- Nhận voice note từ Telegram.
- Tải file về để xử lý.
- Chuyển voice thành text.
- Đưa text vào luồng xử lý như yêu cầu bình thường.
- Nếu transcript không rõ thì trả lại để anh xác nhận.

#### Text-to-voice
- Cho phép chuyển câu trả lời thành voice khi anh yêu cầu.
- Có thể cân nhắc gợi ý voice ở một số trường hợp phù hợp.
- Không bật mặc định cho mọi câu trả lời.

#### Kết quả mong muốn
- Dùng voice được nhưng không làm rối luồng chat chính.

---

### Bước 8 - Ghép tất cả thành workflow PM Agent hoàn chỉnh
**Mục tiêu:** sau khi từng phần nền đã ổn, mới kết hợp thành hệ thống PM Agent dùng thực tế.

#### Việc cần làm
- Liên kết Telegram + memory + Obsidian + skill tài liệu.
- Xây luồng từ hội thoại sang ghi chú, tài liệu, action items.
- Xây cách theo dõi project summary, decision log, pending items.
- Kiểm tra khả năng hỗ trợ công việc PM qua chat theo từng use case thật.

#### Kết quả mong muốn
- Lệ/OpenClaw hoạt động dần như một PM Agent thực dụng, không chỉ là chatbot.

---

## Thứ tự ưu tiên triển khai ngắn gọn
0. Hướng dẫn liên kết OpenClaw/Lệ với Telegram để anh và em chat qua Telegram.
1. Chốt vai trò Claude-mem và Obsidian.
2. Thiết kế mount Obsidian + GitHub + Docker.
3. Thiết kế nhóm skill lõi.
4. Chọn 1 skill đầu tiên để làm thử.
5. Chuẩn hóa hệ thống tài liệu PM.
6. Tích hợp Telegram text sâu hơn vào workflow.
7. Thêm voice-to-text rồi text-to-voice.
8. Ghép thành workflow PM Agent hoàn chỉnh.

---

## Nội dung đã được gộp / loại trùng
- Các ý “skill tài liệu PM” ở Phần 3 và Phần 4 đã được gộp lại thành 1 luồng chung.
- Các ý “Telegram + voice” đã được gộp thành thứ tự triển khai rõ ràng.
- Các ý về Claude-mem + Obsidian được đẩy lên đầu vì đây là nền tảng.
- Các ý về PDF được hạ xuống sau Markdown để tránh làm sai thứ tự ưu tiên.

---

## Ghi chú làm việc tiếp theo
- Từ ngày mai, nên làm theo đúng thứ tự ưu tiên ở trên.
- Không triển khai đồng thời quá nhiều phần.
- Mỗi bước xong mới qua bước tiếp theo để tránh rối hệ thống.
- Khi bắt đầu lại, nên bắt đầu từ **Bước 0: Hướng dẫn liên kết OpenClaw/Lệ với Telegram**.

---

## Quy tắc làm việc anh vừa bổ sung
- Khi anh đưa ra 1 yêu cầu:
  - nếu yêu cầu chỉ có 1-2 nội dung chính thì trả lời trực tiếp
  - nếu yêu cầu có từ 3 nội dung chính trở lên thì phải liệt kê các phần nội dung trước, rồi hỏi anh muốn bắt đầu từ phần nào / có đồng ý bắt đầu từ phần 1 không
- Mục đích là tránh trả lời quá dài gây lỗi truncated.
- Không được nghĩ mình thông minh nên đưa ra thông tin gì cũng đúng.
- Thông tin đưa ra phải giải quyết đúng vấn đề anh đang hỏi, tránh sai lệch làm mất năng suất công việc.
- Ưu tiên chậm mà đúng, sát yêu cầu hơn là trả lời nhanh nhưng sai.
