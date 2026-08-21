#!/usr/bin/env python3
"""下放包 10a：PM 訊號對照（R-1 v2 + R-7）。

A1 之七種訊號（三件組 → `MESSAGE.Signal`）與 A6 之 DBC `VAL_` 標籤，
逐字取自 `10a_pm_full.md` §A1／§A6 兩表，不自行擴充。
"""

from __future__ import annotations

import re

# A1：三件組（R-1 v1，已撤銷） → `MESSAGE.Signal`
TRIPLET_TO_DOTTED = {
    "RemStActvSts in STATUS_BH_BCM2 on BH-CAN": "STATUS_BH_BCM2.RemStActvSts",
    "Batt_ST_Crit in STATUS_LIN on BH-CAN": "STATUS_LIN.Batt_ST_Crit",
    "DriverDoorSts in STATUS_BH_BCM1 on BH-CAN": "STATUS_BH_BCM1.DriverDoorSts",
    "PN14_LS_Actv in STATUS_LIN on BH-CAN": "STATUS_LIN.PN14_LS_Actv",
    "PN14_LS_Lvl7 in STATUS_LIN on BH-CAN": "STATUS_LIN.PN14_LS_Lvl7",
    "PsngrDoorSts in STATUS_BH_BCM1 on BH-CAN": "STATUS_BH_BCM1.PsngrDoorSts",
    "Radio_btn0 in CLIMATIC_PANEL on BH-CAN": "CLIMATIC_PANEL.Radio_btn0",
}

# A6：DBC `VAL_` 列舉，raw → label
VAL_LABELS = {
    "STATUS_BH_BCM2.RemStActvSts": {0: "Remote Start Not Active",
                                    1: "Remote Start Active"},
    "STATUS_BH_BCM1.DriverDoorSts": {0: "Closed", 1: "Open"},
    "STATUS_BH_BCM1.PsngrDoorSts": {0: "Closed", 1: "Open"},
    "STATUS_LIN.Batt_ST_Crit": {0: "False", 1: "True"},
    "STATUS_LIN.PN14_LS_Actv": {0: "Not_Active", 1: "Active"},
    "STATUS_LIN.PN14_LS_Lvl7": {0: "Not_Active", 1: "Active"},
    "CLIMATIC_PANEL.Radio_btn0": {0: "Not_Pressed", 1: "Pressed"},
}

LABEL_TO_RAW = {sig: {v: k for k, v in table.items()}
                for sig, table in VAL_LABELS.items()}

RE_HEX = re.compile(r"^\[(\d+)h\]$")


def to_dotted(text: str) -> str:
    """A1：三件組逐字換為 `MESSAGE.Signal`。"""
    for triplet, dotted in TRIPLET_TO_DOTTED.items():
        text = text.replace(triplet, dotted)
    return text


def resolve_raw(signal: str, value: str) -> int | None:
    """把工作簿之值（`[1h]` 或 `"Label"`）解為 DBC raw 值。

    解不出者回傳 None —— 不猜，交由呼叫端標記待覆核（§8.4.1）。
    """
    value = value.strip().strip('"').strip()
    hexed = RE_HEX.match(value)
    if hexed:
        return int(hexed.group(1))
    return LABEL_TO_RAW.get(signal, {}).get(value)


def assignment(signal: str, raw: int) -> str:
    """R-1 v2(a)/(b) 之賦值片段：`<MSG>.<Sig> = <raw> (<label>)`。"""
    return f"{signal} = {raw} ({VAL_LABELS[signal][raw]})"


def send_step(signal: str, raw: int) -> str:
    """R-1 v2(a)：Procedure 之賦值步驟。"""
    return f"Send CAN: {assignment(signal, raw)}"


def er_sent(signal: str, raw: int) -> str:
    """R-1 v2(b)：ER 之賦值斷言。"""
    return f"{assignment(signal, raw)} is sent"
