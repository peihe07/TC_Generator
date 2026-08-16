#!/usr/bin/env python3
"""Batch 10 generator — Airflow and Defrost (handoff 53 §2).

Scope from framework.md line 42 / its §4 table, derived not retyped (48 §2):

    2.8  6 | 2.9  4 | 2.12  3 | 2.12.1  2 | 2.12.2  6 | 2.15  2  = 23 leaves

037 measured independently: 012(6) + 013(4) + 016(3) + 017(2) + 018(6)
+ 021(2) = 23.

Emitted: 14 TCs, -153 … -166.
WITHHELD: 9 leaves — 2.12 (3) and 2.12.2 (6), both on DR #31.

  !! 53 §2 says "DR #31 只卡其 2 leaf". That is a section count read as a leaf
  !! count: 2.12 and 2.12.2 are 2 SECTIONS but 9 LEAVES. Reported in 上繳
  !! 36 §5.2. The disposition is unchanged either way — both sections stop —
  !! but the coverage arithmetic is not (14/23, not 21/23).

Why the whole of both sections stops, rather than part: C13's subject is the
4-mode configuration ("There are 4 Airflow Mode displayed in this order"), and
C13.1's loop is that same set. DR #31 is that the 4-mode value has no positive
statement of WHICH vehicles have it — so no leaf under either section can name
its own applicability. 2.12.1 is unaffected: C13.0 carries its own qualifier
("In some non-tri mode equipment types"), which is exactly why the third axis
could be swapped in the first place.

§8.2.1 boundaries against the already-generated 3.x, named per 53 §2.1:
  3.2 (C20) MAX DEF sets Windshield + 7/7 + HI + RECIRC open + Sync + REAR
      DEFROST. NOT imported — this batch's Defrost is C7's `FRONT DEF`, a
      different control with a different clause
  3.3 (C21) MAX DEF and REAR DEF remain available during climate off. NOT
      imported — 2.9's greying is CCM availability, not climate-off state
  2.15's clause label is `C16.`, colliding with 16.17's `C16.` (A-CF13 first
      item). Citations key on the outline, never the label

Usage:
    python3 features/comfort/scripts/gen_batch10.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"
TCTABLE = Path("/tmp/b10tcs.json")

TEST_GROUP = "Comfort"
TEST_SET = "Airflow and Defrost"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 153

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
PC_PLAIN = "1. [test-setup] The climate screen is open and the climate system is on"
PC_ATC = ("1. [spec-derived] The vehicle has an ATC climate system, in which "
          "AUTO is shown (2.3)")
PC_REARDEF = ("1. [spec-derived] The vehicle is equipped with rear defrost, "
              "which is absent on some soft top vehicles (3.4)")
# C13.0 carries its own qualifier, so the third axis's value is statable here
# — the one section of this Test Set that DR #31 does not reach.
PC_5STATE = ("1. [spec-verbatim] The vehicle is a non-tri mode equipment type "
             "whose airflow modes have 5 states (2.12.1)")
# C8's own conditional. R-C28 Q1 is satisfied by the clause itself, so this is
# a clause-local trigger condition (§8.5), NOT a new profile axis — the same
# shape as 2.13's "when CCM relays presence of MAX A/C functionality". Whether
# "exterior mirror defrost present/absent" should also be registered as an
# axis is raised in 上繳 36 §5.4 rather than decided here.
PC_MIRROR = ("2. [spec-verbatim] The exterior rear-view mirror defrost feature "
             "is available on the vehicle (2.9)")

# Per-section starting pre_condition and the extra spec_ref sections it cites.
SECTION_PC = {
    "2.8": (PC_PLAIN, ()), "2.9": (PC_REARDEF, ("3.4",)),
    "2.12.1": (PC_5STATE, ()), "2.15": (PC_PLAIN, ()),
}
# -012-05 turns AUTO on, so it needs the ATC value (C2's "AUTO is not shown in
# MTC configurations").
LEAF_PC = {"012-05": (PC_ATC, ("2.3",))}
LEAF_EXTRA = {"013-04": (PC_MIRROR, ())}

REASONING = {
"2.8": "驗證目標：2.8（C7）以七句定出 Defrost 之狀態、其對 A/C 與風速之自動作用、與其他氣流模式之互斥、與 AUTO 之互相關閉，以及 Recirc 可用性之灰化，六個 037 leaf 逐句對應，一葉一 TC（§8.2.1）。關鍵情境條件：本節無配置條件，起始 PC 為 test-setup；`012-05`（AUTO 與 Defrost 互相關閉）另取第一軸之 ATC 值（C2「AUTO is not shown in MTC configurations」，出處 2.3，併入 spec_ref 依 R-C29）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答，第十二軸不補。為什麼這樣切：`012-05` 之兩個方向（AUTO 關掉 Defrost、Defrost 中斷 AUTO）為 037 之同一 leaf，故合為一條而以兩組步驟涵蓋（§8.2 單位歸 037）；`012-06` 之灰化以 CCM 之可用性狀態為觸發，與 `012-02` 之 on/off 無關。刻意略過：**不移植 `3.2`（C20）之 MAX DEF 連動** —— 本節之 Defrost 為 C7 之 `FRONT DEF`，與 MAX DEF 為不同控制、不同條文（§8.2.1）；C7 之「Recirc **is may or may not be** available」為條文之語病，本條依其可判之部分（灰化）立 ER，不推斷其可用性規則。",
"2.9": "驗證目標：2.9（C8）定出 Rear Defrost 之狀態、灰化條件、與其他氣候功能之獨立性，以及對外後視鏡除霜之連動，四個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：第十軸（REAR DEFROST 有無）—— 起始 PC 取其有值，出處 **3.4**（「the rear defrost button will not appear when not present in the vehicle」，跨節取據 R-C29，3.4 併入 spec_ref）；`013-04` 另補 C8 自身之條件「if this feature available」（**條文自帶之情境條件，非新軸** —— R-C28 第一問由 C8 明文滿足，形態同 2.13 之「when CCM relays presence of MAX A/C functionality」）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`013-03`（獨立性）以兩個不同的干擾源（AUTO、FRONT DEF）各驗一次，因「獨立」之否證只需一個反例。刻意略過：**不移植 `3.3`（C21）之 climate off 可用性** —— 本節之灰化來自 CCM 之可用性狀態，與 climate off 之狀態無關（§8.2.1）；C8 未定義「certain modes」為哪些模式，故 `013-02` 以 CCM 狀態為觸發而不列舉模式（§8.4.1）。",
"2.12.1": "驗證目標：2.12.1（C13.0）定出非 tri-mode 設備型之五種氣流模式及其於畫面之呈現，兩個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：profile §3.2 **第三軸（前排氣流模式集合）之「5 狀態」值** —— **本節是該軸三值中唯一自帶正面限定語者**（「In some **non-tri mode equipment types**」），故其值可陳述而 `2.12`／`2.12.2` 不可（DR #31）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`017-01` 驗五個狀態之順序，`017-02` 驗所選狀態之呈現，兩者失效形態不同（順序錯 vs 呈現錯）。刻意略過：**`017-02` 不驗按鈕數** —— 其 ch16 對造 ICE11 自身寫 `5 states` 而其呈現句寫 `ON state for the **four** airflow modes`，係條文內部之數字不一致（A-CF13 同型），故本條只驗「所選模式呈現為作用中」；C13.0 未給硬鍵循環之規則（那在 C13.1，屬停下之 `2.12.2`），本節不涉。",
"2.15": "驗證目標：2.15（C16.）定出對外後視鏡除霜之 on/off 狀態與其獨立性，兩個 037 leaf 對應之，一葉一 TC（§8.2.1）。關鍵情境條件：本節之條文**無任何配置限定語**，故不補配置式 PC（與 `2.4`／`2.5` 同例）—— **惟 `2.9`（C8）以「if this feature available」暗示其為可選配備**，該不對稱已於上繳 36 §5.4 呈報；依 **R-C34** 第九軸與第十三軸暴露 → 全數補，EMEA 排除補並逐條答。為什麼這樣切：`021-02`（獨立性）之驗證需兩個不同干擾源（AUTO、climate off），因「獨立」之否證只需一個反例。刻意略過：**本節之條款標籤為 `C16.`，與 `16.17` 之 `C16.` 撞號**（A-CF13 第一項），故 traceability 一律以 outline 節次為鍵（profile §1），`specification_reference` 記 2.15 而非條款標籤；C16 未述該功能之操作元件位置，故步驟以功能名稱為目標而不指定按鈕位置（§8.4.1）。",
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
    "2.9": {
        "axis": "profile §3.2 第九軸「EMEA ICS 車型」之值（介面型，R-C34）",
        "delta": "`2.9` 取**非 ICS** 值（ch2 之 climate screen），`16.9` 取 **ICS** 值（ch16 之 ICS climate screen）。**兩節之 TC 於 `test_item`／`test_procedure`／`expected_result` 三欄逐字相同**（`013-01`≡`114-01`、`013-02`≡`114-02`，見 pending_sibling 之 `equivalent_tc_pairs`），其唯一差異在 `pre_conditions` 之軸值 —— 此即 §10.6 所謂「另有可區辨之情境條件」，故 **`duplicate_of` 不填**；惟 `2.9` 尚有 `013-03`（獨立性）與 `013-04`（鏡面除霜連動）二條為 ICE8 所無，兩側不等勢",
    },
    "2.15": {
        "axis": "profile §3.2 第九軸「EMEA ICS 車型」之值（介面型，R-C34）",
        "delta": "`2.15` 取**非 ICS** 值，`16.15` 取 **ICS** 值。**兩節之 TC 三欄逐字相同**（`021-01`≡`121-01`、`021-02`≡`121-02`），差異僅在 `pre_conditions` 之軸值，故 `duplicate_of` 不填而以軸值區辨。**本對是全corpus 中唯一兩側 leaf 數相等且逐條等價者**，故其「兩份 TC 是否應合併為一份並以軸值參數化」之問題最為赤裸 —— 已隨 037 分解案登 DR #38",
    },
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

WITHHELD = [
 ("SWE1-HVAC-016-01", "`2.12`（C13）全節之主體為 **4 模式配置**（「There are 4 Airflow Mode displayed in this order」），而 **DR #31**：該值於條文中無正面之適用條件（C13 為無限定之一般句），只能由排除得出。本 leaf 之「ON state … highlighting the button and increasing button size」明寫 `for the four airflow modes`，於 5 狀態與 tri-mode 車上不成立，故無可陳述之 PC"),
 ("SWE1-HVAC-016-02", "同 `016-01`：main category control 顯示所選模式，其模式集合即 C13 之四者"),
 ("SWE1-HVAC-016-03", "同 `016-01`；且「Only one airflow mode can be selected at a time」**於 tri-mode 車為假**（C19 之三鍵可個別 toggle），故尤須先能陳述本車之值"),
 ("SWE1-HVAC-018-01", "`2.12.2`（C13.1）之循環序 `Face > Face/Feet > Feet > Feet plus Windshield` 即 C13 之四模式集合，同受 **DR #31** 所阻"),
 ("SWE1-HVAC-018-02", "同 `018-01`：長按只跳一格，其「一格」之定義依該循環序"),
 ("SWE1-HVAC-018-03", "同 `018-01`"),
 ("SWE1-HVAC-018-04", "同 `018-01`"),
 ("SWE1-HVAC-018-05", "同 `018-01`"),
 ("SWE1-HVAC-018-06", "同 `018-01`；本 leaf 另涉後排畫面（`ch2_ch7_mirror_map.tsv` 記 7.1 ↔ 2.12.2 partial），惟其停下之主因仍為 DR #31"),
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
    parents = {"2.8": "SWE1-HVAC-012", "2.9": "SWE1-HVAC-013",
               "2.12.1": "SWE1-HVAC-017", "2.15": "SWE1-HVAC-021"}

    for o in ["2.8", "2.9", "2.12.1", "2.15"]:
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
    print(f"\n{leaves} emitted + {held} withheld = {leaves + held} leaves "
          f"declared for {TEST_SET} (framework.md: 23)")
    if leaves + held != 23 or total != 14:
        raise SystemExit(
            f"expected 23 leaves declared / 14 TCs, got {leaves + held} / {total}")


if __name__ == "__main__":
    main()
