# Bước 2 - Thiết kế hạ tầng thực tế cho Obsidian + Docker + GitHub

## Mục tiêu
Chốt phương án hạ tầng thực tế để OpenClaw có thể:
- đọc/ghi vault Obsidian an toàn
- quản lý source code không bị kẹt trong container
- dễ backup, dễ khôi phục, dễ mở rộng về sau

---

## 1) Hiện trạng đã kiểm tra

### Môi trường chạy hiện tại
- OpenClaw đang chạy trong môi trường Linux/container.
- Gateway đang lắng nghe tại `0.0.0.0:18789`.
- `openclaw gateway status` báo gateway probe **ok**.
- Workspace hiện tại là: `/root/.openclaw/workspace`

### Dấu hiệu quan trọng về storage
- Thư mục `/mnt` hiện gần như trống, **chưa thấy ổ D được mount vào WSL/container**.
- Điều này có nghĩa là hiện tại OpenClaw **chưa thể truy cập trực tiếp vault Obsidian trên Windows ổ D**.

### Git hiện tại
- Workspace hiện đã là một Git repo local (`.git` có tồn tại).
- Chưa thấy remote GitHub (`git remote -v` đang trống).
- Nghĩa là hiện tại code có thể commit local, nhưng **chưa có đường sync chuẩn với GitHub**.

### Tài liệu liên quan đã có
- `docs/pm-agent/STORAGE-RULES.md`
- `docs/pm-agent/SCRIPTS/backup-and-recreate-docker.ps1`

---

## 2) Kết luận hạ tầng thực tế

### Kết luận 1 - Không nên để dữ liệu quan trọng chỉ sống trong container
Không nên để các thứ sau chỉ tồn tại bên trong container:
- vault Obsidian
- source code dự án
- skill tự viết
- project documents

**Lý do:**
- recreate container dễ làm mất cấu hình/mount nếu làm sai
- backup thủ công sẽ rườm rà
- source code bị “kẹt” trong container gây khó dùng IDE, GitHub, Obsidian, Windows tools

### Kết luận 2 - Nên lấy host làm nguồn dữ liệu thật
Phương án chuẩn nên là:
- **Windows host / thư mục thật** là nơi giữ dữ liệu gốc
- Docker/container chỉ là nơi **mount vào để thao tác**
- GitHub là lớp đồng bộ/version control cho source code và tài liệu phù hợp

### Kết luận 3 - Obsidian và source code nên tách ra thành 2 vùng dữ liệu
Không nên trộn tất cả vào một chỗ.

Nên tách:
- **Vùng 1: Obsidian Vault** → tri thức, note, decision log, meeting minutes, PM artifacts
- **Vùng 2: Source Code / Skills / Projects** → code, scripts, config, templates, repos

---

## 3) Kiến trúc đề xuất

## 3.1. Tầng dữ liệu thật trên host
Đề xuất trên Windows host tạo cấu trúc như sau:

```text
D:\Doanh\ObsidianVault\
D:\Doanh\PM-Agent\repos\
D:\Doanh\PM-Agent\exports\
D:\Doanh\PM-Agent\backups\
```

### Ý nghĩa
- `D:\Doanh\ObsidianVault\`
  - vault Obsidian thật
  - chứa note, project knowledge, meeting notes, decision log
- `D:\Doanh\PM-Agent\repos\`
  - chứa source code các project/repo
  - gồm OpenClaw-related repos, skills, scripts nếu cần tách
- `D:\Doanh\PM-Agent\exports\`
  - nơi xuất file tạm, report, PDF nếu sau này cần
- `D:\Doanh\PM-Agent\backups\`
  - backup thủ công/định kỳ

---

## 3.2. Tầng mount vào Linux/WSL/container
Khi map từ host sang môi trường Linux, nên hướng tới các mount point logic như sau:

```text
/mnt/host/obsidian
/mnt/host/repos
/mnt/host/exports
/mnt/host/backups
```

Hoặc nếu đi theo kiểu WSL tiêu chuẩn:

```text
/mnt/d/Doanh/ObsidianVault
/mnt/d/Doanh/PM-Agent/repos
/mnt/d/Doanh/PM-Agent/exports
/mnt/d/Doanh/PM-Agent/backups
```

### Gợi ý ưu tiên
Nếu dùng WSL tốt và Docker Desktop map ổ đĩa ổn định, ưu tiên kiểu:
- `/mnt/d/...`

Nếu có lớp bind mount riêng vào container, có thể chuẩn hóa lại thành:
- `/data/obsidian`
- `/data/repos`
- `/data/exports`
- `/data/backups`

---

## 3.3. Tầng sử dụng bên trong OpenClaw/container
Trong container/OpenClaw nên dùng các đường dẫn ổn định, ví dụ:

```text
/data/obsidian
/data/repos
/data/exports
/data/backups
```

### Lý do
- dễ đổi backend mount mà không phải sửa nhiều prompt/script
- dễ viết tài liệu, skill, workflow
- dễ backup và migrate

---

## 4) Phương án đề xuất chính thức

## Phương án A - Khuyến nghị mạnh
**Source of truth nằm trên host Windows, rồi mount vào container.**

### Cách dùng
- Vault Obsidian nằm trên ổ D của Windows.
- Source code/repo cũng nằm trên ổ D hoặc một thư mục host ổn định.
- Docker/OpenClaw mount các thư mục này vào container.
- GitHub dùng cho version control repo code và một phần tài liệu phù hợp.

### Ưu điểm
- Obsidian desktop trên Windows đọc trực tiếp vault thật.
- OpenClaw cũng thao tác cùng nguồn dữ liệu.
- IDE trên Windows, GitHub, Docker đều cùng nhìn một bộ dữ liệu.
- Tránh bị khóa dữ liệu trong container.
- Backup rõ ràng hơn.

### Nhược điểm
- cần cấu hình mount đúng
- cần kiểm tra quyền đọc/ghi
- performance có thể cần theo dõi nếu thư mục quá lớn

## Phương án B - Không ưu tiên
**Giữ source code trong container rồi mới export/sync ra ngoài.**

### Vì sao không ưu tiên
- dễ kẹt code trong container
- khó dùng IDE host thuận tiện
- dễ quên backup/sync
- khó tổ chức lâu dài

**Kết luận:** chọn **Phương án A**.

---

## 5) Quy tắc cho Obsidian

## 5.1. Vault Obsidian
Vault Obsidian nên là dữ liệu host thật, không đặt mặc định bên trong workspace container.

### Khuyến nghị
- Obsidian app trên Windows mở trực tiếp vault host.
- OpenClaw chỉ truy cập vault thông qua mount.
- Không dùng workspace hiện tại làm vault chính lâu dài nếu mục tiêu là tích hợp thực tế với Windows + Obsidian desktop.

## 5.2. Dữ liệu nào nên vào vault
Đưa vào vault:
- meeting notes
- meeting minutes
- decision log
- project summary
- action items
- PM templates đã chốt dùng thực tế
- knowledge base dự án

Không bắt buộc đưa toàn bộ vào vault:
- file tạm
- output trung gian
- logs hệ thống
- dependency folders như `node_modules`

---

## 6) Quy tắc cho source code và GitHub

## 6.1. Mô hình source code
Source code nên nằm trong repo riêng hoặc nhóm repo rõ ràng dưới thư mục host như:

```text
D:\Doanh\PM-Agent\repos\openclaw-workspace
D:\Doanh\PM-Agent\repos\pm-agent-skills
D:\Doanh\PM-Agent\repos\web-ban-hang
```

## 6.2. GitHub
### Khuyến nghị
- Mỗi project code quan trọng nên có remote GitHub.
- Repo tài liệu PM có thể:
  - cùng repo với project nếu scope nhỏ
  - hoặc tách repo riêng nếu cần quản trị tốt hơn

## 6.3. Quy tắc vận hành Git
- làm việc trên thư mục host/repo thật
- container chỉ mount vào để chạy/chỉnh/sinh output
- commit/push từ nơi thuận tiện nhất, nhưng phải trên cùng repo mounted
- tránh tạo repo chỉ tồn tại nội bộ container

---

## 7) Thiết kế quyền đọc/ghi

## Mục tiêu quyền
OpenClaw cần có khả năng:
- đọc vault Obsidian
- ghi note mới / cập nhật note
- đọc/ghi source code ở repo được cho phép
- không cần toàn quyền bừa bãi trên toàn ổ D

## Khuyến nghị
- chỉ mount **thư mục cần thiết**, không mount cả ổ D
- tách riêng:
  - vault Obsidian
  - repos
  - exports/backups
- nơi nào chỉ đọc thì mount read-only nếu phù hợp trong tương lai
- nơi cần agent ghi thì giữ read-write

---

## 8) Thiết kế backup

## Backup tối thiểu nên có
### Với Obsidian Vault
- backup định kỳ theo ngày/tuần
- có thể dùng:
  - Git cho note dạng text nếu phù hợp
  - hoặc copy snapshot sang thư mục backup
  - hoặc cloud sync nếu anh dùng riêng

### Với source code
- GitHub là backup/version control chính
- ngoài ra có thể giữ local clone trên host

### Với container/OpenClaw
- container không phải nguồn dữ liệu thật
- backup container chỉ là lớp phụ
- script `backup-and-recreate-docker.ps1` hữu ích, nhưng **không thay thế backup data host + GitHub**

---

## 9) Các bước triển khai thực tế đề xuất

## Giai đoạn 2.1 - Chuẩn hóa storage host
1. Tạo các thư mục thật trên Windows host.
2. Chọn vault Obsidian chính.
3. Chuyển/tổ chức source code vào thư mục repo chuẩn.

## Giai đoạn 2.2 - Mount vào Docker/WSL
1. Xác nhận WSL nhìn thấy ổ D (`/mnt/d/...`).
2. Xác nhận container nhìn thấy các mount cần thiết.
3. Chuẩn hóa các đường dẫn nội bộ như `/data/obsidian`, `/data/repos`.

## Giai đoạn 2.3 - Test quyền đọc/ghi
1. tạo file test trong vault từ container
2. sửa file test từ Windows/Obsidian
3. xác minh 2 chiều đều nhìn thấy thay đổi
4. test tạo/sửa file trong repo code

## Giai đoạn 2.4 - Chốt GitHub workflow
1. tạo hoặc gắn remote GitHub cho từng repo
2. test `pull`, `commit`, `push`
3. xác định repo nào public/private

---

## 10) Checklist xác minh thành công của Bước 2

Bước 2 được xem là ổn khi đạt đủ các điều kiện sau:
- [ ] WSL/container thấy được thư mục Obsidian thật trên host
- [ ] OpenClaw đọc/ghi được vào vault test
- [ ] source code không còn chỉ nằm trong container
- [ ] ít nhất 1 repo có remote GitHub chuẩn
- [ ] có quy ước thư mục host rõ ràng
- [ ] có đường backup tối thiểu cho vault và code

---

## 11) Trạng thái hiện tại sau khi phân tích

### Đã xác định
- Hướng đúng là **host-first storage + mounted access + GitHub for repos**.
- Chưa có bằng chứng ổ D đang được mount vào WSL/container.
- Chưa có remote GitHub cho workspace hiện tại.

### Việc nên làm tiếp ngay sau note này
1. xác minh đường dẫn thật của vault Obsidian trên Windows
2. xác minh cách Docker container hiện tại được tạo / mount ra sao
3. bổ sung mount cho vault + repo host
4. test đọc/ghi thật

---

## 12) Quyết định tạm chốt

### Quyết định hạ tầng
- **Chọn mô hình host-first**.
- **Obsidian vault nằm trên host Windows**.
- **Source code/repo nằm trên host và sync bằng Git/GitHub**.
- **Container/OpenClaw chỉ là lớp chạy và thao tác thông qua mount**.

### Không chọn
- Không chọn mô hình để dữ liệu quan trọng chỉ nằm trong container.

---

## 13) Gợi ý note tiếp theo
Note tiếp theo nên là một checklist triển khai thật, ví dụ:
- đường dẫn vault thật là gì
- repo nào cần đưa lên GitHub trước
- container hiện tại đang mount gì
- lệnh/test nào dùng để xác minh đọc ghi
