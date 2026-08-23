"""W-146（78 包 §3／§5）—— D／E／F 三型之樣板抽驗，每型 2 條共 6 條。

**其 procedure 之觸發與 ER 之標的逐條自條文取，不套 A 型樣板。**
通過 §9 自檢 ＋ 固定錨點 ＋ 分析層抽驗者，其型之樣板方得放量。

型與其條文形態：
  **D 送出型**  `When the customer selects …, the HU shall send an on-change
                $HSW_RQ_TGW$ = [Pressed / PSD] signal to the CSWM within <Tsend>`
                → 觸發為**使用者按壓**；ER 之標的為**匯流排上之送出**
  **E 狀態變更型** `When the HU receives a $HSW_Stat_2$ = […] signal, the HU shall
                change the stored status … and change the display …`
                → 觸發為**收到狀態訊號**；ER 之標的為**顯示之變更**
  **F 啟用／停用型** `The HU shall enable … and display … if $VC_VEH_LINE$ = [WL]
                and $Hybrid_Type$ = [Plugin Hybrid Electric Vehicle]`
                → 觸發為**兩個配置參數之組合**；ER 之標的為**功能與入口之啟用**
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]
HSW2 = "STATUS_CLIMATE8.Tri_Level_HSW_StatSts"
HSW2_LAB = {0: "Heated_steering_wheel_off", 1: "Heated_steering_wheel_low",
            2: "Heated_steering_wheel_medium", 3: "Heated_steering_wheel_high"}
HSW_TLM = "TELEMATIC_VEHICLE_SETUP3.HSW_Tlm"


def build() -> dict:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}

    def src(q: str) -> str:
        return "\n".join(blocks[q]["text"].split("\n")[1:]).strip()

    def base(leaf: str, ts: str, title: str, lower: str, proc, er, method,
             prio="P1", **kw) -> dict:
        d = {"leaf_id": leaf, "test_set": ts, "tc_title": title,
             "test_item": src(re.findall(r"\d{7}", l2r[leaf]["reqid_list"])[0])
                          + "\n\n(" + lower + ")",
             "pre_conditions": kw.pop("pre"), "input_test_data": "NA",
             "test_procedure": "\n".join(proc), "expected_result": "\n".join(er),
             "specification_reference": l2r[leaf]["reqid_list"].replace(";", "\n"),
             "design_method": method, "priority": prio,
             "split_flag": False, "split_reason": "", "dr15_exposed": "no",
             "screen_pending": "no"}
        d.update(kw)
        return d

    tcs = []

    # ── D 型 ──────────────────────────────────────────────────────
    # 觸發＝使用者按壓（條文之 `the customer selects to change the state`）；
    # 標的＝匯流排上之送出。`HSW_RQ_TGW` 為 **DR-15 之 token 級標的**，
    # 依 R-VS71 照寫、標 `dr_dependent = DR-15` ＋ `dr15_exposed = yes`。
    tcs.append(base(
        "SWE1-VC-HeatedSteeringWheel-012", "Heated Steering Wheel",
        "Heated steering wheel press sends the request signal",
        "Press sends the on-change request",
        [f"1. Send CAN: {HSW2} = 0 ({HSW2_LAB[0]})",
         "2. Press the heated steering wheel icon on the Heated / Vented Seats screen",
         f"3. Read the CAN-B trace and check that {HSW_TLM} = 1 (Pressed) is transmitted"],
        [f"1. {HSW2} = 0 ({HSW2_LAB[0]}) is sent",
         "2. The heated steering wheel icon registers the press",
         f"3. {HSW_TLM} = 1 (Pressed) is sent"],
        "功能測試 (Functional based ; no specific technique)",
        pre="\n".join(["1. The vehicle is equipped with a heated steering wheel",
                       "2. The Heated / Vented Seats screen is displayed",
                       "3. CAN-B is connected to the bus simulator with signal tracing enabled"]),
        reasoning=("P1：主要功能邏輯；**D 型之觸發為使用者按壓**（條文 `the customer "
                   "selects to change the state`），與 A 型之 `IF <狀態值> THEN` 不同。"
                   "`HSW_RQ_TGW` 為 DR-15 之 token 級標的，依 R-VS71 照寫；"
                   "其時限 `<Tsend>` 依 42 包之處置以 remarks 標 BLOCKED"),
        dr_dependent="DR-15", dr15_exposed="yes",
        remarks=("BLOCKED: DR-15 —— 請求訊號之編碼待覆；"
                 "BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆，ER 只寫可觀察終態"),
        distinguishing_axis={"axis": "trigger",
                             "delta": "本列之觸發為按壓、標的為送出（D 型）；"
                                      "E 型之觸發為收到狀態訊號、標的為顯示變更。"}))
    tcs.append(base(
        "SWE1-VC-HeatedSteeringWheel-014", "Heated Steering Wheel",
        "Heated steering wheel request depends on current status",
        "Request value follows the current status",
        [f"1. Send CAN: {HSW2} = 3 ({HSW2_LAB[3]})",
         "2. Press the heated steering wheel icon on the Heated / Vented Seats screen",
         f"3. Read the CAN-B trace and check that {HSW_TLM} = 1 (Pressed) is transmitted"],
        [f"1. {HSW2} = 3 ({HSW2_LAB[3]}) is sent",
         "2. The heated steering wheel icon registers the press",
         f"3. {HSW_TLM} = 1 (Pressed) is sent"],
        "決策表 (Decision Table Testing)",
        pre="\n".join(["1. The vehicle is equipped with a heated steering wheel",
                       "2. The Heated / Vented Seats screen is displayed",
                       "3. CAN-B is connected to the bus simulator with signal tracing enabled"]),
        reasoning=("P1：主要功能邏輯；本條文之表（`Current status … Signal to be sent`）"
                   "為真值表，**其送出值依當前狀態而異** —— 本條驗 High 一列，"
                   "餘列依 §8.2.2 各自為一條（W-147 之預估已計）。"
                   "`HSW_RQ_TGW` 為 DR-15 標的，依 R-VS71 照寫"),
        dr_dependent="DR-15", dr15_exposed="yes",
        remarks="BLOCKED: DR-15 —— 請求訊號之編碼待覆，其逐狀態之送出值待覆後補",
        distinguishing_axis={"axis": "mode",
                             "delta": "本列之當前狀態為 high；`-012` 為 off。"}))

    # ── E 型 ──────────────────────────────────────────────────────
    # 觸發＝收到狀態訊號；標的＝顯示之變更。畫面層依 R-VS59(4) 之最弱斷言。
    for leaf, raw in (("SWE1-VC-HeatedSteeringWheel-017", 0),
                      ("SWE1-VC-HeatedSteeringWheel-018", 3)):
        other = 3 if raw == 0 else 0
        tcs.append(base(
            leaf, "Heated Steering Wheel",
            f"Heated steering wheel display follows status {HSW2_LAB[raw].rsplit('_', 1)[-1]}",
            f"Status transition to {HSW2_LAB[raw].rsplit('_', 1)[-1]}",
            [f"1. Send CAN: {HSW2} = {other} ({HSW2_LAB[other]}) and record the heated "
             f"steering wheel display state as HSW_display_before",
             f"2. Send CAN: {HSW2} = {raw} ({HSW2_LAB[raw]})",
             "3. Read the displayed state of the heated steering wheel and check that it "
             "changes from HSW_display_before"],
            [f"1. {HSW2} = {other} ({HSW2_LAB[other]}) is sent；HSW_display_before is recorded",
             f"2. {HSW2} = {raw} ({HSW2_LAB[raw]}) is sent",
             "3. The heated steering wheel display changes from HSW_display_before"],
            "狀態轉換 (State Transition Testing)",
            pre="\n".join(["1. The vehicle is equipped with a heated steering wheel",
                           "2. The Heated / Vented Seats screen is displayed",
                           "3. CAN-B is connected to the bus simulator"]),
            reasoning=("P1：主要功能邏輯；**E 型之觸發為收到狀態訊號**（條文 "
                       "`When the HU receives a … signal`），標的為**顯示之變更** ——"
                       "與 D 型之送出、A 型之命令皆不同。"
                       "其具體樣式待 TLM HMI Document，依 R-VS59(4) 寫最弱斷言"),
            dr_dependent="", screen_pending="yes",
            remarks=("BLOCKED: DR-5-B —— 變更後之顯示樣式待 TLM HMI Document；"
                     "BLOCKED: DR-24′ —— `<Tdisplay>` 之上限值待覆"),
            distinguishing_axis={"axis": "level",
                                 "delta": f"本列之目標狀態為 {HSW2_LAB[raw]}。"}))

    # ── F 型 ──────────────────────────────────────────────────────
    # 觸發＝兩個配置參數之組合；標的＝功能與其入口之啟用。
    for leaf, veh_raw, veh_lab in (("SWE1-VC-FeaturesEnableCriteria-021", 101, "WL (65 Hex)"),
                                   ("SWE1-VC-FeaturesEnableCriteria-022", 98, "553/M4 (62 Hex)")):
        tcs.append(base(
            leaf, "Common Features",
            f"Hybrid pages enabled for {veh_lab.split(' ')[0]} plug-in hybrid",
            "Two configuration parameters combined",
            [f"1. Set PROXI VC_VEH_LINE = {veh_raw} ({veh_lab})",
             "2. Set PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle)",
             "3. Power cycle the HU and check that the Hybrid Electric Pages access "
             "button is displayed"],
            [f"1. PROXI VC_VEH_LINE = {veh_raw} ({veh_lab}) is accepted",
             "2. PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle) is accepted",
             "3. The Hybrid Electric Pages access button is displayed"],
            "決策表 (Decision Table Testing)",
            pre="\n".join(["1. The vehicle is a plug-in hybrid",
                           "2. The HU is in the Full-Operation state"]),
            reasoning=("P1：主要功能邏輯；**F 型之觸發為兩個配置參數之組合**"
                       "（`if $VC_VEH_LINE$ = […] and $Hybrid_Type$ = […]`），"
                       "非訊號注入 —— 其步驟為 PROXI 設定 ＋ 電源循環。"
                       "`VC_VEH_LINE` 之值依 **R-VS62′** 取 PROXI 表列 466；"
                       "`Hybrid_Type` 取 LID `Atlantis(&High)` 欄組"),
            dr_dependent="", distinguishing_axis={
                "axis": "configuration",
                "delta": f"本列之車型碼為 {veh_lab}。"}))
    return {"batch": "batch21_probe", "feature": "vehicle_setting",
            "test_group": "Vehicle Setting", "generated_round": 51,
            "handoff": "docs/handoff/78_fullwrite_review.md",
            "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
            "selection": "W-146：D／E／F 三型各 2 條之**樣板抽驗**，共 6 條。"
                         "其 procedure 之觸發與 ER 之標的逐條自條文取，**不套 A 型樣板**。"
                         "通過 §9 自檢 ＋ 固定錨點 ＋ 分析層抽驗者，其型方得放量。",
            "signal_notation": "R-VS52 ＋ R-VS61 ＋ R-VS67′",
            "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
            "revision": "W-146（51 輪）：batch21_probe 首版",
            "tcs": tcs}


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch21_probe.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch21_probe：{len(d['tcs'])} 條")
    for t in d["tcs"]:
        print(f"  {t['priority']} {t['leaf_id']:44s} {t['tc_title']}")
