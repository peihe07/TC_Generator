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


# D8 修復（下放包 16 §四）：以下三個述詞為「自產物導出」之共用判準。
# 舊版以 leaf 號（`("010", "012")`）硬編 fail-safe 之身分 —— 換一批產物即失效，
# 且 B1／B2 之 fail-safe 列（004／006／008／014／016、018／020／022／024）
# **完全未被檢到**（檢 9 走錯分支、檢 11 之集合為空）。
RE_FAULT = re.compile(r"Stop transmitting|timeout", re.I)

# ── T23b（下放包 17 §四 10-6）—— `RE_ACCESS` 之動詞不再手列，改由交付語料導出 ──
# 上繳 13 §8.2-1 之自認：前版之 `(open|start|select|play|enter|launch)` 是我列的，
# 不是量出來的。本版比照 power profile §3.1 之作法：
#   母體 = 已交付之三產物（pilot／B1／B2）之全部 `test_procedure` 步驟；
#   分類判準（機械）—— 逐動詞看其所有步驟：
#     引用 UI 標籤（`"…"` 且非全大寫之匯流排訊息名）且不涉訊號 → ACCESS
#     涉 `$訊號$` 或匯流排訊息名且不引 UI 標籤            → STIMULUS
#     二者皆否或兼有                                    → 未分類（列出，不逕用）
# 受檢產物若出現**語料聯集外**之起首動詞，檢 8 轉 **WARN 要求人審**，不逕判紅。
# 10-3：本批經下放包 18 §三之**一次人審**後入語料。
# **拘束**：聯集外動詞須經人審方得入語料，且未分類動詞須逐次於 detail 列出 ——
# 否則「新動詞下一輪自動消 WARN」會使該 WARN 失效。
CORPUS = ("pilot_group3.json", "batch_b1.json", "batch_b2.json",
          "batch_body_off_init.json")
CORPUS_REVIEW = "下放包 18 §三 10-3（Bring／Terminate 經人審，落未分類）"
_RE_UI = re.compile(r'"([^"]+)"')
_RE_MSGNAME = re.compile(r"^[A-Z][A-Z_0-9]*$")


def _lead_verbs(tcs):
    out = {}
    for tc in tcs:
        for it in items(tc["test_procedure"]):
            # 分類只看**描述部** —— R-DD21(a)：`$` 指令行非步驟之敘述。
            # 未如此則 `Terminate` 因其 `$ PENDING…` 行含 `$` 而被誤判為 STIMULUS。
            b = " ".join(desc_lines(it)).strip()
            if b:
                out.setdefault(b.split()[0], []).append(b)
    return out


def _build_access():
    """回傳 (ACCESS 動詞集, STIMULUS 動詞集, 未分類集, 語料動詞聯集)。"""
    corpus = []
    for name in CORPUS:
        fp = ROOT / "generated" / name
        if fp.exists():
            corpus += json.loads(fp.read_text("utf-8"))
    acc, sti, unk = set(), set(), set()
    for v, steps in _lead_verbs(corpus).items():
        ui = sum(1 for s in steps
                 if any(not _RE_MSGNAME.match(x) for x in _RE_UI.findall(s)))
        sig = sum(1 for s in steps
                  if "$" in s or any(_RE_MSGNAME.match(x) for x in _RE_UI.findall(s)))
        (acc if ui and not sig else sti if sig and not ui else unk).add(v)
    return acc, sti, unk, set(_lead_verbs(corpus))


def is_fault(tc):
    """simulated fault（停送／逾時）之形態 —— 自 procedure 導出，非以 leaf 號判。"""
    return bool(RE_FAULT.search(tc["test_procedure"]))


def fault_at(tc):
    """注入所在之步驟序（1-based）；非 fault 則 None。"""
    for n, it in enumerate(items(tc["test_procedure"]), 1):
        if RE_FAULT.search(it):
            return n
    return None


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


RE_CLILINE = re.compile(r"^\s*\$ \S")


def desc_lines(item):
    """item 之描述部（§5.4 之 `$` 指令行不屬之）。"""
    body = re.sub(r"^\d+\.\s*", "", item)
    return [l for l in body.split("\n") if not RE_CLILINE.match(l)]


def words(item):
    """步驟字數：去編號前綴後之空白 token 數。

    **母體之更正（下放包 17 T23a）**：R-DD15 之計法（去編號後空白切分）
    定於本 feature 尚無 CLI 步驟之時。§5.4 明定 `$` 指令行為**不編號**之獨立行，
    非步驟之描述；把 shell token 計入「步驟字數」量到的是指令長度，不是步驟粒度。
    故本版把 `$` 行排除於母體之外 —— **這是母體之更正，不是尺之放寬**：
    描述部本身仍受 §5.2 之 12／18 字上限拘束（見 §四之注入 J）。
    **R-DD15「逾限改步驟不改尺」之適用未變**，惟本更正須分析層追認（上繳 14 §十）。
    """
    return len(" ".join(desc_lines(item)).split())


# `_build_access()` 用及 `items()`，故於其定義之後方呼叫
ACCESS_V, STIMULUS_V, UNCLASSED_V, CORPUS_V = _build_access()
RE_ACCESS = (re.compile(r"\b(" + "|".join(sorted(ACCESS_V)) + r")\b", re.I)
             if ACCESS_V else re.compile(r"(?!)"))


# ── 1 Test Set（§4.1／§4.2）—— **對 framework.md 實際比對**（T20b）────
# IN §9-1 之原文為「matches `framework.md`」。前版之標籤誠實載明其未比對
# framework，惟該檔當時不存在（下放包 14 §1.3）。本版讀檔取 Layer 2 之
# (Test Set, leaf 範圍) 集合，逐 TC 驗其 test_set ∈ 該集合**且與其 leaf 之分組相符**。
FW = ROOT / "framework.md"
if not FW.exists():
    add(1, "§4.1/§4.2", "Test Set 對 framework.md Layer 2 之比對",
        False, f"**{FW.name} 不存在** —— IN §4.1：framework 為 Test Set 之前提，"
               "須先於 TC 撰寫存在")
else:
    _fw = FW.read_text("utf-8")
    # Part II 之表列：| # | `Test Set` | leaf 範圍 (n) | … |
    L2 = {}
    for m in re.finditer(r"^\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*(\d{3})[–-](\d{3})",
                         _fw, re.M):
        name, lo, hi = m.group(1), int(m.group(2)), int(m.group(3))
        L2[name] = set(range(lo, hi + 1))
    bad, det = [], []
    for tc in TCS:
        n = int(leaf(tc))
        ts = tc["test_set"]
        if ts not in L2:
            bad.append((tc["tc_id"], ts, "不在 framework Layer 2"))
        elif n not in L2[ts]:
            want = next((k for k, v in L2.items() if n in v), "（無組涵蓋）")
            bad.append((tc["tc_id"], ts, f"leaf {n:03d} 應屬 `{want}`"))
    used = sorted({tc["test_set"] for tc in TCS})
    pre = [s for s in used if s.startswith("Driver Distraction")]
    junk = [s for s in used if s in ("Unclassified", "Misc", "General")]
    add(1, "§4.1/§4.2 + framework.md",
        "Test Set ∈ framework.md Layer 2，且與其 leaf 之分組相符；"
        "無 Test Group 前綴、無 Misc／Unclassified",
        not bad and not pre and not junk,
        f"framework Layer 2 共 {len(L2)} 組 {sorted(L2)}；本產物用 {used}；"
        f"不符 {bad or '無'}；前綴 {pre or '無'}；泛稱組 {junk or '無'}")

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
# 單位不硬編 km/h —— 標籤之覆算由檢 12 承擔，此處只驗行之形式。
RE_SIGSRC = re.compile(
    r"^\d+\. The signal \$[\w.]+\$ is transmitted on the bus at \d+ \([^)]+\)$")
shape = []
npc, nsig = {}, {}
for tc in TCS:
    its = items(tc["pre_conditions"])
    npc[leaf(tc)] = len(its)
    nsig[leaf(tc)] = sum(1 for it in its if "$" in it)
    for it in its:
        if "$" in it and not RE_SIGSRC.fullmatch(it.strip()):
            shape.append((tc["tc_id"], it.strip()))
add(3, "§4.4/§8.5 + R-DD17",
    "Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態；"
    "訊號源行合 R-DD17 之形式（只書訊號源，不兼述環境）",
    not hit and not shape,
    (f"禁式 0 命中；{len(TCS)} 則之 PC item 數 {npc}；其中訊號源行 {nsig}，"
     f"共 {sum(nsig.values())} 行皆合 R-DD17 之形式（§4.5-1 環境資料）"
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
nna = sum(1 for tc in TCS if tc["input_test_data"] == "NA")
add(4, "§4.5", "Input Test Data 歸屬正確；重複值移入 PC／Procedure 或設 NA",
    na and not back and not dupv,
    f"{len(TCS)} 則中 NA {nna} 則（全數={na}）；回指 {back or '無'}；"
    f"跨欄重複 {dupv or '無'}")

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
# 舊版之偵測為 `"$ " in test_procedure` —— 訊號記法 `$MSG.Sig$ = 129` 即含 `$ `，
# 故該集合恆非空；因 verdict 硬寫 "N/A"，此偵測從未影響結果（**空轉之檢**）。
# 本版改判「item 內是否有以 `$ ` 起首之行」，並使 verdict 隨之。
def _cli_lines(it):
    """item 內之 `$` 指令行序（去編號後逐行判）。"""
    body = re.sub(r"^\d+\.\s*", "", it)
    return [n for n, l in enumerate(body.split("\n")) if RE_CLILINE.match(l)]


cli = {}
for tc in TCS:
    hits = [(n, it) for n, it in enumerate(items(tc["test_procedure"]), 1)
            if _cli_lines(it)]
    if hits:
        cli[tc["tc_id"]] = hits
nstep = {leaf(tc): len(items(tc["test_procedure"])) for tc in TCS}
verbs = sorted({re.sub(r"^\d+\.\s*", "", it).split()[0]
                for tc in TCS for it in items(tc["test_procedure"])})
newv = sorted(set(verbs) - CORPUS_V)
_vinfo = (f"步驟起首動詞 {verbs}；語料聯集 {sorted(CORPUS_V)}"
          f"（ACCESS {sorted(ACCESS_V)}／STIMULUS {sorted(STIMULUS_V)}"
          f"／**未分類 {sorted(UNCLASSED_V) or '無'}**，未分類者不參與 RE_ACCESS）；"
          f"聯集外 {newv or '無'}；語料之人審出處 {CORPUS_REVIEW}")
if not cli:
    add(8, "§5.4", "CLI／tooling 步驟採 description + `$` 指令格式"
        "；並比對步驟起首動詞對交付語料之聯集（T23b）",
        "WARN" if newv else "N/A",
        (f"{len(TCS)} 則、共 {sum(nstep.values())} 步驟，以 `$ ` 起首之指令行 0"
         f" —— §5.4 無適用對象；") + _vinfo +
        ("　**聯集外動詞須人審**（下放包 17 §四 10-6）" if newv else ""))
else:
    # §5.4 四判準（下放包 17 §四 10-6：本檢於 -002 首次被真正行使，須強化）
    #   (i)   描述行在前：item 之第 0 行不得為指令行
    #   (ii)  指令行不得編號（`N. $ …` 不合 —— §5.4「unnumbered」）
    #   (iii) 指令行須緊接描述行（immediately under），中間不得有空行或他行
    #   (iv)  ER 之對應 item 不得覆述指令字串（§5.4「do not repeat the command string」）
    bad8 = []
    for t_ in cli:
        tc = next(x for x in TCS if x["tc_id"] == t_)
        er = items(tc["expected_result"])
        for n, it in cli[t_]:
            body = re.sub(r"^\d+\.\s*", "", it).split("\n")
            idx = _cli_lines(it)
            if 0 in idx:
                bad8.append((t_, n, "(i) 無描述行", body[0][:40]))
            for k in idx:
                if k and not body[k - 1].strip():
                    bad8.append((t_, n, "(iii) 指令行未緊接描述行", body[k][:40]))
                if k and RE_CLILINE.match(body[k - 1]):
                    bad8.append((t_, n, "(iii) 連續指令行無各自之描述", body[k][:40]))
            if re.match(r"^\d+\.\s*\$ ", it):
                bad8.append((t_, n, "(ii) 指令行帶編號", it.split("\n")[0][:40]))
            cmds = [body[k].strip()[2:].strip() for k in idx]
            if n <= len(er):
                for c_ in cmds:
                    if c_ and c_ in er[n - 1]:
                        bad8.append((t_, n, "(iv) ER 覆述指令字串", c_[:40]))
    shown = {t_: [n for n, _ in v] for t_, v in cli.items()}
    add(8, "§5.4", "CLI／tooling 步驟採 description + `$` 指令格式"
        "（(i) 描述行在前 (ii) 指令行不編號 (iii) 緊接其下 (iv) ER 不覆述指令）"
        "；並比對步驟起首動詞對交付語料之聯集（T23b）",
        ("WARN" if newv else True) if not bad8 else False,
        f"含指令行之 TC／步驟 {shown}；共 {sum(len(v) for v in cli.values())} 個指令 item；"
        f"四判準違規 {bad8 or '無'}；" + _vinfo +
        ("　**聯集外動詞須人審**（下放包 17 §四 10-6）" if newv and not bad8 else ""))

# ── 9 Baseline（§5.6）───────────────────────────────────────────────
d9 = []
ok9 = True
for tc in TCS:
    k = leaf(tc)
    its = items(tc["test_procedure"])
    if is_fault(tc):
        # before 為「注入之前已見正常行為」—— 不限步驟 1（B2 之注入在步驟 3）
        fi = fault_at(tc)
        base = fi > 1 and any(RE_ACCESS.search(x) for x in its[:fi - 1])
        ok9 &= base
        d9.append(f"{k}: 注入於步驟 {fi}／{len(its)}，其前 {fi - 1} 步建立正常態 "
                  f"{'✓' if base else '✗'}")
    else:
        # before 之載明 = PC 有合 R-DD17 形式之訊號源行（值不硬編）
        srcs = [RE_SIGSRC.fullmatch(x.strip()) for x in items(tc["pre_conditions"])]
        got = [m.group(0).split(" at ", 1)[1] for m in srcs if m]
        ok9 &= bool(got)
        d9.append(f"{k}: before 由 PC 載明（訊號源行 {got or '無'}）"
                  f"{'✓' if got else '✗'}，ER 不比對已記錄值，故不需記錄步驟")
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
# 舊版之條件為 `leaf ∈ {010,012} 且 items[0] 不以 "1." 起首` —— 後者恆為偽
# （items() 之切分即以 `^\d+\.` 為界），故該集合恆空：**此檢從未攔過任何事**。
# 本版：fail-safe 之身分由形態判，且真的驗「注入前已建立正常態」。
ff, d11 = [], []
for tc in TCS:
    if not is_fault(tc):
        continue
    its = items(tc["test_procedure"])
    fi = fault_at(tc)
    pre = its[:fi - 1]
    okff = fi > 1 and any(RE_ACCESS.search(x) for x in pre)
    if not okff:
        ff.append((tc["tc_id"], f"注入於步驟 {fi}，其前 {fi - 1} 步無正常態之建立"))
    d11.append(f"{leaf(tc)}(步驟 {fi}/{len(its)}){'✓' if okff else '✗'}")
# FP：列舉式支援項之偵測（format／device／protocol／codec 之列舉）
RE_ENUM = re.compile(r"\b(formats?|devices?|protocols?|codecs?|container)\b", re.I)
fp = sorted({tc["tc_id"] for tc in TCS for f in FOUR if RE_ENUM.search(tc[f])})
add(11, "§7", "無 FP／FF：含 setup／transition，不假設隱藏狀態；列舉支援項配負向",
    not ff,
    ((f"FF：本產物 {len(d11)} 則為 simulated fault（{'／'.join(d11)}），"
      f"皆先建立正常態再注入，未假設隱藏狀態" if d11
      else "FF：本產物無 simulated fault（`Stop transmitting`／`timeout` 0 命中）"
           "—— **無適用對象，非「已驗證」**")
     if not ff else f"FF 違規 {ff}") +
    f"；FP：列舉式支援項命中 {fp or '無'}"
    f"{'，無配對義務' if not fp else '，須逐項配負向'}")

# ── 12 追溯與範圍（§8.1／§8.2.1／§8.2.2／§8.4.1／§8.4.2）──────────
trace = all(re.fullmatch(r"SWE1-RA-Driver_Distraction-\d{3}", tc["req_id"]) for tc in TCS)
SCOPE = ["seat belt", "seatbelt", "passenger detection", "Are you the passenger",
         "occupant", "ADAS", "Level 3", "per-key-cycle", "key cycle", "Fullscreen"]
leak = [(tc["tc_id"], w) for tc in TCS for w in SCOPE
        for f in FOUR + ["test_item"] if w.lower() in tc[f].lower()]
# §8.4.1 造值 —— **改為溯源檢**（前版之手建白名單換一批 leaf 即失效）：
# 四交付欄內每一個 `= <raw> (<label>)` 之 (raw, label) 須可溯至
#   (i) 該訊號之 DBC `VAL_`（R-DD9(a)）、
#   (ii) profile §3.1 之 raw 表（R-DD9(b)：連續量，label 為物理值＋單位）、或
#   (iii) PROXI `Format` 之 Table 列舉（PROXI 參數）。
def _dbc_vals(sig):
    """`$MSG.Signal$` → {raw: label}，自二綁定 DBC 實讀。"""
    q = sig.strip("$")
    if "." not in q:
        return {}
    msg, sg = q.split(".", 1)
    for dp in (ROOT.parent / "vehicle_setting" / "inputs" / "PDT27_E2A_R4_BHCAN.dbc",
               ROOT.parent / "vehicle_setting" / "inputs" / "PDT27_E2A_R5_FDCAN8.dbc"):
        txt = dp.read_text("utf-8", errors="replace")
        bo = re.search(rf"^BO_ (\d+) {re.escape(msg)}\b", txt, re.M)
        if not bo:
            continue
        for m in re.finditer(rf"^VAL_\s+{bo.group(1)}\s+{re.escape(sg)}\s+(.*);\s*$",
                             txt, re.M):
            return {int(k): v for k, v in re.findall(r'(\d+)\s+"([^"]*)"', m.group(1))}
    return {}

DBC_PATHS = (ROOT.parent / "vehicle_setting" / "inputs" / "PDT27_E2A_R4_BHCAN.dbc",
             ROOT.parent / "vehicle_setting" / "inputs" / "PDT27_E2A_R5_FDCAN8.dbc")


def _dbc_meta(sig):
    """`$MSG.Signal$` → (factor 字串, offset 字串, unit)，自二綁定 DBC 實讀。

    factor **以字串回傳** —— 其小數位數即 R-DD9(b) 之書寫位數，
    由來源決定，不由本檔選定。
    """
    q = sig.strip("$")
    if "." not in q:
        return None
    msg, sg = q.split(".", 1)
    for dp in DBC_PATHS:
        txt = dp.read_text("utf-8", errors="replace")
        bo = re.search(rf"^BO_ (\d+) {re.escape(msg)}\b", txt, re.M)
        if not bo:
            continue
        nxt = re.search(r"^BO_ ", txt[bo.end():], re.M)
        blk = txt[bo.start(): bo.end() + (nxt.start() if nxt else len(txt))]
        m = re.search(rf"^\s*SG_ {re.escape(sg)} : [^(]*\(([^,]+),([^)]+)\)"
                      rf"[^\"]*\"([^\"]*)\"", blk, re.M)
        if m:
            return m.group(1).strip(), m.group(2).strip(), m.group(3)
    return None


def _rdd9b(raw, sig):
    """R-DD9(b) 之覆算：raw × factor + offset，位數取 factor 之小數位，附 DBC 單位。

    T22b（下放包 16 §五）：舊版以手建之 `PROFILE_RAW = {129:…, 77:…, 0:…}`
    放行，其中 **`0` 不在 profile §3.1**（該表只有 129／77）—— 即檢查器對 0
    有未寫明之特例，白名單自後門復歸。本函式把規則寫明並機械化：
    **凡該訊號之 `VAL_` 未涵蓋之 raw，其標籤須等於自 DBC factor／offset 之覆算值**。
    profile §3.1 仍為「取哪一個 raw」之權威（門檻選值，由檢 17 與 A-DD6 承擔），
    **但不再是標籤之溯源出處** —— 故本項之溯源標籤改為 `R-DD9(b) 覆算`。
    """
    meta = _dbc_meta(sig)
    if meta is None:
        return None
    fs, os_, unit = meta
    ndp = len(fs.split(".")[1]) if "." in fs else 0
    val = raw * float(fs) + float(os_)
    return f"{val:.{ndp}f} {unit}".strip()
PROXI_TBL = {0: "Not valid", 1: "MTX", 2: "MTA (Robotized Gearbox)",
             3: "DDCT", 4: "ATX", 5: "CVT"}
fab, prov = [], []
for tc in TCS:
    for f in FOUR:
        body = tc[f]
        # (a) CAN 訊號：`$MSG.Sig$ … = N (Label)` 或 `at N (Label)`
        for m in re.finditer(r"(\$[\w.]+\$)[^\n]*?(?:=|at) (\d+) \(([^)]+)\)", body):
            sig, raw, lab = m.group(1), int(m.group(2)), m.group(3)
            vals = _dbc_vals(sig)
            if raw in vals and vals[raw] == lab:
                prov.append((raw, lab, "DBC VAL_")); continue
            # R-DD9(b)／(c)：VAL_ 未涵蓋之 raw 為連續量，標籤須可覆算
            exp = _rdd9b(raw, sig)
            if exp is not None and exp.lower() == lab.lower():
                prov.append((raw, lab, "R-DD9(b) 覆算")); continue
            fab.append((tc["tc_id"], f, sig, raw, lab,
                        f"覆算得 {exp!r}" if exp is not None else "DBC 查無該訊號"))
        # (b) PROXI 參數：`PROXI Gear_Box_Type = N (Label)`
        for m in re.finditer(r"PROXI Gear_Box_Type = (\d+) \(([^)]+)\)", body):
            raw, lab = int(m.group(1)), m.group(2)
            if PROXI_TBL.get(raw) == lab:
                prov.append((raw, lab, "PROXI Format r443"))
            else:
                fab.append((tc["tc_id"], f, "Gear_Box_Type", raw, lab))
        # (c) 裸 raw（無括號標籤）—— R-DD9 要求一律帶標籤
        for m in re.finditer(r"(?:=|at) (\d+)(?! \()(?![\w.])", body):
            if m.group(1) not in ("91",):        # PROXI Country_Code 為純數值，無列舉標籤
                fab.append((tc["tc_id"], f, "（裸 raw，無括號標籤）", m.group(1), ""))
from collections import Counter as _C
add(12, "§8.1/§8.2/§8.4", "追溯 Req/SWRA；不擴入 sibling；**每一 raw 值可溯至 DBC VAL_／"
    "R-DD9(b) 覆算／PROXI Format**（無未寫明之特例）；無範圍捏造",
    trace and not leak and not fab,
    f"req_id 形制 {trace}；§8.4.2 禁詞 {leak or '0 命中'}；"
    f"溯源 {dict(_C(x[2] for x in prov))}；不可溯 {fab or '無'}")

# ── 13 Design Method（§12 first-match）──────────────────────────────
MENU = {"功能測試 (Functional based ; no specific technique)",
        "狀態轉換 (State Transition Testing)", "決策表 (Decision Table Testing)",
        "等價劃分 (Equivalence Partitioning, EP)",
        "邊界值分析 (Boundary Value Analysis, BVA)",
        "組合測試 (Combinatorial Testing ; Pairwise / t-wise)",
        "情境 / 用例 (Scenario / Use Case Testing)", "負向測試 (Negative / Invalid)",
        "基礎故障注入 (Fault Injection Lite)"}
# §12 first-match **機械化**：自 procedure 之形態推導，非以 AC 別或 leaf 號硬編。
#   Simulated fault（停送／逾時）→ Fault Injection
#   同一訊號送二個相異值      → State Transition
#   否則若條件 ≥2（PC 之組態列 ＋ procedure 之施加）→ Decision Table
def _want(tc):
    """回傳 (method, 命中之分支)。

    **回傳分支名而非只回方法名**（下放包 17 T23a 自查）：前版之 detail 以方法名
    回查一張理由表，故 `-001`／`-002` 明明由 ER 極性對比命中，卻印成
    「同一訊號於 PC 與 procedure 得二相異值」—— **印出來的理由不是實際走的路**，
    與 D8 同族。分支名自此隨判定一起回傳。
    """
    proc = tc["test_procedure"]
    if re.search(r"Stop transmitting|timeout", proc, re.I):
        return ("基礎故障注入 (Fault Injection Lite)",
                "simulated fault（停送／逾時），於 State Transition 前命中", False)
    sends = re.findall(r"Send the signal (\$[\w.]+\$) = ([^\n\[]+)", proc)
    by_sig = {}
    # PC 之訊號源行（R-DD17）亦為該訊號之一個值 —— 轉換之「before」載於 PC
    for m in re.finditer(r"The signal (\$[\w.]+\$) is transmitted on the bus at ([^\n\[]+)",
                         tc["pre_conditions"]):
        by_sig.setdefault(m.group(1), set()).add(m.group(2).strip())
    for s, v in sends:
        by_sig.setdefault(s, set()).add(v.strip())
    if any(len(v) >= 2 for v in by_sig.values()):
        return ("狀態轉換 (State Transition Testing)",
                "同一訊號於 PC 與 procedure 得二相異值（A→B），於 Scenario 前命中", False)
    # IN §12 之列為「State A → State B transition」，**不限以訊號承載**。
    # 前版只認「同一訊號二相異值」，故電源域之 sleep→wake 轉換判不出來
    #（-001 之形態）。補一條同族之機械判準：
    #   ER 中二個 item 對**同一組實詞**分別作否定與肯定之斷言 → A→B。
    NEG = re.compile(r"\b(no longer|not|never|absent|without)\b", re.I)
    STOP = {"the", "a", "an", "is", "are", "on", "in", "of", "its", "it", "and",
            "to", "at", "from", "no", "longer", "not", "all", "any", "within"}
    ers = items(tc["expected_result"])
    bags = [(bool(NEG.search(e)),
             {w.lower().strip('".,') for w in re.sub(r"^\d+\.\s*", "", e).split()}
             - STOP) for e in ers]
    for i_, (neg_i, bag_i) in enumerate(bags):
        for neg_j, bag_j in bags[i_ + 1:]:
            if neg_i != neg_j and len(bag_i & bag_j) >= 3:
                return ("狀態轉換 (State Transition Testing)",
                        "ER 對同一組實詞 "
                        f"{sorted(bag_i & bag_j)} 分作否定與肯定之斷言（A→B）"
                        "（門檻 3 為手定，見 R-G8 界線）", False)
    nconds = len([l for l in items(tc["pre_conditions"]) if "PROXI" in l]) + len(sends)
    if nconds >= 2:
        return ("決策表 (Decision Table Testing)",
                f"條件 {nconds} 項（PC 之組態列 ＋ procedure 之施加）且無二值轉換", False)
    # 10-6(a)(b)：走到這裡代表**三個判準全部沒有命中**（非 fault、無二值對、
    # 無 ER 極性對、條件 <2）。前版靜默判功能測試 —— 而「什麼都沒命中」與
    # 「確定是單一功能檢查」不是同一件事。故標 WARN 要求人審。
    return ("功能測試 (Functional based ; no specific technique)",
            f"**三判準皆未命中**（非 fault、無二值對、無 ER 極性對、條件 {nconds} 項）"
            "—— 落於序末之 fallback，非正面判定", True)
_W = {leaf(tc): _want(tc) for tc in TCS}
WANT = {k: v[0] for k, v in _W.items()}
WHY = {k: v[1] for k, v in _W.items()}
FALLBACK = sorted(k for k, v in _W.items() if v[2])
inmenu = all(tc["design_method"] in MENU for tc in TCS)
firstmatch = all(tc["design_method"] == WANT[leaf(tc)] for tc in TCS)
# 分組之鍵為 (方法, **實際命中之分支**) —— 同一方法由不同分支命中者分列
_grp = {}
for tc in TCS:
    _grp.setdefault((WANT[leaf(tc)], WHY[leaf(tc)]), []).append(leaf(tc))
_mis = [(leaf(tc), tc["design_method"], WANT[leaf(tc)])
        for tc in TCS if tc["design_method"] != WANT[leaf(tc)]]
add(13, "§12", "Design Method 於 procedure 定稿後指派，且合 first-match 序"
    "；落於序末之 fallback 轉 WARN（10-6a/b）",
    (("WARN" if FALLBACK else True) if inmenu and firstmatch else False),
    "；".join(f"{'／'.join(sorted(v))} → {m}（{w}）"
              for (m, w), v in sorted(_grp.items())) +
    f"；不符 first-match {_mis or '無'}；皆為下拉選單實值 {inmenu}"
    + (f"　**fallback 命中 {FALLBACK}，須人審**（10-6a/b）" if FALLBACK else ""))

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
            # `\d+`：A-DD10 起為二位數；舊式 `\d` 會把合法 marker 判為違規
            if re.fullmatch(r"\[ASSUMPTION A-DD\d+\]", m.group(0)):
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
# IN §8.4.3 之缺件佔位形制為 `PENDING: DR-{n} <缺件名>` —— 其角括號為該條所命，
# 非 UI 標籤之誤用（profile §2.5 之立意）。與 `[ASSUMPTION A-DDn]` 同型之 carve-out。
RE_PENDING = re.compile(r"PENDING: DR-[A-Z]+\d+ <[^>]+>")
sq = []
for tc in TCS:
    for f in FOUR:
        stripped = RE_PENDING.sub("", tc[f])
        if re.search(r"(?<![\w])'[^']+'(?![\w])", stripped) or "<" in stripped:
            sq.append((tc["tc_id"], f))
pend = sorted({m.group(0) for tc in TCS for f in FOUR
               for m in RE_PENDING.finditer(tc[f])})
add(15, "§11 + R-DD12(c)", "UI 標籤用 `\"...\"`；方括號僅限 037 逐字之 test_item 上半與 A-DD6 marker",
    not brk and not sq,
    ("0 違規；test_item 上半之 `[Normal]`／`[Exception]` 經比對為 037 逐字（R-DD12(a)）"
     if not brk else str(brk)) + f"；單引號／角括號 {sq or '無'}"
    f"；§8.4.3 PENDING 佔位（carve-out）{pend or '無'}")

# ── 16 spec_reference（§10.7）───────────────────────────────────────
# profile §1 之 SYS-RA → ObjectID 對照（逐字）。雙引 leaf（`-017`~`-028`）之
# spec_reference 為「HK 章閘 `CFTS022-4915120` 一行 ＋ 條文 ObjectID 一行」，升冪。
_OBJ = {"113": "CFTS022-4915104", "114": "CFTS022-4915105", "115": "CFTS022-4915106",
        "116": "CFTS022-4915107", "117": "CFTS022-4915108", "118": "CFTS022-4915109",
        "120": "CFTS022-4915112", "121": "CFTS022-4915115", "125": "CFTS022-4915120",
        "126": "CFTS022-4915121", "127": "CFTS022-4915122", "128": "CFTS022-4915123",
        "129": "CFTS022-4915124"}
det16, ok16 = [], True
for tc in TCS:
    srcs = [m.group(1) for m in
            re.finditer(r"SYS-RA-Driver_Distraction-(\d+)", str(SRC[leaf(tc)][1]))]
    want = [_OBJ[s] for s in srcs]
    got = tc["spec_reference"].split("\n")
    good = (got == want                                   # 逐行對應該列之 source，順序即升冪
            and got == sorted(got)                        # 升冪
            and not re.search(r"[,、;]", tc["spec_reference"]))
    ok16 &= good
    det16.append(f"{leaf(tc)}: source {srcs} → {got}{'' if good else ' **不符**'}")
add(16, "§10.7 + profile §1",
    "spec_reference 逐行對應該 leaf 之每一 source；一行一 ObjectID、升冪、無串接",
    ok16, "；".join(det16))

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

# ── 追加：B1 拘束補（下放包 13 §五）—— ER 不得斷言 128／78 邊界格 ────
edge = []
for tc in TCS:
    k = leaf(tc)
    src_txt = " ".join(str(c) for c in SRC[k] if c is not None)
    for v in ("128", "78"):
        if re.search(rf"(?<![\d.]){v}(?![\d.])", tc["expected_result"]):
            # 037 該列明書者不在此限
            if not re.search(rf"(?<![\d.]){v}(?![\d.])", src_txt):
                edge.append((tc["tc_id"], v))
add("+", "包 13 §五", "ER 不得斷言 128（不應鎖）／78（不應解）之邊界格"
    "（037 該列明書者不在此限）；跨越側 129／77 不受限",
    not edge, f"{edge or '0 命中'}；"
    f"用及跨越側者 {[leaf(t) for t in TCS if re.search(r'= (129|77) ', t['test_procedure'])]}")

# ── 追加：R-DD19(c) 硬邊界 —— MTA(2)／DDCT(3) 不得作 PC 或輸入 ────────
# 其所禁者為「作 Pre-Condition 或輸入」，故掃四個交付欄；reasoning 得載明其被排除。
edge19 = [(tc["tc_id"], f, m.group(0))
          for tc in TCS for f in FOUR
          for pat in (r"Gear_Box_Type\s*=\s*[23]\b", r"\bMTA\b", r"\bDDCT\b")
          for m in re.finditer(pat, tc[f])]
gb = sorted({m.group(0) for tc in TCS for f in FOUR
             for m in re.finditer(r"Gear_Box_Type\s*=\s*\d+ \([A-Z]+\)", tc[f])})
add("+", "R-DD19(c)", "硬邊界：MTA(2)／DDCT(3) 不得出現於四交付欄之任一處",
    not edge19, f"{edge19 or '0 命中'}；四欄所用之 Gear_Box_Type 值 {gb or '（未用）'}")

# ── 追加：R-DD22 交付欄之語言檢（D9；下放包 18 §1.3）─────────────────
# IN §1 逐字：TC workbook fields 為 **English only**。
# **此檢至本輪之前不存在** —— 檢 2 之「中文 無」只掃 `test_item` 之括號下半，
# 四交付欄從無任何非 ASCII 之檢；`-002` 之中文佔位即由此漏出（下放包 18 §1.3）。
#
# 母體：四交付欄 ＋ `test_item`。
# **`reasoning` 不在母體**（R-DD22(b)：推理欄，繁體中文照舊）—— 此即 carve-out 之界。
# R-DD22(a) 之三例外：
#   1. `[ASSUMPTION A-DDn]` marker —— 本即 ASCII，非豁免對象
#   2. `PENDING: DR-DDn <…>` 佔位 —— 形式獲許，**其內文亦須為英文**，故**不豁免**
#   3. 來源逐字之 UI 標籤 —— 若該引號字串為該 leaf 之 037 來源列逐字，
#      其非 ASCII 得留，惟須逐一列出並**登 DR，不逕譯**
LANGF = FOUR + ["test_item"]
na_bad, na_src = [], []
for tc in TCS:
    _row = " ".join(str(c) for c in SRC[leaf(tc)] if c is not None)
    for f in LANGF:
        for m in re.finditer(r"[^\x00-\x7F]+", tc[f]):
            seg = m.group(0)
            verbatim = any(seg in q and q.strip('"') in _row
                           for q in re.findall(r'"[^"]*"', tc[f]))
            (na_src if verbatim else na_bad).append((tc["tc_id"], f, seg))
add("+", "R-DD22 + IN §1", "四交付欄與 test_item 不得含非 ASCII"
    "（例外：來源逐字之 UI 標籤，須另登 DR）；`reasoning` 不在母體",
    not na_bad,
    (f"母體 {len(TCS)}×{len(LANGF)} 欄，非 ASCII 0 命中" if not na_bad and not na_src
     else f"違規 {na_bad or '無'}") +
    (f"；**來源逐字之 UI 標籤含非 ASCII {na_src} —— 須登 DR，不得逕譯**"
     if na_src else "；來源逐字之豁免 0 命中"))

# 追加：marker 義務登記表（用及即須標）
# 10-6(c)：逐列註其裁決號。**加列之義務屬 T-登**，非自檢自行推斷。
MARKER_REG = [
    (r"Gear_Box_Type\s*=",        ["A-DD8", "A-DD9"], "R-DD19(a)(b)（下放包 15 §一）"),
    (r"\$BCM_FD_9\.ParkBrakeSts\$", ["A-DD2"],        "R-DD18(b)（下放包 13 §三）"),
    (r"Body OFF|Body Off",        ["A-DD10"],         "R-DD20 v2(b)(4)（下放包 17 §三-4）"),
]
mk = []
for tc in TCS:
    body = " ".join(tc[f] for f in FOUR)
    # **登記表，非啟發式** —— 每一列由一條裁決所命，與該裁決同進退。
    # 10-6(c)：**每列須註其裁決號**；凡新裁決命 marker 者，同輪加列（T-登 固定項）。
    for tok, req, _rule in MARKER_REG:
        if re.search(tok, body):
            for r_ in req:
                if f"[ASSUMPTION {r_}]" not in body:
                    mk.append((tc["tc_id"], tok, r_))
used = sorted({r_ for tc in TCS for r_ in re.findall(r"\[ASSUMPTION (A-DD\d+)\]",
                                                     " ".join(tc[f] for f in FOUR))})
add("+", "R-DD19/R-DD18/R-DD20", "marker 義務登記表（每列註其裁決號，10-6c）",
    not mk,
    f"缺標 {mk or '無'}；本產物所用之 marker {used or '（無）'}；登記表 "
    + "／".join(f"`{tok}`→{'＋'.join(req)}［{rule}］" for tok, req, rule in MARKER_REG))

# ── 輸出 ───────────────────────────────────────────────────────────
print("=" * 84)
print("TC 自檢 —— IN §9 十七項全跑 ＋ 追加項（骨幹；產物由 SC_ARTIFACT 指定）")
print("=" * 84)
nfail = nna = nwarn = 0
for no, sec, name, v, det in res:
    tag = {True: "PASS", "N/A": "N/A ", "WARN": "WARN"}.get(v, "FAIL")
    nfail += (v is not True and v not in ("N/A", "WARN"))
    nna += (v == "N/A")
    nwarn += (v == "WARN")
    print(f"[{tag}] {str(no):>3} {sec:<16} {name}")
    print(f"         {det}")
print("=" * 84)
npass = len(res) - nfail - nna - nwarn
print(f"RESULT: PASS {npass} ／ N/A {nna} ／ WARN {nwarn} ／ FAIL {nfail}"
      f"　（共 {len(res)} 檢）")
if nwarn:
    print("WARN 不使本檔 exit 1 —— 其義為「機械判準不足，須人審」（下放包 17 §四 10-6）")
sys.exit(1 if nfail else 0)
