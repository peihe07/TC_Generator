#!/usr/bin/env python3
"""Batch 6 generator — ICS Anatomy (handoff 43 §7).

Scope from framework.md line 49: `16.2, 16.14, 16.16` = **17 leaves**.
037 measured independently: 106(9) + 120(3) + 122(5) = 17.

  !! 43 §7's header table lists the Layer 3 as "16.2、16.16" while quoting
  !! 17 leaves. Those two facts are inconsistent: 16.2 + 16.16 is 14 leaves.
  !! framework.md — which 43 §7 itself names as the authority ("Layer 3 與
  !! leaf 數自 framework.md 導出") — lists three sections totalling 17, and
  !! 14 §1's amendment is what moved 16.14 into this pair. Generated from
  !! framework.md; the discrepancy is reported in 上繳 32 §7.1.

Emitted: 16 TCs, -082 … -097.
WITHHELD: SWE1-HVAC-122-02 — "Off icon of seats will depend on system
configuration (see Climate section)". 44 §2 answered the marker question with
R-C39's fourth class [COVERED-BY], and the leaf was re-checked against its
five conditions: condition TWO fails (the target section has no TCs, and the
clause names no section at all), so R-C39's own text applies — record it
`deferred`, do NOT pre-mark [COVERED-BY]. Still stopped; DR #32 updated.

THIS BATCH IS ON THE ch16 SIDE, and three habits from the ch2 batches invert:

  EMEA axis   : ch16 TCs run ON EMEA ICS vehicles. They carry a POSITIVE axis
                pre_condition, never the `is not an EMEA ICS vehicle`
                exclusion. `emea_ics_review` is therefore not applicable and
                the per-TC gate does not apply (it keys on the exclusion).
  mirror map  : used in REVERSE — 16.2 <-> 2.2 and 16.14 <-> 2.14 are read to
                find what the ch2 side has that ch16 does NOT, so that ch2
                content is not imported (§8.2.1). Findings:
                  C1 has "(if the MTC has a Climate screen)" qualifying MTC;
                    ICE1 does not -> not imported
                  ICE1 has "with the exception of the recirculation led in
                    climate off"; C1 does not -> this is 16.2's own -02 leaf
                  ICE13 is C15's FIRST TWO SENTENCES ONLY. C15's 3-knob-ICS
                    paragraph does not exist in ch16 (RUNBOOK: 節級看開頭,
                    TC 級看那一句) -> 16.14 must not VERIFY it, but must
                    still CITE it, see axis 13 below
  axis 13     : "For MTC with ICS ... 3 knob HVAC controls ... no HVAC menu
                bar icons, no HVAC screens and no HVAC pop ups" (2.14 C15).
                `with ICS` means this rule is ABOUT ICS vehicles, so it binds
                the ch16 TCs harder than the ch2 ones — while its only
                statement lives in ch2. Cross-section citation, R-C29.

R-C34's generation-time duty, discharged per section in
data/interface_axis_review.tsv; the per-TC assignment is below.

Usage:
    python3 features/comfort/scripts/gen_batch6.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "ICS Anatomy"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 82

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
DM_STATE = "狀態轉換 (State Transition Testing)"

# The market/variant axis, stated POSITIVELY. ch2's TCs carry its negation
# citing 16.2; ch16's carry its affirmation citing the same section, because
# the fact is one fact seen from two sides.
PC_EMEA = ("1. [spec-derived] The vehicle is an EMEA ICS vehicle, whose climate "
           "interface is specified in chapter 16 (16.2)")
# Axis 13. Source is 2.14 C15 — see the module docstring for why a ch16 TC
# cites a ch2 clause here.
EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
# Axis 9. Exposed wherever the observable lives in the head unit's comfort
# section; NOT exposed where it is a comfort pop-up (6.3's own exception) or
# a hard-control LED.
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
LOWER_EXPOSED = {
    "SWE1-HVAC-106-01", "SWE1-HVAC-106-02", "SWE1-HVAC-106-08",
    "SWE1-HVAC-120-01", "SWE1-HVAC-120-02", "SWE1-HVAC-120-03",
    "SWE1-HVAC-122-01", "SWE1-HVAC-122-03", "SWE1-HVAC-122-04",
    "SWE1-HVAC-122-05",
}
# Axis 13 is NOT exposed on 16.16: C15's exclusion names HVAC menu bar icons,
# HVAC screens and HVAC pop-ups. A seat controls screen is none of those.
ICS_NOT_EXPOSED = {"SWE1-HVAC-122-01", "SWE1-HVAC-122-02", "SWE1-HVAC-122-03",
                   "SWE1-HVAC-122-04", "SWE1-HVAC-122-05"}

# 44 §2 — R-C39 立了第四類 [COVERED-BY]，本 leaf 依其五條件逐項核對：
#   一 委派對象為本 spec 之節  ✅（「see Climate section」未指名外部文件）
#   二 對象節之 leaf 已產出 TC ❌ ← 停在此
#   三 逐句比對其 ER            —— 無對象 TC 可比，不能執行
#   四 扣除委派後無獨立餘留      ✅（餘留為「depend on system configuration」，
#                                無可判之期望值）
#   五 白名單增列               —— 未進入
# R-C39 明定第二項未滿足時「不得先標 [COVERED-BY]，該 leaf 標 deferred」。
# 實測（R-C30）：`data/section_fulltext.tsv` 全 129 節，
#   pattern `off icon|icon of seats` -> 1 命中，即 16.16 自身
#   pattern `\bicon\b`              -> 13 句／9 節（2.5 / 7.3 / 10.8 / 11.10 /
#                                       12.3 / 14.16 / 14.16.1 / 16.5 / 16.16）
# 座椅類候選僅 12.3（Heated Vented Seats）與 14.16.1（Climate Popups），
# 兩組皆未生成，且**條文本身未指名任何一節** —— 「Climate section」不是節次。
WITHHELD = [
    ("SWE1-HVAC-122-02",
     "R-C39 五條件之**第二項未滿足**（對象節未生成），依其明文標 `deferred`、"
     "不得先標 `[COVERED-BY]`。且「Climate section」**未指名任何節次**，"
     "實測全 129 節僅 16.16 自身含 `off icon`；座椅類候選 12.3／14.16.1 皆未生成，"
     "且兩者所述為顏色與熄滅時之灰化，**皆非「configuration → icon」之對照**，"
     "故第三項於該二節生成後仍可能不成立。見 DATA_REQUESTS #32"),
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
        "parent": "SWE1-HVAC-106",
        "outline": "16.2",
        "reasoning":
            "驗證目標：16.2（ICE1）以六句定出 EMEA ICS 介面之狀態同步與 popup 規則，九個 037 leaf 逐句對應，一葉一 TC（§8.2.1）；九者之可觀察量刻意互斥 —— `-01` 驗硬鍵→觸控之反映、`-08` 驗畫面上之狀態呈現且不入 status bar、`-09` 驗觸控→硬鍵 LED 之反向，三者若共用同一組觀察即違 §4.5。關鍵情境條件：**本批為 ch16 側，EMEA 軸取正向值而非排除式**（`PC_EMEA`，出處 16.2）—— ch2 之 TC 寫「不是 EMEA ICS 車」，ch16 之 TC 寫「是」，同一事實之兩面；依 **R-C34**，第十三軸（3 旋鈕 ICS）**全數補**，其出處為 **2.14 C15** 之「For MTC **with ICS** … 3 knob HVAC controls … no HVAC screens and no HVAC pop ups」—— 該句寫在 ch2 而所治者正是 ICS 車，故 ch16 之 TC 反而更須補之（跨節取據，R-C29，2.14 併入 spec_ref）；第九軸僅 `-01`／`-02`／`-08` 補（可觀察量在 head unit 之 comfort section），`-03`～`-07` 之可觀察量為 comfort popup，正是 6.3 之例外，`-09` 之可觀察量為硬鍵 LED，皆不補；第十二軸不補 —— ch16 十八節無任何 tab 條文，2.1 屬另一套介面，援引即為跨介面移植。為什麼這樣切：`-06`／`-07` 為第一軸（ATC／MTC）之兩個值，同一 popup 之兩種呈現，故各自成條並於 PC 具名該值。刻意略過：**鏡射表反向使用之結果** —— C1 之「for MTC (**if the MTC has a Climate screen**)」括號限定於 ICE1 不存在，**不得移植**；ICE1 之「with the exception of the recirculation led in climate off (see ICE11.)」則為 ch16 獨有，即 `-02` 之 leaf，惟其指向之 **ICE11 為 16.12（氣流模式），不含 recirculation LED 之規則**（該規則在 ICE9／16.10），**係條文之誤引**，已登 A-CF25；本條僅驗 ICE1 自身所述之例外（畫面不反映該變更），不驗 16.10 之 LED 規則（§8.2.1）。",
        "keywords": ["ICS", "hard controls", "touchscreen", "pop-up",
                     "status bar"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-106-01",
                "tc_title": "Hard control changes are reflected on the ICS climate screen",
                "test_item":
                    "Whenever changes to the climate system are made via hard "
                    "controls or touchscreen, these changes shall be reflected "
                    "in both locations",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control",
                "expected_result":
                    "1. The climate screen shows the current fan speed\n"
                    "2. The climate screen shows the new fan speed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-02",
                "tc_title": "Recirculation LED change is not reflected while climate is off",
                "test_item":
                    "Changes shall be reflected in both locations with the "
                    "exception of the recirculation LED in climate off",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn the climate system off using the climate power "
                    "button on the climate screen\n"
                    "2. Press the recirculation hard control",
                "expected_result":
                    "1. The CLIMATE OFF screen is displayed\n"
                    "2. The climate screen does not reflect the recirculation "
                    "change",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-03",
                "tc_title": "Fan pop-up appears off the climate screen and times out",
                "test_item":
                    "According pop-ups shall be shown if NOT on climate screen "
                    "(timeout after 3 sec)",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen other than the climate screen\n"
                    "2. Change the fan speed using the fan speed hard control\n"
                    "3. Wait 3 seconds without further interaction",
                "expected_result":
                    "1. The climate screen is not displayed\n"
                    "2. A fan speed pop-up is shown\n"
                    "3. The fan speed pop-up is no longer shown",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-04",
                "tc_title": "No passenger slider pop-up while synced",
                "test_item":
                    "When sync'd, the system shall not show the slider pop-up "
                    "on the passenger side when adjusting the driver slider",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The vehicle is not a single zone climate "
                    "configuration, for which Sync is not shown (16.11)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn SYNC on from the climate screen\n"
                    "2. Adjust the driver temperature slider",
                "expected_result":
                    "1. The \"SYNC\" button is highlighted\n"
                    "2. No slider pop-up is shown on the passenger side",
                "priority": "P2",
                "design_method": DM_FUNC,
                "spec_ref": ("16.2", "16.11"),
            },
            {
                "req_id": "SWE1-HVAC-106-05",
                "tc_title": "Temperature pop-up comes down from the status bar",
                "test_item":
                    "If the user is outside of the climate main category and "
                    "the temperature is changed through hard controls, a "
                    "pop-up shall be shown coming down from that temperature "
                    "in the status bar",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen outside the climate main category\n"
                    "2. Change the temperature using the temperature hard "
                    "control",
                "expected_result":
                    "1. The climate main category is not displayed\n"
                    "2. A pop-up comes down from the temperature in the status "
                    "bar",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-06",
                "tc_title": "ATC pop-up displays the degree being set",
                "test_item":
                    "For ATC the pop-up shall display the degree (or half "
                    "degree increments for Celsius) being set",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The vehicle has an ATC climate system "
                    "(16.2)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Set the temperature units to Celsius and open a screen "
                    "outside the climate main category\n"
                    "2. Change the temperature using the temperature hard "
                    "control",
                "expected_result":
                    "1. The climate main category is not displayed\n"
                    "2. The pop-up displays the degree being set in half "
                    "degree increments",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-07",
                "tc_title": "MTC pop-up displays a slider bar with an arrow",
                "test_item":
                    "For MTC the pop-up shall display a slider bar with the "
                    "arrow pointing to the current setting",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The vehicle has an MTC climate system "
                    "(16.2)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open a screen outside the climate main category\n"
                    "2. Change the temperature using the temperature hard "
                    "control",
                "expected_result":
                    "1. The climate main category is not displayed\n"
                    "2. The pop-up displays a slider bar with the arrow "
                    "pointing to the current setting",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-08",
                "tc_title": "On the climate screen status is not shown in the status bar",
                "test_item":
                    "If on climate screen, status changes shall be indicated "
                    "directly on touchscreen buttons and on the status "
                    "indicator on the category button, and shall not be shown "
                    "in the status bar",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the fan speed using the fan speed control on "
                    "the climate screen\n"
                    "3. Read the status bar",
                "expected_result":
                    "1. The climate screen is displayed\n"
                    "2. The touchscreen button and the status indicator on the "
                    "category button show the new fan speed\n"
                    "3. The status bar does not show the fan speed change",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-106-09",
                "tc_title": "Hard control LEDs follow changes made on the screen",
                "test_item":
                    "If changes are made on climate screen, LEDs on hard "
                    "controls shall reflect the new status",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Read the fan speed LED on the hard controls\n"
                    "2. Change the fan speed using the fan speed control on "
                    "the climate screen",
                "expected_result":
                    "1. The fan speed LED shows the current fan speed\n"
                    "2. The fan speed LED shows the new fan speed",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-120",
        "outline": "16.14",
        "reasoning":
            "驗證目標：16.14（ICE13）以兩句定出 MTC 於 ICS 介面之適用與其與 ATC 之差異，三個 037 leaf 分別對應「MTC 畫面與 popup 被採用」「無離散溫度設定」「無對設定溫度之 AUTO 控制」，一葉一 TC（§8.2.1）。關鍵情境條件：EMEA 軸取正向值（`PC_EMEA`）；`CCM relays MTC functionality` 為條文明文之配置條件，標 spec-verbatim；依 **R-C34** 第十三軸全數補（本節之可觀察量正是 HVAC 畫面與 popup，而 C15 之 3 旋鈕例外恰以「MTC **with ICS**」為前件），第九軸全數補（可觀察量在 head unit 之 comfort section），第十二軸不補（ch16 無 tab 條文）。為什麼這樣切：`-02` 與 `-03` 是同一句之兩個並列否定（`lack of discrete temperature settings` 與 `\"Auto\" control over the set temperature`），037 各給其 leaf，依 §8.2 單位歸 037 不合併，且兩者之可觀察元件不同。刻意略過：**鏡射表反向使用之關鍵結果** —— `ch16_mirror_map.tsv` 記 `16.14 ↔ 2.14` 為 `mirrored`，惟 **ICE13 全文僅 C15 之首二句，C15 之 3 旋鈕 ICS 整段於 ch16 不存在**，故本節之 TC **不驗**該例外行為（§8.2.1），只以其為第十三軸之出處而引 2.14（R-C29）；此即 `RUNBOOK.md`「節級看開頭，TC 級看那一句」之反向應用。",
        "keywords": ["MTC", "ATC", "CCM", "discrete temperature settings"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-120-01",
                "tc_title": "MTC screens and pop-ups are used when CCM relays MTC",
                "test_item":
                    "MTC screens and popups shall be used when CCM relays MTC "
                    "functionality",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The CCM relays MTC functionality (16.14)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Change the temperature using the temperature hard "
                    "control from a screen other than the climate screen",
                "expected_result":
                    "1. The MTC climate screen is displayed\n"
                    "2. The MTC temperature pop-up is displayed",
                "priority": "P1",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-120-02",
                "tc_title": "MTC offers no discrete temperature settings",
                "test_item":
                    "MTC climate shall be differentiated from ATC by the lack "
                    "of discrete temperature settings",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The CCM relays MTC functionality (16.14)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Read the temperature control on the climate screen",
                "expected_result":
                    "1. The MTC climate screen is displayed\n"
                    "2. No discrete temperature setting is shown on the "
                    "temperature control",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-120-03",
                "tc_title": "MTC offers no AUTO control over the set temperature",
                "test_item":
                    "MTC climate shall be differentiated from ATC by the lack "
                    "of \"Auto\" control over the set temperature",
                "pre_conditions": add_lines(
                    PC_EMEA,
                    "[spec-derived] The CCM relays MTC functionality (16.14)"),
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the climate screen\n"
                    "2. Read the climate screen for an \"AUTO\" control over "
                    "the set temperature",
                "expected_result":
                    "1. The MTC climate screen is displayed\n"
                    "2. No \"AUTO\" control over the set temperature is shown",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
        ],
    },
    {
        "parent": "SWE1-HVAC-122",
        "outline": "16.16",
        "reasoning":
            "驗證目標：16.16（ICE15）以五句定出 ICS controls screen 上座椅類控制之標示與狀態呈現，五個 037 leaf 逐句對應，一葉一 TC（§8.2.1），本輪產四條、`-02` 停下（見刻意略過）。關鍵情境條件：EMEA 軸取正向值（`PC_EMEA`）；依 **R-C34**，**第十三軸不補** —— C15 之例外所移除者為 `HVAC menu bar icons`／`HVAC screens`／`HVAC pop ups`，而本節之可觀察量為**座椅控制之 controls screen**，不屬該三者，補之即為過嚴之排除（35 §1 之形態）；第九軸全數補（controls screen 屬 head unit 之 comfort section）；第十二軸不補（ch16 無 tab 條文）。為什麼這樣切：`-03` 與 `-04` 為 active／inactive 兩個互補狀態，各自可獨立失效（白色對而灰色錯），合併後無法定位；`-05` 之驗證對象為**進入畫面時**之狀態呈現，其失效形態（進入後才更新）與前二者無關。刻意略過：**`-02` 停下不產列** —— 「Off icon of seats will depend on system configuration (**see Climate section**)」之委派對象為本 spec 之另一節而非外部文件（故非 `[BLOCKED-SPEC]`），其性質又確為介面可觀察（故非 `[BLOCKED-NON-HMI]`），而所缺者為「哪一種 system configuration 對應哪一個 off icon」之對照表，形態同 `DATA_REQUESTS` #17；新 marker 不得於生成當下自創（**R-C26**／profile §5.4 末），故回報待裁並登 **DR #32**；**44 §2 之 R-C39 立了第四類 `[COVERED-BY]` 後已逐項核對五條件**：第一項成立（未指名外部文件）、**第二項不成立**（「Climate section」未指名節次，實測全 129 節僅 16.16 自身含 `off icon`，座椅類候選 `12.3`／`14.16.1` 兩組皆未生成）、第三項因無對象 TC 而無法執行、第四項成立（餘留為「depend on system configuration」，無可判之期望值），依 R-C39 明文「第二項未滿足時不得先標 `[COVERED-BY]`，該 leaf 標 `deferred`」，**維持停下**。",
        "keywords": ["controls screen", "Driver", "Passenger", "active state",
                     "inactive state"],
        "tcs": [
            {
                "req_id": "SWE1-HVAC-122-01",
                "tc_title": "Driver and Passenger labels are always shown",
                "test_item":
                    "The system shall always show \"Driver\" or \"Passenger\"",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the controls screen\n"
                    "2. Read the labels on the seat controls",
                "expected_result":
                    "1. The controls screen is displayed\n"
                    "2. Each seat control shows a \"Driver\" or \"Passenger\" "
                    "label",
                "priority": "P2",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-122-03",
                "tc_title": "Active state text is white",
                "test_item":
                    "Active state text color shall be white",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the controls screen\n"
                    "2. Turn a seat control on",
                "expected_result":
                    "1. The controls screen is displayed\n"
                    "2. The text of that seat control is white",
                "priority": "P3",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-122-04",
                "tc_title": "Inactive state text is gray",
                "test_item":
                    "Inactive state text color shall be gray",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Open the controls screen\n"
                    "2. Turn a seat control off",
                "expected_result":
                    "1. The controls screen is displayed\n"
                    "2. The text of that seat control is gray",
                "priority": "P3",
                "design_method": DM_FUNC,
            },
            {
                "req_id": "SWE1-HVAC-122-05",
                "tc_title": "Entering the controls screen shows the current button states",
                "test_item":
                    "When entering the controls screen the current state of "
                    "the buttons shall be displayed",
                "pre_conditions": PC_EMEA,
                "input_test_data": "NA",
                "test_procedure":
                    "1. Turn one seat control on and another seat control off, "
                    "then leave the controls screen\n"
                    "2. Enter the controls screen",
                "expected_result":
                    "1. The controls screen is no longer displayed\n"
                    "2. The controls screen shows one seat control active and "
                    "the other inactive",
                "priority": "P2",
                "design_method": DM_STATE,
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
            # R-C29 — PC_EMEA cites 16.2, so 16.2 joins spec_ref on every TC,
            # including the ones whose own section is not 16.2.
            extra, refs = [], list(tc.get("spec_ref", (o,))) + ["16.2"]
            if tc["req_id"] not in ICS_NOT_EXPOSED:
                extra.append(EX_ICS)
                refs.append("2.14")
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
                                   if o == "16.2" else
                                   {"axis": "see per-TC titles",
                                    "delta": ""}),
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
          f"declared for {TEST_SET} (framework.md: 17)")
    if leaves + held != 17 or total != 16:
        raise SystemExit(
            f"expected 17 leaves declared / 16 TCs, got {leaves + held} / {total}")


if __name__ == "__main__":
    main()
