---
title: Root Cause Identification Techniques
created: 2026-05-05
wiki: first-principles
tags:
  - fpt
  - problem-solving
---

# Root Cause Identification Techniques

Khi bị "kẹt" trong vòng lặp "Tại sao?" và không biết phải hỏi thêm hay dừng lại, dùng các kỹ thuật bổ trợ:

## 1. Technique: "Decomposed Into What?"

Thay vì hỏi **"Tại sao?"** (lý do), hãy hỏi **"Nó được cấu thành từ cái gì?"** (thành phần).

**Ví dụ:**
- **Sai:** "Tại sao quản lý dự án hiệu quả?"
- **Đúng:** "Một quá trình quản lý dự án hiệu quả được cấu thành từ những thành phần nhỏ nhất nào?"
  - Sự giao tiếp rõ ràng
  - Sự minh bạch về tiến độ
  - Cam kết từ cả hai bên
  
→ Điều này giúp bạn tìm được các **viên gạch nhỏ nhất** thay vì lạc trong vòng lặp lý do.

## 2. Technique: "Removal Test"

Hãy thử loại bỏ từng yếu tố của vấn đề. **Nếu loại bỏ yếu tố A mà giải pháp vẫn tồn tại được, thì A không phải nguyên lý gốc.**

**Ví dụ:**
Vấn đề: "Tại sao khách hàng không mua sản phẩm X?"

Hãy thử loại bỏ:
- Loại bỏ "giao diện xấu" → Khách vẫn không mua (giao diện không phải nguyên nhân chính)
- Loại bỏ "giá quá cao" → Khách không mua (giá là nguyên nhân chính)

→ Bây giờ bạn tìm được nguyên lý gốc: **Mức giá không tương xứng với giá trị nhận được**.

## 3. Technique: "What Would Disappear?"

Hỏi ngược lại: **"Nếu loại bỏ yếu tố này, toàn bộ hệ thống có sụp đổ không?"**

Những yếu tố nào mà nếu mất đi → hệ thống không còn hoạt động → đó là **nguyên lý gốc**.

**Ví dụ trong Thiết kế:**
- Nếu loại bỏ "Sự tương phản màu sắc" từ giao diện → Người dùng không thể phân biệt nút bấm vs. nền → Hệ thống không sử dụng được.
- Nếu loại bỏ "Phản hồi ngay lập tức" khi người dùng bấm nút → Người dùng không biết liệu có gì xảy ra → Hệ thống mất lòng tin.

---

## Khi Nào Nên Dùng Cái Nào?

| Tình huống | Technique |
|-----------|-----------|
| Vấn đề phức tạp, nhiều nguyên nhân | Decomposed Into What? |
| Cần xác định yếu tố **không cần thiết** | Removal Test |
| Cần xác định yếu tố **tối thiểu để sống sót** | What Would Disappear? |

**Liên kết:**
- [[5-whys]]
- [[stopping-criteria-first-principles]]
- [[first-principles-thinking]]
