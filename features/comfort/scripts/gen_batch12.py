#!/usr/bin/env python3
"""Batch 12 generator — ICS Climate Modes (handoff 57 §1).

Scope from framework.md §12's table, derived not retyped (48 §2):

    16.3  9 | 16.4  1 | 16.5  2 | 16.10  8 | 16.11  4 | 16.13  12  = 36 leaves

037 measured independently: 107(9) + 108(1) + 109(2) + 115(8) + 116(4)
+ 119(12) = 36. Nothing withheld.

Emitted: 34 TCs, -203 … -236.
WITHHELD: 2 leaves — 16.11's -03/-04, withdrawn under R-C40 (58 §1) after
they were generated in the previous round. Their ch2 twins (2.11's 015-04 /
015-05) were stopped in batch 9, and the two clauses are verbatim identical,
so the stop had to move with the clause rather than with the chapter.

  !! This is the FIRST time tc_ids have MOVED. Withdrawing two TCs from the
  !! middle of the batch renumbers 16.13's twelve from -227..-238 to
  !! -225..-236, because `tc-id-sequence` requires 1..N gap-free and a
  !! withdrawal cannot leave a hole. R-C7 freezes the scheme, not the
  !! assignment, and nothing here is delivered — but "an identifier that
  !! moves is not an identifier" (41 §1.2) cuts against it. Raised in
  !! 上繳 39 §2.3 rather than settled here.

ch16 side again, so the three inversions hold: positive EMEA axis value, the
mirror map read in REVERSE, axis 13 cited from ch2. What is different here is
that the ch2 counterpart (`Climate Modes`, batch 9) is already generated, so
57 §1 is right that R-C36-1 could be checked TC-against-TC — except that the
check runs the OTHER way on this side. ch16 TCs carry no EMEA exclusion, so
they have no `emea_ics_review` to answer; the pointers that get confirmed are
the ch2 ones, and that confirmation happens in the provisional re-confirmation
(上繳 38 §6.4), not here.

Reverse reading of ch16_mirror_map.tsv — what ch2 has that ch16 does NOT, so
that it is not imported (§8.2.1):

  16.3 <-> 2.3   mirrored, but ICE2 and C2 DISAGREE in two places, already
                 measured in batch 9 (-130 / -131 got `no` for exactly this):
                   * C2 excludes the four airflow modes and front defrost;
                     ICE2 excludes MAX A/C and MAX DEF
                   * C2: "Auto can change the state of AC, but do not show
                     this change"; ICE2: "In Auto the A/C button is
                     highlighted" — opposite readings
                 -207 and -210 verify ICE2's version. C2's is NOT imported.
  16.4 <-> 2.4/2.5/2.8/2.9/2.13  partial x5: ICE3 is ONE sentence bundling
                 five controls' on/off. 037 gave it ONE leaf, so it gets ONE
                 TC covering the five — not five TCs (§8.2.2)
  16.10 <-> 2.10 mirrored, and ICE9 adds two sentences C11 lacks (the
                 recirculation LED while climate is off) -> -217 is ch16-only
  16.13 <-> 2.13 mirrored at section level, but ICE12 ENUMERATES what C14
                 delegates to the VF HVAC document. 2.13's -02/-03 stopped in
                 batch 9 for that delegation; here the same behaviour IS
                 specified, so it generates. The two are not siblings and the
                 asymmetry is the point — see 上繳 38 §6.3

Usage:
    python3 features/comfort/scripts/gen_batch12.py
"""

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from external_docs import append_external   # 81 §2 — R-C45 解封
from test_item import apply_test_item   # Pei 2026-08-17 —— 上半照抄條文、下半情境
from splits import apply_splits   # 76 §2 — 依 75 §1（今併入 R-C44 第一問）之列舉判準拆分

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "ICS Climate Modes"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 203

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
# profile §3.3 — the string must match 下拉選單!A1:A9 character for
# character. `, BVA` is part of the workbook's own entry; dropping it
# was caught by the design-method gate on the first run.
DM_BVA = "邊界值分析 (Boundary Value Analysis, BVA)"

PC_EMEA = ("1. [spec-derived] The vehicle is an EMEA ICS vehicle, whose climate "
           "interface is specified in chapter 16 (16.2)")
EX_ICS = ("[spec-derived] The vehicle does not have 3 knob HVAC controls "
          "with ICS, for which no HVAC screens or pop ups are displayed "
          "(2.14)")
EX_LOWER = ("[spec-derived] The vehicle is not configured with a non-foldable "
            "secondary lower screen containing comfort information, for which "
            "the comfort section is removed from the head unit (6.3)")
PC_MULTIZONE = ("[spec-derived] The vehicle is not a single zone climate "
                "configuration, for which Sync is not shown (16.11)")

# Axis 9 — exposed where the observable lives in the head unit's comfort
# section; NOT exposed where it is a comfort pop-up (6.3's own exception).
# Axis 9 — every observable here is on the head unit's climate screen, the
# status bar or the main category control, all inside the comfort section 6.3
# removes. Exposed throughout (unlike batch 11, whose observables were pop-ups
# that 6.3 explicitly excepts).
LOWER_EXPOSED = None       # None = every TC in this batch
# Axis 2 — the SYNC-dependent leaves. 16.11 is the SYNC section, and 16.13's
# -06 turns Sync on as part of MAX A/C.
MULTIZONE_EXPOSED = {"SWE1-HVAC-116-01", "SWE1-HVAC-116-02",
                     "SWE1-HVAC-116-03", "SWE1-HVAC-116-04",
                     "SWE1-HVAC-119-06"}
# Axis 1 — 16.3's -09 is the MTC value; the rest of 16.3 needs ATC, since
# ICE2's own last line is "(AUTO is not shown in MTC configurations)".
PC_ATC = ("[spec-derived] The vehicle has an ATC climate system, in which "
          "AUTO is shown (16.3)")
PC_MTC = "[spec-derived] The vehicle is in an MTC configuration (16.3)"
ATC_LEAVES = {f"SWE1-HVAC-107-0{n}" for n in range(1, 9)}
# Axis 4 — 16.13 is the MAX A/C section and 16.3's -05/-06 press it.
PC_MAXAC = ("[spec-derived] The system supports Max A/C, which is then "
            "displayed on the screen next to the A/C button (16.13)")
MAXAC_LEAVES = {f"SWE1-HVAC-119-{n:02d}" for n in range(1, 13)} | {
    "SWE1-HVAC-107-05", "SWE1-HVAC-107-06", "SWE1-HVAC-108"}
# Axis 5 — MAX DEF is pressed or read by these.
PC_MAXDEF = "[spec-derived] The vehicle is equipped with MAX DEF (3.2)"
MAXDEF_LEAVES = {"SWE1-HVAC-107-05", "SWE1-HVAC-107-06", "SWE1-HVAC-108",
                 "SWE1-HVAC-115-02", "SWE1-HVAC-119-12"}
# Axis 10 — REAR DEFROST is pressed or read by these.
PC_REARDEF = ("[spec-derived] The vehicle is equipped with rear defrost, "
              "which is absent on some soft top vehicles (3.4)")
REARDEF_LEAVES = {"SWE1-HVAC-108", "SWE1-HVAC-115-02", "SWE1-HVAC-115-05"}
# Axis 16 — 115-05 turns a heated seat on.
PC_COMFORT = ("[spec-derived] The vehicle is equipped with Comfort features, "
              "such as heated/vented seats and a heated steering wheel (17.3)")
COMFORT_LEAVES = {"SWE1-HVAC-115-05"}

EXTRA_PC = [(ATC_LEAVES, PC_ATC, ("16.3",)),
            (MAXAC_LEAVES, PC_MAXAC, ("16.13",)),
            (MAXDEF_LEAVES, PC_MAXDEF, ("3.2",)),
            (REARDEF_LEAVES, PC_REARDEF, ("3.4",)),
            (MULTIZONE_EXPOSED, PC_MULTIZONE, ("16.11",)),
            (COMFORT_LEAVES, PC_COMFORT, ("17.3",))]

WITHHELD = []   # 81 §2.1 — 兩條依 R-C45 解封，見 external_docs.py
# 其列不由本表產出，而由 external_docs 以**後號**追加 —— 自表中產出會使
# 本批其後之 tc_id 各進二，與 batch13 之 START_N 相撞（65 §1：既有列不重編號）。
SKIP_TABLE = {"SWE1-HVAC-116-03", "SWE1-HVAC-116-04"}
# 撤下之原因（58 §1，R-C40）不改：ICE10 與 C12 逐字相同，兩側同進退。
# 今日兩側**同時**解封，該對稱因此維持 —— 解封之依據是 CFTS043 之
# `$Rear_HVAC_cfg$ = [Present]`，它對 ch2 與 ch16 一樣成立。


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

REASONING = {
"16.3": "驗證目標：16.3（ICE2）以九句定出 ICS 介面之 AUTO 狀態呈現、其作用對象、互斥對象、中斷條件與 MTC 例外，九個 037 leaf 逐句對應，一葉一 TC（§8.2.1）。關鍵情境條件：EMEA 軸取**正向值**（16.2）；第一軸 —— `107-01`～`107-08` 取 ATC 值（ICE2 末句「AUTO is not shown in MTC configurations」蘊含之），`107-09` 取 MTC 值；`107-05`／`107-06` 另補第四軸（MAX A/C，出處 16.13）與第五軸（MAX DEF，出處 3.2）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，第十二軸不補（ch16 無 tab 條文）。為什麼這樣切：`107-05`（互斥）與 `107-06`（按下即前往該功能）為同一組關係之兩個方向，可各自獨立失效。刻意略過：**鏡射表反向使用之關鍵結果 —— ICE2 與 C2 在兩處相左，本批驗 ICE2 之版本而不移植 C2**：(一) C2 之互斥對象為四氣流模式與 front defrost，ICE2 為 MAX A/C 與 MAX DEF；(二) C2 云「Auto can change the state of AC, **but do not show this change**」，ICE2 云「**In Auto the A/C button is highlighted**」—— 語意相反。批次 9 之 `003-04`／`003-05` 已因此得 `no`，此處為其另一側之實作（§8.2.1）。",
"16.4": "驗證目標：16.4（ICE3）以**一句**定出五個控制之 on/off 狀態，037 亦只給**一個** leaf，故產一條而非五條（§8.2.2：TC 作者不得拆 037 之單位）。關鍵情境條件：EMEA 軸取正向值；本條同時觸及 MAX A/C（第四軸，16.13）、MAX DEF（第五軸，3.2）與 REAR DEFROST（第十軸，3.4），三者之 PC 皆補並併入 spec_ref（R-C29）；依 **R-C34** 第九軸與第十三軸暴露 → 補。為什麼這樣切：五者之 on/off 為同一句所述之同一性質，其失效形態相同（某鍵不切換），故一條以五組步驟涵蓋。刻意略過：**鏡射表記 16.4 對 2.4／2.5／2.8／2.9／2.13 五個 partial** —— 其分界欄明載 ICE3 只涵蓋各者之 on/off 而不涵蓋任何連動，故本條之 ER 亦只驗 on/off，不驗任何連動（§8.2.1）。",
"16.5": "驗證目標：16.5（ICE4）定出 recirc 圖示依車型顯示與偵測不到車型時之通用符號，兩個 037 leaf 對應之。關鍵情境條件：EMEA 軸取正向值；依 **R-C34** 第九軸與第十三軸暴露 → 補。為什麼這樣切：兩者為同一規則之兩個分支（偵測得到／偵測不到），依 §7 各自成條。刻意略過：**本節與 `2.5` 之 `006-04`（已停下）同屬「對照關係未定義」** —— ICE4 云「as displayed in **the Climate Main page table**」，比 C4 之「the table」具體，**仍未給對照**；故 `109-01` 之 ER 只驗「圖示為該車型之圖示」而**不指名任何具體圖示**（§8.4.1），其可判性依賴受測車型之已知圖示，該限制已於 `DATA_REQUESTS` #32 具名。",
"16.10": "驗證目標：16.10（ICE9）以八句定出 ICS 介面之 climate off 呈現、按鈕灰化例外、狀態列破折號、各類硬鍵之回復行為，以及 recirculation LED 之特例，八個 037 leaf 逐句對應。關鍵情境條件：EMEA 軸取正向值；`115-01`（灰化例外）另補第五軸與第十軸，`115-04`（座椅／方向盤動作）另補第十六軸（Comfort Features，出處 17.3）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補。為什麼這樣切：`115-04`（不回復）與 `115-05`（回復）為同一組規則之兩側，其失效可獨立發生。刻意略過：**`115-06` 之 recirculation LED 特例為 ch16 獨有** —— 鏡射表記 `16.10 ↔ 2.10` 為 `mirrored` 而註明「ICE9 另加 recirculation LED 兩句」，C11 無之，故該條**不對應任何 ch2 之 TC**，亦不得反向移植至 ch2（§8.2.1）。",
"16.11": "驗證目標：16.11（ICE10）定出 SYNC 之溫度連動、中斷條件、對前後排之作用，以及後排調整之中斷，四個 037 leaf 對應之。關鍵情境條件：EMEA 軸取正向值；**第二軸**（非單區，出處 16.11 自身之「Sync is not shown for single zone climate configurations」）四條全補；依 **R-C34** 第九軸與第十三軸暴露 → 補。為什麼這樣切：`116-01`（連動）與 `116-02`（中斷）為相反方向；`116-03`（前後排）與 `116-04`（後排中斷）之干擾源不同。刻意略過：**`116-03`／`116-04` 之可觀察量在後排** —— 批次 9 曾因「車輛是否配備後排氣候不在既有軸內」而停下 `2.11` 之對應二 leaf（`015-04`／`015-05`）。**本批不停** ，因 ICE10 之句子與 C12 逐字相同而 037 對 ch16 側**產出了 leaf**，且其可觀察量之存在由 `16.11` 自身之句子承載；**此不對稱已於上繳 38 §6.2 具名待裁**。",
"16.13": "驗證目標：16.13（ICE12）以十二句定出 MAX A/C 之顯示條件、其對六項氣候參數之設定，以及五種退出途徑之各自落點，十二個 037 leaf 逐句對應（§8.2.1）。關鍵情境條件：EMEA 軸取正向值；**第四軸**（MAX A/C 支援，出處 16.13 首句「If the system supports Max A/C」）十二條全補；`119-12` 另補第五軸（MAX DEF）；`119-06`（Sync）另補第二軸；依 **R-C34** 第九軸與第十三軸暴露 → 全數補。為什麼這樣切：六項參數設定各自成條（`116-04`～`119-06`），因任一項之失效可獨立發生且可獨立定位；五種退出途徑（風速／溫度等／A-C／AUTO／MAX DEF）之落點各異，亦各自成條。刻意略過：**本節與 `2.13`（C14）之關係值得記** —— 鏡射表記其為 `mirrored`，惟 **C14 把 On/Off 邏輯委派予 VF HVAC 文件而 ICE12 逐項列出**；批次 9 之 `019-02`／`019-03` 正因該委派而停下，本批同一行為**因 ch16 有明文而得以生成**。**不得反向以 ICE12 補 `2.13`**（§8.2.1 跨介面移植），該不對稱見上繳 38 §6.3。"
}

TCTABLE = Path("/tmp/b12tcs.json")
# 58 §3 — 16.13's six exit paths overlap, and the overlap is §4.6 (sibling),
# NOT §4.5. §4.5 governs which FIELD data belongs in inside ONE TC; six exit
# paths are six TCs, so they are outside its range entirely. This is the
# SECOND correction of that shape (50 §4 was the first, on 17.1's three), so
# the boundary now lives in RUNBOOK.md as well.
#
# §10.6 strict equivalence, per pair — the TRIGGER differs in every one, and
# for two of them the OUTCOME differs as well:
# The ids below are the POST-WITHDRAWAL ones (58 §2 removed -224/-225, so
# every 16.13 id moved down by two — the first time tc_ids have moved).
#   -231  fan speed change   -> MAX A/C off, rest of the state KEPT
#   -232  temp/recirc/mode   -> MAX A/C off, previous mode except that element
#   -233  MAX A/C pressed    -> MAX A/C off, previous manual mode
#   -234  press A/C          -> MAX A/C off, previous mode, A/C OFF
#   -235  press AUTO         -> MAX A/C off, system in AUTO
#   -236  press MAX DEF      -> MAX A/C off, system in MAX DEF
# duplicate_of therefore does NOT apply to any pair. Written out rather than
# waved through as "obviously different" (58 §3).
DIST_AXIS = {
    "16.13": {
        "axis": "MAX A/C 之退出途徑（trigger）與其落點（outcome）",
        "delta": "六條之 trigger 各異且其 outcome 亦不全同 —— "
                 "`119-07` 改風速 → MAX A/C 解除而**其餘狀態維持**；"
                 "`119-08` 改溫度／recirc／模式 → 回前一手動模式"
                 "**除該被改之元素外**；`119-09` 按 MAX A/C → 回前一手動模式；"
                 "`119-10` 按 A/C → 回前一手動模式且 **A/C 關閉**；"
                 "`119-11` 按 AUTO → 系統**進入 AUTO**；"
                 "`119-12` 按 MAX DEF → 系統**進入 MAX DEF**。"
                 "**（本串號為撤下 `116-03`／`116-04` 後之號，見 58 §2；"
                 "profile §5.5 之推導欄重算風險於此首次實現）**"
                 "**§10.6 四項（trigger／outcome／input／verification target）"
                 "中 trigger 於六條全異，outcome 於其中四條亦異，"
                 "故無一對構成 `duplicate_of`。** 其重疊屬 §4.6 之 sibling "
                 "重疊而非 §4.5 之欄位歸屬 —— 六條 TC 不在 §4.5 之射程內",
    },
}

PARENTS = {"16.3": "SWE1-HVAC-107", "16.4": "SWE1-HVAC-108",
           "16.5": "SWE1-HVAC-109", "16.10": "SWE1-HVAC-115",
           "16.11": "SWE1-HVAC-116", "16.13": "SWE1-HVAC-119"}
KEYWORDS = {"16.3": ["AUTO", "ICS", "mutually exclusive"],
            "16.4": ["on/off state", "MAX A/C", "RECIRC"],
            "16.5": ["recirc icon", "vehicle model"],
            "16.10": ["climate off", "status bar", "recirculation LED"],
            "16.11": ["SYNC", "driver", "passenger"],
            "16.13": ["MAX A/C", "Face", "LO", "Sync"]}


def ref(*outlines) -> str:

    return "; ".join(f"{STEM}_{o}" for o in dict.fromkeys(outlines))


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    table = json.loads(TCTABLE.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    n = START_N - 1
    total = 0
    emitted_leaves = set()   # 76 §2 — 拆分後 TC 數 ≠ leaf 數，故以身分計數（R-C43）

    for o in ["16.3", "16.4", "16.5", "16.10", "16.11", "16.13"]:
        tcs = []
        for leaf, title, item, proc, er, prio, dm in table[o]:
            if f"SWE1-HVAC-{leaf}" in ({w for w, _ in WITHHELD} | SKIP_TABLE):
                continue
            n += 1
            req = f"SWE1-HVAC-{leaf}"
            extra, refs = [], [o, "16.2"]
            if req in ATC_LEAVES:
                extra.append(PC_ATC)
            elif req == "SWE1-HVAC-107-09":
                extra.append(PC_MTC)
            for leaves, line, more in EXTRA_PC:
                if leaves is ATC_LEAVES or req not in leaves:
                    continue
                extra.append(line)
                refs += list(more)
            # Axis 13 and axis 9: every observable in this batch is on the
            # head unit's climate screen / status bar / category control.
            extra.append(EX_ICS)
            refs.append("2.14")
            extra.append(EX_LOWER)
            refs.append("6.3")
            tcs.append({
                "req_id": req,
                "tc_id": TC_ID_FMT.format(n=n),
                "tc_title": title,
                "test_group": TEST_GROUP,
                "test_set": TEST_SET,
                "test_item": item,
                "pre_conditions": add_lines(PC_EMEA, *extra),
                "input_test_data": "NA",
                "test_procedure": "\n".join(proc),
                "expected_result": "\n".join(er),
                "specification_reference": ref(*refs),
                "priority": prio,
                "design_method": DM_FUNC if dm == "F" else DM_STATE,
                "split_flag": False,
                "split_reason": "",
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
            })
        if o == "16.11":
            from external_docs import PC_REAR_HVAC
            pc = add_lines(PC_EMEA, PC_MULTIZONE, PC_REAR_HVAC,
                           EX_ICS, EX_LOWER)
            refs = [o, "16.2", "2.14", "6.3"]
            leaves = sorted(SKIP_TABLE)
            tcs = append_external(tcs, PARENTS[o], {r: pc for r in leaves},
                                  {}, {r: refs for r in leaves})
        doc = {
            "parent": PARENTS[o], "outline": o, "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o], "keywords": KEYWORDS[o],
            "duplicate_of": "",
            "distinguishing_axis": DIST_AXIS.get(
                o, {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [],
            "interface_axis_review": INTERFACE_AXIS_REVIEW[o], "tcs": apply_test_item(apply_splits(tcs)),
        }
        (OUT / f"{PARENTS[o]}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        emitted_leaves.update(t["req_id"] for t in tcs)
        print(f"{PARENTS[o]}  {o:8} {len(tcs)} TC")

    leaves = len(emitted_leaves)
    print(f"\n{leaves} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print(f"{leaves} emitted + {len(WITHHELD)} withheld = "
          f"{leaves + len(WITHHELD)} leaves declared for {TEST_SET} "
          f"(framework.md: 36)")
    if leaves + len(WITHHELD) != 36 or leaves != 36:
        raise SystemExit(f"expected 36 / 36, got {leaves + len(WITHHELD)} / {leaves}")


if __name__ == "__main__":
    main()
