# Phase 02 — Một entry, runtime và package

## Context links

[Plan](plan.md) · [Phase 01](phase-01-contract-and-sources.md) · [Contract](product-contract.md) · [Distribution](research/distribution-review.md)

## Overview

Trạng thái: pending; phụ thuộc `CONTRACT_READY` và quyền rebuild. Tạo candidate tự chứa cùng công cụ bảo trì nhỏ, kiểm tra trong staging. Không cài vào user-scope thật ở phase này.

## Key Insights

- Một entry không có nghĩa ép mọi bài toán đi qua cùng một chuỗi câu hỏi.
- Reference trong package giúp copy sang nơi khác vẫn hoạt động mà không phụ thuộc repo cũ.
- Installer là công cụ bảo trì riêng; việc gọi FP không cấp quyền dùng installer.
- Package test chỉ chứng minh cấu trúc và an toàn thao tác, chưa chứng minh hành vi model.

## Requirements

- Một public entry đề xuất `fp`, explicit-only; xác minh tên không trùng và metadata theo docs đang áp dụng.
- Runtime giữ mục tiêu, phân biệt fact/hypothesis/unknown, hỏi ở điểm thiếu có thể đổi kết luận, cho user điều khiển phương pháp.
- Có đường giải thích trực tiếp, research chỉ đọc, phân rã/xây lại, so sánh và học tại chỗ.
- Không bắt model tự tạo file/memory, thực thi, cài đặt hoặc delegate khi gọi FP.
- Không phụ thuộc website, global FP, plugin khác, core cũ, plan hoặc vault để load runtime.
- Copy package độc lập; mọi link/reference nằm trong package, không thoát qua symlink.

## Architecture

```text
skills/fp/
  SKILL.md
  agents/openai.yaml
  references/core.md
  references/methods.md
  references/learning-context.md
scripts/manage-fp.py
tests/test_fp_package.py
docs/install.md
```

`SKILL.md` đặt hợp đồng và cách mở reference theo nhu cầu. Core giữ ranh giới/quy tắc chung; methods giải thích khi chọn, đổi và dừng; learning-context hỗ trợ nền tảng khác nhau mà không cần memory. Tránh thêm framework/router mã nguồn khi hướng dẫn và ca hành vi đủ để kiểm tra bản đầu.

Script bảo trì cung cấp validate, dry-run, install, uninstall, rollback với manifest nhỏ ghi version, target, hashes, backup và trạng thái trước thao tác. Runtime không gọi script.

## Related code files

- Tạo candidate: `skills/fp/**`, `scripts/manage-fp.py`, `tests/test_fp_package.py`, `docs/install.md`.
- Đọc đối chiếu: `.agents/skills/fp-*/`, `method/CORE.md`, contract và source register version mới.
- Chuẩn bị diff chuyển hướng: `AGENTS.md`, `README.md`, method links; chỉ kích hoạt migration khi đến gate Phase 04.
- Không xóa bốn entry cũ, vault hoặc bằng chứng để giảm lỗi discovery trong staging.

## Implementation Steps

1. Kiểm tra phiên bản baseline và contract, hướng dẫn thư mục con; kiểm tra xung đột tên `fp` chỉ đọc. Nếu phải đổi tên, ghi lựa chọn trước khi khóa package.
2. Viết entry và reference theo R01–R12. Câu trả lời rõ có thể trực tiếp; khai báo phương pháp khi mở/đổi hướng hữu ích, không nghi thức hóa từng lượt.
3. Đặt giới hạn hypothesis: có căn cứ và nhãn bất định, không chốt nguyên nhân/ưu tiên thiếu dữ liệu; không bịa chuỗi 5 Whys hoặc buộc đủ năm câu.
4. Áp dụng source register; không copy nguồn làm instruction có quyền cao hơn contract. Cá nhân hóa dựa lời user hiện tại, memory tùy host và không tự cập nhật.
5. Thêm metadata explicit-only theo schema đã xác minh; xác minh link tương đối từ root package. Giữ provenance đủ gọn, reference không kéo dependency ra ngoài.
6. Viết công cụ bảo trì với target allowlist và manifest. Target lạ phải báo conflict; target đã quản lý nhưng drift/file dư phải dừng thay thế hoặc xóa. Backup ngoài discovery.
7. Thử trong thư mục tạm: validate/dry-run; cài mới; cài lại đúng version; target lạ; file đã đổi/file dư; uninstall; rollback; phục hồi trạng thái trước install. Kiểm tra không đụng đường dẫn ngoài target/backup.
8. Copy candidate sang path độc lập có dấu cách; thử reference, hash manifest và symlink escape. Xác nhận package không chứa plans/evals/vault/transcript/profile.
9. Chạy kiểm tra phù hợp sau thay đổi; review diff và lỗi thao tác. Sửa lỗi package trong phạm vi triển khai rồi chốt candidate hash; không bắt đầu native test trước khi package đạt.
10. Soạn hướng dẫn install/rollback và diff migration. Ghi `IMPLEMENTED`, `PACKAGE_VALIDATED` cùng bằng chứng; giữ mọi claim picker/native là chưa xác minh.

## Todo list

- [ ] Candidate một entry tự chứa và explicit-only.
- [ ] Quy tắc nguồn/hypothesis/learning khớp contract.
- [ ] Installer nhỏ có manifest và chống drift/conflict.
- [ ] Staging install/uninstall/rollback và package độc lập đạt.
- [ ] Candidate được chốt version/hash.
- [ ] Hướng dẫn và diff migration sẵn review.

## Success Criteria

Package độc lập vượt các ca cấu trúc và thao tác; review không thấy dependency cũ hoặc khả năng tự ghi từ runtime. Candidate cố định đủ để thử native. Không coi exit code xanh là bằng chứng hỏi/chọn phương pháp đúng.

## Risk Assessment

Rủi ro: instruction quá dài, tên trùng, copy thiếu reference, rollback đè file người dùng. Giảm bằng reference chọn lọc, kiểm tra path/content, thử drift/conflict và dừng mutation khi không khớp manifest.

## Security Considerations

Không đụng global settings/AK. Staging target và backup được kiểm tra path; không chạy shell từ dữ liệu nguồn. Manifest không chứa secret; không đóng gói hồ sơ/memory.

## Next steps

Sang [Phase 03](phase-03-native-acceptance.md) với candidate hash cố định. Agent triển khai chịu kiểm tra metadata/path hiện hành; reviewer đối chiếu package và boundary trước native.
