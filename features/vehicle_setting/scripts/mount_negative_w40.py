"""W-40(1) —— 負向測試候選之掛載（28 包 §4 之判準）。

判準（分析層裁定，Pei 得推翻）：
  token 若有其他 Functional leaf 引用 → 掛在該等 leaf，於其 TC 之負向分支承載
  token 無任何 Functional leaf 引用 → 不寫負向 TC，標 `no_mount_point`

token 之查法依 **R-VS36**：三形態並試取聯集，三者命中數分別列出 ——
  (1) `$X$`  (2) 裸名 `X`（詞界）  (3) `(PROXI parameter|signal|LID|parameter)\s+X`
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
SRC = FEAT / "data/negative_test_candidates.tsv"
LEAVES = FEAT / "data/leaves.tsv"
NONFUNC = FEAT / "data/non_functional_leaves.tsv"
DESC = "(?:PROXI parameter|signal|LID|parameter)"


def leaf_texts() -> list[tuple[str, str]]:
    """Functional leaf 之 (swe_id, 全文)。非 Functional 者不入母體（R-VS15）。"""
    with NONFUNC.open(encoding="utf-8") as f:
        drop = {r["swe_id"] for r in csv.DictReader(f, delimiter="\t")}
    out = []
    with LEAVES.open(encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            if r["swe_id"] in drop:
                continue
            out.append((r["swe_id"], " ".join(v or "" for v in r.values())))
    return out


def hits(bare: str, texts: list[tuple[str, str]]) -> dict[str, set[str]]:
    """R-VS36 三形態之命中 leaf 集合，分別回傳。"""
    pats = {
        "dollar": re.compile(re.escape(f"${bare}$")),
        "bare": re.compile(rf"\b{re.escape(bare)}\b"),
        "descr": re.compile(rf"{DESC}\s+{re.escape(bare)}\b", re.I),
    }
    return {k: {sid for sid, t in texts if p.search(t)} for k, p in pats.items()}
