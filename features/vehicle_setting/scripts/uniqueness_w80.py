"""W-80 —— R-VS48：R-VS43(1) 之「目標唯一」判定（47 包 §2）。

R-VS43 之初版實作僅實現「值域大小為 2」，**後半「目標在值域內唯一可判」
從未被實現**（A-VS89 之成因之一）。本模組實現 (a)(b)(c) 三路。
"""
from __future__ import annotations

import re

# **`left`／`right` 不列為停用詞** —— R-VS48(b) 之範例即以 `right` 為共享實詞。
STOPW = {"seat", "the", "of", "and", "a", "an", "signal", "heated", "vented",
         "steering", "wheel", "state", "status"}


def _segs(s: str) -> list[str]:
    """去分隔符後之字元段（小寫）。"""
    return [x for x in re.split(r"[_\s\-/]+", s.strip().lower()) if x]


def is_abbrev(v: str, d: str) -> bool:
    """(a) 縮寫關係：v 去分隔符後之字元序列為 d 去分隔符後之**子序列**，
    且首字元相同、長度 ≥ 3、且 v 不長於 d（R-VS48(a) 之範例
    `ENS_DSBL` → `ENS disabled`：`ENSDSBL` 為 `ENSDISABLED` 之子序列）。"""
    a = "".join(_segs(v))
    b = "".join(_segs(d))
    if len(a) < 3 or len(a) > len(b) or a[0] != b[0]:
        return False
    i = 0
    for ch in a:
        i = b.find(ch, i)
        if i < 0:
            return False
        i += 1
    return True


def words(s: str) -> set[str]:
    return {w for w in _segs(s) if w not in STOPW and len(w) > 1}


def unique_target(v: str, domain: set[str], alias: dict[str, set[str]] | None = None
                  ) -> tuple[str | None, str]:
    """回傳 (唯一之 d, 依據)；無或多於一個則回傳 (None, 理由)。"""
    alias = alias or {}
    for name, test in (("(a) 縮寫", lambda d: is_abbrev(v, d)),
                       ("(b) 共享實詞", lambda d: bool(words(v) & words(d))),
                       ("(c) 來源別名對", lambda d: d.lower() in
                        {x.lower() for x in alias.get(v.lower(), set())})):
        hit = [d for d in domain if test(d)]
        if len(hit) == 1:
            return hit[0], f"{name}：唯一命中 `{hit[0]}`"
        if len(hit) > 1:
            return None, f"{name}：命中 {len(hit)} 個 {sorted(hit)[:3]} —— 非唯一"
    return None, "(a)(b)(c) 皆無命中"
