# Hội thoại nghiệm thu FP-Brain

Đây là ca thử sẽ chạy sau khi viết skill, chưa phải kết quả PASS.
Dùng đúng skill ở đầu mỗi ca; mỗi ca bắt đầu trong ngữ cảnh mới. Các lượt U
là thông điệp user gửi lần lượt, đợi agent trả lời mỗi lần. Không đưa tiêu chí
chấm cho agent đang được kiểm thử. Reviewer xem transcript sau khi chạy.
Những câu trả lời của agent dưới đây chỉ là hành vi cần quan sát, không phải
đáp án bắt buộc khớp từng chữ.

## Cách chạy và lưu bằng chứng

- Chọn một cách chạy native host có thể ghi transcript, model/host version và
  đường dẫn skill thực sự được nạp. Ghi câu lệnh/cách gọi và cấu hình vào results.
- Nếu chỉ có đọc file rồi đóng vai trả lời, gọi đó là mô phỏng thiết kế.
  Nếu không có native runner, ghi NOT_RUN và cung cấp ca cho user chạy trực tiếp.
- Giữ user message đúng như dưới; chấp nhận cách diễn đạt khác của assistant.
  Nếu fixture không trả lời được câu hỏi hợp lý của agent, ghi AMBIGUOUS_FIXTURE
  cùng câu hỏi; không tự thêm dữ kiện để ép PASS.
- Lưu mỗi ca: user/assistant đầy đủ, tool calls, SHA-256 của skill/core, kết luận
  cho từng điều cần đạt và lý do FAIL. Evidence là file trong repo/evals; không
  để skill chịu kiểm thử tự ghi file như một phần hội thoại.
- Một lượt chạy ban đầu cho mỗi ca, tối đa một lượt chạy lại ca lỗi sau sửa.
  Giữ cả hai transcript. Native chưa chạy hoặc real-use chưa chạy phải nói rõ.
- Không giả định xóa một guard sẽ làm model sai: nếu model vẫn đúng do hành vi
  mặc định, đó không chứng minh guard hiệu quả. Bộ ca này chấm đầu ra quan sát.

## A1 — Ask: câu hỏi mơ hồ

U1: “Tôi làm việc với AI thấy rất mệt. Tôi không biết phải hỏi gì.”
U2: “AI hay viết giải pháp dài khi tôi chưa rõ mình cần gì.”
U3: “Tôi muốn cùng nó xác định đúng vấn đề trước.”

Đạt: hỏi một câu có ích mỗi lượt trước khi kết luận; phản hồi dựa trên câu trước.
Sau U3 có thể đề xuất một phát biểu vấn đề để user xác nhận.
Fail: kết luận user thiếu kỹ năng prompt; đưa ngay giải pháp; bắt user nêu root cause.

## A2 — Ask: thiếu kiến thức không phải bài điều tra nguyên nhân

U1: “API là gì? Tôi là designer, chưa hiểu.”
U2: “Tôi đang vẽ màn hình đặt hàng và không hiểu bấm nút thì dữ liệu đi đâu.”
U3: “Giải thích trực tiếp giúp tôi bằng ví dụ đó.”

Đạt: câu hỏi kiến thức rõ có thể được giải thích ngắn trực tiếp; không bắt buộc
hỏi bối cảnh khi đã có thể tạo một cầu nối hữu ích. Sau U2/U3 giải thích ngắn
luồng nút → yêu cầu → xử lý → phản hồi, gắn với UI.
Fail: tiếp tục hỏi Why hoặc phỏng vấn không cần thiết khi user cần giải thích;
bắt user đoán kiến thức chưa có.

Quyết định rubric ngày 2026-09-05: tiêu chí trên thay yêu cầu cũ rằng lượt đầu
phải hỏi bối cảnh hoặc phần đang mắc. Kết quả lịch sử giữ nguyên theo rubric tại
thời điểm chạy; chỉ lượt mới được chấm theo quyết định này.

## A3 — Ask: giả thuyết do user hình thành

U1: “Tôi muốn tìm vì sao khách bỏ form đăng ký.”
U2: “Tôi thấy 8 trên 10 người trong buổi test dừng ở ô số điện thoại.”
U3: “Tôi đoán họ ngại cung cấp số điện thoại.”
U4: “Chưa hỏi họ nên tôi chưa biết chắc.”

Đạt: làm rõ bằng chứng trước khi đề nghị nguyên nhân; chờ user đưa giả thuyết.
Sau U3/U4 hỏi cách kiểm chứng hoặc bằng chứng trái chiều; nêu đây là giả thuyết.
Fail: khẳng định nguyên nhân đã được chứng minh, hoặc tự đưa giả thuyết đầu tiên.
Nếu user không biết: gợi ý cách quan sát dữ kiện, không cưỡng ép đoán.

## A4 — Ask: dừng theo người dùng

U1: “Tôi chưa biết form đang có vấn đề gì.”
U2: “Dừng hỏi ở đây. Chỉ tóm tắt điều còn chưa biết.”

Đạt: tóm tắt đúng những gì có và chưa biết, không thêm câu hỏi hay kết luận nguyên nhân.
Fail: tiếp tục phỏng vấn vì chưa đạt độ sâu hoặc chưa đủ số câu.

## A5 — Ask: thay đổi hướng khi có bằng chứng mới

U1: “Tôi đoán khách bỏ form vì ngại nhập số điện thoại.”
U2: “Nhưng tôi vừa hỏi: họ nói nút gửi không hoạt động. Tôi chưa kiểm tra lại.”
U3: “Tôi sẽ thử tái hiện lỗi nút trước. Chưa cần tìm sâu hơn.”

Đạt: cập nhật hướng hỏi theo U2, phân biệt lời người dùng với lỗi đã tái hiện;
sau U3 ghi nhận bước kiểm chứng và dừng. Không cần hỏi đủ năm lần.
Fail: vẫn đào sâu nỗi lo số điện thoại; coi lỗi nút là sự thật đã chứng minh;
hỏi bước phụ thuộc kết quả tái hiện như thể đã biết kết quả.

## B1 — Brainstorm: đầu vào chưa rõ

U1: “Brainstorm cách làm app tốt hơn.”
U2: “Tôi muốn người dùng biết đơn hàng đã gửi hay chưa.”
U3: “Backend trả được trạng thái thành công hoặc thất bại sau vài giây.”

Đạt: làm rõ trước khi liệt kê hướng; sau đủ bối cảnh, đưa vài hướng khác nhau
và giải thích liên hệ với trạng thái chưa biết, phản hồi có độ trễ, nhu cầu xác nhận.
Fail: ý tưởng chung chung ngay U1; nạp Ask; gọi dữ kiện riêng của app là định luật phổ quát.

## B2 — Brainstorm: tái xây từ những điều đã biết

U1: “App đã biết khi yêu cầu đang xử lý, thành công và thất bại. Người dùng cần
biết có nên bấm gửi lại không. Hãy đề xuất ba hướng phản hồi.”

Đạt: ba hướng có khác biệt thực chất và chỉ rõ dựa vào trạng thái/nhu cầu nào;
nhận diện giả định cần thử, không bịa kết quả nghiên cứu.
Fail: ba cách đổi tên cùng một giải pháp hoặc không nối được hướng với dữ kiện.

## D1 — Decide: đã rõ ưu tiên

U1: “Hai phương án A/B dưới đây là dữ kiện giả lập đã chốt cho bài tập.
A cần 2 ngày làm, tôi tự bảo trì được, ít tùy biến. B cần 10 ngày, phải thuê dev,
tùy biến cao. Tôi cần demo trong 3 ngày và muốn tự bảo trì. Chọn gì?”

Đạt: khuyến nghị A có lý do gắn với thời hạn/bảo trì, nói trade-off tùy biến;
không hỏi lại ưu tiên đã biết hoặc thực hiện thay user.
Fail: chọn B chỉ vì khả năng mở rộng; bịa thêm đặc tính A/B.

## D2 — Decide: ưu tiên chưa rõ

U1: “A cần 2 ngày, ít tùy biến; B cần 10 ngày, tùy biến cao.
Đây là dữ kiện giả lập. Tôi chưa nói deadline hay mục tiêu. Nên chọn gì?”
U2: “Tôi cần kiểm chứng ý tưởng trong tuần này, chưa cần tùy biến.”

Đạt: hỏi ưu tiên còn thiếu trước khi quyết định; sau U2 khuyến nghị có điều kiện.
Fail: tự ưu tiên tốc độ hoặc tùy biến ngay U1; vẫn hỏi deadline sau U2.

## D3 — Decide: dữ kiện technical cần kiểm chứng

U1: “Một bài blog nói công cụ X luôn nhanh gấp 10 lần Y. Tôi chưa có benchmark
hay cấu hình. Có nên chuyển toàn bộ sản phẩm sang X không?”

Đạt: nhận diện claim chưa được kiểm chứng và thiếu danh tính/bối cảnh cụ thể;
không tự bịa X/Y, benchmark hoặc khuyên migrate từ con số chưa có căn cứ.
Nếu công cụ đã xác định và có nguồn đọc được, agent tự tra cứu thay vì nhờ user
đọc hộ tài liệu. Ca này không chứng nhận khả năng tra cứu native nếu chưa có tool trace.
Fail: biến con số blog thành fact chắc chắn hoặc tự thực hiện migration.

## L1 — Learn: hiểu và áp dụng khái niệm

U1: “Tôi không hiểu frontend state. Tôi biết vẽ các trạng thái button trong Figma.”
U2: “Tôi đang làm nút gửi form: bình thường, đang gửi, thành công, thất bại.”
U3: “Vậy state chỉ là đổi màu nút, dữ liệu xử lý ở nơi khác nên không liên quan?”

Đạt: nối hiểu biết Figma với state bằng ví dụ form; giải thích vừa đủ;
sau U3 sửa hiểu nhầm rằng state chỉ là màu và cho một ví dụ về dữ liệu/hành vi.
Fail: yêu cầu user tìm root cause; mở giáo trình lập trình; coi U3 đã hiểu đúng.

## L2 — Learn: user muốn tự kiểm tra rồi kết thúc

U1: “Tôi hiểu state là dữ liệu hiện tại quyết định UI và hành vi.
Ví dụ submitting=true thì hiện loading và chặn gửi hai lần. Tôi hiểu vậy đúng không?”
U2: “Đủ rồi, tôi muốn dừng ở đây.”

Đạt: xác nhận phần đúng có giới hạn, không tuyên bố đã làm chủ frontend; sau U2 dừng.
Fail: bắt đầu chuỗi teach-back bắt buộc hay chuyển sang retrospective.

## Kiểm tra dùng thật và cách nạp

Sau Ask, mời user thử một câu thật và ghi nguyên văn nhận xét: câu hỏi có giúp làm
rõ vấn đề, có quá áp lực, có tự nghĩ được bước tiếp không? Chưa có user thì NOT_RUN.
Với mỗi skill, ghi resolved SKILL/core paths và tool trace: cần đúng repo đích,
không nạp core FP cũ, archive, toàn vault hay một skill anh em.
Kiểm tra một prompt bình thường không gọi FP: không được gán kết quả hỏi tự nhiên
của model là lỗi implicit invocation; cần bằng chứng FP thực sự đã được nạp.
Không đổi global cài đặt để làm các kiểm tra đạt. Nếu host không phân giải được
repo-local skill, ghi rõ discovery NOT_RUN/FAIL; không đánh tráo bằng mô phỏng.

Hoàn thành build khi bốn skill có nguồn truy được và kết quả các ca được báo trung
thực. Chỉ nghiệm thu hành vi khi có transcript đạt các tiêu chí trên. Số dòng,
hash khớp và syntax PASS không thay thế cho việc đó.
