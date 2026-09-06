# Phase 03 — Native acceptance có giới hạn

## Context links

[Plan](plan.md) · [Phase 02](phase-02-runtime-and-package.md) · [Matrix](acceptance-matrix.md) · [Contract](product-contract.md)

## Overview

Trạng thái: **BLOCKED_HOST_MODEL_COMPATIBILITY**. N01 lượt đầu đã tiêu thụ **1/52 sessions** nhưng không có model output: CLI 0.151.0 bị host từ chối khi dùng `gpt-6-astra`/`high`, yêu cầu runtime mới hơn. Không followup/rerun. Gate vẫn `PACKAGE_VALIDATED`; phase 04 chưa chạy. Xem [báo cáo](../../evals/evidence/2026-09-06-fp-rebuild-native-bounded-01/report.md) và [diagnostics](../../evals/evidence/2026-09-06-fp-rebuild-native-bounded-01/N01-first-turn-diagnostics.json). Mục tiêu là quan sát hành vi trong host/model thật với ngân sách hữu hạn.

## Key Insights

- Cấu trúc package đúng không bảo đảm model tuân thủ chỉ dẫn.
- Native PASS chỉ áp dụng candidate/model/host và ca đã chạy; không có bảo đảm tuyệt đối.
- Bằng chứng phải cho thấy skill/path/content thực sự được chọn, không chỉ exit code.
- Thay đổi tiêu chí giữa lượt chạy sẽ làm mất khả năng đánh giá; rubric mới không viết lại outcome cũ.

## Requirements

- Case, rubric và budget theo matrix đã đóng băng: N01–N20 + lượt lặp N02/N05/N08/N11/N20 + ordinary prompt = tối đa 26 phiên/bộ; tối đa hai bộ sau một vòng sửa, 52 phiên tổng.
- Tối đa hai phiên native đồng thời; không dùng thời gian rảnh để thêm probe ngoài danh sách.
- Không tự động repair/rerun đến PASS. Rerun chỉ dùng ô được cho phép trong budget, có lý do và giữ lần trước.
- Fresh session cho từng ca theo matrix; model thử nhận input/context được phép, không nhận expected output hoặc rubric chấm.
- Raw trace, stderr và metadata đủ xác minh provenance; ledger version mới tham chiếu evidence thay vì thay evidence cũ.
- Runtime thử ở chế độ chỉ đọc, không được sửa repo, install, ghi memory hoặc delegate thực thi.

## Architecture

Candidate bất biến → session/context được kiểm soát → raw trace → reviewer chấm ngoài session → ledger mới. Case và rubric là tài sản đánh giá, không thuộc runtime package.

Mỗi record ghi case ID, contract/rubric version, candidate hash, host/model/config, selected path, input đã cấp, lần chạy, timestamps, verdict và evidence. Khi không chứng minh được provenance, ghi `UNVERIFIED`/`BLOCKED` theo matrix thay vì behavioral PASS.

## Related code files

- Runtime đọc: `skills/fp/**` hoặc bản staging đã xác minh hash.
- Định nghĩa kiểm tra: `acceptance-matrix.md` và rubric/cases version mới trong `evals/` sau quyền triển khai.
- Bằng chứng mới: thư mục `evals/evidence/` riêng cho run ID; ledger version mới hoặc phần append rõ phiên bản theo convention đã review.
- Bảo toàn: `evals/results.md` lịch sử, evidence full-pipeline cũ và mọi exact-once run đã tiêu thụ.

## Implementation Steps

1. Kiểm tra candidate không đổi sau package validation; xác nhận matrix có budget cụ thể. Nếu còn `tbd` ở số lần chạy/rerun, chưa được bắt đầu native.
2. Ghi host/model/config thực tế, cấu hình chỉ đọc và đường dẫn nạp dự kiến. Với CLI, đặt `sandbox_mode="read-only"`, `approval_policy="never"` cho cả initial/resume nếu có resume trong case.
3. Kiểm tra cơ chế cách ly staging bằng bằng chứng đường dẫn/content đã chọn trong ca đầu của bộ, tính trong ngân sách; chỉ đổi `CODEX_HOME` không chứng minh user skills đã được cách ly. Không sửa global để ép selected path. Nếu provenance sai, dừng phần phụ thuộc và ghi setup failure, không chạy thêm probe ngầm.
4. Chạy đúng input đã khóa theo matrix, không mớm đáp án hoặc tiêu chí chấm cho model. Tách case knowledge rõ, clarification, hypothesis, ưu tiên, đổi phương pháp, research, learning, memory và boundary theo matrix.
5. Theo dõi các can thiệp nhiều lượt chỉ nếu case định nghĩa; không thêm phản hồi cứu ca ngoài kịch bản. Thu raw trace/stderr nguyên bản và ghi mọi tool action/attempted mutation.
6. Chấm từng ca theo rubric mới với trích đoạn và vị trí trace. Tách lỗi provenance/setup, lỗi hành vi và evidence thiếu/misplaced/incomplete; không đồng nhất chúng.
7. Reviewer khác người viết runtime đọc nguyên trace các ca trọng yếu và mọi ca lỗi/tranh chấp: kiểm tra giữ mục tiêu, quyền user, grounding và dừng đúng. Phân biệt hypothesis hợp lệ với kết luận thiếu tiền đề; ordinary prompt kiểm tra không tự nạp FP.
8. Nếu scope thực thi đã cấp gồm vòng sửa của matrix, sửa một vòng hữu hạn và chạy lại toàn bộ trên candidate hash mới trong bộ thứ hai. Giữ lần đầu; không ghép PASS khác hash, không bắt buộc dùng hết budget nếu bộ đầu đạt. Thay fixture/rubric phải version và ghi rõ, không cứu PASS bằng câu trả lời ngoài nhánh.
9. Khi hết ngân sách hoặc gặp stop condition, dừng. Báo bảng PASS/FAIL/NOT_RUN/UNVERIFIED, phạm vi thực sự và residual; không tự mở vòng sửa.
10. Chỉ ghi `NATIVE_ACCEPTED` khi mọi điều kiện bắt buộc của matrix đạt. Nếu không, viết quyết định hold cùng evidence và đề xuất bước tiếp theo riêng; chưa sang install.

## Todo list

- [x] Candidate file hashes, actual runtime config và ngân sách của attempt đầu xác nhận: 1/52 consumed; model `gpt-6-astra`, effort `high`, read-only/never.
- [ ] Context sạch được chứng minh. Staged entry path/body khớp chính xác, nhưng 165 ambient non-FP catalog entries còn trong context; không gộp injection PASS thành clean-context PASS.
- [ ] Bộ ca chạy hoàn tất. Chỉ N01 lượt đầu được launch, chưa có assistant output; N02–N20, năm repeats, ordinary và batch sau đều NOT_RUN.
- [x] Raw trace/stdout/stderr, invocation/result và budget ledger của attempt đầu được lưu; evidence bộ đầy đủ chưa có.
- [ ] Review hành vi theo rubric hoàn tất. N01 NOT_GRADED do host/model block; không có output để chấm.
- [x] Verdict và residual của attempt đầu được ghi rõ trong report; NATIVE_ACCEPTED chưa đạt.

## Success Criteria

Kết quả đầy đủ cho ngân sách đã được phép, không có lần chạy ngầm hoặc sửa rubric sau quan sát. `NATIVE_ACCEPTED` cần đạt matrix; một báo cáo đầy đủ với FAIL là hoàn thành lần kiểm tra nhưng không là nghiệm thu runtime.

## Risk Assessment

Model có biến thiên, host memory có thể ảnh hưởng, global skill có thể được chọn ngoài ý định. Giữ provenance/config, qualifier về context và budget hữu hạn; không tuyên bố deterministic hoặc clean-context nếu trace không đủ.

## Security Considerations

Evidence có thể chứa dữ liệu phiên; chỉ cung cấp case tối thiểu, không dùng secret thật. Raw evidence bảo toàn; bản chia sẻ được redact riêng có provenance, không sửa trace gốc để che hành vi lỗi.

## Next steps

Hiện giữ dependent native runs tại stop condition. Parent đã báo tìm thấy Desktop CLI 0.153.4 có sẵn qua kiểm tra read-only; [protocol amendment riêng](../../evals/rebuild-v1/host-recovery-v1.md) cho batch thứ hai/cuối đã được chuẩn bị, giữ candidate/model, không có batch thứ ba hoặc runtime repair. Chưa ghi nhận launch recovery; parent review protocol trước khi chạy. Số slot chưa dùng không tự cấp một lượt retry, đổi model, nâng cấp host hay sửa runtime. Không thay frozen fixtures hoặc raw evidence để cứu PASS.

Nếu đạt, chuẩn bị gói cài và review cụ thể cho [Phase 04](phase-04-install-and-closeout.md). Tiếp tục nếu scope đã bao phủ cài đặt; chỉ hỏi phần quyền còn thiếu. Nếu chưa đạt sau ngân sách, user quyết định vòng xử lý mới dựa residual, không mặc định mở rộng budget.
