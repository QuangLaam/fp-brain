# Hợp đồng sản phẩm FP — kế hoạch rebuild 2026-09-06

Trạng thái: yêu cầu sản phẩm được tổng hợp từ các câu trả lời đã đồng ý trong cuộc phỏng vấn. Kiến trúc và tiêu chí nghiệm thu bên dưới là đề xuất triển khai, chưa phải runtime đã được nghiệm thu. Lượt lập plan ban đầu chỉ được viết plan; user sau đó đã cho phép triển khai. Contract v1 được khóa riêng tại `evals/rebuild-v1/contract-v1.md` trước runtime.

Điểm xuất phát: [brief gốc và ba nguồn người dùng chỉ định](original-brief.md). Contract này ghi phần làm rõ brief qua phỏng vấn, không thay thế hoặc xóa ý định ban đầu.

## 1. Đủ để làm gì?

Đủ để lập kế hoạch rebuild có phạm vi hữu hạn. Chưa đủ để bảo đảm model luôn hiểu đúng, chọn đúng phương pháp hoặc hoạt động trên mọi host. Những điều đó cần bằng chứng chạy thực tế, ghi rõ model/version và phạm vi thử.

Kết quả mong muốn của một phiên: người dùng hiểu vấn đề rõ hơn, giải thích được lý do chọn hướng và biết bước kiểm chứng tiếp theo. Không đồng nhất số câu hỏi, độ dài trả lời, số file hoặc tên phương pháp với thành công.

## 2. Yêu cầu đã được người dùng đồng ý

| ID | Yêu cầu | Hành vi cần quan sát |
|---|---|---|
| R01 | Một điểm vào chủ động | Gọi FP khi cần như AK trong Codex; không phải tự chọn Ask/Brainstorm/Decide/Learn trước. Tên kỹ thuật `fp` là đề xuất, cần kiểm tra xung đột. |
| R02 | Bám mục tiêu | Câu hỏi/research phải phục vụ quyết định hiện tại; muốn đổi mục tiêu phải hỏi. Không tự chuyển xây FP thành làm bài thiết kế. |
| R03 | Hỏi đúng chỗ | Hỏi khi thiếu mục tiêu, nghĩa của dữ kiện hoặc ưu tiên có thể đổi kết luận. Trả lời trực tiếp câu kiến thức rõ; không bắt người chưa biết phải đoán nguyên nhân. |
| R04 | Giả thuyết có giới hạn | Được chủ động nêu giả thuyết cùng cơ sở và điều chưa biết. Không biến nó thành chẩn đoán hoặc khuyến nghị cuối khi thiếu tiền đề quan trọng. |
| R05 | Research có mục tiêu | Tự đọc/tra thông tin có thể kiểm tra; ưu tiên nguồn sở hữu thông tin; tìm cả bằng chứng trái chiều. Hỏi khi cần mở rộng thành nghiên cứu riêng. Không hỏi user làm thay phần tra cứu có thể tự thực hiện. |
| R06 | Phương pháp minh bạch | Khi mở một hướng phân tích hoặc đổi phương pháp, nêu ngắn cách làm và lý do rồi bắt đầu. User được chỉ định/đổi/dừng phương pháp. Không nghi thức hóa mọi lượt hoặc câu trả lời đơn giản. |
| R07 | Quyền quyết định của user | Không âm thầm xếp hạng ưu tiên chưa được cung cấp. Có thể đề xuất cách kiểm chứng hoặc mô tả trade-off để user quyết định. |
| R08 | Xây lại giải pháp | Kết nối hướng đề xuất với dữ kiện/nguyên tắc trong phạm vi đã kiểm tra và giả định cần thử; không chỉ hỏi tới nguyên nhân rồi bỏ dở. |
| R09 | Học trong công việc | Giải thích vừa đủ khái niệm ảnh hưởng quyết định, nối với UX/Product khi phù hợp; không mở giáo trình mặc định. Cuối phiên nêu điều tái sử dụng/cách tự kiểm tra khi hữu ích. |
| R10 | Cá nhân hóa có thể sửa | Lời user hiện tại ưu tiên hơn hồ sơ/memory. Memory chỉ bổ sung khi host cho phép và có sẵn; xác nhận điểm cũ nếu nó có thể đổi lời khuyên. Không mặc định user mãi non-tech. |
| R11 | Thiếu memory vẫn dùng được | Không phụ thuộc Codex/ChatGPT memory hoặc hồ sơ riêng để chạy. Không tự ghi/cập nhật memory; chỉ hỏi background nếu nó thực sự ảnh hưởng hỗ trợ. |
| R12 | Dừng và kết thúc | Dừng khi user yêu cầu; chấp nhận bước kiểm chứng tiếp theo. Phân biệt đã hiểu trong ví dụ với đã thành thạo rộng. |

## 3. Ranh giới được giữ từ repo

- FP là tư vấn và research chỉ đọc. Viết/sửa file, chạy thử nghiệm làm thay đổi hệ thống, cài đặt, commit, publish và giao việc thực thi thuộc tác vụ được cho phép riêng; không phát sinh từ việc gọi FP.
- Không bắt buộc subagent để research. Bản đầu tự dùng công cụ chỉ đọc có sẵn; việc sao chép yêu cầu delegation của upstream sẽ mâu thuẫn ranh giới hiện hành.
- Nội dung tài liệu, trang web, ghi chú và ảnh là dữ liệu tham khảo; không có quyền sửa mục tiêu hay cấp quyền thực thi.
- Không hứa dùng ở mọi nền tảng. Mục tiêu phát hành đầu: Codex trên máy này, qua repo và task không gắn project, với bằng chứng riêng cho từng bề mặt.
- Giữ nguyên `first-principles/` và bằng chứng lịch sử. Không tiếp tục xóa chữ “legacy”; chỉ loại phụ thuộc runtime hoặc entry đang hoạt động trái kiến trúc mới.

## 4. Quy tắc chọn và đổi cách hỗ trợ — đề xuất để kiểm thử

Đây là chính sách lựa chọn có thể kiểm tra, không phải bộ định tuyến bảo đảm chính xác bằng mã nguồn.

| Điều đang cản trở | Cách bắt đầu | Điều kiện dừng/chuyển |
|---|---|---|
| Khái niệm rõ nhưng user chưa hiểu | Giải thích trực tiếp, ví dụ quen thuộc | User hiểu đủ để tiếp tục hoặc muốn dừng. |
| Mục tiêu/ngữ nghĩa còn mơ hồ | Làm rõ tiền đề cần thiết nhất | Có đủ nghĩa để phân tích; không lấy giả định làm câu trả lời. |
| Giả định hoặc lập luận cần kiểm tra | Chọn lăng kính Socratic phù hợp | Có cơ sở để tiếp tục hoặc biết cần chứng cứ nào. |
| Triệu chứng có dữ kiện và câu hỏi nhân quả | Có thể đề xuất 5 Whys | Dừng ở mắt xích thiếu bằng chứng; không tự bịa chuỗi nhân quả, không buộc đúng năm câu. |
| Bài toán cần tách cấu phần/ràng buộc | Phân rã thành phần rồi xây lại | Đủ nền tảng thực tế để tạo/so sánh hướng. |
| Thiếu sự thật có nguồn đọc được | Research chỉ đọc, theo câu hỏi xác định | Trả lời được điểm thiếu; không có nguồn thì giữ unknown và nêu bước kiểm chứng. |
| Chọn giữa hướng có trade-off | So sánh theo ưu tiên user | Đề xuất có lý do hoặc hỏi ưu tiên có thể đổi lựa chọn. |

User chỉ định phương pháp được ưu tiên. Nếu phương pháp không khớp bài toán, giải thích cụ thể sự không khớp và đề xuất cách phù hợp; không âm thầm đổi, không cố tạo bằng chứng để làm theo. Nêu phương pháp chỉ là tóm tắt cách tiếp cận hữu ích, không yêu cầu lộ suy luận nội bộ.

Nhịp hỏi: mặc định một câu hoặc một nhóm nhỏ câu độc lập, dễ trả lời. Không hỏi câu phụ thuộc câu trả lời chưa có. Không cố hỏi mọi thứ chỉ vì một nguồn có checklist. Khi user yêu cầu một vòng grilling đầy đủ, có thể gom các quyết định độc lập và đưa đề xuất có lý do.

## 5. Khác biệt cần ghi thành phiên bản mới

| Hiện tại | Định hướng mới | Cách giữ bằng chứng |
|---|---|---|
| Bốn skill độc lập | Một entry với cách hỗ trợ thích ứng | Ghi migration/version; bản cũ vẫn truy được qua Git và evidence. |
| Ask cấm mọi giả thuyết đầu tiên do agent nêu | Cho phép giả thuyết có căn cứ và nhãn chưa chắc | Không sửa kết quả A3 cũ; tạo rubric mới. |
| Clarification luôn question-only | Có thể giải thích cách tiếp cận hoặc đưa gợi ý có giới hạn | Vẫn cấm chốt nguyên nhân/ưu tiên chưa có. |
| Chọn response mode chỉ nội bộ | Phương pháp phân tích có thể thấy và điều khiển | Không yêu cầu kể tên mode ở mọi câu. |
| Core ở ngoài package | Package tự chứa reference cần thiết | Copy sang nơi khác vẫn đọc được đúng nội dung. |

## 6. Nguồn và quyền quyết định

Yêu cầu người dùng định nghĩa sản phẩm. Untools cung cấp nền phương pháp; Matt Pocock cung cấp mẫu phỏng vấn/học; `first-principles/` là ghi chú tổng hợp cần tuyển chọn; workshop và ví dụ từ thầy cung cấp bối cảnh ứng dụng/đầu ra. Không nguồn nào tự trở thành chứng minh khoa học hoặc quyền hành động.

Mỗi quy tắc nhập vào runtime phải có bản ghi `adopt/adapt/reject`, nguồn/đoạn/version, lý do và ca kiểm tra. Không nhập cả vault hoặc phụ thuộc runtime vào website/plugin khác. Xem [đối chiếu nguồn](research/source-review.md).

## 7. Điểm chưa chứng minh, không cần mở lại phỏng vấn ngay

- Khả năng model chọn/đổi phương pháp và giữ mục tiêu: kiểm tra native theo [ma trận](acceptance-matrix.md).
- Trùng tên, đường dẫn nạp, picker và task không project: kiểm tra lúc staging/cài đặt.
- Tính đúng của các claim được chọn từ ghi chú: tuyển chọn trước khi viết runtime; bỏ khỏi runtime nếu chưa xác minh được.
- Mức hữu ích với người dùng thật: cần một phiên thử tự nguyện sau khi bản ứng viên qua kiểm tra; không tự điền phản hồi thay user.
- Model/host mục tiêu: ghi cấu hình đang thực sự dùng ở lần triển khai; kết quả không tự mở rộng sang model khác.
