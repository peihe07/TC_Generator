#!/usr/bin/env python3
"""Batch 13 generator — ICS Airflow and Defrost (handoff 59 §1).

Scope from framework.md §14's table, derived not retyped (48 §2):

    16.8  12 | 16.9  2 | 16.12  3 | 16.12.1  10 | 16.15  2   = 29 leaves

037 measured independently: 113(12) + 114(2) + 117(3) + 118(10) + 121(2) = 29.

Emitted: 29 TCs, -237 … -265. Nothing withheld.

**R-C40 applied BEFORE generating 16.12 / 16.12.1** (59 §1.1), because their
ch2 twins are stopped by DR #31. The one question — is the stop grounded in
the clause or in the chapter? — is answered by comparing the sentences, and
they are NOT verbatim:

  16.12  ICE11  "Airflow Modes has 5 states (1.Face … 5. Windshield)"
  2.12.1 C13.0  "**In some non-tri mode equipment types,** airflow modes
                 has 5 states (1.Face … 5. Windshield)"
                 -> ICE11 has NO configuration qualifier

  16.12.1 ICE11.1 loop: Face > Face/Feet > Feet > Feet/Windshield >
                        **Windshield**
  2.12.2  C13.1   loop: Face > Face/Feet > Feet > Feet plus Windshield >
                        **then repeat loop / Defrost will not be included**
                 -> different loops: FIVE modes vs FOUR

R-C40's precondition (逐字相同) is therefore NOT met for either pair, and the
difference falls exactly where it matters. DR #31 is that ch2's FOUR-mode
value has no positive statement of which vehicles carry it; ch16 has no
four-mode value at all — ICE11 states one airflow-mode set, unconditionally.
So the ch2 stop is grounded in the CHAPTER's context (three values, one of
them unstatable), not in the clause, and 59 §1.1's caution is discharged by
measurement rather than by "ch16's clause is complete". Both sides' reasoning
names its own ground; reported in 上繳 39 §6.2.

16.15 vs DR #40: judged independently, per 59 §1.1. ICE14 carries no
configuration qualifier at all, so -264/-265 take no configuration PC — the
same disposition as 2.15's -165/-166, and for the same reason rather than by
carry-over.

Usage:
    python3 features/comfort/scripts/gen_batch13.py
"""

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
FULLTEXT = FEATURE / "data" / "section_fulltext.tsv"
OUT = FEATURE / "generated"

TEST_GROUP = "Comfort"
TEST_SET = "ICS Airflow and Defrost"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
START_N = 237

DM_FUNC = "功能測試 (Functional based ; no specific technique)"
# profile §3.3 — the string must match 下拉選單!A1:A9 character for
# character. `, BVA` is part of the workbook's own entry; dropping it
# was caught by the design-method gate on the first run.
DM_BVA = "邊界值分析 (Boundary Value Analysis, BVA)"
DM_STATE = "狀態轉換 (State Transition Testing)"

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
MULTIZONE_EXPOSED = {"SWE1-HVAC-113-05"}
# Axis 1 — 16.3's -09 is the MTC value; the rest of 16.3 needs ATC, since
# ICE2's own last line is "(AUTO is not shown in MTC configurations)".
PC_ATC = ("[spec-derived] The vehicle has an ATC climate system, in which "
          "AUTO is shown (16.3)")
PC_MTC = "[spec-verbatim] The vehicle is in an MTC configuration (16.3)"
ATC_LEAVES = {"SWE1-HVAC-113-11"}
# Axis 4 — 16.13 is the MAX A/C section and 16.3's -05/-06 press it.
PC_MAXAC = ("[spec-derived] The system supports Max A/C, which is then "
            "displayed on the screen next to the A/C button (16.13)")
MAXAC_LEAVES = {"SWE1-HVAC-113-12"}
# Axis 5 — MAX DEF is pressed or read by these.
PC_MAXDEF = "[spec-derived] The vehicle is equipped with MAX DEF (3.2)"
MAXDEF_LEAVES = {f"SWE1-HVAC-113-{n:02d}" for n in range(1, 13)}
# Axis 10 — REAR DEFROST is pressed or read by these.
PC_REARDEF = ("[spec-derived] The vehicle is equipped with rear defrost, "
              "which is absent on some soft top vehicles (3.4)")
REARDEF_LEAVES = {"SWE1-HVAC-113-06", "SWE1-HVAC-114-01", "SWE1-HVAC-114-02"}
# Axis 16 — 115-05 turns a heated seat on.
PC_COMFORT = ("[spec-derived] The vehicle is equipped with Comfort features, "
              "such as heated/vented seats and a heated steering wheel (17.3)")
COMFORT_LEAVES = set()

EXTRA_PC = [(ATC_LEAVES, PC_ATC, ("16.3",)),
            (MAXAC_LEAVES, PC_MAXAC, ("16.13",)),
            (MAXDEF_LEAVES, PC_MAXDEF, ("3.2",)),
            (REARDEF_LEAVES, PC_REARDEF, ("3.4",)),
            (MULTIZONE_EXPOSED, PC_MULTIZONE, ("16.11",)),
            (COMFORT_LEAVES, PC_COMFORT, ("17.3",))]

WITHHELD = []



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
"16.8": "驗證目標：16.8（ICE7）以十二句定出 MAX DEF 對六項氣候參數之設定、自動關閉與回復，以及五種中斷途徑之落點，十二個 037 leaf 逐句對應（§8.2.1）。關鍵情境條件：EMEA 軸取正向值（16.2）；**第五軸（MAX DEF 有無，出處 3.2）十二條全補**；`113-06`（Sync）另補第二軸（16.11）、`113-07`（REAR DEFROST）另補第十軸（3.4）、`113-11`（AUTO）另補第一軸之 ATC 值（16.3）、`113-12`（MAX A/C）另補第四軸（16.13）；依 **R-C34** 第九軸與第十三軸暴露 → 全數補。為什麼這樣切：六項參數設定各自成條（`113-01`～`113-06`），任一項之失效可獨立定位；四種中斷途徑之落點各異（`113-09`～`113-12`），亦各自成條；`113-08`（風速不中斷）為其反例，與 `113-09`（其他變更中斷）成正反兩側（§7）。刻意略過：**其對造 `3.2`（C20）已生成而 `2.8`（C7）之 Defrost 為另一控制** —— 鏡射表記 `16.8 ↔ 3.2` 為 mirrored（七項連動逐字相同），故本節與 `3.2` 為鏡射對而非與 `2.8`；`113-01`～`113-12` 之判定與 `024-01`／`024-02` 之 TC 對 TC 比對見上繳 39 §6.3（§8.2.1：不因其為鏡射而互相移植）。",
"16.9": "驗證目標：16.9（ICE8）以兩句定出 Rear Defrost 之 on/off 狀態與 CCM 可用性之灰化，兩個 037 leaf 對應之。關鍵情境條件：EMEA 軸取正向值；**第十軸（REAR DEFROST 有無，出處 3.4）**兩條全補；依 **R-C34** 第九軸與第十三軸暴露 → 補。為什麼這樣切：狀態與灰化之觸發不同（按鍵 vs CCM 狀態），可獨立失效。刻意略過：**ICE8 僅兩句，不含 C8 之「independent of any other climate functions」與鏡面除霜之連動** —— 批次 10 之 `013-03`／`013-04` 已因此得 `no`；本節不驗該二者，亦不得反向以 C8 補之（§8.2.1）。",
"16.12": "驗證目標：16.12（ICE11）定出 ICS 之五種氣流模式、其單選性與 ON 態之呈現，三個 037 leaf 對應之。關鍵情境條件：EMEA 軸取正向值；依 **R-C34** 第九軸與第十三軸暴露 → 補。**R-C40 之一問已於生成前作答**（59 §1.1）：其 ch2 對造 `2.12.1` 之句子為「**In some non-tri mode equipment types,** airflow modes has 5 states…」，而 ICE11 **無該配置限定語**，故兩者**非逐字相同**，R-C40 之前件不成立；ch2 側 `2.12` 之停下（DR #31）源於 ch2 有**三個**氣流模式集合而其一（4 模式）無正面適用條件，而 **ch16 只陳述一組**，該問題於此不存在 —— 依 R-C40 屬「章節脈絡」而非「條文性質」，故不一致為實然，兩側各具名理由。為什麼這樣切：單選性、呈現與 main category control 之三者可獨立失效。刻意略過：**ICE11 自身之數字不一致** ——「Airflow Modes has **5** states」而其呈現句寫「ON state for the **four** airflow modes」（A-CF13 同型），故 `117-01` 只驗「所選之鍵高亮且變大」而**不驗按鈕數**。",
"16.12.1": "驗證目標：16.12.1（ICE11.1）以十句定出 Mode 硬鍵之循環、長按行為、於 Climate main 內外之呈現差異、pop-up 之逾時，以及後排畫面下之作用，十個 037 leaf 逐句對應。關鍵情境條件：EMEA 軸取正向值；依 **R-C34** 第九軸與第十三軸暴露 → 全數補。**R-C40 之一問已於生成前作答**：其 ch2 對造 `2.12.2`（C13.1）之循環為「Face > Face/Feet > Feet > **Feet plus Windshield > then repeat loop / Defrost will not be included**」（**四模式**），而 ICE11.1 為「Face > Face/Feet > Feet > Feet/Windshield > **Windshield**」（**五模式**）—— **兩者非逐字相同**，R-C40 前件不成立，其差異恰落在 DR #31 所治之處（4 模式之適用條件），故 ch2 側之停下不轉移。為什麼這樣切：`118-02`／`118-04`（Climate main 內外之兩種情形）為同一觸發之兩個分支，其呈現差異可獨立失效。刻意略過：**`118-09` 之後排畫面** —— 其可觀察量為**前排**模式（條文明寫 alters the front Mode），故不涉「車輛是否配備後排氣候」之未登記軸；該軸之問題在於**觀察後排**，本條觀察前排（與批次 9 之 `015-04`／`015-05` 之分野）。",
"16.15": "驗證目標：16.15（ICE14）以兩句定出對外後視鏡除霜之 on/off 狀態與其獨立性，兩個 037 leaf 對應之。關鍵情境條件：EMEA 軸取正向值；依 **R-C34** 第九軸與第十三軸暴露 → 補。**DR #40 於本節獨立判定**（59 §1.1：不以 ch2 側之未決為由停下，亦不以其為由生成）：**ICE14 自身無任何配置限定語**，故不補配置式 PC —— 此與 `2.15` 之 `021-01`／`021-02` 結論相同，**而其依據為本節自身之條文，非承襲 ch2 側之處置**。為什麼這樣切：`121-02`（獨立性）之驗證需兩個不同干擾源（AUTO、climate off），因「獨立」之否證只需一個反例。刻意略過：**DR #40 之不對稱於 ch16 側更明顯** —— `16.9`（ICE8）**連引用鏡面除霜都沒有**（C8 尚有「if this feature available」一句），故 ch16 側之語料對該配置**零陳述**；此實測已補入上繳 39 §5。"
}

TCTABLE = Path("/tmp/b13tcs.json")
# 58 §3 — 16.13's six exit paths overlap, and the overlap is §4.6 (sibling),
# NOT §4.5. §4.5 governs which FIELD data belongs in inside ONE TC; six exit
# paths are six TCs, so they are outside its range entirely. This is the
# SECOND correction of that shape (50 §4 was the first, on 17.1's three), so
# the boundary now lives in RUNBOOK.md as well.
#
# §10.6 strict equivalence, per pair — the TRIGGER differs in every one, and
# for two of them the OUTCOME differs as well:
#   -233  fan speed change   -> MAX A/C off, rest of the state KEPT
#   -234  temp/recirc/mode   -> MAX A/C off, previous mode except that element
#   -235  press A/C          -> MAX A/C off, previous mode, A/C OFF
#   -236  press AUTO         -> MAX A/C off, system in AUTO
#   -237… (see below; -236 is the last emitted id)
# duplicate_of therefore does NOT apply to any pair. Written out rather than
# waved through as "obviously different" (58 §3).
DIST_AXIS = {
    "16.9": {
        "axis": "profile §3.2 第九軸「EMEA ICS 車型」之值（介面型，R-C34）",
        "delta": "`2.9` 取**非 ICS** 值（ch2 之 climate screen），`16.9` 取 **ICS** 值（ch16 之 ICS climate screen）。**兩節之 TC 於 `test_item`／`test_procedure`／`expected_result` 三欄逐字相同**（`013-01`≡`114-01`、`013-02`≡`114-02`，見 pending_sibling 之 `equivalent_tc_pairs`），其唯一差異在 `pre_conditions` 之軸值 —— 此即 §10.6 所謂「另有可區辨之情境條件」，故 **`duplicate_of` 不填**；惟 `2.9` 尚有 `013-03`（獨立性）與 `013-04`（鏡面除霜連動）二條為 ICE8 所無，兩側不等勢",
    },
    "16.15": {
        "axis": "profile §3.2 第九軸「EMEA ICS 車型」之值（介面型，R-C34）",
        "delta": "`2.15` 取**非 ICS** 值，`16.15` 取 **ICS** 值。**兩節之 TC 三欄逐字相同**（`021-01`≡`121-01`、`021-02`≡`121-02`），差異僅在 `pre_conditions` 之軸值，故 `duplicate_of` 不填而以軸值區辨。**本對是全corpus 中唯一兩側 leaf 數相等且逐條等價者**，故其「兩份 TC 是否應合併為一份並以軸值參數化」之問題最為赤裸 —— 已隨 037 分解案登 DR #38",
    },
    "16.8": {
        "axis": "MAX DEF 之中斷途徑（trigger）與其落點（outcome）",
        "delta": "四條中斷條各異 —— `113-09` 改溫度／recirc／模式或再按 MAX DEF → "
                 "回前一手動模式且 A/C **開**；`113-10` 按 A/C → 回前一手動模式且 "
                 "A/C **關**；`113-11` 按 AUTO → 系統進入 **AUTO**；`113-12` 按 MAX A/C "
                 "→ 系統進入 **MAX A/C**。另 `113-08`（改風速）之 outcome 為 "
                 "**不中斷**，與其餘四條相反。**§10.6 四項中 trigger 於五條全異、"
                 "outcome 於四條亦異，無一對構成 `duplicate_of`**；其重疊屬 §4.6 "
                 "而非 §4.5（六條 TC 不在 §4.5 之射程內）",
    },
}

PARENTS = {"16.8": "SWE1-HVAC-113", "16.9": "SWE1-HVAC-114",
           "16.12": "SWE1-HVAC-117", "16.12.1": "SWE1-HVAC-118",
           "16.15": "SWE1-HVAC-121"}
KEYWORDS = {"16.8": ["MAX DEF", "Windshield", "HI", "REAR DEFROST"],
            "16.9": ["Rear Defrost", "gray out", "CCM"],
            "16.12": ["airflow mode", "5 states", "highlight"],
            "16.12.1": ["Mode hard control", "loop", "pop-up"],
            "16.15": ["mirror defrost", "independent"]}


def ref(*outlines) -> str:

    return "; ".join(f"{STEM}_{o}" for o in dict.fromkeys(outlines))


def main() -> None:
    full = {r["outline"]: r for r in
            csv.DictReader(FULLTEXT.open(encoding="utf-8"), delimiter="\t")}
    table = json.loads(TCTABLE.read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    n = START_N - 1
    total = 0

    for o in ["16.8", "16.9", "16.12", "16.12.1", "16.15"]:
        tcs = []
        for leaf, title, item, proc, er, prio, dm in table[o]:
            if f"SWE1-HVAC-{leaf}" in {w for w, _ in WITHHELD}:
                continue
            n += 1
            req = f"SWE1-HVAC-{leaf}"
            extra, refs = [], [o, "16.2"]
            if req in ATC_LEAVES:
                extra.append(PC_ATC)

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
        doc = {
            "parent": PARENTS[o], "outline": o, "batch": TEST_SET,
            "source_clause": full[o]["full_text"],
            "reasoning": REASONING[o], "keywords": KEYWORDS[o],
            "duplicate_of": "",
            "distinguishing_axis": DIST_AXIS.get(
                o, {"axis": "see per-TC titles", "delta": ""}),
            "assumptions": [],
            "interface_axis_review": INTERFACE_AXIS_REVIEW[o], "tcs": tcs,
        }
        (OUT / f"{PARENTS[o]}.json").write_text(
            json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(tcs)
        print(f"{PARENTS[o]}  {o:8} {len(tcs)} TC")

    print(f"\n{total} leaves -> {total} TCs; "
          f"tc_id {TC_ID_FMT.format(n=START_N)} … {TC_ID_FMT.format(n=n)}")
    print(f"{total} emitted + {len(WITHHELD)} withheld = "
          f"{total + len(WITHHELD)} leaves declared for {TEST_SET} "
          f"(framework.md: 29)")
    if total + len(WITHHELD) != 29 or total != 29:
        raise SystemExit(f"expected 29 / 29, got {total + len(WITHHELD)} / {total}")


if __name__ == "__main__":
    main()
