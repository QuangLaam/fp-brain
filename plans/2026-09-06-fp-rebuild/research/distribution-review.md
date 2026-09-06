# Đóng gói và cách gọi — 2026-09-06

## Bằng chứng và đề xuất

[Tài liệu OpenAI](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) mô tả user skills trong `$HOME/.agents/skills`, repo skills trong `.agents/skills`, và tên trùng không được gộp. Catalog hiện tại có AK từ `/Users/quanglaam/.agents/skills/ak-*`; đây là bằng chứng discovery trong phiên, không là test UI mới cho FP.

Chọn **nguồn chuẩn `skills/fp/` trong repo**, copy đầy đủ package vào `~/.agents/skills/fp/` khi đến phase phân phối được cho phép. Không để thêm bản cùng tên trong `.agents/skills` của repo sau chuyển đổi. Copy tự chứa giảm phụ thuộc đường dẫn repo và cho phép rollback theo phiên bản; symlink là khả năng host có hỗ trợ nhưng không phải lựa chọn đề xuất ở đây.

Các reference phải nằm trong package và tính từ skill root, theo [Agent Skills specification](https://agentskills.io/specification#file-references). Không đóng gói vault, plan, evals, transcript hoặc hồ sơ riêng của user.

## Cây file dự kiến

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

Một script bảo trì tách khỏi runtime: validate, dry-run, install, uninstall, rollback. Package không gọi script này. Metadata đặt `allow_implicit_invocation: false`; xác minh cú pháp từ docs tại thời điểm build.

## Tính toàn vẹn và rollback

- Manifest cài đặt chứa version, target, hashes, backup và trạng thái trước cài. Backup/manifest đặt ngoài cây discovery.
- Target chưa tồn tại: dry-run rồi install đúng allowlist. Target lạ: báo xung đột, không ghi đè.
- Target do script quản lý nhưng có file thay đổi/file dư: báo drift, không xóa hoặc rollback đè lên công việc người dùng.
- Staging thử đường dẫn có dấu cách; copy sang vị trí độc lập; xác minh toàn bộ reference vẫn tồn tại và không thoát package qua symlink.
- Chỉ thay `CODEX_HOME` không đủ chứng minh cô lập skill user. Kiểm tra selected path/content trong trace.
- Cài/gỡ/khôi phục thử trong thư mục tạm trước; thao tác thật là phase riêng. Không sửa AK hoặc global host settings để ép PASS.

## Giới hạn chứng minh

Tách package validation, native behavior trong staging, discovery ở host thật, picker UI và phiên dùng thật. CLI/IDE docs có `$`/`/skills`; không suy diễn UI Codex Desktop hiện tại từ tài liệu giao diện sản phẩm khác. Picker và task không project phải được quan sát riêng. Không tự tuyên bố ChatGPT web/Claude/Antigravity được hỗ trợ.

Không install, chạy native test hoặc thay file global trong lần nghiên cứu này.
