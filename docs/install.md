# Cài hoặc cập nhật FP

Nguồn chuẩn là thư mục `skills/fp/` trong repo này. Copy nguyên năm file của
package vào `~/.agents/skills/fp/`; mọi reference đi cùng package. Không cần
installer riêng, plugin hay cấu hình global bổ sung.

Nếu target **chưa tồn tại**, chạy từ repo:

```sh
mkdir -p "$HOME/.agents/skills"
cp -R skills/fp "$HOME/.agents/skills/fp"
```

Nếu target đã tồn tại, kiểm tra thay đổi riêng trước. Giữ một bản backup của
thư mục hiện tại ở nơi **ngoài** `~/.agents/skills`, rồi thay đúng thư mục `fp`
bằng bản nguồn đã xem. Không copy lồng thêm `fp/fp`, không ghi đè công việc riêng
chưa đối chiếu. Muốn khôi phục, thay bản hiện tại bằng backup đó; muốn gỡ, chỉ gỡ
bản `fp` đã xác định, không đụng skill khác.

Sau copy, mở task mới trong Codex và gọi `$fp`. Nếu host không nạp được skill,
ghi lỗi thực tế và dừng; thư mục được copy đúng chưa chứng minh hội thoại hoạt
động. Xem [giới hạn hiện tại](../README.md).
