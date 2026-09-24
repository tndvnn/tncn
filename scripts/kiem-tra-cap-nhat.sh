#!/usr/bin/env bash
# Kiểm tra skill tncn có bản mới trên GitHub chưa, tối đa 1 lần mỗi 24 giờ.
# Dùng:  bash scripts/kiem-tra-cap-nhat.sh            # kiểm tra, chỉ báo
#        bash scripts/kiem-tra-cap-nhat.sh --apply    # có bản mới thì git pull luôn
#        bash scripts/kiem-tra-cap-nhat.sh --force    # bỏ qua giới hạn 24 giờ
# Kết quả in ra 1 dòng đầu: DA_MOI_NHAT | CO_BAN_MOI | DA_CAP_NHAT | DA_KIEM_HOM_NAY | KHONG_KIEM_DUOC
set -u
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MARKER="$SKILL_DIR/.kiem-tra-cap-nhat"
REPO_RAW="https://raw.githubusercontent.com/tndvnn/tncn/main"
REPO_URL="https://github.com/tndvnn/tncn"
APPLY=0; FORCE=0
for a in "$@"; do
  [ "$a" = "--apply" ] && APPLY=1
  [ "$a" = "--force" ] && FORCE=1
done

# Giới hạn 1 lần/ngày: bỏ qua nếu marker mới hơn 24 giờ
if [ "$FORCE" -eq 0 ] && [ -f "$MARKER" ]; then
  last=$(cat "$MARKER" 2>/dev/null || echo 0)
  now=$(date +%s)
  if [ $((now - last)) -lt 86400 ]; then
    echo "DA_KIEM_HOM_NAY (lần cuối $(date -d "@$last" +%F' '%H:%M 2>/dev/null || date -r "$last" +%F' '%H:%M)) — dùng --force để kiểm lại"
    exit 0
  fi
fi

local_ver=$(grep -o '"version": *"[^"]*"' "$SKILL_DIR/version.json" 2>/dev/null | head -1 | sed 's/.*"\([^"]*\)"$/\1/')
local_ver=${local_ver:-"?"}

# Cách 1: thư mục là git clone → so với origin/main
if [ -d "$SKILL_DIR/.git" ] && command -v git >/dev/null 2>&1; then
  if git -C "$SKILL_DIR" fetch -q origin main 2>/dev/null; then
    local_rev=$(git -C "$SKILL_DIR" rev-parse HEAD)
    remote_rev=$(git -C "$SKILL_DIR" rev-parse origin/main)
    date +%s > "$MARKER"
    if [ "$local_rev" = "$remote_rev" ]; then
      echo "DA_MOI_NHAT — phiên bản $local_ver, khớp origin/main"
      exit 0
    fi
    remote_ver=$(git -C "$SKILL_DIR" show origin/main:version.json 2>/dev/null | grep -o '"version": *"[^"]*"' | sed 's/.*"\([^"]*\)"$/\1/')
    if [ "$APPLY" -eq 1 ]; then
      if git -C "$SKILL_DIR" pull -q --ff-only origin main; then
        echo "DA_CAP_NHAT — từ $local_ver lên ${remote_ver:-?}"
        git -C "$SKILL_DIR" log --oneline "$local_rev..HEAD" | head -10
        exit 0
      fi
      echo "CO_BAN_MOI — ${remote_ver:-?} nhưng git pull thất bại (có sửa đổi cục bộ?). Chạy tay: git -C \"$SKILL_DIR\" pull"
      exit 2
    fi
    echo "CO_BAN_MOI — đang dùng $local_ver, trên GitHub là ${remote_ver:-?}. Cập nhật: bash \"$SKILL_DIR/scripts/kiem-tra-cap-nhat.sh\" --apply"
    git -C "$SKILL_DIR" log --oneline "$local_rev..origin/main" | head -10
    exit 2
  fi
fi

# Cách 2: không phải git clone → so version.json trên GitHub
fetch() {
  if command -v curl >/dev/null 2>&1; then curl -fsSL -m 20 "$1";
  elif command -v wget >/dev/null 2>&1; then wget -qO- -T 20 "$1";
  else return 1; fi
}
remote_json=$(fetch "$REPO_RAW/version.json" 2>/dev/null) || { echo "KHONG_KIEM_DUOC — không có mạng hoặc không có curl/wget. Đang dùng $local_ver"; exit 3; }
remote_ver=$(echo "$remote_json" | grep -o '"version": *"[^"]*"' | sed 's/.*"\([^"]*\)"$/\1/')
remote_date=$(echo "$remote_json" | grep -o '"data_date": *"[^"]*"' | sed 's/.*"\([^"]*\)"$/\1/')
date +%s > "$MARKER"
if [ "$remote_ver" = "$local_ver" ]; then
  echo "DA_MOI_NHAT — phiên bản $local_ver (data $remote_date)"
  exit 0
fi
echo "CO_BAN_MOI — đang dùng $local_ver, trên GitHub là $remote_ver (data $remote_date). Tải lại: git clone $REPO_URL hoặc zip mới nhất tại $REPO_URL/releases"
exit 2
