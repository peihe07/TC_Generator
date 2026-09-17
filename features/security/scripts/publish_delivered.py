#!/usr/bin/env python3
"""出貨區（`features/security/delivered/`）—— 依 repo 既有慣例自 `sandbox/delivery/` 複製。

慣例出處：`features/power/delivered/MANIFEST.tsv`（欄 `filename | sha256 | source_path |
delivered_round | note | status`，note 記「整檔複製，逐位元組一致（cmp 實測）」）。
`sandbox/` 為產線、`delivered/` 為出貨區；本腳本**只複製不搬移**，並逐位元組複驗。

冪等：重跑會以現行 `sandbox/delivery/` 之內容覆蓋出貨區並重寫 MANIFEST。
"""
from __future__ import annotations

import csv
import filecmp
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "features" / "security" / "sandbox" / "delivery"
OUT = ROOT / "features" / "security" / "delivered"
ROUND = "SEC-17（R-SEC25 六本形制 ＋ 佔位列標色）"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    books = sorted(SRC.glob("*Security_*_20260917.xlsx"))
    shared = ["EXEC_GUIDE.md", "asset_request.md", "coverage.tsv",
              "placeholder_summary.tsv", "placeholder_by_token.tsv", "placeholder_rows.tsv"]
    if len(books) != 6:
        raise SystemExit(f"交付本 {len(books)} 本，應為 6")

    rows = []
    for f in books + [SRC / n for n in shared]:
        dst = OUT / f.name
        shutil.copy2(f, dst)
        if not filecmp.cmp(f, dst, shallow=False):
            raise SystemExit(f"複製後不一致：{f.name}")
        kind = "交付本" if f.suffix == ".xlsx" else "共用件"
        rows.append((f.name, sha256(dst), str(f.relative_to(ROOT)), ROUND,
                     f"{kind}；整檔複製，逐位元組一致（filecmp 實測）", ""))

    with (OUT / "MANIFEST.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["filename", "sha256", "source_path", "delivered_round", "note", "status"])
        for r in rows:
            w.writerow(r)
    print(f"出貨區 → {OUT.relative_to(ROOT)}：{len(books)} 本 ＋ {len(shared)} 共用件")
    for n, s, *_ in rows:
        print(f"  {s[:16]}  {n[:72]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
