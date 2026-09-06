---
type: concept
title: "BRIDGE Prompting Framework"
tags: [prompt-engineering, framework, communication]
source-count: 1
last-updated: 2026-05-09
---

## Định nghĩa
Một khung cấu trúc Prompt toàn diện giúp tối ưu hóa kết quả đầu ra từ các mô hình ngôn ngữ lớn (LLM).

## Core Idea (Cấu trúc B.R.I.D.G.E)
- **Background (Bối cảnh):** Cung cấp dữ liệu nền, lý do thực hiện.
- **Role (Vai trò):** Ép AI đóng một vai chuyên gia cụ thể.
- **Instruction (Chỉ dẫn):** Nhiệm vụ cụ thể cần làm (Động từ mạnh).
- **Detail (Chi tiết):** Các yêu cầu về định dạng, độ dài, giọng văn.
- **Grounding (Dữ liệu nền):** Chỉ định tài liệu nguồn AI được phép dùng (tránh hallucination).
- **Evaluation (Đánh giá):** Tiêu chí để biết kết quả đó đã đạt yêu cầu hay chưa.

## Ứng dụng thực tế
Dùng để xây dựng các **Agent Skills** trong hệ thống Agys. Mỗi Skill nên được thiết kế dựa trên khung BRIDGE này để đảm bảo tính ổn định và chính xác.

## Liên kết
- Liên quan: [[socratic-questioning]] (để làm rõ BRIDGE).
- Nguồn: [[2026-05-09-nblm-tu-duy-phan-bien-hr-ai]]
