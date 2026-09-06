---
type: concept
title: "5 Whys"
tags: [mental-model, root-cause-analysis]
source-count: 1
last-updated: 2026-05-03
---

## Định nghĩa
Kỹ thuật liên tục đặt câu hỏi "Tại sao?" (thường là 5 lần) cho đến khi chạm đến nguyên nhân gốc rễ hoặc sự thật cốt lõi của một vấn đề.

## Core Idea
Đây là công cụ thực hành chính để áp dụng [[first-principles-thinking]]. Khi đối mặt với một giả định, việc hỏi "tại sao" giúp bóc tách các lớp thông tin hời hợt hoặc niềm tin cũ kỹ, từ đó lộ ra những sự thật vật lý hoặc logic không thể chia nhỏ hơn.

## Điểm dừng: "Hố đen sự thật"
Rất khó để biết khi nào nên ngừng hỏi "Tại sao?". Hãy dùng **Law of the world vs Human Choice** làm thước đo:
- **Chưa tới đáy (Human Choice):** Nếu câu trả lời bắt đầu bằng *"vì team quyết..."*, *"vì design system đang vậy..."*, *"vì flow cũ là thế..."* -> Đây vẫn là lựa chọn của con người. Đào tiếp.
- **Chạm đáy (Law of the World):** Khi câu trả lời chuyển thành *"vì viewport mobile chỉ ngần đó pixels"*, *"vì transaction fee của Visa là fixed"*, *"vì user không trust stranger giữ tiền của mình"* -> Bạn đang đứng trước các hố đen sự thật (Vật lý, Toán học, Tâm lý học căn bản). Dừng.

## Kỹ thuật thoát kẹt (Analysis Paralysis)
Khi bị mông lung trong vòng lặp "Tại sao?":
- **Constraint của Deadline:** Đừng dừng vì "đã đủ sâu", hãy dừng vì "đã đủ để ra quyết định". Trọng tâm là: **Nếu đào thêm một layer nữa, quyết định hôm nay có đổi không?** Nếu không đổi, hãy ra quyết định. Đừng tiếc.
- **Biết mình ở Layer mấy:** Cảm giác "chưa tới root" không phải là bug. Không có absolute bottom (luôn còn layer psychology, behavioral economics...). Người thực thi giỏi là người biết mình đang ở layer mấy và chủ động chọn dừng. Dừng đúng lúc khó hơn đào sâu.
- **Đổi câu hỏi:** Hỏi "Nó được cấu thành từ cái gì?" thay vì "Tại sao?".
- **Thử nghiệm xóa bỏ:** "Nếu bỏ yếu tố này, giải pháp có sụp đổ không?". Nếu không sụp đổ, đó chưa phải nguyên lý gốc.

## Liên kết
- Liên quan: [[first-principles-thinking]]
- Ví dụ từ: [[first-principles-intro]]
