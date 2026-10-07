#!/usr/bin/env bash
# 按 data/*.txt 中的图片 ID 从 pbs.twimg.com 下载原图到 images/<分类>/
set -euo pipefail
cd "$(dirname "$0")/.."

failed=0
for list in data/*.txt; do
  category=$(basename "$list" .txt)
  mkdir -p "images/$category"
  while IFS= read -r id; do
    [ -z "$id" ] && continue
    out="images/$category/$id.jpg"
    [ -s "$out" ] && continue
    if curl -fsSL --retry 3 -o "$out" "https://pbs.twimg.com/media/$id.jpg?name=orig"; then
      echo "ok   $out"
    else
      rm -f "$out"
      echo "fail $id" >&2
      failed=$((failed + 1))
    fi
  done < "$list"
done
echo "下载失败: $failed"
