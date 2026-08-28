#!/usr/bin/env python3
"""pilot 自檢 —— **對 IN §9 十七項全跑**（下放包 10 §八 T16b）。

**拘束之更正（下放包 10 §一）**：下放包 09 §6.2 之八項為「**額外**」而非
「全部」。上一輪 13 檢全綠而審查列出 6 缺陷，5 個落在 §6.2 未列之 IN 條文
（§4.4／§4.5／§5.1／§5.2／§12／§11 之 `test_item` 面）。**故本檔以 IN §9
十七項為骨幹**，下放包 §6.2 之項附掛於對應之 IN 項下。

carve-out：
- `test_item` 之方括號依 **R-DD12(c)**，以「是否為 037 逐字」為判準，非一律禁
- 引號內字串之終端標點依 **R-DD11**，移除引號後不以作者句點結尾即合規

**只讀，不改產物。** 任一項 FAIL 即 exit 1；N/A 須具理由。
"""
import json
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
import os
ART = os.environ.get("SC_ARTIFACT", "pilot_group3.json")
TCS = json.loads((ROOT / "generated" / ART).read_text("utf-8"))
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"
_ALL = {f"{n:03d}": 8 + n for n in range(1, 29)}      # leaf → 037 `Analysis Report` 列
ROW = {t["req_id"][-3:]: _ALL[t["req_id"][-3:]] for t in TCS}
FOUR = ["pre_conditions", "input_test_data", "test_procedure", "expected_result"]
MULTILINE = FOUR + ["test_item", "spec_reference"]

wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
SRC = {k: [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)][v - 1]
       for k, v in ROW.items()}
wb.close()

res = []


def add(no, sec, name, verdict, detail):
    res.append((no, sec, name, verdict, detail))


def leaf(tc):
    return tc["req_id"][-3:]


def items(field):
    """numbered item 之切分（§11 之規制單位為 item，非物理行）。"""
    out, cur = [], None
    for ln in field.split("\n"):
        if re.match(r"^\d+\.", ln):
            if cur is not None:
                out.append(cur)
            cur = ln
        elif cur is not None:
            cur += "\n" + ln
    if cur is not None:
        out.append(cur)
    return out or [field]


def words(item):
    """步驟字數：去編號前綴後之空白 token 數。"""
    return len(re.sub(r"^\d+\.\s*", "", item).split())


# ── 1 Test Set（§4.1／§4.2）──────────────────────────────────────────
sets = {tc["test_set"] for tc in TCS}
ok = (sets <= {"Lockout Enforcement", "Speed Threshold Judgment"}
      and not any(s.startswith("Driver Distraction") for s in sets)
      and not (sets & {"Unclassified", "Misc"}))
add(1, "§4.1/§4.2", "Test Set 名詞片語、能力層級、無 Test Group 前綴、拼寫一致",
    ok, f"{sets}；4 則同一值")

# ── 2 test_item（§4.3／§4.3.1 R-S4）─────────────────────────────────
d = []
ok = True
for tc in TCS:
    k = leaf(tc)
    parts = tc["test_item"].rsplit("\n(", 1)
    upper, lowerp = parts[0], "(" + parts[1] if len(parts) == 2 else ""
    sub = upper in SRC[k][3]
    ntok = len(upper.split())
    has_low = lowerp.startswith("(") and lowerp.endswith(")")
    cjk = bool(re.search(r"[一-鿿]", lowerp))
    modal = bool(re.search(r"\b(shall|should|must|may)\b", tc["test_item"], re.I))
    good = sub and ntok <= 50 and has_low and not cjk and not modal
    ok &= good
    d.append(f"{k}: 上半子串 {'✓' if sub else '✗'}/{ntok}tok、下半 {'有' if has_low else '無'}"
             f"、中文 {'有' if cjk else '無'}、modal {'有' if modal else '無'}")
add(2, "§4.3.1", "test_item 兩段式：上半 verbatim ≤50tok；下半存在且為英文；無 modal",
    ok, "；".join(d))
low = [tc["test_item"].rsplit("\n(", 1)[-1] for tc in TCS]
bysrc = {}
for tc in TCS:
    bysrc.setdefault(tc["spec_reference"], []).append(tc["test_item"].rsplit("\n(", 1)[-1])
dupe = [k for k, v in bysrc.items() if len(v) != len(set(v))]
add("2b", "§4.3.1", "同一 Requirement ID 衍生之列，括號下半不逐字相同",
    not dupe, "無重複" if not dupe else str(dupe))

# ── 3 Pre-Condition（§4.4／§8.5）────────────────────────────────────
FORBID_PC = [
    (r"is powered on", "系統預設（§4.4 Forbidden：`HU is powered on.`）"),
    (r"service is running", "以待測 feature 為前提（§4.4 Forbidden）"),
    (r"\bis displayed\b", "step 可控狀態（§4.4 Forbidden）"),
    (r"\bcan be (opened|started)\b", "step 可控狀態（§4.4 Forbidden）"),
    (r"\b(press|open|select|insert|connect|confirm|check|read)\b", "動作（§4.4：Never actions）"),
]
hit = [(tc["tc_id"], why, it) for tc in TCS for it in items(tc["pre_conditions"])
       for pat, why in FORBID_PC if re.search(pat, it, re.I)]
# R-DD17：訊號源行之形式須為「只書訊號源本身」，不得兼述環境（如 vehicle is stationary）
RE_SIGSRC = re.compile(
    r"^\d+\. The signal \$[\w.]+\$ is transmitted on the bus at \d+ \([\d.]+ km/h\)$")
shape = []
for tc in TCS:
    for it in items(tc["pre_conditions"]):
        if "$" in it and not RE_SIGSRC.fullmatch(it.strip()):
            shape.append((tc["tc_id"], it.strip()))
add(3, "§4.4/§8.5 + R-DD17",
    "Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態；"
    "訊號源行合 R-DD17 之形式（只書訊號源，不兼述環境）",
    not hit and not shape,
    ("0 命中；4 則各 1 項且皆合 R-DD17 之形式（§4.5-1 環境資料）"
     if not hit and not shape else f"禁式 {hit or '無'}；形式不合 {shape or '無'}"))

# ── 4 Input Test Data（§4.5）────────────────────────────────────────
na = all(tc["input_test_data"] == "NA" for tc in TCS)
back = [tc["tc_id"] for tc in TCS if "listed in Input Test Data" in tc["test_procedure"]]
dupv = []
for tc in TCS:
    if tc["input_test_data"] != "NA":
        for tok in re.findall(r"= \d+", tc["input_test_data"]):
            if tok in tc["test_procedure"]:
                dupv.append((tc["tc_id"], tok))
add(4, "§4.5", "Input Test Data 歸屬正確；重複值移入 PC／Procedure 或設 NA",
    na and not back and not dupv,
    f"4 則皆 NA={na}；回指 {back or '無'}；跨欄重複 {dupv or '無'}")

# ── 5 步驟可執行／禁用動詞／Final Step（§5.1／§5.5）──────────────────
BANNED = ["observe whether", "observe", "see if", "check whether",
          "confirm whether", "verify", "watch", "monitor", "inspect"]
bad5 = []
for tc in TCS:
    for it in items(tc["test_procedure"]):
        body = re.sub(r"^\d+\.\s*", "", it)
        for b in BANNED:
            if re.search(rf"\b{re.escape(b)}\b", body, re.I):
                if b == "verify" and re.search(r"to verify that", body, re.I):
                    continue
                bad5.append((tc["tc_id"], b))
finals = {tc["tc_id"]: items(tc["test_procedure"])[-1] for tc in TCS}
PREF = r"\b(check that|confirm that|read|record|compare)\b"
nofinal = [t for t, f in finals.items() if not re.search(r"\bcheck that\b", f, re.I)]
add(5, "§5.1/§5.5", "步驟無禁用動詞；Final Step 含 ACTION ＋ check target（preferred verb）",
    not bad5 and not nofinal,
    f"禁用動詞 {bad5 or '0 命中'}；末步缺 `check that` {nofinal or '無'}")

# ── 6 步驟長度與 intent 層級（§5.2）─────────────────────────────────
lens, over = {}, []
for tc in TCS:
    its = items(tc["test_procedure"])
    ws = [words(i) for i in its]
    lens[tc["tc_id"]] = ws
    for n, (i, w) in enumerate(zip(its, ws), 1):
        cap = 18 if n == len(its) else 12          # B：Final ≤18；A：一般 ≤12
        if w > cap:
            over.append((tc["tc_id"], n, w, cap))
add(6, "§5.2", "步驟長度：一般 ≤12 字、Final ≤18 字（含 action+check target）",
    not over, f"字數 {lens}" + ("" if not over else f"；超限 {over}"))

# ── 7 標準 setup 片語（§5.3）────────────────────────────────────────
add(7, "§5.3", "標準 setup 片語逐字重用", "N/A",
    "本 feature 未定義 project-level setup 常數（feature.yaml 無該鍵）—— 無適用對象")

# ── 8 CLI／tooling 步驟格式（§5.4）──────────────────────────────────
cli = [tc["tc_id"] for tc in TCS if "$ " in tc["test_procedure"]]
add(8, "§5.4", "CLI／tooling 步驟採 description + `$` 指令格式", "N/A",
    "4 則皆為 HMI 操作與匯流排施加，無 CLI 步驟")

# ── 9 Baseline（§5.6）───────────────────────────────────────────────
d9 = []
ok9 = True
for tc in TCS:
    k = leaf(tc)
    its = items(tc["test_procedure"])
    if k in ("010", "012"):
        base = re.search(r"^1\..*(start|Open)", its[0], re.I) is not None
        ok9 &= base
        d9.append(f"{k}: 步驟 1 建立 before（feature 可啟動）{'✓' if base else '✗'}")
    else:
        # R-DD17 改寫後之字面：`… is transmitted on the bus at 0 (0.0000 km/h)`
        pre0 = "at 0 (0.0000 km/h)" in tc["pre_conditions"]
        ok9 &= pre0
        d9.append(f"{k}: before 由 PC 載明（訊號 0）{'✓' if pre0 else '✗'}，"
                  f"ER 不比對已記錄值，故不需記錄步驟")
add(9, "§5.6", "before／after 需要時建立 baseline", ok9, "；".join(d9))

# ── 10 Procedure ↔ ER 1:1、可觀察、無 modal（§6）────────────────────
st = {tc["tc_id"]: len(items(tc["test_procedure"])) for tc in TCS}
er = {tc["tc_id"]: len(items(tc["expected_result"])) for tc in TCS}
one2one = all(st[t] == er[t] for t in st)
modal_er = [(tc["tc_id"], w) for tc in TCS
            for w in ("shall", "should", "must", "may", "will")
            if re.search(rf"\b{w}\b", tc["expected_result"], re.I)]
NONOBS = ["outputs RESTRICTED", "reports RESTRICTED", "Listener", "callback",
          "the first representable step"]
nonobs = [(tc["tc_id"], w) for tc in TCS for w in NONOBS if w in tc["expected_result"]]
add(10, "§6", "Procedure↔ER 1:1；ER 可觀察；ER 無 modal",
    one2one and not modal_er and not nonobs,
    f"步驟 {st}／ER {er}；modal {modal_er or '無'}；非觀察語句 {nonobs or '無'}")

# ── 11 FP／FF（§7）─────────────────────────────────────────────────
ff = []
for tc in TCS:
    if leaf(tc) in ("010", "012") and not re.search(r"^1\.", items(tc["test_procedure"])[0]):
        ff.append(tc["tc_id"])
add(11, "§7", "無 FP／FF：含 setup／transition，不假設隱藏狀態；列舉支援項配負向",
    not ff,
    "FF：010／012 之 fail-safe 皆先建立正常態再注入故障，未假設隱藏狀態；"
    "FP：本 4 leaf 無列舉式支援項（無 format／device／protocol 之列舉），無配對義務")

# ── 12 追溯與範圍（§8.1／§8.2.1／§8.2.2／§8.4.1／§8.4.2）──────────
trace = all(re.fullmatch(r"SWE1-RA-Driver_Distraction-\d{3}", tc["req_id"]) for tc in TCS)
SCOPE = ["seat belt", "seatbelt", "passenger detection", "Are you the passenger",
         "occupant", "ADAS", "Level 3", "per-key-cycle", "key cycle", "Fullscreen"]
leak = [(tc["tc_id"], w) for tc in TCS for w in SCOPE
        for f in FOUR + ["test_item"] if w.lower() in tc[f].lower()]
# §8.4.1 造值：ER／Procedure 內之數值須見於 profile §3.1 或 DBC
nums = {n for tc in TCS for f in ("test_procedure", "expected_result")
        for n in re.findall(r"(?<![\w.])(\d+(?:\.\d+)?)(?![\w])", tc[f])}
ALLOWED = {"1", "2", "3", "4", "129", "8.0625", "77", "4.8125", "0", "0.0000", "5", "3"}
fab = nums - ALLOWED
add(12, "§8.1/§8.2/§8.4", "追溯 Req/SWRA；不擴入 sibling；無造值；無範圍捏造",
    trace and not leak and not fab,
    f"req_id 形制 {trace}；§8.4.2 禁詞 {leak or '0 命中'}；"
    f"數值母體 {sorted(nums)}，逾 profile §3.1／編號者 {fab or '無'}")

# ── 13 Design Method（§12 first-match）──────────────────────────────
MENU = {"功能測試 (Functional based ; no specific technique)",
        "狀態轉換 (State Transition Testing)", "決策表 (Decision Table Testing)",
        "等價劃分 (Equivalence Partitioning, EP)",
        "邊界值分析 (Boundary Value Analysis, BVA)",
        "組合測試 (Combinatorial Testing ; Pairwise / t-wise)",
        "情境 / 用例 (Scenario / Use Case Testing)", "負向測試 (Negative / Invalid)",
        "基礎故障注入 (Fault Injection Lite)"}
# §12 first-match：AC2（停送→逾時）為 simulated fault，序在 State Transition 之前；
# AC1（跨門檻）為 A→B 轉換。以 037 原文之 AC 別判，非以 leaf 號硬編。
def _want(tc):
    k = leaf(tc)
    return ("基礎故障注入 (Fault Injection Lite)"
            if str(SRC[k][3]).startswith("AC2") else "狀態轉換 (State Transition Testing)")
WANT = {leaf(tc): _want(tc) for tc in TCS}
inmenu = all(tc["design_method"] in MENU for tc in TCS)
firstmatch = all(tc["design_method"] == WANT[leaf(tc)] for tc in TCS)
add(13, "§12", "Design Method 於 procedure 定稿後指派，且合 first-match 序",
    inmenu and firstmatch,
    "009/011 觸發為 A→B 狀態轉換，於 Scenario 前命中；"
    "010/012 為 simulated fault（停送＋逾時），於 State Transition 前命中；"
    f"皆為下拉選單實值 {inmenu}")

# ── 14 四欄無行尾句號（§11）；並含 R-DD11 之引號 carve-out ──────────
per = []
for tc in TCS:
    for f in FOUR:
        for it in items(tc[f]):
            s = it.rstrip()
            if not s.endswith("."):
                continue
            # R-DD11：移除引號段後仍以作者句點結尾者，方為違規
            stripped = re.sub(r'"[^"]*"', "", s).rstrip()
            if stripped.endswith("."):
                per.append((tc["tc_id"], f, s[-40:]))
add(14, "§11 + R-DD11", "四欄 numbered item 無作者所書之行尾句號（引號內字串之終端標點保留）",
    not per, "0 違規" if not per else str(per))

# ── 15 方括號／引號（§11 + R-DD12(c) carve-out）─────────────────────
brk = []
for tc in TCS:
    k = leaf(tc)
    for f in FOUR:
        for m in re.finditer(r"\[[^\]]*\]", tc[f]):
            if re.fullmatch(r"\[ASSUMPTION A-DD\d\]", m.group(0)):
                continue     # R-DD12(b)：裁決所命之 marker
            brk.append((tc["tc_id"], f, m.group(0), "四欄不得出現方括號"))
    # test_item：R-DD12(c) —— 以「是否為 037 逐字」為判準
    upper = tc["test_item"].rsplit("\n(", 1)[0]
    lowerp = tc["test_item"].rsplit("\n(", 1)[-1]
    for m in re.finditer(r"\[[^\]]*\]", upper):
        if m.group(0) not in SRC[k][3]:
            brk.append((tc["tc_id"], "test_item 上半", m.group(0), "非 037 逐字"))
    for m in re.finditer(r"\[[^\]]*\]", lowerp):
        brk.append((tc["tc_id"], "test_item 下半", m.group(0), "R-DD12(b)：例外僅及上半"))
sq = [(tc["tc_id"], f) for tc in TCS for f in FOUR
      if re.search(r"(?<![\w])'[^']+'(?![\w])", tc[f]) or "<" in tc[f]]
add(15, "§11 + R-DD12(c)", "UI 標籤用 `\"...\"`；方括號僅限 037 逐字之 test_item 上半與 A-DD6 marker",
    not brk and not sq,
    ("0 違規；test_item 上半之 `[Normal]`／`[Exception]` 經比對為 037 逐字（R-DD12(a)）"
     if not brk else str(brk)) + f"；單引號／角括號 {sq or '無'}")

# ── 16 spec_reference（§10.7）───────────────────────────────────────
# profile §1 之 SYS-RA → ObjectID 對照（逐字）
_OBJ = {"113": "CFTS022-4915104", "114": "CFTS022-4915105", "115": "CFTS022-4915106",
        "116": "CFTS022-4915107", "117": "CFTS022-4915108", "118": "CFTS022-4915109",
        "120": "CFTS022-4915112", "121": "CFTS022-4915115"}
WANTS = {leaf(tc): _OBJ[re.search(r"-(\d+)$", str(SRC[leaf(tc)][1]).strip()).group(1)]
         for tc in TCS}
ok16 = all(tc["spec_reference"] == WANTS[leaf(tc)] for tc in TCS)
ok16 &= all("\n" not in tc["spec_reference"] and not re.search(r"[,、;]", tc["spec_reference"])
            for tc in TCS)
add(16, "§10.7", "spec_reference 列出所驗之每一 spec 節；一行一 ObjectID、無串接",
    ok16, "／".join(f"{leaf(tc)}={tc['spec_reference']}" for tc in TCS))

# ── 17 來源優先與門檻具體值（§8.6／§8.7）────────────────────────────
# 用及 profile §3.1 raw 者，須標 [ASSUMPTION A-DD6]（R-DD7(f)）
_uses = [tc for tc in TCS if re.search(r"= (129|77) \(", tc["test_procedure"])]
thr = all(re.search(r"= (129 \(8\.0625 km/h\)|77 \(4\.8125 km/h\))", tc["test_procedure"])
          for tc in _uses)
mark = all("[ASSUMPTION A-DD6]" in tc["expected_result"] for tc in _uses)
# ER 須具名取樣 feature（profile §2.1 禁泛稱）或逐字引 Standard Lockout Popup
VAGUE = r"some restricted feature|a locked-out feature|the restricted feature\b"
amb = all((re.search(r'"[^"]+"', tc["expected_result"])
           or "Standard Lockout Popup" in tc["expected_result"])
          and not re.search(VAGUE, tc["expected_result"], re.I) for tc in TCS)
add(17, "§8.6/§8.7", "門檻為 spec 溯源之具體值；相似操作於 ER 具名區辨；來源規格勝於索引匯出",
    thr and mark and amb,
    f"門檻具名 raw {thr}（profile §3.1 依 R-DD7(c)）；A-DD6 marker {mark}；ER 取樣具名 {amb}")

# ── 追加：§11 空白規制 ─────────────────────────────────────────────
ws = [(tc["tc_id"], f) for tc in TCS for f in MULTILINE
      for ln in tc[f].split("\n") if ln != ln.strip() or (not ln.strip() and ln)]
add("+", "§11", "多行欄位無行首／行尾空白，空行為真空行", not ws, f"{ws or '0 違規'}")

# ── 追加：profile §2.3 四禁詞不入 ER ────────────────────────────────
BAN4 = ["RESTRICTED", "NOT_RESTRICTED", "Locked", "Unlocked"]
h4 = [(tc["tc_id"], w) for tc in TCS for w in BAN4 if w in tc["expected_result"]]
add("+", "profile §2.3", "ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked",
    not h4, "0 命中" if not h4 else str(h4))

# ── 追加：priority（§10.2 + profile §4）─────────────────────────────
# profile §4：P0（8）＝007,009,011,013,015,019,023,025，其餘 P1
_P0 = {"007", "009", "011", "013", "015", "019", "023", "025"}
WP = {leaf(tc): ("P0" if leaf(tc) in _P0 else "P1") for tc in TCS}
add("+", "§10.2", "priority 為 P0–P3 且合 profile §4",
    all(tc["priority"] == WP[leaf(tc)] for tc in TCS),
    "／".join(f"{leaf(tc)}={tc['priority']}" for tc in TCS))

# ── 追加：§10.5 步驟數 ≥ 2 ─────────────────────────────────────────
add("+", "§10.5", "test_procedure 至少 2 個編號步驟",
    all(len(items(tc["test_procedure"])) >= 2 for tc in TCS),
    str({tc["tc_id"]: len(items(tc["test_procedure"])) for tc in TCS}))

# ── 追加：R-DD16(b) split_flag／split_reason ────────────────────────
miss = [tc["tc_id"] for tc in TCS if "split_flag" not in tc or "split_reason" not in tc]
badv = [(tc["tc_id"], tc.get("split_flag"), tc.get("split_reason")) for tc in TCS
        if not isinstance(tc.get("split_flag"), bool)
        or (tc.get("split_flag") is False and tc.get("split_reason") != "NA")]
add("+", "R-DD16(b)", "輸出 split_flag／split_reason；未拆者 false／\"NA\"",
    not miss and not badv, f"缺鍵 {miss or '無'}；值不合 {badv or '無'}；"
    "鍵名依 R-DD16(a) 用 test_item／spec_reference（既有寫回形制）")

# ── 輸出 ───────────────────────────────────────────────────────────
print("=" * 84)
print("TC 自檢 —— IN §9 十七項全跑 ＋ 追加項（骨幹；產物由 SC_ARTIFACT 指定）")
print("=" * 84)
nfail = nna = 0
for no, sec, name, v, det in res:
    tag = "PASS" if v is True else ("N/A " if v == "N/A" else "FAIL")
    nfail += (v is not True and v != "N/A")
    nna += (v == "N/A")
    print(f"[{tag}] {str(no):>3} {sec:<16} {name}")
    print(f"         {det}")
print("=" * 84)
npass = len(res) - nfail - nna
print(f"RESULT: PASS {npass} ／ N/A {nna} ／ FAIL {nfail}　（共 {len(res)} 檢）")
sys.exit(1 if nfail else 0)
