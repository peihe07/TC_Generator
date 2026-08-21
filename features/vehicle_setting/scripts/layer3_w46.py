"""W-46 —— Layer 3 歸屬之全掃（依 R-VS37）。

R-VS37：leaf 之 Layer 3 歸屬以其 `reqid_list` 所跨之 CFTS044 章節判定 ——
全部落在單一章節者依該章節，跨多個同層章節者歸 `Common Features`。
SWE ID 中段 token 僅為預設值，衝突時以章節為準。
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


def by_section(secs: list[str]) -> tuple[str, str]:
    """回傳 (章節判定之 Layer 3, 依據)。"""
    uniq = sorted(set(secs))
    if not uniq:
        return "(無 reqid)", "無章節"
    if len(uniq) == 1:
        return SEC_L3.get(uniq[0], f"(未知章節 {uniq[0]})"), uniq[0]
    return "Common Features", ";".join(uniq)
