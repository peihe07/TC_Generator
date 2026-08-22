"""W-97 —— 交付本其餘四欄之樣式比對（56 包 §4，34 輪 §6-4）。

比對對象：SWC 0708 交付本（286 列）之 `Test Item`／`Pre-Conditions`／
`Test Case Design Methods`／`Test Case Priority` 四欄，
對本 feature 現行 76 條之同名欄。

**只列，不對齊** —— 對齊屬交付形式，Pei 裁（35 輪禁區）。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

import openpyxl

FEAT = Path(__file__).resolve().parents[1]
SWC = Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/SWC/"
           "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
           "Specification & Result_SWQT_SWC_20260708.xlsx")
COLS = {"test_item": 8, "pre_conditions": 9, "design_method": 17, "priority": 15}
OURS = ["generated/batch01_v5.json", "generated/batch02_v3.json",
        "generated/batch03_v4.json", "generated/batch04_v5.json",
        "generated/batch05_v3.json", "generated/batch06_v3.json",
        "generated/batch07_v3.json", "generated/batch08_v4.json",
        "generated/batch10_v3.json", "generated/batch11_v3.json",
        "generated/batch12_v3.json"]


def swc_rows() -> list[dict]:
    ws = openpyxl.load_workbook(SWC, read_only=True, data_only=True)[
        "Test Case Specification 測試用例規範"]
    out = []
    for row in ws.iter_rows(min_row=10, values_only=True):
        if not row[1]:
            continue
        out.append({k: (str(row[i]) if row[i] is not None else "")
                    for k, i in COLS.items()})
    return out


def our_rows() -> list[dict]:
    out = []
    for f in OURS:
        for tc in json.loads((FEAT / f).read_text(encoding="utf-8"))["tcs"]:
            out.append({k: tc[k] for k in COLS})
    return out


def bracket_tail(s: str) -> bool:
    """R-VS6：下半段全在括號內，且以 `)` 收尾。"""
    return "(" in s and s.rstrip().endswith(")")


def two_part(s: str) -> bool:
    """R-VS6(a)：上下兩段以單一空行分隔。"""
    return "\n\n" in s


def numbered(s: str) -> bool:
    return bool(re.match(r"\s*1\.", s))


def report(name: str, rows: list[dict], n: int) -> dict:
    ti = [r["test_item"] for r in rows if r["test_item"]]
    pc = [r["pre_conditions"] for r in rows if r["pre_conditions"]]
    return {
        "列數": n,
        "test_item 非空": len(ti),
        "test_item 有空行分段（R-VS6(a)）": sum(map(two_part, ti)),
        "test_item 以 ) 收尾（R-VS6 下半段）": sum(map(bracket_tail, ti)),
        "test_item 含 $var$": sum("$" in x for x in ti),
        "test_item 平均行數": round(sum(x.count("\n") + 1 for x in ti) / max(len(ti), 1), 2),
        "pre_conditions 非空": len(pc),
        "pre_conditions 為編號清單": sum(map(numbered, pc)),
        "pre_conditions 平均項數": round(
            sum(len(re.findall(r"^\s*\d+\.", x, re.M)) for x in pc) / max(len(pc), 1), 2),
        "design_method 值域": dict(collections.Counter(r["design_method"] for r in rows)),
        "priority 值域": dict(collections.Counter(r["priority"] for r in rows)),
    }


def main() -> None:
    s, o = swc_rows(), our_rows()
    rs, ro = report("SWC 0708", s, len(s)), report("vehicle_setting", o, len(o))
    keys = list(rs)
    print(f"{'項':44s} {'SWC 0708 交付本':>34s} {'vehicle_setting':>34s}  判")
    diff = 0
    for k in keys:
        a, b = rs[k], ro[k]
        same = a == b
        if isinstance(a, dict):
            same = set(a) == set(b)
        if not same:
            diff += 1
        print(f"{k:44s} {str(a)[:34]:>34s} {str(b)[:34]:>34s}  {'同' if same else '**不一致**'}")
    print(f"\n不一致欄位項數：{diff}")


if __name__ == "__main__":
    main()
