# Telegram Voice Ingest Report

## Input
- **Audio:** /root/.openclaw/workspace/tmp/voice/about-doanh.ogg
- **Context:** voice note test
- **Transcript file:** /root/.openclaw/workspace/tmp/voice/transcripts/20260514-034025-semi-auto-test.md

## STT Result
- **Language:** vi
- **Probability:** 1
- **Confidence note:** High - có thể đi tiếp workflow nếu nội dung không chứa dữ liệu mơ hồ quan trọng.

## Transcript
Anh doanh là người chăm chỉ, học công nghệ nghiêm túc, làm việc có định hướng, luôn muốn mọi thứ rõ ràng, thực tế và tiến bộ hơn qua từng ngày.

## Suggested Route
- **Route:** `direct-reply-or-manual-review`
- **Why:** Không đủ tín hiệu mạnh để auto-route; nên đọc transcript và xử lý thủ công.

## Operator Rules
- Nếu transcript chứa deadline, số liệu, tên riêng hoặc quyết định quan trọng mà còn mơ hồ -> xác nhận lại trước.
- Nếu confidence không cao -> ưu tiên manual review trước khi đẩy vào PM workflow.
- Nếu route là `direct-reply-or-manual-review` -> chưa nên auto đẩy sang skill PM.
