"""W-47 —— 交叉前綴污染之全掃（31 包 §5）。

14 輪只掃 `cfts044_include` 一欄、只查 `HS_`/`VS_` 一對前綴（A-VS49）。
本腳本掃**全部值域欄**、對**全部 token** 建立「語意 → 期望值前綴」對照。

判據（R-VS36 之精神：不以單一假設形態下結論）：
每個不符值須回溯其來源 reqid **與其對稱條文**，看對稱側寫什麼 ——
對稱側一律用另一前綴者判 **typo**；對稱側亦用同前綴者判 **別名**。
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
SRC = FEAT / "data/spec_variables.tsv"

VALUE_COLS = ("cfts044_include", "cfts044_exclude", "cfts044_other_arch",
              "lid_values", "dbc", "lid_format")

# token 語意 → 期望之值前綴。順序有意義：先比對較長之樣式。
EXPECT = (
    (re.compile(r"HSW_|Heated_Steering", re.I), "HSW_"),
    (re.compile(r"VentedSeat|Vented_Seat", re.I), "VS_"),
    (re.compile(r"HeatedSeat|Heated_Seat|Heated_Steats", re.I), "HS_"),
)
# 值中之前綴形態：兩到四個大寫字母 ＋ 底線 ＋ 大寫起首
PREFIX_RE = re.compile(r"\b([A-Z]{2,4})_[A-Za-z]")
KNOWN = {"HS", "VS", "HSW"}          # 本 feature 之三個語意前綴


def expect_of(token: str) -> str | None:
    for pat, pref in EXPECT:
        if pat.search(token):
            return pref
    return None


def _values(cell: str, col: str) -> list[str]:
    """展開一格為個別值。`cfts044_other_arch` 為 JSON（架構→值陣列），
    其餘欄為 `|` 分隔。**14 輪之掃描把 JSON 整格當一個值，故只看得到首個命中。**"""
    if col == "cfts044_other_arch" and cell.strip().startswith("{"):
        try:
            return [v for arr in json.loads(cell).values() for v in arr]
        except json.JSONDecodeError:
            return [cell]
    return [v.strip() for v in cell.split("|") if v.strip()]


def scan() -> list[dict]:
    out = []
    with SRC.open(encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            want = expect_of(row["token"])
            if not want:
                continue
            for col in VALUE_COLS:
                for val in _values(row.get(col) or "", col):
                    found = {m for m in PREFIX_RE.findall(val) if m in KNOWN}
                    bad = {p for p in found if p + "_" != want}
                    if bad:
                        out.append({"token": row["token"], "col": col, "value": val,
                                    "expect": want, "found": sorted(bad)})
    return out
