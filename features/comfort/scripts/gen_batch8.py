#!/usr/bin/env python3
"""Batch 8 generator — Home Screen Widget (handoff 49 §2).

Scope from framework.md line 53 and its §15 table, derived rather than
retyped (48 §2 changed the handoff's batch table for exactly this reason):

    17.1  3 | 17.2  8 | 17.3  3 | 17.4  2 | 17.5  2 | 18.1  3   = 21 leaves

037 measured independently: 124(3) + 125(8) + 126(3) + 127(2) + 128(2)
+ 129(3) = 21.

Emitted: 12 TCs, -115 … -126.
WITHHELD: 9 leaves, on TWO unregistered configuration axes (axis 16
registered by 50 §1 released the other two). profile §3.2
is explicit — "未判類別之軸不得使用" — so an axis that is not among the
fifteen, and whose interface-type/function-type category has never been
judged, stops the leaf. Each axis was put through 49 §1's three conditions
anyway, so that registering it costs the analysis layer one line rather than
a fresh investigation (上繳 34 §6):

  (A) 螢幕尺寸 / widget 尺寸  conditions NOT met — same question as DR #6
  (B) Comfort Features 有無   conditions ALL met -> registered as axis 16
                              by 50 §1 (功能型); 17.3-01/-03 unblocked
  (C) dual airflow modes 有無 condition ONE not met — only the positive
                              value is attested; its negation appears nowhere

  (A) 17.2-08, 17.3-02, 17.4-01, 17.4-02, 18.1-01, 18.1-02, 18.1-03
  (C) 17.5-01, 17.5-02

18.1 deserves its own note. Its clause text is **verbatim identical** to
17.1's, minus 17.1's parenthetical. The only thing distinguishing them is the
CHAPTER TITLE (`10.25" Home screen - Comfort Widget` vs `Home screen -
Comfort Widget`) — and a chapter title is not a clause. So a pre_condition
naming the screen size has no clause source at all: R-C28's first question
fails before the axis question is even reached. Generating both sections
without that pre_condition would emit two identical TC sets differing by
nothing (§4.5 / §4.6).

DR #6 ("which screen configurations are in this delivery") is the same
question, and it is still open. Reported in 上繳 34 §6.3: this batch widens
DR #6's blast radius from 19.1–19.3 to 7 leaves here.

R-C17 is this batch's main risk and is handled per-leaf, not per-batch:
Comfort owns "the Comfort widget's own content and behaviour". Home-screen
management (adding/deleting/reordering pages, widget drag-and-drop, Shortcuts
editing, brand-page defaults) belongs to Home Screen's SWE requirements. The
test is WHERE THE RULE IS DEFINED, not who cites it. Measured: none of the
six sections states a home-screen management rule — every leaf below is about
what the widget CONTAINS or DISPLAYS, so no leaf was dropped on R-C17
grounds. The parenthetical in 17.1 is handled at §4 below.

19.x (7" widget) is NOT generated — R-C5-1 leaves it `undetermined` pending
DR #6, and framework.md does not place it in this Test Set either.

Usage:
    python3 features/comfort/scripts/gen_batch8.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "Home Screen Widget"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 115

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"

# ch17/ch18 are the ch2-side interface, so the EMEA exclusion applies here as
# it does to every ch2/ch3 batch — ch16 carries no widget section at all.
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
# Axis 9 — 6.3 removes the comfort section from the head unit. The widget IS
# on the head unit's home screen, so every TC here is exposed.
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
# NOT spec-verbatim: 17.1 says the widget HAS two screens, it never says the
# widget is on the home screen. R-C28's first question fails for a clause
# source, and R-C17 puts "how it got onto the home screen" in Home Screen's
# domain, so this is the tester's setup state.
PC_WIDGET = "1. [test-setup] The Comfort widget is shown on the home screen"
# Axis 16 (50 §1). 17.3 makes the widget's SECOND page conditional, so any
# TC whose observable is that page needs the value stated — including the
# two in 17.1 that merely count or name the screens.
PC_COMFORT_FEATURES = ("[spec-derived] The vehicle is equipped with Comfort "
                       "features, such as heated/vented seats and a heated "
                       "steering wheel (17.3)")

# 64 §1 — these leaves were withheld here and are now generated by
# gen_batch16.py under R-C42 (the clause carries its own condition).
# They stay in this file's arithmetic so the Test Set's leaf count
# still adds up to framework.md's figure — a leaf that moved must
# not look like a leaf that vanished.
MOVED_TO_BATCH16 = ['SWE1-HVAC-127-01', 'SWE1-HVAC-127-02', 'SWE1-HVAC-128-01', 'SWE1-HVAC-128-02']

WITHHELD = [
    ("SWE1-HVAC-129-01",
     "`18.1` 全句與 `17.1` **逐字相同**，唯一區辨者為章標題「10.25\" Home screen」——"
     "**章標題不是條文**，故螢幕尺寸之 PC 連出處都沒有（R-C28 第一問先於軸之問題失敗）；"
     "不補該 PC 而生成，即產出與 `17.1` 完全相同之一組 TC（§4.5／§4.6）"),
    ("SWE1-HVAC-129-02", "同 `129-01`"),
    ("SWE1-HVAC-129-03", "同 `129-01`"),
]


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
        "parent": "SWE1-HVAC-124",
        "outline": "17.1",
        "reasoning":
            "驗證目標：17.1（W0）定出 Comfort widget 具兩個畫面 —— Comfort 與 Seats，三個 037 leaf 分別對應「有兩個畫面」「其一為 Comfort」「其二為 Seats」，一葉一 TC（§8.2.1）。關鍵情境條件：依 **R-C34**，可觀察量為首頁上之 Comfort widget，第九軸暴露（6.3 使 comfort section 自 head unit 移除，widget 即在 head unit 首頁）→ 補；第十三軸暴露（3 旋鈕 ICS 車無 HVAC 畫面）→ 補；EMEA 排除補（ch16 十八節無任何 widget 條文，`ch16_mirror_map.tsv` 之 ch17 側全無列 —— 惟依 **R-C36-1** 該判定不因節級而免除，本節逐條之答為「ch16 無對應句」故排除成立）；第十二軸不補（不觀察 tab）。為什麼這樣切：三者之失效可各自獨立發生（畫面數對而內容錯、或 Seats 頁缺）。刻意略過：**條文之括號「(Refer to the Comfort – Front Comfort/Climate and Comfort – Heated/Vented Seats HMI sections for complete logic.)」為對本 spec 其他節之委派** —— 依 profile §5.3 之判別次序，委派對象為本 spec 之節故指向 `[COVERED-BY]`，惟 **R-C39 條件四不成立**：扣除該委派後仍有獨立餘留（「widget 有兩個畫面且其一為 Comfort、其二為 Seats」本身可驗），故**不標 marker、正常生成**，且本三條**只驗兩個畫面之存在與其名稱，不驗其內容**（內容即被委派者，§8.2.1）；另依 **R-C17**，首頁之頁面管理行為（新增／刪除／重排、widget 拖放）定義於 Home Screen spec，不寫入本批。",
        "keywords": ["Comfort widget", "two screens", "Comfort", "Seats"],
        # 50 §4 — the three TCs overlap, and the overlap is §4.6 (sibling), not
        # §4.5. §4.5 governs which FIELD data belongs in inside ONE TC; these
        # are three TCs against three different leaves, so they are not in its
        # range at all. Recording the §10.6 duplicate_of test explicitly:
        #   -115 trigger: cycle the widget screens      target: HOW MANY there are
        #   -116 trigger: read the first screen          target: WHICH one is first
        #   -117 trigger: move to the second screen      target: WHICH one is second
        # Strict equivalence needs same trigger + outcome + input + verification
        # target. The verification targets differ (count / first identity /
        # second identity), so duplicate_of does NOT apply. Per R-C33 037's
        # unit stands.
        #
        # Recorded on the DOC, not as a new per-TC key: a per-TC field would
        # need a NOT_IN_WORKBOOK ruling (26 §4.1), and `distinguishing_axis`
        # already exists for exactly this. A first attempt did add a per-TC
        # `sibling_token` — it was silently dropped by the doc builder below,
        # which copies named fields only, so json-key-coverage stayed green
        # while the field went nowhere. Dead code that passes every gate.
        "distinguishing_axis": {
            "axis": "verification target within 17.1 (W0)",
            "delta": "-115 = 畫面之數目（two）；-116 = 第一頁之身分（Comfort）；"
                     "-117 = 第二頁之身分（Seats）。§10.6 之嚴格等價四項"
                     "（trigger／outcome／input／verification target）中"
                     "verification target 相異，故不構成 duplicate_of",
        },
        "duplicate_of": "",
        "tcs": [
            {
                "req_id": "SWE1-HVAC-124-01",
                "tc_title": "Comfort widget has two screens",
                # 52 §3 — caught by axis-type-reverse-test's reverse
                # validation: this TC counts the widget screens, and 17.3
                # makes the SECOND one conditional on Comfort Features. Its
                # observable disappears on a vehicle without them while its
                # own subject (17.1's two screens) does not — so the axis-16
                # value has to be stated, or the TC is false on those cars.
                "test_item":
                    "The Comfort widget shall have two screens",
                "pre_conditions": add_lines(PC_WIDGET, PC_COMFORT_FEATURES),
                "spec_ref": ("17.1", "17.3"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the home screen\n"
                    "2. Move through the Comfort widget screens until the "
                    "first screen is shown again",
                "expected_result":
                    "1. The Comfort widget is displayed\n"
                    "2. Two widget screens were shown",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-124-02",
                "tc_title": "First Comfort widget screen is Comfort",
                "test_item":
                    "The first of the two Comfort widget screens shall be "
                    "Comfort",
                "pre_conditions": PC_WIDGET,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the home screen\n"
                    "2. Read the first Comfort widget screen",
                "expected_result":
                    "1. The Comfort widget is displayed\n"
                    "2. The first widget screen is the Comfort screen",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-124-03",
                "tc_title": "Second Comfort widget screen is Seats",
                # 52 §3 — same as -115: the second screen is 17.3-conditional.
                "test_item":
                    "The second of the two Comfort widget screens shall be "
                    "Seats",
                "pre_conditions": add_lines(PC_WIDGET, PC_COMFORT_FEATURES),
                "spec_ref": ("17.1", "17.3"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the home screen\n"
                    "2. Move to the second Comfort widget screen",
                "expected_result":
                    "1. The Comfort widget is displayed\n"
                    "2. The second widget screen is the Seats screen",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-125",
        "outline": "17.2",
        "reasoning":
            "驗證目標：17.2（CW1）定出 Comfort widget 之預設畫面為 Climate 畫面，並列出其所含之六類元素，八個 037 leaf 分別對應「預設畫面」「畫面包含以下」與六個元素，一葉一 TC（§8.2.1）；其中 `-02`「screen includes:」為冒號引導句，**其可觀察量即該六元素之同時呈現**，故以一條驗六者俱在，與各元素之單獨條不重疊（§4.5：前者驗集合、後者驗個別元素之可操作性）。關鍵情境條件：依 **R-C34**，第九軸與第十三軸暴露 → 全數補；EMEA 排除補（ch16 無 widget 條文）；`-06`（MAX A/C）另補第四軸（MAX A/C 有無，出處 2.13），`-05`（SYNC）另補第二軸（非單區，出處 2.11）。為什麼這樣切：六個元素之失效互相獨立（AUTO 在而 SYNC 缺）。刻意略過：**`-08`（12\" Portrait 50% widget 之風速）停下不產列** —— 螢幕尺寸與 widget 尺寸**不在 profile §3.2 之十五軸內**，依該節「配置軸不在既有軸內即停」；其來源問題即 **DR #6**（本次交付出哪幾種螢幕配置），未解。",
        "keywords": ["Comfort widget", "Climate screen", "default screen",
                     "widget elements"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-125-01",
                "tc_title": "Comfort widget defaults to the Climate screen",
                "test_item":
                    "The default screen for the Comfort widget shall be the "
                    "Climate screen",
                "pre_conditions": PC_WIDGET,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Move the Comfort widget to its second screen and "
                    "leave the home screen\n"
                    "2. Open the home screen",
                "expected_result":
                    "1. The home screen is no longer displayed\n"
                    "2. The Comfort widget shows the Climate screen",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-125-02",
                "tc_title": "Climate widget screen shows all its listed elements",
                "test_item":
                    "The Climate screen of the Comfort widget shall include "
                    "driver and passenger temperature, auto button, sync "
                    "button, Max A/C, and airflow modes",
                "pre_conditions": add_lines(
                    PC_WIDGET,
                    "[spec-derived] The vehicle is equipped with MAX A/C, "
                    "whose screens are used when CCM relays its presence "
                    "(2.13)",
                    "[spec-derived] The vehicle is not a single zone climate "
                    "configuration, for which Sync is not shown (2.11)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the home screen\n"
                    "2. Read the Climate screen of the Comfort widget",
                "expected_result":
                    "1. The Comfort widget shows the Climate screen\n"
                    "2. The driver temperature, the passenger temperature, the "
                    "auto button, the sync button, Max A/C and the airflow "
                    "modes are all shown",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("17.2", "2.13", "2.11"),
            },
            {
                "req_id": "SWE1-HVAC-125-03",
                "tc_title": "Widget shows driver and passenger temperature",
                "test_item":
                    "The Climate screen of the Comfort widget shall include "
                    "driver and passenger temperature controls",
                "pre_conditions": PC_WIDGET,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the driver temperature on the Comfort widget\n"
                    "2. Change the driver temperature from the Comfort widget",
                "expected_result":
                    "1. The Comfort widget shows the driver temperature and "
                    "the passenger temperature\n"
                    "2. The Comfort widget shows the new driver temperature",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-125-04",
                "tc_title": "Widget shows the AUTO button",
                "test_item":
                    "The Climate screen of the Comfort widget shall include "
                    "the auto button",
                "pre_conditions": PC_WIDGET,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the Comfort widget for the auto button\n"
                    "2. Press the auto button on the Comfort widget",
                "expected_result":
                    "1. The Comfort widget shows the auto button\n"
                    "2. The auto button changes state",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-125-05",
                "tc_title": "Widget shows the SYNC button",
                "test_item":
                    "The Climate screen of the Comfort widget shall include "
                    "the sync button",
                "pre_conditions": add_lines(
                    PC_WIDGET,
                    "[spec-derived] The vehicle is not a single zone climate "
                    "configuration, for which Sync is not shown (2.11)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the Comfort widget for the sync button\n"
                    "2. Press the sync button on the Comfort widget",
                "expected_result":
                    "1. The Comfort widget shows the sync button\n"
                    "2. The sync button changes state",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("17.2", "2.11"),
            },
            {
                "req_id": "SWE1-HVAC-125-06",
                "tc_title": "Widget shows the Max A/C button",
                "test_item":
                    "The Climate screen of the Comfort widget shall include "
                    "Max A/C",
                "pre_conditions": add_lines(
                    PC_WIDGET,
                    "[spec-derived] The vehicle is equipped with MAX A/C, "
                    "whose screens are used when CCM relays its presence "
                    "(2.13)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the Comfort widget for the Max A/C button\n"
                    "2. Press the Max A/C button on the Comfort widget",
                "expected_result":
                    "1. The Comfort widget shows the Max A/C button\n"
                    "2. The Max A/C button changes state",
                "priority": "P2",
                "design_method": DM_FUNC,
                "spec_ref": ("17.2", "2.13"),
            },
            {
                "req_id": "SWE1-HVAC-125-07",
                "tc_title": "Widget shows the airflow modes",
                "test_item":
                    "The Climate screen of the Comfort widget shall include "
                    "airflow modes",
                "pre_conditions": PC_WIDGET,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the Comfort widget for the airflow modes\n"
                    "2. Select an airflow mode on the Comfort widget",
                "expected_result":
                    "1. The Comfort widget shows the airflow modes\n"
                    "2. The selected airflow mode is shown as active",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-125-08",
                "tc_n": 361,
                "tc_title": "The 12 inch Portrait 50% widget also shows fan speed",
                # 69 §2 — 17.2 writes 12' (apostrophe). The PC was corrected
                # in 67 §2 and this field was not, leaving one TC carrying two
                # spellings of the same identifier.
                "test_item":
                    "The system shall for the 12' Portrait 50% widget also "
                    "display fan speed on the Climate screen of the Comfort "
                    "widget",
                # 67 §2 — quoted verbatim, including the spec's own
                # apostrophe form (12' Portrait, not 12"). R-C42 一 says the
                # PC is the clause's own words; the earlier line was a
                # paraphrase and therefore never fully met it.
                "pre_conditions":
                    "1. [spec-verbatim] 12' Portrait 50% widget also "
                    "includes fan speed (17.2)\n"
                    + PC_WIDGET.split("\n", 1)[0].replace("1. ", "2. "),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the Climate screen of the Comfort widget\n"
                    "2. Read the fan speed on the Comfort widget",
                "expected_result":
                    "1. The Climate screen of the Comfort widget is shown\n"
                    "2. The fan speed is displayed on the Comfort widget",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-126",
        "outline": "17.3",
        "reasoning":
            "驗證目標：17.3（CW2）定出 Comfort widget 之第二畫面含本車所有可用之 Comfort 功能，並定其於無 Comfort 功能之車輛不顯示，三個 037 leaf 對應之，一葉一 TC（§8.2.1）；本輪產 `-01`／`-03` 兩條。關鍵情境條件：本節之配置條件為 profile §3.2 **第十六軸「Comfort Features 有無」**（50 §1 登記，**功能型**）—— 其二值皆為本節之逐字原文，`-01` 取正向值、`-03` 取否定值，出處皆標 17.3；依 **R-C34**，第九軸與第十三軸暴露 → 全數補，EMEA 排除補（ch16 十八節無 widget 條文），第十二軸不補；**第十六軸為功能型故不進 `interface_axis_review` 之鍵**（判定依據見 profile §3.2 之附註）。為什麼這樣切：`-01`（有功能時列出）與 `-03`（無功能時整頁不顯示）為同一條件之兩側，依 §7 各自成條使正負兩向皆被驗，且兩者之失效可獨立發生（頁顯示了但內容不全／頁根本不該顯示卻顯示）。刻意略過：`-01` 之 ER 以條文自舉之二例（Heated/Vented seats、Heated steering wheel）為觀察對象，該二者為 `i.e.` 之明文列舉非造值；**`-02`（50% widget 之駕駛／乘客分列）仍停下** —— widget 尺寸不在既有軸內，與 `125-08`／`127-01`／`127-02` 同因（DR #6）。",
        "keywords": ["second widget screen", "Comfort features",
                     "Heated/Vented seats", "Heated steering wheel"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-126-01",
                "tc_title": "Second widget screen lists the available Comfort features",
                "test_item":
                    "The second Comfort widget screen shall include all "
                    "Comfort features available to the vehicle",
                "pre_conditions": add_lines(
                    PC_WIDGET,
                    "[spec-derived] The vehicle is equipped with Comfort "
                    "features, such as heated/vented seats and a heated "
                    "steering wheel (17.3)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the home screen\n"
                    "2. Move to the second Comfort widget screen",
                "expected_result":
                    "1. The Comfort widget shows the Climate screen\n"
                    "2. The second widget screen shows the Comfort features "
                    "available to the vehicle",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-126-03",
                "tc_title": "Second widget screen is hidden without Comfort features",
                "test_item":
                    "If the vehicle is not equipped with Comfort Features "
                    "this widget page shall not be shown",
                "pre_conditions": add_lines(
                    PC_WIDGET,
                    "[spec-derived] The vehicle is not equipped with Comfort "
                    "Features (17.3)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the home screen\n"
                    "2. Move through the Comfort widget screens until the "
                    "first screen is shown again",
                "expected_result":
                    "1. The Comfort widget shows the Climate screen\n"
                    "2. The second widget screen is not shown",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-126-02",
                "tc_n": 362,
                "tc_title": "The 50% widget separates the features by side",
                "test_item":
                    "The system shall on the 50% widget separate the Comfort "
                    "features between driver and passenger",
                # 67 §2 — quoted verbatim so the qualifier itself is in
                # the pre_condition: "On the 50% widget," is what scopes the
                # clause, and a paraphrase left it out (44 §2.2's finding).
                "pre_conditions":
                    "1. [spec-verbatim] On the 50% widget, these features "
                    "are separated between driver and passenger (17.3)\n"
                    # 69 §1.1 — a paraphrase of CW2's "all Comfort features
                    # available to the vehicle (i.e. …)"; the correspondence
                    # is real, the wording is ours, so the label is derived.
                    "2. [spec-derived] The vehicle is equipped with Comfort "
                    "features, such as heated/vented seats and a heated "
                    "steering wheel (17.3)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the second screen of the 50% Comfort widget\n"
                    "2. Read the Comfort features on that screen",
                "expected_result":
                    "1. The second Comfort widget screen is shown\n"
                    "2. The Comfort features are separated between driver and "
                    "passenger",
                "priority": "P1",
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
            # 64 §1 — R-C42 un-blocked 125-08 and 126-02 AFTER the rest of the
            # corpus was numbered. They take explicit late ids so that nothing
            # renumbers: a renumber is cheap now (prose cites req_id, 60 §1)
            # but it would still rewrite 250 rows of the deliverable for two
            # additions, and that is churn, not information.
            if "tc_n" in tc:
                n_this = tc["tc_n"]
            else:
                n += 1
                n_this = n
            # PC_WIDGET cites 17.1 on every TC, so 17.1 joins spec_ref (R-C29).
            refs = list(tc.get("spec_ref", (o,))) + ["17.1", "2.14", "16.2",
                                                     "6.3"]
            tcs.append({
                "req_id": tc["req_id"],
                "tc_id": TC_ID_FMT.format(n=n_this),
                "tc_title": tc["tc_title"],
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": tc["test_item"],
                "pre_conditions": add_lines(tc["pre_conditions"], EX_ICS,
                                            EX_EMEA, EX_LOWER),
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
                # R-C36-1 — every EMEA exclusion carries a per-TC answer.
                "emea_ics_review": {
                    "ch16_outline": "no-counterpart",
                    "verdict": "yes",
                    "ch16_sentence":
                        "ch16 十八節無任何 widget 條文（`ch16_mirror_map.tsv` "
                        "之 ch17 側全無列）—— 逐條之答為「ch16 無對應句」，"
                        "故 EMEA ICS 車輛上本條無對象，排除成立",
                },
            })
        doc = {
            "parent": b["parent"],
            "outline": o,
            "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": b["reasoning"],
            "keywords": b["keywords"],
            "duplicate_of": b.get("duplicate_of", ""),
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
    for req, why in WITHHELD:
        print(f"- {req}: {why}")
    held = len(WITHHELD)
    moved = len(MOVED_TO_BATCH16)
    print(f"\n{leaves} emitted + {held} withheld + {moved} moved to "
          f"batch 16 (R-C42) = {leaves + held + moved} leaves "
          f"declared for {TEST_SET} (framework.md: 21)")
    if leaves + held + moved != 21 or total != 14:
        raise SystemExit(
            f"expected 21 leaves declared / 14 TCs, got "
            f"{leaves + held + moved} / {total}")


if __name__ == "__main__":
    main()
