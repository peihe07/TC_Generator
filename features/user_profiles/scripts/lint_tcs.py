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
| G17 **多引**：引用欄之每一節須登記；**且其 `provides` 之字面值須真在該 TC 內** | J-6／**J-10**（19 包）|
| G18 **少引**：ER 之字面值（**引號、數字、PU id、狀態值**）須溯得到某一被引之節或登記之來源 | J-6／**J-10**（19 包）|
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


# ---- J-6 雙向自檢（18 包）之來源登記 ----
#
# **這兩閘只做機械可判定的那一半。** 「該節是否真被驗證」與
# 「這個觀察點出自哪一節」終究要人讀，但兩件事可以機器擋：
#   G17 引用欄出現了**沒有登記理由**的節 → 那正是 TC-013 之 11.5 的形狀
#   G18 ER 裡的**引號字面值**溯不到任何被引之節 → 那正是 5.1.1 的形狀
#        （少引之句子，其字面值會落在引用欄之外）

def _ref_allowlist() -> dict:
    """每個 req_id 之 `REF_EXTRA`：{req_id: [(節次, provides, 出處模組), …]}。"""
    mods = []
    for name in ("gen_pilot", "gen_batch01", "gen_batch02",
                 "gen_batch03", "gen_batch04", "gen_batch05",
                 "gen_batch06"):
        try:
            mods.append((__import__(name), name + ".REF_EXTRA"))
        except ImportError:
            pass          # 該批尚未存在
    out = {}
    for mod, tag in mods:
        # 並非每一批都有 REF_EXTRA（第三批即無）
        for k, v in getattr(mod, "REF_EXTRA", {}).items():
            out.setdefault(k, []).extend((sec, prov, tag) for sec, prov in v)
    return out


# **測試設置**（J-12 之第四類）—— 為使 TC 可執行而設之數值，非 spec 之值。
# 條文只說 `memory seat position`，編號是我們擺的；`Profile A/B` 亦然。
# G18 掃到這些數字時不轉紅，**但它們必須登記在此，不得默默通過**。
# **方法**（J-4 之第二類）—— 由測試方法本身要求之數值。
# BVA 之界前讀值（29 秒、11 字元）不在條文裡：條文只給邊界（30／12），
# 界前之值是 §5.6 要求「同一 TC 內取前後兩讀」才產生的。
# **與測試設置不同**：它承載驗證（界前須成立），只是其權威是方法而非條文。
METHOD_NUMERALS = {
    "NR1L-UserProfiles-008": ["29"],   # §5.6 界前讀值（邊界 30 秒）
    "NR1L-UserProfiles-066": ["29"],   # §5.6 界前讀值（邊界 30 分鐘）
    "NR1L-UserProfiles-009": ["11"],   # §5.6 界前讀值（邊界 12 字元）
}

TEST_SETUP_NUMERALS = {
    "NR1L-UserProfiles-028": ["1", "2"],   # memory seat 編號
    "NR1L-UserProfiles-029": ["2"],
    "NR1L-UserProfiles-031": ["2"],
    "NR1L-UserProfiles-030": ["2", "3"],   # profile 數與座椅數之邊界設置
    "NR1L-UserProfiles-056": ["1"],        # memory seat 編號（12.7 只說 the buttons）
    # 第三批（28 包）—— 4.4／4.5.2 之條文只寫 memory seat buttons／position，
    # **未給編號**；編號為測試設置之選擇（J-12），已於各該 remarks 具名。
    "NR1L-UserProfiles-091": ["1"],        # 4.4 覆寫側，座椅鍵編號
    "NR1L-UserProfiles-105": ["1"],        # 4.5.2 反向，座椅位置編號
}

# 狀態值 —— 其字面須溯得到被引之節
STATE_VALUES = ("Small", "Off", "On", "None")


# ER 之字面值溯源時，除被引之節之 `pdf_text` 外，另允許之來源。
# **逐項具名，不得以「其他」概括。**
LITERAL_EXTRA_SOURCES = {
    # Table CPA2 之列名與欄別出自 PDF p17 之**版面**，文字層已攤平（16 輪 F-2）
    "NR1L-UserProfiles-013": "PDF p17 版面（render_spec_region.py --regression 7/7）",
    "NR1L-UserProfiles-044": "PDF p17 之表級註記（R1 High Only）",
    # Table EDPR1 之列項出自 PDF p14 之 must_carry（補句表）
    "NR1L-UserProfiles-017": "PDF p14 之 Table EDPR1（must_carry）",
    # 53 包 §二.1 —— `TC-167` 之 ER4 補可觀察形式。
    # 其副標 `Learn about new features` 出自 **Tutorials HMI Logic and Flow
    # `INTR3.)`**，而**該 PDF 不在本 repo**（52／53 兩輪各查一次，全 repo 0 命中）；
    # 字串為 52 包 §3.1 之逐字引述。
    # **故其 `specification_reference` 未併列該文件** ——
    # G11 要求 `<stem>_<節次>` 之形，而節次只能自該 PDF 讀得；
    # 以 `INTR3` 充作節次等於造一個無法對照之引用（R-U1）。
    # 檔案到位後之修法見 53 上繳 §2.2（一行）。
    "NR1L-UserProfiles-167": "Tutorials HMI L&F `INTR3.)`（**檔案未在 repo**，"
                             "字串為 52 包 §3.1 之逐字引述）",
}

# **UI 定位詞**之來源登記。
#
# G18 首跑對 `“Edit Profile”` 轉紅 5 條 —— 那是真陽性，但屬另一類：
# 它是**跨批重複出現之分頁名**，其來源是 5.1（Profile 區有兩個分頁），
# 而各該 TC 只是把它當導覽起點。若逐條把 5.1 灌進引用欄，
# **每一條 ch9 之 TC 都會引用 5.1**，引用欄就變成導覽紀錄而非追溯。
#
# 故改為**一次登記於此**，並由 G18 自己驗證這張表沒說謊：
# 每個定位詞須確實出現在其登記節次之 `pdf_text` 裡，否則轉紅。
UI_LOCATORS = {
    "Edit Profile": "5.1",     # PRACC7.) …two tabs; “All Profiles” and “Edit Profile”
    "All Profiles": "5.1",     # 同上
}

QUOTED_RE = re.compile(r"[“\"]([^”\"]{4,})[”\"]")


# ── G19（§11 / L-1，22 包）—— 方括號 ─────────────────────────────
#
# canon §11 逐字：方括號 `[...]` 保留給該文件之 placeholder 語法與 sibling row
# 標記，**不得出現在 TC 輸出欄位**；其 profile-scoped 例外為「逐字引自被引來源
# 之 token 得保留原記法，**由 lint 對照來源列驗證，而非一律禁止**」。
#
# 故本閘**不是禁令，是對照**：每個方括號 token 須在該 TC 所引之節（或其
# must_carry）之原文內逐字找得到。找不到者為自擬 —— 轉紅。
#
# **為什麼不做成純禁令**：9.1.1 之 spec 原文即為
# `8.4" will show the username in the Edit Username line like
#  “Edit username: [username]”` —— 純禁令會逼 ER 改寫 spec 之逐字內容
# （§8.4.1 禁止），而純例外則等於開一個沒有邊界的口子。**對照是唯一兩者皆不犯的作法。**
BRACKET_RE = re.compile(r"\[[^\]\n]{0,80}\]")
BRACKET_FIELDS = ("tc_title", "test_item", "pre_conditions", "input_test_data",
                  "test_procedure", "expected_result", "remarks")


# ── G20（§C-2／P-3 之同形，25 包 A-2）—— remarks ↔ specification_reference
#
# **同一形狀已發生兩次**：
#   C-2（20 包）：18 輪之文字說「無界前基準線」而 `design_method` 欄掛 BVA
#   P-3（24 包）：`TC-072` 之 remarks 說「併列 12.3.1 與 12.6」而引用欄只有 12.3.1
# 兩次都是**改了一處而未掃同一條的其他記載**，兩次都由人工覆核才發現。
#
# 判準：`remarks` 中以「併列／引用／列」語境出現之**節號**，
# 須是 `specification_reference` 之子集；多出來者即紅。
#
# **只取「宣稱有引用」之語境**，不取所有節號 —— remarks 常需**說明某節為何
# 不列**（`TC-072` 修正後即如此），那種提及不得轉紅，
# 否則這條閘會逼人刪掉正確的說明。
SEC_RE = re.compile(r"(?<![\d.])(\d+(?:\.\d+)*)(?![\d.])")
# 宣稱引用之語境詞（其後或其前之節號視為「宣稱已列」）
CITE_CLAIM = re.compile(
    r"(併列|一併列|已列|列入引用|引用欄列|故列|列該|列於引用)")
# 明說「不列」之語境 —— 其鄰近之節號**不算宣稱引用**
NO_CITE = re.compile(r"(不列|未列|不另列|不併列|移出|屬多引|不登記)")


def _norm(t: str) -> str:
    return " ".join((t or "").split())


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

    # G17／G18 —— J-6 之雙向自檢（18 包）
    import build_batch_context as _B
    allow = _ref_allowlist()
    outline = _B._outline()
    for t in tcs:
        tid, rid = t["tc_id"], t.get("req_id", "")
        cited = [x.strip().replace(STEM + "_", "")
                 for x in str(t.get("specification_reference", "")).split("; ")]
        own = cited[0] if cited else ""
        registered = {own} | set(_B.PLP_SECTIONS if rid in _B.PLP_LEAVES
                                 else set()) | {a for a, _p, _t in allow.get(rid, [])}
        for sec in cited:
            if sec not in registered:
                out.append(f"G17 {tid}: 引用欄之 `{sec}` 未登記理由"
                           f"（非本節、非 PLP 併列、不在 REF_EXTRA）")
        # J-10：`provides` 之字面值須真的出現在該 TC 之欄位內 ——
        # **登記一個不相干的節，G17 舊版是綠的。**
        blob = _norm(" ".join(str(t.get(f, "")) for f in
                              ("tc_title", "pre_conditions", "test_procedure",
                               "expected_result", "remarks")))
        for sec, prov, tag in allow.get(rid, []):
            if sec in cited and _norm(prov) not in blob:
                out.append(f"G17 {tid}: `REF_EXTRA` 登記 `{sec}` 提供 "
                           f"「{prov[:40]}」，但該字面值不在本 TC 之欄位內"
                           f"（{tag}）")

        body = " ".join(_B.spec_body(s) or "" for s in cited)
        mc = " ".join(m["text"] for m in _B.must_carry_for(own))
        pool = _norm(body + " " + mc)
        er_raw = str(t.get("expected_result", ""))
        # ── G18 之欄位範圍（S-1，29 包）—— **擴及 `pre_conditions`，但只擴引號內**
        #
        # 28 輪之出處對照抓到 `NR1L-UserProfiles-100` 之 `“Driver 2”`
        # 溯不到 4.5.4（該節寫的是 `default Driver 1-2 Profiles`）——
        # **而 G18 當時只掃 ER，結構上看不見它。**
        #
        # 界線沿 R-3（28 包）：
        #   **引號內之字面值** → 溯源，與 ER 同標準
        #   **非引號之設置描述**（`The vehicle is stationary`、
        #   `A Driver Profile is active`）→ **不掃**
        # 全掃 pre-condition 會把每一句測試設置都判成「溯不到源」——
        # 那些本來就不是條文來的，**判它們紅是判準錯**。
        #
        # **只擴引號內，不擴未加引號之數值／狀態值**（那三段仍只掃 ER）：
        # pre-condition 之數字多為測試設置（`Two Driver Profiles`、
        # `2 memory seat buttons`），其登記機制（`TEST_SETUP_NUMERALS`）
        # 是為 ER 而設，貿然擴會產生一批只為轉綠而生的登記。
        for field, raw in (("ER", er_raw),
                           ("pre_conditions", str(t.get("pre_conditions", "")))):
            for lit in QUOTED_RE.findall(raw):
                if _norm(lit) in pool:
                    continue
                if lit.strip() in UI_LOCATORS:
                    continue
                if tid in LITERAL_EXTRA_SOURCES:
                    continue
                out.append(f"G18 {tid}: {field} 之字面值 「{lit[:48]}」 "
                           f"溯不到被引之節（{', '.join(cited)}）亦不在 must_carry")

        # J-10（19 包）—— 擴及**未加引號**之字面值。
        # 掃描前先移除：行首編號、`step N` 之互參、引號內（上面已查過）。
        body = QUOTED_RE.sub(" ", re.sub(r"^\s*\d+\.", " ", er_raw,
                                         flags=re.M))
        # `step 2`／`steps 1 and 2`／`step 1 and 2` 皆為**步驟互參**，非字面值。
        # v1 只寫 `step\s+\d+`，於是 `steps 1 and 2` 之 `2` 被當成字面值（TC-010）。
        body = re.sub(r"\bsteps?\s+\d+(?:\s*(?:and|,|-|to)\s*\d+)*",
                      " ", body, flags=re.I)
        setup_ok = (set(TEST_SETUP_NUMERALS.get(tid, []))
                    | set(METHOD_NUMERALS.get(tid, [])))
        for pu in set(re.findall(r"PU[_\s]?\d{3,4}", body)):
            if _norm(pu.replace("_", "").replace(" ", "")) not in \
                    _norm(pool).replace("_", "").replace(" ", ""):
                out.append(f"G18 {tid}: ER 之 `{pu}` 溯不到被引之節")
        for num in set(re.findall(r"(?<![\w.])\d+(?![\w.])", body)):
            if num in setup_ok or num in pool:
                continue
            out.append(f"G18 {tid}: ER 之數值 `{num}` 溯不到被引之節，"
                       f"亦未登記為測試設置（J-12）")
        # 狀態值以**大小寫不敏感**比對：spec 以散文寫（`default on small`、
        # `If turned off`），UI 以首字大寫顯示（`Small`／`Off`）。
        # **大小寫之差是呈現形式，不是字面值不同** —— 若以大小寫敏感比對，
        # 這條閘會把「spec 有寫」誤報成「溯不到」。
        pool_l = _norm(pool).lower()
        for sv in STATE_VALUES:
            if re.search(rf"\b{sv}\b", body) and sv.lower() not in pool_l:
                out.append(f"G18 {tid}: ER 之狀態值 `{sv}` 溯不到被引之節")

        # ── G19 —— 方括號須逐字溯得到來源（§11 之 profile-scoped 例外）
        for f in BRACKET_FIELDS:
            for tok in BRACKET_RE.findall(str(t.get(f, ""))):
                if _norm(tok) in pool:
                    continue
                out.append(f"G19 {tid}: {f} 之方括號 `{tok[:40]}` "
                           f"非逐字引自被引之節（{', '.join(cited)}）"
                           f"—— §11 禁方括號，例外須對照來源（D-UP22-01）")

        # ── G20 —— remarks 之「宣稱已引用」節號須在引用欄內
        rem = str(t.get("remarks", ""))
        if rem and CITE_CLAIM.search(rem):
            cited_set = {c for c in cited if c}
            for sm in SEC_RE.finditer(rem):
                sec_no = sm.group(1)
                if "." not in sec_no:
                    continue              # 純整數多為條數／編號，非節號
                # 該節號附近若有「不列」語境，視為說明而非宣稱
                lo, hi = max(0, sm.start() - 60), min(len(rem), sm.end() + 60)
                if NO_CITE.search(rem[lo:hi]):
                    continue
                if not CITE_CLAIM.search(rem[lo:hi]):
                    continue              # 不在宣稱語境內
                if sec_no not in cited_set:
                    out.append(f"G20 {tid}: remarks 稱已列 `{sec_no}`，"
                               f"而 specification_reference 為 "
                               f"{sorted(cited_set)} —— 兩處記載不一致")

    # UI 定位詞之登記表自我查核 —— **這張表不得只是宣稱**
    for lit, sec in UI_LOCATORS.items():
        if _norm(lit) not in _norm(_B.spec_body(sec) or ""):
            out.append(f"G18: UI 定位詞登記表有誤 —— 「{lit}」不在 {sec} 之 "
                       f"pdf_text 內")

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

    print("\n## G17／G18 —— J-6 之雙向自檢（18 包）\n")
    g = globals()
    stem = STEM

    def corpus_case(name, tc, expect, gate):
        nonlocal ok
        bad = [b for b in gate_corpus([tc]) if b.startswith(gate)]
        good = bool(bad) == expect
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}")
        for b in bad:
            print(f"      └ {b}")

    # G17 多引 —— TC-013 之 11.5 即此形狀（F-1）
    corpus_case("G17 注入：引用未登記之節（TC-013 之 11.5 形狀）",
                _ok_tc(req_id="SWE1-HMI-PROF-111",
                       specification_reference=f"{stem}_11.4; {stem}_11.5",
                       expected_result="1. a\n2. b"),
                True, "G17")
    # **本案例隨 J-10 更新。** 18 輪版本之 ER 為 `1. a / 2. b` —— 那時 G17 只問
    # 「有沒有登記」，故綠；J-10 加了「`provides` 之字面值須真在 TC 內」之後，
    # 同一個 fixture 會紅。**它測的性質已被擴充，不是它壞了。**
    # 補上該字面值，使其仍測「已登記之節不得轉紅」這一半。
    corpus_case("G17 範圍：REF_EXTRA 已登記之節（9.3.1）→ 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-091-01",
                       specification_reference=f"{stem}_9.3.2; {stem}_9.3.1",
                       expected_result="1. a\n2. “Function not available "
                                       "while vehicle in Motion.” is shown"),
                False, "G17")
    corpus_case("G17 範圍：PLP leaf 併列 3.x → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-001-01",
                       specification_reference="; ".join(
                           [f"{stem}_4.1"] + [f"{stem}_{x}" for x in
                                              ("3.1", "3.2", "3.3", "3.4",
                                               "3.5")]),
                       expected_result="1. a\n2. b"),
                False, "G17")

    # G18 少引 —— 5.1.1 即此形狀
    corpus_case("G18 注入：ER 之字面值溯不到被引之節",
                _ok_tc(req_id="SWE1-HMI-PROF-070",
                       specification_reference=f"{stem}_8.4.1",
                       expected_result="1. a\n2. The “All available users "
                                       "are shown on this tab” text appears"),
                True, "G18")
    corpus_case("G18 範圍：字面值確在被引之節內 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-053",
                       specification_reference=f"{stem}_6.4.1",
                       expected_result="1. a\n2. PU0585 and the “Get "
                                       "Started” button"),
                False, "G18")
    corpus_case("G18 範圍：UI 定位詞已登記 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-087",
                       specification_reference=f"{stem}_9.1.2",
                       expected_result="1. a\n2. The “Edit Profile” tab "
                                       "is displayed"),
                False, "G18")

    # 登記表自我查核之對照向：把某定位詞改成不存在之節，須紅
    _orig_loc = dict(g["UI_LOCATORS"])
    g["UI_LOCATORS"] = {"Edit Profile": "12.9"}    # 12.9 講 PIN，無此字串
    bad = [b for b in gate_corpus([_ok_tc()]) if "登記表有誤" in b]
    ok &= bool(bad)
    print(f"  {'PASS' if bad else '**FAIL**'} — "
          f"登記表說謊（Edit Profile → 12.9）→ {'紅' if bad else '綠'}")
    for b in bad:
        print(f"      └ {b}")
    g["UI_LOCATORS"] = _orig_loc

    print("\n## J-10 —— G17 之 provides 與 G18 之未加引號字面值（19 包）\n")
    stem2 = STEM
    corpus_case("G17 注入：`provides` 之字面值不在 TC 內 → 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-091-01",
                       specification_reference=f"{stem2}_9.3.2; {stem2}_9.3.1",
                       expected_result="1. a\n2. The page is displayed"),
                True, "G17")
    corpus_case("G17 範圍：`provides` 之字面值確在 TC 內 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-091-01",
                       specification_reference=f"{stem2}_9.3.2; {stem2}_9.3.1",
                       expected_result="1. a\n2. “Function not available "
                                       "while vehicle in Motion.” is shown"),
                False, "G17")
    corpus_case("G18 注入：ER 之 PU id 溯不到被引之節 → 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-053",
                       specification_reference=f"{stem2}_6.4.1",
                       expected_result="1. a\n2. PU0091 is displayed"),
                True, "G18")
    corpus_case("G18 注入：ER 之數值溯不到且未登記 → 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-053",
                       specification_reference=f"{stem2}_6.4.1",
                       expected_result="1. a\n2. 7 items are listed"),
                True, "G18")
    corpus_case("G18 範圍：`step 2`／`steps 1 and 2` 之互參不算字面值 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-053",
                       specification_reference=f"{stem2}_6.4.1",
                       expected_result="1. a\n2. The value from steps 1 and 2 "
                                       "is shown"),
                False, "G18")
    corpus_case("G18 範圍：數值已登記為測試設置（J-12）→ 綠",
                _ok_tc(tc_id="NR1L-UserProfiles-029",
                       req_id="SWE1-HMI-PROF-097",
                       specification_reference=f"{stem2}_9.5.2",
                       expected_result="1. a\n2. Memory seat 2 is linked"),
                False, "G18")
    corpus_case("G18 範圍：狀態值大小寫不同（spec `small` / UI `Small`）→ 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-100",
                       specification_reference=f"{stem2}_9.6.1",
                       expected_result="1. a\n2. The setting reads Small"),
                False, "G18")

    print("\n## G19 —— §11 方括號之對照（L-1，22 包）\n")

    # **紅向之第一形狀：自擬之 UI 標籤**（§11 立意所指者）
    corpus_case("G19 注入：procedure 以方括號標 UI 標籤（自擬）→ 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-086",
                       specification_reference=f"{stem2}_9.1.1",
                       test_procedure="1. Press [Media] on Menu Bar\n"
                                      "2. Read the line and check the username"),
                True, "G19")
    # **綠向：TC-018 之實際形狀** —— 9.1.1 原文即含 `[username]`
    corpus_case("G19 範圍：`[username]` 逐字引自 9.1.1 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-086",
                       specification_reference=f"{stem2}_9.1.1",
                       expected_result="1. a\n2. The username appears as "
                                       "“Edit username: [username]”"),
                False, "G19")
    # **本組最關鍵的一條**：同一個 token、換一個被引之節即須紅 ——
    # 證明它對照的是**來源**，不是一張 token 白名單。
    # 若日後有人把本閘改成「`[username]` 一律放行」，紅向全過而**這條會倒**。
    corpus_case("G19 注入：同一 token 但引 9.1（其原文無此 token）→ 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-085",
                       specification_reference=f"{stem2}_9.1",
                       expected_result="1. a\n2. The username appears as "
                                       "“Edit username: [username]”"),
                True, "G19")
    # 紅向之第二形狀：§11 所保留之 placeholder 語法本身漏進輸出欄位
    corpus_case("G19 注入：tc_title 含 §4.3 之 placeholder 語法 → 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-086",
                       specification_reference=f"{stem2}_9.1.1",
                       tc_title="[Outcome] when [trigger]"),
                True, "G19")
    # 綠向：spec 自身之方括號註記（11.4 之 `[This whole note ...]`）
    corpus_case("G19 範圍：remarks 照錄 11.4 原文之方括號註記 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-111",
                       specification_reference=f"{stem2}_11.4",
                       remarks="條文首句為 [This whole note is not applicable "
                               "for R1 H]，故本 TC 排除該變體"),
                False, "G19")

    print("\n## G18 之 pre_conditions 擴掃（S-1，29 包）\n")

    # **紅向即 `TC-100` 於 28 輪修正前之原形**：4.5.4 寫的是
    # `default Driver 1-2 Profiles`，`Driver 2` 單獨出現在 4.5.1。
    corpus_case("G18 注入：pre 之 `“Driver 2”` 引 4.5.4（該節無此字面值）→ 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-012",
                       specification_reference=f"{stem2}_4.5.4",
                       pre_conditions="1. The vehicle has 2 memory seat "
                                      "buttons with default “Driver 2” Profiles",
                       expected_result="1. a\n2. b"),
                True, "G18")
    # **綠向即其修正後之形**：改用**本節自己的寫法**，不去引 4.5.1（S-2 之判例）
    corpus_case("G18 範圍：pre 改用本節寫法 `“Driver 1-2”` → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-012",
                       specification_reference=f"{stem2}_4.5.4",
                       pre_conditions="1. The vehicle has the default "
                                      "“Driver 1-2” Profiles",
                       expected_result="1. a\n2. b"),
                False, "G18")
    # **護欄** —— 非引號之設置描述**不得**因本次擴掃而轉紅。
    # 若這條倒了，代表擴掃溢出到「凡 pre-condition 皆須溯源」，
    # 那會把每一句測試設置都判紅（S-1 明文禁止之情形）。
    corpus_case("**護欄**：pre 之非引號設置描述（stationary／active／two Profiles）→ 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-012",
                       specification_reference=f"{stem2}_4.5.4",
                       pre_conditions="1. Two Driver Profiles exist on the "
                                      "vehicle\n2. The vehicle is stationary\n"
                                      "3. A Driver Profile is active",
                       expected_result="1. a\n2. b"),
                False, "G18")
    # 綠向：pre 之 UI 定位詞經登記表溯源（語料中 7 條為此形）
    corpus_case("G18 範圍：pre 之 `“Edit Profile”` 由 `UI_LOCATORS` 溯源 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-012",
                       specification_reference=f"{stem2}_4.5.4",
                       pre_conditions="1. The “Edit Profile” tab is available",
                       expected_result="1. a\n2. b"),
                False, "G18")

    print("\n## G20 —— remarks ↔ specification_reference（A-2，25 包）\n")

    # **紅向即 P-3 之原形**（`TC-072` 於 24 包修正前之 remarks）
    corpus_case("G20 注入：remarks 稱「併列 12.3.1 與 12.6」而引用欄只有 12.3.1 → 紅",
                _ok_tc(req_id="SWE1-HMI-PROF-134",
                       specification_reference=f"{stem2}_14.1; {stem2}_12.3.1",
                       expected_result="1. a\n2. b",
                       remarks="複位後為 12.3.1（同一 PIN 退出）與 12.6"
                               "（停用詢問），故併列該二節"),
                True, "G20")
    # **綠向即其修正後之形**：說明某節**為何不列** —— 不得轉紅，
    # 否則這條閘會逼人刪掉正確的說明。
    corpus_case("G20 範圍：remarks 說明 12.6 **不列**之理由 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-134",
                       specification_reference=f"{stem2}_14.1; {stem2}_12.3.1",
                       expected_result="1. a\n2. b",
                       remarks="複位後為 12.3.1 與 12.6 兩處。引用欄不列 12.6："
                               "其字面值不在本 TC 內，列之即屬多引"),
                False, "G20")
    # 綠向：宣稱併列，而引用欄確實含之
    corpus_case("G20 範圍：宣稱併列且引用欄確實含該節 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-134",
                       specification_reference=f"{stem2}_14.1; {stem2}_12.3.1",
                       expected_result="1. a\n2. b",
                       remarks="其指涉對象複位後為 12.3.1，故併列該節"),
                False, "G20")
    # 綠向：remarks 只是提到節號，無宣稱語境（多數 TC 之常態）
    corpus_case("G20 範圍：remarks 提及節號但無「已引用」之宣稱 → 綠",
                _ok_tc(req_id="SWE1-HMI-PROF-134",
                       specification_reference=f"{stem2}_14.1",
                       expected_result="1. a\n2. b",
                       remarks="本節之行為與 12.6 之詢問 popup 屬不同觸發"),
                False, "G20")

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

    n = 1 + len(cases) + len(scope) + 22 + 5 + 4 + 4   # +5 G19（22）／+4 G20（25）／+4 G18-pre（29）
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    sys.exit(self_test() if a.self_test else run_corpus())
