#!/usr/bin/env python3
"""Surgically clear or set individual cells in an already-written workbook.

R-BLM16(2)(3) needs two whole columns emptied across rows that are already
delivered. Re-running write_back would rebuild every cell from the batch
json; this touches only the named cells, so a mistake elsewhere in the batch
cannot ride along with the fix.

Emit goes through `backend.xlsx_surgical.surgical_save` for the same reason
write_back does: openpyxl's save() would drop the x14 dropdown.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "scripts"))

import openpyxl                                                    # noqa: E402
from backend.xlsx_surgical import surgical_save                    # noqa: E402
from feature_config import load_feature_config                     # noqa: E402

FEAT = Path(__file__).resolve().parents[1]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rows", required=True, help="例 10-28")
    ap.add_argument("--clear", default="", help="逗號分隔之 feature.yaml 欄名")
    a = ap.parse_args()

    cfg = load_feature_config(FEAT)
    col = cfg["col"]
    lo, hi = (int(x) for x in a.rows.split("-"))
    names = [n.strip() for n in a.clear.split(",") if n.strip()]
    for n in names:
        if n not in col:
            sys.exit(f"unknown column name {n!r}; known: {sorted(col)}")

    wb = openpyxl.load_workbook(Path(a.src))
    ws = wb[cfg["workbook"]["sheet"]]

    before = {}
    for n in names:
        vals = [ws.cell(r, col[n] + 1).value for r in range(lo, hi + 1)]
        before[n] = vals
        for r in range(lo, hi + 1):
            ws.cell(r, col[n] + 1).value = None

    report = surgical_save(wb, Path(a.src), Path(a.out))
    print(f"來源 {Path(a.src).name} -> {Path(a.out).name}")
    print(f"列範圍 {lo}-{hi}（{hi - lo + 1} 列）")
    for n in names:
        seen = sorted({str(v) for v in before[n] if v not in (None, "")})
        print(f"  清空 {n}（欄 {cfg['workbook']['columns'][n]}）"
              f" 原值 {seen or '(已為空)'}")
    print(f"  sheets_patched {report['sheets_patched']}")
    print(f"  zip members {report['members']}  differing {report['differing']}")
    print(f"  dv_counts {report['dv_counts']}")

    rb = openpyxl.load_workbook(Path(a.out), data_only=True)
    rws = rb[cfg["workbook"]["sheet"]]
    bad = 0
    for n in names:
        for r in range(lo, hi + 1):
            if rws.cell(r, col[n] + 1).value not in (None, ""):
                bad += 1
                print(f"  **差異** 列{r} {n} 未清空")
    print(f"  round-trip 讀回：{len(names) * (hi - lo + 1)} 格，未清空 {bad}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
