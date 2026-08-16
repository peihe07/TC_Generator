#!/usr/bin/env python3
"""Batch 11 generator — Climate Popups (handoff 55 §1).

Scope from framework.md §10's table, derived not retyped (48 §2): 23 sections,
42 leaves. 037 measured independently: 42.

Emitted: 36 TCs, -167 … -202.
WITHHELD: 6 leaves, four causes, none new:

  14.1  (1)  "HVAC pop-ups should follow the pop-up list" — an EXTERNAL
             document (HMI Pop Up List, DR #11, never supplied). [BLOCKED-SPEC]
             shape; the whitelist is a ruling (R-C26), so stop and report
  14.12 (3)  DR #37's three questions
  14.14 (1)  dual airflow modes (DR #38) AND screen size (DR #6) at once
  14.15 (1)  "Available comfort controls ... depend on vehicle configuration"
             with no mapping — DR #32's class

15.1's nature was judged BEFORE deciding its leaves (55 §1.1). It is BOTH a
chart reference and a behaviour clause, and 037 already split them the right
way: its two leaves are "pop-up displays current system state" and "graphics
are examples, show actual state" — the residue, not the chart. **037 produced
no leaf for the chart mapping itself**, so that mapping is an R-C16 coverage
gap (no workbook row), not a leaf we may invent. Both leaves generate.

14.16.1 generates, so 122-02's R-C39 condition three could finally be tested
against a real ER — reported in 上繳 37 §5.3. Short version: it fails, but
only ONE of the two candidate sections exists, so 47 §1's trigger ("該二節
生成後") is not yet met and DR #32 is NOT escalated this round.

ch14 has NO ch16 counterpart at all (`ch16_mirror_map.tsv`'s ch14 side is
empty), so every TC's `emea_ics_review` is the same `no-counterpart` answer,
stated per TC rather than section-level (R-C36-1).

Usage:
    python3 features/comfort/scripts/gen_batch11.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"
TCTABLE = Path("/tmp/b11tcs.json")

TEST_GROUP = "Comfort"
TEST_SET = "Climate Popups"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 167

DM = {"F": "功能測試 (Functional based ; no specific technique)",
      "S": "狀態轉換 (State Transition Testing)"}

EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_EMEA = ("[spec-derived] The vehicle is not an EMEA ICS vehicle, whose "
           "climate interface is specified separately in chapter 16 (16.2)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
PC_PLAIN = "1. [test-setup] The head unit is on and the climate system is on"
# Axis 9 — 14.13 is the ONE section here whose subject IS the lower screen, so
# it takes the axis's other value: the vehicle HAS one. Everywhere else the
# observable is a head-unit pop-up, which 6.3 keeps ("except for comfort
# popups"), so axis 9 is not exposed at all in this batch — the first batch
# where that exclusion is dropped on evidence rather than carried by habit.
PC_LOWER_PRESENT = ("1. [spec-derived] The vehicle has a lower HVAC screen "
                    "(14.13)")
# Axis 16 — the seat-comfort sections observe comfort controls, which exist
# only on vehicles equipped with them.
PC_COMFORT = ("1. [spec-derived] The vehicle is equipped with Comfort "
              "features, whose available comfort controls depend on vehicle "
              "configuration (14.15)")
# 機型軸. 14.19 states the R1Low/R1H split itself; only -104-02 turns on it.
PC_R1LOW = ("2. [spec-derived] The vehicle is an R1Low vehicle, for which "
            "the FAN Speed Pop-up is shown (14.19)")
# 14.19's whole clause is conditioned on the widget being on screen.
PC_WIDGET_SHOWN = ("1. [spec-derived] The Climate widget is shown on the "
                   "currently displayed screen (14.19)")

# Per-section starting pre_condition and the extra spec_ref sections it cites.
SECTION_PC = {o: (PC_PLAIN, ()) for o in
              ["14.1.1", "14.2", "14.3", "14.4", "14.5", "14.6", "14.7",
               "14.8", "14.9", "14.10", "14.10.1", "14.11", "15.1"]}
SECTION_PC["14.13"] = (PC_LOWER_PRESENT, ())
for o in ["14.16", "14.16.1", "14.17", "14.18"]:
    SECTION_PC[o] = (PC_COMFORT, ("14.15",))
SECTION_PC["14.19"] = (PC_WIDGET_SHOWN, ())
LEAF_PC = {}
LEAF_EXTRA = {"104-02": (PC_R1LOW, ())}
# Axis 9 is NOT excluded in this batch — see PC_LOWER_PRESENT's note.
NO_AXIS9 = True

REASONING = {
"14.1.1": "驗證目標：14.1.1（HVACP1.2）定出同一 HVAC 事件之再次調整使 popup 逾時重新計時，單一 037 leaf 對應之（§8.2.1）。關鍵情境條件：本節無配置條件，起始 PC 為 test-setup；依 **R-C34**，可觀察量為 HVAC popup 本身 —— **第九軸不補**：6.3 之移除對象為 head unit 之 comfort section，而其明文例外正是 `except for comfort popups`，故 popup 於下螢幕車上仍在（**本批為首次以證據放下該排除，而非沿襲**）；第十三軸補（3 旋鈕 ICS 車無 HVAC popup）；EMEA 排除補並逐條答。為什麼這樣切：條文僅一句一 leaf，不拆。刻意略過：條文未給該 popup 之逾時秒數（`14.18` 之 5 秒為座椅類 popup，屬另一節），故步驟以「就在逾時前」為時點而不寫入秒數（§8.4.1）。",
"14.2": "驗證目標：14.2（HVACP2）定出 RVC 畫面作用中時不顯示 HVAC popup，單一 leaf 對應之。關鍵情境條件：同 14.1.1（第九軸不補、第十三軸補、EMEA 排除補）。為什麼這樣切：一句一 leaf。刻意略過：條文未定義 RVC 畫面之進入方式，依 profile §3.2 之「入口或操作方式未定義」清單，照錄用語並具名，併入 `DATA_REQUESTS` #34 之 `entry` 子類，**不自造入口步驟**（§8.4.1）。",
"14.3": "驗證目標：14.3（HVACP3.1）定出 HVAC popup 具互動性，兩個 037 leaf 分別對應「可互動」與「可自 popup 調整參數」（§8.2.1）。關鍵情境條件：同 14.1.1。為什麼這樣切：`086-01` 驗其可被操作，`086-02` 驗操作之結果生效，兩者失效形態不同（按下無反應 vs 有反應而值不變）。刻意略過：條文以 `e.g.` 舉三種 popup（Temp／fan speed／mode），本批以 fan popup 為代表而不逐一列舉 —— 三者之互動性為同一需求，逐一產出即同一可觀察量重複（§4.5）。",
"14.4": "驗證目標：14.4（HVACP4）定出 simulated off/idle 模式下 HVAC popup 之單獨顯示，兩個 leaf 分別對應「只顯示 popup」與「status bar／category bar／brand background 不顯示」。關鍵情境條件：同 14.1.1。為什麼這樣切：兩者為同一畫面之正反兩面（該顯示者顯示、不該顯示者不顯示），依 §7 各自成條。刻意略過：條文未定義如何進入 simulated off/idle 模式 —— 併入 #34 之 `entry` 子類，不自造。",
"14.5": "驗證目標：14.5（HVACP5）定出 HVAC popup 顯示於 NAV／第三方 App／Projection 之上，單一 leaf。關鍵情境條件：同 14.1.1。為什麼這樣切：一句一 leaf。刻意略過：條文之 `when permitted` 未定義何時為 permitted，故 ER 停在「於該畫面之上顯示」而不宣稱任何許可條件（§8.4.1）；三種畫面取 NAV 與 Projection 兩種為步驟，第三方 App 之進入方式未定義（#34 之 `entry` 子類）。",
"14.6": "驗證目標：14.6（HVACP6）定出觸碰下層 popup 之非可選區域使 HVAC popup 關閉，單一 leaf。關鍵情境條件：同 14.1.1。為什麼這樣切：一句一 leaf。刻意略過：條文未定義「另一個 popup」為何者，故步驟以「開啟一個 popup」為前置而不指名 —— 指名即造值（§8.4.1）。",
"14.7": "驗證目標：14.7（HVACP7）定出觸碰下層 popup 之可選項時執行其動作且關閉 HVAC popup，兩個 leaf 分別對應「動作被執行」與「HVAC popup 關閉」。關鍵情境條件：同 14.1.1。為什麼這樣切：兩者可獨立失效（動作執行了而 popup 未關、或 popup 關了而動作未執行）。刻意略過：同 14.6，不指名下層 popup。",
"14.8": "驗證目標：14.8（HVACP8）定出按壓兩個 popup 之外的區域使兩者皆關閉，單一 leaf。關鍵情境條件：同 14.1.1。為什麼這樣切：一句一 leaf。刻意略過：同 14.6，不指名下層 popup。",
"14.9": "驗證目標：14.9（HVACP9）定出 intro／outro 動畫與 splash 畫面期間不顯示 HVAC popup，單一 leaf。關鍵情境條件：同 14.1.1。為什麼這樣切：一句一 leaf。刻意略過：條文列 intro／outro／splash 三種情形而 037 只給一個 leaf，故本條以 intro 動畫為步驟並於 test_item 保留三者之全稱 —— 依 R-C33 單位歸 037，不因條文列舉而拆（§8.2.2）。",
"14.10": "驗證目標：14.10（HVACP10）定出 idle 模式下 popup 之顯示與非 idle 時相同，單一 leaf。關鍵情境條件：同 14.1.1。為什麼這樣切：一句一 leaf；其驗證形態為**前後對照**（§5.6），故首步先於非 idle 建立基線。刻意略過：條文未定義 idle 模式之進入方式（#34 之 `entry` 子類）；本條與 14.4 之界線 —— 14.4 驗「blank 畫面上只有 popup」，本條驗「popup 本身之呈現不變」，兩者可觀察量不同（§4.5）。",
"14.10.1": "驗證目標：14.10.1（HVACP10.1）定出 Climate 位於主類別列時，風速與模式 popup 於 idle 期間亦自該位置顯示，單一 leaf。關鍵情境條件：同 14.1.1；條文之前件「If Climate is located in the main category bar」為版面配置，**其變異範圍未定義**，故不寫入配置式 PC 而以步驟之觀察對象承載（§8.4.1）。為什麼這樣切：一句一 leaf。刻意略過：條文列 fan speed 與 mode 兩種 popup，本條以 fan popup 為代表（同 14.3 之理由）。",
"14.11": "驗證目標：14.11（HVACP11）定出 popup 僅由使用者之直接互動觸發，兩個 leaf 分別對應「系統自動變更不顯示」與「直接互動才顯示」。關鍵情境條件：同 14.1.1。為什麼這樣切：兩者為同一規則之正反兩側，依 §7 各自成條 —— 只驗其一即無法區分「永遠不顯示」與「正確地只在互動時顯示」。刻意略過：條文以 ignition cycle 為例，本條照用該例而不擴及其他自動變更 —— 其他情形條文未列舉（§8.4.2）。",
"14.13": "驗證目標：14.13（HVACP13）定出配備下 HVAC 螢幕之車輛，於該螢幕上之操作不觸發 head unit 之 popup，單一 leaf。關鍵情境條件：**本節之配置條件為第九軸之另一值** —— 條文明文「For vehicles with **a lower hvac screen**」，故 PC 取其**有**值（出處 14.13），與本批其餘各節之「不補第九軸」形成對照：其餘節之可觀察量為 comfort popup（6.3 之明文例外），而本節之主題正是該螢幕本身。依 **R-C34** 第十三軸補、EMEA 排除補。為什麼這樣切：一句一 leaf。刻意略過：條文以 `e.g.` 舉三種 popup，本條以溫度 popup 為代表（同 14.3）。",
"14.16": "驗證目標：14.16（HVACSB2）定出駕駛與乘客座椅舒適功能之狀態呈現、狀態列圖示之按壓行為，以及 Heat／Vent 之標示，三個 037 leaf 對應之。關鍵情境條件：**第十六軸（Comfort Features 有無）取其有值** —— 出處 `14.15`（「Available comfort controls … depend on vehicle configuration」，跨節取據 R-C29，14.15 併入 spec_ref）；依 **R-C34** 第九軸不補（可觀察量為狀態列與 popup）、第十三軸補、EMEA 排除補。為什麼這樣切：三者之可觀察量互異（狀態之呈現／按壓之結果／標籤文字）。刻意略過：條文未定義 level 之級數，故 `100-03` 之 ER 停在「級數改變」而不寫入任何數值（§8.4.1）—— 級數屬 ch11／ch12 之範圍（§8.2.1）。",
"14.16.1": "驗證目標：14.16.1（HVACSB2.1）定出座椅分區之狀態呈現、三態循環、Zone 標示，以及座椅關閉時之灰化，三個 037 leaf 對應之。關鍵情境條件：同 14.16（第十六軸取有值，出處 14.15）。為什麼這樣切：`101-01` 之三態循環取狀態轉換法，其失效形態（順序錯、循環不回頭）與 `101-03` 之灰化無關。刻意略過：**本節為 `122-02` 之 R-C39 條件三之候選節之一**（47 §1 之預裁對象）—— 逐句比對之結果見上繳 37 §5.3：本節所述為「座椅關閉時圖示變灰」，**非 configuration 到 icon 之對照**，條件三不成立；惟另一候選節 `12.3` 尚未生成，故 47 §1 之觸發條件（該二節生成後）未齊，**本輪不升 DR #32 之等級**。",
"14.17": "驗證目標：14.17（HVACSB3）定出駕駛座椅舒適功能與乘客舒適控制併入車艙溫度且可按壓，按壓後顯示含兩者之 popup，單一 leaf。關鍵情境條件：同 14.16。為什麼這樣切：一句一 leaf；其「併入」與「按壓後之 popup 內容」為同一 leaf 之兩面，故以兩步涵蓋。刻意略過：條文未定義併入後之版面位置，故 ER 停在「顯示為與車艙溫度併合」而不描述版面（§8.4.1）。",
"14.18": "驗證目標：14.18（HVACSB5）定出 popup 之 5 秒逾時與再次按壓之重新計時，兩個 037 leaf 對應之。關鍵情境條件：同 14.16。為什麼這樣切：逾時與重新計時可獨立失效。刻意略過：**5 秒為條文明值，照用**（R-C22 允明值）；本節之 popup 與 14.1.1 之 HVAC popup 逾時**分屬兩節**（前者為座椅類 popup，後者為 HVAC 事件 popup），其可觀察量不同，故不合併（§4.5）。",
"14.19": "驗證目標：14.19（HVACSB6）定出 Climate widget 顯示於當前畫面時八類 popup 之行為，八個 037 leaf 逐項對應（§8.2.1）。關鍵情境條件：條文自身之前件「When the Climate widget is shown on the currently displayed screen」為明文情境條件，標 spec-verbatim（出處 14.19）；`104-04`（風速 popup）另取**機型軸**之 R1Low 值 —— 條文明文「show for R1Low, do not show for R1H」；依 **R-C34** 第九軸不補、第十三軸補、EMEA 排除補。為什麼這樣切：八項之行為互異（只在狀態列／顯示／不顯示三種），逐項成條使任一項之失效可定位。刻意略過：**R1H 側之「do not show」未產出 TC** —— 037 之 `104-02` 只寫 `fan Speed Pop-up: show`，未給 R1H 之 leaf；依 R-C33 單位歸 037，不自行增列（§8.2.2），該缺口依 §8.4.2 於此具名。",
"15.1": "驗證目標：15.1（HVACP11.1）之性質**先判再處置**（55 §1.1）：本節**兼具對照表與行為條文兩種性質** —— 其「the HVAC pop ups displayed will follow the chart below」為對照表（該表為圖片，A-CF23），而「all pop ups should display current state of the HVAC systems (not the exact pictures below…)」為可驗之行為條文。**037 已把兩者分開**：其兩個 leaf 皆屬後者（顯示當前狀態／圖為示例），**對照表本身無 leaf**，故本節兩條皆生成，而**對照表之缺口為 R-C16 形態**（037 未產出該 leaf，不產 workbook 列、不入分母），已於上繳 37 §5.2 具名。關鍵情境條件：同 14.1.1。為什麼這樣切：`105-01` 驗 popup 顯示當前狀態，`105-02` 驗其不依圖片所示，後者以「與圖片不同之值」為輸入，兩者失效形態不同。刻意略過：**不得將表格內容當作行為驗證**（55 §1.1）—— 故無任何一條驗「某功能進入時顯示某 popup」，那正是缺的對照。",
}

# 53 §2.1 / §4.6 — `2.12.1 ↔ 3.1` is recorded `sibling` (41 §2, the tri-mode
# axis) and 3.1 is already generated, so this doc owes the backfill.
# §10.6 strict equivalence, per TC:
#   -163 vs -015  trigger: cycle the airflow modes
#                 target : the 5-state ORDER      vs the 7-combination toggling
#   -164 vs -015  target : the active mode's rendering on a 5-state vehicle
#                          vs on a tri-mode vehicle
# Same requirement, different value of axis 3 — which is what makes them
# siblings — so the verification targets differ by construction and
# duplicate_of does NOT apply.
DIST_AXIS = {
    "2.12.1": {
        "axis": "profile §3.2 第三軸「前排氣流模式集合」之值",
        "delta": "`2.12.1` 取 **5 狀態**（C13.0「In some non-tri mode "
                 "equipment types, airflow modes has 5 states」），"
                 "`3.1` 取 **tri-mode 3 鍵 7 組合**（C19）。"
                 "**兩者為同一需求（本車之氣流模式集合與其選取方式）在該軸"
                 "兩個值上之陳述**，故其 verification target 必然相異 —— "
                 "`017-01` 驗五狀態之循環序，`023-01`／`023-02` 驗七組合之個別 "
                 "toggle 與循環序。四項嚴格等價不成立，`duplicate_of` 不填。"
                 "第三值（4 模式，`2.12`）因 DR #31 未生成，故本軸三值中"
                 "目前只有兩個有 TC",
    },
}

# 64 §1 — these leaves were withheld here and are now generated by
# gen_batch16.py under R-C42 (the clause carries its own condition).
# They stay in this file's arithmetic so the Test Set's leaf count
# still adds up to framework.md's figure — a leaf that moved must
# not look like a leaf that vanished.
MOVED_TO_BATCH16 = ['SWE1-HVAC-096-01', 'SWE1-HVAC-096-02', 'SWE1-HVAC-096-03', 'SWE1-HVAC-098']

WITHHELD = [
 ("SWE1-HVAC-083", "`14.1`（HVACP1.）「HVAC pop-ups should **follow the pop-up list**」—— 委派對象為 **HMI Pop Up List**，一份**外部文件**且**從未入 `inputs/`**（`DATA_REQUESTS` #11，`paths.popup_list` 為 null）。依 profile §5.3 之判別次序屬 `[BLOCKED-SPEC]`，而該 marker 之白名單增列須經裁定（**R-C26**：豁免不可自取），故停下回報，形態同 `080-02`／`081-02`。**本 leaf 另帶 3 個圖片標記**（A-CF23）"),
 ("SWE1-HVAC-099", "`14.15`（HVACSB1）「Available comfort controls … **depend on vehicle configuration**」—— **陳述有對照關係而不給對照**，形態同 `DATA_REQUESTS` #32 之三個成員，本輪併入該類為第四個成員。**注意**：本節雖停下，其句子仍**被引為第十六軸之出處**（14.16～14.18 之 PC）—— 一個 leaf 停下，不代表該節之句子不可作為他條之出處（R-C29）"),
]



def add_lines(pre_conditions: str, *lines: str) -> str:
    n = len([l for l in pre_conditions.split("\n") if l.strip()])
    out = pre_conditions
    for line in lines:
        n += 1
        out = f"{out}\n{n}. {line}"
    return out


def _iar() -> dict:
    with (FEATURE / "data" / "interface_axis_review.tsv").open(encoding="utf-8") as fh:
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
    parents = {"14.1.1": "SWE1-HVAC-084", "14.2": "SWE1-HVAC-085",
               "14.3": "SWE1-HVAC-086", "14.4": "SWE1-HVAC-087",
               "14.5": "SWE1-HVAC-088", "14.6": "SWE1-HVAC-089",
               "14.7": "SWE1-HVAC-090", "14.8": "SWE1-HVAC-091",
               "14.9": "SWE1-HVAC-092", "14.10": "SWE1-HVAC-093",
               "14.10.1": "SWE1-HVAC-094", "14.11": "SWE1-HVAC-095",
               "14.13": "SWE1-HVAC-097", "14.16": "SWE1-HVAC-100",
               "14.16.1": "SWE1-HVAC-101", "14.17": "SWE1-HVAC-102",
               "14.18": "SWE1-HVAC-103", "14.19": "SWE1-HVAC-104",
               "15.1": "SWE1-HVAC-105"}

    for o in ["14.1.1", "14.2", "14.3", "14.4", "14.5", "14.6",
              "14.7", "14.8", "14.9", "14.10", "14.10.1", "14.11",
              "14.13", "14.16", "14.16.1", "14.17", "14.18",
              "14.19", "15.1"]:
        tcs = []
        for (leaf, title, item, proc, er, prio, dm,
             ch16, verdict, sentence) in table[o]:
            n += 1
            base_pc, extra_ref = LEAF_PC.get(leaf, SECTION_PC[o])
            refs = [o] + list(extra_ref)
            pcs = [base_pc]
            if leaf in LEAF_EXTRA:
                line, more = LEAF_EXTRA[leaf]
                pcs.append(line)
                refs += list(more)
            pc = "\n".join(pcs)
            pc = add_lines(pc, EX_ICS, EX_EMEA, EX_LOWER)
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
            "parent": parents[o], "outline": o, "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o],
            "keywords": [], "duplicate_of": "",
            "distinguishing_axis": DIST_AXIS.get(
                o, {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [], "interface_axis_review": iar[o], "tcs": tcs,
        }
        (OUT / f"{parents[o]}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{parents[o]}  {o:8} {len(tcs)} TC")

    leaves = total
    print(f"\n{leaves} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print("\nWITHHELD — stop-and-report, no row produced:")
    for req, why in WITHHELD:
        print(f"- {req}: {why}")
    held = len(WITHHELD)
    moved = len(MOVED_TO_BATCH16)
    print(f"\n{leaves} emitted + {held} withheld + {moved} moved to "
          f"batch 16 (R-C42) = {leaves + held + moved} leaves "
          f"declared for {TEST_SET} (framework.md: 42)")
    if leaves + held + moved != 42 or total != 36:
        raise SystemExit(
            f"expected 42 leaves declared / 36 TCs, got "
            f"{leaves + held + moved} / {total}")


if __name__ == "__main__":
    main()
