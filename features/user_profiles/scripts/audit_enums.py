#!/usr/bin/env python3
"""枚舉型判準之對照（G-B，42 包 §二）。

> `STATE_VALUES`（寫死四個）與 `UI_LOCATORS`（寫死兩個）接上 **VB-2 同型之對照**：
> 以語料實際出現之值回頭比對清單，未入清單者掃描結果不予採認。
> `KNOWN_PU` 與 `DESIGN_METHODS` 為現測，不須。

## 兩張清單之風險方向不同，故兩項檢查不同

| 清單 | 漏一個會怎樣 | 故對照取自 |
|---|---|---|
| `STATE_VALUES` | 該值**永遠不被溯源** —— G18 只查清單上的字，**靜靜通過** | **spec 側**：條文自己標出來的顯示值 |
| `UI_LOCATORS` | 漏了會**轉紅**（G18 溯不到源）；真正的風險是**多了** —— 一個被誤登記者從此免溯源 | **語料側**：跨節重複出現之引號字面值 |

**為什麼 `STATE_VALUES` 之對照不取自語料**：語料側之「首字大寫且非句首」
有 142 個相異 token（實測），登記它們是造一張沒人維護得動的表 ——
**而那種表會被關掉**。spec 側之候選只有十個，且其判準（條文自己加了引號，
或寫在 `turned／set to／default` 之後）就是「顯示值」這個概念本身。

## 兩項

| # | 檢查 | 性質 |
|---|---|---|
| EN-1 | spec 側之顯示值候選中，凡**也出現於語料 ER** 者，須在 `STATE_VALUES` 內或登記為 `not-a-state-value` | 紅 |
| EN-2 | 語料中**跨 ≥2 節**出現之引號字面值，須在 `UI_LOCATORS` 內或登記為 `not-a-locator` | 紅 |

兩項另各驗其清單**不說謊**：`STATE_VALUES` 之每個值須真在 spec 內；
`UI_LOCATORS` 之每個值須真在其登記節次之 `pdf_text` 內
（後者 `lint_tcs` 已驗，此處不重複實作，改驗其登記於本檔之對照表內）。

## 盲區（R-G11）

spec 側之候選判準只認**兩種形態**（引號內單字、`turned/set to/default` 之後）。
一個以第三種形態寫出的顯示值（例：表格某欄之列值）不在候選內 ——
本檔看不見它，`lint_tcs` 也看不見。**這是本對照之上界，不是它的失效。**

Usage:
    python3 scripts/audit_enums.py
    python3 scripts/audit_enums.py --self-test
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

FEATURE = Path(__file__).resolve().parent.parent
VOCAB = FEATURE / "data" / "enum_vocab.tsv"

SPEC_QUOTED = re.compile(r"[“\"]([A-Za-z][A-Za-z]*)[”\"]")
SPEC_VALUE_POS = re.compile(
    r"\b(?:turned|set to|defaults? (?:to|on)|switched)\s+([A-Za-z][a-z]+)\b",
    re.I)
# `turned/set to/default` 之後未必是值（`turned while`、`set to the`）——
# 這些是文法用字，不是顯示值。逐字列出，不以詞性猜。
POS_STOP = {"within", "while", "the", "a", "an", "it", "them", "this"}


def vocab() -> list:
    with VOCAB.open(encoding="utf-8") as fh:
        rd = csv.DictReader((l for l in fh if not l.startswith("#")),
                            delimiter="\t")
        return [r for r in rd if r.get("value")]


def spec_candidates() -> set:
    """spec 側之顯示值候選（**大小寫保留原形**，比對時不敏感）。"""
    import build_batch_context as B
    out = set()
    for v in B._outline().values():
        txt = v.get("pdf_text") or ""
        out |= set(SPEC_QUOTED.findall(txt))
        out |= {w for w in SPEC_VALUE_POS.findall(txt)
                if w.lower() not in POS_STOP}
    return out


def corpus_rows() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append((d["outline"], t))
    return out


def corpus_literals(rows) -> dict:
    """引號字面值 → 出現之節次集合。"""
    import lint_tcs as L
    occ = {}
    for sec, t in rows:
        for fld in ("expected_result", "pre_conditions"):
            for lit in L.QUOTED_RE.findall(str(t.get(fld, ""))):
                occ.setdefault(lit.strip(), set()).add(sec)
    return occ


def audit(rows=None, voc=None, spec=None, state_values=None) -> list:
    import lint_tcs as L
    rows = corpus_rows() if rows is None else rows
    voc = vocab() if voc is None else voc
    spec = spec_candidates() if spec is None else spec
    sv = tuple(L.STATE_VALUES) if state_values is None else tuple(state_values)
    bad = []

    reg = {(r["kind"], r["value"].lower()): r for r in voc}
    er_blob = " ".join(str(t.get("expected_result", "")) for _s, t in rows)

    # ── EN-1
    for cand in sorted(spec):
        if not re.search(rf"\b{re.escape(cand)}\b", er_blob, re.I):
            continue                       # 語料未用到，不必登記
        if any(cand.lower() == x.lower() for x in sv):
            if ("state_value", cand.lower()) not in reg:
                bad.append(f"EN-1 `{cand}` 在 `STATE_VALUES` 內而未登記於 "
                           f"`enum_vocab.tsv` —— 清單與對照表分岔")
            continue
        r = reg.get(("state_value", cand.lower()))
        if r is None:
            bad.append(f"EN-1 spec 側之顯示值 `{cand}` 出現於語料 ER，"
                       f"而**既不在 `STATE_VALUES` 內亦未登記** "
                       f"—— 掃描結果不予採認")
        elif r["status"] == "registered":
            bad.append(f"EN-1 `{cand}` 登記為 registered，"
                       f"而它不在 `STATE_VALUES` 內 —— 登記表說謊")

    # ── 清單不說謊：`STATE_VALUES` 之每個值須真在 spec 之候選內
    for x in sv:
        if not any(x.lower() == c.lower() for c in spec):
            bad.append(f"EN-1 `STATE_VALUES` 之 `{x}` 不在 spec 側之候選內 "
                       f"—— 該值之來源已不存在")

    # ── EN-2
    for lit, secs in sorted(corpus_literals(rows).items()):
        if len(secs) < 2:
            continue
        if lit in L.UI_LOCATORS:
            if ("ui_locator", lit.lower()) not in reg:
                bad.append(f"EN-2 `{lit}` 在 `UI_LOCATORS` 內而未登記於 "
                           f"`enum_vocab.tsv`")
            continue
        r = reg.get(("ui_locator", lit.lower()))
        if r is None:
            bad.append(f"EN-2 跨 {len(secs)} 節出現之字面值 「{lit[:40]}」 "
                       f"**既不在 `UI_LOCATORS` 內亦未登記** "
                       f"—— 掃描結果不予採認")
        elif r["status"] == "registered":
            bad.append(f"EN-2 「{lit[:40]}」 登記為 registered，"
                       f"而它不在 `UI_LOCATORS` 內 —— 登記表說謊")

    # ── 登記表之 note 不得空白
    for r in voc:
        if not (r.get("note") or "").strip():
            bad.append(f"EN-0 `{r['value'][:30]}` 之 note 空白 —— 理由須具名")
    return bad


def self_test() -> int:
    import lint_tcs as L
    rows, voc, spec = corpus_rows(), vocab(), spec_candidates()
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

    case("現行語料 ＋ 現行登記表 → 綠",
         lambda: audit(rows, voc, spec), False)

    # EN-1 —— **本組最關鍵**：spec 新增一個顯示值而語料用了它
    def new_spec_value():
        r2 = [(s, dict(t)) for s, t in rows]
        r2[0][1]["expected_result"] = "1. The setting is Large"
        return audit(r2, voc, spec | {"Large"})
    case("**EN-1 注入：spec 出現新顯示值 `Large` 且語料用了它 → 紅**",
         new_spec_value, True)

    # EN-1 —— 清單少一個（`Off` 被自 STATE_VALUES 移除）
    case("EN-1 注入：`Off` 自 `STATE_VALUES` 移除 → 紅（登記表說它 registered）",
         lambda: audit(rows, voc, spec,
                       [x for x in L.STATE_VALUES if x != "Off"]), True)

    # EN-1 —— 清單多一個（其來源不存在）
    case("EN-1 注入：`STATE_VALUES` 多一個 spec 沒有的 `Bright` → 紅",
         lambda: audit(rows, voc, spec, list(L.STATE_VALUES) + ["Bright"]),
         True)

    # EN-2 —— 語料出現一個跨節之新字面值而未登記
    def new_locator():
        # **須取兩個不同 outline 之列** —— 首跑取 `rows[0]`／`rows[1]`，
        # 而那兩條同屬 4.1，`len(secs) < 2` 遂不觸發。案例沒壞，是取樣取錯了。
        r2 = [(s, dict(t)) for s, t in rows]
        seen, picked = set(), []
        for i, (sec, _t) in enumerate(r2):
            if sec not in seen:
                seen.add(sec)
                picked.append(i)
            if len(picked) == 2:
                break
        for i in picked:
            r2[i][1]["expected_result"] = '1. The “Quick Menu” is displayed'
        return audit(r2, voc, spec)
    case("**EN-2 注入：跨兩節之新字面值 “Quick Menu” 未登記 → 紅**",
         new_locator, True)

    # EN-0 —— note 空白
    def blank_note():
        v2 = [dict(r) for r in voc]
        v2[0]["note"] = ""
        return audit(rows, v2, spec)
    case("EN-0 注入：登記表某列之 note 空白 → 紅", blank_note, True)

    # 護欄：只出現於單一節之字面值不必登記
    def single_section():
        r2 = [(s, dict(t)) for s, t in rows]
        r2[0][1]["expected_result"] = '1. The “Rear Camera” is displayed'
        return audit(r2, voc, spec)
    case("**護欄**：只出現於一節之字面值 → 綠（G18 自會溯源）",
         single_section, False)

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
    rows = corpus_rows()
    spec = spec_candidates()
    bad = audit(rows)
    print(f"登記表 {len(vocab())} 列；spec 側顯示值候選 {len(spec)} 個"
          f"；語料跨節字面值 "
          f"{sum(1 for _l, s in corpus_literals(rows).items() if len(s) >= 2)} 個\n")
    print(f"違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    sys.exit(1 if bad else 0)
