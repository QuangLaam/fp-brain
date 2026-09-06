---
type: concept
title: "First Principles Thinking"
tags: [mental-model, problem-solving]
source-count: 1
last-updated: 2026-05-03
---

## Định nghĩa
Tư duy Nguyên lý gốc là quá trình phân rã một vấn đề phức tạp thành các yếu tố cơ bản nhất (những sự thật không thể phủ nhận) và xây dựng lại giải pháp từ con số 0.

## Core Idea
Thay vì tư duy theo *phép loại suy* (làm theo kinh nghiệm cũ hoặc những gì đã có tiền lệ), phương pháp này ép người giải quyết vấn đề phải đào sâu đến tận cùng của logic. Nó yêu cầu loại bỏ mọi giả định (assumptions) để chỉ giữ lại những mảnh ghép cốt lõi.

## Ứng dụng thực tế: 3 Bước Thực hành (Untools)
1. **Nhận diện giả định:** Bạn đang tin vào điều gì? (Ví dụ: "Làm content tốn nhiều tiền").
2. **Phân rã thành sự thật cơ bản:** "Một video content cần gì?" -> Camera, kịch bản, diễn viên, nền tảng phân phối.
3. **Xây dựng lại từ đầu:** Camera có sẵn trên điện thoại, kịch bản có AI hỗ trợ, nền tảng phân phối miễn phí -> Thực ra làm content tốn thời gian, không tốn tiền.

## Mental Model: Chiều ngang vs Chiều dọc
- **Chiều ngang (Horizontal):** Cách tiếp cận quen thuộc của BA/Designer (liệt kê đủ screens, đủ states, đủ edge cases). Nó tốt cho việc "bọc lót" nhưng không giải quyết gốc rễ.
- **Chiều dọc (Vertical - FPT):** Bỏ qua options, chọn 1 pain point rồi đào ngược tới root constraint (Law of the world).

## Ép AI đào chiều dọc (Prompt)
AI mặc định có xu hướng chiều ngang (liệt kê danh sách, đưa ra options). Để dùng AI làm đối tác FPT, hãy dùng prompt chặn đầu này:
> "Analyze [problem] using first principle. No options, no lists. Each turn dig one layer deeper into assumptions. Start by surfacing the hidden assumption in how I'm framing this."
> Lặp lại: "What assumption is this answer based on? Why is that assumption true?"
> Chốt: "Is this a law of the world, or still a human choice?"

## Cảnh báo từ Daniel Kahneman (Hệ thống 1 & 2)
FPT đòi hỏi năng lượng tư duy cực lớn (Hệ thống 2). Đừng áp dụng nó cho mọi quyết định nhỏ nhặt (ví dụ: "Hôm nay ăn gì?"). Hãy để dành nó cho các quyết định mang tính bước ngoặt, có độ rủi ro cao hoặc cần sự sáng tạo đột phá (tham khảo [[fpt-decision-matrix]]).

## Liên kết
- Kỹ thuật bổ trợ: Sử dụng [[5-whys]] để phân rã vấn đề. Sử dụng [[feynman-technique]] để kiểm chứng mức độ hiểu nguyên lý.
- Ví dụ từ: [[first-principles-intro]]
- Entities: [[elon-musk]]
