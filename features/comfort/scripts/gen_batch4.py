#!/usr/bin/env python3
"""Batch 4 generator — Temperature and Fan (handoff 35 §6).

Scope derived from framework.md line 41, not from the handoff's table
(33 §0's lesson): 2.6, 2.6.1, 2.7, 2.7.1, 2.16 = 19 leaves. 037 measured
independently: 008(5) + 009(6) + 010(5) + 011(1) + 022(2) = 19.

Emitted: 18 TCs, -047 … -064.
WITHHELD: 2.7.1 (SWE1-HVAC-011, 1 leaf) — "In some vehicles fan speed ranges
for front hvac are: Off, 1-8" is a selector, and front-HVAC fan range is not
one of the thirteen axes. See upstream 24 §5.

R-C34's generation-time duty, discharged for every TC below: name the
interface the observable sits on, then ask each interface-type axis whether
one of its values removes that interface.

  observable interface : TS climate screen / status bar / main category
                         control / temperature and fan pop-ups — all HVAC UI
  axis 13 (3-knob ICS) : removes it -> excluded on every TC
  EMEA ICS (ch16)      : ch16.6/6.1/16.7/16.17 mirror these sections for the
                         EMEA variant -> excluded on every TC
  axis 9 (lower screen): 6.3 removes the head unit's comfort section. Only
                         010-01 reads the main category control, so only it
                         is exposed; the climate screen and status bar are
                         not that section
  axis 12 (front-only) : removes TABS. Nothing here observes a tab, so no TC
                         is exposed — reason named rather than left silent

Usage:
    python3 features/comfort/scripts/gen_batch4.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "Temperature and Fan"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 48

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"
DM_BVA = "邊界值分析 (Boundary Value Analysis, BVA)"

EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
LOWER_EXPOSED = {"SWE1-HVAC-010-01"}      # reads the main category control
# 39 §1.1 — per-TC removals, not section-level: the ch16 counterpart covers
# some rows of these sections and not others. 16.14 (ICE13) is two sentences
# where 2.14 (C15) is a paragraph, so 020-01/-02 keep the exclusion while
# 020-03/-04 lose it; likewise 16.17 is one sentence where 2.16 is two.
EMEA_REMOVED_REQ_IDS = {"SWE1-HVAC-022-02", "SWE1-HVAC-011"}


PC_ATC = "1. [spec-verbatim] The climate system is ATC (2.6)"
# 2.11 states Sync is not shown for single zone configurations; the fact is
# cited there, not invented here (R-C29).
PC_DUAL = ("1. [spec-derived] The vehicle is not a single zone climate "
           "configuration, for which Sync is not shown (2.11)")


def add_exclusions(pre_conditions: str, *lines: str) -> str:
    n = len([l for l in pre_conditions.split("\n") if l.strip()])
    out = pre_conditions
    for line in lines:
        n += 1
        out = f"{out}\n{n}. {line}"
    return out


# ---- 36 §6 / R-C34's generation-time duty, recorded per section ----------
# The duty cannot be machine-checked for correctness, but it can be checked
# for having been discharged. Each section names the interface its observables
# sit on and answers all four interface-type axes; the interface-axis-answered
# gate fails on a missing or empty answer.
# ---- 37 §5 — one source, four readers -------------------------------------
# The table lived as four identical literals, one per generator; nothing kept
# them in step, and a reverse-verification that edited only one copy is what
# exposed it. A single file makes divergence structurally impossible, which
# beats adding a gate to compare four copies of something that need not be
# duplicated.
def _load_interface_axis_review() -> dict:
    path = FEATURE / "data" / "interface_axis_review.tsv"
    with path.open(encoding="utf-8") as fh:
        return {r.pop("outline"): r
                for r in csv.DictReader(fh, delimiter="\t")}


INTERFACE_AXIS_REVIEW = _load_interface_axis_review()

# ---- 38 §1 / R-C36-1 — per-TC EMEA judgement -----------------------------
# Section-level `mirrored` was standing in for a per-TC answer, and it hid
# five over-strict exclusions: 16.14 is two sentences where 2.14 is a
# paragraph, and 16.17 is one where 2.16 is two. Each row names the ch16
# sentence its verdict rests on, so "mirrored" is never the whole answer.
def _load_emea_per_tc() -> dict:
    path = FEATURE / "data" / "emea_ics_per_tc.tsv"
    with path.open(encoding="utf-8") as fh:
        return {r.pop("tc_id"): r for r in csv.DictReader(fh, delimiter="\t")}


EMEA_PER_TC = _load_emea_per_tc()


BATCHES = [
    # ----------------------------------------------------------------- 2.6
    {
        "parent": "SWE1-HVAC-008",
        "outline": "2.6",
        "reasoning":
            "驗證目標：2.6（C5）定出溫度之範圍與顯示（度數／HI／LO）、公制之半度增量、非 climate screen 時之 popup，以及四個呈現位置之一致性，五個 037 leaf 逐一對應，一葉一 TC（§8.2.1）。關鍵情境條件：可觀察量皆落於 TS climate screen、狀態列與溫度 popup，依 **R-C34** 對四個介面型軸逐一提問 —— 第十三軸（3 旋鈕 ICS）與 EMEA ICS 皆移除該介面，故全數補排除式 PC；第九軸移除之 head unit comfort section 不含 climate screen 與狀態列，第十二軸移除之 tabs 本節不觀察，二者不補並具名於此。-01 另取第一軸 ATC，其第一問由「Temperature will display the current degree value that the user has set it to for ATC systems」明文對應。為什麼這樣切：五者之失效互相獨立（度數正確而 HI／LO 錯、公制切換正確而 popup 不出），且分屬不同觀察位置。刻意略過：條文之溫度區間（60-84／16-28）為 CCM 轉達之狀態，本節未定義其邊界行為，故 -02 以條文自身之詞「highest possible position」「lowest」判定而不寫入數值（R-C22）。",
        "keywords": ["temperature", "HI", "LO", "Metric", "half degree",
                     "status bar", "temp popup"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-008-01",
                "tc_title": "Temperature shows on the climate screen and the status bar",
                "test_item":
                    "For ATC systems, the temperature shall display the "
                    "current degree value that the user has set it to, "
                    "indicated on the TS climate screen and in the status bar",
                "pre_conditions": PC_ATC,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Set the temperature to a degree value within the range\n"
                    "3. Read the temperature in the status bar",
                "expected_result":
                    "1. The climate screen shows the current temperature\n"
                    "2. The climate screen shows the degree value that was set\n"
                    "3. The status bar shows the same degree value",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-008-02",
                "tc_title": "HI and LO replace the degree value at the extremes",
                "test_item":
                    "When at the highest possible position the system shall "
                    "display HI, and when at the lowest it shall display LO, "
                    "instead of a degree value",
                "pre_conditions": PC_ATC,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the temperature to the highest possible position\n"
                    "2. Set the temperature to the lowest position",
                "expected_result":
                    "1. The climate screen shows HI instead of a degree value\n"
                    "2. The climate screen shows LO instead of a degree value",
                "priority": "P1",
                "design_method": DM_BVA,
            },
            {
                "req_id": "SWE1-HVAC-008-03",
                "tc_title": "Metric readout switches to half degree increments",
                "test_item":
                    "When the user sets the climate system temperature ranges "
                    "to Metric, the readout shall switch to half degree "
                    "increments",
                "pre_conditions": PC_ATC,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the climate system temperature ranges to Metric\n"
                    "2. Change the temperature by one increment",
                "expected_result":
                    "1. The readout switches to half degree increments\n"
                    "2. The temperature changes by half a degree",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-008-04",
                "tc_title": "Temperature pop-up appears off the climate screen",
                "test_item":
                    "The system shall show a pop-up when the status is changed "
                    "via hard control and the currently shown screen is not "
                    "the climate screen",
                "pre_conditions": PC_ATC,
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
                "req_id": "SWE1-HVAC-008-05",
                "tc_title": "Slider status bar and pop-ups follow the increment change",
                "test_item":
                    "The temperature within the temp slider, status bar, temp "
                    "slider popup, and temp popup shall reflect the change in "
                    "temperature increments",
                "pre_conditions": PC_ATC,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the climate system temperature ranges to Metric\n"
                    "2. Read the temperature in the temp slider and in the "
                    "status bar\n"
                    "3. Touch the temp slider and read the temp slider popup",
                "expected_result":
                    "1. The readout switches to half degree increments\n"
                    "2. The temp slider and the status bar show the "
                    "temperature in half degree increments\n"
                    "3. The temp slider popup shows the temperature in half "
                    "degree increments",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    # --------------------------------------------------------------- 2.6.1
    {
        "parent": "SWE1-HVAC-009",
        # 51 §2.1 / §4.6 — 2.11 (C12) is now generated, so this doc's sibling
        # judgement has to be backfilled. It is NOT `see per-TC titles`: the
        # sibling is another SECTION, and what separates the two is the axis
        # below. §10.6's strict-equivalence test on the overlapping pair:
        #   -053 vs -150  trigger: SYNC on + change driver temp
        #                 outcome: passenger temp follows        -> IDENTICAL
        #   -054 vs -151  trigger: SYNC on + change passenger temp
        #                 outcome: SYNC turns off                -> IDENTICAL
        # Those two pairs ARE strictly equivalent. duplicate_of is NOT set,
        # for a reason worth stating rather than hiding: §10.6's field is
        # DOC-level and a digits-only workbook row, while the duplication here
        # is per-TC (2 of 6 here, 2 of 3 there). Setting it would claim the
        # whole section duplicates the other, which is false. Reported in
        # 上繳 35 §8.4 as a granularity question for the analysis layer.
        "distinguishing_axis": {
            "axis": "which side of SYNC the section owns (2.6.1 vs 2.11)",
            "delta": "`2.6.1`（C5.1）之主題為**溫度之調整途徑**（箭頭 1 增量、長按快移、"
                     "滑桿把手、跳值），SYNC 之連動是其中一句；`2.11`（C12）之主題為 "
                     "**SYNC 這個功能本身**（其高亮指示、單區不顯示、對前後排風速與模式之作用）。"
                     "**惟 `-053`／`-054` 與 `-150`／`-151` 兩對為嚴格等價**（trigger／outcome／"
                     "input／verification target 四項皆同）—— 依 R-C33 037 之單位不動，"
                     "故兩側各自保留其 leaf 與 TC；`duplicate_of` 未設，理由見上方註解",
        },
        "outline": "2.6.1",
        "reasoning":
            "驗證目標：2.6.1（C5.1）定出 SYNC 下之驅動關係，以及溫度之四種調整途徑（箭頭、長按、滑桿跳值／語音、滑桿把手），六個 037 leaf 逐一對應，一葉一 TC（§8.2.1）。關鍵情境條件：可觀察量落於 climate screen 之溫度滑桿與 TEMP popup，依 **R-C34** 補第十三軸與 EMEA ICS 之排除；-01／-02 另取第二軸，其事實出處為 **2.11**「Sync is not shown for single zone climate configurations」，依 R-C29 標 (2.11) 並併入 specification_reference。**與 2.11 之 sibling 關係**：2.11（`Climate Modes` 組，尚未生成）亦述「changing the driver temperature automatically changes the passenger temperature」與「Adjusting the passenger temperature … would break SYNC」，與本節 -01／-02 為同一行為之兩處陳述；依 §8.2 單位歸 037，本節之 leaf 為 `SWE1-HVAC-009-01`／`-02`，`duplicate_of` 因 2.11 尚無列號而暫空，該組生成時須依 §4.6 回填（見上繳 24 §6）。為什麼這樣切：四種調整途徑之操作元件互異，失效可各自發生。刻意略過：語音命令之辨識行為屬他份文件，本節只驗其結果為溫度跳至該值（§8.2.1）。",
        "keywords": ["SYNC", "driver temperature", "passenger temperature",
                     "slider", "long press", "voice command"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-009-01",
                "tc_title": "Driver temperature drives passenger temperature when SYNC is on",
                "test_item":
                    "If SYNC is ON, adjusting the driver temperature shall "
                    "affect the passenger temperature",
                "pre_conditions": PC_DUAL,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn SYNC on\n"
                    "2. Change the driver temperature",
                "expected_result":
                    "1. SYNC is on\n"
                    "2. The passenger temperature changes with the driver "
                    "temperature",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-009-02",
                "tc_title": "Adjusting the passenger temperature breaks SYNC",
                "test_item":
                    "Adjusting the passenger temperature shall break SYNC and "
                    "turn it off",
                "pre_conditions": PC_DUAL,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn SYNC on\n"
                    "2. Change the passenger temperature",
                "expected_result":
                    "1. SYNC is on\n"
                    "2. SYNC is off",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-009-03",
                "tc_title": "Arrow press moves the temperature by one increment",
                "test_item":
                    "The user shall be able to change the temperature on the "
                    "climate screen by using arrows, which shall move 1 "
                    "increment up or down per press",
                "pre_conditions": "1. [spec-derived] The climate screen "
                                  "provides temperature arrows (2.6.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Press the temperature up arrow once\n"
                    "3. Press the temperature down arrow once",
                "expected_result":
                    "1. The climate screen shows the current temperature\n"
                    "2. The temperature moves up by 1 increment\n"
                    "3. The temperature moves down by 1 increment",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-009-04",
                "tc_title": "Long press gives a fast move on screen and hard controls",
                "test_item":
                    "Long press shall be a fast move, and long press as a fast "
                    "move shall also work for temperature HARD CONTROLS",
                "pre_conditions": "1. [spec-derived] The climate screen "
                                  "provides temperature arrows (2.6.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Long-press the temperature up arrow on the climate "
                    "screen\n"
                    "2. Long-press the temperature hard control",
                "expected_result":
                    "1. The temperature changes with a fast move\n"
                    "2. The temperature changes with a fast move",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-009-05",
                "tc_title": "Temperature jumps to a value by slider touch or voice",
                "test_item":
                    "The system shall be able to jump to a value via touching "
                    "a spot in a slider bar or voice command",
                "pre_conditions": "1. [spec-derived] The climate screen "
                                  "provides a temperature slider (2.6.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Touch a spot in the temperature slider bar\n"
                    "2. Set the temperature to a value by voice command",
                "expected_result":
                    "1. The temperature jumps to the value at the touched "
                    "spot\n"
                    "2. The temperature jumps to the value given by voice "
                    "command",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-009-06",
                "tc_title": "Only the slider handle moves the slider position",
                "test_item":
                    "The user must press the slider handle to move the "
                    "temperature slider position, and if the user initially "
                    "presses the slider area outside of the handle the press "
                    "shall be ignored",
                "pre_conditions": "1. [spec-derived] The climate screen "
                                  "provides a temperature slider (2.6.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the temperature slider handle and move it\n"
                    "2. Press the slider area to the left of the slider handle",
                "expected_result":
                    "1. The temperature slider position moves\n"
                    "2. The press is ignored and the temperature slider "
                    "position does not change",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    # ----------------------------------------------------------------- 2.7
    {
        "parent": "SWE1-HVAC-010",
        "outline": "2.7",
        "reasoning":
            "驗證目標：2.7（C6）定出風量之範圍與呈現位置、非 climate screen 時之 popup、climate screen 上之三種調整途徑，以及「風量不可手動關至全暗」此一限制與其唯一例外，五個 037 leaf 逐一對應，一葉一 TC（§8.2.1）。關鍵情境條件：可觀察量落於 TS climate screen 與 main category control，依 **R-C34** 補第十三軸與 EMEA ICS 之排除；**-01 另補第九軸** —— 其讀 main category control，而 6.3 使 comfort section 自 head unit 移除，故該介面可能不存在，標 (6.3) 並併入 specification_reference；其餘四條之可觀察量在 climate screen 與 popup，不受第九軸影響。為什麼這樣切：三種調整途徑與兩項限制之失效互相獨立。刻意略過：條文之 `15h` 標示 AUTO 一項語意不明（未見於他節），本批不驗，僅驗 Off 與 1-7 之呈現；-02 與 `NR1L-ComfortHMI-033`（2.2 之 popup）形態相近而 leaf 不同，依 §8.2 各自成條，本條之主詞為風量、該條為一般性狀態變更；**A-CF23 之逐條複查（42 §4 之名單重建）**：037 對本 leaf 之描述帶 1 張圖，五條之答**皆為否** —— `fan segment`／`one bar highlighted`／`all FAN bars grayed out`／`main category control`／`pop-up` 五個可觀察量**全部是 C6 自己的字**，ER 未使用任何條文以外之視覺描述。",
        "keywords": ["fan", "main category control", "fan segment",
                     "greyed out", "climate power button"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-010-01",
                "tc_title": "Fan speed shows on the climate screen and category control",
                "test_item":
                    "The fan status shall be indicated on the TS climate "
                    "screen and in the main category control",
                "pre_conditions": "1. [spec-derived] The head unit provides a "
                                  "main category control for climate (2.7)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed\n"
                    "3. Read the main category control",
                "expected_result":
                    "1. The climate screen shows the current fan speed\n"
                    "2. The climate screen shows the new fan speed\n"
                    "3. The main category control shows the new fan speed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-010-02",
                "tc_title": "Fan pop-up appears off the climate screen",
                "test_item":
                    "The system shall show a pop-up when the fan status is "
                    "changed via hard control and the currently shown screen "
                    "is not the climate screen",
                "pre_conditions": "1. [spec-derived] The vehicle has a fan "
                                  "speed hard control (2.7)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen other than the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control",
                "expected_result":
                    "1. The climate screen is not displayed\n"
                    "2. A fan pop-up is shown",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-010-03",
                "tc_title": "Fan is adjustable by buttons touch or slide on screen",
                "test_item":
                    "When on climate screen, the user shall be able to either "
                    "use the Fan up/down buttons, directly touch a fan segment "
                    "to jump, or slide",
                "pre_conditions": "1. [spec-derived] The climate screen "
                                  "provides fan up and down buttons and fan "
                                  "segments (2.7)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the fan up button on the climate screen\n"
                    "2. Touch a fan segment on the climate screen\n"
                    "3. Slide across the fan segments on the climate screen",
                "expected_result":
                    "1. The fan speed increases\n"
                    "2. The fan speed jumps to the touched segment\n"
                    "3. The fan speed follows the slide",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-010-04",
                "tc_title": "Fan cannot be turned off from the screen or hard control",
                "test_item":
                    "The user shall not be able to turn the FAN off by using "
                    "the FAN controls on the screen or the FAN hard control, "
                    "and there shall always be one bar highlighted",
                "pre_conditions": "1. [spec-derived] The vehicle has a fan "
                                  "speed hard control (2.7)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the fan down button on the climate screen "
                    "repeatedly until the fan speed stops decreasing\n"
                    "2. Turn the fan speed hard control down repeatedly until "
                    "the fan speed stops decreasing",
                "expected_result":
                    "1. The fan is not off and one fan bar remains "
                    "highlighted\n"
                    "2. The fan is not off and one fan bar remains highlighted",
                "priority": "P1",
                "design_method": DM_BVA,
            },
            {
                "req_id": "SWE1-HVAC-010-05",
                "tc_title": "All fan bars grey out only when the climate system is off",
                "test_item":
                    "The only way to have all FAN bars grayed out shall be by "
                    "shutting the CLIMATE system OFF, using the climate power "
                    "button on the screen or the hard control",
                "pre_conditions": "1. [spec-derived] The vehicle has a climate "
                                  "power hard control (2.7)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn the climate system off using the climate power "
                    "button on the climate screen\n"
                    "2. Turn the climate system on again\n"
                    "3. Turn the climate system off using the climate power "
                    "hard control",
                "expected_result":
                    "1. All FAN bars are greyed out\n"
                    "2. One fan bar is highlighted\n"
                    "3. All FAN bars are greyed out",
                "priority": "P1",
                "design_method": DM_STATE,
            },
        ],
    },
    # ---------------------------------------------------------------- 2.16
    {
        "parent": "SWE1-HVAC-022",
        "outline": "2.16",
        "reasoning":
            "驗證目標：2.16（C18）規定語音辨識期間之自動降風量不對使用者顯示，且結束後回復前一風速亦不顯示變化，兩個 037 leaf 分別對應降低時與回復時，一葉一 TC（§8.2.1）。關鍵情境條件：可觀察量為 climate screen 上之風速顯示，依 **R-C34** 補第十三軸與 EMEA ICS 之排除；第九軸與第十二軸不涉（不讀 category control、不讀 tab），具名於此。為什麼這樣切：降低時不顯示與回復時不顯示為兩個時點之兩個獨立可失效行為 —— 降低時正確而回復時閃動，或反之，皆可能發生。**-02 之 EMEA 排除式 PC 與 16.2 引用已依 39 §1.1 移除** —— 16.17 全文僅一句（降風量不顯示），**不含 C18 之第二句「After blower reduction, return blower speed to previous speed without showing a change in fan speed」**，故本條所驗之回復行為於 ch16 無對應句；-01 之排除維持。刻意略過：語音辨識會話之觸發與降風量之幅度屬他處，本節只規定其「不顯示」，故 procedure 以「造成降風量之語音辨識會話」為步驟而不驗其辨識行為（§8.2.1）；條文未給降風量之數值，ER 不寫入任何幅度（R-C22）。",
        "keywords": ["blower reduction", "Voice Recognition", "fan speed",
                     "not displayed"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-022-01",
                "tc_title": "Automatic blower reduction is not shown to the user",
                "test_item":
                    "If blower reduction occurs automatically due to an active "
                    "Voice Recognition session, the change in fan speed shall "
                    "not be displayed to the user",
                "pre_conditions": "1. [spec-derived] The vehicle supports "
                                  "Voice Recognition sessions that cause "
                                  "automatic blower reduction (2.16)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen and read the fan speed\n"
                    "2. Start a Voice Recognition session that causes blower "
                    "reduction",
                "expected_result":
                    "1. The climate screen shows the current fan speed\n"
                    "2. The fan speed shown on the climate screen does not "
                    "change",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-022-02",
                "tc_title": "Blower returns to the previous speed without showing a change",
                "test_item":
                    "After blower reduction, the system shall return the "
                    "blower speed to the previous speed without showing a "
                    "change in fan speed",
                "pre_conditions": "1. [spec-derived] The vehicle supports "
                                  "Voice Recognition sessions that cause "
                                  "automatic blower reduction (2.16)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Start a Voice Recognition session that causes blower "
                    "reduction\n"
                    "2. End the Voice Recognition session",
                "expected_result":
                    "1. The fan speed shown on the climate screen does not "
                    "change\n"
                    "2. The blower returns to the previous speed and the fan "
                    "speed shown on the climate screen does not change",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    # --------------------------------------------------------------- 2.7.1
    {
        "parent": "SWE1-HVAC-011",
        "outline": "2.7.1",
        "reasoning":
            "驗證目標：2.7.1（C6.1）規定部分車輛之前排 HVAC 風速範圍為 Off, 1-8，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：取 profile §3.2 **第十四軸「前排 HVAC 風速範圍」**（37 §4 增列），其 R-C28 第一問由本節明文「In some vehicles fan speed ranges for front hvac are: Off, 1-8」對應，標 spec-verbatim；對照值 Off, 1-7 出自 2.7（C6.），依 R-C29 標 (2.7) 並併入 specification_reference —— C6.1 為 C6. 之子條，合讀非推論。依 **R-C34** 可觀察量為 climate screen 之風速段，補第十三軸與 EMEA ICS 之排除（16.7 ICE6 mirrored），第九軸與第十二軸不涉；本節只定出一個值域，無分支可分，且**第十四軸為功能型**，兩值皆不移除介面。刻意略過：條文未述「some vehicles」係由何配置決定，故 PC 以該值域本身為陳述而不寫入其成因（§8.4.1）；亦未述 1-8 之車輛其 AUTO 標示或下界行為是否不同，不擴張；**EMEA 排除式 PC 與 16.2 引用已依 39 §1.1 移除**，因 ICE6 只列「Fan ranges: Off, 1-7」，本條所驗之 Off, 1-8 於 ch16 無對應句（鏡射表亦記 2.7.1 為 no-counterpart）。",
        "keywords": ["fan speed range", "front hvac", "Off, 1-8",
                     "Off, 1-7"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-011",
                "tc_title": "Front HVAC fan range runs to 8 on vehicles configured for it",
                "test_item":
                    "In some vehicles the fan speed ranges for front hvac "
                    "shall be Off, 1-8",
                "pre_conditions":
                    "1. [spec-verbatim] The vehicle's front hvac fan speed "
                    "range is Off, 1-8 (2.7.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Raise the fan speed until it stops increasing\n"
                    "3. Read the number of fan segments on the climate screen",
                "expected_result":
                    "1. The climate screen shows the current fan speed\n"
                    "2. The fan speed reaches 8\n"
                    "3. The climate screen shows 8 fan segments",
                "priority": "P2",
                "design_method": DM_BVA,
                "spec_ref": ("2.7.1", "2.7"),
            },
        ],
    },
]

# 37 §4 lifted the hold: the fourteenth axis is now in profile §3.2, so
# 2.7.1 generates and nothing is withheld from this Test Set.
WITHHELD = []


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
            ex, refs = [EX_ICS], list(tc.get("spec_ref", (o,))) + ["2.14"]
            if tc["req_id"] not in EMEA_REMOVED_REQ_IDS:
                ex.append(EX_EMEA)
                refs.append("16.2")
            if "(2.11)" in tc["pre_conditions"]:
                refs.append("2.11")
            if tc["req_id"] in LOWER_EXPOSED:
                ex.append(EX_LOWER)
                refs.append("6.3")
            tcs.append({
                "req_id": tc["req_id"],
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": tc["tc_title"],
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": tc["test_item"],
                "pre_conditions": add_exclusions(tc["pre_conditions"], *ex),
                "input_test_data": tc["input_test_data"],
                "test_procedure": tc["test_procedure"],
                "expected_result": tc["expected_result"],
                "specification_reference": "; ".join(
                    f"{STEM}_{x}" for x in dict.fromkeys(refs)),
                "priority": tc["priority"],
                "design_method": tc["design_method"],
                "split_flag": tc.get("split_flag", False),
                "split_reason": tc.get("split_reason", ""),
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
                **({"emea_ics_review": EMEA_PER_TC[_tid]}
                   if (_tid := TC_ID_FMT.format(n=n)) in EMEA_PER_TC else {}),
            })
        doc = {
            "parent": b["parent"],
            "outline": o,
            "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": b["reasoning"],
            "keywords": b["keywords"],
            "duplicate_of": "",
            "distinguishing_axis": b.get(
                "distinguishing_axis",
                {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [],
            "interface_axis_review": INTERFACE_AXIS_REVIEW[o],
            "tcs": tcs,
        }
        (OUT / f"{b['parent']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{b['parent']}  {o:8} {len(tcs)} TC  -> generated/{b['parent']}.json")

    leaves = len({tc["req_id"] for b in BATCHES for tc in b["tcs"]})
    print(f"\n{leaves} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print("\nWITHHELD — stop-and-report, no row produced:")
    for o, parent, k, why in WITHHELD:
        print(f"- {o} ({parent}, {k} leaf): {why}")
    held = sum(k for _, _, k, _ in WITHHELD)
    print(f"\n{leaves} emitted + {held} withheld = {leaves + held} leaves "
          f"declared for {TEST_SET} (framework.md: 19)")
    if leaves + held != 19:
        raise SystemExit(f"expected 19 leaves declared, got {leaves + held}")
    if total != 19:
        raise SystemExit(f"expected 19 TCs, emitted {total}")


if __name__ == "__main__":
    main()
