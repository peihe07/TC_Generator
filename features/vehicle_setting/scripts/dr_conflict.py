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
    # **R-VS61（63 包 §3，Pei 2026-08-23）**：無匯流排對應者仍產 TC，
    # 其值取分析／規格之逐字（不附 label），標 `dr_dependent = DR-19`。
    # 本 DR 之性質由**阻塞轉確認**，故自閘中移出；其 token／值仍登記於下以留痕。
    # "DR-19": ("value", {"EngRun_Stat"}, r"IDLE_STBL|UNLIMITED|LIMITED|\bRUN\b", "待覆"),
    "DR-19": ("value", set(), r"(?!x)x", "待覆（性質轉確認，R-VS61；不阻塞）"),
    "DR-21": ("value", {"PowerMode", "EngRun_Stat"}, r"IGN_START|IGN_OFF_ACC", "待送"),
    # DR-22′ **已撤回**（R-VS49）—— 四個 PROXI 參數之值域已有來源，其閘同步移除。
    # `VC_HdRstPrsnt` 之缺仍在，改由 DR-22（B3 類）承載。
    "DR-22": ("token", {"VC_HdRstPrsnt"}, r".", "待送"),
    "DR-18": ("value", {"VentedSeatFL", "VentedSeatFR"}, r"HS_HI|HS_OFF", "待送"),
    # **R-VS62（63 包 §4，Pei 2026-08-23）**：`VC_VEH_LINE` 之車型碼取自
    # `PROXI_HDCC27_R3` 之 Format 分頁列 466。`332`／`WS`／`DT`／`HDCC` **已解**；
    # DR-8′ 縮限為 `M182`／`M189`／`M240` 三碼。
    "DR-8": ("value", {"VC_VEH_LINE"}, r"M182|M189|M240", "待送（縮為三碼，R-VS62）"),
    "DR-24′": ("value", {"FL_HS_RQ", "FR_HS_RQ", "FL_VS_RQ_TGW", "FR_VS_RQ_TGW",
                         "HSW_RQ_TGW"}, r"Tsend|Tdisplay", "待送"),
}


def conflict(token: str, value: str) -> str | None:
    """回傳與之衝突之 DR 編號；無衝突回傳 None。"""
    for dr, (_lvl, toks, pat, _state) in OPEN_DR.items():
        if token in toks and re.search(pat, value, re.I):
            return dr
    return None


# 得過閘之結論。**不含 `"blocked"`** —— 已阻塞者無結論可解，
# 舊版以 `verdict != "blocked"` 靜默直通，其誤用在計數上與正確呼叫不可分辨
# （32 輪之實例：58 次被誤記為「被攔」）。55 包 §2 令改為 raise。
CONCLUSIONS = frozenset({"resolved", "derivable", "write"})


def guard_new_conclusion(token: str, value: str, conclusion: str) -> tuple[str, str]:
    """判定結論之輸出閘。落在未結 DR 提問範圍內者一律改標 `DR-CONFLICT`。

    回傳 (conclusion, note)。**不採用原結論** —— 即使其為 `derivable`。

    `conclusion` 僅受 `CONCLUSIONS`；其餘一律 **raise**，不靜默直通。
    """
    if conclusion not in CONCLUSIONS:
        raise ValueError(
            f"guard_new_conclusion: conclusion 須為 {sorted(CONCLUSIONS)} 之一，"
            f"得到 {conclusion!r}。已阻塞之結論無須過閘，不應呼叫本函式。")
    dr = conflict(token, value)
    if dr:
        lvl, _t, _p, state = OPEN_DR[dr]
        return "DR-CONFLICT", f"{dr}（{lvl} 級，{state}）之提問標的，依 R-VS44′ 不採用「{conclusion}」"
    return conclusion, ""


def guard(token: str, value: str, verdict: str) -> tuple[str, str]:
    """**已棄用**（55 包 §2）—— 保留供既有呼叫端過渡，見 R-TM13。

    `verdict == "blocked"` 時直接回傳，此即其靜默直通之缺陷所在。
    新程式一律用 `guard_new_conclusion()`。
    """
    if verdict == "blocked":
        return verdict, ""
    return guard_new_conclusion(token, value, verdict)
