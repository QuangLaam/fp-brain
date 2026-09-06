# Trạng thái FP — 2026-09-06

**Đã thu gọn và cài một `$fp` để dùng thử.** Nguồn chuẩn là
[skills/fp](skills/fp/SKILL.md); bản copy dùng chung nằm tại
`/Users/quanglaam/.agents/skills/fp/`. Mở task mới trong Codex để gọi `$fp`.

Bốn entry cũ và custom installer/tests đã rời phần hoạt động. Nguồn gốc,
ghi chú và bằng chứng cũ được giữ; [lịch sử](docs/history.md) không phải kế hoạch
đang tiếp tục. Không chạy lại bộ 26 ca hoặc vòng sửa tự động.

Đã kiểm tra cấu trúc, liên kết cần dùng và bản copy năm file. Ba cuộc hội thoại
thực bằng CLI 0.153.4 / gpt-6-astra đã kết thúc:

| Tình huống | Quan sát |
|---|---|
| Mục tiêu cải thiện công việc thiết kế chưa rõ | Nạp đúng FP nhưng chỉ nói sẽ làm rõ, chưa hỏi cụ thể; có đoạn tiếng Anh thừa. Còn điểm chất lượng chưa giải quyết. |
| 5 Whys khi chỉ có ba báo cáo thanh toán chậm | Phân biệt báo cáo với bằng chứng, dừng chuỗi nguyên nhân và đề xuất đo/tái hiện. |
| Giải thích loading và xác nhận từ server | Giải thích trực tiếp, chính xác và gắn với UX. |

[Báo cáo và phản hồi nguyên văn](evals/evidence/2026-09-06-fp-simple-tryout/report.md).
Không sửa prompt rồi chạy lại để tìm kết quả đẹp hơn. Ba ví dụ không bảo đảm mọi
hành vi; picker Desktop và mức hữu ích với bài toán thật của bạn chưa được đánh giá.
Bước tiếp theo là dùng FP trong công việc, ghi lỗi cụ thể nếu gặp.
