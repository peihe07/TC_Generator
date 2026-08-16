#!/usr/bin/env python3
"""Batch 14 generator — Rear Climate (handoff 61 §2).

Scope from framework.md §6's table, derived not retyped (48 §2):

    7.1 3 | 7.1.1 3 | 7.2 5 | 7.3 3 | 7.4 4 | 7.5 4 | 7.6 5 | 7.7 3
    7.8 5 | 7.9 1 | 7.10 2                                    = 38
    9.1 1 | 9.2 2 | 9.3 1 | 9.4 3 | 9.4.1 1                   =  8
                                                       16 節 / 46 leaf

Emitted: 38 TCs, -266 … -303. Withheld: the 8 leaves of ch9 (see WITHHELD).

--------------------------------------------------------------------------
R-C40, answered BEFORE generating, per section (61 §2.1)
--------------------------------------------------------------------------
Only two ch7 sections have a ch2 counterpart that is STOPPED, and both stops
are DR #31:

  7.8 <-> 2.12 (mirror map: `mirrored`)
      CR8  "ON state for the **three** airflow modes is shown by highlighting
            the button and increasing button size"
      C13  "ON state for the **four** airflow modes is shown by ..."
      -> NOT verbatim. And CR8 opens "The Rear Airflow Modes has 3 states:
         1) Feet, 2) Face + Feet, 3) Face" with NO configuration qualifier:
         ch7 has ONE rear mode set, ch2 has THREE competing front sets and
         DR #31 is about which vehicles carry the 4-mode one. The stop is
         grounded in the CHAPTER's context, not in the clause.

  7.1 / 7.8 <-> 2.12.2 (mirror map: `partial`)
      2.12.2's own stop is the same DR #31 loop. CR1 and CR8's hard-control
      sentences are `partial` matches by measurement, not verbatim.

R-C40's precondition is therefore unmet in every case, and all 11 ch7
sections generate. The remaining counterparts (2.2, 2.3, 2.4, 2.6, 2.6.1,
2.7, 2.10, 2.11) are all generated, so R-C36-1's TC-to-TC comparison applies
to them instead; 7.3 and 7.10 are `no-counterpart` (37 §1).

--------------------------------------------------------------------------
"Is a rear-climate axis owed a registration?" (61 §2.2) — NO, and the three
conditions say why
--------------------------------------------------------------------------
  1. two values verbatim:      **FAIL** — only the NEGATIVE value has a
     literal ("If only Front climate is available in a specific vehicle",
     2.1). No sentence in the corpus states the positive value; ch7 asserts
     rear behaviour unconditionally and 2.1 lists "Rear" only as one of the
     tab names.
  2. mutually exclusive/exhaustive, or stated as parallel cases: FAIL — the
     spec never sets the two side by side.
  3. no value supplied by inference: **FAIL** — the positive value is
     obtainable only by negating 2.1, which is DR #17's open question
     ("which configuration produces which tab set").

So the axis is NOT registered, and DR #17 keeps it. It blocks nothing here:
ch7's clauses ARE the rear-climate clauses, so the equipment is the section's
own subject rather than an unstated configuration (R-C28 Q1 is satisfied by
the section itself), and writing "the vehicle has rear climate" as a
pre_condition is exactly the "Climate is available" shape profile §3.2
forbids. That is also what separates these 38 from the four leaves that
stayed stopped (2.11's 015-04/015-05 and 16.11's 116-03/116-04): those are
FRONT-climate clauses whose observable is in the rear, so for them the rear
equipment is an unstated precondition, not the subject.

--------------------------------------------------------------------------
ch9 withheld — the same three conditions, the DR #38 shape
--------------------------------------------------------------------------
CR11 "On some vehicles (See CFTS043 for details), there are additional Rear
Climate controls and shortcuts" is the positive literal, and 9.2/9.4 scope
themselves to it ("in these variants"). The NEGATIVE value has no literal
anywhere in the 129 sections, so conditions 1 and 3 fail exactly as they did
for DR #38's "dual airflow modes 有無" — whose two leaves (17.5) are stopped
for this reason. Same shape, same disposition: 8 leaves stopped, DR #41.

Usage:
    python3 features/comfort/scripts/gen_batch14.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"
TCTABLE = Path("/tmp/b14tcs.json")

TEST_GROUP = "Comfort"
TEST_SET = "Rear Climate"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 266

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

PC_PLAIN = ("1. [test-setup] The rear climate screen is open and the climate "
            "system is on")
PC_FRONT = ("1. [test-setup] The front climate screen is open and the climate "
            "system is on")
# Axis 2, value 四區 — 7.10's own sentence is the literal for that value.
PC_4ZONE = ("1. [spec-verbatim] The vehicle is a 4 Zone Climate vehicle, "
            "which includes two temperature zones in the rear climate (7.10)")
# Axis 2, non-single-zone — SYNC is not shown for single zone configurations
# (2.11, cross-section source per R-C29).
PC_MULTIZONE = ("[spec-derived] The vehicle is not a single zone climate "
                "configuration, for which Sync is not shown (2.11)")
# Axis 1, ATC — CR4 says the current degree is displayed "for ATC systems".
PC_ATC = ("[spec-verbatim] The vehicle has an ATC climate system, for which "
          "the temperature displays the current degree (7.4)")

SECTION_PC = {"7.1": PC_PLAIN, "7.1.1": PC_FRONT, "7.2": PC_PLAIN,
              "7.3": PC_PLAIN, "7.4": PC_PLAIN, "7.5": PC_PLAIN,
              "7.6": PC_PLAIN, "7.7": PC_PLAIN, "7.8": PC_PLAIN,
              "7.9": PC_PLAIN, "7.10": PC_4ZONE}
# 029-03 starts on the REAR screen even though its section starts on the front
# one; the clause's own condition is "if on rear climate screen".
LEAF_PC = {"029-03": PC_PLAIN}
LEAF_EXTRA = {"032-01": (PC_ATC, ()),
              "032-04": (PC_MULTIZONE, ("2.11",)),
              "035-01": (PC_MULTIZONE, ("2.11",)),
              "035-02": (PC_MULTIZONE, ("2.11",)),
              "035-03": (PC_MULTIZONE, ("2.11",))}

CH9_WHY = (
    "**依 61 §2.2 之三條件停下（DR #41）。** 本節之適用範圍由 `9.1`（CR11）"
    "「On some vehicles (See CFTS043 for details), there are additional Rear "
    "Climate controls and shortcuts」界定，本節自身亦以「in these variants」"
    "回指之。**條件一與條件三不成立**：正向值有字面（CR11），"
    "**否定值於全 129 節無任何字面**（實測 pattern `without|no additional|"
    "not equipped` 對 rear climate 之附加控制 0 命中），故該值只能由排除得出。"
    "**與 DR #38（dual airflow modes 有無）同型**，其 `17.5` 之二 leaf 已因"
    "同一理由停下（**處置一致，非新裁**）。**不以 CFTS043 自行補值**："
    "CR11 委派的是「哪些車輛」，補之即為本層代上游決定配置軸（§8.4.1），"
    "且 D-C10 對 20.x 之判讀仍為 `undetermined`")

# 64 §1 — these leaves were withheld here and are now generated by
# gen_batch16.py under R-C42 (the clause carries its own condition).
# They stay in this file's arithmetic so the Test Set's leaf count
# still adds up to framework.md's figure — a leaf that moved must
# not look like a leaf that vanished.
MOVED_TO_BATCH16 = ['SWE1-HVAC-040-01', 'SWE1-HVAC-040-02', 'SWE1-HVAC-041', 'SWE1-HVAC-042-01', 'SWE1-HVAC-042-02', 'SWE1-HVAC-042-03', 'SWE1-HVAC-043']

WITHHELD = [
    ("SWE1-HVAC-039", CH9_WHY + "。**本節自身即 leaf**（037 無子條），"
     "其內容只有「某些車輛另有附加控制」一句，**無可觀察之行為**"),
]

REASONING = {
"7.1": "驗證目標：7.1（CR1）定出「在後排氣候畫面上，前排硬控仍控制前排」此一通則及其兩個例示（風扇旋鈕、駕駛／乘客溫度控制），三個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：起始 PC 為 test-setup（後排畫面已開）—— **本節無配置限定語**；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：通則（`028-01`）與兩個具名控制（`028-02` 風扇、`028-03` 溫度）之失效可各自發生，且後二者之可觀察量分屬不同控制。刻意略過：**其 ch2 對造 `2.12.2` 已停下（DR #31），本節不受其影響** —— 依 **R-C40** 之一問，`2.12.2` 之停下源於前排四模式集合之適用條件（章節脈絡），而 CR1 與 C13.1 末句為 `partial` 而非逐字相同，前件不成立（61 §2.1）。",
"7.1.1": "驗證目標：7.1.1（CR1.1）定出後排硬控之變更不在前排畫面顯示、駕駛須進後排畫面方見其變更，以及在後排畫面上操作前排控制時仍出 popup，三個 037 leaf 對應之。關鍵情境條件：起始 PC 依各條之視點而異 —— `029-01`／`029-02` 自**前排**畫面起（其斷言為「前排畫面不顯示」），`029-03` 依條文自帶之條件「if on rear climate screen」自**後排**畫面起；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`029-01`（不顯示）與 `029-03`（顯示）為同一 popup 機制之正反兩側（§7），其否定式一條與正向一條各自成立。刻意略過：**popup 之內容與版面不在本節** —— CR1.1 只述其出現與否，`14.x`（HVAC Popups）方述其內容；本節之 ER 不描述 popup 內部（§8.2.1）。",
"7.2": "驗證目標：7.2（CR2）定出後排 AUTO 之狀態呈現、其對風速與模式之作用、與三種氣流模式之互斥、中斷條件與其落點，以及不中斷之情形，五個 037 leaf 逐句對應之。關鍵情境條件：起始 PC 為 test-setup —— **CR2 未如 C2 般載明「AUTO is not shown in MTC configurations」，故本節不補第一軸**（不以前排條文補後排，§8.2.1）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`030-04`（中斷後落到最接近之手動模式，除非按下特定模式鍵）取狀態轉換法，其失效形態（落錯模式）與 `030-05`（不中斷）相反，二者成正反兩側。刻意略過：**後排是否亦有 `AUTO ECO`（DR #25）** —— ch10 全 9 節對 `rear` 零命中而 CR2 只述兩狀態，故本節之 AUTO 一律以兩狀態驗之，**不引入 ch10 之三狀態**（§8.4.1）。",
"7.3": "驗證目標：7.3（CR3）定出 LOCK REAR 之狀態、其對後排控制之鎖定，以及文字與圖示之對應切換，三個 037 leaf 對應之。關鍵情境條件：起始 PC 為 test-setup；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：鎖定之效力（`031-01`）、文字之切換（`031-02`）與圖示之切換（`031-03`）三者可獨立失效 —— 條文把文字與圖示寫成一組對應（unlocked = Lock Rear text with unlocked icon／locked = Unlock Rear text with Lock icon），惟其為兩個可觀察量。刻意略過：**本節於 ch2 為 `no-counterpart`**（鏡射表已記：前排無鎖定能力），故無 TC 對 TC 之比對對象，亦不得以任何前排條文類推（§8.2.1）。",
"7.4": "驗證目標：7.4（CR4）定出後排溫度之範圍與呈現、slider 之 TEMP popup、Metric 之半度增量與其四處同步，以及 SYNC 開啟時之連動與中斷，四個 037 leaf 對應之。關鍵情境條件：`032-01` 依條文自帶之「for ATC systems」補第一軸之 ATC 值（出處 7.4 自身）；`032-04` 補第二軸之非單區值（出處 2.11，跨節取據 R-C29）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`032-01` 取 BVA —— 其失效集中在兩端（最高顯示 HI、最低顯示 LO）；`032-03` 亦取 BVA，因半度增量之失效形態即進位邊界。刻意略過：**`hold longer that 500 ms` 之長按門檻於本節有值而前排無值（DR #21）** —— 本輪不驗長按之時間門檻，因其可判性依賴計時設備而條文未定量測方法；該不對稱之方向已於上繳 30 §2.3 訂正為「前排缺值」。",
"7.5": "驗證目標：7.5（CR5）定出後排風速之值域與呈現位置、三種調整途徑、不可自畫面關閉風扇之限制，以及全暗之唯一途徑，四個 037 leaf 對應之。關鍵情境條件：起始 PC 為 test-setup；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`033-01` 取 BVA（Off／1／7／15h 為值域端點）；`033-03`（恆有一格高亮）與 `033-04`（唯一之全暗途徑）為同一限制之兩面，前者為否定式、後者給出其唯一例外（§7）。刻意略過：**前排之第二值域 `Off, 1-8`（2.7.1 C6.1，profile §3.2 第十四軸）不適用於後排** —— CR5 只列一組值域，ch7 無第二值域之節（鏡射表 `no-counterpart`），故本節不補第十四軸。",
"7.6": "驗證目標：7.6（CR6）定出後排氣候關閉之狀態與其畫面、按鈕轉換與空白化之例外，以及前排關閉時之連動與後排之不可用，五個 037 leaf 逐句對應之。關鍵情境條件：起始 PC 為 test-setup；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`034-04`（前排關閉時之畫面轉換）與 `034-05`（後排不可用）雖同源於「front climate off」，惟前者之可觀察量為畫面轉換與 REAR CLIMATE 按鈕之空白化，後者為後排之不可操作，兩者可獨立失效。刻意略過：**本節與 `2.10`（C11）為 `partial` 鏡射（共用 climate off 之骨架）而非逐字相同** —— 兩節之 TC 皆已產出，其 `expected_result` 分屬前排與後排畫面，無共用可觀察量（§8.2.1 不互相移植）。",
"7.7": "驗證目標：7.7（CR7）定出 SYNC 之狀態呈現、前後排之連動範圍（溫度、模式、風速）與其中斷條件，三個 037 leaf 對應之。關鍵情境條件：三條全補第二軸之非單區值（出處 2.11「Sync is not shown for single zone climate configurations」，跨節取據 R-C29）—— **CR7 自身未載該限定語，惟 C12 與 ICE10 皆載之，且三節述同一 SYNC**；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`035-01`（連動）與 `035-02`（中斷）為相反方向；`035-03`（風速與鼓風前後同步）之可觀察量與前二者不同。刻意略過：**`2.11` 之 `015-04`／`015-05` 停下而本節生成，其分野已於上繳 40 §2 具名** —— 前者為**前排**條文而其可觀察量在後排，後排配備成為未陳述之前提；本節之主體即後排，該事實由本章自身承擔（R-C28 第一問）。",
"7.8": "驗證目標：7.8（CR8）定出後排三種氣流模式、ON 態之呈現、與 AUTO 之互斥、單選性，以及硬鍵之循環與長按行為，五個 037 leaf 逐句對應之。關鍵情境條件：起始 PC 為 test-setup —— **CR8 陳述一組（且僅一組）後排模式集合，無配置限定語**；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。**R-C40 之一問已於生成前作答**（61 §2.1）：其 ch2 對造 `2.12` 之句子為「ON state for the **four** airflow modes…」而 CR8 為「**three**」，**非逐字相同**，前件不成立；`2.12` 之停下（DR #31）源於 ch2 有**三組**前排模式集合而其一無正面適用條件，**ch7 只有一組**，該問題於此不存在 —— 屬章節脈絡而非條文性質。為什麼這樣切：`036-05` 取狀態轉換法（循環序與長按只跳一格），其失效形態與其餘四條無關。刻意略過：**CR8 未列後排硬鍵循環之模式順序** —— 故 `036-05` 之 ER 只寫「移至 loop 中之下一個模式」而不列舉順序（§8.4.1）。",
"7.9": "驗證目標：7.9（CR9）全節僅一句「A/C has on/ off state.」，其 037 leaf 即本節自身（無子條），故一節一 TC。關鍵情境條件：起始 PC 為 test-setup；依 **R-C34** 第九軸與第十三軸暴露 → 補，EMEA 排除補並答。為什麼這樣切：條文只給狀態，故 TC 只驗開與關兩態之切換，**不驗任何連動**。刻意略過：**`2.4`（C3）之四項連動（Auto／Defrost／Recirc 可自動開 A/C、A/C 中斷 Auto）於 ch7 全 11 節不存在**（**DR #28** 已具名）—— 以 C3 補之即以前排條文補後排（§8.4.1 造值）；`7.2`（CR2）述後排 AUTO 之中斷條件亦不含 A/C，故此缺口非本層可補。",
"7.10": "驗證目標：7.10（CR10）定出 4 Zone Climate 之後排兩溫區與其各自之滑桿，兩個 037 leaf 對應之。關鍵情境條件：起始 PC 取 **profile §3.2 第二軸之「四區」值**，其字面即 CR10 自身（「4 Zone Climate includes two temperature zones in the rear climate」）—— **本節是該軸四區值於全 corpus 之唯一正面出處**；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`038-01` 驗兩滑桿之存在，`038-02` 驗其各控其區，後者之失效（兩區連動）不會使前者失效。刻意略過：**本節之 037 描述帶圖**（A-CF23 名單內）—— 五問之答皆為否：圖中之滑桿位置與外觀非條文所定，ER 只驗「兩個獨立滑桿存在且各控其區」，不指名任何版面座標（§8.4.1）；本節於 ch2 為 `no-counterpart`。",
}

DIST_AXIS = {
    "7.2": {
        "axis": "所控之氣候區（前排 vs 後排）—— 同一行為在兩區之兩處陳述",
        "delta": "`2.3` 之主體為**前排**AUTO（其狀態、15h 指示、與氣流模式之互斥、中斷條件），`7.2` 之主體為**後排**同一AUTO（其狀態、15h 指示、與氣流模式之互斥、中斷條件）（鏡射表記其為 partial／mirrored）。**§10.6 逐項**：trigger 之操作對象不同（前排控制 vs 後排控制）、outcome 之可觀察量不同（前排風速／模式 vs 後排風速／模式）、input 皆 NA、verification target 各為該區之行為。**四項中兩項相異 → 非嚴格等價，`duplicate_of` 不填。** 與 `2.9`↔`16.9` 之四對逐字等價不同：**該對之兩側互斥**（同一車不可能既 ICS 又非 ICS），**本對之兩側並存**（一台四區車同時有前排與後排），故兩條 TC 於同一車上皆須執行",
    },
    "7.4": {
        "axis": "所控之氣候區（前排 vs 後排）—— 同一行為在兩區之兩處陳述",
        "delta": "`2.6` 之主體為**前排**溫度（值域、HI／LO、Metric 半度、slider 與 popup），`7.4` 之主體為**後排**同一溫度（值域、HI／LO、Metric 半度、slider 與 popup）（鏡射表記其為 partial／mirrored）。**§10.6 逐項**：trigger 之操作對象不同（前排控制 vs 後排控制）、outcome 之可觀察量不同（前排溫度顯示 vs 後排溫度顯示）、input 皆 NA、verification target 各為該區之行為。**四項中兩項相異 → 非嚴格等價，`duplicate_of` 不填。** 與 `2.9`↔`16.9` 之四對逐字等價不同：**該對之兩側互斥**（同一車不可能既 ICS 又非 ICS），**本對之兩側並存**（一台四區車同時有前排與後排），故兩條 TC 於同一車上皆須執行",
    },
    "7.5": {
        "axis": "所控之氣候區（前排 vs 後排）—— 同一行為在兩區之兩處陳述",
        "delta": "`2.7` 之主體為**前排**風速（值域、三種調整途徑、不可自畫面關閉之限制），`7.5` 之主體為**後排**同一風速（值域、三種調整途徑、不可自畫面關閉之限制）（鏡射表記其為 partial／mirrored）。**§10.6 逐項**：trigger 之操作對象不同（前排控制 vs 後排控制）、outcome 之可觀察量不同（前排風速格 vs 後排風速格）、input 皆 NA、verification target 各為該區之行為。**四項中兩項相異 → 非嚴格等價，`duplicate_of` 不填。** 與 `2.9`↔`16.9` 之四對逐字等價不同：**該對之兩側互斥**（同一車不可能既 ICS 又非 ICS），**本對之兩側並存**（一台四區車同時有前排與後排），故兩條 TC 於同一車上皆須執行",
    },
    "7.7": {
        "axis": "所控之氣候區（前排 vs 後排）—— 同一行為在兩區之兩處陳述",
        "delta": "`2.11／2.6.1` 之主體為**前排**SYNC（其狀態指示與連動、中斷條件），`7.7` 之主體為**後排**同一SYNC（其狀態指示與連動、中斷條件）（鏡射表記其為 partial／mirrored）。**§10.6 逐項**：trigger 之操作對象不同（前排控制 vs 後排控制）、outcome 之可觀察量不同（前排駕駛／乘客溫度 vs 前後排之溫度、模式與風速）、input 皆 NA、verification target 各為該區之行為。**四項中兩項相異 → 非嚴格等價，`duplicate_of` 不填。** 與 `2.9`↔`16.9` 之四對逐字等價不同：**該對之兩側互斥**（同一車不可能既 ICS 又非 ICS），**本對之兩側並存**（一台四區車同時有前排與後排），故兩條 TC 於同一車上皆須執行",
    },
    "7.8": {
        "axis": "所控之氣候區（前排 vs 後排）—— 同一行為在兩區之兩處陳述",
        "delta": "`2.12` 之主體為**前排**氣流模式（狀態集合、ON 態呈現、單選性、硬鍵循環），`7.8` 之主體為**後排**同一氣流模式（狀態集合、ON 態呈現、單選性、硬鍵循環）（鏡射表記其為 partial／mirrored）。**§10.6 逐項**：trigger 之操作對象不同（前排控制 vs 後排控制）、outcome 之可觀察量不同（前排四模式鍵 vs 後排三模式鍵）、input 皆 NA、verification target 各為該區之行為。**四項中兩項相異 → 非嚴格等價，`duplicate_of` 不填。** 與 `2.9`↔`16.9` 之四對逐字等價不同：**該對之兩側互斥**（同一車不可能既 ICS 又非 ICS），**本對之兩側並存**（一台四區車同時有前排與後排），故兩條 TC 於同一車上皆須執行。**另**：`2.12` 因 DR #31 停下而本節生成，其 R-C40 之一問已於生成前作答（61 §2.1）",
    },
}

PARENTS = {"7.1": "SWE1-HVAC-028", "7.1.1": "SWE1-HVAC-029",
           "7.2": "SWE1-HVAC-030", "7.3": "SWE1-HVAC-031",
           "7.4": "SWE1-HVAC-032", "7.5": "SWE1-HVAC-033",
           "7.6": "SWE1-HVAC-034", "7.7": "SWE1-HVAC-035",
           "7.8": "SWE1-HVAC-036", "7.9": "SWE1-HVAC-037",
           "7.10": "SWE1-HVAC-038"}
KEYWORDS = {"7.1": ["hard controls", "rear climate screen"],
            "7.1.1": ["popup", "rear climate screen"],
            "7.2": ["AUTO", "15h", "mutually exclusive"],
            "7.3": ["LOCK REAR", "UNLOCK REAR", "lock icon"],
            "7.4": ["LO", "HI", "half degree", "slider"],
            "7.5": ["fan ranges", "Off, 1-7", "15h"],
            "7.6": ["REAR CLIMATE OFF", "REAR ON", "blank"],
            "7.7": ["SYNC", "front to back"],
            "7.8": ["3 states", "Feet", "Face", "loop"],
            "7.9": ["A/C", "on/ off state"],
            "7.10": ["4 Zone Climate", "temperature zones"]}
ORDER = ["7.1", "7.1.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8",
         "7.9", "7.10"]


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
            refs = [o]
            pcs = [LEAF_PC.get(leaf, SECTION_PC[o])]
            if leaf in LEAF_EXTRA:
                line, more = LEAF_EXTRA[leaf]
                pcs.append(line)
                refs += list(more)
            pc = add_lines("\n".join(pcs), EX_ICS, EX_EMEA, EX_LOWER)
            refs += ["2.14", "16.2", "6.3"]
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

    print(f"\n{total} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print("\nWITHHELD — stop-and-report, no row produced:")
    for req, why in WITHHELD:
        print(f"- {req}: {why[:90]}…")
    held = len(WITHHELD)
    moved = len(MOVED_TO_BATCH16)
    print(f"\n{total} emitted + {held} withheld + {moved} moved to "
          f"batch 16 (R-C42) = {total + held + moved} leaves "
          f"declared for {TEST_SET} (framework.md: 46)")
    if total + held + moved != 46 or total != 38:
        raise SystemExit(
            f"expected 46 / 38, got {total + held + moved} / {total}")


if __name__ == "__main__":
    main()
