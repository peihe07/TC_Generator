#!/usr/bin/env python3
"""Batch 9 generator — Climate Modes (handoff 51 §2).

Scope from framework.md line 40 / its §2 table, derived not retyped (48 §2):

    2.3  9 | 2.3.1  2 | 2.4  4 | 2.5  4 | 2.5.1  2 | 2.10  6 | 2.11  5
    | 2.13  3        = 35 leaves

037 measured independently: 003(9) + 004(2) + 005(4) + 006(4) + 007(2)
+ 014(6) + 015(5) + 019(3) = 35.

Emitted: 26 TCs, -127 … -152.
WITHHELD: 9 leaves, each named with the axis or delegation that stops it —
see WITHHELD below. Four distinct causes, none of them new:

    2.3.1 x2   dual airflow modes axis      -> DR #38
    2.5-04     configuration -> icon table  -> DR #32 (class)
    2.5.1 x2   recirc control form varies   -> DR #37
    2.11 x2    rear climate presence axis   -> DR #17
    2.13 x2    VF HVAC external delegation  -> [BLOCKED-SPEC] whitelist (R-C26)

This is the ch2 side, so the habits are the ch2 ones again (EMEA exclusion,
not the positive value). R-C36-1 applies per TC and this batch is where it
bites hardest: 51 §2 flagged that ch16_mirror_map records most of these
sections as `partial`, and the boundary column earns its keep — SIX of the
26 TCs get a `no` verdict, each pointing at the boundary that excludes it.
Two of those six are not "ch16 is silent" but "**ch16 says the opposite**"
(-131 and -138); recorded as such rather than flattened into "no counterpart".

Usage:
    python3 features/comfort/scripts/gen_batch9.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"
TCTABLE = Path("/tmp/b9tcs.json")

TEST_GROUP = "Comfort"
TEST_SET = "Climate Modes"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 127

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
PC_ATC = ("1. [spec-derived] The vehicle has an ATC climate system, in which "
          "AUTO is shown (2.3)")
PC_MTC = "1. [spec-verbatim] The vehicle is in an MTC configuration (2.3)"
PC_PLAIN = "1. [test-setup] The climate screen is open and the climate system is on"
PC_MULTIZONE = ("1. [spec-derived] The vehicle is not a single zone climate "
                "configuration, for which Sync is not shown (2.11)")
PC_MAXAC = ("1. [spec-derived] The vehicle has MAX A/C functionality, whose "
            "presence the CCM relays (2.13)")
PC_DEFROST = ("2. [spec-derived] The vehicle is equipped with MAX DEF (3.2) "
              "and with rear defrost, which is absent on some soft top "
              "vehicles (3.4)")

# Per-section starting pre_condition and the extra spec_ref sections it cites.
SECTION_PC = {
    "2.3": (PC_ATC, ()), "2.4": (PC_PLAIN, ()), "2.5": (PC_PLAIN, ()),
    "2.10": (PC_PLAIN, ()), "2.11": (PC_MULTIZONE, ()),
    "2.13": (PC_MAXAC, ()),
}
LEAF_PC = {"003-09": (PC_MTC, ())}
LEAF_EXTRA = {"014-02": (PC_DEFROST, ("3.2", "3.4"))}

REASONING = {
"2.3": "驗證目標：2.3（C2）以九句定出 AUTO 之狀態呈現、其對風速／模式／A-C 之作用、互斥對象、中斷條件與中斷後之落點，以及 MTC 之例外，九個 037 leaf 逐句對應，一葉一 TC（§8.2.1）。關鍵情境條件：第一軸（ATC／MTC）—— `003-01`～`003-08` 取 ATC 值（C2 末句「AUTO is not shown in MTC configurations」蘊含 AUTO 之存在以 ATC 為前提），`003-09` 取 MTC 值，出處皆 2.3；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答（R-C36-1），第十二軸不補。為什麼這樣切：九者之失效互相獨立，且中斷條件（`003-06`）與中斷後落點（`003-07`）分屬兩個失效面 —— 前者「有沒有斷」，後者「斷了以後去哪」。刻意略過：**C2 之「the manual mode that most closely matches the auto mode exited」無可判之對照** —— 條文未給 auto 模式與手動模式之對應表，故 `003-07` 只驗其確定之另一半（按下特定模式鍵即進該模式），「最接近」之一半不寫入 ER（§8.4.1 禁造值），該缺口於 reasoning 具名而不吸收（§8.4.2）。",
"2.4": "驗證目標：2.4（C3）定出 A/C 之 on/off 狀態與其與 Auto／Defrost／Recirc 之四項連動，四個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：本節無配置條件，起始 PC 為 test-setup；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答，第十二軸不補。為什麼這樣切：`005-02`（Auto 自動開 A/C）與 `005-03`（A/C 中斷 Auto）為相反方向之兩條連動，可各自獨立失效。刻意略過：`005-04` 之 ER 以「A/C 按鈕狀態不變」驗「do not show this change」—— 條文所述之隱藏對象為**畫面上之呈現**，非 A/C 之實際開關，故 ER 停在按鈕而不宣稱壓縮機狀態（§6 可觀察性）。**R-C36-1 之逐條答本節四條有三條為 `no`**：ICE3 只述五者之 on/off 而不述任何連動，鏡射表之分界欄已明載。",
"2.5": "驗證目標：2.5（C4）定出 RECIRC 之 on/off 狀態、不可用時之灰化、可自動開啟 A/C，以及車型專屬圖示，四個 037 leaf 對應之，本輪產三條。關鍵情境條件：本節無配置條件，起始 PC 為 test-setup；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答，第十二軸不補。為什麼這樣切：`006-02` 之灰化以 CCM 之可用性狀態為觸發，其失效與 `006-01` 之 on/off 無關。刻意略過：**`006-04`（車型專屬 recirc 圖示）停下不產列** —— C4 之「as displayed in **the table**」未指名任何節次，全 129 節亦無該對照表之內容；此與 `16.16` 之座椅 off icon **同型**，併入 `DATA_REQUESTS` #32 之「configuration → icon 對照未定義」類。**16.5（ICE4）逐字重述該句且把表之位置寫成 `Climate Main page table`，仍未給對照** —— 故非 ch16 有而 ch2 無，是兩側皆無。",
"2.10": "驗證目標：2.10（C11）定出 climate off 之畫面、按鈕灰化之例外、category button 與 status bar 之呈現，以及以 temp/fan 控制回復之行為，六個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：`014-02` 另補第五軸（MAX DEF 有無，出處 3.2）與第十軸（REAR DEFROST 有無，出處 3.4）—— 該條之 ER 以該二鍵**不灰化**為觀察對象，其不存在即使該觀察無對象；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答，第十二軸不補。為什麼這樣切：`014-05`（回復至上次等級）與 `014-06`（持續按住持續變化）為同一操作之兩個階段，其失效可獨立發生（回復了但停在最低／回復正確但不續動）。刻意略過：C11 之「Climate off affects every climate function with the exception of…」為總述句，037 未另給 leaf，故不另立 TC；其可觀察內容已由 `014-02` 之灰化例外涵蓋（§4.5：同一可觀察量不得由兩個 leaf 共用）。",
"2.11": "驗證目標：2.11（C12）定出 SYNC 之狀態呈現與其雙側溫度連動、中斷條件，以及其對前後排之作用，五個 037 leaf 對應之，本輪產三條。關鍵情境條件：第二軸（單區／雙區／四區）—— C12 明文「Sync is not shown for single zone climate configurations」，故起始 PC 即取該軸之非單區值，出處 2.11；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答，第十二軸不補。為什麼這樣切：`015-02`（連動）與 `015-03`（中斷）為 SYNC 之兩個相反方向。刻意略過：**`015-04`／`015-05` 停下不產列** —— 兩者之可觀察量皆在**後排**（「alter the Front and Rear passengers」「rear fan speed, mode, or temp」），而「車輛是否配備後排氣候」**不在 profile §3.2 之十六軸內**，其來源即 `2.1` 之 tab 集合問題（`DATA_REQUESTS` #17，未解）。**本節與已生成之 `2.6.1` 重疊之判定**：C5.1 與 C12 皆述 SYNC 之溫度連動與中斷，`pending_sibling.tsv` 已記 `2.6.1 ↔ 2.11` 為 `sibling`，兩側今皆有 TC，其 `duplicate_of` 判定見上繳 35 §8.4。",
"2.13": "驗證目標：2.13（C14）定出 MAX A/C 之畫面採用時機、on/off 狀態呈現，以及其對多項氣候參數之修改與 On/Off 邏輯之委派，三個 037 leaf 對應之，本輪產一條。關鍵情境條件：第四軸（MAX A/C 有無）—— C14 首句「MAX A/C screens/popups are to be used when CCM relays presence of MAX A/C functionality」為明文配置條件，故起始 PC 取該軸之有值，出處 2.13；依 **R-C34** 第九軸與第十三軸暴露 → 補，EMEA 排除補並逐條答，第十二軸不補。為什麼這樣切：`019-01` 之可觀察量為按鈕高亮，與被委派之參數修改邏輯無關，故可獨立成條。刻意略過：**`019-02`／`019-03` 停下不產列** —— C14 之「On/Off logic should follow requirements from **VF HVAC document**」為**對外部文件之明文委派**，依 profile §5.3 之判別次序屬 `[BLOCKED-SPEC]`，而該 marker 之白名單增列須經裁定（**R-C26**：豁免不可自取），故停下回報，形態與 `080-02`／`081-02` 相同。**不以 16.13（ICE12）之逐項列舉補之** —— 那是另一套介面之條文，援引即跨介面移植（§8.2.1）。",
}

# 51 §2.1 / §4.6 — `2.10 ↔ 3.3` is recorded `sibling` and 3.3 is already
# generated, so this doc owes the backfill. §10.6 strict equivalence:
#   3.3 (-030) trigger: climate off, read MAX DEF / REAR DEF availability
#              target : that the two remain AVAILABLE
#   2.10 (-144) trigger: climate off, read the buttons
#              target : that the OTHER buttons are greyed and these two are not
# Same fact seen from the two sides of the exception. The verification targets
# differ (availability of the two vs greying of the rest), so duplicate_of does
# NOT apply — but the overlap is real and is named here rather than left to be
# rediscovered.
DIST_AXIS = {
    "2.3": {
        "axis": "所控之氣候區（前排 vs 後排）—— 同一行為在兩區之兩處陳述",
        "delta": "`2.3` 之主體為**前排**AUTO（其狀態、15h 指示、與氣流模式之互斥、中斷條件），`7.2` 之主體為**後排**同一AUTO（其狀態、15h 指示、與氣流模式之互斥、中斷條件）（鏡射表記其為 partial／mirrored）。**§10.6 逐項**：trigger 之操作對象不同（前排控制 vs 後排控制）、outcome 之可觀察量不同（前排風速／模式 vs 後排風速／模式）、input 皆 NA、verification target 各為該區之行為。**四項中兩項相異 → 非嚴格等價，`duplicate_of` 不填。** 與 `2.9`↔`16.9` 之四對逐字等價不同：**該對之兩側互斥**（同一車不可能既 ICS 又非 ICS），**本對之兩側並存**（一台四區車同時有前排與後排），故兩條 TC 於同一車上皆須執行",
    },
    "2.10": {
        "axis": "which side of the climate-off exception the section owns "
                "(2.10 vs 3.3)",
        "delta": "`2.10`（C11）自**通則**一側陳述：climate off 時其餘按鈕灰化，"
                 "而 Front/Max defrost 與 rear defrost 為例外；`3.3`（C21）自**例外**"
                 "一側陳述：MAX DEF 與 REAR DEF 於 climate off 期間可用。"
                 "`014-02` 之 verification target 為「其餘按鈕變灰」，`025-02` 之 target "
                 "為「該二者仍可用」—— 四項嚴格等價中 verification target 相異，"
                 "故不構成 `duplicate_of`；惟兩者共用同一條文事實，記此以免重複驗證",
    },
}

# 64 §1 — these leaves were withheld here and are now generated by
# gen_batch16.py under R-C42 (the clause carries its own condition).
# They stay in this file's arithmetic so the Test Set's leaf count
# still adds up to framework.md's figure — a leaf that moved must
# not look like a leaf that vanished.
MOVED_TO_BATCH16 = ['SWE1-HVAC-004-01', 'SWE1-HVAC-004-02', 'SWE1-HVAC-007-01', 'SWE1-HVAC-007-02']

WITHHELD = [
 ("SWE1-HVAC-006-04", "「The recirc icon will display the vehicle model specific icon **as displayed in the table**」—— **未指名任何節次**，全 129 節無該對照表之內容；與 `16.16` 之座椅 off icon 同型，併入 `DATA_REQUESTS` #32 之「configuration → icon 對照未定義」類。**16.5（ICE4）逐字重述且把表寫成 `Climate Main page table`，仍未給對照** —— 兩側皆無"),
 ("SWE1-HVAC-015-04", "「Adjusting Fan speed and Mode will alter the **Front and Rear** passengers」—— 可觀察量在後排，而「車輛是否配備後排氣候」**不在十六軸內**；其來源即 `2.1` 之 tab 集合問題（`DATA_REQUESTS` #17，未解）"),
 ("SWE1-HVAC-015-05", "「If the **rear** fan speed, mode, or temp are adjust … will break SYNC」—— 同 `015-04`"),
 ("SWE1-HVAC-019-02", "「MAX A/C modifies multiple climate parameters」—— C14 未列出任何一項參數，其內容由次句委派予 **VF HVAC document**（外部文件）；依 profile §5.3 屬 `[BLOCKED-SPEC]`，白名單增列須經裁定（**R-C26**）"),
 ("SWE1-HVAC-019-03", "「On/Off logic should follow requirements from **VF HVAC document**」—— 同 `019-02`，明文外部委派"),
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
    parents = {"2.3": "SWE1-HVAC-003", "2.4": "SWE1-HVAC-005",
               "2.5": "SWE1-HVAC-006", "2.10": "SWE1-HVAC-014",
               "2.11": "SWE1-HVAC-015", "2.13": "SWE1-HVAC-019"}

    for o in ["2.3", "2.4", "2.5", "2.10", "2.11", "2.13"]:
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
          f"declared for {TEST_SET} (framework.md: 35)")
    if leaves + held + moved != 35 or total != 26:
        raise SystemExit(
            f"expected 35 leaves declared / 26 TCs, got "
            f"{leaves + held + moved} / {total}")


if __name__ == "__main__":
    main()
