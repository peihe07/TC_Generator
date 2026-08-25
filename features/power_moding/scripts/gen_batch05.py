#!/usr/bin/env python3
"""batch 5 —— `Power Off Behavior`(8 leaf) ＋ `Off Road Plus`(2 leaf)（36 包步驟 7）。

**四項拘束**（36 包 §四步驟 7）：
  (a) `source_clause` 取自 **PDF**，`origin` = `spec_pdf p{n}`（R-PMH50）；
  (b) 產出後即跑涵蓋表（正向＋反向），不待下一輪；
  (c) 限定依 R-PMH94／R-PMH97／R-PMH101 逐斷言導出，
      **依 R-PMH126 逐條具名其所對之該一個 ER，不得樣板**；
  (d) **`-021` 之 PC 須含 `Gear != Reverse`**（R-PMH80(a)）——
      矩陣 `r48c10` 逐字 `Popup not displayed over RVC` 與 `PITA6` 取相反值。

**`tc_id` 續為 provisional**；**零寫回工作簿**。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
EP = "等價劃分 (Equivalence Partitioning, EP)"

POB, ORP = "Power Off Behavior", "Off Road Plus"

# --- R-PMH50：逐字取自 PDF ---
PDF = {
 "PITA4": ("PITA4: Screen Off and HU Power button selections shall be ignored while backup "
           "cam is being shown."),
 "PITA5": ("PITA5: If backup cam needs to be shown during Power Button OFF state, then it "
           "shall be shown. This shall not cancel Power Button Off state. Once the backup cam "
           "is dismissed, the Power Button Off state shall be reinstated."),
 "PITA6": ("PITA6: HVAC pop-ups shall be temporarily displayed during Power Button Off state. "
           "Any interactions with the popups shall not cancel Power Button Off state."),
 "PITA6_1": ("PITA6.1: If radio is in Power Button Off state upon going from ignition in OFF "
             "position to ignition in ACC or RUN, HVAC popups shall display on the screen."),
 "PITA9_a": "PITA9: Phone call popups can be displayed over Power Button Off state.",
 "PITA9_b": "Ignoring a Phone call popup returns to the Power Button Off state.",
 "PITA9_c": ("If a call is answered either by soft control or hard control and the user does "
             "not change screens during the phone call, the head unit will return to Power Off "
             "State upon the call ending."),
 "PITA10": "PITA10: SOS and ASSIST can turn head unit power back on.",
 "OFF1": ("OFF1.) If vehicle is in Off Road state prior to pressing Off Road+ hard control "
          "head unit will not initiate wake up (Power Button On)."),
 "OFF3": "OFF3.)Head unit is muted when launching app from Power Off State.",
}

# --- 事件層限定（R-PMH126：逐條具名其所對之 ER）---
MUTE = "Do not press the Mute key"


def r126(er_ref: str, why: str) -> str:
    return ("⚠ **事件層限定（R-PMH55(c)／R-PMH126）** —— 其所對之斷言為 "
            f"**{er_ref}**：{why}，而二者之條件**未證互斥**（R-PMH84）。"
            "**其為測試員之動作，故置於 procedure**（canon §4.5）。")


TCS = [
 dict(leaf="SWE1-HMI-PM-019", outline="10.1", ts=POB, src="PITA4", dm=EP, pri="P1",
   title="Screen Off and power button selections are ignored during the backup camera",
   item="(等價類：倒車影像顯示中之被忽略輸入 —— 二鍵同結果，故為一類)",
   pre=["The backup camera is being shown on the screen",
        "The head unit is on"],
   proc=["Press the Screen Off hard key and read the screen",
         "Press the HU Power button and read the screen",
         "Check that neither selection changed the screen"],
   er=["The screen still shows the backup camera after the Screen Off key press",
       "The screen still shows the backup camera after the HU Power button press",
       "Neither selection had any effect"],
   reason=("**P1 —— 主要功能邏輯**：其失效使倒車中畫面被關閉，為行車安全相關之顯示中斷。"
     "**設計方法 EP** —— `Screen Off` 與 `HU Power button` 為**同一等價類之兩個成員**"
     "（規格以 `and` 並列而給同一結果 `shall be ignored`），**非兩個獨立分支**，"
     "故不依 §8.2.2 拆分。**其與 batch 4 之「門被移除」條（`ACC, RUN, or START` 三值一條）同一處置** ——**此處不以 tc_id 指涉**（R-PMH53 之檢查只認同軸之批內指涉，34 包 §6.3 已具名該限度）。"
     "⚠ **§8.2.2 之壓力測試於此不觸發之理由須具名**：二鍵之預期結果**完全相同**"
     "（皆為「無效果」），**其任一失效之診斷由 ER1／ER2 分別承載**，"
     "故 pass/fail 之歸因仍明確。"
     "⚠ **本條不斷言倒車影像之顯示條件** —— 其屬本批之倒車影像顯示條與矩陣 `r42` 之射程（§8.5）。"),
   axis="等價類：倒車影像中之被忽略輸入（對 -039 之倒車影像顯示本身）"),

 dict(leaf="SWE1-HMI-PM-020", outline="10.2", ts=POB, src="PITA5", dm=STATE, pri="P1",
   title="Backup camera shows during Power Button Off without cancelling that state",
   item="(同一觸發之三個連續後果 —— 顯示、不取消、解除後回復)",
   pre=["The radio is in Power Button Off state",
        "The vehicle is able to request the backup camera"],
   proc=["Put the vehicle into reverse so that the backup camera is requested",
         "Read the screen and record the power state",
         "Dismiss the backup camera and read the power state",
         "Check that the Power Button Off state was reinstated"],
   er=["The backup camera is shown",
       "The radio remains in Power Button Off state while the camera is shown",
       "The backup camera is dismissed",
       "The Power Button Off state is reinstated"],
   reason=("**P1 —— 主要功能邏輯**：其失效使關機狀態被倒車影像取消，使用者需再關一次。"
     "設計方法 STATE —— 標的為 Power Button Off 狀態於倒車影像期間之維持與其回復。"
     "⚠ **三個後果不拆之依據（canon §5.7）** —— `shown`／`shall not cancel`／`reinstated` "
     "為**同一觸發（倒車影像被請求）之連續後果**，屬一條時序鏈；"
     "**§8.2.2 於此不觸發**（其所禁者為獨立分支）。"
     "⚠ **本條不斷言倒車影像之內容或其請求條件** —— 規格只言 `needs to be shown`（§8.4.1）。"),
   axis="謂詞：倒車影像期間之電源狀態（對 -038 之輸入被忽略）"),

 dict(leaf="SWE1-HMI-PM-021", outline="10.3", ts=POB, src="PITA6", dm=STATE, pri="P1",
   title="HVAC pop-ups display temporarily during Power Button Off state",
   item="(HVAC popup 於關機狀態之暫時顯示 —— 其互動不取消該狀態)",
   pre=["The radio is in Power Button Off state",
        "The vehicle gear is not in Reverse",
        "The HVAC hard controls are available"],
   proc=["Adjust an HVAC hard control and read the screen",
         "Interact with the pop-up shown and read the power state",
         "Check that the Power Button Off state was not cancelled"],
   er=["An HVAC pop-up is displayed temporarily",
       "The radio remains in Power Button Off state after the interaction",
       "The Power Button Off state is not cancelled"],
   reason=("**P1 —— 主要功能邏輯**：其失效使 HVAC 操作意外開機。設計方法 STATE。"
     "⚠ **R-PMH80(a) 之 pre_condition `The vehicle gear is not in Reverse`（本條必備）** —— "
     "State Matrix `r48c10`（`Key On, Gear = Reverse`／`Power Button State = OFF`）逐字為 "
     "`Popup not displayed over RVC`，與本條 ER1 之「HVAC popup 顯示」**同謂詞取相反值**；"
     "**該牴觸為 20 包所查出、R-PMH80 所處置者**（`10.3` × `r48c10`）。"
     "**其為狀態而非動作，故置於 pre_condition**（canon §4.4；對照 R-PMH113 之同一原則）。"
     "⚠ **連帶之覆蓋缺口**：**倒車情境下 HVAC popup 之行為本條不驗**，"
     "其已由 R-PMH80(b) 登記並入 `DR-PMH6` Q1。"
     "⚠ **二個後果不拆之依據（canon §5.7）** —— `shall be temporarily displayed` 與 "
     "`Any interactions ... shall not cancel Power Button Off state` 為**同一觸發"
     "（HVAC 硬控之操作）之連續後果**，屬一條時序鏈：**popup 未顯示則其互動無從發生**。"
     "**§8.2.2 之壓力測試於此不觸發** —— 該條所禁者為**兩個獨立分支**之部分失效落在同一判定上；"
     "**本處後者以前者為前提，非獨立**。"
     "⚠ **`temporarily` 之時長規格未給**（§8.4.1 不造值），ER1 只斷言其為暫時顯示而不給秒數。"),
   axis="謂詞：HVAC popup 於關機狀態（對 -041 之點火轉換觸發）"),

 dict(leaf="SWE1-HMI-PM-022-01", outline="10.4", ts=POB, src="PITA6_1", dm=STATE, pri="P1",
   title="HVAC pop-ups display when the ignition moves from off to ACC or RUN",
   item="(點火自 OFF 轉 ACC/RUN 之觸發 —— 與 -040 之 HVAC 操作觸發為不同觸發)",
   pre=["The radio is in Power Button Off state",
        "The ignition is in the OFF position"],
   proc=["Turn the ignition from OFF to ACC or RUN",
         "Check that the HVAC pop-ups are displayed on the screen"],
   er=["The ignition moves from OFF to ACC or RUN",
       "The HVAC pop-ups are displayed on the screen"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE —— 標的為點火轉換所引發之顯示。"
     "⚠ **與 `-040` 之區別為觸發**（profile §4）：`-040` 之觸發為 HVAC 硬控之操作，"
     "本條之觸發為**點火位置之轉換**；**二者之後果同為 HVAC popup 顯示**。"
     "⚠ **`ACC or RUN` 二值為同一等價類**（規格以 `or` 並列而給同一結果），"
     "步驟 1 涵蓋二者而不拆（同本批被忽略輸入條之等價類處置 —— **跨軸故不以 tc_id 指涉**）。"
     "⚠ **本條之 `source_clause` 只取 `PITA6.1` 之第一句** —— 其第二句"
     "（`Upon pressing power button to On state disclaimer screen shall be displayed …`）"
     "屬 leaf `SWE1-HMI-PM-022-02` 之射程（其由 batch 1 之免責畫面顯示條承載），依 R-PMH122 不併入本條之追溯欄。"),
   axis="觸發：點火自 OFF 轉 ACC/RUN（對 -040 之 HVAC 硬控操作）"),

 dict(leaf="SWE1-HMI-PM-024-01", outline="10.6", ts=POB, src="PITA9_a", dm=FUNC, pri="P1",
   title="Phone call pop-ups can be displayed over Power Button Off state",
   item="(來電 popup 之顯示 —— 與 -043 之忽略、-044 之通話結束為三個不同事件)",
   pre=["The radio is in Power Button Off state",
        "A phone is paired and able to receive a call"],
   proc=["Place an incoming call to the paired phone",
         "Check that the phone call pop-up is displayed over the Power Button Off state"],
   er=["An incoming call arrives at the paired phone",
       "The phone call pop-up is displayed over the Power Button Off state"],
   reason=("**P1 —— 主要功能邏輯**：其失效使使用者於關機狀態下看不到來電。設計方法 FUNC。"
"⚠ **許可式之處置（R-PMH140）** —— 具名三事："
     "(a) **其來源為許可式** —— `source_clause` 逐字用 `can`，其保證該行為之**容許**，"
     "不保證其**必然發生**；"
     "(b) **本 TC 所驗者為「於本條所述之條件下該行為確實可發生」**，非其於任何情形皆發生；"
     "(c) **其不發生不必然為缺陷** —— **判 fail 前須先確認本條之 pre_condition 確已成立**。"
     "**不另開 DR**（R-PMH140）—— 許可式為規格之常見書寫，非未定義之記法，與 A-PMH22 不同類。"
     "⚠ **037 之 DESC 亦為許可式** —— 其逐字為 `The system **may** display phone call popups`。"),
   axis="事件：來電 popup 之顯示（對 -043 之忽略、-044 之通話結束）"),

 dict(leaf="SWE1-HMI-PM-024-02", outline="10.6", ts=POB, src="PITA9_b", dm=STATE, pri="P1",
   title="Ignoring a phone call pop-up returns to Power Button Off state",
   item="(忽略路徑 —— 與 -044 之接聽後通話結束路徑成對)",
   pre=["The radio is in Power Button Off state",
        "A phone call pop-up is displayed over that state"],
   proc=["Ignore the phone call pop-up",
         "Check that the radio returned to Power Button Off state"],
   er=["The phone call pop-up is ignored",
       "The radio returns to Power Button Off state"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE。"
     "⚠ **與 `-044` 拆分之依據（profile §4）**：本條之事件為**忽略**，"
     "`-044` 之事件為**接聽後通話結束**；**二者為不同事件而非同一事件之兩個後果**。"),
   axis="事件：忽略來電 popup（對 -044 之接聽後通話結束）"),

 dict(leaf="SWE1-HMI-PM-024-03", outline="10.6", ts=POB, src="PITA9_c", dm=STATE, pri="P1",
   title="Answered call returns to Power Off state when it ends without screen change",
   item="(接聽後通話結束路徑 —— 與 -043 之忽略路徑成對)",
   pre=["The radio is in Power Button Off state",
        "A phone call pop-up is displayed over that state"],
   proc=["Answer the call by soft control and do not change screens",
         "End the call and read the power state",
         "Check that the head unit returned to Power Off state"],
   er=["The call is answered and no screen is changed during the call",
       "The call ends",
       "The head unit returns to Power Off state"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE。"
     "⚠ **`either by soft control or hard control` 為同一等價類之二成員**，"
     "步驟 1 取 soft control 一者；**hard control 一者本條未驗，據實記載為限度**"
     "（其結果依規格為同一，故不另立條 —— 同本批被忽略輸入條之等價類處置）。"
     "⚠ **該「同結果故不拆」為推定，須具名（37 包 §3.3）** —— "
     "**規格未言 soft control 與 hard control 之接聽為同一實作路徑**；"
     "其只給同一結果。**`hard control` 一路因而無 TC 覆蓋，登記為覆蓋缺口**（A-PMH31）。"
     "**不補條**（37 包明令）—— 補之即為對同一結果之重複驗證（canon §8.2.1）。"
     "⚠ **`does not change screens` 為條件而非斷言** —— 其置於步驟 1 之措詞與 ER1，"
     "**本條不驗「改變畫面時之行為」**（規格未言之，§8.4.1）。"),
   axis="事件：接聽後通話結束（對 -043 之忽略）"),

 dict(leaf="SWE1-HMI-PM-025", outline="10.7", ts=POB, src="PITA10", dm=EP, pri="P0",
   title="SOS and ASSIST can turn the head unit power back on",
   item="(等價類：可使電源回復之二個呼叫鍵 —— 二者同結果，故為一類)",
   pre=["The head unit power is off",
        "The SOS and ASSIST controls are available in the vehicle"],
   proc=["Press the SOS control and read the head unit power state",
         "Return the head unit to power off and press the ASSIST control",
         "Check that each control turned the head unit power back on"],
   er=["The head unit power turns back on after the SOS control is pressed",
       "The head unit power turns back on after the ASSIST control is pressed",
       "Both controls turn the head unit power back on"],
   reason=("**P0 —— 其為緊急呼叫之電源回復路徑**：SOS／ASSIST 於事故時須能喚醒主機，"
     "**其失效直接影響求救**。"
     "**其判 P0 之依據為 canon §10.2 之 `safety`／`eCall` 明列**（37 包 §3.1）。"
     "⚠ **本條非本批亦非本 feature 唯一之 P0** —— 實測全六批 P0 共 **4 條**"
     "（batch 1 之三條免責畫面相關者 ＋ 本條；**跨批故不以 tc_id 指涉**，R-PMH53 之限度見 34 包 §6.3）。**其依據各異而互不矛盾**（R-PMH59）："
     "前三者為開機序列之阻斷（使用者無法離開免責畫面即無法用車），本條為緊急呼叫之電源回復。"
     "⚠ **前一版之軸註曾寫「本批唯一之 P0」而其 priority 欄填 P1** —— 該矛盾為 37 包 §3.1 所指；"
     "**修正時我又寫成「本 feature 唯一之 P0」而實測為 4 條，於此一併更正**。"
     "**修正時我又寫成「本 feature 唯一之 P0」而實測為 4 條，於此一併更正**。"
     "其依據與其餘各條之 P1（功能邏輯失效而不阻斷安全）**不同級而不矛盾**（R-PMH59）。"
     "**設計方法 EP** —— `SOS` 與 `ASSIST` 為同一等價類之二成員（規格以 `and` 並列而給同一結果），"
     "同本批被忽略輸入條之等價類處置。"
     "⚠ **許可式之處置（R-PMH140）** —— 具名三事："
     "(a) **其來源為許可式** —— `source_clause` 逐字用 `can`，其保證該行為之**容許**，"
     "不保證其**必然發生**；"
     "(b) **本 TC 所驗者為「於本條所述之條件下該行為確實可發生」**，非其於任何情形皆發生；"
     "(c) **其不發生不必然為缺陷** —— **判 fail 前須先確認本條之 pre_condition 確已成立**。"
     "**不另開 DR**（R-PMH140）—— 許可式為規格之常見書寫，非未定義之記法，與 A-PMH22 不同類。"),
   axis="等價類：緊急呼叫鍵之電源回復（P0：canon §10.2 之 eCall）"),

 dict(leaf="SWE1-HMI-PM-027", outline="12.1", ts=ORP, src="OFF1", dm=STATE, pri="P1",
   title="Off Road Plus press does not wake the head unit when already in Off Road",
   item="(Off Road 狀態下按 Off Road+ —— 其不引發喚醒)",
   pre=["The vehicle is in Off Road state",
        "The head unit is in Power Button Off state"],
   proc=["Press the Off Road Plus hard control",
         "Check that the head unit did not initiate wake up"],
   er=["The Off Road Plus hard control is pressed",
       "The head unit does not initiate wake up and stays in Power Button Off state"],
   reason=("**P1 —— 主要功能邏輯**：其失效使車輛於越野狀態下主機意外開機。設計方法 STATE。"
     "⚠ **`prior to pressing` 之時序為 pre_condition 之依據** —— "
     "「按下之前已在 Off Road state」為**狀態**（canon §4.4），故置於 pre_condition 1。"
     "⚠ **leaf `SWE1-HMI-PM-028`（12.2）已依 R-PMH72 撤除**（其行為委於 CFTS009），"
     "故本組僅 `12.1` 與 `12.3` 二 leaf。"),
   axis="事件：Off Road 狀態下之 Off Road+ 按壓（對 -047 之 app 啟動）"),

 dict(leaf="SWE1-HMI-PM-029", outline="12.3", ts=ORP, src="OFF3", dm=FUNC, pri="P1",
   title="Head unit is muted when an app is launched from Power Off state",
   lim=("ER3 `The head unit is muted`",
        "State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Inactive` **使靜音被解除**，"
        "與本 ER 之「已靜音」**同謂詞取相反值**"),
   item="(自關機狀態啟動 app —— 其結果為主機靜音)",
   pre=["The head unit is in Power Off state",
        "An app that can be launched from that state is available"],
   proc=["Launch the app from Power Off state",
         "Read the head unit audio state",
         "Check that the head unit is muted"],
   er=["The app is launched from Power Off state",
       "The head unit audio state is recorded",
       "The head unit is muted"],
   reason=("**P1 —— 主要功能邏輯**：其失效使自關機啟動 app 時突然出聲。設計方法 FUNC。"
     "⚠ **`launching app` 未指明為哪一個 app**（§8.4.1 不造值）—— "
     "pre_condition 2 只寫「可自該狀態啟動之 app」而不指名。"),
   axis="事件：自關機狀態啟動 app（對 -046 之 Off Road+ 按壓）"),
]

BASE = 37        # batch 1–4 用 001–037（`-024` 位次空出），本批續 038 起


def norm_item(s: str) -> str:
    s = s.replace("‘", "'").replace("’", "'")
    return re.sub(r"\s*\[CR\d+\]", "", s)


def main() -> None:
    out = []
    for n, t in enumerate(TCS, BASE + 1):
        proc, er = list(t["proc"]), list(t["er"])
        if t.get("lim"):
            proc.insert(0, MUTE)
            er.insert(0, "No Mute key press occurs")
        out.append({
            "tc_id": f"NR1L-DisclaimerScreen-{n:03d}",
            "leaf_id": t["leaf"],
            "test_group": "Disclaimer screen",
            "test_set": t["ts"],
            "tc_title": t["title"],
            "test_item": norm_item(f"{PDF[t['src']]}\n\n{t['item']}"),
            "pre_conditions": "\n".join(f"{i}. {x}" for i, x in enumerate(t["pre"], 1)),
            "input_test_data": "NA",
            "test_procedure": "\n".join(f"{i}. {x}" for i, x in enumerate(proc, 1)),
            "expected_result": "\n".join(f"{i}. {x}" for i, x in enumerate(er, 1)),
            "specification_reference": f"{SPEC}_{t['outline']}",
            "design_method": t["dm"],
            "priority": t["pri"],
            "functional_safety": "NA",
            "estimated_test_time": "",
            "vehicle_models": "",
            "remarks": f"Test Set: {t['ts']}",
            "reasoning": t["reason"] + (r126(*t["lim"]) if t.get("lim") else ""),
            "distinguishing_axis": t["axis"],
            "source_clause": PDF[t["src"]],
            "source_clause_origin": "spec_pdf p10" if t["outline"].startswith("10") else "spec_pdf p11",
        })
    doc = {
        "batch": "batch05",
        "feature": "power_moding",
        "test_group": "Disclaimer screen",
        "test_sets": sorted({t["ts"] for t in TCS}),
        "handoff": "docs/handoff/36_batch5.md",
        "profile": "docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md",
        "selection": ("Test Set `Power Off Behavior`(8 leaf) ＋ `Off Road Plus`(2 leaf)，"
                      "共 **10 leaf**（R-PMH120 之收尾計畫第二批）。**10 條 TC** —— "
                      "本批無一 leaf 須拆（其多值處皆為同一等價類之成員，非獨立分支）。"),
        "tc_id_status": "provisional",
        "leaf_scope": sorted({t["leaf"] for t in TCS}),
        "source_clause_basis": "R-PMH50 —— 取自 spec_pdf p10／p11（R-PMH75 之反轉只及於 9.1）。",
        "write_back": "凍結 —— 本批只產出 JSON，不寫回工作簿",
        "limits": {f"NR1L-DisclaimerScreen-{BASE + 1 + i:03d}": [MUTE]
                   for i, x in enumerate(TCS) if x.get("lim")},
        "tcs": out,
    }
    p = ROOT / "generated" / "batch05.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(out)} TC（自 {len(doc['leaf_scope'])} leaf，"
          f"{len(doc['test_sets'])} 個 Test Set）")


if __name__ == "__main__":
    main()
