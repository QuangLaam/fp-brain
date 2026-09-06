---
title: "Rebuild FP thành một skill tư vấn tự chứa"
description: "Kế hoạch có cổng kiểm chứng cho contract, runtime, native behavior và cài đặt Codex."
status: in_progress
priority: P2
effort: tbd
branch: codex/fp-rebuild
tags: [fp, advisory, rebuild, native-acceptance]
created: 2026-09-06
---

# Kế hoạch rebuild FP

Lượt lập plan ban đầu chỉ tạo kế hoạch. User sau đó đã cho phép triển khai toàn plan; phase 01/02 đang được thực hiện trong branch `codex/fp-rebuild`. Các phase cần quyền thực thi bao phủ thao tác tương ứng. Nếu user sau đó cho triển khai toàn plan, bao gồm cài đặt/migration/commit đã mô tả, tiếp tục trong phạm vi đó mà không hỏi lại từng cổng; chỉ xin bổ sung phần chưa được cấp.

## Brief gốc và nguồn để xây

[Brief nguyên văn của người dùng](original-brief.md) là điểm xuất phát của kế hoạch: **đào sâu vấn đề để đưa giải pháp; phỏng vấn khi cần thay vì chốt trước; giúp học theo background non-tech/UX/UI và memory sẵn có; gọi FP thuận tiện ở các repo như AK trong Codex.** Các điều làm rõ được user đồng ý nằm trong [hợp đồng sản phẩm](product-contract.md).

| Nguồn người dùng chỉ định | Vai trò trong rebuild |
|---|---|
| [Untools — First principles](https://untools.co/first-principles/) | Nền phương pháp phân rã và xây lại giải pháp; đối chiếu cách dùng Socratic/5 Whys. |
| [Matt Pocock — productivity skills](https://github.com/mattpocock/skills/tree/main/skills/productivity) | Tham khảo grill-me/grilling cho phỏng vấn; tuyển chọn mẫu hỗ trợ học phù hợp. |
| [Kho first-principles local](../../first-principles/) — `/Users/quanglaam/fp-brain/first-principles` | Đối chiếu các khái niệm/ghi chú đã tích lũy, giữ nguồn gốc và kiểm tra claim trước khi đưa vào runtime. |

Ba nguồn này phải xuất hiện trong bảng nguồn → quy tắc → ca kiểm thử ở Phase 01. [Đối chiếu chi tiết](research/source-review.md) ghi phần kế thừa/điều chỉnh/loại và lý do. Workshop và AK là tham chiếu bổ sung, không thay thế nguồn gốc hoặc mục tiêu của user.

## Phạm vi bản đầu

Một điểm vào `fp` hỗ trợ làm rõ, phân rã, kiểm tra giả định, research chỉ đọc, so sánh và học trong công việc. Thành công là user hiểu vấn đề, lý do chọn hướng và bước kiểm chứng tiếp theo. Phương pháp có thể đổi theo bài toán, với giải thích ngắn và quyền điều khiển của user.

Vị trí package đề xuất: `skills/fp/`; phân phối bằng copy tự chứa vào `~/.agents/skills/fp/`. Tên/path phải qua kiểm tra xung đột. Runtime không tự ghi memory, sửa file, cài đặt hoặc giao việc thực thi. Bản đầu nhắm Codex trên máy này; không hứa hỗ trợ host khác.

## Context links

- [Hợp đồng sản phẩm](product-contract.md): yêu cầu đã chốt, quy tắc lựa chọn phương pháp và thay đổi so với bản cũ.
- [Ma trận nghiệm thu](acceptance-matrix.md): ca thử, rubric, ngân sách chạy và điều kiện dừng.
- [Nguồn phương pháp](research/source-review.md) và [phân phối](research/distribution-review.md): bằng chứng, đề xuất và giới hạn.

## Phases và cổng

| Phase | Kết quả bắt buộc | Cổng sang bước sau |
|---|---|---|
| [01 — Contract và nguồn](phase-01-contract-and-sources.md) | Checkpoint hiện trạng, contract/rubric mới, nguồn có quyết định tiếp nhận | Phạm vi, bảo toàn và ngân sách được chốt trước implementation |
| [02 — Runtime và package](phase-02-runtime-and-package.md) | Một entry tự chứa; script bảo trì nhỏ; thử package trong staging | `IMPLEMENTED` và `PACKAGE_VALIDATED`, chưa là native acceptance |
| [03 — Native acceptance](phase-03-native-acceptance.md) | Chạy hữu hạn, raw trace, chấm theo rubric cố định, review | `NATIVE_ACCEPTED` chỉ trong model/host/candidate đã ghi |
| [04 — Install và closeout](phase-04-install-and-closeout.md) | Cài trong phạm vi được phép; picker/task mới; feedback thật; migration có rollback | Tách `INSTALLED`, discovery và `PRODUCT_ACCEPTED` |

## Thứ tự bằng chứng

`CONTRACT_READY → IMPLEMENTED → PACKAGE_VALIDATED → NATIVE_ACCEPTED → INSTALLED → PRODUCT_ACCEPTED`

Mỗi nhãn cần bằng chứng của chính nó. File đúng cú pháp hoặc test package xanh không chứng minh model làm đúng; native PASS không chứng minh picker hoặc hữu ích với user. Bước chưa thử phải ghi `NOT_RUN`/`UNVERIFIED`; thất bại không được đổi tên thành PASS bằng sửa rubric.

## Bảo toàn và chuyển đổi

Baseline được báo tại lúc lập plan: `main`, HEAD `7c894c2`; `evals/results.md` đang dirty với 12 fixture, 7 PASS/5 FAIL (A1, A2, B1, D3, L2). Có evidence full-pipeline cũ và `first-principles/` untracked. Phase 01 phải kiểm tra lại, không coi snapshot này là grant ghi đè.

Chụp/checkpoint toàn bộ phần cần giữ và tạo baseline commit sau khi thực thi được cho phép, trước rebuild. Lúc lập plan repo còn `main`; triển khai đã chuyển sang `codex/fp-rebuild` sau baseline `f8b6caa`. Giữ nguyên kết quả lịch sử theo rubric cũ. Contract mới cho phép giả thuyết có căn cứ; điều này không sửa kết quả A3 cũ. Core và bốn entry cũ còn truy được qua Git/history; runtime mới không phụ thuộc chúng.

Chỉ retire bốn entry đang hoạt động và chuyển hướng `AGENTS.md`, README, method links sau khi candidate qua staging và các cổng chuyển đổi liên quan. Không dọn vault, evidence hoặc mọi chữ “legacy”.

## Điểm cần kiểm chứng

Agent triển khai xác minh nguồn/license ở Phase 01, package và tên gọi ở Phase 02; reviewer chấm hành vi ở Phase 03; kiểm tra discovery/picker ở Phase 04. User đánh giá mức hữu ích qua phiên dùng thật. Chi tiết trách nhiệm và cổng nằm trong từng phase.

## Giới hạn thực thi

Ngân sách native staging đề xuất: 20 ca + 5 lượt lặp trọng yếu + 1 ordinary prompt = tối đa 26 phiên/bộ; tối đa hai bộ sau một vòng sửa, tổng 52 phiên, tối đa hai phiên đồng thời. Khóa exact messages/nhánh/nguồn ở Phase 01. Phase 04 có tối đa bốn phiên kiểm tra phân phối, một lượt UI và một phiên dùng thật riêng. Không tự rerun đến PASS hoặc tiêu thụ lại exact-once evidence. Snapshot cuối phải đạt cả bộ cùng hash; giữ raw trace và rubric ngoài context model thử. Nếu còn fail sau budget, báo residual và bước cần quyền mới.

Tiến độ: phase 01 **CONTRACT_READY**, phase 02 **PACKAGE_VALIDATED**, phase 03/04 **NOT_RUN**. Xem [implementation status](implementation-status.md); checklist triển khai nằm trong từng phase. Tài liệu kế hoạch không phải kết quả nghiệm thu.
