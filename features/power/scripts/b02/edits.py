#!/usr/bin/env python3
"""批 1（下放包 02）PM 回修之編輯規則：M3／M11／M15。

M10 之摘句另置於 excerpt.py。本模組只產生「欄位新值」，
不觸碰 xlsx；寫回由 apply.py 經 xlsx_surgical 為之。
"""

from __future__ import annotations

import re

# --- M3 訊號記法（R-1）：僅施於 pre/input/proc/er 四欄 ---------------------
# 依 02_pm_signal_map.md 第一節逐字照抄，不得自行擴充。
SIGNAL_FIELDS = ("pre", "input", "proc", "er")

CAN_MAP = {
    "STATUS_BH_BCM2.RemStActvSts": "RemStActvSts in STATUS_BH_BCM2 on BH-CAN",
    "STATUS_LIN.Batt_ST_Crit": "Batt_ST_Crit in STATUS_LIN on BH-CAN",
    "STATUS_BH_BCM1.DriverDoorSts": "DriverDoorSts in STATUS_BH_BCM1 on BH-CAN",
    "STATUS_LIN.PN14_LS_Actv": "PN14_LS_Actv in STATUS_LIN on BH-CAN",
    "STATUS_LIN.PN14_LS_Lvl7": "PN14_LS_Lvl7 in STATUS_LIN on BH-CAN",
    "STATUS_BH_BCM1.PsngrDoorSts": "PsngrDoorSts in STATUS_BH_BCM1 on BH-CAN",
    # A-PM01：DBC 實為 Radio_btn0（小寫 b），大小寫一併更正
    "CLIMATIC_PANEL.Radio_Btn0": "Radio_btn0 in CLIMATIC_PANEL on BH-CAN",
}

# A-PM02：同一內部訊號之兩種拼法，統一為多數式
INTERNAL_MAP = {"PhoneCall.Info": "Phone_Call.Info"}

# A-PM03：$Radio_Theme$ 為 PROXI 參數，雖 DBC 有同名 CAN signal 亦不套三件組。
# PROXI 層以 `$...$` 包夾，CAN_MAP 之鍵皆不含 `$`，故本規則天然不觸及之。

# 舊式 CAN 記法之偵測（檢查 P）：全大寫 message + `.` + signal。
# 內部訊號（Phone_Call.Info、TLM_Status.Info…）之 message 段含小寫，不命中。
CAN_LEGACY_RE = re.compile(r"\b[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\b")


def apply_signal_map(text: str) -> str:
    """M3：CAN 七種改三件組、內部訊號拼法統一。"""
    for old, new in INTERNAL_MAP.items():
        # 避免把已正確之 Phone_Call.Info 再改；僅換無底線之舊拼法
        text = re.sub(rf"(?<![A-Za-z_]){re.escape(old)}\b", new, text)
    for old, new in CAN_MAP.items():
        text = text.replace(old, new)
    return text


# --- M11 首字大寫（R-4）------------------------------------------------------


def capitalise_first(test_item: str) -> str:
    """verbatim 中段起抄者，首字母轉大寫（排版正規化）。"""
    for i, ch in enumerate(test_item):
        if ch.isalpha():
            return test_item[:i] + ch.upper() + test_item[i + 1:]
        if not ch.isspace():
            break
    return test_item


# --- M15 sibling 區分 token（S4）--------------------------------------------

PAREN_LINE_RE = re.compile(r"^\((.+)\)$")


def rewrite_paren(test_item: str, token: str) -> str:
    """將區分 token 前置於括號下半：`(<token> — <原內容>)`。

    前置而非附加，是因 canon §4.3 明訂「the tag IS the distinguishing
    token」，區分項應最先可見。原內容逐字保留。
    """
    out = []
    done = False
    for line in test_item.split("\n"):
        stripped = line.strip()
        m = PAREN_LINE_RE.match(stripped)
        if m and not done:
            out.append(f"({token} — {m.group(1)})")
            done = True
        else:
            out.append(line)
    if not done:
        raise ValueError("找不到括號下半，無法寫入區分 token")
    return "\n".join(out)
