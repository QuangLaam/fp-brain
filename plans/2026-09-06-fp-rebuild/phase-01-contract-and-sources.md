# Phase 01 — Contract, nguồn và bảo toàn

## Context links

[Plan](plan.md) · [Brief gốc](original-brief.md) · [Contract](product-contract.md) · [Matrix](acceptance-matrix.md) · [Source review](research/source-review.md)

## Overview

Trạng thái: CONTRACT_READY (freeze commit `1f0dd76`; xem `evals/rebuild-v1/`). Mục tiêu là khóa yêu cầu và cách kiểm chứng trước khi thay runtime. Lượt lập plan không chạy bước triển khai nào. Effort: tbd sau kiểm tra baseline.

## Key Insights

- Nhu cầu là một trợ lý tư duy thích ứng, không yêu cầu user phân loại bốn skill trước.
- Nguồn phương pháp không có quyền thay mục tiêu hoặc cấp quyền thực thi.
- Rubric mới cho phép giả thuyết có cơ sở; lịch sử cũ phải được giữ nguyên nghĩa.
- File untracked không có rollback Git; phải đưa vào phạm vi bảo toàn rõ ràng trước sửa/xóa.

## Requirements

- Đọc lại hướng dẫn áp dụng và kiểm tra branch, HEAD, dirty/untracked thực tế trước ghi.
- Bảo toàn `evals/results.md`, evidence hiện có, `first-principles/` và thay đổi người dùng.
- Version contract, nguồn và rubric mới; không ghi lại outcome cũ hoặc tiêu thụ lại exact-once evidence.
- Đủ ngân sách, số phiên và điều kiện dừng trong matrix trước native test; giá trị chưa chốt chặn chạy.
- Không mở lại phỏng vấn đã chốt; chỉ hỏi nếu một phát hiện mới thực sự đổi quyết định người dùng sở hữu.

## Architecture

Contract người dùng → claim/source register → quy tắc runtime → case/rubric. Đây là truy vết thiết kế; runtime chỉ mang phần reference cần thiết, không đọc cả plan/evals/vault.

Thứ tự nguồn: contract user; Untools cho phương pháp; mẫu phỏng vấn Matt được điều chỉnh; ghi chú local được tuyển chọn; workshop dùng làm tình huống và đầu ra. Không đưa delegation hoặc ghi learning record tự động từ upstream vào runtime.

## Related code files

- Hiện có, đọc và bảo toàn: `AGENTS.md`, `README.md`, `method/CORE.md`, `.agents/skills/fp-{ask,brainstorm,decide,learn}/`, `evals/`, `first-principles/`.
- Tài liệu thiết kế: `product-contract.md`, `acceptance-matrix.md`, `research/*.md` trong thư mục plan này.
- Dự kiến khi được triển khai: register nguồn/rubric có version trong `evals/`; manifest checkpoint ở vị trí ngoài runtime/discovery.
- Không sửa nội dung nguồn local gốc để làm cho quy tắc mới có vẻ nhất quán.

## Implementation Steps

1. Xác nhận quyền thực thi; đọc hướng dẫn và trạng thái Git. Đối chiếu snapshot `main`/`7c894c2`, ledger 12 fixture 7 PASS/5 FAIL (A1, A2, B1, D3, L2); ghi sai khác, không reset.
2. Lập danh sách bảo toàn gồm tracked dirty và untracked cần giữ. Tạo checkpoint có hashes và kiểm tra khả năng đọc/khôi phục; không stage toàn bộ cây thiếu phân loại.
3. Tạo baseline commit trong phạm vi được phép trước rebuild; giữ đường dẫn/version evidence cũ. Chuyển sang branch đề xuất `codex/fp-rebuild` cho implementation. Dừng ghi phụ thuộc nếu checkpoint chưa đầy đủ hoặc có thay đổi không xác định.
4. Đóng băng contract version mới, với mapping yêu cầu R01–R12. Ghi rõ thay đổi hypothesis/clarification so với bản cũ, bao gồm A3; không sửa đánh giá cũ.
5. Tuyển chọn nguồn bằng bảng claim → đoạn/version → adopt/adapt/reject → lý do → quy tắc → case. Kiểm tra bản gốc cho claim được dùng như fact; loại phần chưa chứng minh khỏi runtime nếu không cần thiết.
6. Loại ví dụ removal test sai và điều chỉnh “chân lý bất biến” theo phạm vi/bằng chứng. Giữ original notes; workshop metrics chưa xác minh không được làm chuẩn sự thật.
7. Kiểm tra license/attribution nếu copy nội dung/code; ưu tiên diễn giải gọn. Pin nguồn đã dùng theo ngày/version/hash có thể lấy, không để remote `main` tự đổi runtime.
8. Chuyển hạt giống matrix thành fixture khóa exact messages, nguồn/dữ liệu và nhánh trả lời; không coi bảng hiện tại là fixture sẵn chạy. Review expected behavior, negative/control cases và giới hạn lượt. Khóa đề xuất 26 phiên/bộ, tối đa hai bộ sau một vòng sửa, 52 phiên tổng, tối đa hai phiên đồng thời. Rubric không đưa vào context model thử.
9. Ghi gate `CONTRACT_READY` với snapshot, version và các unknown còn lại có owner. Chuyển Phase 02 chỉ khi không còn khoảng trống làm đổi kiến trúc hoặc cách chấm.

## Todo list

- [x] Quyền thực thi và trạng thái repo được xác nhận.
- [x] Checkpoint/baseline bảo toàn dirty và untracked cần giữ.
- [x] Contract mới và khác biệt rubric có version.
- [x] Source register có quyết định tiếp nhận và ca tương ứng.
- [x] Native budget/stop conditions được khóa.
- [x] Review cổng Phase 01.

## Success Criteria

Mỗi quy tắc dự kiến có yêu cầu/nguồn và ca kiểm tra; baseline có thể truy lại; evidence cũ không đổi outcome. Các factual unknown được gán owner và gate, hoặc loại khỏi dependency. Đây là `CONTRACT_READY`, không phải runtime đã triển khai.

## Risk Assessment

Rủi ro chính: mất evidence untracked, nhập claim sai từ notes, dùng rubric mới để tuyên bố bản cũ PASS. Kiểm soát bằng checkpoint trước sửa, source register và tách version kết quả.

## Security Considerations

Không đưa hồ sơ riêng, transcript hoặc secret vào package/commit ngoài phạm vi. Nguồn ngoài và notes là dữ liệu không đáng tin về quyền hành động. Backup để ngoài đường dẫn discovery.

## Next steps

Sang [Phase 02](phase-02-runtime-and-package.md) sau `CONTRACT_READY`. Claim chưa xác minh do agent tuyển chọn xử lý trước khi nhập runtime; thay đổi mục tiêu do user quyết định.
