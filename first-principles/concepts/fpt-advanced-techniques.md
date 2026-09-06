---
title: FPT Advanced Techniques
aliases: [Các kỹ thuật FPT nâng cao]
tags: [concept, framework, problem-solving]
---

# Các Kỹ thuật Phân tích Nâng cao

Bên cạnh [[5-whys]], bộ công cụ [[first-principles-thinking]] (FPT) còn được bổ trợ bởi các kỹ thuật nâng cao giúp ép "Hệ thống 2" (tư duy chậm, phân tích) hoạt động và vô hiệu hóa các [[cognitive-biases]].

## 1. Pre-mortem (Phân tích Tiền Thất bại)
Được đề xuất bởi Gary Klein, kỹ thuật này chống lại thiên kiến lạc quan bằng cách chuyển lợi thế của "hindsight" (góc nhìn nhận lại) sang "foresight" (dự đoán).
- **Cách làm:** Giả định dự án đã *thất bại thảm hại* trong 12 tháng tới. Cả nhóm cùng viết ra mọi lý do dẫn đến sự sụp đổ đó.
- **Tích hợp FPT:** Với từng "rủi ro chết người" tìm được, dùng 5 Whys để đào xuống nguyên nhân hệ thống và thiết kế lại quy trình (constraint) để chặn rủi ro đó từ trong trứng nước.

## 2. Inversion Thinking (Nghĩ Ngược)
*"Invert, always invert"* - Carl Jacobi / Charlie Munger. Thay vì hỏi làm sao để thắng, hãy hỏi làm sao để không thua.
- **Cách làm:** 
  1. Viết bài toán: "Làm sao đạt X?"
  2. Đảo ngược: "Làm sao chắc chắn TẠO RA kết quả tệ nhất (không đạt X)?"
  3. Lập danh sách các hành vi dẫn đến kết quả tệ đó, và dùng làm Checklist những việc **tuyệt đối không được làm (Anti-patterns)**.

## 3. Steel-manning (Lập luận Thép)
Đối lập với "Straw-man" (Bóp méo lập luận của đối thủ để dễ chửi), Steel-manning là việc xây dựng phiên bản *mạnh nhất có thể* của quan điểm đối lập trước khi phản biện.
- **Tích hợp FPT:** Trước khi chốt một "Nguyên lý nền tảng", hãy ép bản thân tự Steel-man một mô hình đối lập. Đưa ra các ví dụ và bằng chứng tốt nhất cho nó. Nếu nguyên lý của bạn vẫn đứng vững, nó mới là nguyên lý thật sự.

## 4. Fermi Estimation (Ước lượng Fermi)
Kỹ thuật ước lượng bậc độ lớn (order-of-magnitude) cho các câu hỏi thiếu dữ liệu.
- **Cách làm:** Phân rã bài toán thành vài yếu tố ước lượng được (ví dụ: số ngày x số giờ x tỷ lệ chuyển đổi), dùng các con số có lý, rồi nhân/chia. Các sai số thường tự triệt tiêu nhau.
- **Tích hợp FPT:** Dùng Fermi làm thước đo định lượng cho FPT, chỉ ra các giả định (explicit assumptions) thay vì phán đoán theo cảm tính.

## 5. Second-order Thinking (Tư duy Bậc 2)
Howard Marks phân biệt tư duy Bậc 1 (phản ứng trực tiếp, tuyến tính) và Bậc 2 (hỏi tiếp "So what?").
- **Tích hợp FPT:** Trong mọi phân tích, thêm bước liệt kê ít nhất 3 hệ quả vòng hai (Second-order consequences) nếu giải pháp thành công hoặc thất bại.
