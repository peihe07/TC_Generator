#!/usr/bin/env python3
"""動詞詞表之閘（41 包 §三之常規）。

> 凡以**動詞**為觸發條件之掃描，須另立同義動詞對照表；
> 每批生成後，以該批 procedure 實際用過的動詞回頭比對詞表一次，
> 新動詞未入表者，掃描結果不予採認。

## 三項

| # | 檢查 | 性質 |
|---|---|---|
| VB-1 | 語料之每個 procedure 首詞都登記於 `data/verb_synonyms.tsv` | 紅 |
| VB-2 | 每個標了 `trigger` 之動詞，其 `probe` 須被該掃描之 action 正則命中 | 紅 |
| VB-3 | 同組之動詞其 `trigger` 須一致 —— **同義而只登記其一，即 40 輪之缺陷** | 紅 |

**VB-2 是本檔的重心。** 它把「詞表說 `activate` 會觸發 PU0580」這個宣稱
拿去**問掃描本身**：`POPUP_TRIGGERS` 之正則對 `1. Activate Driver Profile B`
成不成立？40 輪之前，答案是**不成立**，而沒有任何一支閘問過這個問題。

## 盲區（R-G11）

1. **只看首詞。** `Press the Profile button and read which tab is shown` 之
   `read` 不在檢查範圍 —— 首詞判準與 `lint_tcs` 之 G8／G15 一致，
   非首詞之動詞由那兩閘之查核目標判準承擔。
2. **只驗「詞表 → 掃描」，不驗「掃描 → 詞表」。**
   若某掃描之正則含一個詞表沒有的動詞，本檔不報。
   那一側由 VB-1 間接承擔（語料若真用了它，VB-1 會要求登記）。
3. **無 PU id 之 popup 不在 X-1 之射程內，故亦不在本檔射程內。**
   7.1（PRWEL1）之「ignition on 時之 welcome popup」**條文未給 id**，
   `POPUP_TRIGGERS` 以 PU id 為鍵，結構上看不見它。
   現行處置：凡 procedure 含 key cycle 且與 welcome popup 無關者，
   其 pre-condition 已由 `popup_guard` 指定該設定為關閉。

Usage:
    python3 scripts/audit_verbs.py
    python3 scripts/audit_verbs.py --self-test
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent
TABLE = FEATURE / "data" / "verb_synonyms.tsv"
LEAD = re.compile(r"^\s*\d+\.\s*([A-Za-z][A-Za-z'-]*)")


def rows() -> list:
    with TABLE.open(encoding="utf-8") as fh:
        rd = csv.DictReader((l for l in fh if not l.startswith("#")),
                            delimiter="\t")
        return [r for r in rd if r.get("verb")]


def corpus_verbs() -> dict:
    """首詞 → 出現次數。"""
    out = {}
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            for ln in str(t["test_procedure"]).splitlines():
                m = LEAD.match(ln)
                if m:
                    out[m.group(1)] = out.get(m.group(1), 0) + 1
    return out


def _trigger_action(trigger: str):
    """`X-1:PU0580` → 該 popup 於 `POPUP_TRIGGERS` 之 action 正則。"""
    import audit_consistency as A
    scan, pid = trigger.split(":", 1)
    if scan != "X-1":
        return None
    for p, _secs, action, _cond, _why in A.POPUP_TRIGGERS:
        if p == pid:
            return action
    return "**該 popup 不在 POPUP_TRIGGERS 內**"


def audit(table=None, verbs=None) -> list:
    table = rows() if table is None else table
    verbs = corpus_verbs() if verbs is None else verbs
    bad = []
    known = {r["verb"].lower() for r in table}

    # ── VB-1
    for v, n in sorted(verbs.items()):
        if v.lower() not in known:
            bad.append(f"VB-1 語料之首詞 `{v}`（{n} 處）未登記於 "
                       f"`data/verb_synonyms.tsv` —— **掃描結果不予採認**")

    # ── VB-2
    for r in table:
        trig = (r.get("trigger") or "-").strip()
        if trig in ("-", ""):
            continue
        action = _trigger_action(trig)
        if action is None or action.startswith("**"):
            bad.append(f"VB-2 `{r['verb']}` 之 trigger `{trig}` 無對應之掃描"
                       f"觸發正則")
            continue
        probe = (r.get("probe") or "").strip()
        if not probe or not re.search(action, probe, re.I):
            bad.append(f"VB-2 `{r['verb']}` 標了 `{trig}`，而該掃描之正則"
                       f"**對其探針句不成立** → 「{probe}」"
                       f"—— 詞表與掃描已分岔（40 輪之缺陷形態）")

    # ── VB-3
    by_group = {}
    for r in table:
        by_group.setdefault(r["group"], []).append(r)
    for g, rs in sorted(by_group.items()):
        trigs = {(r.get("trigger") or "-").strip() for r in rs}
        if len(trigs) > 1:
            bad.append(f"VB-3 同義組 `{g}` 之 trigger 不一致 {sorted(trigs)}"
                       f" —— 同義而只登記其一，即 40 輪之缺陷")
    return bad


def self_test() -> int:
    table, verbs = rows(), corpus_verbs()
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

    case("現行語料 ＋ 現行詞表 → 綠", lambda: audit(table, verbs), False)

    # VB-1：語料出現未登記之動詞
    case("VB-1 注入：語料出現未登記之 `Toggle` → 紅",
         lambda: audit(table, {**verbs, "Toggle": 3}), True)

    # VB-2 —— **本組最關鍵**：把 PU0580 之正則改回 40 輪之前（只認 select）
    def regex_regressed():
        import audit_consistency as A
        orig = A.POPUP_TRIGGERS
        A.POPUP_TRIGGERS = [
            (p, s, (r"\bselect\b[^.\n]{0,40}Driver Profile\b"
                    if p == "PU0580" else a), c, w)
            for p, s, a, c, w in orig]
        try:
            return audit(table, verbs)
        finally:
            A.POPUP_TRIGGERS = orig
    case("**VB-2 注入：PU0580 之正則退回只認 `select`（40 輪之缺陷本身）→ 紅**",
         regex_regressed, True)

    # VB-3：同義組內漏標 trigger
    def group_split():
        t = [dict(r) for r in table]
        for r in t:
            if r["verb"].lower() == "select":
                r["trigger"] = "-"
        return audit(t, verbs)
    case("VB-3 注入：`Select` 之 trigger 改為 `-`（同組不一致）→ 紅",
         group_split, True)

    # 護欄：詞表多登記一個語料未用之動詞 → 不得轉紅
    def extra_row():
        t = [dict(r) for r in table]
        t.append({"verb": "Rotate", "group": "gesture", "trigger": "-",
                  "probe": "-", "note": "語料尚未用到"})
        return audit(t, verbs)
    case("**護欄**：詞表登記語料未用之動詞 → 綠（詞表得先於語料）",
         extra_row, False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    v = corpus_verbs()
    bad = audit()
    print(f"詞表 {len(rows())} 列；語料首詞 {len(v)} 種、"
          f"{sum(v.values())} 處\n")
    print(f"違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    sys.exit(1 if bad else 0)
