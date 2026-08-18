#!/usr/bin/env python3
"""User Profiles 之 TC lint —— 掃 `generated/*.json`，逐閘印實測值。

**本檔為本 feature 自建，非自 Comfort 複製** —— Comfort 之 lint 帶其
feature-specific 白名單（`[BLOCKED-SPEC]` 標記、HVAC 之 tc_id 集合）與
其 spec stem，套到本 feature 只會產生誤報。共用的是 canon，不是那支程式。

## 閘

| 閘 | 依據 |
|---|---|
| G1 必填欄位齊全 | 工作簿之 15 欄對映（feature.yaml）|
| G2 `tc_id` 格式、不重複、自 001 起連續 | canon §10.3、R-U2 |
| G3 `test_item` == `tc_title` 且 2–14 字 | R-U6（BLANK 綁定）、canon §4.3 |
| G4 `tc_title` 無 modal／hedge | canon §4.3 |
| G5 sibling `tc_title` 不得雷同 | canon §4.3 |
| G6 pre-condition 不含動作／查核 | canon §4.4 |
| G7 步驟數 ≥ 2 | canon §10.5 |
| G8 最終步須帶查核目標；不得以禁用動詞為主動詞 | canon §5.1／§5.5 |
| G9 步驟數與 ER 行數相等 | canon §6 |
| G10 `design_method` 屬下拉選單九條逐字 | feature.yaml lint.design_method_source |
| G11 `specification_reference` 之 stem 與節次形態 | R-U1、canon §10.7 |
| G12 `priority` ∈ {P0..P3} | 工作簿 DV（feature.yaml）|
| G13 `test_group`／`test_set` 逐字 | R-U1、framework §2 |
| G16 `feature.yaml` 之 popup_ids 與現測 `pdf_text` 一致 | D-5（14 包）|
| G15 步驟長度：一般 ≤12 詞、最終步／intent 步 ≤18 詞 | canon §5.2 |
| G14 PU id 須屬 spec 之 PU 全集（**現測 `pdf_text`**，21 個）| R-U35 (a)；feature.yaml 之 20 個為 xlsx 側，見 `known_pu()` |

## 範圍向（R-G9）

`--self-test` 對**每一閘**造一條會紅之假 TC ＋ 一條不得轉紅之對照，
證明該閘既抓得到違規、也不會對合規者誤報。**只跑語料不算驗過。**

Usage:
    python3 features/user_profiles/scripts/lint_tcs.py              # 掃語料
    python3 features/user_profiles/scripts/lint_tcs.py --self-test  # 範圍向
"""

import argparse
import json
import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent
CFG = yaml.safe_load((FEATURE / "feature.yaml").read_text(encoding="utf-8"))

TC_ID_RE = re.compile(r"^NR1L-UserProfiles-(\d{3})$")
STEM = "Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)"
REF_ITEM_RE = re.compile(re.escape(STEM) + r"_\d+(?:\.\d+)*$")

REQUIRED = ("req_id", "tc_id", "tc_title", "test_group", "test_set",
            "test_item", "pre_conditions", "input_test_data",
            "test_procedure", "expected_result", "specification_reference",
            "priority", "design_method", "functional_safety", "remarks")

MODALS = re.compile(r"\b(should|shall|will|must)\b", re.I)
HEDGES = re.compile(r"\b(properly|successfully|correctly|as expected|"
                    r"within reasonable time)\b", re.I)
# canon §5.1 —— 把判斷推給測試員之主動詞
BANNED_MAIN_VERB = re.compile(
    r"^\s*\d+\.\s*(observe|see if|check whether|confirm whether|verify|"
    r"watch|monitor|inspect)\b", re.I | re.M)
CHECK_INTENT = re.compile(r"\b(check that|confirm that|to verify|to check|"
                          r"read|record|compare)\b", re.I)
# canon §4.4 —— pre-condition 不得要求 do / check / confirm
#
# **判準改過一次（R-U37：改判準，不改案例）。**
# v1：整行掃動詞字樣 —— 對「The Profile setup flow **is open** at Step 2
#     “**Enter** a username”」轉紅。那一行寫的是**狀態**，
#     `open` 是形容詞、`Enter` 是被引號括起來的畫面標題。
#     **一個掃字樣的判準分不出「動詞」與「長得像動詞的字」。**
# v2（現行）：只在**句首**（編號之後）認祈使動詞 —— pre-condition 之合規寫法
#     一律為「The X is …」，以動詞起首者才是動作；
#     另保留 check/confirm/verify 之全行比對（它們在句中亦屬查核）。
PRE_ACTION_HEAD = re.compile(
    r"^\s*\d+\.\s*(press|select|open|enter|insert|navigate|tap|swipe|"
    r"connect|activate|type)\b", re.I)
PRE_CHECK_ANY = re.compile(r"\b(check that|confirm that|verify)\b", re.I)

DESIGN_METHODS = {
    "功能測試 (Functional based ; no specific technique)",
    "狀態轉換 (State Transition Testing)",
    "決策表 (Decision Table Testing)",
    "等價劃分 (Equivalence Partitioning, EP)",
    "邊界值分析 (Boundary Value Analysis, BVA)",
    "組合測試 (Combinatorial Testing ; Pairwise / t-wise)",
    "情境 / 用例 (Scenario / Use Case Testing)",
    "負向測試 (Negative / Invalid)",
    "基礎故障注入 (Fault Injection Lite)",
}
TEST_SETS = {"Preference Storage", "Profile List", "Defaults",
             "Welcome Flow", "Setup Flow", "Editing",
             "Connected Account", "Valet Mode"}
PU_RE = re.compile(r"PU[\s_]?(\d{3,4})", re.I)


def known_pu() -> set:
    """PU id 之全集 —— **以 `pdf_text` 現測，不用 feature.yaml 之定值**。

    `feature.yaml` 之 `lint.popup_ids`（20 個）其量測條件自陳為
    「掃 `outline_map.json` 之 169 條 **Description** 欄」—— 那是 **xlsx 側**，
    而 R-U35 (a) 已定 `pdf_text` 為判讀基準。兩側差一個：**`PU0609`**，
    它正好落在 9.8 之掉句裡（`data/xlsx_missing_clauses.tsv` 之 must_carry）。

    即：**以 xlsx 側量得之清單去檢查以 PDF 側生成之 TC，必然誤報**。
    故本函式現測 PDF 側；`feature.yaml` 之值不動（它是有量測條件的紀錄，
    其條件在當時為真），差異已具名上報。
    """
    import build_batch_context as _B
    out = set()
    for v in _B._outline().values():
        for m in PU_RE.finditer(v.get("pdf_text") or ""):
            out.add(f"PU{int(m.group(1)):04d}")
    return out


KNOWN_PU = known_pu()
RULED_PU = {f"PU{int(x[2:]):04d}" for x in CFG["lint"]["popup_ids"]}


def _lines(v: str) -> list:
    """**頂層**編號行。

    **判準改過一次（R-U37）。** v1 取所有非空行 —— 但 canon §6.1 允許
    ER 以 `a./b./c.` 子層列出列項（D-3 之 Table CPA2 即此形態），
    於是「ER 行數」被子層灌大，G9 對一條正確的 TC 轉紅。
    v2：只計頂層之 `N.` 行；縮排之子層不計。
    """
    return [x for x in str(v).splitlines()
            if x.strip() and not x.startswith((" ", "\t"))]


# --------------------------------------------------------------- 逐條之閘

def gate_tc(tc: dict) -> list:
    """單條 TC 之違規清單（不含跨條之 G2／G5）。"""
    out, tid = [], tc.get("tc_id", "?")

    missing = [f for f in REQUIRED if f not in tc]
    if missing:
        out.append(f"G1 {tid}: 缺欄位 {missing}")

    if not TC_ID_RE.match(str(tc.get("tc_id", ""))):
        out.append(f"G2 {tid}: tc_id 不合 NR1L-UserProfiles-NNN")

    title = str(tc.get("tc_title", ""))
    if str(tc.get("test_item", "")) != title:
        out.append(f"G3 {tid}: test_item 與 tc_title 不同（R-U6）")
    n = len(title.split())
    if not 2 <= n <= 14:
        out.append(f"G3 {tid}: tc_title {n} 字，須 2–14（§4.3）")

    if MODALS.search(title):
        out.append(f"G4 {tid}: tc_title 含 modal（§4.3）")
    if HEDGES.search(title):
        out.append(f"G4 {tid}: tc_title 含 hedge（§4.3）")

    for ln in _lines(tc.get("pre_conditions", "")):
        if PRE_ACTION_HEAD.search(ln) or PRE_CHECK_ANY.search(ln):
            out.append(f"G6 {tid}: pre-condition 含動作／查核 → {ln[:60]}")

    proc = _lines(tc.get("test_procedure", ""))
    er = _lines(tc.get("expected_result", ""))
    if len(proc) < 2:
        out.append(f"G7 {tid}: 步驟 {len(proc)} 條，須 ≥ 2（§10.5）")
    if proc:
        if BANNED_MAIN_VERB.search(tc.get("test_procedure", "")):
            out.append(f"G8 {tid}: 步驟以禁用動詞為主動詞（§5.1）")
        if not CHECK_INTENT.search(proc[-1]):
            out.append(f"G8 {tid}: 最終步無查核目標（§5.5）→ {proc[-1][:60]}")
    if len(proc) != len(er):
        out.append(f"G9 {tid}: 步驟 {len(proc)} 條 vs ER {len(er)} 條（§6）")

    # G15 —— canon §5.2 之步驟長度（D-4）
    #   A 一般 setup／transition 步：≤ 12 詞
    #   B 最終步（§5.5 查核擁有者）：≤ 18 詞（含 action ＋ check target）
    #   C §5.1 例外之 intent 步（帶 `to …` 目的子句）：≤ 18 詞
    for i, ln in enumerate(proc, 1):
        body = re.sub(r"^\s*\d+\.\s*", "", ln)
        w = len(body.split())
        is_final = (i == len(proc))
        is_intent = bool(re.search(r"\bto\s+\w+", body)) and not is_final
        cap = 18 if (is_final or is_intent) else 12
        kind = "最終步" if is_final else ("intent 步" if is_intent else "一般步")
        if w > cap:
            out.append(f"G15 {tid}: 步驟 {i}（{kind}）{w} 詞 > {cap}（§5.2）"
                       f" → {body[:50]}…")

    if tc.get("design_method") not in DESIGN_METHODS:
        out.append(f"G10 {tid}: design_method 非下拉選單九條之一")

    for ref in str(tc.get("specification_reference", "")).split("; "):
        if not REF_ITEM_RE.match(ref.strip()):
            out.append(f"G11 {tid}: spec_reference 形態不符 → {ref[:70]}")

    if tc.get("priority") not in ("P0", "P1", "P2", "P3"):
        out.append(f"G12 {tid}: priority 不在 P0–P3")

    if tc.get("test_group") != CFG["test_group"]:
        out.append(f"G13 {tid}: test_group 非 `{CFG['test_group']}`")
    if tc.get("test_set") not in TEST_SETS:
        out.append(f"G13 {tid}: test_set `{tc.get('test_set')}` 不在八組內")

    blob = " ".join(str(tc.get(f, "")) for f in
                    ("test_item", "pre_conditions", "test_procedure",
                     "expected_result", "remarks"))
    for m in PU_RE.finditer(blob):
        pu = f"PU{int(m.group(1)):04d}"
        if pu not in KNOWN_PU:
            out.append(f"G14 {tid}: {pu} 不在 spec 之 PU 全集內"
                       f"（現測 pdf_text，{len(KNOWN_PU)} 個）")
    return out


def gate_corpus(tcs: list) -> list:
    """跨條之閘。"""
    out = []
    # **判準改過一次（R-U37）。**
    # v1：驗「以檔案順序讀出之 tc_id 遞增」—— 但檔案順序是 `sorted(glob)`，
    #     即檔名序；`…-070.json` 排在 `…-073-01.json` 之前，而號碼是依
    #     **取樣順序**指派的。於是它對一批正確指派的號碼轉紅。
    #     **驗錯了對象：canon §10.3 管的是指派，不是我讀檔的順序。**
    # v2（現行）：驗真正的不變量 —— 號碼**不重複**且**自 001 起連續**。
    seq = sorted(TC_ID_RE.match(t["tc_id"]).group(1) for t in tcs
                 if TC_ID_RE.match(str(t.get("tc_id", ""))))
    if len(set(seq)) != len(seq):
        out.append(f"G2: tc_id 有重複 → {[x for x in seq if seq.count(x) > 1]}")
    expect = [f"{i:03d}" for i in range(1, len(tcs) + 1)]
    if seq != expect:
        out.append(f"G2: tc_id 未自 001 起連續 → 實得 {seq}")
    # G16（D-5）—— `feature.yaml` 之定值與現測不得分岔。
    # 13 輪之狀態是「lint 現測 21、yaml 記 20，兩個數並存而無指引」；
    # D-5 已使其一致，**本閘防止它再度悄悄分岔**（分岔時無人會發現）。
    if RULED_PU != KNOWN_PU:
        out.append(f"G16: feature.yaml 之 popup_ids（{len(RULED_PU)}）與現測 "
                   f"pdf_text（{len(KNOWN_PU)}）不符 —— "
                   f"yaml 多：{sorted(RULED_PU - KNOWN_PU)}；"
                   f"現測多：{sorted(KNOWN_PU - RULED_PU)}")

    seen = {}
    for t in tcs:
        key = str(t.get("tc_title", "")).lower().strip()
        if key in seen:
            out.append(f"G5: tc_title 與 {seen[key]} 雷同 → {t['tc_id']}")
        seen[key] = t.get("tc_id")
    return out


# ------------------------------------------------------------------ 語料

def run_corpus() -> int:
    recs, tcs = [], []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        recs.append(r)
        tcs += r.get("tcs", [])
    if not tcs:
        print("generated/ 為空 —— 無可掃之 TC")
        return 0
    bad = [b for tc in tcs for b in gate_tc(tc)] + gate_corpus(tcs)
    print(f"掃 {len(recs)} 個 leaf 檔 / {len(tcs)} 條 TC")
    # **以號碼取最小最大，不取檔案順序** —— 檔案是依 req_id 排的，
    # 其首尾不等於號碼之首尾（batch01 加入後 `132-02` 仍排在最後而其號為 016）。
    ids = sorted(t["tc_id"] for t in tcs)
    print(f"tc_id 範圍 {ids[0]} … {ids[-1]}（{len(ids)} 條）")
    print(f"design_method 分布：" + ", ".join(
        f"{m.split(' (')[0]}×{sum(1 for t in tcs if t['design_method'] == m)}"
        for m in sorted({t["design_method"] for t in tcs})))
    print(f"priority 分布：" + ", ".join(
        f"{p}×{sum(1 for t in tcs if t['priority'] == p)}"
        for p in sorted({t["priority"] for t in tcs})))
    print(f"\n違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    return 1 if bad else 0


# ------------------------------------------------------------- 範圍向自驗

def _ok_tc(**kw) -> dict:
    """一條合規之基準 TC —— 每個範圍向案例自它改一處。"""
    base = {
        "req_id": "SWE1-HMI-PROF-001-01",
        "tc_id": "NR1L-UserProfiles-001",
        "tc_title": "Preferences recalled per Driver Profile",
        "test_group": "User Profiles",
        "test_set": "Preference Storage",
        "test_item": "Preferences recalled per Driver Profile",
        "pre_conditions": "1. Two Driver Profiles exist on the vehicle",
        "input_test_data": "NA",
        "test_procedure": ("1. Activate Driver Profile A\n"
                           "2. Read the preference and check that it matches "
                           "the recorded value"),
        "expected_result": ("1. Driver Profile A is active\n"
                            "2. The preference matches the recorded value"),
        "specification_reference": f"{STEM}_4.1",
        "priority": "P0",
        "design_method": "功能測試 (Functional based ; no specific technique)",
        "functional_safety": "NA",
        "remarks": "",
    }
    base.update(kw)
    if "tc_title" in kw and "test_item" not in kw:
        base["test_item"] = kw["tc_title"]
    return base


def self_test() -> int:
    ok = True

    def case(name, tc, expect_fail, gate):
        nonlocal ok
        bad = [b for b in gate_tc(tc) if b.startswith(gate)]
        good = bool(bad) == expect_fail
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_fail else '綠'}")
        for b in bad:
            print(f"      └ {b}")

    print("## 對照向 —— 合規之基準 TC 不得對任何閘轉紅\n")
    base_bad = gate_tc(_ok_tc())
    ok &= not base_bad
    print(f"  {'PASS' if not base_bad else '**FAIL**'} — 基準 TC 全綠")
    for b in base_bad:
        print(f"      └ {b}")

    print("\n## 注入 —— 每閘一條會紅，一條同閘之合規對照\n")
    cases = [
        ("G1", "缺 remarks 欄", {k: v for k, v in _ok_tc().items()
                                if k != "remarks"}),
        ("G2", "tc_id 格式錯", _ok_tc(tc_id="UserProfiles-1")),
        ("G3", "test_item 與 tc_title 不同", _ok_tc(test_item="something else")),
        ("G3", "tc_title 15 字", _ok_tc(tc_title=" ".join(["word"] * 15))),
        ("G4", "tc_title 含 shall", _ok_tc(tc_title="Preferences shall be recalled")),
        ("G4", "tc_title 含 properly", _ok_tc(tc_title="Preferences recalled properly")),
        ("G6", "pre-condition 含動作", _ok_tc(
            pre_conditions="1. Press the Profile button")),
        ("G7", "只有一步", _ok_tc(
            test_procedure="1. Read the preference and check that it matches",
            expected_result="1. The preference matches")),
        ("G8", "最終步無查核目標", _ok_tc(
            test_procedure="1. Activate Driver Profile A\n2. Open the list",
            expected_result="1. Active\n2. The list is displayed")),
        ("G8", "以 verify 為主動詞", _ok_tc(
            test_procedure="1. Activate Driver Profile A\n"
                           "2. Verify the preference is recalled",
            expected_result="1. Active\n2. The preference is recalled")),
        ("G9", "步驟 2 vs ER 3", _ok_tc(
            expected_result="1. a\n2. b\n3. c")),
        ("G10", "design_method 不在九條內", _ok_tc(design_method="Functional")),
        ("G11", "spec_reference 用檔名形式", _ok_tc(
            specification_reference="SYS1_HMI_Personal_Account_R1L-R_4.1")),
        ("G12", "priority = High", _ok_tc(priority="High")),
        ("G13", "test_set 不在八組", _ok_tc(test_set="Profiles")),
        ("G15", "一般步 13 詞（上限 12）", _ok_tc(
            test_procedure="1. " + " ".join(["word"] * 13) +
                           "\n2. Read the value and check that it matches",
            expected_result="1. a\n2. b")),
        ("G15", "最終步 19 詞（上限 18）", _ok_tc(
            test_procedure="1. Activate Driver Profile A\n"
                           "2. Read and check that " + " ".join(["w"] * 15),
            expected_result="1. a\n2. b")),
        ("G14", "PU9999 不存在", _ok_tc(
            expected_result="1. Driver Profile A is active\n"
                            "2. PU9999 is displayed")),
    ]
    for gate, name, tc in cases:
        case(f"{gate} 注入：{name}", tc, True, gate)

    print("\n## 範圍向 —— 同閘之合規者不得誤報\n")
    scope = [
        ("G4", "tc_title 含 will 之外形但為名詞 Willingness",
         _ok_tc(tc_title="Willingness prompt shown on setup")),
        ("G6", "pre-condition 為純狀態", _ok_tc(
            pre_conditions="1. Valet Mode is active and a PIN is set")),
        # v1 判準對這一行誤報（`is open` 之 open、引號內之 Enter）——
        # 這正是判準改版之案例，留作回歸。
        ("G6", "狀態句含 `is open` 與引號內之 `Enter`", _ok_tc(
            pre_conditions="1. The Profile setup flow is open at Step 2 "
                           "\u201cEnter a username\u201d")),
        ("G8", "最終步用 Read 為主動詞", _ok_tc(
            test_procedure="1. Activate Driver Profile A\n"
                           "2. Read the preference value shown in the list",
            expected_result="1. Active\n2. The value is shown")),
        ("G14", "PU0584 為實測 20 個之一", _ok_tc(
            expected_result="1. Driver Profile A is active\n"
                            "2. PU0584 is displayed")),
        # D-4 之明文要求：證明它對 12 詞之正常步驟不轉紅
        ("G15", "一般步剛好 12 詞 → 綠", _ok_tc(
            test_procedure="1. " + " ".join(["word"] * 12) +
                           "\n2. Read the value and check that it matches",
            expected_result="1. a\n2. b")),
        ("G15", "最終步剛好 18 詞 → 綠", _ok_tc(
            test_procedure="1. Activate Driver Profile A\n"
                           "2. Read and check that " + " ".join(["w"] * 13),
            expected_result="1. a\n2. b")),
        ("G15", "intent 步帶 `to …` 得放寬至 18 詞 → 綠", _ok_tc(
            test_procedure="1. Press and hold the top right and bottom left "
                           "corners for five seconds to enter Dealer Mode\n"
                           "2. Read the value and check that it matches",
            expected_result="1. a\n2. b")),
        ("G9", "ER 帶 a./b./c. 子層 → 綠（§6.1）", _ok_tc(
            expected_result="1. Driver Profile A is active\n"
                            "2. The screen lists:\n"
                            "   a. Personalization\n"
                            "   b. App Store Download")),
        ("G11", "spec_reference 併列 3.x", _ok_tc(
            specification_reference=f"{STEM}_4.1; {STEM}_3.1; {STEM}_3.5")),
    ]
    for gate, name, tc in scope:
        case(f"{gate} 範圍：{name}", tc, False, gate)

    print("\n## G16 —— yaml 與現測之分岔（D-5）\n")
    # 以 globals() 改寫，不用 `import lint_tcs` —— 本檔以 __main__ 執行時，
    # 再 import 一次會得到**另一個 module 物件**，改到的不是同一個名字。
    g = globals()
    _orig = g["RULED_PU"]
    for name, ruled, expect in [
        ("yaml 與現測一致 → 綠", set(KNOWN_PU), False),
        ("yaml 少一個（回到 13 輪之狀態）→ 紅",
         set(KNOWN_PU) - {"PU0609"}, True),
        ("yaml 多一個不存在者 → 紅", set(KNOWN_PU) | {"PU9999"}, True),
    ]:
        g["RULED_PU"] = ruled
        bad = [b for b in gate_corpus([_ok_tc()]) if b.startswith("G16")]
        good = bool(bad) == expect
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}")
        for b in bad:
            print(f"      └ {b}")
    g["RULED_PU"] = _orig

    print("\n## 跨條之閘（G2 單調／G5 雷同）\n")
    for name, tcs, expect in [
        ("遞增且相異 → 綠",
         [_ok_tc(tc_id="NR1L-UserProfiles-001"),
          _ok_tc(tc_id="NR1L-UserProfiles-002", tc_title="Second distinct title")],
         False),
        # **本案例隨 G2 之判準改版而更換。**
        # 舊案例為「tc_id 倒序 → 紅」，測的是「讀取順序遞增」——
        # v2 判準刻意不管讀取順序（號碼依取樣序指派，檔案依檔名序讀出），
        # 故該案例測的是**已被廢除的性質**，留著只會逼判準倒退。
        # 換為 v2 真正該抓的兩種：重複、跳號。
        ("倒序但不重複不跳號 → 綠（v2 不管讀取順序）",
         [_ok_tc(tc_id="NR1L-UserProfiles-002"),
          _ok_tc(tc_id="NR1L-UserProfiles-001", tc_title="Second distinct title")],
         False),
        ("tc_id 重複 → 紅",
         [_ok_tc(tc_id="NR1L-UserProfiles-001"),
          _ok_tc(tc_id="NR1L-UserProfiles-001", tc_title="Second distinct title")],
         True),
        ("tc_id 跳號（001, 003）→ 紅",
         [_ok_tc(tc_id="NR1L-UserProfiles-001"),
          _ok_tc(tc_id="NR1L-UserProfiles-003", tc_title="Second distinct title")],
         True),
        ("tc_title 雷同 → 紅",
         [_ok_tc(tc_id="NR1L-UserProfiles-001"),
          _ok_tc(tc_id="NR1L-UserProfiles-002")],
         True),
    ]:
        bad = gate_corpus(tcs)
        good = bool(bad) == expect
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}")
        for b in bad:
            print(f"      └ {b}")

    n = 1 + len(cases) + len(scope) + 8
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    sys.exit(self_test() if a.self_test else run_corpus())
