#!/usr/bin/env python3
"""Batch 3 generator — Front Climate Anatomy (handoff 32 §5).

Part N group 1 is 2.1, 2.2, 2.14, 6.3 = 16 leaves. The handoff's Layer-3 line
lists only 2.1/2.2/6.3 (12 leaves) while its leaf count says 16 and its §5
asks for 2.14's ICS boundary — framework.md line 39 settles it at four
sections, so 2.14 is in scope. Reported in upstream 21 §1.

Emitted here: 2.2 (8), 6.3 (1), 2.1-03 (1), 2.14 (4) = 14 TCs, -032 … -045.

WITHHELD, 2 leaves — 2.1-01 and 2.1-02. Not an axis problem: the clause says
tabs appear "depending on vehicle configuration" and never says depending on
WHAT, so no known tab set can be established as a pre_condition without
fabricating one (R-C28 first question). Logged as an RD-1 open question,
together with the 037-vs-clause gap that R-C33 settles in the clause's favour.

Rulings applied, each visible in the data below:
  R-C33   the unit is 037's call, the content is the clause's — 2.1's leaves
          say 3 tabs where the clause says 4, so the TCs follow the clause
          and the leaf ids stay 037's
  R-C31   a clause's own execution premise counts as explicit — 2.2 names
          hard controls as the thing being operated, so their presence is
          the sentence's premise, not an addition
  R-C28   every pre_condition answers provenance first; the sentence is
          named in `reasoning`
  R-C29   6.3's premise is stated in 6.3 itself, so no cross-section citation
          arises here; 13.x is NOT the source and is not cited
  §8.2.1  2.14's ICS behaviour belongs to the ICS groups; 6.3's popup rules
          belong to 2.2/ch14. Neither is reached from here
  §7 FF   on-screen / off-screen is established by a step, never assumed

Usage:
    python3 features/comfort/scripts/gen_batch3.py
"""

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_item import apply_test_item   # Pei 2026-08-17 —— 上半照抄條文、下半情境
from splits import apply_splits   # 76 §2 — 依 75 §1（今併入 R-C44 第一問）之列舉判準拆分
from gap_tcs import append_gap   # 97／98 —— 2.1 之四條補產，tc_id 435–438

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "Front Climate Anatomy"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 32               # 001–031 taken by pilot + batch 2 (R-C7)

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"
DM_DECISION = "決策表 (Decision Table Testing)"

# 39 §1.2 — named on both rows so the split reads from the workbook alone.
SPLIT_REASON_002_05 = (
    "§8.3 input_data axis: the temperature unit takes two values with different expected results and they fail independently — Celsius half degrees can be right while Fahrenheit wrongly shows them. 39 §1.2; the EMEA verdict split is what made it visible, not the cause")

# Named on both rows so the split is legible from the workbook alone.
SPLIT_REASON_020_04 = (
    "(§8.2.2 independent partial failures + §7 negative pairing) the main case and the exception are different vehicle configurations with opposite results and can fail independently, so 020-04 splits into two TCs that both trace to it (handoff 34 §2)")

# ---- 35 §1 / R-C34 interface-type axes ------------------------------------
# Per-TC rather than per-batch: which interface an observable sits on differs
# inside 2.2 and 2.14, so the exposure is listed by req_id and stays auditable.
EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")

# ch2 and ch3 are mirrored by ch16 for the EMEA ICS variant (framework.md
# §3.2's four mirrored pairs), so every ch2 TC excludes it. ch6 and ch13 have
# no ICS mirror and are left alone.
# 37 §1 — 2.1 dropped: the mirror map has no ch16 counterpart for it.
EMEA_EXPOSED_SECTIONS = {"2.2", "2.14"}
# 39 §1.1 — per-TC removals, not section-level: the ch16 counterpart covers
# some rows of these sections and not others. 16.14 (ICE13) is two sentences
# where 2.14 (C15) is a paragraph, so 020-01/-02 keep the exclusion while
# 020-03/-04 lose it; likewise 16.17 is one sentence where 2.16 is two.
EMEA_REMOVED_REQ_IDS = {"SWE1-HVAC-020-03", "SWE1-HVAC-020-04"}

# 6.3 removes the head unit's comfort section except for comfort popups.
# Only TCs whose observable IS that section or its category button are
# exposed; a popup-based observable survives 6.3 by the clause's own words.
LOWER_EXPOSED = {
    "SWE1-HVAC-002-03",   # reads the comfort category button's indicator
    "SWE1-HVAC-002-07",   # reads the category button
    "SWE1-HVAC-001-03",   # opens the comfort category
    "SWE1-HVAC-020-03",   # head unit menu — see upstream 24 §2.3
    "SWE1-HVAC-020-04",   # both rows: -046 has no object, -045 would pass
                          # for the wrong reason; the pair must sit on the
                          # same vehicle class
}
# Exempt by req_id, not by section: 020-03 and 020-04 positively require
# 3-knob ICS (or, for -046, name a different value of the same axis), so a
# negated form on top would contradict their own pre_conditions. 020-01 and
# 020-02 read the climate screen like everything else and stay exposed —
# exempting all of 2.14 would have silently covered them too.
ICS_EXEMPT_REQ_IDS = {"SWE1-HVAC-020-03", "SWE1-HVAC-020-04"}


def add_exclusions(pre_conditions: str, *lines: str) -> str:
    n = len([l for l in pre_conditions.split("\n") if l.strip()])
    out = pre_conditions
    for line in lines:
        n += 1
        out = f"{out}\n{n}. {line}"
    return out


# R-C31. 2.2 carries NO "on vehicles with X" selector — unlike 3.1's "On
# vehicles with Tri-Mode climate" or 3.2's "On vehicles with MAX DEF". It
# names hard controls as the thing being operated, so their presence is the
# sentence's execution premise rather than a configuration axis choosing
# between behaviours. The presence or absence of that selector is what
# separates the two cases (upstream 21 §4.1).
PC_CONTROLS = ("1. [spec-derived] The vehicle has climate hard controls and a "
               "climate touchscreen (2.2)")
# Axis 13, cited across sections per R-C29 — 2.2 itself says nothing about
# equipment, and the fact lives in 2.14. Added after the 33 §4.1 re-review:
# a 3-knob-ICS vehicle displays no HVAC screens at all, so every one of 2.2's
# eight TCs is unexecutable there. The "no selector in the clause" reading
# produced an empty candidate list and the substantive answer was not empty.
PC_NOT_ICS = ("2. [spec-derived] The vehicle does not have 3 knob HVAC "
              "controls with ICS, for which no HVAC screens or pop ups are "
              "displayed (2.14)")
# Axis 1 of profile §3.2.
PC_ATC = "2. [spec-derived] The climate system is ATC (2.2)"
PC_MTC = "2. [spec-derived] The climate system is MTC (2.2)"

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
    # ----------------------------------------------------------------- 2.2
    {
        "parent": "SWE1-HVAC-002",
        "outline": "2.2",
        "reasoning":
            "驗證目標：2.2（C1）定義硬鍵與觸控之狀態互相反映，以及使用者在／不在 climate screen 時之呈現差異，八個 037 leaf 分別對應鏡射、popup、狀態列、Sync 抑制、ATC 呈現、MTC 呈現、在 climate screen 之呈現、LED 回饋，一葉一 TC（§8.2.1）。關鍵情境條件：硬鍵與觸控之存在依 R-C31 為句子之執行前提，標 spec-derived 並具名「Whenever changes to the climate system are made via hard controls or touchscreen」；另依 33 §4.1 之實質複查補第十三軸之排除項，標 (2.14) 並具名「no HVAC menu bar icons, no HVAC screens and no HVAC pop ups will be displayed」——3 旋鈕 ICS 之車輛無氣候觸控畫面，本節八條於該車皆不可執行，故 2.14 依 R-C29 併入 specification_reference，僅取其裝備事實而不驗其行為（§8.2.1）；-05／-06 另取 profile §3.2 第一軸 ATC／MTC，其第一問由「for ATC it will display the degree」「for MTC (if the MTC has a Climate screen)」兩句明文對應；-04 之 passenger side 蘊含雙區以上，取第二軸。為什麼這樣切：八者之失效互相獨立（狀態列正確而 popup 逾時錯、ATC 呈現正確而 MTC 呈現錯），且分屬不同觀察位置，合併後無法定位。**-05 依 39 §1.2 拆為攝氏、華氏二條**（§8.3 之 input_data 軸，兩值之預期結果不同且各自獨立可失效），拆後 design_method 由決策表改為功能測試（單一單位下之顯示檢查，R-C19）；**華氏條之 EMEA 排除式 PC 已移除** —— ICE1 有「or half degree increments for Celsius」而**無 C1 之「and for Fahrenheit do not show half degrees」**，攝氏條之排除則維持。刻意略過：「timeout after 3 sec」之秒數為條文明載故照用（R-C22 不適用），而 popup 之樣式、尺寸與動畫本節未定義，不寫入；-06 之「if the MTC has a Climate screen」為條文自身之限定語，照錄為 pre_condition，其非獨立配置變數而為第十三軸之後果，依 33 §3 不另立軸。",
        "keywords": ["hard controls", "touchscreen", "pop-up", "status bar",
                     "Sync", "ATC", "MTC", "LED"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-002-01",
                "tc_title": "Hard control and touchscreen changes mirror each other",
                "test_item":
                    "Whenever changes to the climate system are made via hard "
                    "controls or touchscreen, these changes shall be reflected "
                    "in both locations",
                "pre_conditions": PC_CONTROLS,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control\n"
                    "3. Change the temperature on the climate screen",
                "expected_result":
                    "1. The climate screen shows the current fan speed and "
                    "temperature\n"
                    "2. The fan speed shown on the climate screen is the one "
                    "set by the hard control\n"
                    "3. The temperature indicated by the hard controls is the "
                    "one set on the climate screen",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-002-02",
                "tc_title": "Pop-up appears off the climate screen and times out",
                "test_item":
                    "Whenever fan speed or temperature hard controls are used "
                    "(even if at highest/lowest setting), according pop-ups "
                    "shall be shown if NOT on climate screen, and shall time "
                    "out after 3 sec",
                "pre_conditions": PC_CONTROLS,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen other than the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control\n"
                    "3. Do not interact with the head unit for 3 seconds",
                "expected_result":
                    "1. The climate screen is not displayed\n"
                    "2. A fan speed pop-up is shown\n"
                    "3. The fan speed pop-up is no longer shown",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-002-03",
                "tc_title": "Status bar and category button indicator follow the change",
                "test_item":
                    "Whenever fan speed or temperature hard controls are used, "
                    "the changes shall be reflected in the status bar and in "
                    "the status indicator on the category button",
                "pre_conditions": PC_CONTROLS,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen other than the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control\n"
                    "3. Read the status indicator on the comfort category "
                    "button",
                "expected_result":
                    "1. The climate screen is not displayed\n"
                    "2. The status bar shows the new fan speed\n"
                    "3. The status indicator on the comfort category button "
                    "shows the new fan speed",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-002-04",
                "tc_title": "Sync suppresses the passenger side slider pop-up",
                "test_item":
                    "When sync'd, the system shall not show the slider pop-up "
                    "on the passenger side when the driver slider is adjusted",
                "pre_conditions":
                    f"{PC_CONTROLS}\n"
                    "2. [spec-derived] The vehicle has a passenger side "
                    "temperature control (2.2)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn Sync on\n"
                    "2. Adjust the driver temperature slider",
                "expected_result":
                    "1. Sync is on\n"
                    "2. No slider pop-up is shown on the passenger side",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-002-05",
                "tc_title": "ATC pop-up shows half degree increments for Celsius",
                "test_item":
                    "If the user is outside of the climate main category and "
                    "the temperature is changed through hard controls, for ATC "
                    "the pop-up shall display the degree being set, in half degree increments for Celsius",
                "pre_conditions": f"{PC_CONTROLS}\n{PC_ATC}",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen outside the climate main category\n"
                    "2. Set the temperature unit to Celsius\n"
                    "3. Change the temperature using the temperature hard "
                    "control",
                "expected_result":
                    "1. The climate main category is not displayed\n"
                    "2. The temperature unit is Celsius\n"
                    "3. A pop-up comes down from the temperature in the status bar and displays the degree being set, in half degree increments",
                "priority": "P1",
                "spec_ref": ("2.2",),
                "design_method": DM_FUNC,
                "split_flag": True,
                "split_reason": SPLIT_REASON_002_05,
            },
            {
                "req_id": "SWE1-HVAC-002-05",
                "tc_title": "ATC pop-up shows no half degrees for Fahrenheit",
                "no_emea": True,   # 39 §1.2 — ICE1 lacks the Fahrenheit sentence
                "test_item":
                    "If the user is outside of the climate main category and "
                    "the temperature is changed through hard controls, for ATC "
                    "the pop-up shall display the degree being set, and for Fahrenheit it shall not show half degrees",
                "pre_conditions": f"{PC_CONTROLS}\n{PC_ATC}",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen outside the climate main category\n"
                    "2. Set the temperature unit to Fahrenheit\n"
                    "3. Change the temperature using the temperature hard "
                    "control",
                "expected_result":
                    "1. The climate main category is not displayed\n"
                    "2. The temperature unit is Fahrenheit\n"
                    "3. A pop-up comes down from the temperature in the status bar and displays the degree being set, without half degrees",
                "priority": "P1",
                "spec_ref": ("2.2",),
                "design_method": DM_FUNC,
                "split_flag": True,
                "split_reason": SPLIT_REASON_002_05,
            },
            {
                "req_id": "SWE1-HVAC-002-06",
                "tc_title": "MTC pop-up shows a slider bar with the arrow at the setting",
                "test_item":
                    "If the user is outside of the climate main category and "
                    "the temperature is changed through hard controls, for MTC "
                    "the pop-up shall display a slider bar with the arrow "
                    "pointing to the current setting, and this information "
                    "shall change as the user alters the temp",
                "pre_conditions":
                    f"{PC_CONTROLS}\n{PC_MTC}\n"
                    "3. [spec-derived] The MTC has a Climate screen (2.2)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen outside the climate main category\n"
                    "2. Change the temperature using the temperature hard "
                    "control\n"
                    "3. Continue altering the temperature using the "
                    "temperature hard control",
                "expected_result":
                    "1. The climate main category is not displayed\n"
                    "2. A pop-up comes down from the temperature in the status "
                    "bar and displays a slider bar with the arrow pointing to "
                    "the current setting\n"
                    "3. The arrow moves with the temperature being set",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-002-07",
                "tc_title": "On the climate screen no status bar pop-up is shown",
                "test_item":
                    "If on climate screen, status changes shall be indicated "
                    "directly on the touchscreen buttons and the status "
                    "indicator on the category button, and shall not be shown "
                    "in the status bar",
                "pre_conditions": PC_CONTROLS,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control\n"
                    "3. Read the status bar",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. The new fan speed is indicated on the climate screen's "
                    "touchscreen buttons and on the status indicator on the "
                    "category button\n"
                    "3. No pop-up is shown in the status bar",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-002-08",
                "tc_title": "Hard control LEDs follow a change made on the climate screen",
                "test_item":
                    "If changes are made on climate screen, LEDs on hard "
                    "controls shall reflect the new status",
                "pre_conditions": PC_CONTROLS,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed on the climate screen\n"
                    "3. Read the LEDs on the fan speed hard control",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. The climate screen shows the new fan speed\n"
                    "3. The LEDs on the fan speed hard control show the new "
                    "fan speed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    # ----------------------------------------------------------------- 6.3
    {
        "parent": "SWE1-HVAC-027",
        "outline": "6.3",
        "reasoning":
            "驗證目標：6.3（CM1）規定車輛配備含 comfort 資訊之 non-foldable secondary lower screen 時，head unit 之 comfort section 移除而 comfort popups 除外，單一 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第九軸 secondary lower screen 之來源節即本節，其 R-C28 第一問由本節自身之句「When a vehicle is configured with a non-foldable secondary lower screen that contains comfort information」明文對應，標 spec-verbatim —— **措辭取自 6.3 自身，不引 13.x**（19 §2.1 明禁跨節套用措辭，且 13.x 之「the lower screen」為另一節之文字）。為什麼這樣切：本節只定出一個移除結果與一個除外項，無分支可分。刻意略過：comfort popup **自身之出現規則**定義於 2.2 與 ch14，本 TC 只驗「移除後 popup 仍在」此一 6.3 明文之事實，不驗 popup 之觸發條件、樣式或逾時（§8.2.1 不得擴張至 sibling Req）；「comfort section」之具體範圍本節未列舉，故 ER 以該詞本身判定而不列舉其子項（§8.4.1）。",
        "keywords": ["non-foldable secondary lower screen", "comfort section",
                     "head unit", "comfort popups"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-027",
                "tc_title": "Comfort section is removed from the head unit except popups",
                "test_item":
                    "When a vehicle is configured with a non-foldable "
                    "secondary lower screen that contains comfort information, "
                    "the comfort section shall be removed from the head unit "
                    "except for comfort popups",
                "pre_conditions":
                    "1. [spec-derived] The vehicle is configured with a "
                    "non-foldable secondary lower screen that contains comfort "
                    "information (6.3)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the head unit menu\n"
                    "2. Read the head unit menu for the comfort section\n"
                    "3. Change the fan speed using the fan speed hard control",
                "expected_result":
                    "1. The head unit menu is displayed\n"
                    "2. The comfort section is not present on the head unit\n"
                    "3. A comfort pop-up is shown on the head unit",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    # ----------------------------------------------------------------- 2.1
    {
        "parent": "SWE1-HVAC-001",
        "outline": "2.1",
        "reasoning":
            "驗證目標：2.1（R1C1）定出 comfort category 之 tab 數、順序，以及僅前排氣候時不顯示 tab，三個 037 leaf 分別對應之，一葉一 TC（§8.2.1）；本輪只生成 -03，-01／-02 之情形見下。關鍵情境條件：-03 取 profile §3.2 第十二軸「僅前排氣候」，其 R-C28 第一問由本節明文「If only Front climate is available in a specific vehicle the tabs will not be displayed」對應，標 spec-verbatim，出處與所屬節同一故 specification_reference 僅列本節。為什麼這樣切：037 之切分為單位權威（§8.2），未合併未拆分；-01（tab 數）與 -02（順序）**不生成**，因條文只寫「depending on vehicle configuration」而未述何種配置產生何種 tab，任何具體配置之 pre_condition 皆為造值（R-C28 第一問／§8.4.1），此為內容不足而非軸不足，已登 RD-1 待答。**EMEA ICS 排除式 PC 已依 37 §1 移除**（`ch16_mirror_map.tsv` 判 2.1 為 no-counterpart —— ch16 十八節無 comfort category tabs 之對應節）。刻意略過：037 之 -01 寫 up to 3 tabs、-02 之順序無 Massage，而條文為 up to 4 tabs 且順序含 Massage —— 依 **R-C33** 內容以條文為準、單位以 037 為準，該落差已登 A-CF21 並列 RD-1；Massage tab 之**行為**由條文明文委派他份文件，但其**是否顯示**仍屬本節，兩者不混（§8.2.1）；**A-CF23 之逐條複查（42 §4 之名單重建）**：037 對本 leaf 之描述帶 3 張圖，`-03` 所驗者為「tab 一個都不顯示」，其判讀只需認得 tab 之有無而不需知其外觀，故**不依賴圖片所載內容** —— **惟未生成之 `-01`（tab 數）與 `-02`（順序）恰恰相反**，那兩者所缺的正是「哪一種配置產生哪一組 tab」（DATA_REQUESTS #17），而圖片極可能載之，故該二 leaf 解封時須先讀圖。",
        "keywords": ["comfort category", "tabs", "Front", "Massage",
                     "only Front climate"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-001-03",
                "tc_title": "No tabs are displayed when only Front climate is available",
                "test_item":
                    "If only Front climate is available in a specific vehicle, "
                    "the tabs shall not be displayed",
                "pre_conditions":
                    "1. [spec-derived] Only Front climate is available in the "
                    "vehicle (2.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the comfort category\n"
                    "2. Read the comfort category for tabs",
                "expected_result":
                    "1. The comfort category is displayed\n"
                    "2. No tabs are displayed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
        ],
    },
    # ---------------------------------------------------------------- 2.14
    {
        "parent": "SWE1-HVAC-020",
        "outline": "2.14",
        "reasoning":
            "驗證目標：2.14（C15）定出 MTC 相對 ATC 之兩項缺項（無離散溫度設定、無 Auto 控制），以及 3 旋鈕 ICS 車輛之 HVAC 觸控 UI 不顯示，四個 037 leaf 分別對應之，一葉一 TC（§8.2.1）。關鍵情境條件：-01／-02 取第一軸 MTC，其第一問由「MTC climate is primarily differentiated from ATC by the lack of discrete temperature settings and \"Auto\" control over the set temperature」對應；-03／-04 另取 profile §3.2 第十三軸「3 旋鈕 ICS」，其第一問由「For MTC with ICS … certain types of physical knobs (3 knob HVAC controls)」對應，**該軸指 ch2 之實體旋鈕配置，非市場／變體軸之 EMEA ICS（ch16 全章）**，兩者外觀皆含 ICS 而所指不同（33 §3）。為什麼這樣切：-03 驗機制（螢幕無重複互動），-04 驗其三項具體後果（無 menu bar icon、無畫面、無 popup），037 給了兩個 leaf 故不合併（§8.2）；**-03 之 037 描述「no mismatch occurs」係條文之目的子句「in order to prevent a mismatch」，目的不是可觀察量，故被驗證者為其機制句**（R-C22；且 3 旋鈕 ICS 車上無螢幕，mismatch 於該配置本就無從觀察，以它為 ER 將產生永遠無法判定之 TC）。-04 依 §8.2.2「independent partial failures」與 §7（列舉之支援項須配負向對照）拆為主情形與例外二條，同溯該 leaf。刻意略過：ICS 自身之行為（旋鈕如何運作、ICS 畫面之內容）屬 ICS Anatomy 與 ICS Climate Modes 兩組，本批只驗 head unit 上之**缺席**此一 2.14 明文之事實，觀察位置不同（§8.2.1）；**-03／-04 之 EMEA 排除式 PC 與 16.2 引用已依 39 §1.1 移除**，因 ICE13 全文僅兩句而不含 C15 之 3 旋鈕 ICS 段落，-01／-02 之排除則因落在 ICE13 第二句內而維持；-04 之例外情形「one zone MTC with push button TEMPERATURE」為另一種車輛配置，無法與主情形共用 pre_conditions，本批未生成其 TC，已於上繳 22 §5.3 列為覆蓋缺口待裁。",
        "keywords": ["MTC", "ATC", "discrete temperature", "Auto",
                     "3 knob HVAC controls", "ICS", "menu bar icons"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-020-01",
                "tc_title": "MTC shows no discrete temperature setting",
                "test_item":
                    "MTC climate shall be differentiated from ATC by the lack "
                    "of discrete temperature settings",
                "pre_conditions":
                    "1. [spec-derived] The climate system is MTC (2.14)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Read the temperature control on the climate screen",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. No discrete temperature setting is displayed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-020-02",
                "tc_title": "MTC offers no Auto control over the set temperature",
                "test_item":
                    "MTC climate shall be differentiated from ATC by the lack "
                    "of \"Auto\" control over the set temperature",
                "pre_conditions":
                    "1. [spec-derived] The climate system is MTC (2.14)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Read the climate screen for an \"Auto\" control over "
                    "the set temperature",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. No \"Auto\" control over the set temperature is "
                    "available",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-020-03",
                "tc_title": "Screen offers no redundant interaction with the 3 knob controls",
                "test_item":
                    "For MTC with ICS, there shall be no redundant interaction "
                    "with the screen for 3 knob HVAC controls, in order to "
                    "prevent a mismatch between the soft and hard controls",
                "pre_conditions":
                    "1. [spec-derived] The climate system is MTC (2.14)\n"
                    "2. [spec-derived] The vehicle has 3 knob HVAC controls "
                    "with ICS (2.14)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the head unit menu\n"
                    "2. Read the head unit menu for an HVAC interaction that "
                    "duplicates the 3 knob HVAC controls",
                "expected_result":
                    "1. The head unit menu is displayed\n"
                    "2. The head unit offers no interaction that duplicates "
                    "the 3 knob HVAC controls",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-020-04",
                "tc_title": "No HVAC icons screens or pop-ups with 3 knob ICS controls",
                "test_item":
                    "For MTC with ICS and 3 knob HVAC controls, no HVAC menu "
                    "bar icons, no HVAC screens and no HVAC pop ups shall be "
                    "displayed",
                "pre_conditions":
                    "1. [spec-derived] The climate system is MTC (2.14)\n"
                    "2. [spec-derived] The vehicle has 3 knob HVAC controls "
                    "with ICS (2.14)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the head unit menu\n"
                    "2. Read the menu bar for HVAC icons\n"
                    "3. Change the temperature using the HVAC knob",
                "expected_result":
                    "1. The head unit menu is displayed\n"
                    "2. No HVAC menu bar icon is displayed\n"
                    "3. No HVAC screen and no HVAC pop up is displayed",
                "priority": "P1",
                "design_method": DM_FUNC,
                "split_flag": True,
                "split_reason": SPLIT_REASON_020_04,
            },
            {
                "req_id": "SWE1-HVAC-020-04",
                "tc_title": "HVAC UI is shown for one zone MTC with push button temperature",
                "test_item":
                    "For one zone MTC with push button TEMPERATURE and hard "
                    "controls that would not create a mismatch between hard "
                    "controls, the exception shall not apply, and the HVAC "
                    "menu bar icons, screens and pop ups shall be displayed",
                "pre_conditions":
                    "1. [spec-derived] The climate system is MTC (2.14)\n"
                    "2. [spec-derived] The vehicle is one zone MTC with push "
                    "button TEMPERATURE and hard controls that would not "
                    "create a mismatch between hard controls (2.14)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the head unit menu\n"
                    "2. Read the menu bar for HVAC icons\n"
                    "3. Change the temperature using the push button "
                    "TEMPERATURE hard control",
                "expected_result":
                    "1. The head unit menu is displayed\n"
                    "2. An HVAC menu bar icon is displayed\n"
                    "3. An HVAC pop up is displayed",
                "priority": "P1",
                "design_method": DM_FUNC,
                "split_flag": True,
                "split_reason": SPLIT_REASON_020_04,
            },
        ],
    },
]

# Named on every run so the stop is visible rather than being an absence
# nobody notices (R-C24's principle applied to scope, as in batch 2).
# 97 §1 之判準訂正使兩者之停下理由失效 ——「不知道誰適用」與「不知道有哪些」
# 是兩件事：條文把四個 tab 逐字列出、順序給定、上界給定，未給者僅「哪台車給
# 哪一組」，而那是測試員面對實車時看得見的事。98 §A／§B 依 **R-C33** 定其
# 內容取條文（4 tabs、順序含 Massage），落差為 RD-1 既有記載 A-CF21。
# 兩葉之列見 `gap_tcs.py`（tc_id 435–438），本清單因而為空。
WITHHELD = []


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    OUT.mkdir(parents=True, exist_ok=True)
    from gap_tcs import gap_for
    gap_rows = gap_for("SWE1-HVAC-" + "001")   # 字串組出：見 gen_batch17.py 之 PARENT()
    n = START_N - 1
    total = 0

    for b in BATCHES:
        o = b["outline"]
        if o not in full:
            raise SystemExit(f"{o} not in section_fulltext.tsv")
        tcs = []
        for tc in b["tcs"]:
            n += 1
            ex, refs = [], list(tc.get("spec_ref", (o,)))
            if tc["req_id"] not in ICS_EXEMPT_REQ_IDS:
                ex.append(EX_ICS)
                refs.append("2.14")
            if (o in EMEA_EXPOSED_SECTIONS
                    and tc["req_id"] not in EMEA_REMOVED_REQ_IDS
                    and not tc.get("no_emea")):
                ex.append(EX_EMEA)
                refs.append("16.2")
            if tc["req_id"] in LOWER_EXPOSED:
                ex.append(EX_LOWER)
                refs.append("6.3")
            refs = list(dict.fromkeys(refs))
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
                    f"{STEM}_{x}" for x in refs),
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
        tcs = append_gap(tcs, b["parent"])
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
            "tcs": apply_test_item(apply_splits(tcs)),
        }
        (OUT / f"{b['parent']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{b['parent']}  {o:8} {len(tcs)} TC  -> generated/{b['parent']}.json")

    leaves = len({tc["req_id"] for b in BATCHES for tc in b["tcs"]}
                 | {r["req_id"] for r in gap_rows})
    print(f"\n{leaves} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print("\nWITHHELD — stop-and-report, no row produced (28 §2.1(b)):")
    for o, parent, k, why in WITHHELD:
        print(f"- {o} ({parent}, {k} leaf): {why}")
    held = sum(k for _, _, k, _ in WITHHELD)
    print(f"\n{leaves} emitted + {held} withheld = {leaves + held} leaves "
          f"declared for {TEST_SET} (framework.md: 16)")
    if leaves + held != 16:
        raise SystemExit(f"expected 16 leaves declared, got {leaves + held}")
    if total != 20:
        raise SystemExit(f"expected 20 TCs（16 ＋ 97／98 之 4）, emitted {total}")


if __name__ == "__main__":
    main()
