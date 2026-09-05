#!/usr/bin/env bash
# GC-06 §二-3-a／補遺 §2：driver_distraction 之二檔搬入 sandbox/（R-G64 產出物目錄政策）。
# **Pei 專門 commit 用；執行層只產生，不執行。** 每行一 pathspec（R-G51）。
#
# 前提實測（GC-06 §二-3-a）：該線 **無** `[OVERRIDE R-G64] workbook/` 之宣告 ——
#   grep "OVERRIDE R-G" features/driver_distraction/ docs/runtime/profiles/ → 命中 0 檔；
#   `DECISIONS.md:64` 之 `Profile [OVERRIDE] clauses needed` 仍為 `[PROPOSED]` 佔位。
#   依補遺 §2「無宣告即無例外」，搬。
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"

mkdir -p features/driver_distraction/sandbox        # 該線目前無 sandbox/
git mv -- "features/driver_distraction/workbook/driver_distraction_00.xlsx" \
          "features/driver_distraction/sandbox/driver_distraction_00.xlsx"
git mv -- "features/driver_distraction/workbook/driver_distraction_00_bak.xlsx" \
          "features/driver_distraction/sandbox/driver_distraction_00_bak.xlsx"

# **搬完必改這一行，否則 feature.yaml 指向不存在之路徑（R-G63 路徑實在性）**：
#   features/driver_distraction/feature.yaml:17
#     - workbook: "workbook/driver_distraction_00.xlsx"
#     + workbook: "sandbox/driver_distraction_00.xlsx"
# 執行層未代改：改 feature.yaml 屬該線之作業，且與本搬移須同一 commit 才不留中間態。
echo "gc06_mv: 2 moved; 記得同步 features/driver_distraction/feature.yaml:17"
