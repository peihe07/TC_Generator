#!/usr/bin/env python3
"""Batch 15 generator — Heated Vented Seats (handoff 63 §1). The last set.

Scope from framework.md §12's table, derived not retyped (48 §2):

    11.1 4 | 11.2 4 | 11.3 1 | 11.4 2 | 11.5 1 | 11.6 6 | 11.6.1 2 | 11.7 4
    11.8 4 | 11.9 2 | 11.10 3 | 11.11 3 | 11.11.1 1              = 37 (ch11)
    12.1 4 | 12.2 4 | 12.3 2 | 12.4 1 | 12.5 2 | 12.6 1 | 12.7 2
    12.8 3 | 12.9 3                                              = 22 (ch12)
                                                        22 節 / 59 leaf

Emitted: 57 TCs, -304 … -360. Withheld: 11.5 (058) and 12.6 (072).

--------------------------------------------------------------------------
DR #11's 11 leaves — R-C28's three questions, leaf by leaf (63 §1.1)
--------------------------------------------------------------------------
The 11 ch11 leaves carrying the popup wording are 054-01, 055-01, 059-02,
061-02, 061-03, 061-04, 062-01, 063-01, 064-01, 064-02, 065-02.

All 11 GENERATE, and the reason is the same for each: every expected_result
uses only ch11's OWN words — "opens popup", "«Driver Seat Zone»", "3
seconds", "status bar and temperature/comfort popup". None of them asserts
anything about the popup's CONTENT, which is what the missing Pop Up List
would supply. R-C28 Q1 is therefore satisfied by the section itself.

What DR #11 actually decides is whether ch11 and ch12 are one requirement or
two — a GROUPING question (Part N, duplicate_of), not a "can this ER be
written" question. So DR #11 blocks 0 leaves; its impact column is corrected
accordingly in 上繳 41 §4.2. Each of the 11 names DR #11 in its section's
reasoning.

--------------------------------------------------------------------------
11.5 / 12.6 withheld — and they delegate to DIFFERENT documents
--------------------------------------------------------------------------
  11.5 "Refer to HMI **Settings List** for the details on the Auto Comfort
        Settings options for heated/vented seats."
  12.6 "Refer to HMI **Notes** for the details on the Auto Comfort Settings
        options for heated/vented seats."

Both delegate the whole content elsewhere, so both are [BLOCKED-SPEC] in
shape — but profile §5.1's whitelist is a ruling, not a generation-time
decision (R-C26), and neither leaf is on it. They are therefore withheld and
reported, not marked.

The two targets differ, which also settles their sibling status: the pair is
NOT verbatim-identical (measured: the shared run breaks at "HMI "), so R-C40
does not make one side's disposition bind the other. Here it makes no
difference — both stop — but the measurement is on the record.

--------------------------------------------------------------------------
11.11's "hard buttons for comfort controls" — an axis? No (63 §1.3)
--------------------------------------------------------------------------
  1. two values verbatim:  FAIL — the positive value is verbatim ("if the
     vehicle is configured with hard buttons for comfort controls"), the
     negative one is nowhere in the 129 sections.
  2. mutually exclusive / stated as parallel: FAIL.
  3. no value by inference:  FAIL — the other value is the negation.

Not registered. The three leaves still generate, with the clause's OWN
sentence as a §8.5 clause-local trigger condition — the same treatment 2.9's
013-04 received for "if this feature available" (batch 10), and the same
treatment 上繳 41 §5 argues ch9's leaves are owed. A clause-local trigger is
not a profile axis: it scopes ONE section that says so itself, and it cannot
be reused elsewhere.

Usage:
    python3 features/comfort/scripts/gen_batch15.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"
TCTABLE = Path("/tmp/b15tcs.json")

TEST_GROUP = "Comfort"
TEST_SET = "Heated Vented Seats"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 304

DM = {"F": "功能測試 (Functional based ; no specific technique)",
      "S": "狀態轉換 (State Transition Testing)",
      "B": "邊界值分析 (Boundary Value Analysis, BVA)"}

EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
# Axis 12 — first use as an EXCLUSION. These observables live in the comfort
# section's Seats tab, and 2.1 removes the tabs on front-climate-only
# vehicles. R-C34's per-TC question is answered `exposed` for them and `not
# exposed` for the status-bar ones, which 2.1 does not touch.
EX_TABS = ("[spec-derived] The vehicle is not a front-climate-only vehicle, "
           "for which the comfort tabs are not displayed (2.1)")

PC_SEAT_MULTI = ("1. [spec-verbatim] The vehicle has Multi-Level "
                 "Heated/Vented seats (11.1)")
PC_SEAT_MULTI12 = ("1. [spec-verbatim] The vehicle has Multi-Level "
                   "Heated/Vented seats (12.1)")
PC_SEAT_STD = ("1. [spec-verbatim] The vehicle has Standard Heated/Vented "
               "seats (12.8)")
PC_WHEEL_MULTI = ("1. [spec-verbatim] The vehicle has a Multi-Level heated "
                  "steering wheel (11.8)")
PC_WHEEL_SINGLE = ("1. [spec-verbatim] The vehicle has a Single-Level heated "
                   "steering wheel (11.9)")
PC_ZONE = ("1. [spec-verbatim] The independent seat zone feature is available "
           "on the vehicle (11.6)")
PC_ZONE_SOFT = ("1. [spec-verbatim] The vehicle is equipped with the seat "
                "zone feature without a hard control or capacitive control, "
                "for which a soft button controls it (11.6.1)")
PC_COMFORT = ("1. [spec-derived] The vehicle is equipped with Comfort "
              "features, such as heated/vented seats and a heated steering "
              "wheel (17.3)")
# 11.11's own conditional — a §8.5 clause-local trigger, NOT a profile axis.
PC_HARDBTN = ("1. [spec-verbatim] The vehicle is configured with hard buttons "
              "for comfort controls (11.11)")
PC_HAPTIC = ("1. [spec-verbatim] The vehicle program has haptic "
             "heated/vented seat and heated steering wheel buttons placed on "
             "the side of the radio (11.11)")

SECTION_PC = {
    "11.1": (PC_SEAT_MULTI, ()), "11.2": (PC_SEAT_MULTI, ("11.1",)),
    "11.3": (PC_COMFORT, ("17.3",)), "11.4": (PC_COMFORT, ("17.3",)),
    "11.6": (PC_ZONE, ()), "11.6.1": (PC_ZONE_SOFT, ("11.6",)),
    "11.7": (PC_ZONE_SOFT, ("11.6", "11.6.1")),
    "11.8": (PC_WHEEL_MULTI, ()), "11.9": (PC_WHEEL_SINGLE, ()),
    "11.10": (PC_COMFORT, ("17.3",)), "11.11": (PC_HARDBTN, ()),
    "11.11.1": (PC_COMFORT, ("17.3",)),
    "12.1": (PC_SEAT_MULTI12, ()), "12.2": (PC_SEAT_MULTI12, ("12.1",)),
    "12.3": (PC_COMFORT, ("17.3",)), "12.4": (PC_COMFORT, ("17.3",)),
    "12.5": (PC_COMFORT, ("17.3",)), "12.7": (PC_COMFORT, ("17.3",)),
    "12.8": (PC_SEAT_STD, ()), "12.9": (PC_SEAT_STD, ("12.8",)),
}
LEAF_PC = {"065-03": (PC_HAPTIC, ())}

# R-C34, per TC. The status bar and the temperature/comfort popup survive
# both 6.3 (which removes the comfort SECTION) and 2.1 (which removes the
# TABS); everything else here is inside the Seats tab of the comfort section.
STATUS_BAR_ONLY = {"056", "070", "066", "065-02", "065-03"}

# 66 §1 — DR #43 ruled (一): both leaves are now whitelisted [BLOCKED-SPEC]
# rows (tc_id -382/-383), produced below by BLOCKED_ROWS. Nothing is withheld
# in this Test Set any more.
WITHHELD = []

# 65 §1 froze the existing numbering, so these take late ids rather than
# renumbering 380 rows for two additions.
BLOCKED_ROWS = [
    ("11.5", "SWE1-HVAC-058", 382,
     "Auto Comfort Settings options follow the HMI Settings List",
     "The system shall follow the HMI Settings List for the details on the "
     "Auto Comfort Settings options for heated/vented seats (HVS6.)",
     # 67 §3 — the customer must read "this option is not covered by this
     # delivery", not merely "this option belongs to someone". Owner: stays
     # inside the first 60 characters (R-C27); the coverage sentence follows.
     "[BLOCKED-SPEC] Owner: HMI Settings List — the Auto Comfort Settings "
     "options for heated/vented seats are defined there; with that delegation "
     "removed this requirement has no content verifiable against the Comfort "
     "HMI specification alone. No test case in this delivery covers those "
     "options."),
    ("12.6", "SWE1-HVAC-072", 383,
     "Auto Comfort Settings options follow the HMI Notes",
     "The system shall follow the HMI Notes for the details on the Auto "
     "Comfort Settings options for heated/vented seats (HVS6.)",
     "[BLOCKED-SPEC] Owner: HMI Notes — the Auto Comfort Settings options for "
     "heated/vented seats are defined there; with that delegation removed "
     "this requirement has no content verifiable against the Comfort HMI "
     "specification alone. No test case in this delivery covers those "
     "options."),
]

REASONING = {
"11.1": "驗證目標：11.1（HVS1）以四句定出 Multi-Level 加熱座椅之四段按壓循環（HI／MED／LO／OFF）及其每段之高亮與指示，四個 037 leaf 逐句對應（§8.2.1）。關鍵情境條件：起始 PC 取 **profile §3.2 第八軸「Standard vs Multi-Level 座椅」之 Multi-Level 值**，其字面即本節首句；依 **R-C34**，第九軸（6.3 移除 comfort section）、第十二軸（2.1 使 tabs 不顯示，座椅控制在 Seats 分頁內）、第十三軸與 EMEA 皆暴露 → 全數補。**第十二軸於本組為首次以排除式使用**。為什麼這樣切：四段之循環取狀態轉換法，任一段之落點錯誤可獨立定位。刻意略過：**`054-01` 之 popup 內容不驗** —— 本節只寫「opens popup」，popup 之內容由未入案之 HMI Pop Up List 定義（**DR #11**），故 ER 只驗其開啟；**DR #11 之答案影響的是 ch11／ch12 是否為同一需求（分組），不是本條之 ER 可否寫出**（63 §1.1 之逐 leaf 判定，見上繳 41 §4.2）。",
"11.2": "驗證目標：11.2（HVS2）以四句定出 Multi-Level 通風座椅之四段按壓循環及其藍色高亮與風扇指示，四個 037 leaf 逐句對應。關鍵情境條件：同 11.1（第八軸之 Multi-Level 值）；依 **R-C34** 四個介面型軸中三者暴露 → 補，第十二軸亦補。為什麼這樣切：與 11.1 為同型之四段循環，惟其可觀察量（藍色、風扇大小、LED 數）與加熱側完全不同，故不因形態相同而合併（§8.2 單位歸 037）。刻意略過：**`055-01` 之 popup 內容不驗**（同 11.1，DR #11）；條文之「no arrows are shown」與加熱側之「3 arrows are shown」不一致，**照錄各自之字面**，不推斷孰為筆誤（§8.4.1）。",
"11.3": "驗證目標：11.3（HVS4）一句定出 climate 關閉時狀態列仍顯示座椅狀態，其 037 leaf 即本節自身（無子條）。關鍵情境條件：起始 PC 取第十六軸之正向值（17.3）—— **本節未自帶配備限定語**；依 **R-C34**：可觀察量在**狀態列**，而 6.3 移除者為 head unit 之 comfort section、2.1 移除者為 tabs，**兩者皆不含狀態列** → **第九軸與第十二軸不補**（此為本組內之分野，與 11.1 相反）；第十三軸與 EMEA 補。為什麼這樣切：一葉一 TC，其驗證點為「climate off 之後狀態列仍在」，故步驟必先建立座椅開啟之基線。刻意略過：**本節與 `12.4`（HVS4）逐字相同** —— 兩者同屬本組，其 sibling 判定於組內進行（見 `distinguishing_axis`）。",
"11.4": "驗證目標：11.4（HVS5）以兩句定出加熱座椅鍵作用時為紅、通風座椅鍵作用時為藍，兩個 037 leaf 對應之。關鍵情境條件：第十六軸之正向值（17.3）；依 **R-C34** 第九軸、第十二軸、第十三軸與 EMEA 皆暴露 → 補（其可觀察量在 comfort section 之按鍵本身）。為什麼這樣切：兩色分屬兩個控制，可獨立失效。刻意略過：**本節與 `12.5`（HVS5）逐字相同**，同組內判定；顏色之色碼未定義，ER 依條文用語寫 red／blue 而不寫任何色碼（§8.4.1）。",
"11.6": "驗證目標：11.6（R1HVS1）以六句定出獨立座椅分區之預設、popup 抑制、兩段循環、不可關閉，以及座椅未作用時之 off 態，六個 037 leaf 逐句對應。關鍵情境條件：起始 PC 取 **profile §3.2 第六軸「独立座椅分區有無」**，其字面即本節首句「If the independent seat zone feature is available」；依 **R-C34** 第九／十二／十三軸與 EMEA 皆暴露 → 補。為什麼這樣切：`059-03`／`059-04` 為循環之兩段，取狀態轉換法；`059-05`（不可關閉）為其否定側，與二者成正反（§7）。刻意略過：**`059-02` 之 popup 內容不驗** —— 其驗證點為「不顯示」，不需知道該 popup 長什麼樣（**DR #11** 於此不構成阻礙）。",
"11.6.1": "驗證目標：11.6.1（R1HVS1.1）以兩句定出無硬控之車輛以軟鍵控制座椅分區、其三態與灰化態，兩個 037 leaf 對應之。關鍵情境條件：起始 PC 取本節自帶之限定語（「equipped with the seat zone feature **without a hard control or capacitive control**」）—— **此為 §8.5 之條文自帶觸發條件，非新軸**（形態同 2.9 之「if this feature available」）；依 **R-C34** 四軸中三者暴露 → 補，第十二軸亦補。為什麼這樣切：三態之循環（`060-01`）取狀態轉換法，灰化（`060-02`）之觸發為座椅關閉，兩者失效形態不同。刻意略過：**本節與 `11.7` 之三態循環重疊** —— `11.6.1` 定其「有哪三態」，`11.7` 定其「按下時如何前進與其 popup」，故兩者各自成條（§4.6 見 `distinguishing_axis`）。",
"11.7": "驗證目標：11.7（R1HVS1.2）以四句定出座椅分區軟控之 key cycle 預設、按壓開 popup 並前進一態、popup 之兩種標籤，以及灰化時不開 popup，四個 037 leaf 逐句對應。關鍵情境條件：同 11.6.1（條文自帶之無硬控限定語）；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：`061-04`（灰化時不開）為 `061-02`（按壓即開）之否定側，二者成正反兩側（§7）。刻意略過：**`061-03` 之標籤取條文之逐字原文 «Driver Seat Zone»／«Passenger Seat Zone»**（profile §3.4 之 source-quoted token），**其餘 popup 內容不驗**（DR #11）；`061-01` 之 key cycle 為條文用語，不定義其起訖時點（§8.4.1）。",
"11.8": "驗證目標：11.8（W1HVS2）以四句定出 Multi-Level 加熱方向盤之四段循環及其指示，四個 037 leaf 逐句對應。關鍵情境條件：起始 PC 取 **第七軸「加熱方向盤 Multi / Single」之 Multi-Level 值**（字面即本節首句）；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：與 11.1 同型之四段循環，惟其對象為方向盤。刻意略過：**037 之 leaf 描述在本節與 `12.1`（座椅）逐字相同**（「The system shall fourth press: OFF…」），**主詞只在母節** —— 依 63 §1.2 一律回母節取主詞，故本節四條之主詞為 wheel heat 而非 seat（此即 R-C18 之同型：被省略之欄位不得用於判讀）。",
"11.9": "驗證目標：11.9（R1HVS2）以兩句定出 Single-Level 加熱方向盤之開關兩態，兩個 037 leaf 對應之。關鍵情境條件：起始 PC 取第七軸之 Single-Level 值；依 **R-C34** 三軸暴露 → 補。為什麼這樣切：兩態各自成條，其失效（開不了／關不掉）互相獨立。刻意略過：**`063-01` 之 popup 內容不驗**（DR #11）；本節與 `11.8` 為同一功能在第七軸兩值上之陳述，故非重複而為軸值之別（見 `distinguishing_axis`）。",
"11.10": "驗證目標：11.10（R1HVS3）以三句定出 comfort popup 之出現時機、3 秒之顯示與其重計，以及後續按壓之行為，三個 037 leaf 逐句對應。關鍵情境條件：第十六軸之正向值（17.3）；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：`064-02` 之兩個斷言（3 秒關閉、選取後重計）為同一 leaf 之兩面，故合為一條而以三步涵蓋（§8.2 單位歸 037）。刻意略過：**popup 之內容與版面不驗** —— 本節只定其時機與時長（**DR #11**）；**3 秒為條文明值**，故 ER 寫入該值而不寫「短暫」（R-C22 之反面：有值即用值）。",
"11.11": "驗證目標：11.11（R1HVS4）以三句定出硬鍵配置車輛之 comfort section 不顯示座椅／方向盤控制、其控制仍存在於狀態列與 popup，以及 WS 型觸覺鍵不列於狀態列，三個 037 leaf 逐句對應。關鍵情境條件：`065-01`／`065-02` 取本節自帶之「configured with **hard buttons for comfort controls**」、`065-03` 取本節自帶之 WS 觸覺鍵限定語 —— **兩者皆為 §8.5 之條文自帶觸發條件；本節之「硬鍵配置有無」依三條件查證不得登記為軸**（否定值於 129 節無字面，見上繳 41 §5.3）；依 **R-C34**：`065-01` 之可觀察量在 comfort section → 第九／十二軸補；`065-02`／`065-03` 在**狀態列與 popup** → 二軸不補。為什麼這樣切：`065-01`（不顯示）與 `065-02`（仍存在）為同一配置下之兩個相反斷言，各自可失效（§7）。刻意略過：**「hard buttons for comfort controls」與 `11.6.1` 之「without a hard control」非同一軸** —— 前者指 comfort 控制之整體配置，後者指座椅分區單一功能之控制方式，兩句不可互推（§8.2.1）。",
"11.11.1": "驗證目標：11.11.1（R1HS4.1）一句定出 comfort 控制未作用時於狀態列之組合溫度／comfort 角落呈灰，其 037 leaf 即本節自身（無子條）。關鍵情境條件：第十六軸之正向值（17.3）；依 **R-C34**：可觀察量在**狀態列** → 第九軸與第十二軸不補，第十三軸與 EMEA 補。為什麼這樣切：一葉一 TC，其步驟先使控制不作用再讀狀態列；**條文未定義「不作用」之全部情形**（座椅關閉？climate 關閉？），故步驟以「turn the comfort controls off」為之而不列舉其他途徑（§8.4.1）。",
"12.1": "驗證目標：12.1（HVS1）以四句定出 Multi-Level 加熱座椅之四段按壓循環及其指示，四個 037 leaf 逐句對應。關鍵情境條件：第八軸之 Multi-Level 值（字面即本節首句）；依 **R-C34** 第九／十二／十三軸與 EMEA 皆暴露 → 補。為什麼這樣切：與 `11.1` 同型之四段循環。刻意略過：**本節與 `11.1` 之唯一實質差異為 popup**（`11.1` 之首句有「opens popup」而本節無）—— **DR #11 之問句所指之三對即此**（另二對為 `11.2`↔`12.2`、`11.8`↔`12.1`）；依 63 §1.2 之指示，兩章之比對回**母節 full_text**，不以 037 之 leaf 描述代之（其描述省略主詞，`062-02`～`062-04` 與 `067-02`～`067-04` 逐字相同即其證）。",
"12.2": "驗證目標：12.2（HVS2）以四句定出 Multi-Level 通風座椅之四段循環及其藍色與風扇指示，四個 037 leaf 逐句對應。關鍵情境條件：同 12.1；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：同 `11.2` 之切法。刻意略過：**與 `11.2` 之差異僅為 popup 片語**（DR #11）；本節之「no arrows are shown」與 `11.2` 逐字相同，兩章之該筆語病一致。",
"12.3": "驗證目標：12.3（HVS3）以兩句定出作用中按鍵之文字／圖示為白、未作用者為灰，兩個 037 leaf 對應之。關鍵情境條件：第十六軸之正向值（17.3）；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：兩態各自成條。刻意略過：**本節為 `122-02` 之 R-C39 條件三之第二個候選節**（47 §1 之預裁對象）—— 逐句比對之結果見上繳 41 §6：本節所定為 **active／inactive 之顏色**，`122-02` 所缺為 **system configuration → icon 之對照**，**兩者不同層，條件三不成立**；兩個候選節（`14.16.1`／本節）皆已生成且皆不成立，**47 §1 之預裁條件已滿足**。",
"12.4": "驗證目標：12.4（HVS4）一句定出 climate 關閉時狀態列仍顯示座椅狀態，其 037 leaf 即本節自身。關鍵情境條件：第十六軸之正向值；依 **R-C34**：可觀察量在狀態列 → 第九軸與第十二軸不補。為什麼這樣切：同 `11.3`。刻意略過：**本節與 `11.3` 逐字相同**（實測 100% 相同），故兩者為本組內之等價對，其判定見 `distinguishing_axis` 與 `pending_sibling` 之 `equivalent_tc_pairs`。",
"12.5": "驗證目標：12.5（HVS5）以兩句定出加熱座椅鍵為紅、通風座椅鍵為藍，兩個 037 leaf 對應之。關鍵情境條件：第十六軸之正向值；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：同 `11.4`。刻意略過：**本節與 `11.4` 逐字相同**，同組內判定。",
"12.7": "驗證目標：12.7（HVS7）以兩句定出 popup 之圖片須完整顯示、且不得緊置於按鍵正上方以免裁切，兩個 037 leaf 對應之。關鍵情境條件：第十六軸之正向值；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：「完整」與「位置」為兩個可觀察量，可獨立失效。刻意略過：**本節是 ch12 唯一提及 pop ups 之節**（DR #11 之 leaf 級實測），惟其所定為**版面**而非 popup 之內容或其進入路徑，故不回答 DR #11 之問句；其末句「This also applies to climate controls popups for FAN and MODE」為跨組適用之陳述，**本組不代 `Climate Popups` 組驗之**（§8.2.1）。",
"12.8": "驗證目標：12.8（SHVS1）以三句定出 Standard 加熱座椅之三段循環（HI／LO／OFF）及其指示，三個 037 leaf 逐句對應。關鍵情境條件：起始 PC 取 **第八軸之 Standard 值**（字面即本節首句）；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：三段循環取狀態轉換法。刻意略過：**Standard 與 Multi-Level 之差別在段數（3 vs 4）與箭頭數（2 vs 3）** —— 兩者為第八軸之兩值，故 `12.1` 與本節非重複（見 `distinguishing_axis`）；ch11 無 Standard 之對造節（其 13 節皆為 Multi-Level 或方向盤／分區），此不對稱記於此。",
"12.9": "驗證目標：12.9（SHVS2）以三句定出 Standard 通風座椅之三段循環及其藍色與風扇指示，三個 037 leaf 逐句對應。關鍵情境條件：同 12.8（第八軸之 Standard 值）；依 **R-C34** 三軸暴露 → 補，第十二軸亦補。為什麼這樣切：同 `12.8`。刻意略過：**本節末之「a unhighlighted fan is shown」與 `12.2` 之「no arrows are shown」形態不同**，各依其節之字面立 ER，不互相統一（§8.4.1）。",
}

S16_BLOCKED = ("ch16 十八節中僅 `16.16`（ICE15）提及座椅圖示，**無 Auto Comfort "
               "Settings 之節**；本列為 BLOCKED row，其內容之定義不在本 spec 內，"
               "故 ch16 亦無對造句（R-C36-1 逐條之答為 `no`）")

REASONING["11.5"] = ("驗證目標：11.5（HVS6）全句為「Refer to **HMI Settings List** for the details "
 "on the Auto Comfort Settings options for heated/vented seats.」—— **整條委派予本 spec 以外之文件**，"
 "其 037 leaf 即本節自身（無子條）。**依 DR #43 之裁定（66 §1）產 `[BLOCKED-SPEC]` 列**："
 "扣除該委派後**零餘留**（對照 `14.1` 尚有「pop-ups 存在」之隱含餘留，本節連該隱含餘留都沒有），"
 "與白名單既有二例（`080-02` → HMI Core Logic and Flow、`081-02` → CFTS044）同型；"
 "`[BLOCKED-NON-HMI]` 不適用（內容若給了是 HMI 可觀察之設定選項），`[COVERED-BY]` 不適用"
 "（委派對象非本 spec 之節）。為什麼這樣切：BLOCKED 列不驗行為，其 `test_procedure` 與 "
 "`expected_result` 留白（R-C24），Remarks 於首 60 字元內具名 owner（R-C27）。"
 "刻意略過：**其 ch12 對造 `12.6` 委派之對象為 HMI Notes，與本節不同一份文件** —— "
 "實測共同連續字串 78 字元，在 `HMI ` 之後即分歧，故 R-C40 之前件不成立，"
 "**兩者之解封條件不同**，該後果已逐字寫入 DR #43。")
REASONING["12.6"] = ("驗證目標：12.6（HVS6）全句為「Refer to **HMI Notes** for the details on the Auto "
 "Comfort Settings options for heated/vented seats.」—— 同 `11.5` 之形態（整條外部委派、零餘留），"
 "依 DR #43 之裁定產 `[BLOCKED-SPEC]` 列，其 037 leaf 即本節自身。關鍵情境條件：BLOCKED 列不設"
 "配置式 PC，僅記其可觀察介面之前提（第十六軸之正向值，出處 17.3）。為什麼這樣切：一節一列，"
 "不驗任何行為 —— 其行為之定義不在本 spec 內。刻意略過：**委派對象與 `11.5` 不同**"
 "（HMI Notes vs HMI Settings List），**兩節之條款標籤卻同為 `HVS6.`**（A-CF13 第三項）；"
 "**看起來一樣而依據不同者，最容易在日後被誤以為可以一起處理** —— 見 DR #43 之條目。")

AXIS8 = "profile §3.2 第八軸「Standard vs Multi-Level 座椅」之值（功能型）"
AXIS7 = "profile §3.2 第七軸「加熱方向盤 Multi / Single」之值（功能型）"
CH11_CH12 = "章之別（ch11 `Heated Vented Seats` vs ch12 之同名條款）"

DIST_AXIS = {
 "11.1": {"axis": "章之別（ch11 vs ch12）；本對之實質差異為 `opens popup` 片語",
          "delta": "見 `12.1` 之 delta —— 同一對，自 ch11 側記之。`11.1` 之首句有 `opens popup` 而 `12.1` 無，其餘三段逐字相同，故 `054-02`～`054-04` 與 `067-02`～`067-04` 之 TC 三欄等價（見 `equivalent_tc_pairs`）；**該片語之性質即 DR #11 之問句**，本層不代答，兩份保留、`duplicate_of` 不填"},
 "11.2": {"axis": "章之別（ch11 vs ch12）；本對之實質差異為 `opens popup` 片語",
           "delta": "`11.2` 之首句有 `opens popup` 而 `12.2` 無，其餘三段逐字相同，三對 TC 三欄等價（`055-02`～`055-04` ↔ `068-02`～`068-04`）。處置同 `11.1`↔`12.1`：兩份保留、`duplicate_of` 不填、等價記於 `equivalent_tc_pairs`"},
 "12.2": {"axis": "章之別（ch11 vs ch12）；本對之實質差異為 `opens popup` 片語",
           "delta": "見 `11.2` 之 delta —— 同一對，自 ch12 側記之"},
 "11.3": {"axis": CH11_CH12,
          "delta": "`11.3`（HVS4）與 `12.4`（HVS4）**逐字相同**（實測相似度 1.000，"
                   "62 §1.1 (b) 之量測方式）。**§10.6 四項全同 → 嚴格等價**，"
                   "兩條 TC 亦逐字相同（見 `equivalent_tc_pairs`）。"
                   "`duplicate_of` **不填**：該欄為節級且帶工具側之列號，"
                   "而 037 之兩個 leaf 各自存在（§8.2.2 禁本層合併）。"
                   "**兩章是否為同一需求即 DR #11 之問**，其答案未到之前，"
                   "本層維持兩份並使其可見"},
 "12.4": {"axis": CH11_CH12,
          "delta": "見 `11.3` 之 delta —— 同一對，自 ch12 側記之"},
 "11.4": {"axis": CH11_CH12,
          "delta": "`11.4`（HVS5）與 `12.5`（HVS5）**逐字相同**（實測 1.000）；"
                   "兩節各二 leaf，四條 TC 兩兩等價。處置同 `11.3`：兩份保留、"
                   "`duplicate_of` 不填、等價記於 `equivalent_tc_pairs`"},
 "12.5": {"axis": CH11_CH12, "delta": "見 `11.4` 之 delta"},
 "12.1": {"axis": AXIS8 + "；另與 `11.1` 為 " + CH11_CH12,
          "delta": "**兩個判定**：(一) 對 `12.8`（SHVS1）—— 第八軸之 Multi-Level "
                   "與 Standard 兩值，段數（4 vs 3）與箭頭數（3 vs 2）皆異，"
                   "**非等價**；(二) 對 `11.1`（HVS1）—— **唯一實質差異為 popup "
                   "片語**（`11.1` 有 `opens popup`，本節無），其餘三段逐字相同，"
                   "故 `067-02`～`067-04` 與 `054-02`～`054-04` 之 TC 內容近乎相同"
                   "而其 `test_item` 各自照錄母節（63 §1.2）。**兩章是否應合併即 "
                   "DR #11**，本層不代答"},
 "12.8": {"axis": AXIS8,
          "delta": "見 `12.1` 之 delta (一)：Standard 為三段（HI／LO／OFF）、"
                   "箭頭 2 支，Multi-Level 為四段、箭頭 3 支 —— 同一功能在第八軸"
                   "兩值上之陳述，`duplicate_of` 不填"},
 "11.8": {"axis": AXIS7,
          "delta": "`11.8`（Multi-Level 方向盤，四段）與 `11.9`（Single-Level，"
                   "兩態）為第七軸兩值上之同一功能，段數不同故非等價。"
                   "**另記**：037 對本節之 leaf 描述與 `12.1`（座椅）之描述"
                   "**逐字相同**，因其省略主詞；主詞在母節，本節為方向盤 —— "
                   "leaf 描述不可用於判定等價（63 §1.2／R-C18 同型）"},
 "11.9": {"axis": AXIS7, "delta": "見 `11.8` 之 delta"},
 "11.6.1": {"axis": "同一功能之「有哪些狀態」與「如何前進」之別",
            "delta": "`11.6.1`（R1HVS1.1）定座椅分區軟鍵之**三態集合**與灰化態，"
                     "`11.7`（R1HVS1.2）定其**按壓之前進方式、popup 與其標籤**。"
                     "§10.6 之 trigger 與 verification target 皆異 → 非等價；"
                     "其重疊屬 §4.6 而非 §4.5"},
 "11.7": {"axis": "同一功能之「有哪些狀態」與「如何前進」之別",
          "delta": "見 `11.6.1` 之 delta"},
}

PARENTS = {"11.5": "SWE1-HVAC-058", "12.6": "SWE1-HVAC-072",
           "11.1": "SWE1-HVAC-054", "11.2": "SWE1-HVAC-055",
           "11.3": "SWE1-HVAC-056", "11.4": "SWE1-HVAC-057",
           "11.6": "SWE1-HVAC-059", "11.6.1": "SWE1-HVAC-060",
           "11.7": "SWE1-HVAC-061", "11.8": "SWE1-HVAC-062",
           "11.9": "SWE1-HVAC-063", "11.10": "SWE1-HVAC-064",
           "11.11": "SWE1-HVAC-065", "11.11.1": "SWE1-HVAC-066",
           "12.1": "SWE1-HVAC-067", "12.2": "SWE1-HVAC-068",
           "12.3": "SWE1-HVAC-069", "12.4": "SWE1-HVAC-070",
           "12.5": "SWE1-HVAC-071", "12.7": "SWE1-HVAC-073",
           "12.8": "SWE1-HVAC-074", "12.9": "SWE1-HVAC-075"}
KEYWORDS = {o: [] for o in PARENTS}
ORDER = ["11.1", "11.2", "11.3", "11.4", "11.6", "11.6.1", "11.7", "11.8",
         "11.9", "11.10", "11.11", "11.11.1", "12.1", "12.2", "12.3", "12.4",
         "12.5", "12.7", "12.8", "12.9"]


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
    table = json.loads(TCTABLE.read_text(encoding="utf-8"))
    iar = _iar()
    OUT.mkdir(parents=True, exist_ok=True)
    n = START_N - 1
    total = 0

    for o in ORDER:
        tcs = []
        for (leaf, title, item, proc, er, prio, dm,
             ch16, verdict, sentence) in table[o]:
            n += 1
            base_pc, extra_ref = LEAF_PC.get(leaf, SECTION_PC[o])
            refs = [o] + list(extra_ref)
            extra = [EX_ICS, EX_EMEA]
            if leaf not in STATUS_BAR_ONLY:
                extra += [EX_LOWER, EX_TABS]
            pc = add_lines(base_pc, *extra)
            refs += ["2.14", "16.2"]
            if leaf not in STATUS_BAR_ONLY:
                refs += ["6.3", "2.1"]
            tcs.append({
                "req_id": f"SWE1-HVAC-{leaf}",
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": title,
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": item,
                "pre_conditions": pc,
                "input_test_data": "NA",
                "test_procedure": "\n".join(proc),
                "expected_result": "\n".join(er),
                "specification_reference": ref(*refs),
                "priority": prio,
                "design_method": DM[dm],
                "split_flag": False,
                "split_reason": "",
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
                "emea_ics_review": {"ch16_outline": ch16, "verdict": verdict,
                                    "ch16_sentence": sentence},
            })
        doc = {
            "parent": PARENTS[o], "outline": o, "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o], "keywords": KEYWORDS[o],
            "duplicate_of": "",
            "distinguishing_axis": DIST_AXIS.get(
                o, {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [], "interface_axis_review": iar[o], "tcs": tcs,
        }
        (OUT / f"{PARENTS[o]}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{PARENTS[o]}  {o:8} {len(tcs)} TC")

    # ---- 66 §1 — the two [BLOCKED-SPEC] rows, each its own section/doc
    for o, parent, tc_n, title, item, remarks in BLOCKED_ROWS:
        tc = {
            "req_id": parent,
            "tc_id": TC_ID_FMT.format(n=tc_n),
            "tc_title": title,
            "test_group": TEST_GROUP,
            "test_set": TEST_SET,
            "test_item": item,
            "pre_conditions": add_lines(PC_COMFORT, EX_ICS, EX_EMEA),
            "input_test_data": "NA",
            "test_procedure": "",
            "expected_result": "",
            "specification_reference": ref(o, "17.3", "2.14", "16.2"),
            "priority": "P3",
            "design_method": DM["F"],
            "split_flag": False,
            "split_reason": "",
            "functional_safety": "NA",
            "estimated_test_time": "",
            "remarks": remarks,
            "emea_ics_review": {
                "ch16_outline": "16.16", "verdict": "no",
                "ch16_sentence": S16_BLOCKED},
        }
        doc = {
            "parent": parent, "outline": o, "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o], "keywords": [],
            "duplicate_of": "",
            "distinguishing_axis": {"axis": "see per-TC titles", "delta": ""},
            "assumptions": [], "interface_axis_review": iar[o], "tcs": [tc],
        }
        (OUT / f"{parent}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += 1
        print(f"{parent}  {o:8} 1 TC  [BLOCKED-SPEC]")

    print(f"\n{total} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print("\nWITHHELD — stop-and-report, no row produced:")
    for req, why in WITHHELD:
        print(f"- {req}: {why[:80]}…")
    held = len(WITHHELD)
    print(f"\n{total} emitted + {held} withheld = {total + held} leaves "
          f"declared for {TEST_SET} (framework.md: 59)")
    if total + held != 59 or total != 59:
        raise SystemExit(f"expected 59 / 59, got {total + held} / {total}")


if __name__ == "__main__":
    main()
