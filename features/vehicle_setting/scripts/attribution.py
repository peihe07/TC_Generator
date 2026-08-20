"""W-23(b) —— 值域差異之歸因判準（C1–C5）。

02 上繳 §2.2 以人讀將 W-19 之 39 項差異分為五類，**未寫成判準**，
故下輪重跑會再次全部列出。本模組將其判準化。

  C1 別名切分   我方以 ` / ` 切分 CFTS044 之 `全名 / 縮寫`，
                於是縮寫成為「僅 CFTS 有」之值
  C2 LID 列粒度 LID 之一列同時對映狀態訊號與失效訊號，
                故其值集合含 Fail_* 而 CFTS044 之 token 僅指狀態
  C3 Format 解析殘缺  我方解析跨越了多訊號之邊界（已於 `lid_parse.py` 修正；
                此類應收斂為 0，仍出現即為回歸）
  C4 規格引用子集     CFTS044 只引用其所需之值，非列舉全集
  C5 縮寫 vs 全名     二來源之命名體系不同（`BEV` vs `battery electric vehicle`）

**只有不落入 C1–C5 者進待判清單。**
每輪列 C1–C5 計數以證明判準運作（§5a 條 11：檢查項須確認其在該階段確實可能失敗）。
"""

from __future__ import annotations

import re

FAIL_RE = re.compile(r"\bfail[_ ]?(not[_ ]?)?present\b", re.I)
ABBR_RE = re.compile(r"^[a-z]{2,6}([_ ][a-z]{2,6})?$", re.I)


def _initials(s: str) -> str:
    return "".join(w[0] for w in re.split(r"[\s_]+", s) if w).lower()


def classify(token: str, src_a: str, only_a: set[str], src_b: str,
             only_b: set[str], both: set[str]) -> str | None:
    """回傳 C1–C5 之一，或 None（＝進待判清單）。"""
    extra = only_a | only_b

    # C3 —— 值內殘留另一訊號之名或「N bit signal」字樣＝解析跨界
    if any(re.search(r"\bbit signal\b|STATFailSts|STATSts", v, re.I) for v in extra):
        return "C3"

    # C2 —— 差集全為 Fail_* 而另一側無
    if extra and all(FAIL_RE.search(v) for v in extra):
        return "C2"

    # C1 —— 差集中每個值都是 both 或對側某值之縮寫／首字母縮寫
    ref = both | (only_b if extra is only_a else only_a) | only_a | only_b
    def is_alias(v: str) -> bool:
        for r in ref:
            if v == r:
                continue
            if _initials(r) and v.replace(" ", "").replace("_", "") == _initials(r):
                return True
            if v in r or r in v:
                return True
        return False
    if extra and all(is_alias(v) for v in extra):
        return "C1"

    # C5 —— 一側全為短碼、另一側全為長名，且短碼為長名之首字母
    if only_a and only_b:
        sa = all(ABBR_RE.match(v) and len(v) <= 8 for v in only_a)
        sb = all(len(v) > 8 for v in only_b)
        if (sa and sb) or (all(ABBR_RE.match(v) and len(v) <= 8 for v in only_b)
                           and all(len(v) > 8 for v in only_a)):
            return "C5"

    # C4 —— 單向子集：一側之值全在另一側內（差集單向）
    if both and (not only_a or not only_b):
        return "C4"

    return None
