"""W-44 —— 委派收斂之重做（30 包 §4）。

08 包 W-34(1) 之 `0 / 174` 已因 A-VS43 撤回（其階數掃描形態漏了 `Level`）。
本腳本以 W-43 建立之橋接重做：

  階數  Comfort `Single-Level` ↔ 本側 `OneStage`
        Comfort `Multi-Level`  ↔ 本側 `TwoStages` / `ThreeStages`
        **`Multi` 無法分辨 Two 與 Three** —— 此為橋接之已知上限
  側別  Comfort 明示 `driver`／`left` 等 ↔ 本側 `LeftFront`／`RightFront`

收斂之定義（同 08 包）：一列之 `comfort_leaf_ids` 經過濾後**縮短**者為
「有收斂」，縮至**恰一個**者為「完全收斂」。
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
STAGE = re.compile(r"\b(one|two|three|single|multi)[\s-]?(stage|level)s?\b", re.I)
SIDE = re.compile(r"\b(driver|passenger|left|right)\b", re.I)
OURS_STAGE = re.compile(r"(One|Two|Three)Stages?")
OURS_SIDE = re.compile(r"(Left|Right)Front")


def comfort_tags() -> dict[str, dict]:
    """每個 Comfort leaf 之階數與側別標記；無標記者為 None（視為相容於任何值）。"""
    txt = json.loads((FEAT / "data/_comfort_leaf_text.json").read_text(encoding="utf-8"))
    out = {}
    for cid, t in txt.items():
        st = {w.lower() for w, _ in STAGE.findall(t)}
        sd = {w.lower() for w in SIDE.findall(t)}
        out[cid] = {
            "stage": ("single" if "single" in st else "multi") if st else None,
            "side": ({"driver": "left", "left": "left",
                      "passenger": "right", "right": "right"}.get(next(iter(sd)))
                     if len(sd) == 1 else None),
        }
    return out


def ours(leaf_id: str) -> dict:
    """本側 leaf 之階數與側別，取自其 SWE ID 中段 token。"""
    m, s = OURS_STAGE.search(leaf_id), OURS_SIDE.search(leaf_id)
    stage = {"One": "single", "Two": "multi", "Three": "multi"}.get(m.group(1)) if m else None
    return {"stage": stage,
            "side": {"Left": "left", "Right": "right"}[s.group(1)] if s else None,
            "exact_stage": m.group(1) if m else None}


def compatible(o: dict, tag: dict) -> bool:
    """Comfort leaf 是否與本 leaf 相容。**未標記之維度不構成排除。**"""
    if o["stage"] and tag["stage"] and o["stage"] != tag["stage"]:
        return False
    return not (o["side"] and tag["side"] and o["side"] != tag["side"])
