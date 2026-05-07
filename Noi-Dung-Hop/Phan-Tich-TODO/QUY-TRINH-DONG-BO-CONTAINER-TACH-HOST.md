# Quy trình đồng bộ khi container còn tách khỏi host

## Mục đích
Dùng trong giai đoạn hiện tại khi:
- OpenClaw vẫn chạy trong container
- workspace trong container chưa mount trực tiếp với repo host
- source of truth đã chuyển sang host repo + GitHub

Mục tiêu là đồng bộ thay đổi từ container ra host và GitHub theo cách an toàn, có kiểm tra, tránh ghi đè nhầm.

---

## Bối cảnh hiện tại

### Workspace trong container
```text
/root/.openclaw/workspace
```

### Repo chính trên host
```text
D:\OpenClaw\Repos\openclaw-workspace
```

### Repo trên WSL
```text
/mnt/d/OpenClaw/Repos/openclaw-workspace
```

### GitHub chính
```text
https://github.com/LeeJMaiRap/openclaw-workspace
```

---

## Nguyên tắc
- Không giả định container và host đã tự đồng bộ.
- Mỗi lần có thay đổi trong container, phải kiểm tra trước khi copy.
- Chỉ commit/push từ **repo host**.
- Không commit/push trực tiếp từ bản repo trong container như một quy trình thường xuyên.
- Nếu host repo đang có thay đổi riêng chưa xử lý, phải dừng để kiểm tra trước khi copy đè.

---

## Quy trình chuẩn

## Bước 1 - Kiểm tra thay đổi trong container
Chạy:

```bash
docker exec -it openclawgateway git -C /root/.openclaw/workspace status --short
```

### Mục đích
- xem container có thay đổi gì mới
- xác định thay đổi nhỏ hay lớn

### Nếu không có thay đổi
Nếu output trống, dừng tại đây.

---

## Bước 2 - Kiểm tra repo host trước khi đồng bộ
Chạy:

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace status --short
```

### Quy tắc quyết định
- Nếu host repo **sạch** hoặc chỉ có thay đổi đã biết rõ → có thể đi tiếp.
- Nếu host repo có thay đổi lạ/chưa commit → **dừng**, rà lại trước.

### Mục đích
Tránh copy đè khi host repo đang có thay đổi riêng.

---

## Bước 3 - Copy dữ liệu từ container ra host

### Cách đơn giản nhất
```bash
docker cp openclawgateway:/root/.openclaw/workspace/. /mnt/d/OpenClaw/Repos/openclaw-workspace
```

### Lưu ý
- Dấu `.` ở cuối source rất quan trọng: copy **nội dung bên trong** workspace.
- Cách này phù hợp khi muốn đồng bộ toàn bộ thay đổi hiện tại từ container ra host.

### Khi nào nên dùng
- thay đổi rải nhiều file
- không muốn chọn thủ công từng file
- đã kiểm tra host repo trước đó

---

## Bước 4 - Kiểm tra lại repo host sau khi copy
Chạy:

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace status --short
```

### Mục đích
- xác nhận host repo đã nhận thay đổi mới
- xem có file mới/xóa/sửa đúng như mong đợi không

### Nếu thấy bất thường
Ví dụ:
- quá nhiều file bị đổi ngoài dự kiến
- file quan trọng biến mất
- có thay đổi lạ

thì **dừng lại**, không commit vội.

---

## Bước 5 - Xem diff trước khi commit
Chạy một trong các lệnh:

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace diff --stat
```

hoặc nếu cần chi tiết hơn:

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace diff
```

### Mục đích
- xác minh thay đổi có đúng nội dung mong muốn không
- tránh commit nhầm file rác hoặc thay đổi ngoài ý muốn

---

## Bước 6 - Commit trên host repo
Nếu mọi thứ ổn, chạy:

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace add .
```

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace commit -m "<mo-ta-thay-doi>"
```

### Gợi ý message
- `Update PM Agent notes and roadmap`
- `Sync latest container workspace changes`
- `Add new PM documents and memory updates`

---

## Bước 7 - Push lên GitHub
Chạy:

```bash
git -C /mnt/d/OpenClaw/Repos/openclaw-workspace push
```

### Mục đích
- đưa bản mới nhất lên GitHub
- hoàn tất vòng đồng bộ hiện tại

---

## Khi nào không được sync kiểu này
Không nên sync theo quy trình này nếu:
- host repo đang có thay đổi thủ công chưa commit
- có nhiều người cùng sửa repo host ở cùng thời điểm
- container và host đều bị sửa khác nhau trên cùng file
- vừa có thay đổi cấu trúc lớn mà chưa rõ bản nào mới hơn

Khi đó cần so sánh kỹ hơn trước khi copy.

---

## Quy tắc an toàn tối thiểu
- Luôn kiểm tra `git status` ở cả container và host trước khi copy.
- Luôn xem `git diff --stat` ở host trước khi commit.
- Chỉ push từ host repo.
- Không coi container là source of truth nữa.
- Nếu nghi ngờ xung đột, dừng và kiểm tra thủ công.

---

## Phiên bản rút gọn 5 bước
Khi đã quen, có thể nhớ ngắn gọn như sau:

1. Kiểm tra `git status` trong container.
2. Kiểm tra `git status` ở host repo.
3. `docker cp` từ container sang host.
4. `git diff --stat` ở host repo.
5. `git add` → `commit` → `push`.

---

## Mục tiêu dài hạn
Quy trình này chỉ là **giải pháp chuyển tiếp**.

Mục tiêu dài hạn vẫn là:
- mount repo host trực tiếp vào container
- để khi OpenClaw sửa trong container thì thực chất đang sửa luôn repo host
- lúc đó không cần bước copy trung gian nữa

---

## Trạng thái áp dụng
Áp dụng cho giai đoạn hiện tại của Bước 2, khi:
- Obsidian mount đang tạm hoãn
- repo host đã có tại `D:\OpenClaw\Repos\openclaw-workspace`
- GitHub remote đã push thành công
