# Brief gốc và nguồn người dùng chỉ định

Đây là yêu cầu gốc của người dùng trong cuộc trao đổi, được giữ riêng để đối chiếu mọi quyết định trong [plan](plan.md). Những nội dung đã làm rõ sau đó nằm trong [hợp đồng sản phẩm](product-contract.md); chúng không được trình bày như nguyên văn brief gốc.

## Yêu cầu gốc

> Tôi muốn bạn hiểu lại concept của repo này 1 lần nữa. Đây là repo sẽ giúp tôi xử lý problem gặp phải:
>
> - Giúp tôi đưa giải pháp dựa trên việc đào sâu đến gốc rễ vấn đề, không phải để agent chốt trước mà khi cần, sẽ phải phỏng vấn tôi dựa trên nguồn grill-me (tham khảo)
> - Giúp tôi học hỏi được những điều mới dựa trên background của tôi: non-tech, UX/UI designer, và tham khảo thêm trong memory của codex/ChatGPT.
> - Có thể là một agent hoạt động gọi được ở mọi repo, mọi nơi bằng lệnh slash $.
>
> Nguồn để xây:
>
> - [https://untools.co/first-principles/](https://untools.co/first-principles/)
> - [https://github.com/mattpocock/skills/tree/main/skills/productivity](https://github.com/mattpocock/skills/tree/main/skills/productivity)
> - /Users/quanglaam/fp-brain/first-principles
>
> Hiện tại yêu cầu này có hợp lý hay không? Có cần làm rõ vấn đề gì hay không?

Đường dẫn nguồn local: [first-principles](../../first-principles/). Khoảng trắng thừa sau đường dẫn trong tin nhắn được bỏ khi ghi lại; nội dung yêu cầu không thay đổi.

## Từ brief gốc tới những điều đã làm rõ

| Ý định gốc | Làm rõ qua phỏng vấn, được user đồng ý | Quy tắc và ca kiểm tra |
|---|---|---|
| Đào sâu để đưa giải pháp; phỏng vấn khi cần; không chốt trước | Agent có thể nêu giả thuyết có căn cứ, chủ động research; hỏi phần thiếu có thể đổi kết luận. Nêu phương pháp/lý do, cho user chỉ định Socratic/5 Whys, đổi hướng và dừng. | R02–R08/R12; N01–N16 và N20. |
| Học theo background UX/UI, non-tech; tham khảo memory | Học trong việc đang giải quyết; dùng lời hiện tại trước thông tin cũ; không giữ user ở mức non-tech; không có memory vẫn hoạt động. | R09–R11; N03/N17–N19. |
| Gọi thuận tiện ở mọi repo/mọi nơi | Một điểm vào, trải nghiệm gọi trong Codex như AK. Codex là phạm vi bản đầu; repo khác và task không project phải được kiểm chứng. Chưa xác nhận hỗ trợ mọi nền tảng hoặc chia sẻ memory Codex/ChatGPT tự động. | R01/R11; cổng P/D1/D2/U. |

Tra ID tại [hợp đồng](product-contract.md) và [ma trận](acceptance-matrix.md). Tên `fp`, vị trí `skills/fp/`, cách copy package, script bảo trì và ngân sách test là đề xuất kỹ thuật trong plan, không phải lời người dùng trong brief gốc.

## Vai trò của nguồn bổ sung

Ba nguồn trên là nguồn gốc bắt buộc phải đối chiếu khi rebuild. Workshop bốn level và các ảnh từ thầy được người dùng bổ sung làm ví dụ về ứng dụng, học và tiêu chí đầu ra; chúng không thay thế ba nguồn gốc. AK là tham chiếu về sự thuận tiện khi gọi skill, không phải nguồn phương pháp FP.

Xem [đối chiếu nguồn](research/source-review.md) để biết phần kế thừa, điều chỉnh hoặc không đưa vào runtime cùng lý do. Chưa truy được bằng chứng cho một claim thì phải ghi trạng thái đó, không tự nâng thành sự thật hoặc âm thầm bỏ cả nguồn.
