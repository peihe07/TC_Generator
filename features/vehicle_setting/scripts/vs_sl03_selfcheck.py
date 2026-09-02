#!/usr/bin/env python3
"""VS-SL-03 §1 自檢（四項，同 VS-SL-02 §2.6）。

  1. 三本報告列數 457／151／126
  2. assert  PROXI_PENDING ∩ ALIAS_UNRESOLVED = 0
  3. assert  proxi_now 非空而提議為 PENDING 之列 = 0
  4. 抽 3 條（含 `ForwardCollisionWarning-034`／`-035`）貼 proposed 全文
"""

from __future__ import annotations

import csv
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as v1  # noqa: E402
import vs_sl02_dryrun_v2 as v2
import vs_sl03_dryrun_v3 as v3
import vs_sl03_bind as bind  # noqa: E402
from settings_lookup import Lookup, format_proxi  # noqa: E402

warnings.filterwarnings("ignore")
ROOT = v1.ROOT
REPORTS = {
    "VF230": (v1.VF230, "features/vehicle_setting/reports/vf230_settings_dryrun_v3.tsv", 457),
    "BedLowering": (v1.BL, "features/bed_lowering/reports/bl_settings_dryrun_v3.tsv", 151),
    "VehicleCategory": (v1.VC, "features/vehicle_category/reports/vc_settings_dryrun_v3.tsv", 126),
}


def load(path: str) -> list[dict]:
    return list(csv.DictReader(open(ROOT / path), delimiter="\t"))


def flags_of(row: dict) -> set[str]:
    return {f for f in row["flags"].split("｜")[0].split(";") if f}


def compose(lk: Lookup, g, r: int, alias_by_tc: dict) -> str:
    """依 §4 形制組 proposed 全文；選項套 §2.4 之正規化。"""
    item = g(r, 9)
    name = v2.setting_of_v2(g, r)
    alias = alias_by_tc.get(name, {"match_type": "UNRESOLVED"})
    status = alias["match_type"]
    bound = compose.bound
    if name in bound:
        b = bound[name]
        res = v3.query_bound(lk, name, b["item"], b["fip_no"], item)
        proposed, branch, _ = v3.proxi_bound(lk, res, item, v1.proxi_now_of(g, r))
    elif status == "exact":
        res = lk.query(alias.get("hmi_name") or name, item, v1.DR_NO)
        proposed, branch, _ = v2.proxi_v2(lk, res, item, v1.proxi_now_of(g, r), status)
    else:
        res = {"name": name, "path": None, "control": None, "proxi": [], "flags": []}
        proposed, branch, _ = v2.proxi_v2(lk, res, item, v1.proxi_now_of(g, r), status)
    notes: list[str] = []
    if proposed and not proposed[0].get("pending"):
        proposed, notes = v1.propose_proxi(lk, {"proxi": proposed}, item, v1.proxi_now_of(g, r))
    neg = v1.is_negative(item)

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
        leaf, shape = path[-1], v2.control_text(res["control"])
        verb = "is not displayed" if neg else f"is displayed with {shape}"
        proc.append(f'{n}. Check that "{leaf}" {verb}')
        exp.append(f'{n}. "{leaf}" '
                   + ("is not displayed" if neg else f"is displayed as {shape}"))
    tail = f"\n\n分支：{branch}" + (("\n註：" + "；".join(notes)) if notes else "")
    return ("Pre-Condition\n" + "\n".join(pre)
            + "\n\nProcedure\n" + "\n".join(proc)
            + "\n\nExpected Result\n" + "\n".join(exp) + tail)


def main() -> int:
    ok = True
    print("== 自檢 1：三本報告列數 ==")
    for tag, (wb, rep, want) in REPORTS.items():
        ws, g = v1.cells(ROOT / wb)
        actual = len(v1.data_rows(ws, g))
        got = len(load(rep))
        good = actual == got == want
        ok &= good
        print(f"  {tag:16} 工作簿 {actual:4}  報告 {got:4}  期望 {want:4}  "
              f"{'PASS' if good else 'FAIL'}")

    vf = load(REPORTS["VF230"][1])

    print("\n== 自檢 2：assert PROXI_PENDING ∩ ALIAS_UNRESOLVED = 0 ==")
    both = [r["row"] for r in vf
            if {"PROXI_PENDING", "ALIAS_UNRESOLVED"} <= flags_of(r)]
    ok &= not both
    print(f"  交集 {len(both)} 列  {'PASS' if not both else 'FAIL ' + str(both[:10])}")

    print("\n== 自檢 3：assert proxi_now 非空而提議 PENDING 之列 = 0 ==")
    bad = [r["row"] for r in vf
           if r["proxi_now"].strip() and "PENDING" in r["proxi_proposed"]]
    ok &= not bad
    print(f"  違反 {len(bad)} 列  {'PASS' if not bad else 'FAIL ' + str(bad[:10])}")

    print("\n== 自檢 4：proposed 全文抽驗 ==")
    lk, bound = bind.build(ROOT)
    compose.bound = bound
    ws, g = v1.cells(ROOT / v1.VF230)
    names = v1.collect_names(g, v1.data_rows(ws, g))
    alias_by_tc = {a["tc_name"]: a for a in v3.build_alias_v3(lk, names, bound)}
    for r in (150, 151, 14):  # 14 = SWITCH5PowerMode-023，本輪已綁
        print(f"\n--- row {r}  D={g(r, 4)} ---")
        print(compose(lk, g, r, alias_by_tc))

    print("\n總判：", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
