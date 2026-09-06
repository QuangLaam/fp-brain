# Lịch sử — đã được thay thế

Ngày 2026-09-06, người dùng chọn đơn giản hóa FP: một skill, cài bằng copy và tối
đa ba cuộc hội thoại thử. **Kế hoạch rebuild nhiều phase, custom lifecycle và bộ
26 ca/52 sessions đã dừng.** Không tiếp tục batch recovery hoặc dùng quyền/budget
trong các tài liệu cũ để chạy việc mới.

Giữ nguyên các đường dẫn sau để không phá liên kết và bằng chứng lịch sử. Chúng
nằm ngoài đường discovery của skill và không phải hướng dẫn công việc hiện tại:

- [Plan rebuild cũ](../plans/2026-09-06-fp-rebuild/plan.md), các phase và migration patch.
- [Fixtures/rubric đã khóa](../evals/rebuild-v1/README.md), [runner cũ](../evals/rebuild-v1/run-native.py) và [host amendment chưa chạy](../evals/rebuild-v1/host-recovery-v1.md).
- [Lượt native bị host chặn](../evals/evidence/2026-09-06-fp-rebuild-native-bounded-01/report.md): giữ nguyên raw evidence và 1 session đã tiêu thụ; không chấm thành lỗi hành vi hay dùng lại slot đó.
- [Kết quả bốn skill cũ](../evals/results.md), [core cũ](../method/CORE.md) và [ghi chú nguồn](../first-principles/).

Commit `d667f9d` bảo toàn phần rebuild đang dở trước simplification. Custom
installer/tests và bốn entry cũ được giữ trong Git history; bản đang dùng chỉ có
[skills/fp](../skills/fp/SKILL.md). Tài liệu hiện hành: [README](../README.md),
[cài đặt](install.md), [trạng thái và thử dùng](../STATUS.md).
