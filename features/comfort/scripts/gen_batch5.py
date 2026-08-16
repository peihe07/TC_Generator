#!/usr/bin/env python3
"""Batch 5 generator — ECO HVAC (handoff 38 §6, unblocked by 39 §2).

Scope from framework.md line 45: 10.1 ~ 10.9.1 = 15 leaves. 037 measured
independently: 044(2) + 045..047(1 each) + 048(3) + 049(2) + 050..052(1 each)
+ 053(2) = 15.

Emitted: 15 TCs — -067 … -080 plus the pinned -081.
SWE1-HVAC-044-02 ("reduces climate control system power consumption") has no
HMI-observable quantity AND names no external owner, so it is neither
[BLOCKED-SPEC] (which requires a delegation) nor an R-C16 coverage gap (which
requires 037 not to have produced the leaf). 41 §1.2 rules it the third
class: [BLOCKED-NON-HMI] (R-C38), whitelisted in the same package. Its
tc_id is pinned to -081 so that adding it does not renumber -067…-080.

The fifteenth axis (powertrain) was judged here per 39 §2's criteria and is
now in profile §3.2:

  one axis, not two — ch10 never makes "ECO HVAC equipped" a second variable
    that can take a value independently of EV/BEV; 10.9.1's "When ECO HVAC is
    equipped on a vehicle" restates the chapter's scope. AUTO ECO vs AUTO ON
    is runtime state cycled by pressing AUTO (10.4/10.5), so it lands in
    test_procedure under R-C28's third question.
  function-type, not interface-type — an ICE vehicle has the AUTO button, the
    menu bar icon and the comfort pop-ups; what it lacks is the ECO capability
    (10.5 cites "standard ICE AUTO logics", 10.9.1 contrasts "the standard ICE
    AUTO pop up"). ch16 is another interface for the same capabilities; ch10
    is an extra set of capabilities. Same shape, opposite class (R-C18).

R-C34's generation-time duty, discharged for every TC below:

  observable interface : climate screen AUTO control, main Menu Bar icon,
                         comfort pop-ups — all HVAC UI
  axis 13 (3-knob ICS) : removes it -> excluded on every TC
  EMEA ICS (ch16)      : ch16 has no ECO HVAC section (mirror map lists no
                         counterpart for ch10 at all) -> NOT excluded, and
                         the reason is named rather than left silent
  axis 9 (lower screen): only -077 (051) reads the main Menu Bar icon
  axis 12 (front-only) : removes TABS; nothing here observes a tab

Usage:
    python3 features/comfort/scripts/gen_batch5.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "ECO HVAC"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 67

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"

EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
LOWER_EXPOSED = {"SWE1-HVAC-051"}          # reads the main Menu Bar icon

# Axis 15. 10.1 states the scope of the whole chapter, so every TC carries it.
PC_EV = ("1. [spec-verbatim] The vehicle is an EV vehicle, on which ECO HVAC "
         "is used (10.1)")


def add_exclusions(pre_conditions: str, *lines: str) -> str:
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

# 41 §1.2 — 044-02 is no longer withheld. It is NOT [BLOCKED-SPEC]: 10.1
# names no external owner, so there is nothing to delegate to. It is the
# third class, [BLOCKED-NON-HMI] (R-C38), and its whitelist entry was ruled
# in the same package. The list stays as a named, printed slot so that a
# future withheld leaf cannot become a silent omission.
WITHHELD = []

BATCHES = [
    {
        "parent": "SWE1-HVAC-044",
        "outline": "10.1",
        "reasoning":
            "驗證目標：10.1（EH1）定出 ECO HVAC 為一種 HVAC Mode、限用於 EV 車輛、其目的為降低氣候系統耗電，兩個 037 leaf 分別對應「可被選取為一種模式」與「降低耗電」，一葉一 TC（§8.2.1）。關鍵情境條件：取 profile §3.2 **第十五軸（39 §2 增列）**，其 R-C28 第一問由本節明文「used on EV Vehicles only」對應，標 spec-verbatim；依 **R-C34**，可觀察量為 climate screen 之 AUTO 控制，補第十三軸之排除，而 **EMEA ICS 不補** —— ch16 十八節無 ECO HVAC 之對應節（`ch16_mirror_map.tsv` 之 ch10 側全無列），排除即無所依據。為什麼這樣切：兩者之可觀察量不同 —— 前者為模式可被選取，後者為耗電變化。刻意略過：**-02 之「降低耗電」條文未給任何可於 HMI 觀察之量**，且 10.1 **未指名任何外部擁有者**，故其非 `[BLOCKED-SPEC]`（該類之判準為條文把內容委派到別的文件）而屬 **R-C38** 之第三類 `[BLOCKED-NON-HMI]`——內容不是介面行為，依 41 §1.2 產 BLOCKED row 並經白名單增列；**不採 R-C16 覆蓋缺口**，因 R-C16 治「037 未對其產出需求」而 037 確實產出了本 leaf，以 R-C16 處置會使它在工作簿中不留任何痕跡；替代觀察量之排除已具名兩處 —— AUTO ECO 之降耗機制（取消 airflow mode 選取、風速指示）為 **10.6 之 leaf**（已由 `049-02`／`050` 涵蓋），而全 129 節中唯一於介面上出現耗電字樣者為 **10.9.1 之 pop-up 文字**「Press again for lower battery consumption」，那是該文字之顯示（10.9.1 自身之 leaf，已由 `053-02` 涵蓋）而非耗電量本身，取用任一者皆違 §4.5；搜尋範圍（R-C30）為 `data/section_fulltext.tsv` 全 129 節、pattern `power|consumption|energy|batter` 不分大小寫，命中 5 節：2.7／7.5／16.7 之 `climate power button`（電源鍵，非耗電量）、10.1（本節）、10.9.1（前述 pop-up 文字）；**A-CF23 之逐條複查（42 §4 之名單重建）**：037 對本 leaf 之描述帶 3 張圖，`-01` 之答為**否** —— 其 ER 之「AUTO ECO 模式為作用中」之判讀依據在 **10.3（EH3「Button label will read AUTO ECO」，已由 `046` 涵蓋）**，是條文而非圖片；`-02` 為 BLOCKED row，procedure 與 ER 皆空，無可依賴。",
        "keywords": ["ECO HVAC", "HVAC Mode", "EV Vehicles",
                     "power consumption"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-044-01",
                "tc_title": "ECO HVAC is selectable as an HVAC mode",
                "test_item":
                    "ECO HVAC shall be an HVAC Mode, used on EV Vehicles only",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Press the AUTO button",
                "expected_result":
                    "1. The climate screen shows the AUTO control\n"
                    "2. The AUTO ECO mode is active",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                # R-C38 / profile §5.2 — BLOCKED row, third class. Remarks
                # carries NO owner: not naming one is the classification,
                # not an omission.
                "req_id": "SWE1-HVAC-044-02",
                "tc_id": "NR1L-ComfortHMI-081",
                "tc_title": "ECO HVAC reduces climate system power consumption",
                "test_item":
                    "The system shall reduce climate control system power "
                    "consumption",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure": "",
                "expected_result": "",
                "priority": "P2",
                "design_method": DM_FUNC,
                "blocked":
                    "[BLOCKED-NON-HMI] Not an HMI-observable property — the "
                    "requirement states a reduction in climate control system "
                    "power consumption, which no Comfort HMI screen, pop-up or "
                    "status indicator displays, and which no other document "
                    "is stated to own",
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-045",
        "outline": "10.2",
        "reasoning":
            "驗證目標：10.2（EH2）定出 BEV 車輛之 AUTO 具三狀態（AUTO ECO／AUTO ON／AUTO OFF），單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸之出處於本節為「For BEV vehicles」，惟軸之來源節記於 10.1（`used on EV Vehicles only` 為整章之適用界定），故 PC 標 (10.1)，本節併入 specification_reference（R-C29）；依 R-C34 補第十三軸排除，EMEA ICS 不補（ch16 無 ECO HVAC 之對應節）。為什麼這樣切：三狀態之存在為單一事實，其**循環順序**另由 10.4／10.5 各自成條，本條不重複驗（§4.5）。刻意略過：條文附三張圖片而 `section_fulltext` 僅存其檔名，圖片內容不可讀，故不以圖推斷狀態之視覺呈現（R-C18 同型：讀不到者不得用於判讀）。",
        "keywords": ["BEV", "AUTO ECO", "AUTO ON", "AUTO OFF"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-045",
                "tc_title": "AUTO has three states on BEV vehicles",
                "test_item":
                    "For BEV vehicles, the AUTO functionality shall have 3 "
                    "states: AUTO ECO, AUTO ON, AUTO OFF",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until AUTO is off\n"
                    "2. Press the AUTO button\n"
                    "3. Press the AUTO button",
                "expected_result":
                    "1. The AUTO state is AUTO OFF\n"
                    "2. The AUTO state is AUTO ECO\n"
                    "3. The AUTO state is AUTO ON",
                "priority": "P1",
                "design_method": DM_STATE,
                "spec_ref": ("10.2", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-046",
        "outline": "10.3",
        "reasoning":
            "驗證目標：10.3（EH3）定出按鈕標籤顯示為 AUTO ECO，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1) 並將該節併入 specification_reference；依 R-C34 補第十三軸排除，EMEA ICS 不補。為什麼這樣切：本節只定出一個顯示字串，無分支可分。刻意略過：條文未述該標籤於何種狀態下顯示（AUTO ECO 作用中或恆常），故 procedure 以「進入 AUTO ECO」為步驟而 ER 只判標籤文字，不判其出現時機（§8.4.1）。",
        "keywords": ["AUTO ECO", "button label"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-046",
                "tc_title": "Button label reads AUTO ECO",
                "test_item":
                    "The button label shall read AUTO ECO",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active\n"
                    "2. Read the label on the AUTO button",
                "expected_result":
                    "1. The AUTO ECO mode is active\n"
                    "2. The button label reads AUTO ECO",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.3", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-047",
        "outline": "10.4",
        "reasoning":
            "驗證目標：10.4（EH4）定出 AUTO 關閉且可用時之第一次按壓啟動 AUTO ECO，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；「AUTO 關閉且可用」為 spec 定義之 trigger，惟 TC 自身之步驟即可建立，依 **R-C28 第三問**落 test_procedure 而不入 pre_conditions；依 R-C34 補第十三軸排除，EMEA ICS 不補。為什麼這樣切：本節只定出第一次按壓之結果，第二、三次按壓由 10.5 各自成條。刻意略過：條文之「available」未定義其不可用之條件，故不寫入任何可用性判定（§8.4.1）。",
        "keywords": ["AUTO ECO", "first press", "AUTO off"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-047",
                "tc_title": "First AUTO press activates AUTO ECO",
                "test_item":
                    "When the AUTO function is off and available, the user's "
                    "first press of the AUTO button shall activate the AUTO "
                    "ECO functionality",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until AUTO is off\n"
                    "2. Press the AUTO button once",
                "expected_result":
                    "1. The AUTO state is AUTO OFF\n"
                    "2. The AUTO ECO functionality is activated",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.4", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-048",
        "outline": "10.5",
        "reasoning":
            "驗證目標：10.5（EH5）定出第二次按壓切至 AUTO ON、第三次回到 AUTO ECO，以及 AUTO 模式無法由再按 AUTO 鍵退出而僅能由其他按鍵中斷，三個 037 leaf 逐一對應，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；起始狀態由 procedure 建立（R-C28 第三問）；依 R-C34 補第十三軸排除，EMEA ICS 不補。為什麼這樣切：三者之失效互相獨立 —— 第二次按壓正確而第三次未回到 AUTO ECO，或循環正確而 AUTO 可被按鍵退出，皆可能發生。刻意略過：條文之「acting on other buttons e.g. fan speed, airflow mode etc (see standard ICE AUTO logics)」把中斷條件之完整清單委派予 standard ICE AUTO 邏輯，故 -03 只驗其列舉之二例（fan speed 與 airflow mode）而不擴張（§8.2.1）。",
        "keywords": ["second press", "third press", "AUTO ON", "AUTO ECO",
                     "broken by other buttons"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-048-01",
                "tc_title": "Second AUTO press switches to AUTO ON",
                "test_item":
                    "The second press shall switch to AUTO on",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active\n"
                    "2. Press the AUTO button once",
                "expected_result":
                    "1. The AUTO state is AUTO ECO\n"
                    "2. The AUTO state is AUTO ON",
                "priority": "P1",
                "design_method": DM_STATE,
                "spec_ref": ("10.5", "10.1"),
            },
            {
                "req_id": "SWE1-HVAC-048-02",
                "tc_title": "Third AUTO press returns to AUTO ECO",
                "test_item":
                    "A third press shall go back to AUTO ECO",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ON state is "
                    "active\n"
                    "2. Press the AUTO button once",
                "expected_result":
                    "1. The AUTO state is AUTO ON\n"
                    "2. The AUTO state is AUTO ECO",
                "priority": "P1",
                "design_method": DM_STATE,
                "spec_ref": ("10.5", "10.1"),
            },
            {
                "req_id": "SWE1-HVAC-048-03",
                "tc_title": "AUTO is broken by other buttons not by AUTO itself",
                "test_item":
                    "The user shall not be able to exit AUTO mode by pressing "
                    "the AUTO button again, and AUTO mode shall only be broken "
                    "by acting on other buttons such as fan speed or airflow "
                    "mode",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active\n"
                    "2. Press the AUTO button repeatedly\n"
                    "3. Change the fan speed\n"
                    "4. Press the AUTO button until the AUTO ECO mode is "
                    "active, then change the airflow mode",
                "expected_result":
                    "1. The AUTO state is AUTO ECO\n"
                    "2. The AUTO state stays within AUTO ECO and AUTO ON and "
                    "does not leave AUTO\n"
                    "3. AUTO is broken\n"
                    "4. AUTO is broken",
                "priority": "P1",
                "design_method": DM_STATE,
                "spec_ref": ("10.5", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-049",
        "outline": "10.6",
        "reasoning":
            "驗證目標：10.6（EH6）定出 AUTO ECO 作用中時 airflow modes 之取消選取（同標準 AUTO）與風速指示反映 AUTO ECO，兩個 037 leaf 分別對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；AUTO ECO 之啟動由 procedure 建立；依 R-C34 補第十三軸排除，EMEA ICS 不補。為什麼這樣切：airflow mode 之取消與風速指示為兩個不同位置之可觀察量，失效可各自發生。刻意略過：條文之「as in standard AUTO mode」把取消選取之細節委派予標準 AUTO（2.3，屬 `Climate Modes` 組，尚未生成），故 -01 只驗「airflow modes 被取消選取」此一本節明文之結果，不驗其動畫或順序（§8.2.1）；「fan speed indication should denote that AUTO ECO is active」未給具體樣式，ER 以該詞本身判定（R-C22）。",
        "keywords": ["AUTO ECO", "deselect airflow modes", "fan speed "
                     "indication"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-049-01",
                "tc_title": "AUTO ECO deselects the airflow modes",
                "test_item":
                    "When AUTO ECO is on, the system shall deselect airflow "
                    "modes as in standard AUTO mode",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Select an airflow mode on the climate screen\n"
                    "2. Press the AUTO button until the AUTO ECO mode is "
                    "active",
                "expected_result":
                    "1. The selected airflow mode is shown as selected\n"
                    "2. The airflow modes are deselected",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.6", "10.1"),
            },
            {
                "req_id": "SWE1-HVAC-049-02",
                "tc_title": "Fan speed indication denotes AUTO ECO is active",
                "test_item":
                    "When AUTO ECO is on, the fan speed indication shall "
                    "denote that AUTO ECO is active",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active\n"
                    "2. Read the fan speed indication on the climate screen",
                "expected_result":
                    "1. The AUTO ECO mode is active\n"
                    "2. The fan speed indication denotes that AUTO ECO is "
                    "active",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.6", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-050",
        "outline": "10.7",
        "reasoning":
            "驗證目標：10.7（EH7）定出 HVAC AUTO 之選定設定跨點火循環保留，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；依 R-C34 補第十三軸排除，EMEA ICS 不補。為什麼這樣切：本節只定出一項保留行為，無分支可分。刻意略過：條文未區分保留者為 AUTO ECO 抑或 AUTO ON，故 procedure 以 AUTO ECO 為設定值而 ER 判「與點火前相同」，不宣稱其對另一狀態亦成立（§8.4.2 禁範圍造值）。",
        "keywords": ["HVAC AUTO", "ignition cycles", "keep setting"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-050",
                "tc_title": "AUTO setting survives an ignition cycle",
                "test_item":
                    "HVAC AUTO shall keep the selected setting through "
                    "ignition cycles",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active\n"
                    "2. Run an ignition cycle\n"
                    "3. Read the AUTO state on the climate screen",
                "expected_result":
                    "1. The AUTO state is AUTO ECO\n"
                    "2. The ignition cycle completes\n"
                    "3. The AUTO state is AUTO ECO",
                "priority": "P1",
                "design_method": DM_STATE,
                "spec_ref": ("10.7", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-051",
        "outline": "10.8",
        "reasoning":
            "驗證目標：10.8（EH8）定出 Comfort main Menu Bar icon 反映 AUTO ECO 與 AUTO 狀態，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；依 **R-C34**，本條之可觀察量為 **main Menu Bar icon**，落於 head unit 之 comfort section，故**另補第九軸之排除**（6.3 使該 section 自 head unit 移除），標 (6.3) 並併入 specification_reference —— 本組唯一暴露於第九軸者；第十三軸照補，EMEA ICS 不補。為什麼這樣切：本節只定出一項反映關係，兩個狀態於同一條內以兩步驟驗證。刻意略過：條文未給 icon 之具體圖樣，ER 以「反映該狀態」判定而不描述圖形（R-C22）。",
        "keywords": ["Menu Bar icon", "AUTO ECO", "AUTO states"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-051",
                "tc_title": "Menu Bar icon reflects the AUTO ECO and AUTO states",
                "test_item":
                    "The Comfort main Menu Bar icon shall reflect the AUTO ECO "
                    "and AUTO states",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active, then read the Comfort main Menu Bar icon\n"
                    "2. Press the AUTO button once, then read the Comfort main "
                    "Menu Bar icon",
                "expected_result":
                    "1. The Comfort main Menu Bar icon reflects the AUTO ECO "
                    "state\n"
                    "2. The Comfort main Menu Bar icon reflects the AUTO ON "
                    "state",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.8", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-052",
        "outline": "10.9",
        "reasoning":
            "驗證目標：10.9（EH9）定出由硬鍵互動觸發之 comfort popup 反映 AUTO ECO 與 AUTO 狀態，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；依 R-C34 補第十三軸排除（3 旋鈕 ICS 車上無 HVAC popup），EMEA ICS 不補；popup 於 6.3 之車輛仍存（`except for comfort popups`），故第九軸不暴露。為什麼這樣切：本節只定出一項反映關係。刻意略過：popup 之觸發規則本身定義於 2.2 與 ch14，本條只驗其**內容反映該狀態**，不驗其出現時機或逾時（§8.2.1）；附加提示文字另由 10.9.1 各自成條。",
        "keywords": ["comfort pop ups", "hard controls", "AUTO ECO",
                     "AUTO states"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-052",
                "tc_title": "Comfort pop-ups reflect the AUTO ECO and AUTO states",
                "test_item":
                    "The comfort pop ups triggered by hard controls "
                    "interaction shall reflect the AUTO ECO and AUTO states",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active, then change the fan speed using the fan speed "
                    "hard control\n"
                    "2. Press the AUTO button once, then change the fan speed "
                    "using the fan speed hard control",
                "expected_result":
                    "1. The comfort pop up reflects the AUTO ECO state\n"
                    "2. The comfort pop up reflects the AUTO ON state",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.9", "10.1"),
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-053",
        "outline": "10.9.1",
        "reasoning":
            "驗證目標：10.9.1（EH9.1）定出配備 ECO HVAC 之車輛其 AUTO popup 較標準 ICE AUTO popup 多一段提示文字，並給出兩種狀態下之逐字文字，兩個 037 leaf 分別對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十五軸依 R-C29 標 (10.1)；依 R-C34 補第十三軸排除，EMEA ICS 不補；popup 於 6.3 車輛仍存，第九軸不暴露。為什麼這樣切：兩段文字對應兩個不同狀態，失效可各自發生（進入 AUTO ECO 之文字正確而標準 AUTO 之文字錯，是可能的）。刻意略過：條文以「compared to the standard ICE AUTO pop up」作對照，而標準 ICE popup 屬 ch2／ch14，本條只驗本節所給之兩段文字逐字出現，不驗其與標準 popup 之差異集合（§8.2.1）；文字照條文之書名號內容逐字引用，不改寫（R-C33：內容以條文為準）；**A-CF23 之逐條複查（42 §4 之名單重建）**：037 對本 leaf 之描述帶 1 張圖，兩條之答**皆為否** —— ER 所驗者為 EH9.1 書名號內之兩段文字**逐字出現**，該文字在條文內，圖片所載之 popup 版面與圖示不在本條驗證範圍。",
        "keywords": ["AUTO pop ups", "additional info text",
                     "Press again to improve climate performance",
                     "Press again for lower battery consumption"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-053-01",
                "tc_title": "AUTO ECO pop-up shows the climate performance text",
                "test_item":
                    "When entering the AUTO ECO mode, the AUTO pop up text "
                    "shall read \"Press again to improve climate performance\"",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until AUTO is off\n"
                    "2. Press the AUTO button once and read the AUTO pop up",
                "expected_result":
                    "1. The AUTO state is AUTO OFF\n"
                    "2. The AUTO pop up reads \"Press again to improve climate "
                    "performance\"",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.9.1", "10.1"),
            },
            {
                "req_id": "SWE1-HVAC-053-02",
                "tc_title": "Standard AUTO pop-up shows the battery consumption text",
                "test_item":
                    "When standard AUTO is activated, the AUTO pop up text "
                    "shall read \"Press again for lower battery consumption\"",
                "pre_conditions": PC_EV,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the AUTO button until the AUTO ECO mode is "
                    "active\n"
                    "2. Press the AUTO button once and read the AUTO pop up",
                "expected_result":
                    "1. The AUTO state is AUTO ECO\n"
                    "2. The AUTO pop up reads \"Press again for lower battery "
                    "consumption\"",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("10.9.1", "10.1"),
            },
        ],
    },
]


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
            # 41 §7.2 — 044-02 lands AFTER the batch's own 14 rows, so its
            # tc_id is pinned rather than drawn from the running counter.
            # Drawing it would renumber -067…-080, and a tc_id that moves
            # is not an identifier (R-C7 / §4.1).
            if "tc_id" in tc:
                tid = tc["tc_id"]
            else:
                n += 1
                tid = TC_ID_FMT.format(n=n)
            ex, refs = [EX_ICS], list(tc.get("spec_ref", (o,))) + ["2.14"]
            if tc["req_id"] in LOWER_EXPOSED:
                ex.append(EX_LOWER)
                refs.append("6.3")
            blocked = tc.get("blocked", "")
            tcs.append({
                "req_id": tc["req_id"],
                "tc_id": tid,
                "tc_title": tc["tc_title"],
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": tc["test_item"],
                "pre_conditions": add_exclusions(tc["pre_conditions"], *ex),
                "input_test_data": tc["input_test_data"],
                "test_procedure": "" if blocked else tc["test_procedure"],
                "expected_result": "" if blocked else tc["expected_result"],
                "specification_reference": "; ".join(
                    f"{STEM}_{x}" for x in dict.fromkeys(refs)),
                "priority": tc["priority"],
                "design_method": tc["design_method"],
                "split_flag": tc.get("split_flag", False),
                "split_reason": tc.get("split_reason", ""),
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": blocked,
            })
        doc = {
            "parent": b["parent"],
            "outline": o,
            "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": b["reasoning"],
            "keywords": b["keywords"],
            "duplicate_of": "",
            "distinguishing_axis": {"axis": "see per-TC titles", "delta": ""},
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
    for req, why in WITHHELD:
        print(f"- {req}: {why}")
    held = len(WITHHELD)
    print(f"\n{leaves} emitted + {held} withheld = {leaves + held} leaves "
          f"declared for {TEST_SET} (framework.md: 15)")
    if leaves + held != 15 or total != 15:
        raise SystemExit(
            f"expected 15 leaves declared / 15 TCs, got {leaves + held} / {total}")


if __name__ == "__main__":
    main()
