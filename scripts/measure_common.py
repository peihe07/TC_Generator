"""量測腳本之共用常數（R-G16 補充，Pei 2026-09-05 追認）。

**量測產出不得回頭成為量測母體。** 此形態在 GC 系列犯過兩次：

- `up/20260905_GC-02.md` 9-3 節：`lint_reports_refs` 首跑把自己剛寫出的 tsv 納入母體，
  106 檔全被判為「有引用」，可移除數由 81 掉成 0。
- `up/20260905_GC-03.md` 9-4 節：R-G43 改號之母體掃描納入 `rg_refs_20260905.tsv`，
  引用處由 2,620 膨脹為 8,574；若照此改號，還會把一張已交付之量測表一併改寫。

排除集寫在**這一處**，掃描腳本 import 之，不得逐包各記（R-G16 補充明文）。
"""
from __future__ import annotations

import fnmatch
from pathlib import Path

# `docs/reports/` 下帶日期尾綴之 tsv 一律為量測產出。
MEASUREMENT_OUTPUT_GLOBS: tuple[str, ...] = (
    "docs/reports/*_20[0-9][0-9][0-9][0-9][0-9][0-9].tsv",
    "docs/reports/binding_diff_*.tsv",
    "docs/reports/binding_hits_*.tsv",
)


def is_measurement_output(rel: Path | str) -> bool:
    """`rel` 為 repo 根之相對路徑；命中任一 glob 即為量測產出，不入任何母體。"""
    s = Path(rel).as_posix()
    return any(fnmatch.fnmatch(s, g) for g in MEASUREMENT_OUTPUT_GLOBS)
