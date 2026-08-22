"""R-VS44 —— 判定結論與未結 DR 之交叉檢查（41 包 §1）。

**任何判準、演繹、對映或正規化，不得使一個已開立且未結之 DR 所問之事項
獲得解答。** 本模組供各判定腳本於**輸出階段**呼叫，非事後人工核對。

未結 DR 之提問範圍以 (token, 值) 為單位宣告 —— 該粒度即判定腳本之輸出粒度。
"""
from __future__ import annotations

import re

# 未結 DR 之提問範圍。key = DR 編號，value = (級別, token 集合, 值之正則, 狀態)
# **待覆者亦在內** —— 其已送出，上游正在作答（R-VS44 逐字）。
#
# 級別（**R-VS44′**，43 包 §2）：
#   "token"  該 DR 問的是某訊號之編碼／位元寬／存在與否 → 該 token 之**任何值**皆在範圍
#   "value"  該 DR 問的是某幾個特定值之對應          → 僅該等值在範圍
#   "clause" 該 DR 問的是某條文之引用或語意          → 該條文所涉全部 token 與值皆在範圍
# **未具名者預設為最寬之級別（clause）。**
OPEN_DR: dict[str, tuple[str, set[str], str, str]] = {
    # DR-15 問的是請求訊號之**編碼**（1 bit 或承載階數）→ **token 級**，值樣式為全部
    "DR-15": ("token", {"FL_HS_RQ", "FR_HS_RQ", "FL_VS_RQ_TGW", "FR_VS_RQ_TGW", "HSW_RQ_TGW"},
              r".", "待覆"),
    "DR-17": ("clause", set(), r"(?!x)x", "待覆"),          # 委派界線，非值域
    "DR-19": ("value", {"EngRun_Stat"}, r"IDLE_STBL|UNLIMITED|LIMITED|\bRUN\b", "待覆（併入 DR-21）"),
    "DR-21": ("value", {"PowerMode", "EngRun_Stat"}, r"IGN_START|IGN_OFF_ACC", "待送"),
    "DR-22′": ("token", {"VC_HdRstPrsnt", "Cooled_Seats", "Heated_Seats",
                         "Heated_Seat_Levels", "Heated_Steering_Wheel"}, r".", "待送"),
    "DR-18": ("value", {"VentedSeatFL", "VentedSeatFR"}, r"HS_HI|HS_OFF", "待送"),
    "DR-8": ("token", {"VC_VEH_LINE"}, r".", "待送"),
    "DR-24′": ("value", {"FL_HS_RQ", "FR_HS_RQ", "FL_VS_RQ_TGW", "FR_VS_RQ_TGW",
                         "HSW_RQ_TGW"}, r"Tsend|Tdisplay", "待送"),
}


def conflict(token: str, value: str) -> str | None:
    """回傳與之衝突之 DR 編號；無衝突回傳 None。"""
    for dr, (_lvl, toks, pat, _state) in OPEN_DR.items():
        if token in toks and re.search(pat, value, re.I):
            return dr
    return None


def guard(token: str, value: str, verdict: str) -> tuple[str, str]:
    """判定結論之輸出閘。落在未結 DR 提問範圍內者一律改標 `DR-CONFLICT`。

    回傳 (verdict, note)。**不採用原結論** —— 即使其為 `derivable`。
    """
    dr = conflict(token, value)
    if dr and verdict != "blocked":
        lvl, _t, _p, state = OPEN_DR[dr]
        return "DR-CONFLICT", f"{dr}（{lvl} 級，{state}）之提問標的，依 R-VS44′ 不採用「{verdict}」"
    return verdict, ""
