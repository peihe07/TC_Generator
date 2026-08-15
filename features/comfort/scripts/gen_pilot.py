#!/usr/bin/env python3
"""Pilot batch generator — Seat Control Tab, 14 leaves (handoff 19 §7.5).

The TC content is authored here rather than emitted by a template, because
every field is a judgement traceable to a clause. What the script contributes
is determinism: tc_ids are assigned by position (never by the model, R-C7),
the clause text is read from section_fulltext.tsv (never the truncated
title, R-C18), and the same run always produces the same files.

Rulings applied, each visible in the data below:
  19 §2.1  lower-screen presence is the ninth configuration axis; its source
           class is decided per clause, never by copying 6.3's wording
  19 §2.2  stowed/retracted is runtime state — pre_condition only when the
           TC's target IS the behaviour in that state
  19 §3    `(-, +)` verbatim in test_item and quoted spec fragments;
           `"-"` / `"+"` in procedure steps and non-quoting ER
  19 §4    13.4 / 13.5 are in scope but narrowed; the delegated part is named
           in reasoning and is not tested
  R-C22    no fabricated magnitudes; ER uses the clause's own observable
           ("level", "greyed out", "error tone")

Usage:
    python3 features/comfort/scripts/gen_pilot.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "Seat Control Tab"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"
DM_DECISION = "決策表 (Decision Table Testing)"
DM_BVA = "邊界值分析 (Boundary Value Analysis, BVA)"

# The ninth axis, phrased from 13.2's OWN wording ("the lower screen"), not
# from 6.3's "non-foldable secondary lower screen" (19 §2.1 forbids reuse).
PC_SCREEN = ("1. [spec-derived] The vehicle is equipped with a lower screen "
             "that provides seat controls (13.2)")
PC_DOOR = ("2. [spec-derived] The door control carries the seat control "
           "(-, +) buttons for lumbar and bolster (13.2)")

BATCHES = [
    # ---------------------------------------------------------------- 13.2
    {
        "parent": "SWE1-HVAC-076",
        "outline": "13.2",
        "reasoning":
            "驗證目標：13.2（LS1.）以 lower screen 是否 stowed、使用者是否已在 climate section 兩條件分出三個分支，三個 037 leaf 恰對應之，故一葉一 TC（§8.2.1）。關鍵情境條件：第九軸之措辭取自本節自身「the lower screen」而非 6.3 之「non-foldable secondary lower screen」，故標 spec-derived；stowed／retracted 依 19 §2.2 判定測試入 pre_conditions，因三條之驗證目標即該狀態下之行為。為什麼這樣切：條文之三分支互斥且各有獨立結果，合併會使任一分支失敗都無法定位。刻意略過：popup 樣式與 Seats tab 內容本節未定義，寫入即造值（§8.4.1）；5 秒 timeout 為條文明載，照用。",
        "keywords": ["lower screen", "stowed", "Seats tab",
                     "Seat Control Popup", "lumbar", "bolster"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-076-01",
                "tc_title": "Seats tab opens on the lower screen when it is not stowed",
                "test_item":
                    "When the (-, +) seat control buttons are pressed from the "
                    "door control for lumbar & bolster, if the lower screen is "
                    "not in the stowed position, the system shall switch the "
                    "tab on the lower screen to the Seats tab",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-verbatim] The lower screen is not in the stowed "
                    "position (13.2)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Note which tab is currently shown on the lower screen\n"
                    "2. Press \"-\" on the door seat control",
                "expected_result":
                    "1. The tab shown on the lower screen is not the Seats tab\n"
                    "2. The lower screen switches to the Seats tab",
                "priority": "P1",
                "design_method": DM_DECISION,
            },
            {
                "req_id": "SWE1-HVAC-076-02",
                "tc_title": "Seat Control Popup appears on the head unit when the lower screen is stowed",
                "test_item":
                    "When the (-, +) seat control buttons are pressed from the "
                    "door control for lumbar & bolster, if the lower screen is "
                    "in the stowed position, the system shall display the Seat "
                    "Control Popup on the head unit, and the popup shall time "
                    "out after 5 seconds of not interaction",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-verbatim] The lower screen is in the stowed "
                    "position (13.2)\n"
                    "4. [spec-derived] The user is not in the climate section "
                    "on the main head unit (13.2)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"-\" on the door seat control\n"
                    "2. Do not interact with the head unit for 5 seconds",
                "expected_result":
                    "1. The Seat Control Popup is displayed on the head unit\n"
                    "2. The Seat Control Popup is no longer displayed",
                "priority": "P1",
                "design_method": DM_DECISION,
            },
            {
                "req_id": "SWE1-HVAC-076-03",
                "tc_title": "Seats tab is opened when the user is already in the climate section",
                "test_item":
                    "When the (-, +) seat control buttons are pressed from the "
                    "door control for lumbar & bolster, if the lower screen is "
                    "in the stowed position and the user is already in the "
                    "climate section on the main head unit, the system shall "
                    "switch the user to the Seats tab",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-verbatim] The lower screen is in the stowed "
                    "position (13.2)\n"
                    "4. [spec-verbatim] The user is already in the climate "
                    "section on the main head unit (13.2)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Note which tab is currently shown in the climate "
                    "section on the head unit\n"
                    "2. Press \"-\" on the door seat control",
                "expected_result":
                    "1. The tab shown in the climate section is not the Seats tab\n"
                    "2. The head unit switches to the Seats tab",
                "priority": "P1",
                "design_method": DM_DECISION,
            },
        ],
    },
    # -------------------------------------------------------------- 13.2.1
    {
        "parent": "SWE1-HVAC-077",
        "outline": "13.2.1",
        "reasoning":
            "驗證目標：13.2.1（LS1.1）所列腰靠／側靠四種可調類型皆可取得。關鍵情境條件：需先開啟 Seats tab —— 該動作為 step-controlled state，依 §4.4 下放為 procedure 第 1 步而非 Pre-Condition（20 §1 修正）。為什麼這樣切：037 對本節僅產出一個 leaf（parent 形態即需求，R-C3），且條文以單句列舉四者，拆成四條會使 Test Set 欄淪為 TC ID 副本。刻意略過：各類型之調整範圍與級距 —— 本節未定義，級距屬 13.5 且其量值由 CFTS044 擁有（19 §4.2）。",
        "keywords": ["lumbar", "bolster", "adjustment types", "Seats tab"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-077",
                "tc_title": "Four lumbar and bolster adjustment types are available",
                "test_item":
                    "The 4 types of adjustments the user will be able to alter "
                    "for lumbar/bolster will be: Lumbar In/Out, Lumbar Up/Down, "
                    "Back Bolster, Thigh Bolster",
                "pre_conditions": PC_SCREEN,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the Seats tab\n"
                    "2. Read the list of lumbar and bolster adjustment types "
                    "offered on the Seats tab",
                "expected_result":
                    "1. The Seats tab is shown\n"
                    "2. The offered adjustment types are \"Lumbar In/Out\", "
                    "\"Lumbar Up/Down\", \"Back Bolster\" and \"Thigh Bolster\"",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    # ---------------------------------------------------------------- 13.3
    {
        "parent": "SWE1-HVAC-078",
        "outline": "13.3",
        "reasoning":
            "驗證目標：13.3（LS2.）第一次按壓只觸發 popup 或 tab 切換，調整要到第二次按壓才 reflected。關鍵情境條件：按壓序數為唯一變數，其餘條件兩條 TC 相同。為什麼這樣切：兩個 037 leaf 對應兩個階段，以按壓序數為 distinguishing axis 分兩條（§4.6）。刻意略過：popup 與 tab 切換何者發生由 13.2 之分支決定，本節不重複驗證該分支（§8.2.1 不擴張至 sibling）。ER 錨定條文自身之 reflected，不引入 13.6 才使用之 level（20 §4）。",
        "keywords": ["first press", "second press", "popup", "tab change",
                     "level"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-078-01",
                "tc_title": "First press triggers the popup or tab change only",
                "test_item":
                    "When the (-, +) seat control buttons are pressed, the "
                    "system shall trigger the popup or tab change within "
                    "climate, and only on the second press will the adjustment "
                    "be reflected",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [test-setup] The Seats tab is not currently shown, and "
                    "the lumbar/bolster level is away from both its minimum and "
                    "its maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record the lumbar/bolster state shown before the "
                    "adjustment\n"
                    "2. Press \"+\" once on the door seat control",
                "expected_result":
                    "1. The lumbar/bolster state shown before the adjustment "
                    "is recorded\n"
                    "2. The popup or the tab change is shown, and the "
                    "adjustment is not reflected",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-078-02",
                "tc_title": "Second press applies the lumbar adjustment",
                "test_item":
                    "When the (-, +) seat control buttons are pressed, only on "
                    "the second press will the adjustment be reflected",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-derived] The first press has already triggered "
                    "the popup or the tab change (13.3)\n"
                    "4. [test-setup] The lumbar/bolster level is away from both "
                    "its minimum and its maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record the lumbar/bolster state shown before the "
                    "adjustment\n"
                    "2. Press \"+\" a second time on the door seat control",
                "expected_result":
                    "1. The lumbar/bolster state shown before the adjustment "
                    "is recorded\n"
                    "2. The adjustment is reflected",
                "priority": "P1",
                "design_method": DM_STATE,
            },
        ],
    },
    # -------------------------------------------------------------- 13.3.1
    {
        "parent": "SWE1-HVAC-079",
        "outline": "13.3.1",
        "reasoning":
            "驗證目標：13.3.1（LS2.1）之 latching —— 最後選定之腰靠／側靠選項跨 keycycle 與螢幕收合後仍保持。關鍵情境條件：條文先給通則（三個生命週期事件），再給具名例子（Back Bolster ＋ 收合 ＋ door 按鍵或 HU seat tab 重入）。為什麼這樣切：兩個 037 leaf 恰對應通則與例子，distinguishing axis 為 lifecycle event —— -01 驗 keycycle 邊界，-02 驗收合後之重入路徑。刻意略過：例子中之 Back Bolster 為條文具名，照錄不替換為其他類型。",
        "keywords": ["latching", "keycycle", "retract", "Back Bolster",
                     "selected option"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-079-01",
                "tc_title": "Last selected adjustment latches across a keycycle",
                "test_item":
                    "The user last selected lumbar/bolster selection will be "
                    "latching during a keycycle, after a keycycle, and after "
                    "the lower screen has been stowed/retracted",
                "pre_conditions":
                    f"{PC_SCREEN}\n"
                    "2. [spec-derived] A lumbar/bolster adjustment type is "
                    "currently the selected option (13.3.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record which lumbar/bolster adjustment type is the "
                    "selected option\n"
                    "2. Run a keycycle\n"
                    "3. Open the Seats tab and read the selected option",
                "expected_result":
                    "1. The selected option shown before the keycycle is "
                    "recorded\n"
                    "2. The head unit completes the keycycle\n"
                    "3. The selected option is the one recorded in step 1",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-079-02",
                "tc_title": "Back Bolster stays selected after the lower screen is retracted",
                "test_item":
                    "If the lower screen displayed the last selected option as "
                    "Back Bolster , then the user retracts the lower screen, "
                    "the next time they press the door (-, +) buttons or enter "
                    "the seat tab on the HU, Back Bolster will still be the "
                    "selected option",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-verbatim] The lower screen displayed the last "
                    "selected option as Back Bolster (13.3.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Retract the lower screen\n"
                    "2. Press \"+\" on the door seat control\n"
                    "3. Read the selected option",
                "expected_result":
                    "1. The lower screen is retracted\n"
                    "2. The Seat Control Popup or the Seats tab is shown\n"
                    "3. The selected option is \"Back Bolster\"",
                "priority": "P2",
                "design_method": DM_STATE,
            },
        ],
    },
    # ---------------------------------------------------------------- 13.4
    {
        "parent": "SWE1-HVAC-080",
        "outline": "13.4",
        "reasoning":
            "驗證目標：13.4（LS3.）長按 (-, +) 或觸控螢幕啟動快速增減。關鍵情境條件：依 19 §4.1 收窄 —— 長按之判定門檻、重複速率、加速曲線由 HMI Core Logic and Flow requirement N0 擁有，不在本 feature 範圍，不測、不補值，故 procedure 不指定按壓時長、ER 不述速率。為什麼這樣切：037 拆為「快速增減被啟動」與「邏輯依 Core N0」兩個 leaf。刻意略過：-080-02 之區別內容純為上述委派，且其 Verification Criteria 之 Action 與 -01 相同（兩個操作面本就同在 -01），扣除委派後無餘留 —— 依 20 §2.1 回報停下，待裁（見 split_reason）。",
        "keywords": ["long press", "fast increase", "fast decrease", "level",
                     "delegated"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-080-01",
                "tc_title": "Long press initiates fast lumbar level change",
                "test_item":
                    "The user will be able to long press on the hard button "
                    "(-, +) or on the touch screen itself to initiate fast "
                    "increases/decreases",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [test-setup] The Seats tab is open and the "
                    "lumbar/bolster level is away from both its minimum and its "
                    "maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record the lumbar/bolster state shown before the "
                    "adjustment\n"
                    "2. Long press \"+\" on the door seat control\n"
                    "3. Release \"+\"",
                "expected_result":
                    "1. The lumbar/bolster state shown before the adjustment "
                    "is recorded\n"
                    "2. The lumbar/bolster increases faster than it does for a "
                    "single short press\n"
                    "3. The lumbar/bolster stops increasing",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-080-02",
                "tc_title": "Long press on the touch screen initiates the same fast change",
                "test_item":
                    "The user will be able to long press on the touch screen "
                    "itself to initiate fast increases/decreases, with the "
                    "long-press logic as per HMI Core Logic and Flow "
                    "(requirement N0)",
                "pre_conditions":
                    f"{PC_SCREEN}\n"
                    "2. [test-setup] The Seats tab is open and the "
                    "lumbar/bolster level is away from both its minimum and its "
                    "maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record the lumbar/bolster state shown before the "
                    "adjustment\n"
                    "2. Long press \"+\" on the door seat control\n"
                    "3. Release \"+\"",
                "expected_result":
                    "1. The lumbar/bolster state shown before the adjustment "
                    "is recorded\n"
                    "2. The lumbar/bolster increases faster than it does for a "
                    "single short press\n"
                    "3. The lumbar/bolster stops increasing",
                "priority": "P2",
                "design_method": DM_FUNC,
                "split_flag": True,
                "split_reason":
                    "037 將本節拆為兩個 leaf，本 leaf 之區別內容純為委派至外部 "
                    "spec，於本 feature 範圍內扣除後無餘留。依 20 §2.1 回報停下，"
                    "待裁；本 TC 之驗證目標暫同其 -01 sibling，不得視為已定案",
                "duplicate_of": "",
                "axis": "delegated-only",
                "delta":
                    "037 之 -080-02 全文為「The system shall logic as per HMI "
                    "Core Logic and Flow (requirement N0)」，其 Verification "
                    "Criteria 之 Action 與 -080-01 相同（Long press (-, +) "
                    "hard button or touchscreen control）—— **兩個操作面本就"
                    "同在 -01**。故本 leaf 之區別內容純為委派（Core N0 之"
                    "長按門檻／速率／加速曲線），扣除後於本 feature 範圍內"
                    "**無餘留**。依 20 §2.1 回報停下，待裁",
            },
        ],
    },
    # ---------------------------------------------------------------- 13.5
    {
        "parent": "SWE1-HVAC-081",
        "outline": "13.5",
        "reasoning":
            "驗證目標：13.5（LS4.）短按 (-, +) 使腰靠／側靠增加一個級距。關鍵情境條件：依 19 §4.2 收窄 —— 級距之量值及與舊款 4-way rocker 之等效性由 CFTS044 擁有，不在範圍；依 R-C22，ER 不補任何量值，改用條文自身之動詞 increase／decrease（13.5 未使用 level 一詞，故不外推，20 §4）。為什麼這樣切：037 拆為「小級距增減」與「與 rocker 等效」兩個 leaf。刻意略過：-081-02 之區別內容純為上述委派，Action 與 -01 相同，扣除後無餘留 —— 依 20 §2.1 回報停下，待裁（見 split_reason）。",
        "keywords": ["short press", "increment", "level", "lumbar", "bolster",
                     "delegated"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-081-01",
                "tc_title": "Short press moves the lumbar level by one step",
                "test_item":
                    "A short press of the (-, +) button will increase the "
                    "lumbar/bolster by a small set amount",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-derived] The popup or tab change has already been "
                    "triggered, so the next press is applied (13.3)\n"
                    "4. [test-setup] The lumbar/bolster level is away from both "
                    "its minimum and its maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record the lumbar/bolster state shown before the "
                    "adjustment\n"
                    "2. Short press \"+\" on the door seat control\n"
                    "3. Short press \"-\" on the door seat control",
                "expected_result":
                    "1. The lumbar/bolster state shown before the adjustment "
                    "is recorded\n"
                    "2. The lumbar/bolster is increased\n"
                    "3. The lumbar/bolster is decreased back to the state "
                    "recorded in step 1",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-081-02",
                "tc_title": "Short press on the touch screen moves the level by one step",
                "test_item":
                    "A short press will increase the lumbar/bolster by a small "
                    "set amount, that would be equivalent to a short press of "
                    "the previous 4-way rocker hard control",
                "pre_conditions":
                    f"{PC_SCREEN}\n"
                    "2. [test-setup] The Seats tab is open and the "
                    "lumbar/bolster level is away from both its minimum and its "
                    "maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Record the lumbar/bolster state shown before the "
                    "adjustment\n"
                    "2. Short press \"+\" on the door seat control\n"
                    "3. Short press \"-\" on the door seat control",
                "expected_result":
                    "1. The lumbar/bolster state shown before the adjustment "
                    "is recorded\n"
                    "2. The lumbar/bolster is increased\n"
                    "3. The lumbar/bolster is decreased back to the state "
                    "recorded in step 1",
                "priority": "P2",
                "design_method": DM_FUNC,
                "split_flag": True,
                "split_reason":
                    "037 將本節拆為兩個 leaf，本 leaf 之區別內容純為委派至外部 "
                    "spec，於本 feature 範圍內扣除後無餘留。依 20 §2.1 回報停下，"
                    "待裁；本 TC 之驗證目標暫同其 -01 sibling，不得視為已定案",
                "duplicate_of": "",
                "axis": "delegated-only",
                "delta":
                    "037 之 -081-02 全文為「The system shall equivalent to "
                    "short press of previous 4-way rocker hard control」，其 "
                    "Verification Criteria 之 Action 與 -081-01 相同"
                    "（Short press (-, +) button）。故本 leaf 之區別內容純為"
                    "委派（CFTS044 所定之級距量值與等效性），扣除後於本 "
                    "feature 範圍內**無餘留**。依 20 §2.1 回報停下，待裁",
            },
        ],
    },
    # ---------------------------------------------------------------- 13.6
    {
        "parent": "SWE1-HVAC-082",
        "outline": "13.6",
        "reasoning":
            "驗證目標：13.6（LS5.）到達上下限後控制被 grey out，以及再按觸發 error tone。關鍵情境條件：本節為 ch13 唯一使用 level 一詞者，故 ER 保留該詞；error tone 照錄條文措辭，其頻率、時長、視覺回饋一律不寫（條文未給）。為什麼這樣切：兩個 037 leaf 對應兩者，distinguishing axis 為 observable channel —— -01 驗視覺（greyed out），-02 驗聽覺加上級距不再變化。刻意略過：不標 BLOCKED（R-C22：值不知道但事件看得見）；設計方法取 BVA 而非負向測試，因於上限再按 (+) 是合法輸入落在邊界，非注入非法值。",
        "keywords": ["minimum", "maximum", "level", "greyed out", "error tone"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-082-01",
                "tc_title": "Control is greyed out at the minimum and maximum level",
                "test_item":
                    "Once the minimum or maximum level has been reach, the "
                    "system shall grey out the (-, +) control",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [test-setup] The Seats tab is open and the "
                    "lumbar/bolster level is away from both its minimum and its "
                    "maximum",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"+\" repeatedly until the lumbar/bolster level "
                    "stops increasing\n"
                    "2. Read how the \"+\" control is presented\n"
                    "3. Press \"-\" repeatedly until the lumbar/bolster level "
                    "stops decreasing\n"
                    "4. Read how the \"-\" control is presented",
                "expected_result":
                    "1. The lumbar/bolster reaches its maximum level and stops "
                    "changing\n"
                    "2. The \"+\" control is greyed out\n"
                    "3. The lumbar/bolster reaches its minimum level and stops "
                    "changing\n"
                    "4. The \"-\" control is greyed out",
                "priority": "P1",
                "design_method": DM_BVA,
            },
            {
                "req_id": "SWE1-HVAC-082-02",
                "tc_title": "Error tone is played when pressing beyond the maximum level",
                "test_item":
                    "So if the user is increasing their lumbar, once the "
                    "maximum has been reached, pressing the (+) button again "
                    "will result in error tone being triggered",
                "pre_conditions":
                    f"{PC_SCREEN}\n{PC_DOOR}\n"
                    "3. [spec-derived] The lumbar/bolster level is already at "
                    "its maximum (13.6)\n"
                    "4. [test-setup] The cabin is quiet enough for a tone to be "
                    "heard",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"+\" repeatedly until the lumbar/bolster stops "
                    "increasing\n"
                    "2. Press \"+\" once more on the door seat control",
                "expected_result":
                    "1. The lumbar/bolster is at its maximum level\n"
                    "2. An error tone is played and the lumbar/bolster stays at "
                    "its maximum level",
                "priority": "P2",
                "design_method": DM_BVA,
            },
        ],
    },
]


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    OUT.mkdir(exist_ok=True)
    n = 0
    total = 0
    for b in BATCHES:
        o = b["outline"]
        if o not in full:
            raise SystemExit(f"{o} not in section_fulltext.tsv")
        tcs = []
        for tc in b["tcs"]:
            n += 1
            row = {
                "req_id": tc["req_id"],
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": tc["tc_title"],
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": tc["test_item"],
                "pre_conditions": tc["pre_conditions"],
                "input_test_data": tc["input_test_data"],
                "test_procedure": tc["test_procedure"],
                "expected_result": tc["expected_result"],
                "specification_reference": f"{STEM}_{o}",
                "priority": tc["priority"],
                "design_method": tc["design_method"],
                "split_flag": tc.get("split_flag", False),
                "split_reason": tc.get("split_reason", ""),
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
            }
            tcs.append(row)
        # distinguishing_axis is driven by the axis/delta keys, NOT by
        # duplicate_of. Keying it on duplicate_of was what let a removed
        # duplicate_of silently blank the axis (20 §2).
        axed = [t for t in b["tcs"] if t.get("axis")]
        dupes = [t for t in b["tcs"] if t.get("duplicate_of")]
        doc = {
            "parent": b["parent"],
            "outline": o,
            "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": b["reasoning"],
            "keywords": b["keywords"],
            "duplicate_of": dupes[0]["duplicate_of"] if dupes else "",
            "distinguishing_axis": {
                "axis": axed[0]["axis"] if axed else "see per-TC titles",
                "delta": axed[0]["delta"] if axed else "",
            },
            "assumptions": [],
            "tcs": tcs,
        }
        (OUT / f"{b['parent']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{b['parent']}  {o:8} {len(tcs)} TC  -> generated/{b['parent']}.json")
    print(f"\n{total} TCs across {len(BATCHES)} parents; "
          f"tc_id {TC_ID_FMT.format(n=1)} … {TC_ID_FMT.format(n=total)}")
    if total != 14:
        raise SystemExit(f"expected 14 TCs, emitted {total}")


if __name__ == "__main__":
    main()
