# Bước 2 - Checklist triển khai hạ tầng Obsidian + Docker + GitHub

## Mục tiêu checklist
Biến thiết kế hạ tầng ở file `BUOC-2-THIET-KE-HA-TANG-THUC-TE.md` thành các bước triển khai thật, có thể kiểm tra được.

Mục tiêu cuối:
- OpenClaw đọc/ghi được Obsidian vault thật trên Windows.
- Source code/project không bị kẹt trong container.
- GitHub được dùng làm version control/backup cho repo quan trọng.
- Có quy trình kiểm tra rõ trước khi chuyển sang Bước 3.

---

## 0) Quyết định nền đã chốt

- Dùng mô hình **host-first storage + mounted access + GitHub for repos**.
- Host Windows giữ dữ liệu thật.
- Docker/container chỉ mount dữ liệu vào để thao tác.
- Không để vault Obsidian, source code, skill quan trọng chỉ sống trong container.

---

## 1) Giai đoạn 2.1 - Xác định đường dẫn thật trên Windows

## 1.1. Xác định vault Obsidian thật
Anh cần xác định vault Obsidian đang hoặc sẽ nằm ở đâu.

### Phương án đề xuất
```text
D:\Doanh\ObsidianVault\
```

### Checklist
- [ ] Anh xác nhận tên vault Obsidian muốn dùng.
- [ ] Anh xác nhận đường dẫn thật trên Windows.
- [ ] Nếu chưa có vault, tạo vault mới bằng Obsidian desktop.
- [ ] Không đặt vault chính trong container.

### Thông tin đã chốt
```text
OBSIDIAN_VAULT_NAME = OpenClaw-Vault
OBSIDIAN_VAULT_WINDOWS_PATH = D:\OpenClaw\Obsidian\OpenClaw-Vault
OBSIDIAN_VAULT_WSL_PATH = /mnt/d/OpenClaw/Obsidian/OpenClaw-Vault
```

### Trạng thái
- [x] Anh đã tạo vault Obsidian mới.
- [x] Tên vault: `OpenClaw-Vault`.
- [x] Đường dẫn vault thật trên Windows: `D:\OpenClaw\Obsidian\OpenClaw-Vault`.
- [x] Đường dẫn vault thật trên WSL: `/mnt/d/OpenClaw/Obsidian/OpenClaw-Vault`.
- [x] WSL đã đọc được vault, thấy `.obsidian` và `Welcome.md`.

---

## 1.2. Xác định thư mục source code/repo trên Windows

### Phương án đã chốt
```text
D:\OpenClaw\Repos\
```

### Checklist
- [x] Đã chốt thư mục repo/source code trên host: `D:\OpenClaw\Repos\`.
- [x] Đã tạo thư mục `D:\OpenClaw\Repos\` và WSL đã thấy tại `/mnt/d/OpenClaw/Repos`.
- [x] Xác định repo đầu tiên cần đưa ra host: `openclaw-workspace`.
- [x] Đã copy workspace từ container ra host tại `/mnt/d/OpenClaw/Repos/openclaw-workspace` (`D:\OpenClaw\Repos\openclaw-workspace`).
- [x] Kiểm tra repo host đã đủ file và trạng thái Git đúng.
  - Đã xác nhận nhiều file `M` ban đầu là do file mode `100644 => 100755` khi copy sang ổ D.
  - Đã cấu hình `core.filemode false` cho repo host.
  - Sau khi sửa, trạng thái Git chỉ còn các thay đổi thật: `MEMORY.md`, `projects/web-ban-hang/frontend/index.html` và các file/thư mục mới cần xét commit.
- [ ] Không tiếp tục phát triển source code quan trọng chỉ trong `/root/.openclaw/workspace` nếu chưa có kế hoạch sync.

### Repo ưu tiên nên xử lý trước
```text
openclaw-workspace hoặc pm-agent-workspace
web-ban-hang
pm-agent-skills nếu sau này tạo skill riêng
```

---

## 1.3. Xác định thư mục exports/backups

### Phương án đề xuất
```text
D:\Doanh\PM-Agent\exports\
D:\Doanh\PM-Agent\backups\
```

### Checklist
- [ ] Tạo thư mục exports.
- [ ] Tạo thư mục backups.
- [ ] Quy ước exports là nơi chứa file sinh ra tạm/thành phẩm.
- [ ] Quy ước backups là nơi chứa snapshot/backup thủ công.

---

## 2) Giai đoạn 2.2 - Kiểm tra WSL có thấy ổ D không

## 2.1. Kiểm tra trong WSL Ubuntu trên Windows
Chạy trong terminal WSL của Windows:

```bash
ls -la /mnt
ls -la /mnt/d
ls -la /mnt/d/Doanh
```

### Kết quả mong muốn
- `/mnt/d` tồn tại.
- WSL đọc được thư mục `D:\Doanh\...`.

### Nếu `/mnt/d` không tồn tại
Cần kiểm tra WSL automount.

Gợi ý file WSL:
```bash
cat /etc/wsl.conf
```

Cấu hình thường cần có:
```ini
[automount]
enabled = true
root = /mnt/
```

Sau khi chỉnh, chạy từ PowerShell:
```powershell
wsl --shutdown
```

Rồi mở lại WSL và kiểm tra lại `/mnt/d`.

---

## 2.2. Kiểm tra Docker/container có thấy mount không
Trong phiên hiện tại đã kiểm tra:

```text
/mnt gần như trống
```

Anh đã chạy:

```bash
docker exec -it openclawgateway ls -la /mnt/d/OpenClaw/Obsidian/OpenClaw-Vault
```

Kết quả:

```text
No such file or directory
```

Anh đã chạy tiếp:

```bash
docker inspect openclawgateway --format '{{json .Mounts}}'
```

Kết quả:

```json
[]
```

Kết luận: container OpenClaw hiện tại **chưa có mount nào** và **chưa thấy Obsidian vault**.

### Checklist
- [ ] Xác định container hiện tại được chạy bằng `docker run`, Docker Desktop UI, hay compose.
- [ ] Xác định image/container name hiện tại là `openclawgateway` hay tên khác.
- [ ] Xác định cần recreate container hay có cách thêm mount qua Docker Desktop.

### Lệnh kiểm tra từ PowerShell/CMD Windows
```powershell
docker ps
docker inspect openclawgateway
```

Nếu muốn xem mount ngắn gọn:
```powershell
docker inspect openclawgateway --format "{{json .Mounts}}"
```

---

## 3) Giai đoạn 2.3 - Thiết kế mount Docker chính thức

## 3.1. Mount point nên dùng trong container
Để dễ nhớ và ổn định, trong container nên dùng:

```text
/data/obsidian
/data/repos
/data/exports
/data/backups
```

## 3.2. Mapping đề xuất
Ví dụ nếu host dùng cấu trúc đề xuất:

```text
D:\Doanh\ObsidianVault        -> /data/obsidian
D:\Doanh\PM-Agent\repos      -> /data/repos
D:\Doanh\PM-Agent\exports    -> /data/exports
D:\Doanh\PM-Agent\backups    -> /data/backups
```

## 3.3. Docker run mẫu
Nếu recreate container bằng `docker run`, lệnh mẫu sẽ có dạng:

```powershell
docker run -d `
  --name openclawgateway `
  -p 22:22 `
  -p 18789:18789 `
  -p 3000:3000 `
  -p 5000:5000 `
  -v "D:\Doanh\ObsidianVault:/data/obsidian" `
  -v "D:\Doanh\PM-Agent\repos:/data/repos" `
  -v "D:\Doanh\PM-Agent\exports:/data/exports" `
  -v "D:\Doanh\PM-Agent\backups:/data/backups" `
  openclawgateway:backup-YYYY-MM-DD
```

### Lưu ý quan trọng
- Không chạy ngay lệnh trên nếu chưa backup container.
- Tên image `openclawgateway:backup-YYYY-MM-DD` phải thay bằng image thật.
- Nếu container hiện tại có thêm env/config/volume khác, phải giữ lại khi recreate.
- Cần inspect container hiện tại trước để tránh mất cấu hình.

---

## 4) Giai đoạn 2.4 - Backup trước khi recreate container

Hiện đã có script:
```text
docs/pm-agent/SCRIPTS/backup-and-recreate-docker.ps1
```

Nhưng script hiện tại mới chủ yếu backup/recreate theo port mapping, chưa chắc đã thêm volume mount mới.

### Checklist an toàn
- [ ] Chạy `docker ps` để xác nhận container.
- [ ] Chạy `docker inspect openclawgateway > openclawgateway-inspect.json` để lưu cấu hình cũ.
- [ ] Backup container bằng `docker commit`.
- [ ] Export container bằng `docker export` nếu cần.
- [ ] Chỉ recreate sau khi có danh sách mount/env/port đầy đủ.

### Lệnh backup mẫu PowerShell
```powershell
$DATE = Get-Date -Format "yyyy-MM-dd-HH-mm-ss"
docker inspect openclawgateway > "openclawgateway-inspect-$DATE.json"
docker commit openclawgateway "openclawgateway:backup-$DATE"
docker export openclawgateway > "openclawgateway-backup-$DATE.tar"
```

---

## 5) Giai đoạn 2.5 - Test quyền đọc/ghi Obsidian

Sau khi mount xong, chạy trong container/OpenClaw:

```bash
ls -la /data/obsidian
printf "OpenClaw write test at $(date -Is)\n" > /data/obsidian/OPENCLAW_WRITE_TEST.md
cat /data/obsidian/OPENCLAW_WRITE_TEST.md
```

### Kiểm tra từ Windows
- [ ] Mở vault Obsidian.
- [ ] Thấy file `OPENCLAW_WRITE_TEST.md` xuất hiện.
- [ ] Sửa nội dung file từ Obsidian/Windows.

### Kiểm tra lại từ container
```bash
cat /data/obsidian/OPENCLAW_WRITE_TEST.md
```

### Kết quả đạt
- [ ] Container tạo file được trong vault.
- [ ] Windows/Obsidian thấy file đó.
- [ ] Windows sửa file, container đọc lại được.

Sau khi test xong có thể xóa file test hoặc chuyển vào thư mục test riêng.

---

## 6) Giai đoạn 2.6 - Test quyền đọc/ghi repo source code

Sau khi mount `/data/repos`, chạy trong container/OpenClaw:

```bash
ls -la /data/repos
mkdir -p /data/repos/openclaw-mount-test
printf "OpenClaw repo mount test at $(date -Is)\n" > /data/repos/openclaw-mount-test/README.md
cat /data/repos/openclaw-mount-test/README.md
```

### Kiểm tra từ Windows
- [ ] Thư mục `openclaw-mount-test` xuất hiện trong `D:\Doanh\PM-Agent\repos`.
- [ ] Windows sửa được file.
- [ ] Container đọc lại được thay đổi.

---

## 7) Giai đoạn 2.7 - Chốt GitHub workflow

## 7.1. Repo nào nên đưa lên GitHub trước
Ưu tiên:
1. repo PM Agent/OpenClaw workspace hoặc tài liệu cấu hình quan trọng
2. project `web-ban-hang` nếu còn dùng
3. skill tự viết sau này

## 7.2. Quy trình với repo mới
Trong thư mục repo host:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
```

## 7.3. Quy trình với repo đã có sẵn local
```bash
git remote -v
git status
git remote add origin <GITHUB_REPO_URL>
git push -u origin main
```

### Checklist GitHub
- [ ] Chốt repo nào public/private.
- [ ] Tạo repo trên GitHub.
- [ ] Gắn remote.
- [ ] Push thử thành công.
- [ ] Pull thử thành công.

---

## 8) Giai đoạn 2.8 - Quy ước vận hành sau khi mount xong

### Với Obsidian
- OpenClaw chỉ tạo/sửa note theo quy tắc trong `docs/pm-agent/STORAGE-RULES.md`.
- Không ghi tùy tiện mọi đoạn chat vào vault.
- Tài liệu PM, meeting minutes, decision log, project summary mới đưa vào vault.

### Với source code
- Code quan trọng phải nằm trong `/data/repos/...` hoặc repo host-mounted tương đương.
- Trước khi sửa project, kiểm tra `git status`.
- Sau khi sửa, test/lint/build nếu có.
- Commit theo từng nhóm thay đổi rõ nghĩa.

### Với backup
- Container backup chỉ là phụ.
- Source of truth là host + GitHub + backup vault.

---

## 9) Tiêu chí hoàn thành Bước 2

Bước 2 hoàn thành khi:

- [x] Đã xác định vault Obsidian thật trên Windows.
- [ ] Đã xác định thư mục repos/source code thật trên Windows.
- [ ] Container/OpenClaw thấy được `/data/obsidian`.
- [ ] Container/OpenClaw thấy được `/data/repos`.
- [ ] Test đọc/ghi Obsidian hai chiều thành công.
- [ ] Test đọc/ghi repo hai chiều thành công.
- [x] Ít nhất một repo quan trọng có remote GitHub.
  - Repo: `openclaw-workspace`
  - Host path: `D:\OpenClaw\Repos\openclaw-workspace`
  - GitHub: `https://github.com/LeeJMaiRap/openclaw-workspace`
  - Branch: `main`
  - Commit đã push: `799fa40` - `Move workspace to host and update PM Agent roadmap`
- [x] TODO.md được cập nhật trạng thái Bước 2.

### Trạng thái tạm thời
- Phần **mount Obsidian vào container** đang được **tạm hoãn** theo quyết định hiện tại.
- Những mục liên quan đến `/data/obsidian` và test đọc/ghi Obsidian sẽ được làm tiếp sau.
- Có thể tiếp tục các phần khác của Bước 2 trước, ví dụ:
  - chuẩn hóa thư mục repo/source code trên host
  - chốt workflow Git/GitHub
  - thiết kế mount cho repo code sau

---

## 10) Các thông tin còn thiếu cần anh xác nhận

Để triển khai thật, cần anh xác nhận 4 thông tin:

1. Vault Obsidian hiện đã có chưa? Nếu có, đường dẫn Windows là gì?
2. Anh muốn dùng thư mục host chuẩn là `D:\Doanh\PM-Agent\...` hay tên khác?
3. Repo nào cần đưa lên GitHub trước?
4. GitHub repo nên để public hay private?

---

## 11) Việc em có thể làm tiếp sau khi anh cung cấp thông tin

Sau khi anh xác nhận đường dẫn và repo:
- em có thể cập nhật checklist này bằng đường dẫn thật
- em có thể viết script PowerShell recreate container an toàn có mount mới
- em có thể viết lệnh test đọc/ghi riêng cho máy anh
- em có thể cập nhật TODO.md thành trạng thái đang triển khai/đã hoàn thành từng mục
