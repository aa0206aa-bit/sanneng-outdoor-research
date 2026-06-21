#!/bin/bash
# CI 報告審查腳本 — 結合 validate.py + claude -p AI 分析

set -e

REPORT="2026-06-18-三能戶外市場研究報告.md"
EXIT_CODE=0

echo "=== Step 1: 格式驗證 ==="
if ! python3 validate.py; then
  echo "❌ 格式驗證失敗，終止審查"
  exit 1
fi

echo ""
echo "=== Step 2: AI 論述一致性審查 ==="
PROMPT="你是市場研究報告的品質審查員。
閱讀以下報告片段，只回答：
1. 執行摘要的核心定位與第 10 章結論是否一致？（一致 / 不一致 + 理由）
2. 有無自相矛盾的數據或建議？（有 / 無 + 具體位置）
限制在 150 字內，繁體中文回答。"

cat "$REPORT" | claude -p "$PROMPT" && echo "" || { echo "⚠️  AI 審查失敗（跳過，不阻斷 CI）"; }

echo ""
echo "=== Step 3: ⚠️ 待驗證數據計數 ==="
COUNT=$(grep -c "⚠️" "$REPORT" || true)
echo "目前共有 $COUNT 處待驗證標記"

if [ "$COUNT" -gt 20 ]; then
  echo "⚠️  待驗證數據超過 20 處，建議在發布前補強驗證"
  EXIT_CODE=1
fi

echo ""
if [ "$EXIT_CODE" -eq 0 ]; then
  echo "✅ CI 審查通過"
else
  echo "⚠️  CI 審查完成，有警告需處理"
fi

exit $EXIT_CODE
