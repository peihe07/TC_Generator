#!/usr/bin/env python3
"""R-VC16 之 Layer 2 分組規則 —— 單一實作，供 map 產生與驗算共用。

R-VC16 明文「規則為權威，節次清單為其展開結果」，故本模組實作**規則**，
**不硬編 leaf 清單**。map 與 verifier 皆自此匯入，二處不會各改其一。

母體標註（R-VC15）：本模組之 `leaves()` 回傳 **117 leaf 母體**；
`sections()` 回傳 **66 section 母體**。
"""
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

PARENT = re.compile(r"^SWE1-HMI-VC-(\d{3})$")
CHILD = re.compile(r"^SWE1-HMI-VC-(\d{3})-(\d{2})$")

# R-VC16 之驗算目標：Test Set -> (leaf 數, section 數)
TARGETS = {
    "Category Structure":   (24, 13),
    "Controls":             (17, 12),
    "Glove Box":            (12,  8),
    "Settings Behavior":    (15,  6),
    "Settings List":        (30, 17),
    "Ignition Availability": (16, 8),
    "Brake Service":        (2,   1),
    "Cabrio Widget":        (1,   1),
}
ORDER = list(TARGETS)


def test_set(section: str) -> str:
    """R-VC16 之邊界規則。section 為 037 HMI Source ID 尾段之章節號。

    「章」取首段；「次級節號」取第二段（`11.7.1` 之次級節號為 7）。
    """
    parts = [int(x) for x in section.split(".")]
    ch = parts[0]
    if ch == 2:
        return "Category Structure"
    if ch == 3:
        return "Controls"
    if ch in (4, 5, 6, 7):
        return "Glove Box"
    if ch == 11:
        sub = parts[1] if len(parts) > 1 else 0
        return "Settings Behavior" if sub <= 6 else "Settings List"
    if ch == 12:
        return "Settings List"
    if ch == 13:
        return "Ignition Availability"
    if ch == 14:
        return "Brake Service"
    if ch == 16:
        return "Cabrio Widget"
    raise ValueError(f"R-VC16 之規則未涵蓋章 {ch}（section={section!r}）")


def outline_key(s: str):
    return [int(x) for x in s.split(".")]


def load():
    """回傳 (leaf 列之 list[dict], 145 列母體之 list[dict])。"""
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    raw = list(wb["Analysis Report"].iter_rows(values_only=True))
    rows = []
    for r in raw[7:]:                       # 表頭列 = 7，資料列自 8 起
        if r[0] in (None, ""):
            continue
        rid = str(r[0]).strip()
        rows.append({
            "req_id": rid,
            "section": str(r[2]).split("\n")[0].strip().rsplit("_", 1)[-1],
            "title": str(r[3]).strip(),
            "frop": str(r[7]).strip(),
            "sub_cat": str(r[8]).strip(),
        })
    ids = [r["req_id"] for r in rows]
    pc = {CHILD.match(i).group(1) for i in ids if CHILD.match(i)}
    leafset = {i for i in ids
               if CHILD.match(i)
               or (PARENT.match(i) and PARENT.match(i).group(1) not in pc)}
    leaves = [r for r in rows if r["req_id"] in leafset]
    for r in leaves:
        r["test_set"] = test_set(r["section"])
    return leaves, rows
