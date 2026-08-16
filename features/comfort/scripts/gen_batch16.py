#!/usr/bin/env python3
"""Batch 16 generator — R-C42 unblock (handoff 64 §1).

Not a Test Set. These are leaves that were stopped in earlier batches for one
reason only — "the configuration axis is not registered" — which R-C42 now
rules is not a reason to stop: a clause that carries its own applicability
condition satisfies R-C28 Q1 by itself, and whether that condition is ever
registered as a profile axis is a separate question about cross-TC
consistency.

Each TC below keeps the Test Set of the section it belongs to, so the
workbook's grouping is unchanged; only the generator that owns the file is
new. The two leaves whose sections already have a doc (17.2's 125-08 and
17.3's 126-02) are NOT here — they are un-withheld inside gen_batch8.py,
which owns those files, with explicit late tc_ids so nothing renumbers.

19 leaves, tc_id -363 … -381:

    2.3.1  004-01/-02      dual AUTO           (C2.1  "Some vehicles …")
    2.5.1  007-01/-02      3-state recirc      (C4.1  "Some vehicles …")
    9.2    040-01/-02      alt fan pop-up      (CR11  "On some vehicles …")
    9.3    041             pop-up labels       (CR11 back-reference)
    9.4    042-01/-02/-03  status-bar shortcut (CR11 back-reference)
    9.4.1  043             button label        (CR11 back-reference)
    14.12  096-01/-02/-03  pop-up style        (HVACP12 "If the hard controls …")
    14.14  098             centric pop-ups     (HVACP14 "For vehicles with …")
    17.4   127-01/-02      25% widget toggle   (CW3  "For 8.4/10.1/12 …")
    17.5   128-01/-02      dual airflow widget (CW4  "For dual zone …")

Each section's own qualifying sentence is quoted verbatim as the leading
pre_condition and marked `spec-verbatim`; the "待軸化候選" list is kept in
profile §3.2 so R-C42 三's gate can find conditions used in ≥2 sections.

Usage:
    python3 features/comfort/scripts/gen_batch16.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 363

DM_F = "功能測試 (Functional based ; no specific technique)"
DM_S = "狀態轉換 (State Transition Testing)"

EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")

# --- the clause-local trigger conditions R-C42 unblocks, quoted verbatim ----
PC_DUAL_AUTO = ("1. [spec-verbatim] The vehicle has dual zone climate with "
                "dual airflow mode and a configuration for dual AUTO modes, "
                "one for the driver side and passenger side (2.3.1)")
PC_RECIRC3 = ("1. [spec-verbatim] The vehicle has a configuration for a 3 "
              "state toggle recirc button: Auto, Manual, Open (2.5.1)")
PC_CH9 = ("1. [spec-verbatim] The vehicle is one of the vehicles that have "
          "additional Rear Climate controls and shortcuts (9.1)")
# 65 §2 — quoted verbatim. The earlier wording said "the hard controls FOR
# THIS FUNCTION", which quietly picked one reading of HVACP12 — the per-control
# one — and that reading is precisely what DR #37 is still asking. §8.4.1: an
# ambiguous source keeps its ambiguity. Wording it away answers for upstream.
PC_KNOB = ("1. [spec-verbatim] If the hard controls are knobs that turn "
           "(14.12)")
PC_TOGGLE = ("1. [spec-verbatim] If the hard controls are UP/DOWN toggles "
             "(14.12)")
PC_CENTRIC = ("1. [spec-verbatim] The vehicle has a dual zone climate version "
              "with dual airflow modes on an 8.4\", 10.1\" Landscape, 10.25\" "
              "or 12.3\" radio (14.14)")
PC_LANDSCAPE = ("1. [spec-verbatim] The vehicle has an 8.4/10.1/12 landscaped "
                "screen (17.4)")
PC_DUAL_WIDGET = ("1. [spec-verbatim] The vehicle is a dual zone climate with "
                  "dual airflow modes equipped vehicle (17.5)")
PC_WIDGET = "2. [test-setup] The Comfort widget is shown on the home screen"

# 66 §3 — the ambiguity must reach the person who executes, not only the
# person who reviews. reasoning's reader is the reviewer; Remarks' reader is
# the tester, and the tester is the one who walks into it. No internal id and
# no DR number (profile §3.6 keeps Remarks externally visible).
# 68 §2 — one sentence per row, each naming what THIS row cannot decide.
# The shared wording was reconcilable only as "did someone write that
# sentence", not as "is what was written about this row". A register whose
# values repeat verifies the presence of text, not its aboutness.
_COLLECTIVE = ("The clause refers to the hard controls collectively. On "
               "vehicles whose hard controls are of mixed types, ")
REMARKS_1412 = {
    "096-01": _COLLECTIVE + ("whether radial popups apply cannot be "
                             "determined from the Comfort HMI specification "
                             "alone."),
    "096-02": _COLLECTIVE + ("whether vertical popups apply cannot be "
                             "determined from the Comfort HMI specification "
                             "alone."),
    "096-03": _COLLECTIVE + ("whether the popup style must match every "
                             "control or only the predominant control type "
                             "cannot be determined from the Comfort HMI "
                             "specification alone."),
}
LEAF_REMARKS = REMARKS_1412

SECTIONS = {
 "2.3.1": dict(parent="SWE1-HVAC-004", test_set="Climate Modes",
               pc=PC_DUAL_AUTO, refs=("2.3",), lower=True),
 "2.5.1": dict(parent="SWE1-HVAC-007", test_set="Climate Modes",
               pc=PC_RECIRC3, refs=("2.5",), lower=True),
 "9.2": dict(parent="SWE1-HVAC-040", test_set="Rear Climate",
             pc=PC_CH9, refs=("9.1",), lower=True),
 "9.3": dict(parent="SWE1-HVAC-041", test_set="Rear Climate",
             pc=PC_CH9, refs=("9.1", "9.2"), lower=True),
 "9.4": dict(parent="SWE1-HVAC-042", test_set="Rear Climate",
             pc=PC_CH9, refs=("9.1",), lower=True),
 "9.4.1": dict(parent="SWE1-HVAC-043", test_set="Rear Climate",
               pc=PC_CH9, refs=("9.1", "9.4"), lower=True),
 "14.12": dict(parent="SWE1-HVAC-096", test_set="Climate Popups",
               pc=PC_KNOB, refs=(), lower=True),
 "14.14": dict(parent="SWE1-HVAC-098", test_set="Climate Popups",
               pc=PC_CENTRIC, refs=(), lower=True),
 "17.4": dict(parent="SWE1-HVAC-127", test_set="Home Screen Widget",
              pc=PC_LANDSCAPE, refs=("17.1",), lower=True),
 "17.5": dict(parent="SWE1-HVAC-128", test_set="Home Screen Widget",
              pc=PC_DUAL_WIDGET, refs=("17.1",), lower=True),
}
LEAF_PC = {"096-02": PC_TOGGLE, "096-03": PC_KNOB}
WIDGET_SECTIONS = {"17.4", "17.5"}

TCS = {
 "2.3.1": [
  ("004-01", "The vehicle offers a dual AUTO mode for each side",
   "The system shall provide dual AUTO modes, one for the driver side and one for the passenger side",
   ["1. Open the climate screen", "2. Read the AUTO controls"],
   ["1. The climate screen is displayed",
    "2. A driver side AUTO mode and a passenger side AUTO mode are provided"], "P1", DM_F),
  ("004-02", "The AUTO indicators are displayed separately for each side",
   "The system shall display the AUTO indicators separately for each side",
   ["1. Turn the driver side AUTO on", "2. Read the driver and passenger AUTO indicators"],
   ["1. The driver side AUTO is on",
    "2. The driver side AUTO indicator is shown as on and the passenger side AUTO indicator is shown separately"], "P1", DM_F)],
 "2.5.1": [
  ("007-01", "The recirc button cycles through its three states",
   "The system shall cycle RECIRC through three states: Auto, Manual and Open",
   ["1. Press the RECIRC button", "2. Press the RECIRC button again",
    "3. Press the RECIRC button again"],
   ["1. RECIRC is in the Auto state", "2. RECIRC is in the Manual state",
    "3. RECIRC is in the Open state"], "P1", DM_S),
  ("007-02", "The recirc state is indicated on the climate screen",
   "The system shall indicate the correct RECIRC state on the TS climate screen",
   ["1. Set RECIRC to Manual", "2. Read the RECIRC control on the climate screen"],
   ["1. RECIRC is in the Manual state",
    "2. The climate screen indicates the Manual state"], "P2", DM_F)],
 "9.2": [
  ("040-01", "The alternative fan pop-up shows front and rear fan status",
   "The system shall show the front fan speed status (level number, AUTO, OFF) and the Rear fan status (level number, AUTO, OFF) in the fan speed pop up",
   ["1. Trigger the fan speed pop up using the hard controls",
    "2. Read the pop up"],
   ["1. The fan speed pop up is displayed",
    "2. The pop up shows the front fan status and the rear fan status"], "P1", DM_F),
  ("040-02", "The fan pop-up areas navigate to the front and rear tabs",
   "The system shall on pressing the Front Fan area redirect the user to the Front climate tab, and on pressing the Rear fan area redirect the user to the Rear climate tab",
   ["1. Trigger the fan speed pop up and press the Front Fan area",
    "2. Trigger the fan speed pop up and press the Rear fan area"],
   ["1. The Front climate tab is displayed",
    "2. The Rear climate tab is displayed"], "P1", DM_F)],
 "9.3": [
  ("041", "The fan pop-up carries the Front and Rear labels",
   "The system shall show the text labels «Front» for front climate and «Rear» for Rear Climate in the pop up",
   ["1. Trigger the fan speed pop up using the hard controls",
    "2. Read the labels in the pop up"],
   ["1. The fan speed pop up is displayed",
    "2. The pop up shows the label «Front» for front climate and «Rear» for Rear Climate"], "P2", DM_F)],
 "9.4": [
  ("042-01", "The status bar dropdown toggles the rear climate on and off",
   "The system shall provide a Rear Climate button in the driver side climate dropdown menu that turns the Rear Climate OFF and On again",
   ["1. Open the driver side climate dropdown menu",
    "2. Press the Rear Climate button", "3. Press the Rear Climate button again"],
   ["1. The dropdown menu shows a Rear Climate button",
    "2. The Rear Climate is off", "3. The Rear Climate is on"], "P1", DM_S),
  ("042-02", "The rear climate tab reflects the shortcut change",
   "The system shall reflect the change in the Rear Climate Tab",
   ["1. Turn the Rear Climate off using the status bar dropdown button",
    "2. Open the Rear Climate tab"],
   ["1. The Rear Climate is off",
    "2. The Rear Climate tab shows the rear climate as off"], "P1", DM_F),
  ("042-03", "A highlighted shortcut button means the rear climate is on",
   "The system shall highlight the button when the Rear Climate is On",
   ["1. Turn the Rear Climate on", "2. Read the Rear Climate button in the dropdown menu"],
   ["1. The Rear Climate is on", "2. The Rear Climate button is highlighted"], "P2", DM_F)],
 "9.4.1": [
  ("043", "The rear climate shortcut button is labelled Rear",
   "The system shall label the button «Rear»",
   ["1. Open the driver side climate dropdown menu",
    "2. Read the Rear Climate button label"],
   ["1. The dropdown menu is displayed",
    "2. The button label reads «Rear»"], "P2", DM_F)],
 "14.12": [
  ("096-01", "Knob hard controls produce radial pop-ups",
   "The system shall show radial popups if the hard controls are knobs that turn",
   ["1. Operate the hard controls", "2. Read the HVAC popups"],
   ["1. The HVAC popups are displayed",
    "2. The HVAC popups are radial popups"], "P1", DM_F),
  ("096-02", "UP and DOWN toggle controls produce vertical pop-ups",
   "The system shall show vertical popups if the hard controls are UP/DOWN toggles",
   ["1. Operate the hard controls", "2. Read the HVAC popups"],
   ["1. The HVAC popups are displayed",
    "2. The HVAC popups are vertical popups"], "P1", DM_F),
  ("096-03", "The pop-up style mirrors the physical control action",
   "The system shall match the style of HVAC popups to the type of hard controls, mirroring the physical action of turning UP/DOWN",
   ["1. Operate the hard controls",
    "2. Read the style of the HVAC popups"],
   ["1. The HVAC popups are displayed",
    "2. The style of the HVAC popups matches the type of the hard controls and mirrors their physical action"], "P2", DM_F)],
 "14.14": [
  ("098", "Driver and passenger centric pop-ups are shown",
   "The system shall show driver and passenger centric popups for vehicles with dual zone climate versions with dual airflow modes on the listed radios",
   ["1. Trigger a climate popup from the driver side control",
    "2. Trigger a climate popup from the passenger side control"],
   ["1. A driver centric popup is displayed",
    "2. A passenger centric popup is displayed"], "P1", DM_F)],
 "17.4": [
  ("127-01", "The 25% widget toggles between Heat and Vent",
   "The system shall provide a toggle button on the 25% widget to switch between either Heat or Vent",
   ["1. Read the 25% Comfort widget", "2. Press the toggle button"],
   ["1. The 25% widget shows a toggle button",
    "2. The widget switches between Heat and Vent"], "P1", DM_S),
  ("127-02", "The toggle switches display and control between the two types",
   "The system shall toggle the display and control functionality between the two different Comfort control types",
   ["1. Press the toggle button on the 25% widget so that Heat is selected",
    "2. Press the toggle button again"],
   ["1. The widget displays and controls the Heat control type",
    "2. The widget displays and controls the Vent control type"], "P1", DM_F)],
 "17.5": [
  ("128-01", "The widget shows driver and passenger temperatures",
   "The system shall show driver and passenger temperature on the widget of dual zone climate with dual airflow modes equipped vehicles",
   ["1. Open the Comfort widget on the home screen",
    "2. Read the temperature area of the widget"],
   ["1. The Comfort widget is displayed",
    "2. The widget displays a driver temperature and a passenger temperature"], "P1", DM_F),
  ("128-02", "The widget shows two sets of airflow modes",
   "The system shall show two sets of airflow modes on the widget, one for the driver and one for the passenger",
   ["1. Read the Comfort widget", "2. Read the airflow mode controls on the widget"],
   ["1. The Comfort widget is displayed",
    "2. Two sets of airflow modes are shown, one for the driver and one for the passenger"], "P1", DM_F)],
}

S16_CH9 = ("ch16 十八節**無後排氣候之節**（DR #41 之實測），亦無 status bar "
           "dropdown 之後排捷徑，故本條之 EMEA 排除無 ch16 對造句可依")
S16_GEN = ("ch16 十八節無對應句 —— 本節之主體（{what}）於 ch16 全章無任何陳述；"
           "EMEA 排除依 R-C36-1 逐條答為 `no`")
EMEA = {
 "2.3.1": S16_GEN.format(what="dual AUTO 配置"),
 "2.5.1": S16_GEN.format(what="三態 recirc 之切換") +
          "（`16.5` 之 ICE4 僅述 recirc 圖示依車型，不述三態）",
 "9.2": S16_CH9, "9.3": S16_CH9, "9.4": S16_CH9, "9.4.1": S16_CH9,
 "14.12": S16_GEN.format(what="HVAC popup 之型式與硬控型態之對應"),
 "14.14": S16_GEN.format(what="driver/passenger centric popup"),
 "17.4": S16_GEN.format(what="Comfort widget 之 25% 版面與其 toggle"),
 "17.5": S16_GEN.format(what="Comfort widget 之雙側溫度與兩組氣流模式"),
}

R42 = ("**本節依 R-C42 解封**（64 §1）：其停下之唯一依據為「該配置軸未登記」，"
       "而條文自帶適用條件 —— ")
REASONING = {
"2.3.1": R42+"「**Some vehicles with dual zone climate with dual airflow mode can have a configuration for dual AUTO modes**」，故 R-C28 第一問由本節自身滿足，PC 逐字引之並標 `spec-verbatim`。驗證目標：C2.1 定出雙側各一 AUTO 之配置與其指示器之分列，兩個 037 leaf 對應之。關鍵情境條件：本節自帶之 dual AUTO 配置條件（**尚未登記為軸，登為待軸化候選；其與 `14.14`／`17.5` 共用 dual airflow modes 一語，依 R-C42 三須登記**，見上繳 42 §5）；依 **R-C34** 第九／十三軸與 EMEA 暴露 → 補。為什麼這樣切：配置之存在（`004-01`）與指示器之分列（`004-02`）可獨立失效。刻意略過：**C2.1 未定義兩個 AUTO 之互動**（一側開另一側是否受影響），故 ER 只驗其各自存在與分列（§8.4.1）。",
"2.5.1": R42+"「**Some vehicles have a configuration for a 3 state toggle recirc button: Auto, Manual, Open**」，三個狀態亦為逐字原文。驗證目標：C4.1 定出三態切換與其指示，兩個 037 leaf 對應之。關鍵情境條件：本節自帶之三態 recirc 配置（待軸化候選）；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：循環（`007-01`）取狀態轉換法，指示（`007-02`）為其呈現面。刻意略過：**`2.5`（C4）之 recirc 圖示對照仍未定義（DR #32），本節不驗圖示** —— 只驗狀態之名稱與其切換順序，該順序為條文逐字所列。",
"9.2": R42+"其適用範圍由 `9.1`（CR11）「**On some vehicles (See CFTS043 for details), there are additional Rear Climate controls and shortcuts**」界定，本節以「in these variants」回指之（跨節取據 R-C29）。驗證目標：CR12 定出替代式風速 popup 之內容與其觸控導向，兩個 037 leaf 對應之。關鍵情境條件：上述變體條件（**待軸化候選；DR #41 之問句改為「該變體涵蓋哪些車輛」而非「可否生成」**）；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：popup 之內容（`040-01`）與其互動（`040-02`）失效形態不同；**「See «HVAC Popups» chapter and C1./C2. requirements」為對本 spec 他節之委派**，其 popup 之一般邏輯不在本節驗（§8.2.1，此即本節刻意略過者）。",
"9.3": R42+"同 `9.2`，其變體條件由 `9.1` 界定。驗證目標：C12.1 一句定出該 popup 之兩個文字標籤，其 037 leaf 即本節自身（無子條）。關鍵情境條件：同 `9.2`；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：一葉一 TC，兩個標籤同屬一句故同條驗之。刻意略過：**本 leaf 帶圖**（A-CF23 名單內）—— 五問之答皆為否：ER 只用條文逐字之 «Front»／«Rear»（profile §3.4 之 source-quoted token），不描述圖中之版面。",
"9.4": R42+"同 `9.2`。驗證目標：CR13 定出狀態列下拉之後排捷徑鍵、其對後排分頁之反映，以及高亮之語意，三個 037 leaf 對應之。關鍵情境條件：同 `9.2`；依 **R-C34**：可觀察量在**狀態列之下拉選單**，6.3 移除者為 comfort section → **第九軸仍補**（下拉選單屬 head unit 之氣候介面，其存廢與 comfort section 同源，此判斷為 `[manual]`）；第十三軸與 EMEA 補。為什麼這樣切：切換（`042-01`）取狀態轉換法；`042-02` 之可觀察量在另一畫面（後排分頁），與 `042-03` 之高亮不同。刻意略過：**「following core Rear Climate on / off logics」為對 `7.6` 之委派**，其細節不在本節驗。",
"9.4.1": R42+"同 `9.2`。驗證目標：CR13.1 一句定出該捷徑鍵之標籤，其 037 leaf 即本節自身。關鍵情境條件：同 `9.4`（其按鈕即 `9.4` 所定者，跨節取據 R-C29）；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：一葉一 TC。刻意略過：**«Rear» 為 source-quoted token**，照錄不譯（profile §3.4）。",
"14.12": R42+"「**If the hard controls are knobs that turn** … **If the hard controls are UP/DOWN toggles** …」—— 兩個值皆為條文自帶之逐字條件。驗證目標：HVACP12 定出 popup 型式須與硬控型態相符，三個 037 leaf 對應之。關鍵情境條件：`096-01`／`096-03` 取旋鈕值、`096-02` 取 UP/DOWN 值，**PC 與 ER 皆逐字引條文，不加「該功能之」等限定**（65 §2）；依 **R-C34** 三軸暴露 → 補。**DR #37 之歧義保留於條文所在之處**：HVACP12 寫「**the hard controls**」為全車之集合語，而同一車上各控制之型態可能不同 —— **於混合型態之車輛上，本條依 14.12 之字面無法判定其適用**，測試員將於該車型撞見此事，而那正是 DR #37 應被回答之證據；**以措辭消解歧義等於替上游作答**（§8.4.1）。為什麼這樣切：兩個型態各自成條，`096-03` 驗其「相符」之通則；**radial／vertical 之外觀未定義**，故 ER 只用條文之詞（§8.4.1，此即本節刻意略過者）。",
"14.14": R42+"「**For vehicles with dual zone climate versions with dual airflow modes on 8.4\", 10.1\" Landscape, 10.25\" and 12.3\" radios**」—— 兩個配置條件（雙區雙氣流、螢幕型號）皆為條文逐字所列。驗證目標：HVACP14 一句定出雙側 centric popup，其 037 leaf 即本節自身。關鍵情境條件：上述條件（**待軸化候選：dual airflow modes 與螢幕型號；後者即 DR #6 之對象** —— 惟 **DR #6 問的是「本次交付出哪幾種螢幕」，非「條文有無陳述」**，故不阻卻生成）；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：一葉一 TC，兩側各驗一次。刻意略過：**centric popup 之版面未定義**，ER 只驗其為駕駛側／乘客側之 popup。",
"17.4": R42+"「**For 8.4/10.1/12 landscaped screens, there will be a toggle button on the 25% widget**」。驗證目標：CW3 定出 25% widget 之 Heat／Vent 切換鍵與其功能切換，兩個 037 leaf 對應之。關鍵情境條件：本節自帶之螢幕條件（待軸化候選，同 `14.14`）；依 **R-C34** 第九軸暴露（widget 在 head unit 首頁）、第十三軸與 EMEA 補。為什麼這樣切：鍵之存在與切換（`127-01`）與其所切換之內容（`127-02`）可獨立失效。刻意略過：**25% 與 50% widget 之版面差異不在本節**（`17.2`／`17.3` 各有其句），故不跨節移植。",
"17.5": R42+"「**For dual zone climate with dual airflow modes equipped vehicles**」。驗證目標：CW4 定出該類車 widget 之雙側溫度與兩組氣流模式，兩個 037 leaf 對應之。關鍵情境條件：本節自帶之雙區雙氣流條件（**待軸化候選，與 `2.3.1`／`14.14` 同一條件 —— 依 R-C42 三，同一條件出現於三節而未登記為軸，gate 將 FAIL**，故本輪一併登記，見上繳 42 §5）；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：溫度（`128-01`）與氣流模式（`128-02`）為 widget 上兩個獨立區塊。刻意略過：**DR #38 之否定值仍無字面** —— 惟依 R-C42 二，軸之登記與可生成性無關，本節之 PC 由其自身條文支持。",
}

DIST_AXIS = {}


def add_lines(pre_conditions: str, *lines: str) -> str:
    n = len([l for l in pre_conditions.split("\n") if l.strip()])
    out = pre_conditions
    for line in lines:
        n += 1
        out = f"{out}\n{n}. {line}"
    return out


def _iar() -> dict:
    with (FEATURE / "data" / "interface_axis_review.tsv").open(
            encoding="utf-8") as fh:
        return {r.pop("outline"): r for r in csv.DictReader(fh, delimiter="\t")}


def ref(*outlines) -> str:
    return "; ".join(f"{STEM}_{o}" for o in dict.fromkeys(outlines))


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    iar = _iar()
    OUT.mkdir(parents=True, exist_ok=True)
    n = START_N - 1
    total = 0

    for o, meta in SECTIONS.items():
        tcs = []
        for leaf, title, item, proc, er, prio, dm in TCS[o]:
            n += 1
            pc = LEAF_PC.get(leaf, meta["pc"])
            if o in WIDGET_SECTIONS:
                pc = f"{pc}\n{PC_WIDGET}"
            pc = add_lines(pc, EX_ICS, EX_EMEA, EX_LOWER)
            refs = [o] + list(meta["refs"]) + ["2.14", "16.2", "6.3"]
            tcs.append({
                "req_id": f"SWE1-HVAC-{leaf}",
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": title,
                "test_group": TEST_GROUP,
                "test_set": meta["test_set"],
                "test_item": item,
                "pre_conditions": pc,
                "input_test_data": "NA",
                "test_procedure": "\n".join(proc),
                "expected_result": "\n".join(er),
                "specification_reference": ref(*refs),
                "priority": prio,
                "design_method": dm,
                "split_flag": False,
                "split_reason": "",
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": LEAF_REMARKS.get(leaf, ""),
                "emea_ics_review": {"ch16_outline": "no-counterpart",
                                    "verdict": "no",
                                    "ch16_sentence": EMEA[o]},
            })
        doc = {
            "parent": meta["parent"], "outline": o, "batch": meta["test_set"],
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o], "keywords": [],
            "duplicate_of": "",
            "distinguishing_axis": DIST_AXIS.get(
                o, {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [], "interface_axis_review": iar[o], "tcs": tcs,
        }
        (OUT / f"{meta['parent']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{meta['parent']}  {o:8} {len(tcs)} TC  [{meta['test_set']}]")

    print(f"\n{total} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    if total != 19:
        raise SystemExit(f"expected 19, got {total}")


if __name__ == "__main__":
    main()
