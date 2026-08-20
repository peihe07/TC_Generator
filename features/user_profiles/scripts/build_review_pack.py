#!/usr/bin/env python3
"""覆核用全文 ＋ ER 出處對照之產生器（40 包作業 5）。

21／23／29／34／35 輪之 review pack 皆為**手打**。手打的代價在 35 輪已經
出現過一次：拆兩檔時要逐條搬運欄位，而**搬運本身沒有閘**。
本檔把該格式變成一支程式 —— 內容一律自 `generated/*.json` 讀出，
**不經人手轉錄**。

出處對照併入同一檔（每條之引號字面值 → 其來源節），
判準與 `lint_tcs` 之 G18 同一支：`_pool()` 取被引之節之 `pdf_text`
加其 must_carry，`UI_LOCATORS` 之登記另計。
**兩者若分歧，是 G18 或本檔其一寫錯了** —— 故本檔直接呼叫 G18 之資料源，
不另抄一份判準。

Usage:
    python3 scripts/build_review_pack.py 135 145 > out.md
"""

import argparse
import datetime
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
import lint_tcs as L                                  # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
FIELDS = [
    # **55 包起 `test_item` 為兩段**（首段 tc_title、第二段一句說明），
    # 兩者不再等同，故 pack 印出**整個 `test_item`** ——
    # 否則覆核者看不到實際交付的那一欄。
    # 第二段之**英文措辭本身未經第二人讀過**（其中文來源已讀過），
    # 這正是它須進 pack 之理由。
    ("test_item（兩段）", "test_item"),
    ("tc_title（＝ test_item 首段）", "tc_title"),
    ("pre_conditions", "pre_conditions"),
    ("input_test_data", "input_test_data"),
    ("test_procedure", "test_procedure"),
    ("expected_result", "expected_result"),
    ("specification_reference", "specification_reference"),
    ("design_method", "design_method"),
]


def _cell(v: str) -> str:
    return " ".join(str(v).split("\n")).replace("|", "\\|") if "\n" not in str(v) \
        else "<br>".join(x.strip() for x in str(v).splitlines() if x.strip()) \
                 .replace("|", "\\|")


def records(lo: int, hi: int) -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            n = int(t["tc_id"].rsplit("-", 1)[1])
            if lo <= n <= hi:
                out.append((n, d, t))
    return [x[1:] for x in sorted(out)]


def pool_for(t: dict) -> tuple:
    cited = [x.strip().replace(B.SPEC_STEM + "_", "")
             for x in str(t["specification_reference"]).split("; ")]
    pool = " ".join(B.spec_body(c) for c in cited)
    for c in cited:
        for r in B.must_carry_for(c):
            pool += " " + (r.get("text") or "")
    return cited, " ".join(pool.split())


def provenance(rows: list) -> list:
    out = []
    for d, t in rows:
        cited, pool = pool_for(t)
        for field, raw in (("ER", t["expected_result"]),
                           ("pre", t["pre_conditions"])):
            for lit in L.QUOTED_RE.findall(str(raw)):
                if " ".join(lit.split()) in pool:
                    src = f"逐字見於 **{'／'.join(cited)}**"
                elif lit.strip() in L.UI_LOCATORS:
                    src = (f"`UI_LOCATORS` 登記：其來源為 "
                           f"**{L.UI_LOCATORS[lit.strip()]}**")
                else:
                    src = "**未溯得 —— 須處置**"
                out.append((t["tc_id"], d["outline"], lit, field, src))
    return out


# ── AA-1（44 包 §一）—— pack 之時效 ────────────────────────────────
#
# `24a`／`24b` 產於 40 輪，而 41 輪之 RD #8 處置與 `popup_guard` 之 20 條修正
# 都在其後。**review pack 是靜態轉錄，不隨重生成更新** ——
# 分析層讀到 `TC-142` 之 `Press Yes on popup PU_0129`，
# 而語料早已是 `Press Yes on each confirmation popup PU0626/PU_0129`。
#
# **這是覆核依據之正確性問題**：對一份已被修好的內容開缺陷單，
# 或把已修的版本當成未修而放過 —— 兩個方向都會發生。
#
# ## 指紋之範圍 ＝ **pack 實際轉錄的東西**
#
# 不取 `audit_pending` 之六欄（那是為待判掃描而定的），
# 而取 **pack 自己印出來的每一個欄位**：若 pack 印的沒變，它就沒過期；
# 若 pack 沒印的變了（例如 `keywords`），它不影響覆核。
# **兩支工具之 digest 範圍不同，是因為它們防的是不同的事。**

DIGEST_FIELDS = [k for _lbl, k in FIELDS] + [
    "priority", "priority_basis", "remarks"]
FP_LINE = re.compile(r"^\| `(NR1L-UserProfiles-\d{3})` \| `([0-9a-f]{12})` \|",
                     re.M)
FP_ROUND = re.compile(r"產生輪次：\*\*(\d+)\*\*")


def pack_digest(d: dict, t: dict) -> str:
    blob = "␟".join(" ".join(str(t.get(k, "")).split())
                    for k in DIGEST_FIELDS)
    blob += "␟" + " ".join(str(d.get("reasoning", "")).split())
    blob += "␟" + " ".join(str(d.get("source_clause", "")).split())
    blob += "␟" + " ".join(str(d.get("leaf_desc_037", "")).split())
    return hashlib.sha1(blob.encode("utf-8")).hexdigest()[:12]


def current_digests(lo: int, hi: int) -> dict:
    return {t["tc_id"]: pack_digest(d, t) for d, t in records(lo, hi)}


def verify_pack(path: Path) -> tuple:
    """回傳 (違規清單, 相符數)。**不符即『pack 已過期，拒絕採信』。**"""
    txt = path.read_text(encoding="utf-8")
    stated = dict(FP_LINE.findall(txt))
    bad = []
    if not stated:
        return ([f"AA-1 `{path.name}` **無語料指紋** —— 產於指紋機制之前，"
                 f"一律視為過期，**拒絕採信**"], 0)
    ids = sorted(stated)
    lo, hi = int(ids[0][-3:]), int(ids[-1][-3:])
    now = current_digests(lo, hi)
    for tid, dg in sorted(stated.items()):
        cur = now.get(tid)
        if cur is None:
            bad.append(f"AA-1 {tid}: 已不在語料內")
        elif cur != dg:
            bad.append(f"AA-1 {tid}: pack 之指紋 `{dg}` 與現況 `{cur}` 不符 "
                       f"—— **該條已變動，pack 之轉錄不得採信**")
    for tid in sorted(now):
        if tid not in stated:
            bad.append(f"AA-1 {tid}: 在語料內而 pack 未載")
    return (bad, len(stated) - len(bad))


# ── 變動清單 —— **逐欄比對，不只報「變了」** ──────────────────────
BLOCK = re.compile(r"^### (NR1L-UserProfiles-\d{3}) —.*?(?=^### |\Z)",
                   re.M | re.S)
ROW = re.compile(r"^\| ([^|]+?) \| (.*) \|$", re.M)
REASONING = re.compile(r"^\*\*reasoning\*\*：(.*)$", re.M)


def changes(path: Path) -> list:
    """舊 pack 之逐條逐欄 vs 現況。**不用 git —— 舊值就在那份檔案裡。**"""
    txt = path.read_text(encoding="utf-8")
    cur = {}
    ids = re.findall(r"^### (NR1L-UserProfiles-(\d{3})) —", txt, re.M)
    if not ids:
        return []
    lo, hi = int(ids[0][1]), int(ids[-1][1])
    for d, t in records(lo, hi):
        cur[t["tc_id"]] = (d, t)
    out = []
    for m in BLOCK.finditer(txt):
        tid = m.group(1)
        block = m.group(0)
        old = {lbl.strip(): val.strip() for lbl, val in ROW.findall(block)}
        rm = REASONING.search(block)
        if rm:
            old["reasoning"] = rm.group(1).strip()
        if tid not in cur:
            out.append((tid, ["**已不在語料內**"]))
            continue
        d, t = cur[tid]
        diff = []
        for label, key in FIELDS:
            o = old.get(label)
            n = _cell(t[key])
            if o is not None and o != n:
                diff.append(label)
        if old.get("priority") is not None and \
                old["priority"] != f"**{t['priority']}** — {t['priority_basis']}":
            diff.append("priority")
        if old.get("remarks") is not None and old["remarks"] != _cell(t["remarks"]):
            diff.append("remarks")
        if old.get("reasoning") is not None and \
                old["reasoning"] != " ".join(str(d["reasoning"]).split()):
            diff.append("reasoning")
        if diff:
            out.append((tid, diff))
    return out


BATCH = "第五批"
SUPERSEDES = ""


def emit(lo: int, hi: int, title: str, other: str) -> None:
    rows = records(lo, hi)
    prov = provenance(rows)
    unresolved = [x for x in prov if "未溯得" in x[4]]
    verbatim = [x for x in prov if x[4].startswith("逐字")]
    loc = [x for x in prov if "UI_LOCATORS" in x[4]]

    print(f"# 覆核用全文 ＋ ER 出處對照 — {BATCH} {title}"
          f"（`{lo:03d}`–`{hi:03d}`）\n")
    # **日期取產生當下**（58 包）—— 原為寫死之 `2026-08-18`，
    # 而 57 輪四份 pack 產於 8/20 卻印著 8/18。它不影響判定
    # （pack 之新鮮度由 §0.0 之語料指紋管，不由日期管），
    # 但那是「值看起來像決定過」之同型（G-C）：
    # **一個寫死的日期與一個正確的日期，在紙上長得一模一樣。**
    today = datetime.date.today().isoformat()
    print(f"- 產出層：執行層｜{today}｜**供分析層逐條覆核**")
    print(f"- 本檔 **{len(rows)} 條**；另半在 `{other}`")
    print(f"- 由 `scripts/build_review_pack.py` 產生，不經人手轉錄")
    if SUPERSEDES:
        print(f"- **本檔取代 `{SUPERSEDES}`**（AA-1，44 包）——"
              f"該檔無語料指紋，`--verify` 一律判過期")
    print()
    print("> 讀法：先讀「spec 原文」與「037 description」，再讀 ER ——")
    print("> 「這句話對不對」是本檔要問的；「這句話有沒有來源」見 §0 之出處對照。\n")

    print(f"## 0.0 語料指紋（AA-1，44 包）—— 產生輪次：**{ROUND}**\n")
    print("> **本表是本 pack 之保鮮期。** 覆核前先跑：")
    print("> `python3 scripts/build_review_pack.py --verify <本檔>` ——")
    print("> **不符即「pack 已過期，拒絕採信」**，須重出後再讀。")
    print("> 指紋之範圍即本 pack 所轉錄之每一個欄位"
          "（含 spec 原文、037 description、reasoning）。\n")
    print("| tc_id | digest |")
    print("|---|---|")
    for d, t in rows:
        print(f"| `{t['tc_id']}` | `{pack_digest(d, t)}` |")
    print()

    print("## 0. ER 出處對照\n")
    print("| 項 | 數 |")
    print("|---|---|")
    print(f"| 引號字面值（ER ＋ pre_conditions）| **{len(prov)}** |")
    print(f"| 逐字溯得到被引之節或其 must_carry | **{len(verbatim)}** |")
    print(f"| 經 `UI_LOCATORS` 登記表溯源 | **{len(loc)}** |")
    print(f"| **未溯得者** | **{len(unresolved)}** |")
    n_none = sum(1 for d, t in rows
                 if not L.QUOTED_RE.findall(str(t["expected_result"])
                                            + str(t["pre_conditions"])))
    print(f"| 全條無引號字面值者 | **{n_none} 條** |\n")
    print("| tc_id | 節 | 字面值 | 欄位 | 出處 |")
    print("|---|---|---|---|---|")
    for tid, sec, lit, field, src in prov:
        print(f"| `{tid}` | {sec} | 「{lit}」| {field} | {src} |")
    print("\n---\n")

    print("## 1. 逐條全文\n")
    for d, t in rows:
        print(f"### {t['tc_id']} — {t['req_id']}"
              f"（{d['outline']} / {d['test_set']}）\n")
        print("**spec 原文（`pdf_text`）**：\n")
        print("> " + " ".join(str(d["source_clause"]).split()) + "\n")
        print("**037 description**：" +
              " ".join(str(d["leaf_desc_037"]).split()) + "\n")
        print("| 欄 | 值 |")
        print("|---|---|")
        for label, key in FIELDS:
            print(f"| {label} | {_cell(t[key])} |")
        print(f"| priority | **{t['priority']}** — {t['priority_basis']} |")
        print(f"| remarks | {_cell(t['remarks'])} |")
        print(f"\n**reasoning**：{' '.join(str(d['reasoning']).split())}\n")
        print("---\n")


ROUND = 44


def self_test() -> int:
    """方向性案例 —— **過期檢查若不會紅，它就只是一張表。**"""
    import tempfile
    ok, cases = True, []

    def case(name, fn, expect_red):
        nonlocal ok
        cases.append(name)
        bad = fn()
        good = bool(bad) == expect_red
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_red else '綠'}")
        for b in bad[:2]:
            print(f"      └ {b}")

    with tempfile.TemporaryDirectory() as td:
        fresh = Path(td) / "fresh.md"
        import contextlib, io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            emit(135, 140, "測試", "—")
        fresh.write_text(buf.getvalue(), encoding="utf-8")

        case("**剛產生之 pack → 綠**", lambda: verify_pack(fresh)[0], False)

        # 注入：指紋被改一個字元（＝語料變動之等價形態）
        tampered = Path(td) / "tampered.md"
        txt = fresh.read_text(encoding="utf-8")
        m = FP_LINE.search(txt)
        old = m.group(2)
        tampered.write_text(
            txt.replace(f"`{old}`", "`000000000000`", 1), encoding="utf-8")
        case("**注入：某條之指紋與語料不符 → 紅（拒絕採信）**",
             lambda: verify_pack(tampered)[0], True)

        # 注入：整段指紋表被移除（＝指紋機制之前產生者）
        nofp = Path(td) / "nofp.md"
        nofp.write_text(FP_LINE.sub("", txt), encoding="utf-8")
        case("**注入：無指紋表之舊 pack → 紅（一律視為過期）**",
             lambda: verify_pack(nofp)[0], True)

        # 護欄：`changes()` 對剛產生者須為空
        case("**護欄**：`changes()` 對剛產生之 pack → 無變動",
             lambda: changes(fresh), False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("args", nargs="*")
    ap.add_argument("--verify", default=None, help="檢查某份 pack 是否過期")
    ap.add_argument("--changes", default=None,
                    help="列出某份舊 pack 自其產生以來有變動之條目")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if a.verify:
        bad, okn = verify_pack(Path(a.verify))
        print(f"{Path(a.verify).name}：相符 {okn} 條，不符 {len(bad)} 條")
        for b in bad:
            print(f"  {b}")
        sys.exit(1 if bad else 0)
    if a.changes:
        ch = changes(Path(a.changes))
        print(f"{Path(a.changes).name}：有變動 {len(ch)} 條")
        for tid, flds in ch:
            print(f"  {tid} — {'／'.join(flds)}")
        sys.exit(0)
    if len(a.args) > 4:
        globals()['BATCH'] = a.args[4]
    if len(a.args) > 5:
        globals()['SUPERSEDES'] = a.args[5]
    emit(int(a.args[0]), int(a.args[1]), a.args[2], a.args[3])
