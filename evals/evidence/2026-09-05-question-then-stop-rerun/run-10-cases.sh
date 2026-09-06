#!/bin/bash
set -u

evidence_root=/Users/quanglaam/fp-brain/evals/evidence/2026-09-05-question-then-stop-rerun/cases
mkdir -p "$evidence_root"

run_case() {
  case_id="$1"
  skill_name="$2"
  shift 2
  case_root="$evidence_root/$case_id"
  mkdir -p "$case_root"

  turn=1
  first_message="$1"
  shift
  initial_prompt="\$${skill_name}

${first_message}"

  codex exec \
    -C /Users/quanglaam/fp-brain \
    --sandbox read-only \
    -c 'sandbox_mode="read-only"' \
    -c 'approval_policy="never"' \
    --ignore-user-config \
    --enable skip_host_skill_discovery \
    --disable plugins \
    --disable memories \
    -m gpt-5.4-mini \
    --json \
    "$initial_prompt" \
    >"$case_root/turn-1.stdout.jsonl" \
    2>"$case_root/turn-1.stderr.txt"
  rc=$?
  printf '%s\n' "$rc" >"$case_root/turn-1.exit.txt"
  if [ "$rc" -ne 0 ]; then
    printf '%s\n' 'initial turn failed; later fixture turns were not run' >"$case_root/stop.txt"
    return
  fi

  thread_id=$(jq -r 'select(.type == "thread.started") | .thread_id' "$case_root/turn-1.stdout.jsonl" | head -n 1)
  if [ -z "$thread_id" ] || [ "$thread_id" = null ]; then
    printf '%s\n' 'thread.started was not captured; later fixture turns were not run' >"$case_root/stop.txt"
    return
  fi
  printf '%s\n' "$thread_id" >"$case_root/thread-id.txt"

  for message in "$@"; do
    turn=$((turn + 1))
    codex exec resume "$thread_id" \
      -c 'sandbox_mode="read-only"' \
      -c 'approval_policy="never"' \
      --ignore-user-config \
      --enable skip_host_skill_discovery \
      --disable plugins \
      --disable memories \
      -m gpt-5.4-mini \
      --json \
      "$message" \
      >"$case_root/turn-${turn}.stdout.jsonl" \
      2>"$case_root/turn-${turn}.stderr.txt"
    rc=$?
    printf '%s\n' "$rc" >"$case_root/turn-${turn}.exit.txt"
    if [ "$rc" -ne 0 ]; then
      printf 'turn %s failed; later fixture turns were not run\n' "$turn" >"$case_root/stop.txt"
      return
    fi
  done
}

run_case A1 fp-ask \
  '“Tôi làm việc với AI thấy rất mệt. Tôi không biết phải hỏi gì.”' \
  '“AI hay viết giải pháp dài khi tôi chưa rõ mình cần gì.”' \
  '“Tôi muốn cùng nó xác định đúng vấn đề trước.”' &
run_case A2 fp-ask \
  '“API là gì? Tôi là designer, chưa hiểu.”' \
  '“Tôi đang vẽ màn hình đặt hàng và không hiểu bấm nút thì dữ liệu đi đâu.”' \
  '“Giải thích trực tiếp giúp tôi bằng ví dụ đó.”' &
run_case A3 fp-ask \
  '“Tôi muốn tìm vì sao khách bỏ form đăng ký.”' \
  '“Tôi thấy 8 trên 10 người trong buổi test dừng ở ô số điện thoại.”' \
  '“Tôi đoán họ ngại cung cấp số điện thoại.”' \
  '“Chưa hỏi họ nên tôi chưa biết chắc.”' &
run_case A4 fp-ask \
  '“Tôi chưa biết form đang có vấn đề gì.”' \
  '“Dừng hỏi ở đây. Chỉ tóm tắt điều còn chưa biết.”' &
wait

run_case A5 fp-ask \
  '“Tôi đoán khách bỏ form vì ngại nhập số điện thoại.”' \
  '“Nhưng tôi vừa hỏi: họ nói nút gửi không hoạt động. Tôi chưa kiểm tra lại.”' \
  '“Tôi sẽ thử tái hiện lỗi nút trước. Chưa cần tìm sâu hơn.”' &
run_case B1 fp-brainstorm \
  '“Brainstorm cách làm app tốt hơn.”' \
  '“Tôi muốn người dùng biết đơn hàng đã gửi hay chưa.”' \
  '“Backend trả được trạng thái thành công hoặc thất bại sau vài giây.”' &
run_case B2 fp-brainstorm \
  '“App đã biết khi yêu cầu đang xử lý, thành công và thất bại. Người dùng cần biết có nên bấm gửi lại không. Hãy đề xuất ba hướng phản hồi.”' &
run_case D1 fp-decide \
  '“Hai phương án A/B dưới đây là dữ kiện giả lập đã chốt cho bài tập. A cần 2 ngày làm, tôi tự bảo trì được, ít tùy biến. B cần 10 ngày, phải thuê dev, tùy biến cao. Tôi cần demo trong 3 ngày và muốn tự bảo trì. Chọn gì?”' &
wait

run_case D2 fp-decide \
  '“A cần 2 ngày, ít tùy biến; B cần 10 ngày, tùy biến cao. Đây là dữ kiện giả lập. Tôi chưa nói deadline hay mục tiêu. Nên chọn gì?”' \
  '“Tôi cần kiểm chứng ý tưởng trong tuần này, chưa cần tùy biến.”' &
run_case D3 fp-decide \
  '“Một bài blog nói công cụ X luôn nhanh gấp 10 lần Y. Tôi chưa có benchmark hay cấu hình. Có nên chuyển toàn bộ sản phẩm sang X không?”' &
wait
