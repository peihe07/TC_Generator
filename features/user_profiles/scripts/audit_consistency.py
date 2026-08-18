#!/usr/bin/env python3
"""記載一致性與指代之稽核（21 包 K-3／K-4）。

## 為什麼不是 lint 的閘

lint 之閘要能給出「紅／綠」之判定；本檔之三項掃描**產出的是待判清單** ——
命中不等於錯（`the message specified above` 之內容可能已由別節之逐字引用補上；
`Scenario` 之步數判準對某些流程本來就寬）。
**把待判清單做成閘，會逼人為了轉綠而改對的東西。**

## 三項

| # | 掃描 | 依據 |
|---|---|---|
| K-3 | ER 以**指代詞**引用表格內容而其後無 `a./b./c.` 列舉 | D-3（14 輪）、C-1（20 輪）之同型 |
| K-4a | `design_method` ↔ `input_test_data`／procedure 之實際形態 | C-2（20 輪）之記載矛盾 |
| K-4b | `priority` ↔ `priority_basis` 之措辭 | C-5（20 輪）|

## K-3 之盲區（R-G11，**下放包已先聲明**）

本掃描抓**指代詞**。抓不到「以自然語句概括表格內容而未用指代詞」者 ——
**C-1 之原句 `followed by the applicable examples` 正屬此型**：
`examples` 是複數名詞，句中無 `the rows of`／`described in` 之類。
故掃描結果為**下界**，另以「複數名詞 + 無列舉」之形態人工複讀補足（見 `--plural`）。

Usage:
    python3 scripts/audit_consistency.py            # 三項全跑
    python3 scripts/audit_consistency.py --plural   # K-3 之盲區補足清單
    python3 scripts/audit_consistency.py --self-test  # 方向性案例（R-G7）

## 為什麼需要 `--self-test`（21 輪 §6 第 7 項之自陳缺口）

三項掃描目前皆以「0 處」收尾。**一個永遠 0 處的掃描與一個壞掉的掃描，輸出相同** ——
語料全綠時，掃描本身是死是活看不出來。故每項各備紅／綠兩向案例，
其中**紅向優先取本 feature 真實出現過的形狀**：C-1 之原句（`--plural` 須紅）、
C-5 之 P1 basis 寫「非主路徑分支」（K-4b 須紅）、
TC-047 之無非法操作（K-4a 須紅）；綠向取**曾被誤判為紅者**：
TC-017 之行內逗號列舉、TC-022 之非法性顯示在 ER、
P0 之 basis 寫「防護本身」（v1 因詞表不全而誤紅）。
"""

import argparse
import json
import re
import sys
from pathlib import Path

FEATURE = Path(__file__).resolve().parent.parent

# K-3 —— 指代詞
DEIXIS = re.compile(
    r"\b(the rows? of|the items? in|the info in|the list of|described in|"
    r"specified in|as (?:described|specified|shown) above|listed (?:above|in)|"
    r"the chart|the table)\b", re.I)
SUBLIST = re.compile(r"^\s+[a-z]\.\s", re.M)
# **判準改過一次（R-U37）。** v1 只認 `a./b./c.` 子層 —— 而 TC-017 之列舉是
# **行內逗號分隔**（`Resume Setup, Edit Name, Edit Avatar, …`）。
# 那是已列舉，不是指代。v2：同一 ER 內有 ≥3 個逗號分隔項亦視為已列舉。
INLINE_LIST = re.compile(r"(?:[^,\n]+,){3,}")

# K-3 之盲區補足：複數名詞而無列舉
PLURAL_VAGUE = re.compile(
    r"\b(the applicable \w+|the relevant \w+|the corresponding \w+|"
    r"\w+ examples|the (?:other )?(?:options|items|entries|examples|"
    r"categories|sections))\b", re.I)

# K-4a —— design_method 之形態要求
FORM_RULES = {
    "邊界值分析": ("邊界對（limit 與 limit±1，或界前／界上兩讀）",
                   lambda tc: bool(re.search(r"\d+\s*(?:→|->|,|s|min|"
                                             r"characters|attempts)?\s*(?:→|->|,)",
                                             tc["input_test_data"]))
                   or "→" in tc["input_test_data"]),
    "狀態轉換": ("A→B 之狀態變化（procedure 內有造成狀態改變之步驟）",
                 lambda tc: bool(re.search(
                     r"\b(bring the vehicle into motion|activate|deactivate|"
                     r"exit|switch the ignition|disconnect|select memory seat|"
                     r"swap)\b", tc["test_procedure"], re.I))),
    # v1 只掃 procedure 之關鍵詞，漏掉「選取一個已鎖定之項目」這種寫法
    # （TC-022 之 `Select the greyed-out “Delete Profile” item`、
    #  TC-057 之 `Select Device Manager`）—— 動作本身讀不出它非法，
    # **非法性顯示在 ER**（不被接受／被鎖住）。v2 兩邊都看。
    "負向測試": ("無效輸入或非法操作（procedure 之嘗試，或 ER 明載其被擋）",
                 lambda tc: bool(re.search(
                     r"\b(attempt|greyed|incorrect|differs|other than)\b",
                     tc["test_procedure"], re.I))
                 or bool(re.search(
                     r"\b(not accepted|does not respond|is blocked|"
                     r"locked out|cannot be opened|not available|"
                     r"is not accessible)\b", tc["expected_result"], re.I))),
    "情境 / 用例": ("≥3 步或跨 ≥3 功能",
                    lambda tc: len([x for x in tc["test_procedure"].splitlines()
                                    if x.strip()]) >= 3),
    "基礎故障注入": ("注入之故障（input_test_data 或 procedure 明載）",
                     lambda tc: "Fault injected" in tc["input_test_data"]
                     or bool(re.search(r"\b(disconnect|withhold)\b",
                                       tc["test_procedure"], re.I))),
}

# K-4b —— **判準改過一次（R-U37）。**
#
# v1 驗「該級之 basis 是否含該級之關鍵詞」—— 那測的是**用字是否落在我列的詞表裡**，
# 於是 13 條轉紅，其中絕大多數只是我的詞表不夠（`防護本身` 不在 P0 詞表裡，
# `開啟`／`落點` 不在 P2 詞表裡）。**詞表不全不等於記載矛盾。**
#
# C-5 要抓的是**相斥**：basis 用了**別級**之措辭
# （P1 之 basis 寫「非主路徑分支」而條文說 `will always be displayed`）。
# v2：只在 basis 出現**低於本級**之定性詞時轉紅。
LOWER_BAND_WORDS = {
    "P0": re.compile(r"呈現層|回饋|提示音|輔助功能|細節|罕用"),
    "P1": re.compile(r"呈現層|罕用|版面上限"),
    "P2": re.compile(r"核心五類|防線本身|資料遺失風險"),
    "P3": re.compile(r"核心五類|防線本身|資料遺失風險|邊界"),
}


def tcs() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append((d["outline"], t))
    return sorted(out, key=lambda x: x[1]["tc_id"])


def k3(rows) -> list:
    hits = []
    for sec, t in rows:
        er = t["expected_result"]
        for m in DEIXIS.finditer(er):
            if SUBLIST.search(er) or INLINE_LIST.search(er):
                continue          # 已有 a./b./c. 子層或行內逗號列舉
            hits.append((t["tc_id"], sec, m.group(0),
                         er[max(0, m.start() - 50):m.end() + 50]
                         .replace("\n", " ")))
    return hits


def k3_plural(rows) -> list:
    hits = []
    for sec, t in rows:
        er = t["expected_result"]
        if SUBLIST.search(er):
            continue
        for m in PLURAL_VAGUE.finditer(er):
            hits.append((t["tc_id"], sec, m.group(0),
                         er[max(0, m.start() - 50):m.end() + 50]
                         .replace("\n", " ")))
    return hits


def k4a(rows) -> list:
    bad = []
    for sec, t in rows:
        key = t["design_method"].split(" (")[0]
        rule = FORM_RULES.get(key)
        if rule and not rule[1](t):
            bad.append((t["tc_id"], sec, key, rule[0]))
    return bad


def k4b(rows) -> list:
    bad = []
    for sec, t in rows:
        pat = LOWER_BAND_WORDS.get(t["priority"])
        m = pat.search(t.get("priority_basis", "")) if pat else None
        if m:
            bad.append((t["tc_id"], sec, t["priority"],
                        f"basis 用了低於本級之措辭「{m.group(0)}」："
                        + t.get("priority_basis", "")[:50]))
    return bad


# ---------------------------------------------------------------- 方向性案例
#
# 每案 = (說明, 掃描名, 假 TC, 期望紅?)。**紅向取本 feature 真實出現過之形狀，
# 綠向取曾被誤判為紅者** —— 後者即兩次判準修正（R-U37）之回歸。

def _tc(**kw) -> dict:
    base = {
        "tc_id": "FAKE-000", "expected_result": "1. NA", "test_procedure": "1. NA",
        "input_test_data": "NA", "design_method": "功能測試 (Functional based ; no specific technique)",
        "priority": "P2", "priority_basis": "呈現層",
    }
    base.update(kw)
    return base


SELF_CASES = [
    # ---- K-3：指代詞而其後無列舉
    ("D-3／C-1 之同型：ER 指代一張表而未列舉 → **須紅**", "k3",
     _tc(expected_result="1. The page is displayed\n2. The categories described in "
                         "the table above are shown"), True),
    ("**TC-017 之形狀**：行內逗號列舉（v1 誤判為指代）→ **須綠**", "k3",
     _tc(expected_result="1. The tab is displayed\n2. The options are listed in the "
                         "Table EDPR1 order: Resume Setup, Edit Name, Edit Avatar, "
                         "Connected Account, Memory Seat, Welcome Pop Up"), False),
    ("已以 §6.1 子層逐列補上（現行 TC-039 之形狀）→ **須綠**", "k3",
     _tc(expected_result="2. The rows of Table PIP1 are shown:\n   a. Screen "
                         "Customization\n   b. Apps\n   c. Media"), False),

    # ---- K-3 盲區補足：複數名詞而無列舉
    ("**C-1 之原句**（無指代詞，故 k3 抓不到）→ `--plural` **須紅**", "k3_plural",
     _tc(expected_result="2. The page reads the intro text followed by the applicable "
                         "examples"), True),
    ("同句已補子層列舉 → **須綠**", "k3_plural",
     _tc(expected_result="2. The applicable examples are shown:\n   a. Screen "
                         "Customization\n   b. Apps"), False),

    # ---- K-4a：design_method ↔ 實際形態
    ("**TC-036 之形狀**：BVA 而 input 只有 limit、無 limit±1 → **須紅**", "k4a",
     _tc(design_method="邊界值分析 (Boundary Value Analysis)",
         input_test_data="Line count per page: 6 (limit)"), True),
    ("BVA 且有邊界對（TC-008 之形狀）→ **須綠**", "k4a",
     _tc(design_method="邊界值分析 (Boundary Value Analysis)",
         input_test_data="Timeout: 29 s → 30 s"), False),
    ("**TC-047 之形狀**：負向而 procedure 與 ER 皆無非法操作 → **須紅**", "k4a",
     _tc(design_method="負向測試 (Negative Testing)",
         test_procedure="1. Open the Profile section\n2. Read the option list",
         expected_result="1. The tab is displayed\n2. No Valet control is shown"), True),
    ("**TC-022 之形狀**：非法性顯示在 **ER** 而非 procedure（v1 誤判為紅）→ **須綠**",
     "k4a",
     _tc(design_method="負向測試 (Negative Testing)",
         test_procedure="1. Select the greyed-out “Delete Profile” item",
         expected_result="1. The selection is not accepted"), False),
    ("狀態轉換而 procedure 無造成狀態改變之步驟 → **須紅**", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Read the screen\n2. Check the label"), True),
    ("狀態轉換且有 A→B（TC-021 之形狀）→ **須綠**", "k4a",
     _tc(design_method="狀態轉換 (State Transition Testing)",
         test_procedure="1. Read the list\n2. Bring the vehicle into motion\n"
                        "3. Read the list"), False),
    ("情境／用例而只有 2 步 → **須紅**", "k4a",
     _tc(design_method="情境 / 用例 (Scenario / Use Case)",
         test_procedure="1. Open the tab\n2. Read the screen"), True),
    ("基礎故障注入而未載注入之故障 → **須紅**", "k4a",
     _tc(design_method="基礎故障注入 (Fault Injection)",
         test_procedure="1. Open the tab\n2. Read the screen",
         input_test_data="NA"), True),

    # ---- K-4b：priority ↔ priority_basis 之措辭（測**相斥**，非詞表命中）
    ("**C-5 之形狀**：P1 之 basis 寫「呈現層」→ **須紅**", "k4b",
     _tc(priority="P1", priority_basis="連網配置之呈現層細節"), True),
    ("P0 之 basis 寫「輔助功能」→ **須紅**", "k4b",
     _tc(priority="P0", priority_basis="輔助功能之提示音"), True),
    ("P2 之 basis 寫「核心五類」→ **須紅**（反向：高於本級亦相斥）", "k4b",
     _tc(priority="P2", priority_basis="R-U5 核心五類之一"), True),
    ("**v1 之誤判**：P0 之 basis 寫「防護本身」（詞表無此詞）→ **須綠**", "k4b",
     _tc(priority="P0", priority_basis="啟用之 PIN —— Valet Mode 之防護本身"), False),
    ("P2 之 basis 寫「呈現層」（本級措辭）→ **須綠**", "k4b",
     _tc(priority="P2", priority_basis="變灰之外觀 —— 呈現層"), False),
]

SCANS = {"k3": k3, "k3_plural": k3_plural, "k4a": k4a, "k4b": k4b}


def self_test() -> int:
    ok = 0
    for desc, scan, tc, want_red in SELF_CASES:
        got = SCANS[scan]([("0.0", tc)])
        red = bool(got)
        mark = "PASS" if red == want_red else "**FAIL**"
        ok += red == want_red
        print(f"  {mark} — [{scan}] {desc}: "
              f"{'紅' if red else '綠'}，期望 {'紅' if want_red else '綠'}")
        if red != want_red:
            print(f"      └ 實得 {got}")
    print(f"\n{ok} / {len(SELF_CASES)} directional cases "
          f"{'PASS' if ok == len(SELF_CASES) else 'FAIL'}")
    return 0 if ok == len(SELF_CASES) else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--plural", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()

    if a.self_test:
        sys.exit(self_test())

    rows = tcs()
    print(f"語料 {len(rows)} 條\n")

    if a.plural:
        h = k3_plural(rows)
        print(f"## K-3 盲區補足 —— 複數名詞而無列舉：{len(h)} 處\n")
        for tid, sec, w, ctx in h:
            print(f"  {tid} ({sec}) 「{w}」 … {ctx.strip()[:100]}")
        sys.exit(0)

    h = k3(rows)
    print(f"## K-3 —— 指代詞而其後無列舉：{len(h)} 處\n")
    for tid, sec, w, ctx in h:
        print(f"  {tid} ({sec}) 「{w}」 … {ctx.strip()[:100]}")

    b = k4a(rows)
    print(f"\n## K-4a —— design_method ↔ 實際形態：{len(b)} 處待判\n")
    for tid, sec, key, want in b:
        print(f"  {tid} ({sec}) {key} —— 缺 {want}")

    c = k4b(rows)
    print(f"\n## K-4b —— priority ↔ priority_basis 之措辭：{len(c)} 處待判\n")
    for tid, sec, pri, msg in c:
        print(f"  {tid} ({sec}) {pri} —— {msg}")
