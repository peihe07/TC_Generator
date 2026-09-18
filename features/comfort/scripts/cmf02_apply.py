#!/usr/bin/env python3
"""CMF-02 §1–§3 之 JSON 層 —— patch、裁定回灌與 sibling（下放包 CMF-02／CMF-02_A）。

套用對象為 `generated/*.json`，內容依序：

  R-C47          465 條 priority 依 0907 本 P 欄回灌（經 write_back.row_plan 對位）
  R-C6(amend)    test_group 一律 `Climate Control Interface`
  M8             三條 test_set 依 framework Part N
  M2             103-01／103-02 改為「timeout 前再按」，**不用 `3 seconds`**
  M6             四條之 CCM 步驟改為整行 `PENDING: DR-46 …`
  M9-Note        25 步 `Note` → `Read … and record it`
  M9-compound    35 行雙動作拆步，ER 同步補行維持 1:1
  R-C50          26 條上半摘為該句之連續子字串（≤ 50 token）
  R-C52          wb-001～004 之 Remarks conflict 句
  R-C51          019-03 之 [BLOCKED-SPEC] 列（tc_id -466）
  §3             sibling（R-C44 三問逐條答後實產者，自 -467 起）

**一次性**：每一處改寫皆先斷言其被取代之原值，第二次執行會在第一處斷言
即中止，不會重複套用。下半（test_item 之括號）只在末步或末行 ER 改變時
重算（`test_item.situation()`），其餘不動。

產出 `docs/reports/cmf02_json_change_log.tsv`（tc_id／field／item／before／after）
供候選本之逐格對帳歸因。

Usage:
    python3 features/comfort/scripts/cmf02_apply.py            # 套用
    python3 features/comfort/scripts/cmf02_apply.py --dry-run  # 只驗斷言、不寫檔
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as W                                   # noqa: E402
from test_item import situation                          # noqa: E402

FEATURE = W.FEATURE
GEN = W.GEN
REPORTS = FEATURE / "docs" / "reports"
BASE_0907 = FEATURE / "delivered" / (
    "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
    "Specification & Result_SWQT_ComfortHMI_20260907.xlsx")
TEST_GROUP = "Climate Control Interface"                 # R-C6(amend)


def T(n: int) -> str:
    return f"NR1L-ComfortHMI-{n:03d}"


# ------------------------------------------------------------------ M8
TEST_SET_FIX = {T(434): ("HVAC Pop-ups", "Climate Popups"),
                T(432): ("EMEA ICS Interface", "ICS Climate Modes"),
                T(433): ("EMEA ICS Interface", "ICS Climate Modes")}

# ------------------------------------------------------ 步驟級之改寫
# ("step", k, 原步驟, [(新步驟, 新 ER 或 KEEP), …])   k 為**原**行號
#   以新行取代第 k 步及其 ER；清單為空即刪去該步。KEEP 表示該行 ER 沿用原值。
# ("er", k, 原 ER, 新 ER)       只改第 k 行 ER（k 為拆步**之後**之行號）
# ("set", field, 原值, 新值)    整欄取代（M2 用）
KEEP = object()


def note(obj: str, pron: str = "it") -> str:
    """M9-Note：`Note X` → `Read X and record it`（CMF-02 §2，canon §5.6）。"""
    return f"Read {obj} and record {pron}"


FAN_HC = "Change the fan speed using the fan speed hard control"

STEP_EDITS = {
    # ---- M2（CMF-02 §2 之骨架；5 s 之錨取自條文，再按時點不造值）--------
    T(191): [
        ("set", "test_procedure",
         "1. Press the driver comfort seat icon in the status bar\n"
         "2. Wait 5 seconds without further interaction",
         "1. Press the driver comfort seat icon in the status bar\n"
         "2. Press the driver comfort seat icon again before the popup times out\n"
         "3. Wait until 5 seconds have passed since the press in step 1"),
        ("set", "expected_result",
         "1. A popup for the comfort feature is shown\n"
         "2. The popup is no longer shown",
         "1. A popup for the comfort feature is shown\n"
         "2. The popup is still shown\n"
         "3. The popup is still shown"),
    ],
    T(192): [
        ("set", "test_procedure",
         "1. Press the driver comfort seat icon in the status bar\n"
         "2. Wait 5 seconds without further interaction",
         "1. Press the driver comfort seat icon in the status bar\n"
         "2. Press the driver comfort seat icon again before the popup times out\n"
         "3. Wait 5 seconds after the press in step 2 without further interaction"),
        ("set", "expected_result",
         "1. A popup for the comfort feature is shown\n"
         "2. The popup is no longer shown",
         "1. A popup for the comfort feature is shown\n"
         "2. The popup is still shown\n"
         "3. The popup is no longer shown"),
    ],
    # ---- M6 —— 該步整行 PENDING；值以 "…" 呈現（`[…]` 會觸 ui-bracket）------
    T(141): [("step", 1, "Set the recirc availability status from the CCM to unavailable",
              [('PENDING: DR-46 DBC message and raw value for $RECIRC_STAT$ = '
                '"not available/Blink"', KEEP)])],
    # wb-069：原第 2 步為「設定 ＋ 讀取」，整行 PENDING 會吞掉讀取，故讀取另成一步
    # （形同 wb-033 之結構，PENDING 步之 ER 取該結構之同一句）
    T(158): [("step", 2, 'Set the recirc availability status from the CCM to '
                         'unavailable and read the "RECIRC" button',
              [('PENDING: DR-46 DBC message and raw value for $RECIRC_STAT$ = '
                '"not available/Blink"', "The climate screen is displayed"),
               ('Read the "RECIRC" button on the climate screen', KEEP)])],
    T(160): [("step", 1, "Set the rear defrost availability status from the CCM to unavailable",
              [('PENDING: DR-46 DBC message and raw value for $EBL_Stat$ = '
                '"not available/Blink"', KEEP)])],
    T(250): [("step", 1, "Set the rear defrost availability status from the CCM to unavailable",
              [('PENDING: DR-46 DBC message and raw value for $EBL_Stat$ = '
                '"not available/Blink"', KEEP)])],
    # ---- M9-compound（M9-Note 同列者併於此）-------------------------------
    T(130): [("step", 1, "Select an airflow mode and turn front defrost on from the climate screen",
              [("Select an airflow mode on the climate screen", "The selected airflow mode is active"),
               ("Turn front defrost on from the climate screen", '"FRONT DEF" is active')])],
    T(147): [("step", 1, "Note the fan speed, then turn the climate system off using "
                         "the climate power button on the climate screen",
              [(note("the fan speed on the climate screen"), "The climate screen shows the current fan speed"),
               ("Turn the climate system off using the climate power button on the climate screen",
                "The CLIMATE OFF screen is displayed")]),
             ("er", 3, "The climate system is on and the fan speed is at the level noted",
              "The climate system is on and the fan speed is at the level recorded in step 1")],
    T(454): [("step", 1, "Open a screen other than Climate main and press the Mode hard control once",
              [("Open a screen other than Climate main", "The Climate main screen is not displayed"),
               ("Press the Mode hard control once", KEEP)])],
    T(455): [("step", 1, "Open a screen other than Climate main and press the Mode hard control once",
              [("Open a screen other than Climate main", "The Climate main screen is not displayed"),
               ("Press the Mode hard control once", KEEP)])],
    T(275): [("step", 3, "Turn rear AUTO on again and press a specific rear airflow mode button",
              [("Turn rear AUTO on again", "The rear AUTO button is highlighted"),
               ("Press a specific rear airflow mode button", KEEP)])],
    T(400): [("step", 1, 'Press "LOCK REAR", then press "UNLOCK REAR"',
              [('Press "LOCK REAR"', "The rear climate is locked"),
               ('Press "UNLOCK REAR"', KEEP)])],
    T(368): [("step", 1, "Trigger the fan speed pop up and press the Front Fan area",
              [("Trigger the fan speed pop up", "The fan speed pop up is displayed"),
               ("Press the Front Fan area", KEEP)]),
             ("step", 2, "Trigger the fan speed pop up and press the Rear fan area",
              [("Trigger the fan speed pop up", "The fan speed pop up is displayed"),
               ("Press the Rear fan area", KEEP)])],
    # 048-03：第 4 步拆步（其 sibling 依 R-C44 三不產，見 SIBLING_NOT_PRODUCED）
    T(73): [("step", 4, "Press the AUTO button until the AUTO ECO mode is active, "
                        "then change the airflow mode",
             [("Press the AUTO button until the AUTO ECO mode is active", "The AUTO state is AUTO ECO"),
              ("Change the airflow mode", KEEP)])],
    # 052：原「press once」於風速硬鍵已破 AUTO 之後，其落點不定 —— 改用
    # `until … AUTO ON` 之既有形（048-02），使拆出之 ER 只陳述該步自身之結果
    T(78): [("step", 1, "Press the AUTO button until the AUTO ECO mode is active, "
                        "then change the fan speed using the fan speed hard control",
             [("Press the AUTO button until the AUTO ECO mode is active", "The AUTO state is AUTO ECO"),
              (FAN_HC, KEEP)]),
            ("step", 2, "Press the AUTO button once, then change the fan speed using "
                        "the fan speed hard control",
             [("Press the AUTO button until the AUTO ON state is active", "The AUTO state is AUTO ON"),
              (FAN_HC, KEEP)])],
    T(334): [("step", 3, "Display the popup again and select an item in it",
              [("Display the popup again", "The popup is displayed"),
               ("Select an item in the popup", KEEP)])],
    T(173): [("step", 1, "Open a NAV screen and change the fan speed using the fan speed hard control",
              [("Open a NAV screen", "The NAV screen is displayed"), (FAN_HC, KEEP)]),
             ("step", 2, "Open a Projection screen and change the fan speed using the fan speed hard control",
              [("Open a Projection screen", "The Projection screen is displayed"), (FAN_HC, KEEP)])],
    T(174): [("step", 1, "Open a pop-up, then change the fan speed using the fan speed hard control",
              [("Open a pop-up", "The pop-up is displayed"), (FAN_HC, KEEP)])],
    T(175): [("step", 1, "Open a pop-up that has a selectable item, then change the fan "
                         "speed using the fan speed hard control",
              [("Open a pop-up that has a selectable item", "The pop-up is displayed"), (FAN_HC, KEEP)])],
    T(176): [("step", 1, "Open a pop-up that has a selectable item, then change the fan "
                         "speed using the fan speed hard control",
              [("Open a pop-up that has a selectable item", "The pop-up is displayed"), (FAN_HC, KEEP)])],
    T(177): [("step", 1, "Open a pop-up, then change the fan speed using the fan speed hard control",
              [("Open a pop-up", "The pop-up is displayed"), (FAN_HC, KEEP)])],
    T(179): [("step", 2, "Put the head unit into simulated off/idle mode and change the fan speed again",
              [("Put the head unit into simulated off/idle mode",
                "The head unit is in simulated off/idle mode"),
               ("Change the fan speed again", KEEP)])],
    T(184): [("step", 1, "Turn the driver heated seat on, then turn it off",
              [("Turn the driver heated seat on", "The driver heated seat is on"),
               ("Turn the driver heated seat off", KEEP)])],
    T(384): [("step", 1, 'Turn "FRONT DEF" on and set the airflow mode and the fan speed to known values',
              [('Turn "FRONT DEF" on', '"FRONT DEF" is active'),
               ("Set the airflow mode and the fan speed to known values", KEEP)])],
    T(385): [("step", 1, 'Turn "FRONT DEF" on and set the fan speed to a value that differs '
                         'from the one in the example graphic',
              [('Turn "FRONT DEF" on', '"FRONT DEF" is active'),
               ("Set the fan speed to a value that differs from the one in the example graphic", KEEP)]),
             ("er", 3, "The HVAC pop-up shows the fan speed set in step 1",
              "The HVAC pop-up shows the fan speed set in step 2")],
    T(87): [("step", 1, "Set the temperature units to Celsius and open a screen outside "
                        "the climate main category",
             [("Set the temperature units to Celsius", "The temperature units are Celsius"),
              ("Open a screen outside the climate main category", KEEP)])],
    T(98): [("step", 1, "Set the temperature units to English and open the climate screen",
             [("Set the temperature units to English", "The temperature units are English"),
              ("Open the climate screen", KEEP)])],
    T(413): [("step", 1, "Set the temperature units to Metric and open the climate screen",
              [("Set the temperature units to Metric", "The temperature units are Metric"),
               ("Open the climate screen", KEEP)])],
    T(237): [("step", 1, 'Turn "A/C" off and select an airflow mode other than Windshield on the climate screen',
              [('Turn "A/C" off on the climate screen', 'The "A/C" button is not highlighted'),
               ("Select an airflow mode other than Windshield on the climate screen",
                "The selected airflow mode is active")])],
    T(243): [("step", 1, 'Select a known airflow mode on the climate screen, then press "MAX DEF"',
              [("Select a known airflow mode on the climate screen", "The selected airflow mode is active"),
               ('Press "MAX DEF"', KEEP)])],
    T(245): [("step", 1, 'Select a known airflow mode, then press "MAX DEF"',
              [("Select a known airflow mode", "The selected airflow mode is active"),
               ('Press "MAX DEF"', KEEP)])],
    T(421): [("step", 1, 'Select a known airflow mode, then press "MAX DEF"',
              [("Select a known airflow mode", "The selected airflow mode is active"),
               ('Press "MAX DEF"', KEEP)])],
    T(422): [("step", 1, 'Select a known airflow mode, then press "MAX DEF"',
              [("Select a known airflow mode", "The selected airflow mode is active"),
               ('Press "MAX DEF"', KEEP)])],
    T(246): [("step", 1, 'Select a known airflow mode, then press "MAX DEF"',
              [("Select a known airflow mode", "The selected airflow mode is active"),
               ('Press "MAX DEF"', KEEP)])],
    T(233): [("step", 1, 'Set a known airflow mode and temperature, then press "MAX A/C"',
              [("Set a known airflow mode and temperature",
                "The climate screen shows the airflow mode and temperature set"),
               ('Press "MAX A/C"', KEEP)])],
    T(234): [("step", 1, 'Set a known airflow mode, then press "MAX A/C"',
              [("Set a known airflow mode", "The selected airflow mode is active"),
               ('Press "MAX A/C"', KEEP)])],
    T(97): [("step", 1, "Turn one seat control on and another seat control off, then leave the controls screen",
             [("Turn one seat control on and another seat control off",
               "The controls screen shows one seat control active and the other inactive"),
              ("Leave the controls screen", KEEP)])],
    T(118): [("step", 1, "Move the Comfort widget to its second screen and leave the home screen",
              [("Move the Comfort widget to its second screen", "The Comfort widget shows its second screen"),
               ("Leave the home screen", KEEP)])],
    # ---- 002-01：wb-006 第 3 步依 sibling plan 刪（TS→HC 向由 002-08 承接）----
    T(32): [("step", 3, "Change the temperature on the climate screen", [])],
}

# M9-Note（除上列已併處理之 T(147)）：tc -> (第 k 步, 原句, 新句)
NOTE_EDITS = {
    T(131): (1, 'Note the state of the "A/C" button on the climate screen with AUTO off',
             note('the state of the "A/C" button on the climate screen with AUTO off')),
    T(57): (1, "Note the temperature shown on the climate screen",
            note("the temperature shown on the climate screen")),
    T(391): (1, "Note the temperature shown on the climate screen",
             note("the temperature shown on the climate screen")),
    T(58): (1, "Note the temperature slider position", note("the temperature slider position")),
    T(61): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(393): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(394): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(62): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(395): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(155): (1, "Note the fan speed on the climate screen", note("the fan speed on the climate screen")),
    T(1): (1, "Note which tab is currently shown on the lower screen",
           note("which tab is currently shown on the lower screen")),
    T(3): (1, "Note which tab is currently shown in the climate section on the head unit",
           note("which tab is currently shown in the climate section on the head unit")),
    T(106): (1, "Note the temperature shown on the climate screen", note("the temperature shown on the climate screen")),
    T(414): (1, "Note the temperature shown on the climate screen", note("the temperature shown on the climate screen")),
    T(415): (1, "Note the temperature shown on the climate screen", note("the temperature shown on the climate screen")),
    T(416): (1, "Note the temperature slider position", note("the temperature slider position")),
    T(112): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(417): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(418): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(419): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(113): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(420): (1, "Note the fan speed shown on the climate screen", note("the fan speed shown on the climate screen")),
    T(252): (1, "Note the size and highlight of the Feet airflow mode button",
             note("the size and highlight of the Feet airflow mode button", "them")),
    T(262): (1, "Note the main category label on the climate screen",
             note("the main category label on the climate screen")),
}

# 下半之手寫者（合成器只讀末步；M2 之分別在中段）
LOWER_OVERRIDE = {
    T(191): "(press the icon again before the timeout -> the timeout restarts)",
    T(192): "(press the icon again before the timeout -> the popup stays for "
            "another 5 seconds, then closes)",
}

# ------------------------------------------------------------ R-C50
# 上半 > 50 token 者摘為該句之連續子字串（取與下半直接相關之段）。
# 104-0x 之條文於 SYS1 export 中帶字面 `\n`（非換行），摘句照錄。
_S_002 = ("a pop-up will be shown coming down from that "
          "temperature in the status bar to indicate it is being altered, for ATC it will "
          "display the degree (or half degree increments for Celsius and for Fahrenheit do "
          "not show half degrees) being set")
_S_106 = ("If the user is outside of the climate main category and the temperature is "
          "changed through hard controls, a pop-up will be shown coming down from that "
          "temperature in the status bar to indicate it is being altered")
_S_104H = ("HVACSB6.) When the Climate widget is shown on the currently displayed screen and "
           "the user interacts with climate controls, either soft or hard, pop ups will "
           "behave as follows:\\n-Temperature Pop-up: only on status bar (do not show drop "
           "down menu)")
_S_118A = ("When the Mode hard control is pressed, if the user is on Climate main the new "
           "mode button will be shown highlighted.")
_S_118B = ("if the user is not on Climate main when pressing the Mode hard control a small "
           "pop -up will appear above the Climate main category control")
_S_118C = ("a small pop -up will appear above the Climate main category control (timeout "
           "after 3 seconds of inactivity or as soon as another button except Mode HC is "
           "pressed)")
_S_118D = ("a small pop -up will appear above the Climate main category control (timeout "
           "after 3 seconds of inactivity or as soon as another button except Mode HC is "
           "pressed), the user will not be shifted to climate main.")
_S_018A = ("a small pop-up will appear above the Climate main category control (timeout "
           "after 3 seconds of inactivity or as soon as another button except Mode HC is "
           "pressed), the user will not be shifted to climate main.")
_S_018B = ("a small pop-up will appear above the Climate main category control (timeout "
           "after 3 seconds of inactivity or as soon as another button except Mode HC is "
           "pressed)")
UPPER_EXCERPT = {
    T(36): _S_002,
    T(37): _S_002,
    T(38): ("for MTC (if the MTC has a Climate screen) it will display a slider bar with the "
            "arrow pointing to the current setting, this information will change as the user "
            "alters the temp."),
    T(86): _S_106,
    T(87): ("a pop-up will be shown coming down from that temperature in the status bar to "
            "indicate it is being altered, for ATC it will display the degree (or half degree "
            "increments for Celsius) being set"),
    T(88): ("for MTC it will display a slider bar with the arrow pointing to the current "
            "setting, this information will change as the user alters the temp."),
    T(193): _S_104H,
    T(194): "-FAN Speed Pop-up: show for R1Low, do not show for R1H.",
    T(195): "-Air Flow Mode (distribution) Pop-up: do not show (feedback is already on widget)",
    T(196): "-Climate On/Off Pop-up: do not show (feedback is already on widget)",
    T(197): "-Auto Pop-up: do not show (feedback is already on widget)",
    T(198): "-Heated Seats Pop-up: only on status bar (do not show drop down menu)",
    T(199): "-Vented Seats Pop-up: only on status bar (do not show drop down menu)",
    T(200): "-Heated Steering Wheel Pop-up: only on status bar (do not show drop down menu)",
    T(254): ("ICE11.1) If the Mode hard control is pressed the user will be moved to the next "
             "mode available in the loop (Face > Face/Feet > Feet > Feet/Windshield > "
             "Windshield), the user will be shifted with each press"),
    T(255): ("the user will be shifted with each press, press and hold of the control will only "
             "move one mode over, it will not continue to move through modes."),
    T(256): _S_118A,
    T(257): _S_118A,
    T(258): _S_118B,
    T(259): _S_118B,
    T(260): _S_118C,
    T(426): _S_118C,
    T(261): _S_118D,
    T(453): _S_018A,
    T(454): _S_018B,
    T(455): _S_018B,
}
UPPER_MAX_TOKENS = 50

# ------------------------------------------------------------ R-C52
# 條文（SR24 2.1）寫 4 tabs 含 Massage，037 寫 up to 3 tabs 而無 Massage。
# 登錄簿之值取**本列之區辨片段**（68 §2），故四列之句尾各異。
_CONFLICT = ("The Comfort HMI specification allows up to 4 tabs including Massage, while "
             "the software requirement for this case allows up to 3 tabs and does not "
             "list Massage. ")
_CONFLICT_ORDER = ("The Comfort HMI specification orders the tabs Front, Seats, Massage, "
                   "Rear, while the software requirement for this case lists Front, Seats, "
                   "Rear without Massage. ")
REMARKS_C52 = {
    T(435): (_CONFLICT + "This case checks the specification's upper limit of 4 tabs.",
             "upper limit of 4 tabs"),
    T(436): (_CONFLICT + "This case checks 3 tabs drawn from the specification's four "
             "areas, which may include Massage.", "checks 3 tabs drawn from"),
    T(437): (_CONFLICT + "This case checks 2 tabs drawn from the specification's four "
             "areas, which may include Massage.", "checks 2 tabs drawn from"),
    T(438): (_CONFLICT_ORDER + "This case checks the specification's order, including "
             "Massage.", "specification's order, including Massage"),
}

# ------------------------------------------------------------ R-C51
BLOCKED_019_03 = {
    "tc_title": "MAX A/C on/off logic follows the VF HVAC document",
    "upper": "On/Off logic should follow requirements from VF HVAC document.",
    "remarks": ("[BLOCKED-SPEC] Owner: VF HVAC document — the MAX A/C on/off logic is "
                "defined there; with that delegation removed this requirement has no "
                "content verifiable against the Comfort HMI specification alone. No test "
                "case in this delivery covers that logic."),
    # 無同 leaf 既有 TC 可取級（R-C47 之 sibling 規則不及於此）。取三條既有
    # [BLOCKED-SPEC] 列之形態：0907 本中皆低其同 parent 之可測 leaf 一級
    # （080-02 P1 vs 080-01 P0；081-02 P1；072 P2），019-01／-02 為 P0 → P1。
    "priority": "P1",
    "authored": "The On/Off logic of MAX A/C shall follow the requirements of the VF HVAC document",
    # R-C36-1 —— 本列之 PC 帶 EMEA 排除（取自 019-01），故須逐條答
    "emea_ics_review": {
        "ch16_outline": "16.13",
        "ch16_sentence": ("C14 把 MAX A/C 之 On/Off 邏輯委派予 VF HVAC document，ICE12 則於 "
                          "ch16 逐項列出其參數與退出途徑 —— 兩側之涵蓋範圍不同，故本列之 EMEA "
                          "排除為過嚴側（R-C36-1，同 `019-02`）；本列為 [BLOCKED-SPEC]，不以 "
                          "ICE12 補其內容（§8.2.1）"),
        "verdict": "no"},
}
TC_ID_019_03 = T(466)
SIBLING_FIRST_ID = 467

# ------------------------------------------------------------ §3 siblings
# 逐條之 R-C44 三問與停點判讀見 `docs/reports/sibling_plan_cmf02.tsv`。
# 本表只列實產者；src 為同 leaf 之既有 TC（其 PC／spec ref／test_set／
# design_method／emea_ics_review／priority 為 sibling 之起點）。
_SR_BRANCH_A = (
    "§8.2.2 之拆分，依 R-C44 三問：`2.3`（C2）之「When breaking Auto the system will go to the "
    "manual mode that most closely matches the auto mode exited, unless a specific mode button "
    "is pressed」以 `unless` 分出兩個分支；分支 (b)（按下特定模式鍵）由既有一條承載，其模式鍵"
    "為條文之泛稱（`a specific mode button`），故依第一問不再展開；分支 (a) 此前無任何 TC，"
    "其觸發取同節前句所列而非模式鍵者（`Manually selecting A/C` 與 `changing fan speeds`），"
    "條文逐字列舉、各為一種按法、無舉例語 —— 三問皆是，故一觸發一條。"
    "分支 (a) 之落點（`most closely matches`）條文無值，ER 該行為 PENDING（CMF-02 §3）。")
_SR_TEMP_LP = (
    "§8.2.2 之拆分，依 R-C44 三問：`{o}` 之條文以兩句分別點名長按快移之兩個通道 —— "
    "「Change temperature on climate screen by using arrows (… long press = fast move …」與"
    "「Long press = fast move shall also work for temperature HARD CONTROLS」；條文列舉、"
    "兩種按法、非舉例 —— 三問皆是，故一通道一條（CMF-01 sibling plan）。")
_SR_FAN_HC = (
    "§8.2.2 之拆分，依 75 §1 之判準（**條文列舉之項即拆分之維度**）：本節之條文逐字列舉其觸發 —— "
    "「user can either use Fan up/down (minus/plus) buttons, directly touch a fan segment to jump "
    "or slide, or use Hard Control」—— 故一觸發一條；前三者已各有一條，`or use Hard Control` "
    "此前無條（037 之 leaf 文少此項，依 R-C33 內容以條文為準；ICS 側 `112-04` 已有其硬控條）。")
_SR_015_04 = (
    "§8.2.2 之拆分，依 R-C44 三問：「Adjusting Fan speed and Mode will alter the Front and Rear "
    "passengers」逐字列舉兩個觸發（fan speed、mode），各為一種按法、非舉例 —— 三問皆是，"
    "故一觸發一條（CMF-01 sibling plan）；原條之兩個觸發步驟分入兩條。")
_SR_018_05 = (
    "§8.2.2 之拆分，判準為 §5.7 之 scope：「In both cases the main category label will be "
    "updated」之兩個 case 為按 Mode 硬鍵時之兩種起始畫面（Climate main 內／外），兩者之"
    "起點與呈現路徑不同、可各自失效，故各一條（CMF-02 §3 依 CMF-01 sibling plan）。"
    "037 VC 所列之 `press and hold` 回條文判讀屬 `018-03`（長按只移一格），不屬本 leaf，不產。")
_SR_080_01 = (
    "§8.2.2 之拆分，依 R-C44 三問：LS3 之「long press on the hard button (-, +) or on the touch "
    "screen itself」逐字列舉兩個通道，各為一種按法、非舉例 —— 三問皆是，故一通道一條"
    "（CMF-01 sibling plan）。")

PC_ATC = "1. [spec-derived] The vehicle has an ATC climate system, in which AUTO is shown (2.3)"

SIBLINGS = [
    # ---- 003-07 分支 (a) ×2（ER 之落點 PENDING: DR-47）--------------------
    dict(req="SWE1-HVAC-003-07", src=T(133),
         title="Pressing A/C in AUTO goes to the closest manual mode",
         upper=("When breaking Auto the system will go to the manual mode that most closely "
                "matches the auto mode exited, unless a specific mode button is pressed, in "
                "which case the system would go to that mode."),
         proc=["Turn AUTO on from the climate screen", 'Press "A/C"'],
         er=['The "AUTO" button is highlighted',
             "PENDING: DR-47 the manual mode the system goes to when AUTO is broken without a mode button"],
         lower='(press "A/C" -> the system goes to the manual mode that most closely matches '
               'the AUTO mode exited)',
         split_reason=_SR_BRANCH_A),
    dict(req="SWE1-HVAC-003-07", src=T(133),
         title="Changing fan speed in AUTO goes to the closest manual mode",
         upper=("When breaking Auto the system will go to the manual mode that most closely "
                "matches the auto mode exited, unless a specific mode button is pressed, in "
                "which case the system would go to that mode."),
         proc=["Turn AUTO on from the climate screen", "Change the fan speed"],
         er=['The "AUTO" button is highlighted',
             "PENDING: DR-47 the manual mode the system goes to when AUTO is broken without a mode button"],
         lower="(change the fan speed -> the system goes to the manual mode that most closely "
               "matches the AUTO mode exited)",
         split_reason=_SR_BRANCH_A),
    # ---- 009-04 觸控箭頭 ---------------------------------------------------
    dict(req="SWE1-HVAC-009-04", src=T(56),
         title="Long press on the temperature arrow moves fast",
         upper=("Change temperature on climate screen by using arrows (move 1 increment up/down "
                "per press, long press = fast move or slider (TEMP pop-up next to slider when "
                "touching it so that finger does not cover number)."),
         proc=[note("the temperature shown on the climate screen"),
               "Long-press the temperature up arrow on the climate screen"],
         er=["The climate screen shows the current temperature",
             "The temperature changes with a fast move"],
         split_reason=_SR_TEMP_LP.format(o="2.6.1")),
    # ---- 010-03 硬控 ---------------------------------------------------------
    dict(req="SWE1-HVAC-010-03", src=T(61),
         title="The fan hard control changes the fan speed",
         pc=("1. [spec-derived] The vehicle has a fan speed hard control (2.7)\n"
             "2. [spec-derived] The vehicle does not have 3 knob HVAC controls with ICS, for "
             "which no HVAC screens or pop ups are displayed (2.14)\n"
             "3. [spec-derived] The vehicle is not an EMEA ICS vehicle, whose climate interface "
             "is specified separately in chapter 16 (16.2)"),
         proc=[note("the fan speed shown on the climate screen"), FAN_HC],
         er=["The climate screen shows the current fan speed", "The fan speed follows the hard control"],
         split_reason=_SR_FAN_HC),
    # ---- 015-04 風速 ---------------------------------------------------------
    dict(req="SWE1-HVAC-015-04", src=T(430),
         title="Changing the fan speed alters front and rear passengers",
         proc=['Turn "SYNC" on from the climate screen', "Change the fan speed from the climate screen"],
         er=['The "SYNC" button is highlighted',
             "The fan speed changes for the front and the rear passengers"],
         split_reason=_SR_015_04),
    # ---- 018-05 Climate main 內 --------------------------------------------
    dict(req="SWE1-HVAC-018-05", src=T(456),
         title="Mode hard control on Climate main updates the category label",
         proc=["Open the Climate main screen",
               "Press the Mode hard control while on the Climate main screen and read the main "
               "category label"],
         er=["The Climate main screen is displayed", "The main category label shows the new airflow mode"],
         split_reason=_SR_018_05),
    # ---- 080-01 觸控 ---------------------------------------------------------
    dict(req="SWE1-HVAC-080-01", src=T(9),
         title="Long press on the touch screen initiates fast lumbar change",
         pc=("1. [spec-derived] The vehicle is equipped with a lower screen that provides seat "
             "controls (13.2)\n"
             "2. [test-setup] The Seats tab is open and the lumbar/bolster level is away from "
             "both its minimum and its maximum"),
         proc=["Record the lumbar/bolster state shown before the adjustment",
               'Long press "+" on the Seats tab of the touch screen',
               'Release "+" on the touch screen'],
         er=["The lumbar/bolster state before the adjustment is shown",
             "The lumbar/bolster increases faster than it does for a single short press",
             "The lumbar/bolster stops increasing"],
         split_reason=_SR_080_01),
    # ---- 111-04 觸控箭頭（ICS）----------------------------------------------
    dict(req="SWE1-HVAC-111-04", src=T(107),
         title="Holding the ICS temperature arrow moves more than one step",
         upper=("Change temperature on climate screen by using arrows (move 1 increment up/ "
                "down per press, long press = fast move or slider (TEMP pop-up next to slider "
                "when touching it so that finger does not cover number)."),
         proc=[note("the temperature shown on the climate screen"),
               "Press and hold the temperature up arrow on the climate screen"],
         er=["The climate screen shows the current temperature",
             "The temperature moves up by more than 1 increment while the press is held"],
         split_reason=_SR_TEMP_LP.format(o="16.6.1")),
]

# 原條之同步瘦身：拆出之步驟自原條移除（tc -> [(k, 原步驟)]，自後往前刪），
# 必要時補一個 setup 步驟以守 §10.5 之最少兩步
SLIM = {
    T(56): {"del": [(1, "Long-press the temperature up arrow on the climate screen")],
            "prepend": (note("the temperature shown on the climate screen"),
                        "The climate screen shows the current temperature")},
    T(107): {"del": [(1, "Press and hold the temperature up arrow on the climate screen")],
             "prepend": (note("the temperature shown on the climate screen"),
                         "The climate screen shows the current temperature")},
    T(430): {"del": [(2, "Change the fan speed from the climate screen")]},
    T(456): {"del": [(1, "Press the Mode hard control while on the Climate main screen and read "
                         "the main category label")],
             "prepend": ("Open a screen other than Climate main",
                         "The Climate main screen is not displayed")},
}
# 原條因拆分而改設 split_flag（req-id-unique：同 req 之每列皆須宣告）
SPLIT_REASON_FOR_ORIGINAL = {
    T(133): _SR_BRANCH_A,
    T(56): _SR_TEMP_LP.format(o="2.6.1"),
    T(107): _SR_TEMP_LP.format(o="16.6.1"),
    T(430): _SR_015_04,
    T(456): _SR_018_05,
    T(9): _SR_080_01,
}

# 018 之 reasoning 中「018-05 維持一條」一句與本輪之拆分相反，改寫該句（句數不變）
REASONING_FIX = {
    "SWE1-HVAC-003": (
        "故 `003-07` 只驗其確定之另一半（按下特定模式鍵即進該模式），「最接近」之一半不寫入 ER"
        "（§8.4.1 禁造值），該缺口於 reasoning 具名而不吸收（§8.4.2）",
        "故 `003-07` 之「最接近」一半不造值（§8.4.1）—— CMF-02 §3 另產其兩條（A/C、風速）而 ER "
        "之落點為 `PENDING: DR-47`，按下特定模式鍵之一半仍由原條驗"),
    "SWE1-HVAC-018": (
        "**`018-05` 維持一條** —— 條文以「In both cases」把兩個情境併為一句，其驗證目標為"
        "標籤之更新此一事，兩個步驟各覆一個情境。",
        "**`018-05` 依 CMF-02 §3 拆為兩條**（Climate main 內／外各一）—— 條文以「In both "
        "cases」併述之兩個情境，其起始畫面與呈現路徑不同而可各自失效。"),
    "SWE1-HVAC-019": (
        "**`019-02`／`019-03` 停下不產列**",
        "**`019-03` 依 R-C51 產 `[BLOCKED-SPEC]` 列（`019-02` 已另補產）**"),
}


# ================================================================ 執行層
class Log:
    def __init__(self):
        self.rows = []

    def add(self, tc, field, item, before, after):
        self.rows.append({"tc_id": tc["tc_id"], "req_id": tc["req_id"],
                          "field": field, "item": item,
                          "before": before, "after": after})


def _items(text: str) -> list:
    out = []
    for ln in text.split("\n"):
        if not ln.strip():
            continue
        m = re.match(r"^(\d+)\.\s(.*)$", ln)
        if not m:
            raise SystemExit(f"unnumbered line, refusing to renumber: {ln!r}")
        out.append(m.group(2))
    return out


def _numbered(items: list) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))


def _setf(tc, field, new, item, log, expect=None):
    before = tc[field]
    if expect is not None and before != expect:
        raise SystemExit(f"{tc['tc_id']}.{field}: pre-state mismatch\n"
                         f"  expected {expect!r}\n  found    {before!r}")
    if before == new:
        return
    tc[field] = new
    log.add(tc, field, item, before, new)


def apply_steps(tc, ops, item, log):
    proc = _items(tc["test_procedure"])
    er = _items(tc["expected_result"])
    if len(proc) != len(er):
        raise SystemExit(f"{tc['tc_id']}: 1:1 broken before edit")
    # 自後往前處理，前面之 k 不因後面之插入而位移
    for op in sorted([o for o in ops if o[0] == "step"], key=lambda o: -o[1]):
        _, k, old, repl = op
        if proc[k - 1] != old:
            raise SystemExit(f"{tc['tc_id']} step {k}: expected {old!r}, found {proc[k-1]!r}")
        new_p = [p for p, _ in repl]
        new_e = [er[k - 1] if e is KEEP else e for _, e in repl]
        proc[k - 1:k] = new_p
        er[k - 1:k] = new_e
    for op in [o for o in ops if o[0] == "er"]:
        _, k, old, new = op
        if er[k - 1] != old:
            raise SystemExit(f"{tc['tc_id']} ER {k}: expected {old!r}, found {er[k-1]!r}")
        er[k - 1] = new
    _setf(tc, "test_procedure", _numbered(proc), item, log)
    _setf(tc, "expected_result", _numbered(er), item, log)
    for op in [o for o in ops if o[0] == "set"]:
        _, field, old, new = op
        _setf(tc, field, new, item, log, expect=old)


def set_lower(tc, lower, item, log):
    upper, _ = tc["test_item"].split("\n\n")
    _setf(tc, "test_item", f"{upper}\n\n{lower}", item, log)


def refresh_lower_if_needed(tc, before_proc, before_er, item, log):
    """末步或末行 ER 改變者重算下半；其餘不動（手寫之下半不被覆寫）。"""
    last = lambda s: (_items(s) or [""])[-1]
    if tc["tc_id"] in LOWER_OVERRIDE:
        set_lower(tc, LOWER_OVERRIDE[tc["tc_id"]], item, log)
        return
    if (last(tc["test_procedure"]) != last(before_proc)
            or last(tc["expected_result"]) != last(before_er)):
        set_lower(tc, situation(tc), item, log)


def priority_from_0907(tcs: list) -> dict:
    import openpyxl
    ws = openpyxl.load_workbook(BASE_0907, read_only=False)[W.SHEET]
    plan = W.row_plan(tcs)
    out = {}
    for i, row in enumerate(plan):
        if row.get(W.BLANK):
            continue
        v = ws[f"P{W.FIRST_ROW + i}"].value
        if ws[f"D{W.FIRST_ROW + i}"].value != row["req_id"]:
            raise SystemExit(f"row {W.FIRST_ROW + i}: D != {row['req_id']}")
        out[row["tc_id"]] = v
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    paths = sorted(GEN.glob("*.json"))
    docs = {p: json.loads(p.read_text(encoding="utf-8")) for p in paths}
    by_parent = {d["parent"]: (p, d) for p, d in docs.items()}
    tcs = {t["tc_id"]: t for d in docs.values() for t in d["tcs"]}
    doc_of = {t["tc_id"]: d for d in docs.values() for t in d["tcs"]}
    if len(tcs) != 465:
        raise SystemExit(f"expected the 465-TC corpus of ENTRY 035, found {len(tcs)} "
                         "— already applied?")
    log = Log()

    # ---- R-C47 / R-C6(amend) ---------------------------------------------
    prio = priority_from_0907(list(tcs.values()))
    for tid, tc in tcs.items():
        _setf(tc, "priority", prio[tid], "R-C47", log)
        _setf(tc, "test_group", TEST_GROUP, "R-C6(amend)", log)

    # ---- M8 ---------------------------------------------------------------
    for tid, (old, new) in TEST_SET_FIX.items():
        _setf(tcs[tid], "test_set", new, "M8", log, expect=old)

    # ---- M2 / M6 / M9 ------------------------------------------------------
    for tid, ops in STEP_EDITS.items():
        tc = tcs[tid]
        bp, be = tc["test_procedure"], tc["expected_result"]
        item = ("M2" if tid in (T(191), T(192)) else
                "M6" if tid in (T(141), T(158), T(160), T(250)) else
                "sibling-plan wb-006" if tid == T(32) else "M9-compound")
        apply_steps(tc, ops, item, log)
        refresh_lower_if_needed(tc, bp, be, item, log)
    for tid, (k, old, new) in NOTE_EDITS.items():
        tc = tcs[tid]
        bp, be = tc["test_procedure"], tc["expected_result"]
        apply_steps(tc, [("step", k, old, [(new, KEEP)])], "M9-Note", log)
        refresh_lower_if_needed(tc, bp, be, "M9-Note", log)

    # ---- R-C50 ------------------------------------------------------------
    for tid, excerpt in UPPER_EXCERPT.items():
        tc = tcs[tid]
        upper, lower = tc["test_item"].split("\n\n")
        body = " ".join(doc_of[tid]["source_clause"].split())
        if " ".join(excerpt.split()) not in " ".join(upper.split()):
            raise SystemExit(f"{tid}: excerpt is not a contiguous substring of its own upper")
        if " ".join(excerpt.split()) not in body:
            raise SystemExit(f"{tid}: excerpt not in source_clause")
        n = len(excerpt.split())
        if n > UPPER_MAX_TOKENS:
            raise SystemExit(f"{tid}: excerpt is {n} tokens > {UPPER_MAX_TOKENS}")
        _setf(tc, "test_item", f"{excerpt}\n\n{lower}", "R-C50", log)
    still_long = [t["tc_id"] for t in tcs.values()
                  if len(t["test_item"].split("\n\n")[0].split()) > UPPER_MAX_TOKENS]
    if still_long:
        raise SystemExit(f"R-C50: uppers still > {UPPER_MAX_TOKENS} tokens: {still_long}")

    # ---- R-C52 ------------------------------------------------------------
    for tid, (text, _frag) in REMARKS_C52.items():
        _setf(tcs[tid], "remarks", text, "R-C52", log, expect="")

    # ---- 同步瘦身（sibling 之原條）------------------------------------------
    for tid, spec in SLIM.items():
        tc = tcs[tid]
        bp, be = tc["test_procedure"], tc["expected_result"]
        proc, er = _items(bp), _items(be)
        for k, old in sorted(spec["del"], key=lambda x: -x[0]):
            if proc[k - 1] != old:
                raise SystemExit(f"{tid} slim step {k}: expected {old!r}, found {proc[k-1]!r}")
            del proc[k - 1], er[k - 1]
        if "prepend" in spec:
            p, e = spec["prepend"]
            proc.insert(0, p)
            er.insert(0, e)
        _setf(tc, "test_procedure", _numbered(proc), "§3 slim", log)
        _setf(tc, "expected_result", _numbered(er), "§3 slim", log)
        refresh_lower_if_needed(tc, bp, be, "§3 slim", log)
    for tid, reason in SPLIT_REASON_FOR_ORIGINAL.items():
        tc = tcs[tid]
        if not tc["split_flag"]:
            _setf(tc, "split_flag", True, "§3 split", log)
            _setf(tc, "split_reason", reason, "§3 split", log, expect="")

    # ---- reasoning 之句子訂正 ----------------------------------------------
    for parent, (old, new) in REASONING_FIX.items():
        _, d = by_parent[parent]
        if old not in d["reasoning"]:
            raise SystemExit(f"{parent}: reasoning fragment not found")
        d["reasoning"] = d["reasoning"].replace(old, new, 1)

    # ---- R-C51：019-03 BLOCKED 列 -----------------------------------------
    _, d019 = by_parent["SWE1-HVAC-019"]
    src = tcs[T(152)]                                   # 019-01
    b = BLOCKED_019_03
    new = {
        "req_id": "SWE1-HVAC-019-03", "tc_id": TC_ID_019_03,
        "tc_title": b["tc_title"], "test_group": TEST_GROUP,
        "test_set": src["test_set"],
        "test_item": (f"{b['upper']}\n\n(the requirement's content is owned by another "
                      "document, so this delivery carries no test case for it; see Remarks)"),
        "pre_conditions": src["pre_conditions"], "input_test_data": "NA",
        "test_procedure": "", "expected_result": "",
        "specification_reference": W.SYS1_STEM + "_2.13",
        "priority": b["priority"], "design_method": src["design_method"],
        "split_flag": False, "split_reason": "", "functional_safety": "NA",
        "estimated_test_time": "", "remarks": b["remarks"],
        "test_item_authored": b["authored"],
        "emea_ics_review": b["emea_ics_review"],
    }
    if " ".join(b["upper"].split()) not in " ".join(d019["source_clause"].split()):
        raise SystemExit("019-03 upper not in source_clause")
    d019["tcs"].append(new)
    log.add(new, "(new TC)", "R-C51", "", new["tc_id"])

    # ---- §3 siblings --------------------------------------------------------
    n = SIBLING_FIRST_ID
    for s in SIBLINGS:
        base = tcs[s["src"]]
        d = doc_of[s["src"]]
        if base["req_id"] != s["req"]:
            raise SystemExit(f"sibling src {s['src']} is {base['req_id']}, not {s['req']}")
        upper = s.get("upper") or base["test_item"].split("\n\n")[0]
        if " ".join(upper.split()) not in " ".join(d["source_clause"].split()):
            raise SystemExit(f"{s['req']}: sibling upper not in source_clause")
        tc = {
            "req_id": s["req"], "tc_id": T(n), "tc_title": s["title"],
            "test_group": TEST_GROUP, "test_set": base["test_set"],
            "test_item": "", "pre_conditions": s.get("pc", base["pre_conditions"]),
            "input_test_data": "NA",
            "test_procedure": _numbered(s["proc"]),
            "expected_result": _numbered(s["er"]),
            "specification_reference": base["specification_reference"],
            "priority": base["priority"], "design_method": base["design_method"],
            "split_flag": True, "split_reason": s["split_reason"],
            "functional_safety": "NA", "estimated_test_time": "", "remarks": "",
        }
        if "emea_ics_review" in base:
            tc["emea_ics_review"] = base["emea_ics_review"]
        tc["test_item"] = f"{upper}\n\n{s.get('lower') or situation(tc)}"
        d["tcs"].append(tc)
        log.add(tc, "(new TC)", "§3 sibling", "", tc["tc_id"])
        n += 1

    # ---- 寫出 ----------------------------------------------------------------
    total = sum(len(d["tcs"]) for d in docs.values())
    print(f"TCs after: {total} (465 + 1 BLOCKED + {len(SIBLINGS)} siblings)")
    print(f"change-log rows: {len(log.rows)}")
    if args.dry_run:
        print("dry-run — nothing written")
        return 0
    for p, d in docs.items():
        text = json.dumps(d, ensure_ascii=False, indent=1)
        if text != p.read_text(encoding="utf-8"):
            p.write_text(text, encoding="utf-8")
    out = REPORTS / "cmf02_json_change_log.tsv"
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(log.rows[0]), delimiter="\t")
        w.writeheader()
        w.writerows(log.rows)
    print(f"wrote {out.relative_to(FEATURE)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
