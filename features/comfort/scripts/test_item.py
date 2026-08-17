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
    """該條 TC 之測項定義：**做了什麼 → 預期看到什麼**。

    第一版把配置條件（軸 PC）也寫進來，實測之後三個毛病都出來了：

      - 同一句配置被寫兩次（`-425` 之 Comfort features 出現兩遍）
      - 理由子句一併抄入（`…, which is absent on some soft top vehicles`）
      - **根本上抄錯了東西** —— 它把 J 欄之 pre_conditions 複述一遍，
        而 J 欄就在旁邊。95 §2 要的是「這一條驗什麼」，
        不是「這一條的前提是什麼」。

    長度：中位 97 → 95，**最長 356 → 223**，>200 者由 12 條降為 2 條。
    且拆分列之下半相同者由 **11 條降為 1 條** —— 只差觀察結果的那幾對
    （`032-01` 之 HI／LO、`040-01` 之三個狀態值），加上 ER 就分得開了。
    """
    steps = [re.sub(r"^\d+\.\s*", "", " ".join(s.split()))
             for s in tc["test_procedure"].split("\n") if s.strip()]
    ers = [re.sub(r"^\d+\.\s*", "", " ".join(s.split()))
           for s in tc["expected_result"].split("\n") if s.strip()]
    if not steps and not ers:
        # marker 列（L／M 刻意留白，R-C24／R-C38／R-C39）。其下半不能空 ——
        # 空的話該格只剩一段條文，讀者無從知道這一列為何沒有步驟。
        # 寫其**為何無測項**，出處仍在 Remarks，不在此複述。
        mark = (tc.get("remarks") or "").split("]")[0].lstrip("[")
        if mark == "BLOCKED-NON-HMI":
            return ("(no observable behaviour on the HMI, so this delivery "
                    "carries no test case for it; see Remarks)")
        return ("(the requirement's content is owned by another document, so "
                "this delivery carries no test case for it; see Remarks)")
    # 最後一步即觸發（§5.7：動作步驟以其後果之斷言為準，而該斷言在末步之 ER）
    trig = steps[-1].rstrip(". ") if steps else ""
    if trig:
        trig = trig[0].lower() + trig[1:]
    obs = ers[-1].rstrip(". ") if ers else ""
    if trig and obs:
        lower = f"({trig} -> {obs})"
    else:
        lower = f"({trig or obs})"
    return HAND_WRITTEN.get(tc["tc_id"], lower)


# 合成分不開者，逐條手寫。**其分別在步驟之中段而非末步**，
# 而合成器只讀末步 —— 這是它的界線，不是它的錯。
HAND_WRITTEN = {
    "NR1L-ComfortHMI-192":
        "(let the popup time out untouched -> it is gone after five seconds)",
    "NR1L-ComfortHMI-410":
        "(press the icon again just before it times out -> the popup stays, "
        "and the five seconds start again)",
}


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
