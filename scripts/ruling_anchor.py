"""條文錨點之單一定義（R-G43(c)／R-G43(d)，Pei 2026-09-05）。

**解析面與指紋面同源。** `rulings_hash.py`（指紋）與 `canon_refs.py`（引用解析）
必須用同一個錨點判準，否則會出現「有指紋但解析不到」之洞 ——
GC-06 §一 A-GC15 實測即此：指紋表重生後 `canon_refs` 之 ruling unresolved
仍有 963 處，全部落在「台帳有錨、FO 無」，因 `canon_refs` 當時只索引 FO。

判準（R-G43(c)）：條號須**領頭於標題行**（`## R-Gnn — …`／`### R-Gnn — …`）。
條號在括號內之敘述式標題（`## 合併包 19 之全域條文（R-G26–R-G31）`）不算錨點。
"""
from __future__ import annotations

import re

# 子條之三種書寫（`R-VS57 之 (4)`／`R-VS57(4)`／`R-VS7(a)′`）一律收進 id，
# 否則子條會與母條同 id 而假性碰撞。
RE_ANCHOR = re.compile(
    r"^(?P<hashes>#{2,4})\s*"
    r"(?P<base>R-[A-Z]{0,3}\d+[A-Za-z]?)"
    r"(?P<sub>(?:\s*之)?\s*\([0-9a-z]+\))?"
    r"(?P<prime>[′″‴]*)"
    r"(?P<qual>\s*(?:之補充|之修訂|之解釋|之更正|但書))?"
    r"\s*(?P<rest>.*)$"
)


def anchor_ruling_numbers(text: str, prefix: str = "R-G") -> set[str]:
    """自 markdown 全文取**錨點所載**之條號（去前綴之數字部）。

    `canon_refs` 之 ruling 索引用之；只認錨點，不認行內提及 ——
    行內提及會把「依 R-G34」這種引用讀成錨點而造出假錨。
    """
    out: set[str] = set()
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        m = RE_ANCHOR.match(line)
        if m and m.group("base").startswith(prefix):
            out.add(m.group("base")[len(prefix):])
    return out
