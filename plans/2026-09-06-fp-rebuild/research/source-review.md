# Đối chiếu nguồn — 2026-09-06

Nguồn live/địa phương đã được đọc để lập kế hoạch; đây không phải native acceptance hay kiểm định toàn bộ claims.

[Brief gốc](../original-brief.md) chỉ định ba nguồn: Untools, thư mục productivity của Matt Pocock và `/Users/quanglaam/fp-brain/first-principles`. Ba nguồn này là đầu vào phải đối chiếu; các nguồn còn lại trong bảng là phần liên quan được tuyển chọn hoặc ví dụ bổ sung, không thay thế brief.

| Nguồn | Vai trò | Cách kế thừa |
|---|---|---|
| [Untools](https://untools.co/first-principles/) | Nền phương pháp | Giữ hai phần phân rã và xây lại. Socratic/Why là kỹ thuật hỗ trợ, không đồng nhất toàn bộ FP với hỏi nguyên nhân. Dùng sự thật trong phạm vi có bằng chứng. |
| [Matt productivity](https://github.com/mattpocock/skills/tree/main/skills/productivity), [grill-me](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grill-me/SKILL.md), [grilling](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md) | Mẫu phỏng vấn | `grill-me` hiện gọi `grilling`. Nhận quy tắc phụ thuộc câu hỏi và tách facts/decisions. Điều chỉnh nhịp hỏi cho user; không nhập mặc định toàn bộ vòng hỏi, delegation hoặc nghi thức. |
| [teach](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/SKILL.md), [learning record](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/teach/LEARNING-RECORD-FORMAT.md), [wait-what](https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/wait-what/SKILL.md) | Nguồn bổ sung nếu cần cho learning | Bài ngắn theo khả năng, feedback, giải thích lại khi chưa hiểu. Không nhập workspace học, HTML, ghi memory, khóa học hoặc ngôn ngữ tiếng Anh bắt buộc. Không cần triển khai mọi skill trong thư mục productivity. |
| [Ghi chú local](../../../first-principles/) | Tổng hợp/heuristic, không phải toàn bộ nguồn nguyên thủy | Chỉ lấy đoạn cần thiết sau đối chiếu. Các link dạng `05 References/Articles/...` có thể cần truy bản gốc; chưa đọc bản gốc thì ghi rõ. Giữ nguyên bản ghi chú. |
| [Workshop L1](https://jangtrinh.github.io/lam-workshop/levels/level-1-foundation.html), [L2](https://jangtrinh.github.io/lam-workshop/levels/level-2-design-system.html), [L3](https://jangtrinh.github.io/lam-workshop/levels/level-3-prototype.html), [L4](https://jangtrinh.github.io/lam-workshop/levels/level-4-production.html) | Tình huống áp dụng và tiêu chí đầu ra | Chuỗi context → design rules → prototype → QA giúp tạo tình huống học/thử; không biến FP thành công cụ chỉ làm design system. Không nhập lời hứa tốc độ/chất lượng chưa xác minh. |
| Ảnh trao đổi với thầy và cuộc phỏng vấn hiện tại | Bối cảnh và yêu cầu của user | Thành công gắn với kết quả có thể đánh giá; hình thư viện component không chứng minh workflow tự động hay năng lực hiện tại của user. |

## Mâu thuẫn cụ thể cần chặn khỏi runtime

- [Removal test](../../../first-principles/concepts/root-cause-identification.md): ví dụ loại “giá quá cao”, khách vẫn không mua nhưng kết luận giá là nguyên nhân chính. Kết luận không được chứng minh bởi dữ kiện đó. Không mang ví dụ này vào quy tắc nhân quả.
- [Stopping criteria](../../../first-principles/concepts/stopping-criteria-first-principles.md): liệt kê chi phí nguyên liệu và hành vi người như chân lý bất biến. Cần giới hạn phạm vi, thời điểm và bằng chứng; không dùng nhãn “nguyên lý gốc” để bỏ qua kiểm chứng.
- [Provenance cũ](../../../evals/provenance.md) ghi quyết định sản phẩm bốn skill và nhịp Ask. Đó là lịch sử thiết kế, không phủ quyết yêu cầu mới đã được user đồng ý.
- Register cũ bên ngoài repo `/Users/quanglaam/fp-brain-rebuild-planning/rebuild-contract.yaml` chỉ dùng đối chiếu lịch sử, không là dependency của bản mới.

## Điều kiện tiếp nhận nguồn ở phase 1

1. Ghi URL/path, tác giả/nguồn sở hữu, đoạn áp dụng, ngày và commit/hash khi khả dụng.
2. Lập bảng claim → adopt/adapt/reject → lý do → quy tắc → ca kiểm thử. Tách claim của nguồn khỏi tính đúng đã được xác minh.
3. Nếu tái sử dụng nguyên văn/code từ upstream, kiểm tra license/attribution trước khi phân phối; ưu tiên diễn giải ngắn. Không cần chép nguyên trang vào repo.
4. Nguồn đổi trên `main` không tự thay runtime. Mọi thay đổi phải được review và version lại.
5. Không nâng ghi chú chưa truy được nguồn gốc thành fact bắt buộc. Có thể bỏ claim đó và tiếp tục phần build không phụ thuộc vào nó.

Giới hạn: đã đọc nguồn chọn lọc và toàn bộ văn bản 4 level qua agent; không kiểm định toàn bộ vault, nghiên cứu bên ngoài hoặc khả năng các tool trong workshop. Không sửa nguồn/bằng chứng.
