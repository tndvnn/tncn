#!/usr/bin/env bash
# Chạy quét luật mới rồi gửi báo cáo. Cron gọi mỗi ngày.
# Email: cần ~/.msmtprc (SMTP). Chưa có thì chỉ lưu báo cáo + log, không lỗi.
set -u
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG="$DIR/logs/$(date +%Y-%m).log"
mkdir -p "$DIR/logs" "$DIR/reports"
TO="${BAO_CAO_TOI:-mr@tnd.vn}"
{
  echo "=== $(date '+%F %T') bắt đầu"
  out=$(python3 "$DIR/quet_luat_moi.py" 2>&1); rc=$?
  echo "$out"
  echo "rc=$rc"
  bc="$DIR/reports/$(date +%F).md"
  if [ "$rc" -eq 10 ] && [ -f "$bc" ]; then
    uu_tien=$(python3 -c "import json,sys;print(json.load(open(sys.argv[1]))['uu_tien'])" "$DIR/reports/$(date +%F).json" 2>/dev/null || echo 0)
    if [ "$uu_tien" -gt 0 ]; then subj="[thue-tncn] ⚠️ ƯU TIÊN: văn bản skill đang dùng bị sửa/thay — $(date +%F)"; else subj="[thue-tncn] Luật thuế/hỏi đáp mới cần rà — $(date +%F)"; fi
    if [ -f "$HOME/.msmtprc" ] && command -v msmtp >/dev/null; then
      { printf 'To: %s\nFrom: %s\nSubject: %s\nContent-Type: text/plain; charset=UTF-8\n\n' "$TO" "$(grep -m1 '^from' "$HOME/.msmtprc" | awk '{print $2}')" "$subj"; cat "$bc"; } | msmtp "$TO" && echo "đã gửi email tới $TO" || echo "GỬI EMAIL LỖI"
    else
      echo "chưa cấu hình msmtp — không gửi email, báo cáo tại $bc"
    fi
  elif [ "$rc" -eq 0 ]; then
    echo "không có gì mới"
  else
    echo "QUÉT LỖI, xem report"
    if [ -f "$HOME/.msmtprc" ] && command -v msmtp >/dev/null; then
      printf 'To: %s\nFrom: %s\nSubject: [thue-tncn] Quét luật LỖI %s\n\n%s\n' "$TO" "$(grep -m1 '^from' "$HOME/.msmtprc" | awk '{print $2}')" "$(date +%F)" "$out" | msmtp "$TO"
    fi
  fi
  echo "=== kết thúc"
} >> "$LOG" 2>&1
