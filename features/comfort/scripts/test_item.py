#!/usr/bin/env python3
"""`test_item` 之兩段式：上半照抄條文原文，下半括號寫該條 TC 之情境。

Pei 2026-08-17 裁定（下放包 94 之後續）：

    一、`pre_conditions` 移除 source class 標籤（見 `write_back.render`）
    二、`test_item` 上半**改為條文原文完整照抄** —— 現行為改寫
        （`The system shall follow…`），須回到 `source_clause` 之原文
    三、下半括號改為**該條 TC 之情境**
        —— 拆分出來之 TC 各自不同，**這是它存在的理由**

上半之單位為「該 leaf 對應之那一句」（Pei 選定）。037 把同一句切成多個 leaf
時（如 `14.19` 之 8 條、`16.13` 之 6 條），那幾條之上半相同而下半各異 ——
**那正是下半存在的理由**。

leaf → 原句之對應由 `scripts/clause_map.py` 產出至
`data/leaf_clause_sentence.tsv`。**「照抄」是機器可證的**（該字串須為該節
`full_text` 之連續子字串，lint 之 `test-item-verbatim` 逐條驗）；
**「選對句」不可機器證**，故其低分列已逐條讀過，訂正記於該檔之 `OVERRIDES`。

原作者所寫之 `test_item` 不丟棄，移入 `test_item_authored`（doc 層，不入
工作簿）—— 它是當初判讀該 leaf 之依據，日後複判時需要它。
"""

import csv
import re
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent
MAP_PATH = FEATURE / "data" / "leaf_clause_sentence.tsv"

# 三個排除式 PC（每條 TC 都有，講的是「這輛車不是哪一種車」）不入情境 ——
# 情境要說的是這一條在什麼狀況下驗什麼，不是它不在什麼狀況下驗。
EXCLUSION_REFS = ("2.14", "16.2", "6.3")
SOURCE_CLASS = re.compile(
    r"\[(?:spec-verbatim|spec-derived|test-setup|ext-verbatim)\]\s*")


def _load_map() -> dict:
    with MAP_PATH.open(encoding="utf-8") as fh:
        return {r["tc_id"]: r["clause_verbatim"]
                for r in csv.DictReader(fh, delimiter="\t")}


CLAUSE = _load_map()


def _condition(line: str) -> str:
    """一行 pre_condition → 情境所用之短語。"""
    t = re.sub(r"^\d+\.\s*", "", " ".join(line.split()))
    t = SOURCE_CLASS.sub("", t)
    t = re.sub(r"\s*\([\d.]+\)$", "", t)                      # 節次括號
    t = re.sub(r"\s*\((?:CFTS\d+|[A-Z][\w ]*)\s+NEWR1L-\d+\)$", "", t)
    # 「, for which …」之後為該條件之理由，情境只要條件本身
    t = re.sub(r",?\s+(?:for which|in which|which is then|whose)\s.*$", "", t)
    return t.rstrip(". ")


def situation(tc: dict) -> str:
    """該條 TC 之情境：其配置條件 ＋ 其觸發步驟。"""
    parts = []
    for line in tc["pre_conditions"].split("\n"):
        if not line.strip():
            continue
        if any(f"({ref})" in line for ref in EXCLUSION_REFS):
            continue
        cond = _condition(line)
        if cond and not cond.lower().startswith(("the head unit is on",)):
            parts.append(cond)
    steps = [re.sub(r"^\d+\.\s*", "", " ".join(s.split()))
             for s in tc["test_procedure"].split("\n") if s.strip()]
    if steps:
        # 最後一步即觸發（§5.7 之判準：動作步驟以其後果之斷言為準，
        # 而後果之斷言在最後一步之 ER）
        trig = steps[-1].rstrip(". ")
        parts.append(trig[0].lower() + trig[1:] if trig else trig)
    return "(" + "; ".join(parts) + ")" if parts else ""


def apply_test_item(tcs: list) -> list:
    """把每條 TC 之 test_item 換成「條文原文 ＋ 空行 ＋ 情境」。"""
    out = []
    for tc in tcs:
        clause = CLAUSE.get(tc["tc_id"])
        if clause is None:                 # 對應表未涵蓋者不動，由 lint 抓
            out.append(tc)
            continue
        row = dict(tc)
        row["test_item_authored"] = tc["test_item"]
        row["test_item"] = f"{clause}\n\n{situation(tc)}"
        out.append(row)
    return out
