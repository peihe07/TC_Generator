#!/usr/bin/env python3
"""VS-SL-06 §1 —— 沙盒稿轉正至各 feature 之 `output/`。

轉正前**逐本核 SHA**（須等於站④ 抽驗通過之稿），不符即停。
沙盒稿與 `.bak` 鏈保留不刪（追溯）。**不入 `delivered/`**（出貨 gate 未過）。

MANIFEST 之落點與包內字面不同，理由：
  `scripts/lint_paths.py:check_delivered()` 對 `features/*/delivered/MANIFEST.tsv`
  逐列檢「對照表有列而檔不存在」。轉正本在 `output/` 而非 `delivered/`，
  若寫入 `delivered/MANIFEST.tsv` 會立即產生一筆新紅。
  故改落 `features/<slug>/output/MANIFEST.tsv`（`output/` 於 `EXEMPT_TOPS` 內，不受落點檢查）。
"""

from __future__ import annotations

import csv
import hashlib
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as v1  # noqa: E402

ROOT = v1.ROOT
STATUS = "writeback-pending-DR"

# slug: (沙盒稿, 抽驗通過之 SHA, 轉正檔名)
BOOKS = {
    "vehicle_setting": (
        "features/vehicle_setting/sandbox/vssl/vf230_vssl.xlsx",
        "49b1bf94eb368ee362378733fe0ad2e36c6f5b8ada3b07fcaec952c476218ac3",
        "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
        "Specification & Result_SWQT_VF230_20260902.xlsx"),
    "bed_lowering": (
        "features/bed_lowering/sandbox/vssl/bl_vssl.xlsx",
        "b0ee608d5469d31b36a067d0db63f7efd2b40c388e7d58e4fdd6f6a3286f28ec",
        "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
        "Specification & Result_SWQT_BedLowering_20260902.xlsx"),
    "vehicle_category": (
        "features/vehicle_category/sandbox/vssl/vc_vssl.xlsx",
        "3a1b5f401fada13ea39a79e85b8e849a24d1398f8831eba8b4470ec063f65541",
        "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
        "Specification & Result_SWQT_VehicleCategory_20260902_working.xlsx"),
}

MANIFEST_COLS = ["filename", "sha256", "source_path", "round", "status", "note"]


def sha256_of(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def promote(slug: str) -> dict:
    src_rel, want, name = BOOKS[slug]
    src = ROOT / src_rel
    got = sha256_of(src)
    if got != want:
        raise AssertionError(f"{slug}：沙盒稿 SHA {got[:16]} ≠ 抽驗通過之 {want[:16]}，停")

    out_dir = ROOT / "features" / slug / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / name
    shutil.copy2(src, dst)
    after = sha256_of(dst)
    assert after == want, f"{slug}：轉正後 SHA 不等於沙盒稿"

    man = out_dir / "MANIFEST.tsv"
    rows = []
    if man.exists():
        rows = list(csv.DictReader(open(man), delimiter="\t"))
    rows = [r for r in rows if r.get("filename") != name]
    rows.append({"filename": name, "sha256": after, "source_path": src_rel,
                 "round": "VS-SL-06", "status": STATUS,
                 "note": "站④ 抽驗通過之稿；出貨 gate 未過，不入 delivered/"})
    with open(man, "w", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_COLS, delimiter="\t")
        w.writeheader()
        w.writerows(rows)
    return {"slug": slug, "path": str(dst.relative_to(ROOT)), "sha": after,
            "manifest": str(man.relative_to(ROOT)), "manifest_rows": len(rows)}


def main() -> int:
    for slug in BOOKS:
        r = promote(slug)
        print(f"{r['slug']:<18} → {Path(r['path']).name[-46:]}")
        print(f"{'':<18}   SHA {r['sha'][:32]}…  MANIFEST {r['manifest_rows']} 列（assert PASS）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
