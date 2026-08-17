#!/usr/bin/env python3
"""Batch 7 generator — ICS Temperature and Fan (handoff 44 §8).

Scope from framework.md line 51: `16.6, 16.6.1, 16.7, 16.17` = **17 leaves**.
037 measured independently: 110(6) + 111(5) + 112(5) + 123(1) = 17.

  !! 44 §8's header table lists the Layer 3 as "16.6、16.6.1、16.7" while
  !! quoting 17 leaves. Those two facts are inconsistent: the three sections
  !! are 16 leaves. framework.md lists FOUR (16.17 added by 14 §1's amendment,
  !! which paired 2.16/16.17) totalling 17. Generated from framework.md, which
  !! 44 §8 itself names as the authority. This is the SECOND package in a row
  !! with the same shape (32 §7.1); reported in 上繳 33 §8.1.

Emitted: 17 TCs, -098 … -114. Nothing withheld.

ch16 side, so the three inversions of batch 6 apply again (positive EMEA axis
value, mirror map read in REVERSE, axis 13 cited from ch2). What is NEW here:

  every counterpart is generated. 16.6<->2.6, 16.6.1<->2.6.1, 16.7<->2.7 and
  16.17<->2.16 are all `mirrored`, and all four ch2 sections already have TCs.
  R-C36-1's TC-against-TC check is therefore available for the whole batch
  rather than for a sample — see 上繳 33 §8.4.

Reverse reading of ch16_mirror_map.tsv — what ch2 has that ch16 does NOT, so
that it is not imported (§8.2.1):

  C5  (2.6)   has "This status is relayed from the CCM"; ICE5 has no such
              sentence -> not imported
  C5  (2.6)   says Metric switches "the READOUT"; ICE5 says "the CCM switches
              to half degree increments" -> different actor, ICE5's wording
              used, ER stays on the observable (the displayed increment)
  C6  (2.7)   has "Off, 1-7, **15h** (denoting to show AUTO instead)";
              ICE6 has "Off, 1-7 (denoting to show AUTO label instead when in
              AUTO)" -> **ICE6 carries no 15h**. The CAN value must not be
              imported; -098's ER states the AUTO label, not 15h
  C6  (2.7)   "or use Hard Control" for fan adjustment: ICE6 keeps it
  ICE5.1      states the slider-handle rule TWICE (two near-identical
              sentences). 037 gave it ONE leaf (111-05); one leaf, one TC

Usage:
    python3 features/comfort/scripts/gen_batch7.py
"""

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_item import apply_test_item   # Pei 2026-08-17 —— 上半照抄條文、下半情境
from splits import apply_splits   # 76 §2 — 依 75 §1（今併入 R-C44 第一問）之列舉判準拆分

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "ICS Temperature and Fan"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 98

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
# profile §3.3 — the string must match 下拉選單!A1:A9 character for
# character. `, BVA` is part of the workbook's own entry; dropping it
# was caught by the design-method gate on the first run.
DM_BVA = "邊界值分析 (Boundary Value Analysis, BVA)"

PC_EMEA = ("1. [spec-derived] The vehicle is an EMEA ICS vehicle, whose climate "
           "interface is specified in chapter 16 (16.2)")
EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
PC_MULTIZONE = ("[spec-derived] The vehicle is not a single zone climate "
                "configuration, for which Sync is not shown (16.11)")

# Axis 9 — exposed where the observable lives in the head unit's comfort
# section; NOT exposed where it is a comfort pop-up (6.3's own exception).
LOWER_EXPOSED = {
    "SWE1-HVAC-110-01", "SWE1-HVAC-110-02", "SWE1-HVAC-110-03",
    "SWE1-HVAC-110-05",
    "SWE1-HVAC-111-01", "SWE1-HVAC-111-02", "SWE1-HVAC-111-03",
    "SWE1-HVAC-111-04", "SWE1-HVAC-111-05",
    "SWE1-HVAC-112-01", "SWE1-HVAC-112-02", "SWE1-HVAC-112-04",
    "SWE1-HVAC-112-05",
    "SWE1-HVAC-123",
}
# Axis 2 — only the SYNC-dependent leaves.
MULTIZONE_EXPOSED = {"SWE1-HVAC-110-06", "SWE1-HVAC-111-01",
                     "SWE1-HVAC-111-02"}

WITHHELD = []


def add_lines(pre_conditions: str, *lines: str) -> str:
    n = len([l for l in pre_conditions.split("\n") if l.strip()])
    out = pre_conditions
    for line in lines:
        n += 1
        out = f"{out}\n{n}. {line}"
    return out


def _load_interface_axis_review() -> dict:
    path = FEATURE / "data" / "interface_axis_review.tsv"
    with path.open(encoding="utf-8") as fh:
        return {r.pop("outline"): r
                for r in csv.DictReader(fh, delimiter="\t")}


INTERFACE_AXIS_REVIEW = _load_interface_axis_review()

BATCHES = [
    {
        "parent": "SWE1-HVAC-110",
        "outline": "16.6",
        "reasoning":
            "驗證目標：16.6（ICE5）定出 ICS 介面之溫度值域、HI／LO 取代度數、狀態呈現位置、硬鍵 popup 條件、Metric 半度增量與其四處同步，六個 037 leaf 逐句對應，一葉一 TC（§8.2.1）。關鍵情境條件：EMEA 軸取正向值（出處 16.2，併入 spec_ref 依 R-C29）；依 **R-C34** 第十三軸全數補（可觀察量為 HVAC 畫面與 popup），第九軸補 `-01`／`-02`／`-03`／`-05`（可觀察量在 head unit 之 comfort section），`-04`（popup）與 `-06`（sync 時之 slider popup）不補 —— popup 正是 6.3 之例外，第十二軸不補（ch16 無 tab 條文）；`-06` 另補第二軸（非單區，出處 16.11）。為什麼這樣切：`-01` 驗值域之兩端與單位切換、`-02` 驗端點以 HI／LO 取代度數，兩者失效形態不同（值域錯 vs 端點顯示錯），故 `-01` 取邊界值分析而 `-02` 另立。刻意略過：**鏡射表反向使用之結果** —— C5 之「This status is relayed from the CCM」一句於 ICE5 不存在，**不移植**；C5 記 Metric 切換者為「the **readout**」而 ICE5 記為「the **CCM** switches to half degree increments」，**兩者主詞不同**，本批依 ICE5 之措辭，惟 ER 停在可觀察量（畫面所示之增量）而不驗 CCM 內部行為（§8.2.1）。",
        "keywords": ["temperature range", "HI", "LO", "Metric",
                     "half degree"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-110-01",
                "tc_title": "Temperature range covers both English and Metric",
                "test_item":
                    "Temperature ranges shall be LO, 60-84, HI (English) and "
                    "LO, 16-28, HI (Metric)",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the temperature units to English and open the "
                    "climate screen\n"
                    "2. Adjust the temperature across its whole range\n"
                    "3. Set the temperature units to Metric\n"
                    "4. Adjust the temperature across its whole range",
                "expected_result":
                    "1. The climate screen shows the temperature setting\n"
                    "2. The settings available are LO, 60 to 84, HI\n"
                    "3. The climate screen shows the temperature setting\n"
                    "4. The settings available are LO, 16 to 28, HI",
                "priority": "P1",
                "design_method": DM_BVA,
            },
            {
                "req_id": "SWE1-HVAC-110-02",
                "tc_title": "HI and LO replace the degree value at the extremes",
                "test_item":
                    "When at the highest possible position the system shall "
                    "display HI, and when at the lowest shall display LO, "
                    "instead of a degree value",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The vehicle has an ATC climate system "
                    "(16.6)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Adjust the temperature to its highest position on the "
                    "climate screen\n"
                    "2. Adjust the temperature to its lowest position",
                "expected_result":
                    "1. The climate screen shows HI instead of a degree value\n"
                    "2. The climate screen shows LO instead of a degree value",
                "priority": "P1",
                "design_method": DM_BVA,
            },
            {
                "req_id": "SWE1-HVAC-110-03",
                "tc_title": "Temperature status shows on the screen and status bar",
                "test_item":
                    "The temperature status shall be indicated on the TS "
                    "climate screen and in the status bar",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Adjust the temperature on the climate screen\n"
                    "3. Read the status bar",
                "expected_result":
                    "1. The climate screen shows the current temperature\n"
                    "2. The climate screen shows the new temperature\n"
                    "3. The status bar shows the new temperature",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-110-04",
                "tc_title": "Temperature pop-up appears off the climate screen",
                "test_item":
                    "The system shall show a pop-up when the status is changed "
                    "via hard control and the currently shown screen is not "
                    "the climate screen",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen other than the climate screen\n"
                    "2. Change the temperature using the temperature hard "
                    "control",
                "expected_result":
                    "1. The climate screen is not displayed\n"
                    "2. A temperature pop-up is shown",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-110-05",
                "tc_title": "Metric switches every temperature readout to half degrees",
                "test_item":
                    "When the user sets the climate system temperature ranges "
                    "to Metric, the temp slider, status bar, temp slider "
                    "popup and temp popup shall reflect half degree increments",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the climate system temperature ranges to Metric\n"
                    "2. Adjust the temperature using the temp slider and read "
                    "the temp slider popup\n"
                    "3. Read the status bar\n"
                    "4. Change the temperature using the temperature hard "
                    "control from a screen other than the climate screen",
                "expected_result":
                    "1. The climate screen shows the temperature in Metric\n"
                    "2. The temp slider and the temp slider popup move in half "
                    "degree increments\n"
                    "3. The status bar shows the temperature in half degree "
                    "increments\n"
                    "4. The temp popup shows the temperature in half degree "
                    "increments",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-110-06",
                "tc_title": "No passenger slider pop-up while synced",
                "test_item":
                    "When sync'd, the system shall not show the slider pop-up "
                    "on the passenger side when adjusting the driver slider",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn SYNC on from the climate screen\n"
                    "2. Adjust the driver temperature slider",
                "expected_result":
                    "1. The \"SYNC\" button is highlighted\n"
                    "2. No slider pop-up is shown on the passenger side",
                "priority": "P2",
                "design_method": DM_FUNC,
                "spec_ref": ("16.6", "16.11"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-111",
        "outline": "16.6.1",
        "reasoning":
            "驗證目標：16.6.1（ICE5.1）定出 SYNC 之溫度連動與中斷、三種調整途徑、長按快移、以及滑桿把手之按壓判定，五個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：EMEA 軸取正向值（16.2，R-C29 併入 spec_ref）；依 **R-C34** 第十三軸全數補，第九軸全數補（五條之可觀察量皆在 head unit 之 climate screen），第十二軸不補；`-01`／`-02` 另補第二軸（SYNC 於單區不顯示，出處 16.11）。為什麼這樣切：`-01`（連動）與 `-02`（中斷）為 SYNC 之兩個相反方向，可各自獨立失效；`-04` 之長按快移同時適用畫面箭頭與**硬鍵**，其失效與 `-03` 之途徑列舉無關。刻意略過：**ICE5.1 把滑桿把手規則寫了兩次**（`User must press slider handle…` 與 `The user can also press slider handle…`，後者多一個括號說明），037 只給一個 leaf（`-05`），故一葉一 TC 不因條文重複而拆；**`voice command` 照錄於 `-03` 之 test_item 而不入 procedure** —— 語音辨識之觸發方式本節未定義，寫入即造值（§8.4.1）。",
        "keywords": ["SYNC", "slider", "long press", "slider handle"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-111-01",
                "tc_title": "Driver temperature drives passenger temperature when synced",
                "test_item":
                    "If SYNC is ON, adjusting the driver temperature shall "
                    "affect the passenger temperature",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn SYNC on from the climate screen\n"
                    "2. Adjust the driver temperature",
                "expected_result":
                    "1. The \"SYNC\" button is highlighted\n"
                    "2. The passenger temperature follows the driver "
                    "temperature",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("16.6.1", "16.11"),
            },
            {
                "req_id": "SWE1-HVAC-111-02",
                "tc_title": "Adjusting passenger temperature breaks SYNC",
                "test_item":
                    "Adjusting the passenger temperature shall break SYNC and "
                    "turn it off",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn SYNC on from the climate screen\n"
                    "2. Adjust the passenger temperature",
                "expected_result":
                    "1. The \"SYNC\" button is highlighted\n"
                    "2. The \"SYNC\" button is no longer highlighted",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("16.6.1", "16.11"),
            },
            {
                "req_id": "SWE1-HVAC-111-03",
                "tc_title": "Temperature changes by arrows and by slider",
                "test_item":
                    "The user shall be able to change the temperature on the "
                    "climate screen by using arrows or the slider, and the "
                    "system shall be able to jump to a value via the slider "
                    "or voice command",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the temperature up arrow on the climate screen\n"
                    "2. Touch the slider handle and drag it to another value",
                "expected_result":
                    "1. The temperature moves 1 increment up\n"
                    "2. The temperature follows the slider handle, and a TEMP "
                    "pop-up is shown next to the slider",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-111-04",
                "tc_title": "Long press moves the temperature fast on screen and hard control",
                "test_item":
                    "Long press shall be a fast move, and shall also work for "
                    "temperature HARD CONTROLS",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press and hold the temperature up arrow on the climate "
                    "screen\n"
                    "2. Press and hold the temperature hard control in the up "
                    "direction",
                "expected_result":
                    "1. The temperature moves up by more than 1 increment "
                    "while the press is held\n"
                    "2. The temperature moves up by more than 1 increment "
                    "while the press is held",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-111-05",
                "tc_title": "Slider presses outside the handle are ignored",
                "test_item":
                    "The user must press the slider handle to move the "
                    "temperature slider position; if the user initially "
                    "presses the slider area outside of the handle, the system "
                    "shall ignore the press",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the slider area to the left of the slider handle\n"
                    "2. Press the slider handle and drag it",
                "expected_result":
                    "1. The temperature slider position does not move\n"
                    "2. The temperature slider position follows the handle",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-112",
        "outline": "16.7",
        "reasoning":
            "驗證目標：16.7（ICE6）定出 ICS 介面之風速值域、狀態呈現位置、硬鍵 popup 條件、三種畫面調整途徑、以及不可由控制關閉風扇，五個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：EMEA 軸取正向值（16.2，R-C29）；依 **R-C34** 第十三軸全數補，第九軸補 `-01`／`-02`／`-04`／`-05`（可觀察量在 climate screen 與 main category control），`-03`（popup）不補，第十二軸不補。為什麼這樣切：`-05` 之「不可關閉」與「唯一全灰途徑為關閉 CLIMATE」為同一 leaf 之兩面，037 未拆，故合為一條並以兩組步驟涵蓋其正反兩側（§7 之 supported 配 negative）。刻意略過：**鏡射表反向使用之關鍵差異** —— C6 之值域為「Off, 1-7, **15h** (denoting to show AUTO instead)」而 **ICE6 無 `15h`**，其措辭為「Off, 1-7 (denoting to show AUTO **label** instead **when in AUTO**)」；`15h` 為 CAN 值，**不得自 ch2 移植**，故 `-01` 之 ER 述 AUTO 標示而不述 15h（§8.2.1）。",
        "keywords": ["fan range", "AUTO label", "fan segment",
                     "main category control"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-112-01",
                "tc_title": "Fan range runs Off to 7 and shows AUTO when in AUTO",
                "test_item":
                    "Fan ranges shall be Off, 1-7, denoting to show the AUTO "
                    "label instead when in AUTO",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Adjust the fan speed across its whole range on the "
                    "climate screen\n"
                    "2. Turn AUTO on",
                "expected_result":
                    "1. The fan speeds available are 1 to 7\n"
                    "2. The fan speed indicator shows the AUTO label instead "
                    "of a fan speed",
                "priority": "P1",
                "design_method": DM_BVA,
            },
            {
                "req_id": "SWE1-HVAC-112-02",
                "tc_title": "Fan status shows on the screen and category control",
                "test_item":
                    "The fan status shall be indicated on the TS climate "
                    "screen and in the main category control",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed on the climate screen\n"
                    "3. Read the main category control",
                "expected_result":
                    "1. The climate screen shows the current fan speed\n"
                    "2. The climate screen shows the new fan speed\n"
                    "3. The main category control shows the new fan speed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-112-03",
                "tc_title": "Fan pop-up appears off the climate screen",
                "test_item":
                    "The system shall show a pop-up when the status is changed "
                    "via hard control and the currently shown screen is not "
                    "the climate screen",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen other than the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control",
                "expected_result":
                    "1. The climate screen is not displayed\n"
                    "2. A fan speed pop-up is shown",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-112-04",
                "tc_title": "Fan is adjustable by buttons touch or slide on screen",
                "test_item":
                    "When on the climate screen, the user shall be able to use "
                    "the Fan up/down buttons, directly touch a fan segment to "
                    "jump, or slide, or use the Hard Control",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the fan up button on the climate screen\n"
                    "2. Touch a fan segment on the climate screen\n"
                    "3. Slide across the fan segments on the climate screen\n"
                    "4. Change the fan speed using the fan speed hard control",
                "expected_result":
                    "1. The fan speed increases\n"
                    "2. The fan speed jumps to the touched segment\n"
                    "3. The fan speed follows the slide\n"
                    "4. The fan speed follows the hard control",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-112-05",
                "tc_title": "Fan cannot be turned off except by the climate system",
                "test_item":
                    "The user shall not be able to turn the FAN off by using "
                    "the FAN controls on the screen or the FAN hard control, "
                    "and the only way to have all FAN bars grayed out shall be "
                    "by shutting the CLIMATE system OFF",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the fan down button on the climate screen "
                    "repeatedly until the fan speed stops decreasing\n"
                    "2. Turn the fan speed hard control down repeatedly until "
                    "the fan speed stops decreasing\n"
                    "3. Turn the climate system off using the climate power "
                    "button on the screen",
                "expected_result":
                    "1. The fan is not off and one fan bar remains highlighted\n"
                    "2. The fan is not off and one fan bar remains highlighted\n"
                    "3. All FAN bars are grayed out",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-123",
        "outline": "16.17",
        "reasoning":
            "驗證目標：16.17 定出語音辨識期間之自動風機降速**不顯示**於使用者，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：EMEA 軸取正向值（16.2，R-C29）；依 **R-C34** 第十三軸補（可觀察量為風速指示，屬 HVAC 畫面），第九軸補（風速指示在 head unit 之 comfort section），第十二軸不補。為什麼這樣切：本節僅一句一 leaf，不拆；其驗證形態為**否定式**（變化不顯示），故步驟以「降速前後各讀一次風速指示」建立基線與對照（§5.6），末步持驗證（§5.5）。刻意略過：**條文未給降速之幅度與其觸發之語音操作**，故步驟以「啟動語音辨識工作階段」為觸發而不指定任何語音指令內容，亦不寫入任何風速數值（§8.4.1 禁造值）；**本節之條款 id 標為 `C16.)`，與 `2.15` 之 `C16.)` 相撞**，屬 A-CF13 已登之四項之一，traceability 一律以 outline 為鍵（profile §1），故本條之 spec_ref 記 16.17 而非條款標籤。",
        "keywords": ["blower reduction", "Voice Recognition", "fan speed"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-123",
                "tc_title": "Blower reduction during voice recognition is not shown",
                "test_item":
                    "If blower reduction occurs automatically due to an active "
                    "Voice Recognition session, the change in fan speed shall "
                    "not be displayed to the user",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen and read the fan speed "
                    "indicator\n"
                    "2. Start a Voice Recognition session and read the fan "
                    "speed indicator\n"
                    "3. End the Voice Recognition session and read the fan "
                    "speed indicator",
                "expected_result":
                    "1. The climate screen shows the current fan speed\n"
                    "2. The fan speed indicator is unchanged\n"
                    "3. The fan speed indicator is unchanged",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
]


def ref(*outlines) -> str:
    return "; ".join(f"{STEM}_{o}" for o in dict.fromkeys(outlines))


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    OUT.mkdir(parents=True, exist_ok=True)
    n = START_N - 1
    total = 0

    for b in BATCHES:
        o = b["outline"]
        if o not in full:
            raise SystemExit(f"{o} not in section_fulltext.tsv")
        tcs = []
        for tc in b["tcs"]:
            n += 1
            # R-C29 — PC_EMEA cites 16.2, so 16.2 joins spec_ref everywhere.
            extra, refs = [], list(tc.get("spec_ref", (o,))) + ["16.2"]
            extra.append(EX_ICS)
            refs.append("2.14")
            if tc["req_id"] in MULTIZONE_EXPOSED:
                extra.append(PC_MULTIZONE)
                refs.append("16.11")
            if tc["req_id"] in LOWER_EXPOSED:
                extra.append(EX_LOWER)
                refs.append("6.3")
            tcs.append({
                "req_id": tc["req_id"],
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": tc["tc_title"],
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": tc["test_item"],
                "pre_conditions": add_lines(tc["pre_conditions"], *extra),
                "input_test_data": tc["input_test_data"],
                "test_procedure": tc["test_procedure"],
                "expected_result": tc["expected_result"],
                "specification_reference": ref(*refs),
                "priority": tc["priority"],
                "design_method": tc["design_method"],
                "split_flag": tc.get("split_flag", False),
                "split_reason": tc.get("split_reason", ""),
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
            })
        doc = {
            "parent": b["parent"],
            "outline": o,
            "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": b["reasoning"],
            "keywords": b["keywords"],
            "duplicate_of": "",
            "distinguishing_axis": ({"axis": "節之主題（ICS 畫面解剖 vs ICS 溫度控制）—— 惟其一對 TC 為嚴格等價",
                                    "delta": "`16.2`（ICE1）之主題為 ICS climate 畫面之組成與其元素，`16.6`（ICE5）之主題為溫度之控制與呈現。**兩節各有一 leaf 述同一件事**：`106-04` 與 `110-06` 之 `test_item`／`test_procedure`／`expected_result` **與 `pre_conditions` 皆相同**（僅 PC 行序不同），即**同一台車上要跑兩次一模一樣的測試**。**§10.6 四項全同 → 嚴格等價**，惟 `duplicate_of` **不填** —— 該欄為節級（宣稱整節重複，為假）而此處為條級；037 之兩個 leaf 各自存在，§8.2.2 禁本層合併 leaf。已登 **DR #42**，並記於 pending_sibling 之 `equivalent_tc_pairs`。**本對與跨第九軸之等價對不同**：那些兩側互斥（同一車不可能既 ICS 又非 ICS），本對兩側**同章同軸值**，故重複是實在的"}
                                   if o == "16.6" else
                                   {"axis": "see per-TC titles",
                                    "delta": ""}),
            "assumptions": [],
            "interface_axis_review": INTERFACE_AXIS_REVIEW[o],
            "tcs": apply_test_item(apply_splits(tcs)),
        }
        (OUT / f"{b['parent']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{b['parent']}  {o:8} {len(tcs)} TC  -> generated/{b['parent']}.json")

    leaves = len({tc["req_id"] for b in BATCHES for tc in b["tcs"]})
    print(f"\n{leaves} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    held = len(WITHHELD)
    print(f"{leaves} emitted + {held} withheld = {leaves + held} leaves "
          f"declared for {TEST_SET} (framework.md: 17)")
    if leaves + held != 17 or total != 17:
        raise SystemExit(
            f"expected 17 leaves declared / 17 TCs, got {leaves + held} / {total}")


if __name__ == "__main__":
    main()
