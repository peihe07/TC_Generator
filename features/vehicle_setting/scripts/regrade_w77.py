"""W-77 —— 依 R-VS47 之可寫性重分級（46 包 §1）。

  W0  無未解值
  W1  有未解值，惟扣除 PENDING 後仍有 ≥2 個可執行步驟，
      **且其驗證目標本身不是該未解值**
  W2  否則

操作型判準（兩條件皆須成立方為 W1）：
  (b) **後件（consequent）不含未解值** —— 驗證目標與未解值分離
  (a) **前件（antecedent）至少有一個已解之 (token, 值) 條件** ——
      扣除 PENDING 步驟後仍有可執行之 setup，加上驗證步驟即 ≥2
"""
from __future__ import annotations

import re

# 後件之起點：`THEN`／`then`／`, the HU shall`／`the HMI shall` 等
CONSEQ = re.compile(r"\bTHEN\b|\bthen\b|(?<=[),])\s*(?:-\s*)?(?=[Tt]he (?:HU|HMI|CCDMF|ETM|TLM)\b)")


def split_clause(text: str) -> tuple[str, str]:
    """切為 (前件, 後件)。無明顯分界者，前件為空、全文為後件。"""
    m = CONSEQ.search(text)
    if not m:
        return "", text
    return text[:m.start()], text[m.end():]


def grade(text: str, pairs: list[tuple[str, str]], unresolved: set[tuple[str, str]]) -> tuple[str, dict]:
    """`pairs` 為該條文之全部 (token, 值)；`unresolved` 為其中未解者。"""
    if not any(p in unresolved for p in pairs):
        return "W0", {"理由": "無未解值"}
    ante, cons = split_clause(text)
    in_cons = [p for p in pairs if p in unresolved
               and (re.search(re.escape(p[0]), cons) and re.search(re.escape(p[1][:24]), cons))]
    resolved_in_ante = [p for p in pairs if p not in unresolved
                        and re.search(re.escape(p[0]), ante)]
    # **R-VS71（77 包 §1，Pei 2026-08-23）：值之未解不阻塞生成。**
    # 得判 W2 者僅二類 —— (a) 條文無可測內容；(b) 與他 leaf 不可分辨。
    # 二者皆非本函式所判（(a) 由 `PREAMBLE` 判 B4、(b) 由冗餘掃描判 B7），
    # 故本函式**不再回傳 W2**。原式保留於下，不刪（R-TM13）：
    #
    #     if in_cons:
    #         return "W2", {"理由": "未解值位於後件 —— 驗證目標即該值", …}
    #     if not resolved_in_ante:
    #         return "W2", {"理由": "前件無已解條件 —— 扣除 PENDING 後不足 2 步", …}
    #
    # 「扣除 PENDING 不足 2 步」之判準**經 R-VS71 廢止**。
    if in_cons:
        return "W1", {"理由": "未解值位於後件 —— 依 R-VS71 照寫，該處標 PENDING／"
                              "dr_dependent／impl_gap",
                      "後件之未解值": [f"{t}={v[:24]}" for t, v in in_cons]}
    if not resolved_in_ante:
        return "W1", {"理由": "未解值僅在前件而前件無已解條件 —— 依 R-VS71 照寫",
                      "前件之已解條件": []}
    return "W1", {"理由": "未解值僅在前件，且前件另有已解條件",
                  "前件之已解條件": [f"{t}={v[:24]}" for t, v in resolved_in_ante][:3]}
