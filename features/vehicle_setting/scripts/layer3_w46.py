"""W-46／W-49 —— Layer 3 歸屬之全掃（依 **R-VS37′** 四分支）。

R-VS37′（31 包 §1，取代 R-VS37）：
  (1) 全部 reqid 落在單一章節      → 依該章節
  (2) 跨多個**同層**章節（段數同）  → `CrossZone Common`
  (3) 跨**異層**章節（段數不同）    → 依**最深**（段數最多）之章節
  (4) 無 reqid                     → 依 token 預設值，標 `UNRESOLVED-SOURCE`

14 輪之實作只有 (1)(2) 兩分支，把 (3) 誤併入 (2)（A-VS50）；本版補齊。
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

# 章節 → Layer 3。取自 12 輪 framework 草案之對照，皆為 037 實際落點。
SEC_L3 = {
    "1.3.2.1.3.1": "LeftFrontHeatedSeat",   "1.3.2.1.3.2": "RightFrontHeatedSeat",
    "1.3.2.1.3.3": "LeftFrontVentedSeat",   "1.3.2.1.3.4": "RightFrontVentedSeat",
    "1.3.2.1.3.11": "HeatedSteeringWheel",  "1.3.2.1.3.12.1": "Stop-StartSystem",
    "1.3.2.1.3.13": "SwitchLHD/RHDConfiguration", "1.3.2.1.18": "ThirdRowHeadrestDump",
    "1.3.2.1.22": "ThirdRowHeadrestDump",   "1.3.2.1.29": "ScreenOFF",
    "1.3.3.3.1.1": "OneStageHeatedSeat",    "1.3.3.3.2.1": "TwoStagesHeatedSeat",
    "1.3.3.3.3.1": "ThreeStagesHeatedSeat", "1.3.3.3.4.1": "TwoStagesVentedSeatsManagement",
    "1.3.3.3.5.1": "ThreeStagesVentedSeatsManagement",
    "1.3.3.3.6.1": "HeatedSteeringWheelManagement", "1.3.3.3.7": "StopStartSystemBehavior",
    "1.3.3.3.8": "SwitchLHD/RHDConfiguration", "1.3.4.2": "PHEVFeatures",
    "1.3.4.2.2": "FeaturesEnableCriteria", "1.3.2.1.3": "HeatedSteeringWheelManagement",
}


def rows() -> list[dict]:
    with (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def token_of(swe_id: str) -> str:
    m = re.match(r"SWE1-VC-(.+)-\d+$", swe_id)
    return m.group(1) if m else "(不合形態)"


def by_section(secs: list[str], token: str = "") -> tuple[str, str, str]:
    """依 R-VS37′ 回傳 (Layer 3, 依據, 分支)。"""
    uniq = sorted(set(secs))
    if not uniq:                                            # (4)
        return token, "無 reqid", "R-VS37′(4)"
    if len(uniq) == 1:                                      # (1)
        return SEC_L3.get(uniq[0], f"(未知章節 {uniq[0]})"), uniq[0], "R-VS37′(1)"
    depths = {s.count(".") for s in uniq}
    if len(depths) == 1:                                    # (2) 同層
        return "CrossZone Common", ";".join(uniq), "R-VS37′(2)"
    deepest = max(uniq, key=lambda s: s.count("."))          # (3) 異層 → 取最深
    return SEC_L3.get(deepest, f"(未知章節 {deepest})"), deepest, "R-VS37′(3)"
