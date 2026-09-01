#!/usr/bin/env python3
"""VS-SL-01 §2 任務 4 自檢：先量再斷，並貼出 3 條 proposed 全文。

自檢項：
  1. dry-run 報告列數 = 工作簿實測資料列數（三本各自比對）
  2. 別名表列數 = VF230 之相異 `"X" customer setting` 名數；UNRESOLVED 數明列
  3. 抽 3 條貼 proposed 全文（含 FCW `-034`／`-035`）
     —— test_item 括號下半、無尾句號、UI 標籤雙引號
"""

from __future__ import annotations

import csv
import re
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as dr  # noqa: E402
from settings_lookup import Lookup, format_proxi  # noqa: E402

warnings.filterwarnings("ignore")
ROOT = dr.ROOT


def compose(lk: Lookup, g, r: int, alias_by_tc: dict) -> str:
    """依 §4 參考形制組 proposed 全文。UI 標籤加雙引號，句尾不加句號。"""
    item = g(r, 9)
    name = dr.setting_of(g, r)
    alias = alias_by_tc.get(name, {})
    res = lk.query(alias.get("hmi_name") or name, item, dr.DR_NO)
    neg = dr.is_negative(item)
    proposed, notes = dr.propose_proxi(lk, res, item, dr.proxi_now_of(g, r))

    pre = ["1. The HU is in the Full-Operation state"]
    for i, p in enumerate(proposed, start=2):
        pre.append(f"{i}. " + format_proxi([p]))

    proc = ["1. Power cycle the HU", '2. Press "Settings" on Menu Bar']
    exp = ["1. The HU completes start-up", "2. The Settings screen is displayed"]
    n = 3
    path = res["path"] or []
    for node in path[1:-1]:
        proc.append(f'{n}. Select "{node}"')
        exp.append(f'{n}. The "{node}" page is displayed')
        n += 1
    if path:
        leaf = path[-1]
        ctrl = res["control"] or {}
        opts = " / ".join(f'"{o}"' for o in ctrl.get("options", []))
        tmpl = ctrl.get("template", "")
        shape = f"{tmpl} {opts}".strip() if opts else tmpl
        verb = "is not displayed" if neg else f"is displayed with {shape}"
        proc.append(f'{n}. Check that "{leaf}" {verb}')
        exp.append(f'{n}. "{leaf}" '
                   + ("is not displayed" if neg else f"is displayed as {shape}"))

    tail = ("\n\n註：" + "；".join(notes)) if notes else ""
    return ("Pre-Condition\n" + "\n".join(pre)
            + "\n\nProcedure\n" + "\n".join(proc)
            + "\n\nExpected Result\n" + "\n".join(exp) + tail)


def main() -> int:
    lk = Lookup(ROOT)
    ok = True

    checks = [("VF230", dr.VF230, "features/vehicle_setting/reports/vf230_settings_dryrun.tsv"),
              ("BedLowering", dr.BL, "features/bed_lowering/reports/bl_settings_dryrun.tsv"),
              ("VehicleCategory", dr.VC, "features/vehicle_category/reports/vc_settings_dryrun.tsv")]
    print("== 自檢 1：報告列數 vs 工作簿實測 ==")
    for tag, wb, rep in checks:
        ws, g = dr.cells(ROOT / wb)
        want = len(dr.data_rows(ws, g))
        got = sum(1 for _ in csv.DictReader(open(ROOT / rep), delimiter="\t"))
        mark = "PASS" if want == got else "FAIL"
        ok &= want == got
        print(f"  {tag:16} 工作簿 {want:4} 列  報告 {got:4} 列  {mark}")

    print("\n== 自檢 2：別名表 ==")
    ws, g = dr.cells(ROOT / dr.VF230)
    names = dr.collect_names(g, dr.data_rows(ws, g))
    alias = list(csv.DictReader(open(ROOT / "features/vehicle_setting/data/settings_alias.tsv"),
                                delimiter="\t"))
    mark = "PASS" if len(alias) == len(names) else "FAIL"
    ok &= len(alias) == len(names)
    print(f"  母體相異名 {len(names)}  別名表 {len(alias)} 列  {mark}")
    for k in ("exact", "manual", "UNRESOLVED"):
        print(f"    {k:12} {sum(1 for a in alias if a['match_type'] == k)}")

    print("\n== 自檢 3：proposed 全文抽驗 ==")
    alias_by_tc = {a["tc_name"]: a for a in alias}
    for r in (150, 151, 249):
        print(f"\n--- row {r}  D={g(r, 4)} ---")
        print(compose(lk, g, r, alias_by_tc))

    print("\n總判：", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
