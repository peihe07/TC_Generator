#!/usr/bin/env python3
"""Batch 2 generator — Tri-Mode Climate (handoff 28 §2).

All 14 leaves of Tri-Mode Climate: 3.1 (3), 3.2 (8), 3.3 (2), 3.4 (1),
tc_id NR1L-ComfortHMI-015 … -028.

3.3 and 3.4 were withheld in the first pass — they need configuration axes
profile §3.2's nine did not carry. Handoff 29 §2 added the tenth (REAR
DEFROST presence) and eleventh (soft top body), both sourced to 3.4, and
R-C29 settled how a pre_condition cites a section other than its own. The
11 already-emitted TCs were not regenerated for it; nothing in them changed.

§8.2.2 was tested against every leaf and no split was taken; the reasoning
for the two that came closest (024-02's seven simultaneous effects and
024-07's four independent breakers) is in upstream 18 §4. Both keep
procedure/ER 1:1 by enumerating the observations as steps, which preserves
locatability without inventing TCs the spec does not distinguish.

Rulings applied, each visible in the data below:
  R-C28   every pre_condition line answers provenance first; the clause
          sentence it rests on is named in `reasoning`
  R-C18   clause text comes from section_fulltext.tsv, never the title
  R-C22   no fabricated magnitude — 3.2's "set time" has no number in the
          clause, so the procedure waits on the observable, not a duration
  R-C29   a pre_condition's section marker points at where the FACT is
          stated, not at the TC's own section; the cited section joins
          specification_reference and reasoning says why
  §8.2.1  2.10 (Climate Modes) owns both the greyed-out treatment and the
          press-to-restore behaviour; 3.3's TCs stay on "available" and do
          not reach for either
  §7 FF   the starting mode of a cycle is established by a step, never
          assumed as a pre_condition

Usage:
    python3 features/comfort/scripts/gen_batch2.py
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
TEST_SET = "Tri-Mode Climate"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 15                   # pilot occupies 001–014 (R-C7: by position)

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"
DM_DECISION = "決策表 (Decision Table Testing)"

# handoff 30 §1.4. Named on every one of the four rows that carry it, so
# the split is legible from the workbook alone rather than only from here.
SPLIT_REASON = (
    "§8.2.2 control-entity criterion: the four breakers are four different control entities and fail independently, so the leaf splits into four TCs that all trace to it (handoff 30 §1)")

# Axis 3 of profile §3.2. Verbatim: "On vehicles with Tri-Mode climate".
PC_TRIMODE = ("1. [spec-derived] The vehicle is equipped with Tri-Mode "
              "climate (3.1)")
# Axis 5 of profile §3.2. Verbatim: "On vehicles with MAX DEF".
PC_MAXDEF = "1. [spec-derived] The vehicle is equipped with MAX DEF (3.2)"
# 43 §5 / DR #29 — C20 hard-codes MAX DEF's top fan speed as "(7/7)", but
# C6.1 states that some vehicles run Off, 1-8, where the top is 8. The ER
# cannot be rewritten (8/8 would be fabricated, "the highest setting" would
# be weaker than the clause), so the TC is CONFINED instead: axis 14 is the
# configuration variable, and naming its value makes the existing ER true.
# The Off,1-8 side stays uncovered and is tracked by DR #29, not absorbed.
PC_FAN_1_7 = ("[spec-derived] The front HVAC fan range of the vehicle is "
              "Off, 1-7 (2.7)")
# Same fact, same marker — but here it is a CROSS-section citation, because
# 3.3\u0027s own clause states no equipment condition (R-C29).
PC_MAXDEF_X = PC_MAXDEF
# The clause names the control ("Pressing the hard control MODE button"); the
# vehicle's having one is derived from that sentence, not assumed.
PC_MODE_HC = ("2. [spec-derived] The vehicle has a hard control MODE "
              "button (3.1)")
# Axis 10 (29 §2). Sourced to 3.4, NOT to 3.3 — C21 is a single sentence with
# no equipment condition in it at all, so marking this (3.3) would fail
# R-C28's first question. R-C29 is what makes the (3.4) marker legal.
PC_REARDEF = ("2. [spec-derived] Rear defrost is present in the "
              "vehicle (3.4)")
# Axis 11 (29 §2). "soft top" is the criterion; JL/JT is the clause's own
# example and is carried as one — writing "JL or JT" narrows an illustration
# into an enumeration, which is §8.4.1 run backwards.
PC_SOFTTOP = ("1. [spec-derived] The vehicle is a soft top vehicle, such as "
              "JL/JT (3.4)")
# 3.3 and 3.4 cite sections beyond their own (R-C29 obligation 1). The TC's
# own section leads; the sections a pre_condition draws its fact from follow.
def ref(*outlines):
    return "; ".join(f"{STEM}_{o}" for o in outlines)

# ---- 35 §1 / R-C34 interface-type axes ------------------------------------
# An interface-type axis removes the surface an observable sits on while the
# function may still exist. Three of them bite here; each exclusion names the
# section that states the fact (R-C29), and that section joins spec_ref.
EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")


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


# 37 §1 — sections whose ch16 counterpart does not exist (mirror map's
# no-counterpart rows). The EMEA exclusion rested on "ch2/ch3 is mirrored
# by ch16"; for these that premise is false, so the PC and its 16.2
# citation both go. The other sections keep theirs — they are `mirrored`.
NO_CH16_COUNTERPART = {"2.1", "3.1", "3.4"}

BATCHES = [
    # ----------------------------------------------------------------- 3.1
    {
        "parent": "SWE1-HVAC-023",
        "outline": "3.1",
        "reasoning":
            "驗證目標：3.1（C19）定義 Tri-Mode 之三個 airflow mode 按鈕與 MODE 硬鍵之循環，三個 037 leaf 分別對應「個別 toggle」「單向循環順序」「多向前後移動」，三者之操作元件與失效形態互異，故一葉一 TC（§8.2.1）。關鍵情境條件：配置軸取 profile §3.2 第三軸「tri-mode 有無」，其 R-C28 第一問由條文首句「On vehicles with Tri-Mode climate」明文對應，標 spec-verbatim；硬鍵之存在由「Pressing the hard control MODE button」一句推得，標 spec-derived。為什麼這樣切：三條之失效可各自獨立發生（個別 toggle 正常而循環順序錯，或循環正常而反向移動錯），合併後無法定位。**EMEA ICS 排除式 PC 已依 37 §1 移除** —— `ch16_mirror_map.tsv` 判 3.1 為 no-counterpart（16.12 ICE11 為 5 states 單選，非 tri-mode 之三鍵組合），原排除建立在「ch2／ch3 於 ch16 有對應」此一對本節為假之前提上。刻意略過：條文列出七種組合而未定義開機預設模式，故循環之起點由 procedure 第一步建立而非寫入 pre_conditions（§7 FF ＋ R-C28 第三問）；「7 possible distribution modes」之計數本身不另立 TC，它是 -02 循環之結果而非獨立行為；**A-CF23 之逐條複查（41 §5）**：037 對本 leaf 之描述帶 6 張圖，逐條問「所驗行為是否依賴圖片所載內容」——`-01` 之個別 toggle 邏輯、`-02` 之七組合循環順序、`-03` 之前後移動方向**皆由 C19 之文字明載**，該三者不依賴圖；**惟三條之 ER 皆以「toggled ON」／「active」陳述狀態，而 tri-mode 三鍵之 ON 態如何呈現，C19 全句未定義**（C13 之 highlighting the button and increasing button size 屬 2.12 之四模式，於 tri-mode 車不適用），該呈現形式現無涵蓋，已記入 A-CF23 之影響清單。",
        "keywords": ["Tri-Mode Climate", "airflow mode", "Windshield",
                     "Face", "Feet", "MODE"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-023-01",
                "tc_title": "Each Tri-Mode airflow button toggles independently",
                "test_item":
                    "On vehicles with Tri-Mode climate, each of the three "
                    "airflow mode buttons (Windshield, Face, Feet) on the "
                    "Tri-Mode Climate screen shall be pressable to "
                    "individually toggle that mode ON / OFF",
                "pre_conditions": PC_TRIMODE,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the Tri-Mode Climate screen\n"
                    "2. Press the \"Face\" mode button\n"
                    "3. Press the \"Face\" mode button again\n"
                    "4. Press the \"Feet\" mode button\n"
                    "5. Press the \"Windshield\" mode button",
                "expected_result":
                    "1. The Tri-Mode Climate screen shows the \"Windshield\", "
                    "\"Face\" and \"Feet\" mode buttons\n"
                    "2. The Face mode is toggled ON and the Windshield and "
                    "Feet modes are unchanged\n"
                    "3. The Face mode is toggled OFF and the Windshield and "
                    "Feet modes are unchanged\n"
                    "4. The Feet mode is toggled ON and the Windshield and "
                    "Face modes are unchanged\n"
                    "5. The Windshield mode is toggled ON and the Face and "
                    "Feet modes are unchanged",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-023-02",
                "tc_title": "MODE hard control cycles the airflow combinations in order",
                "test_item":
                    "On vehicles with Tri-Mode climate, pressing the hard "
                    "control MODE button shall cycle through all MODE "
                    "combinations in the order Face, Face & Feet, Feet, "
                    "Windshield & Feet, Windshield, Windshield & Face, "
                    "Windshield & Face & Feet, and shall loop at the end of "
                    "each cycle",
                "pre_conditions": f"{PC_TRIMODE}\n{PC_MODE_HC}",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press the hard control MODE button repeatedly until "
                    "the Face mode alone is active\n"
                    "2. Press the hard control MODE button\n"
                    "3. Press the hard control MODE button\n"
                    "4. Press the hard control MODE button\n"
                    "5. Press the hard control MODE button\n"
                    "6. Press the hard control MODE button\n"
                    "7. Press the hard control MODE button\n"
                    "8. Press the hard control MODE button",
                "expected_result":
                    "1. Only the Face mode is active\n"
                    "2. The Face and Feet modes are active\n"
                    "3. Only the Feet mode is active\n"
                    "4. The Windshield and Feet modes are active\n"
                    "5. Only the Windshield mode is active\n"
                    "6. The Windshield and Face modes are active\n"
                    "7. The Windshield, Face and Feet modes are active\n"
                    "8. Only the Face mode is active",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-023-03",
                "tc_title": "Multi-directional MODE control moves forward and backward",
                "test_item":
                    "If the MODE button is a multi-directional toggle or a "
                    "hard control that allows 2 controls (UP/DOWN or "
                    "RIGHT/LEFT), toggling UP (or RIGHT) shall move forward "
                    "in the order of airflow mode combinations and toggling "
                    "DOWN (or LEFT) shall move backwards through the cycle",
                "pre_conditions":
                    f"{PC_TRIMODE}\n"
                    "2. [spec-derived] The MODE button is a multi-directional "
                    "toggle or a hard control that allows 2 controls (UP/DOWN "
                    "or RIGHT/LEFT) (3.1)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Toggle the MODE control repeatedly until the Face mode "
                    "alone is active\n"
                    "2. Toggle the MODE control UP (or RIGHT)\n"
                    "3. Toggle the MODE control UP (or RIGHT)\n"
                    "4. Toggle the MODE control DOWN (or LEFT)\n"
                    "5. Toggle the MODE control DOWN (or LEFT)",
                "expected_result":
                    "1. Only the Face mode is active\n"
                    "2. The Face and Feet modes are active\n"
                    "3. Only the Feet mode is active\n"
                    "4. The Face and Feet modes are active\n"
                    "5. Only the Face mode is active",
                "priority": "P1",
                "design_method": DM_STATE,
            },
        ],
    },
    # ----------------------------------------------------------------- 3.2
    {
        "parent": "SWE1-HVAC-024",
        "outline": "3.2",
        "reasoning":
            "驗證目標：3.2（C20）定義 MAX DEF 之取代關係、開啟時之連動設定、自動關閉，以及六種「破壞／不破壞」之區別，八個 037 leaf 逐一對應，故一葉一 TC（§8.2.1）。關鍵情境條件：配置軸取 profile §3.2 第五軸「MAX DEF 有無」，其 R-C28 第一問由條文首句「On vehicles with MAX DEF」明文對應，標 spec-verbatim；-06 另需第四軸「MAX A/C 有無」，其第一問由「Similarly, pressing MAX A/C turns MAX DEF off」一句推得該功能存在，標 spec-derived。為什麼這樣切：-02（七項連動）為一個 trigger 之七個 outcome，依 §5.7 保持一條並以列舉式步驟維持 procedure／ER 1:1；-07（溫度／RECIRC／mode／再按 MAX DEF）為四個不同控制實體且各自獨立可失效，依 §8.2.2 之控制實體判準拆為四條並同溯該 leaf，其 design_method 於拆後由決策表改為狀態轉換（拆後各為單一狀態遷移，§12）；-08（風速改變不破壞）維持一條，其 §7 negative 配對對象為拆後之四條全體，非其中任一條。刻意略過：**ch10（ECO HVAC）未述其與本節之差異** —— 實測 ch10 全章對 `MAX DEF`／`defrost`／`break` **零命中**，故依 39 §3 分支二，`024-05`（按 AUTO 中斷 MAX DEF）**不補排除式 PC、不改 ER**，3.2 之字面於 BEV 亦成立，惟**配備 ECO HVAC 之 BEV 上「進入 AUTO」究為 AUTO ECO 抑或 AUTO ON，兩側條文皆未述，已依 §8.4.2 呈報為 coverage hole（`DATA_REQUESTS` #22）**；「switches off automatically after a set time」條文未給數值，故 -03 之步驟以可觀察量（MAX DEF 不再作用）為終止條件，不寫入任何秒數（R-C22 ／ §8.4.1）；A/C、AUTO、溫度等基本控制非配置軸，不寫入 pre_conditions（profile §3.2 禁「Climate is available」型隱含前提）；**`-02`（`024-02`）依 43 §5 增一行限定式 PC**：C20 把最高風速寫死 `(7/7)`，而 C6.1 明載某些車輛之前排風速值域為 `Off, 1-8`（其最高為 8），故該 ER 於該類車輛為假 —— **ER 不改**（寫 8/8 為造值、寫「最高設定」弱於條文，皆違 §8.4.1），改以 profile §3.2 **第十四軸**之值（前排風速範圍 `Off, 1-7`，出處 2.7 `C6.` 之逐字，2.7 併入 specification_reference 依 R-C29）限定本條之適用車輛，使既有 ER 在其可陳述之範圍內為真；**`Off, 1-8` 車輛上 MAX DEF 所設之風速未經條文界定，本 TC 不涵蓋**，該缺口由 `DATA_REQUESTS` #29 追，不吸收（§8.4.2）。",
        "keywords": ["MAX DEF", "FRONT DEF", "REAR DEFROST", "RECIRC",
                     "Sync", "MAX A/C", "AUTO"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-024-01",
                "tc_title": "MAX DEF replaces the FRONT DEF button",
                "test_item":
                    "On vehicles with MAX DEF, MAX DEF shall replace the "
                    "FRONT DEF button",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Read the front defrost control label on the climate screen",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. The \"MAX DEF\" button is shown in place of the "
                    "\"FRONT DEF\" button",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-024-02",
                "confine": PC_FAN_1_7,          # 43 §5 / DR #29
                "spec_ref": ("3.2", "2.7"),
                "tc_title": "MAX DEF sets seven climate states when turned on",
                "test_item":
                    "MAX DEF shall automatically turn on A/C, change airflow "
                    "modes to Windshield, increase fan speed to the highest "
                    "setting (7/7), set the temperature (driver and passenger "
                    "if available) at the highest setting (HI), change RECIRC "
                    "to open (LED off), turn on Sync and activate the REAR "
                    "DEFROST",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen with MAX DEF not active\n"
                    "2. Press \"MAX DEF\"\n"
                    "3. Read the A/C state\n"
                    "4. Read the airflow mode\n"
                    "5. Read the fan speed\n"
                    "6. Read the temperature setting for the driver and, if "
                    "available, the passenger\n"
                    "7. Read the RECIRC state and its LED\n"
                    "8. Read the Sync state\n"
                    "9. Read the REAR DEFROST state",
                "expected_result":
                    "1. The \"MAX DEF\" button is not active\n"
                    "2. The \"MAX DEF\" button is active\n"
                    "3. A/C is on\n"
                    "4. The airflow mode is Windshield\n"
                    "5. The fan speed is at the highest setting (7/7)\n"
                    "6. The temperature is at the highest setting (HI) for the "
                    "driver and, if available, the passenger\n"
                    "7. RECIRC is open and its LED is off\n"
                    "8. Sync is on\n"
                    "9. REAR DEFROST is active",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-024-03",
                "tc_title": "MAX DEF switches off automatically and restores the manual mode",
                "test_item":
                    "MAX DEF shall switch off automatically after a set time, "
                    "after which the system shall go back to the previous "
                    "manual mode",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the climate system to a manual mode with a known "
                    "airflow mode, fan speed and temperature setting\n"
                    "2. Press \"MAX DEF\"\n"
                    "3. Leave the climate controls untouched until the "
                    "\"MAX DEF\" button is no longer active",
                "expected_result":
                    "1. The climate screen shows the airflow mode, fan speed "
                    "and temperature setting that were set\n"
                    "2. The \"MAX DEF\" button is active\n"
                    "3. The \"MAX DEF\" button is no longer active and the "
                    "airflow mode, fan speed and temperature setting are those "
                    "of the previous manual mode",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-024-04",
                "tc_title": "Pressing A/C breaks MAX DEF and leaves A/C off",
                "test_item":
                    "Pressing A/C shall break MAX DEF, turning MAX DEF off, "
                    "and the system shall go back to the previous manual mode "
                    "with the A/C off",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the climate system to a manual mode with a known "
                    "airflow mode, fan speed and temperature setting\n"
                    "2. Press \"MAX DEF\"\n"
                    "3. Press \"A/C\"",
                "expected_result":
                    "1. The climate screen shows the airflow mode, fan speed "
                    "and temperature setting that were set\n"
                    "2. The \"MAX DEF\" button is active\n"
                    "3. The \"MAX DEF\" button is no longer active, the "
                    "airflow mode, fan speed and temperature setting are those "
                    "of the previous manual mode, and A/C is off",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-024-05",
                "tc_title": "Pressing AUTO breaks MAX DEF and enters AUTO",
                "test_item":
                    "Pressing AUTO shall break MAX DEF, turning MAX DEF off, "
                    "and the system shall go to AUTO",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Press \"AUTO\"",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The \"MAX DEF\" button is no longer active and the "
                    "climate system is in AUTO",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-024-06",
                "tc_title": "Pressing MAX A/C breaks MAX DEF and enters MAX A/C",
                "test_item":
                    "Pressing MAX A/C shall turn MAX DEF off, and the system "
                    "shall go to MAX A/C",
                "pre_conditions":
                    f"{PC_MAXDEF}\n"
                    "2. [spec-derived] The vehicle is equipped with MAX A/C "
                    "(3.2)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Press \"MAX A/C\"",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The \"MAX DEF\" button is no longer active and MAX A/C "
                    "is active",
                "priority": "P1",
                "design_method": DM_STATE,
            },
            {
                "req_id": "SWE1-HVAC-024-07",
                "tc_title": "Changing the temperature breaks MAX DEF",
                "test_item":
                    "Changing the temperature shall break MAX DEF, turning MAX DEF off, "
                    "and the system shall go back to the previous manual mode "
                    "with the A/C on",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Change the temperature setting",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The \"MAX DEF\" button is no longer active and the "
                    "system is in the previous manual mode with A/C on",
                "priority": "P1",
                "design_method": DM_STATE,
                "split_flag": True,
                "split_reason": SPLIT_REASON,
            },
            {
                "req_id": "SWE1-HVAC-024-07",
                "tc_title": "Changing RECIRC breaks MAX DEF",
                "test_item":
                    "Changing recirculation shall break MAX DEF, turning MAX DEF off, "
                    "and the system shall go back to the previous manual mode "
                    "with the A/C on",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Change RECIRC",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The \"MAX DEF\" button is no longer active and the "
                    "system is in the previous manual mode with A/C on",
                "priority": "P1",
                "design_method": DM_STATE,
                "split_flag": True,
                "split_reason": SPLIT_REASON,
            },
            {
                "req_id": "SWE1-HVAC-024-07",
                "tc_title": "Changing the mode distribution breaks MAX DEF",
                "test_item":
                    "Changing the mode distribution shall break MAX DEF, turning MAX DEF off, "
                    "and the system shall go back to the previous manual mode "
                    "with the A/C on",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Change the mode distribution",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The \"MAX DEF\" button is no longer active and the "
                    "system is in the previous manual mode with A/C on",
                "priority": "P1",
                "design_method": DM_STATE,
                "split_flag": True,
                "split_reason": SPLIT_REASON,
            },
            {
                "req_id": "SWE1-HVAC-024-07",
                "tc_title": "Pressing MAX DEF again breaks MAX DEF",
                "test_item":
                    "Pressing MAX DEF again shall break MAX DEF, turning MAX DEF off, "
                    "and the system shall go back to the previous manual mode "
                    "with the A/C on",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Press \"MAX DEF\" again",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The \"MAX DEF\" button is no longer active and the "
                    "system is in the previous manual mode with A/C on",
                "priority": "P1",
                "design_method": DM_STATE,
                "split_flag": True,
                "split_reason": SPLIT_REASON,
            },
            {
                "req_id": "SWE1-HVAC-024-08",
                "tc_title": "A fan speed change does not break MAX DEF",
                "test_item":
                    "A change in fan speed shall not break MAX DEF",
                "pre_conditions": PC_MAXDEF,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Press \"MAX DEF\"\n"
                    "2. Change the fan speed",
                "expected_result":
                    "1. The \"MAX DEF\" button is active\n"
                    "2. The fan speed changes and the \"MAX DEF\" button is "
                    "still active",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    # ----------------------------------------------------------------- 3.3
    {
        "parent": "SWE1-HVAC-025",
        "outline": "3.3",
        "reasoning":
            "驗證目標：3.3（C21）以一句話定出 climate off 期間之可用性例外，兩個 037 leaf 分別對應「MAX DEF 與 REAR DEF 可用」與「其餘 climate 功能不可用」，一葉一 TC（§8.2.1）。關鍵情境條件：本節條文不含任何裝備條件，故兩項裝備前提依 R-C29 標其明文出處 —— MAX DEF 標 (3.2)「On vehicles with MAX DEF」，rear defrost 標 (3.4)「when not present in the vehicle」，兩節一併列入 specification_reference（§10.7 賴以作為 setup 者）；引用其裝備事實不等於驗證該兩節之行為，本批未擴張至 3.2 之 MAX DEF 連動或 3.4 之按鈕隱藏（§8.2.1）。為什麼這樣切：climate off 為 spec 定義之 trigger 但 TC 步驟必須自行建立，依 R-C28 第三問落於 procedure 首步而非 pre_conditions。刻意略過：2.10（C11）同時擁有「grey out remaining buttons」之視覺處置與「按 temp/fan 控制即讓 climate 復電」之行為，兩者皆非本節所定，故 -02 只以本節自身之詞「available」判定，不驗 greyed out、亦不按下任何功能鍵（後者若寫入將與 2.10 明文相牴觸）。**「not available」之可觀察外觀由 2.10 擁有，本節未定義**，故其 ER 停在該詞而不描述外觀（A-CF18）。",
        "keywords": ["climate off", "MAX DEF", "REAR DEF", "available"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-025-01",
                "tc_title": "MAX DEF and REAR DEF stay available while climate is off",
                "test_item":
                    "MAX DEF and REAR DEF shall be available during climate "
                    "off",
                "pre_conditions": f"{PC_MAXDEF_X}\n{PC_REARDEF}",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn the climate system off\n"
                    "2. Read the \"MAX DEF\" button on the climate screen\n"
                    "3. Read the \"REAR DEF\" button on the climate screen",
                "expected_result":
                    "1. The climate system is off\n"
                    "2. The \"MAX DEF\" button is available\n"
                    "3. The \"REAR DEF\" button is available",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("3.3", "3.2", "3.4"),
            },
            {
                "req_id": "SWE1-HVAC-025-02",
                "tc_title": "Other climate functions are not available while climate is off",
                "test_item":
                    "During climate off, the climate functions other than MAX "
                    "DEF and REAR DEF shall not be available",
                "pre_conditions": f"{PC_MAXDEF_X}\n{PC_REARDEF}",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn the climate system off\n"
                    "2. Read the climate functions other than \"MAX DEF\" and "
                    "\"REAR DEF\" on the climate screen",
                "expected_result":
                    "1. The climate system is off\n"
                    "2. The climate functions other than \"MAX DEF\" and "
                    "\"REAR DEF\" are not available",
                "priority": "P2",
                "design_method": DM_FUNC,
                "spec_ref": ("3.3", "3.2", "3.4"),
            },
        ],
    },
    # ----------------------------------------------------------------- 3.4
    {
        "parent": "SWE1-HVAC-026",
        "outline": "3.4",
        "reasoning":
            "驗證目標：3.4（C22）規定 soft top 車身在未配備 rear defrost 時，該按鈕不出現，單一 037 leaf 對應之，故一葉一 TC（§8.2.1）。關鍵情境條件：兩項前提皆為本節明文，故依 R-C28 第一問通過並標 (3.4)，無跨節取據，specification_reference 僅列本節。第十一軸之措辭以「soft top」為準並以「such as JL/JT」引條文自身之例示 —— 寫成「JL or JT」即把例示讀成窮舉，屬 §8.4.1 之反向造值（29 §2）。為什麼這樣切：本節只定出一個顯示結果，無分支可分。刻意略過：條文之「when configured」未定義其所指之設定項，故不寫入任何配置步驟（§8.4.1）；**EMEA ICS 排除式 PC 亦已依 37 §1 移除**（`ch16_mirror_map.tsv` 判 3.4 為 no-counterpart）；rear defrost 存在時之按鈕行為本節未述，不作反向配對（§7 之 negative pairing 需條文支撐，此處無）。",
        "keywords": ["soft top", "JL", "JT", "rear defrost", "not present"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-026",
                "tc_title": "Rear defrost button is absent when the vehicle has no rear defrost",
                "test_item":
                    "For soft top vehicles such as JL/JT, when configured, the "
                    "rear defrost button shall not appear when not present in "
                    "the vehicle",
                "pre_conditions":
                    f"{PC_SOFTTOP}\n"
                    "2. [spec-derived] Rear defrost is not present in the "
                    "vehicle (3.4)",
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Read the climate screen for the rear defrost button",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. The rear defrost button does not appear",
                "priority": "P1",
                "design_method": DM_FUNC,
                "spec_ref": ("3.4",),
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
            n += 1
            tcs.append({
                "req_id": tc["req_id"],
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": tc["tc_title"],
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": tc["test_item"],
                # 43 §5 — a `confine` line is NOT an exclusion: it selects a
                # value of an axis so that an ER already written stays true,
                # rather than removing an interface. It is ordered before the
                # exclusions because it belongs to the requirement, not to the
                # interface bookkeeping.
                "pre_conditions": add_exclusions(
                    tc["pre_conditions"],
                    *([tc["confine"]] if tc.get("confine") else []),
                    EX_ICS,
                    *([] if o in NO_CH16_COUNTERPART else [EX_EMEA])),
                "input_test_data": tc["input_test_data"],
                "test_procedure": tc["test_procedure"],
                "expected_result": tc["expected_result"],
                "specification_reference": ref(
                    *tc.get("spec_ref", (o,)), "2.14",
                    *([] if o in NO_CH16_COUNTERPART else ["16.2"])),
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
            "distinguishing_axis": {"axis": "see per-TC titles", "delta": ""},
            "assumptions": [],
            "interface_axis_review": INTERFACE_AXIS_REVIEW[o],
            "tcs": apply_test_item(apply_splits(tcs)),
        }
        (OUT / f"{b['parent']}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{b['parent']}  {o:8} {len(tcs)} TC  -> generated/{b['parent']}.json")

    print(f"\n{total} TCs across {len(BATCHES)} parents; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    # TC count now exceeds leaf count — 024-07 splits four ways (30 §1.4).
    # Progress is counted in leaves, effort in TCs; the two stopped being
    # interchangeable here, so both are asserted separately.
    leaves = len({tc["req_id"] for b in BATCHES for tc in b["tcs"]})
    print(f"\n{leaves} leaves -> {total} TCs for Tri-Mode Climate "
          f"(3.1:3, 3.2:8, 3.3:2, 3.4:1 leaves); nothing withheld")
    split = [tc["req_id"] for b in BATCHES for tc in b["tcs"]
             if tc.get("split_flag")]
    print(f"split leaves: "
          f"{ {r: split.count(r) for r in sorted(set(split))} or 'none'}")
    if leaves != 14:
        raise SystemExit(f"expected 14 leaves, emitted {leaves}")
    if total != 17:
        raise SystemExit(f"expected 17 TCs, emitted {total}")


if __name__ == "__main__":
    main()
