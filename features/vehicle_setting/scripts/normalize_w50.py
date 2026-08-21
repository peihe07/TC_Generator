"""W-50 —— 值域正規化與剩餘 token 之污染掃描（33 包 §4）。

R-VS39 之正規化鍵：casefold ＋ 連續空白壓為單一空白 ＋ 去首尾空白
                   ＋ 依 R-VS38 判定之 typo 前綴修正。
**原始寫法一律保留**，本腳本只增欄。
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
SEMANTIC = ("HS_", "VS_", "HSW_")
# R-VS38 已判定之 typo 前綴修正（15 輪 W-47，4 值）
TYPO_FIX = {"HS_HI": "VS_HI", "HS_OFF": "VS_OFF"}


def norm(value: str, fix_typo: bool = True) -> str:
    """R-VS39 之正規化鍵。`fix_typo` 為 False 時只做大小寫與空白正規化。"""
    k = re.sub(r"\s+", " ", value).strip().casefold()
    if fix_typo:
        for bad, good in TYPO_FIX.items():
            if "vented" in k:                       # 僅對通風座椅之值修正
                k = k.replace(bad.casefold(), good.casefold())
    return k


def values(cell: str, col: str) -> list[str]:
    if col == "cfts044_other_arch" and cell.strip().startswith("{"):
        try:
            return [v for arr in json.loads(cell).values() for v in arr]
        except json.JSONDecodeError:
            return [cell]
    return [v.strip() for v in cell.split("|") if v.strip()]


def rows() -> list[dict]:
    with SRC.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))
