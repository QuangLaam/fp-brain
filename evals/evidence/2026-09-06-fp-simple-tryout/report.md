# Ba lần thử FP sau khi đơn giản hóa

Đã kết thúc: **ba phiên, mỗi phiên một lượt, không retry hoặc mở vòng sửa**.
Đây là quan sát nhỏ để bắt đầu dùng, không phải nghiệm thu toàn bộ sản phẩm.

Copy năm file từ `skills/fp/` vào `/Users/quanglaam/.agents/skills/fp/` khi target
chưa tồn tại; đối chiếu bản copy giống nguồn. [Bản ghi cài](installation.json).
Không dùng installer riêng. Không thay cấu hình chung hoặc skill khác.

Các phiên dùng executable `/Applications/ChatGPT.app/Contents/Resources/codex`
0.153.4, model `gpt-6-astra`, reasoning `high`, thư mục làm việc tạm mới;
sandbox `read-only`, approval `never`, web/plugins/memories tắt qua tham số phiên.
Global skill catalog và cảnh báo về agent definitions của host vẫn xuất hiện;
không tuyên bố môi trường cách ly hoàn toàn và không sửa host để làm sạch kết quả.

1. **Làm rõ mục tiêu — chưa hoàn chỉnh.** [Prompt](01-clarify/prompt.txt),
   [phản hồi/tool trace](01-clarify/stdout.jsonl). Đã đọc entry/core/methods của
   FP được cài. Phản hồi cuối nói bắt đầu từ tình huống cụ thể nhưng không đưa
   câu hỏi để người dùng trả lời, và chứa đoạn thừa “not necessarily speed avoid
   english.” Không đưa giải pháp sớm, nhưng chưa thực sự giúp người dùng bắt đầu
   cuộc phỏng vấn. Giữ nguyên lỗi quan sát; chưa xác định nguyên nhân chỉ từ một mẫu.
2. **Thiếu bằng chứng nguyên nhân — phù hợp trong mẫu này.**
   [Prompt](02-evidence/prompt.txt), [phản hồi/tool trace](02-evidence/stdout.jsonl).
   Đọc reference của FP; tách ba báo cáo chậm khỏi số đo/tái hiện, không bịa chuỗi
   năm nguyên nhân. Đề xuất ghi nhận một lượt thanh toán có đo rồi mới đi tiếp.
   Chỉ đề xuất kiểm chứng, không thực thi nó.
3. **Học qua UX — phù hợp trong mẫu này.** [Prompt](03-learning/prompt.txt),
   [phản hồi/tool trace](03-learning/stdout.jsonl). Đọc entry/core/learning của FP;
   giải thích loading do UI bật chưa xác nhận server nhận yêu cầu, và xác nhận
   tiếp nhận cũng chưa đồng nghĩa xử lý thành công. Không mở cuộc phỏng vấn thừa.

Cả ba tiến trình kết thúc exit 0; nhận xét trên dựa vào nội dung và các lệnh đọc,
không lấy exit code làm đánh giá chất lượng. Trace ghi các lệnh đọc reference,
không thấy lệnh ghi file hay giao việc của model. Candidate không được sửa sau thử.

Một đường gọi CLI ngoài repo đã đọc đúng bản global. Chưa có quan sát picker
Desktop hoặc phản hồi về công việc thật của người dùng. Không chuyển kết quả
hai mẫu phù hợp thành lời bảo đảm cho mọi repo, mọi host hoặc mọi câu hỏi.
