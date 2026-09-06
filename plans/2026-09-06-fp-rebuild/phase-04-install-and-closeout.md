# Phase 04 — Cài đặt, chuyển đổi và closeout

## Context links

[Plan](plan.md) · [Phase 03](phase-03-native-acceptance.md) · [Matrix](acceptance-matrix.md) · [Distribution](research/distribution-review.md)

## Overview

Trạng thái: pending; phụ thuộc `NATIVE_ACCEPTED` và scope cho phép cài đặt user-scope cùng migration cụ thể. Hoàn tất đường gọi thật trong Codex, phản hồi người dùng và trạng thái phát hành có giới hạn. Không hỏi lại quyền đã được cấp trong yêu cầu triển khai toàn plan.

## Key Insights

- Có thư mục trong `~/.agents/skills` chưa chứng minh picker thấy đúng skill hoặc task mới nạp đúng content.
- Task trong repo và task không project cần bằng chứng riêng.
- “Giống AK” là trải nghiệm gọi chủ động; không phải quyền sửa AK hay host settings.
- User feedback không thể do agent điền thay hoặc suy ra từ test tự động.

## Requirements

- Trình bày candidate version/hash, target, file changes, backup và rollback cụ thể trước bước cấp quyền cuối.
- Target đề xuất `~/.agents/skills/fp/`; không tạo thêm bản cùng tên trong `.agents/skills` repo.
- Chỉ cài bằng script đã thử staging; conflict/drift thì dừng thao tác liên quan, không ghi đè.
- Backup/manifest đặt ngoài discovery; không gỡ hoặc rollback đè thay đổi phát sinh của user.
- Chỉ retire bốn entry cũ sau khi candidate và đường gọi mới đạt cổng chuyển đổi; giữ core/source/evidence lịch sử truy được.
- Fresh picker, new task trong repo, projectless và user feedback có kết quả riêng theo matrix.
- Ngân sách: một native preflight ở fixture repo khác, ba native session sau migration (repo nguồn/repo khác/projectless), một lượt picker UI, một phiên dùng thật. Mỗi mục một lần; lỗi được báo và xử lý rollback, không tự chạy lại cho tới PASS. Rollback verification chỉ kiểm tra khôi phục, không phải rerun nghiệm thu.

## Architecture

`skills/fp/` là nguồn chuẩn → copy version cố định → user-scope discovery → explicit invocation trong task mới. Installer/manifest quản lý bản copy; runtime chỉ đọc reference trong chính package.

Migration tài liệu trỏ vào nguồn chuẩn/cách cài mới. Bốn entry cũ rời active discovery theo diff được phép, nhưng có checkpoint để khôi phục. Core cũ còn trong lịch sử hoặc vị trí lịch sử đã chốt, không là dependency runtime mới.

## Related code files

- Nguồn chuẩn: `skills/fp/**`; công cụ: `scripts/manage-fp.py`; hướng dẫn: `docs/install.md`.
- Target thật sau quyền riêng: `/Users/quanglaam/.agents/skills/fp/`; manifest/backup ngoài discovery.
- Migration: `.agents/skills/fp-{ask,brainstorm,decide,learn}/`, `AGENTS.md`, `README.md`, các method links đang mô tả kiến trúc hoạt động.
- Ledger phát hành và evidence mới trong `evals/` theo cấu trúc đã chốt; không sửa `first-principles/` hoặc kết quả rubric cũ.

## Implementation Steps

1. Đối chiếu candidate hash với native acceptance và kiểm tra lại target/discovery chỉ đọc. Soạn dry-run, allowlist, backup, diff retirement/docs và cách khôi phục thành một thay đổi review được.
2. Đối chiếu quyền hiện có với target và diff đã chuẩn bị. Quyền viết plan không cấp quyền cài; nếu user đã cho triển khai toàn plan gồm phase này thì tiếp tục, không xin lại. Chỉ hỏi phần cài/migration còn ngoài phạm vi đã được cấp, với thay đổi cụ thể sẵn review.
3. Kiểm tra preconditions một lần nữa; checkpoint trạng thái target thật, chạy install đúng candidate. Nếu target lạ/drift/file dư, báo xung đột; không xóa hoặc mở rộng allowlist tùy tiện.
4. Xác minh manifest và hashes bản copy. Ghi `INSTALLED` khi file đã cài đúng; chưa tuyên bố picker hoặc sản phẩm được nghiệm thu.
5. Trong fixture repo khác dành riêng cho kiểm tra, xác minh explicit invocation chọn đúng bản user-scope đã cài bằng path/hash. Đây là preflight chuyển đổi, chưa là toàn bộ D1/D2; chưa retire entry đang dùng nếu chưa xác minh được candidate mới.
6. Sau preflight, áp dụng diff retire bốn entry cũ và chuyển hướng `AGENTS.md`, README, method links. Chỉ sửa phần mô tả kiến trúc hoạt động, giữ hướng dẫn cá nhân liên quan và lịch sử truy được.
7. Kiểm tra D1 trong fresh contexts của repo nguồn sau migration, repo fixture khác và task không project; kiểm tra D2 trên picker Codex Desktop hiện tại. Ghi paths/hashes và quan sát UI thật. Không còn entry cũ cạnh tranh/bản `fp` trùng; không sửa dự án khác hoặc global settings để ép PASS. Nếu fail, chuyển ngay bước 9, chưa thử U.
8. Thực hiện một phiên dùng thật do user tự nguyện chọn bài toán. Thu phản hồi trực tiếp về hiểu vấn đề, lý do lựa chọn, quyền điều khiển và bước kiểm chứng; không tự dựng feedback hoặc đổi sang bài design riêng.
9. Nếu check sau retirement fail, khôi phục cả global target lẫn đúng migration patch của repo theo checkpoint trong quyền rollback đã cấp; không `git reset --hard`. Kiểm tra drift trước khôi phục, giữ evidence lỗi; drift thì dừng phần xung đột để bảo toàn công việc mới. U thiếu feedback ghi `NOT_RUN`, chưa `PRODUCT_ACCEPTED`.
10. Closeout với version, file changes, package/native/discovery/user-feedback verdict riêng, residual và cách gọi/khôi phục. `PRODUCT_ACCEPTED` chỉ khi đạt đủ matrix và user feedback bắt buộc; commit/publish chỉ theo quyền hiện hành.

## Todo list

- [ ] Gói cài/diff migration/rollback sẵn review.
- [ ] Phạm vi được phép đã bao phủ cài và migration.
- [ ] Target copy và manifest đúng candidate.
- [ ] Fresh picker, repo task và projectless có evidence riêng.
- [ ] Bốn entry cũ retire có rollback; tài liệu hoạt động thống nhất.
- [ ] Phiên dùng thật và feedback do user cung cấp.
- [ ] Closeout ghi rõ accepted/remaining và cách sử dụng.

## Success Criteria

Người dùng gọi một FP đã cài trong các bề mặt mục tiêu, package nạp đúng nguồn và không còn cạnh tranh entry cũ. Kết quả user thật đáp ứng tiêu chí matrix. Nếu chỉ cài thành công mà chưa có UI/feedback, báo chính xác `INSTALLED`, chưa `PRODUCT_ACCEPTED`.

## Risk Assessment

Discovery trùng/cache, target drift, retirement sớm và feedback thiếu là các rủi ro chính. Kiểm soát bằng staging trước, hash/provenance, fresh UI/task evidence và retirement sau cổng đường gọi mới; không mở vòng thử không giới hạn.

## Security Considerations

Giới hạn mutation ở target/backup và file migration được phép; không sửa AK, host settings hoặc memory. Backup không trở thành một skill được discover. Giữ dữ liệu bài toán thật tối thiểu trong evidence và không publish transcript riêng.

## Next steps

Sau closeout, dùng FP cho công việc thực tế. Cải tiến tiếp dựa phản hồi cụ thể qua một scope/version mới; không tự tạo automation, mở rộng nền tảng hoặc tiếp tục rebuild ngoài mục tiêu này.
