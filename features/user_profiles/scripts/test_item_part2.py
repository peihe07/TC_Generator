#!/usr/bin/env python3
"""`Test Item` 第二段之查表（55 包 §一）。

`Test Item` 之內容為兩段，**中間空一行**（Pei 2026-08-20 指示）：

    <tc_title>

    (<一句：本條在測什麼>)

空行只影響**呈現**（Excel 之儲存格內兩段分開），
不影響任何閘 —— `TI-1`／`G3`／`audit_second_segment` 之切段皆先濾掉空行。

**第二段之來源為各條 `reasoning` 之「驗證目標」句改寫為英文**（§1.2），
逐條落於 `data/test_item_part2.tsv`，**以 `tc_id` 為鍵** ——
§7 之配對造者與其正向共用同一個 `req_id`（如 `017`／`074` 皆為
`SWE1-HMI-PROF-085`），以 `req_id` 為鍵會把兩條併成一條。

**為什麼放一張表而不是散在七支生成器裡**：同 `popup_guard` 之理由 ——
散開就沒有任何一處記得它們是同一件事，而本項是 189 條**一致**之欄位紀律。
"""

import csv
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent
TSV = FEATURE / "data" / "test_item_part2.tsv"

_CACHE = None


def table() -> dict:
    global _CACHE
    if _CACHE is None:
        with TSV.open(encoding="utf-8") as fh:
            rd = csv.DictReader((l for l in fh if not l.startswith("#")),
                                delimiter="\t")
            _CACHE = {r["tc_id"]: r["sentence"].strip()
                      for r in rd if r.get("tc_id")}
    return _CACHE


def compose(tc_id: str, tc_title: str) -> str:
    """`test_item` 之兩段值。**查不到即停** —— 缺一條就是缺一條。"""
    s = table().get(tc_id)
    if not s:
        raise SystemExit(f"`data/test_item_part2.tsv` 缺 {tc_id} 之第二段")
    return f"{tc_title}\n\n({s})"
