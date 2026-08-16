#!/usr/bin/env python3
"""Coverage audit — the seven questions of handoff 73 §3, per LEAF.

Not a generator and not a gate: it asks, for every leaf that already has a
test case, whether the canon's own multiplying rules were applied — §7's
reverse pairing, §8.3's five sibling axes, and §8.2.2's split stress test.

Two rules govern every answer:

  * **A gap needs a clause.** 73 §2: a gap is only a gap if the requirement
    text supports the missing test. Questions 3 and 4 (environment,
    persistence) are the dangerous ones — common sense will fill them in if
    nobody stops it — so they have a third answer, `無明文`: the behaviour
    plausibly has the property, the specification never says so, and the item
    becomes an RD-1 candidate rather than a test case.
  * **Evidence over verdict.** Every answer carries a reason naming the
    clause fragment or the TC that decided it. The keyword sets are printed
    with the output; they find candidates, they do not judge.

Output: data/coverage_audit.tsv, one row per leaf.

Usage:
    python3 features/comfort/scripts/coverage_audit.py
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]
REPORT = FEATURE / "inputs" / ("FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 "
                               "STLA 報告.xlsx")
TSV = FEATURE / "data" / "coverage_audit.tsv"

# ---------------------------------------------------------------------------
# Keyword sets. Named, printed with the output, and deliberately narrow: a
# miss here becomes 不適用, which is why §5 of the report states how many
# 不適用 answers were read by a human rather than inferred.
KW = {
    # Q1 — the clause names a closed set of supported items / valid values
    "enumeration": r"(has \d+ states?|there are \d+|\d+ states|ranges?:|"
                   r"only one|in this order|up to \d+|two screens|"
                   r"3 states|following order|available|supports?)",
    # Q1 — what an unsupported / invalid ER looks like
    "reverse_er": r"(not available|unavailable|greyed|grey|gray|blank|"
                  r"no longer|is not|does not|cannot|no \w+ is|not shown|"
                  r"not displayed|turned off|un-highlight)",
    # Q2 — the clause states a limit, a range or a count
    # 75 §6 — `\d+/\d+` matched the SCREEN SIZE string `8.4/10.1/12` and
    # reported a limit where there is none. Now: a fraction only counts when
    # both sides are whole numbers AND it is not part of a longer
    # slash-separated size list, and inch marks disqualify it outright.
    "limit": r"(?<![\d.\"'/])\d+/\d+(?![\d./])|(1-7|1-8|Off, 1|highest|lowest|"
             r"minimum|maximum|"
             r"\bHI\b|\bLO\b|\d+ ?sec|\d+ ?ms|15h|up to \d+|first press|"
             r"second press|third press|only one)",
    "limit_er": r"(highest|lowest|\bHI\b|\bLO\b|7/7|maximum|minimum|"
                r"cannot|does not|no longer|Off\b|first|second|third)",
    # Q3 — the clause ties the behaviour to power / boot
    "environment": r"(ignition|key ?cycle|cold boot|boot|power cycle|"
                   r"start-?up|restart|power on)",
    # Q4 — the clause says a state survives something
    "persistence": r"(latch|remember|retain|persist|after a keycycle|"
                   r"last selected|first time in a key cycle|restore|"
                   r"goes back to the previous|default to)",
    # Q3/Q4 — what COVERAGE of those two axes looks like in a TC. Kept apart
    # from the clause patterns above: the clause says "latching after a
    # keycycle", the procedure says "Run a keycycle", and one pattern cannot
    # be asked to find both. (First run reported 0 covered for persistence
    # because it looked for the clause's words inside the test steps.)
    "environment_er": r"(ignition|key ?cycle|keycycle|reboot|restart|"
                      r"power (on|off)|cold boot)",
    "persistence_er": r"(key ?cycle|keycycle|reboot|restart|again|"
                      r"previous|last|still|retained|default)",
    # Q4 — a leaf that HAS a settable state (so persistence is a fair
    # question even when the clause is silent)
    "stateful": r"(on/ ?off state|turns? on|turn off|set to|selected|"
                r"toggle|activate|highlight|state)",
    # Q5 — interruption / concurrency / interaction with other functions
    "concurrency": r"(break|interrupt|while|during|at a time|at the same "
                   r"time|timeout|time out|repeat|until|mutually exclusive|"
                   r"automatically turns|will be turned off)",
    "concurrency_er": r"(no longer|deactivat|turns? off|is off|unchanged|"
                      r"still|remains|breaks?|closes after|is not displayed|"
                      r"does not)",
    # Q6 — an invalid operation, an unavailable state, a rejected input
    "invalid": r"(shall not|will not|cannot|not able|ignore|not allowed|"
               r"do not|does not|no effect|greyed|gray|disabled|"
               r"not available|not shown|not displayed)",
    "invalid_er": r"(not |no |cannot|does not|greyed|grey|gray|blank|"
                  r"ignored|no effect|un-highlight)",
}
C = {k: re.compile(v, re.I) for k, v in KW.items()}


ACTION = re.compile(r"^\d+\.\s*(Press|Turn|Change|Select|Set|Move|Slide|Touch|"
                    r"Operate|Open|Adjust|Raise|Lower|Run|Retract|Toggle|"
                    r"Activate|Attempt|Wait|Configure|Leave|Start)\b", re.I)
# 74 §2 — a step is a TRIGGER only when its ER asserts a CONSEQUENCE. Setup
# steps are recognised the other way round: their ER restates the state the
# step just created ("Turn SYNC on" -> "The SYNC button is highlighted"), and
# that is not a consequence of the requirement under test.
CONSEQUENCE = re.compile(
    r"(no longer|breaks?\b|is broken|follows|jumps|increases|decreases|"
    r"moves|switches|becomes|turned off|turns off|goes to|has changed|"
    r"closes|opens|unavailable|takes effect|no effect|is still|remains|"
    r"stays|and .{0,40} is not|does not|is not displayed|greyed|gray)", re.I)


def _trigger_object(step: str) -> str:
    s = re.sub(r"^\d+\.\s*", "", step)
    s = re.sub(r"^(Press|Turn|Change|Select|Set|Move|Slide|Touch|Operate|Open|"
               r"Adjust|Raise|Lower|Run|Retract|Toggle|Activate|Attempt|Wait|"
               r"Configure|Leave|Start)\s+", "", s, flags=re.I)
    s = re.sub(r"\b(on|off|to|from|the|a|an|again|once|repeatedly|and|then|"
               r"read|until)\b", " ", s, flags=re.I)
    return re.sub(r"\W+", " ", s).strip().lower()


def leaf_texts() -> dict:
    import warnings
    warnings.filterwarnings("ignore")
    import openpyxl
    wb = openpyxl.load_workbook(REPORT, data_only=True)
    ws = wb["Analysis Report"]
    out = {}
    for row in ws.iter_rows(min_row=8, values_only=True):
        rid = str(row[0] or "")
        if re.fullmatch(r"SWE1-HVAC-\d+(-\d+)?", rid):
            out[rid] = str(row[4] or "").strip()
    return out


def _hit(pat: str, text: str) -> str:
    m = C[pat].search(text or "")
    return m.group(0) if m else ""


def audit_leaf(req_id, tcs, outline, clause, leaf_text, sec_er, sec_proc):
    """The seven questions for one leaf. Returns {q: (answer, reason)}."""
    basis = f"{leaf_text}\n{clause}"          # what the requirement says
    own = "\n".join(f"{t['test_procedure']}\n{t['expected_result']}"
                    for t in tcs)             # what this leaf's TCs do
    section = f"{sec_proc}\n{sec_er}"         # what the whole section's TCs do
    q = {}

    # ---- Q1 §7 reverse pairing -------------------------------------------
    enum = _hit("enumeration", basis)
    if not enum:
        q["q1"] = ("不適用", "條文未列舉支援項／有效值／可選項")
    else:
        rev_own = _hit("reverse_er", own)
        rev_sec = _hit("reverse_er", sec_er)
        if rev_own:
            q["q1"] = ("有", f"列舉句 `{enum}`；本 leaf 之 ER 自帶反向側 "
                             f"`{rev_own}`")
        elif rev_sec:
            q["q1"] = ("有", f"列舉句 `{enum}`；同節他條之 ER 為反向側 "
                             f"`{rev_sec}`")
        else:
            q["q1"] = ("無", f"列舉句 `{enum}`；本 leaf 與同節皆無未支援／"
                             f"無效之反向 ER")

    # ---- Q2 boundary ------------------------------------------------------
    lim = _hit("limit", basis)
    if not lim:
        q["q2"] = ("不適用", "條文未給限值、範圍或計數")
    else:
        cov = _hit("limit_er", own) or _hit("limit_er", section)
        q["q2"] = (("有", f"限值 `{lim}`；TC 之 ER 觸及端點 `{cov}`") if cov
                   else ("無", f"限值 `{lim}`；TC 未觸及 limit／limit±1／=0"))

    # ---- Q3 environment (cold boot / power cycle) -------------------------
    env = _hit("environment", basis)
    if env:
        cov = _hit("environment_er", own) or _hit("environment_er", section)
        q["q3"] = (("有", f"條文明文 `{env}`；TC 有對應步驟") if cov
                   else ("無", f"條文明文 `{env}`；無 TC 覆蓋該情形"))
    elif _hit("stateful", basis):
        q["q3"] = ("無明文", "本 leaf 有可設定之狀態，惟條文未述及 "
                             "cold boot／power cycle 後之行為 → RD-1 候選")
    else:
        q["q3"] = ("不適用", "條文未述及電源／啟動，且本 leaf 非狀態型")

    # ---- Q4 persistence ---------------------------------------------------
    per = _hit("persistence", basis)
    if per:
        cov = _hit("persistence_er", own) or _hit("persistence_er", section)
        q["q4"] = (("有", f"條文明文 `{per}`；TC 有對應步驟") if cov
                   else ("無", f"條文明文 `{per}`；無 TC 覆蓋其保留"))
    elif _hit("stateful", basis):
        q["q4"] = ("無明文", "本 leaf 之狀態由使用者設定，惟條文未述及其於 "
                             "reboot／ignition cycle 後是否保留 → RD-1 候選")
    else:
        q["q4"] = ("不適用", "條文未述及保留，且本 leaf 非狀態型")

    # ---- Q5 concurrency / interruption ------------------------------------
    con = _hit("concurrency", basis)
    if not con:
        q["q5"] = ("不適用", "條文未述及中斷、並行或與他功能之交互")
    else:
        cov = _hit("concurrency_er", own) or _hit("concurrency_er", section)
        q["q5"] = (("有", f"條文 `{con}`；TC 之 ER 覆蓋該交互 `{cov}`") if cov
                   else ("無", f"條文 `{con}`；無 TC 覆蓋該中斷／並行"))

    # ---- Q6 negative / invalid --------------------------------------------
    inv = _hit("invalid", basis)
    if not inv:
        q["q6"] = ("不適用", "條文未述及無效操作、不可用狀態或被拒之輸入")
    else:
        cov = _hit("invalid_er", own) or _hit("invalid_er", section)
        q["q6"] = (("有", f"條文 `{inv}`；TC 之 ER 覆蓋否定側 `{cov}`") if cov
                   else ("無", f"條文 `{inv}`；無 TC 覆蓋該否定側"))

    # ---- Q7 §8.2.2 split stress -----------------------------------------
    # 74 §2 — the criterion is the TRIGGER, not the observable. canon §5.7:
    # one trigger with several consequential outcomes is ONE test case; the
    # outcomes are facts to check, not test cases. The first implementation
    # asked "are there two independent observables", which is the §8.3 wording
    # and produced 106 false candidates — including `024-02`, whose seven
    # outcomes all follow from a single press and which 30 §2 had already
    # ruled must stay whole.
    #
    # A step counts as a trigger when it is an action AND its expected_result
    # line asserts a consequence rather than confirming the state the step
    # just established. Setup steps ("Turn SYNC on" → "The SYNC button is
    # highlighted") are excluded on that basis.
    if len(tcs) > 1:
        q["q7"] = ("有", f"本 leaf 已拆為 {len(tcs)} 條")
    else:
        steps = [l for l in tcs[0]["test_procedure"].split("\n") if l.strip()]
        ers = [l for l in tcs[0]["expected_result"].split("\n") if l.strip()]
        trig = []
        for i, st in enumerate(steps):
            if not ACTION.match(st):
                continue
            er = ers[i] if i < len(ers) else ""
            if not CONSEQUENCE.search(er):
                continue
            o = _trigger_object(st)
            if o and not any(o[:16] == x[:16] for x in trig):
                trig.append(o)
        if len(trig) >= 2:
            q["q7"] = ("無", f"{len(trig)} 個觸發，其 ER 各自斷言後果："
                             f"{trig[:4]} —— 依 §5.7 不同 trigger 應各自成條")
        else:
            q["q7"] = ("不適用", "單一觸發；其後果不論幾項，依 §5.7 同屬一條")
    return q


def main() -> int:
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted((FEATURE / "generated").glob("*.json"))]
    leaves = leaf_texts()
    full = L.FULLTEXT_BY_OUTLINE

    by_leaf = defaultdict(list)
    outline_of = {}
    for d in docs:
        for tc in d["tcs"]:
            if tc["remarks"].startswith("[BLOCKED"):
                continue          # no procedure/ER to audit (R-C24)
            by_leaf[tc["req_id"]].append(tc)
            outline_of[tc["req_id"]] = d["outline"]
    sec_er = {d["outline"]: " || ".join(t["expected_result"] for t in d["tcs"])
              for d in docs}
    sec_pr = {d["outline"]: " || ".join(t["test_procedure"] for t in d["tcs"])
              for d in docs}

    rows = []
    for req_id, tcs in sorted(by_leaf.items()):
        o = outline_of[req_id]
        q = audit_leaf(req_id, tcs, o, full.get(o, ""), leaves.get(req_id, ""),
                       sec_er[o], sec_pr[o])
        row = {"req_id": req_id.replace("SWE1-HVAC-", ""), "outline": o,
               "test_set": tcs[0]["test_set"], "tc_count": len(tcs)}
        for i in range(1, 8):
            row[f"q{i}"] = q[f"q{i}"][0]
            row[f"q{i}_why"] = q[f"q{i}"][1].replace("\t", " ")
        rows.append(row)

    fields = (["req_id", "outline", "test_set", "tc_count"]
              + [f"q{i}{s}" for i in range(1, 8) for s in ("", "_why")])
    with TSV.open("w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, delimiter="\t",
                           lineterminator="\n", quoting=csv.QUOTE_NONE,
                           quotechar="", escapechar=None)
        w.writeheader()
        w.writerows(rows)

    names = {"q1": "§7 反向配對", "q2": "boundary", "q3": "environment",
             "q4": "persistence", "q5": "concurrency/interruption",
             "q6": "negative/invalid", "q7": "§8.2.2 壓力測試"}
    print(f"leaves audited: {len(rows)}  ->  {TSV}\n")
    print("keyword sets (evidence finders, printed so they can be argued with):")
    for k, v in KW.items():
        print(f"  {k:16} {v[:76]}")

    print("\n== 各問之答分佈 ==")
    for k, nm in names.items():
        c = Counter(r[k] for r in rows)
        parts = "  ".join(f"{a} {c[a]:4}" for a in
                          ("有", "無", "無明文", "不適用") if c[a])
        print(f"  {nm:26} {parts}")

    print("\n== 缺口（無）依 Test Set ==")
    gap_ts = Counter((r["test_set"], k) for r in rows for k in names
                     if r[k] == "無")
    for ts in sorted({t for t, _ in gap_ts}):
        line = "  ".join(f"{names[k].split('/')[0]} {n}"
                         for (t, k), n in sorted(gap_ts.items()) if t == ts)
        print(f"  {ts:26} {line}")

    print("\n== 缺口（無）依節，前 20 ==")
    gap_sec = Counter((r["outline"], k) for r in rows for k in names
                      if r[k] == "無")
    for (o, k), n in gap_sec.most_common(20):
        ex = [r["req_id"] for r in rows if r["outline"] == o and r[k] == "無"]
        print(f"  {o:8} {names[k]:26} {n:3}  e.g. {ex[:4]}")

    rd1 = [r for r in rows if r["q3"] == "無明文" or r["q4"] == "無明文"]
    print(f"\n== RD-1 候選（Q3／Q4 無明文）：{len(rd1)} leaf "
          f"（Q3 {sum(1 for r in rows if r['q3'] == '無明文')}、"
          f"Q4 {sum(1 for r in rows if r['q4'] == '無明文')}）==")
    ts_rd1 = Counter(r["test_set"] for r in rd1)
    for ts, n in ts_rd1.most_common():
        print(f"  {ts:26} {n:4}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
