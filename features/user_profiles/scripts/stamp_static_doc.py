#!/usr/bin/env python3
"""靜態轉錄文件之指紋（G-F，45 包 §採納-1）。

## 為什麼不是只有 review pack 需要

44 輪為 review pack 加了指紋，其成因自陳為：
**把時效性當成「檢查」之性質，而它是任何靜態轉錄之性質。**

同型者尚有 **RD 查詢單**與**各批之 ER 出處對照** ——
兩者都逐字轉錄了語料之內容，而兩者都不隨重生成更新。

| 檔 | 轉錄了什麼 |
|---|---|
| `27_rd_queries_v2.md` | 各 leaf 之條文引述與我方對其之處置敘述 |
| `28_provenance4.md`／`34_provenance5.md` | 各條之引號字面值、欄位與其溯源結果 |

## 指紋之範圍：**保守取全欄**

review pack 之指紋只取「pack 印出來的欄位」，因為那份文件印了什麼是明確的。
本檔所涵蓋之三份**各印各的**（RD 單印條文與處置、出處對照印字面值），
逐份定義其範圍會產生三套判準，而**三套判準只要有一套劃錯，
那份文件就會在該欄變動時靜靜地維持「新鮮」**。

故一律取 `build_review_pack.pack_digest`（全欄 ＋ reasoning ＋ spec 原文）：
**保守之方向是安全的** —— 誤判過期只是多重出一次，
誤判新鮮則是拿舊資料下判斷。**兩種錯之代價不對稱。**

## 標的之辨識

文件內出現之 `NR1L-UserProfiles-NNN`（tc_id）與
`SWE1-HMI-PROF-...`（leaf id，映射為其 TC）皆計入。

Usage:
    python3 scripts/stamp_static_doc.py --stamp docs/upstream/34_provenance5.md
    python3 scripts/stamp_static_doc.py --verify docs/upstream/34_provenance5.md
    python3 scripts/stamp_static_doc.py --self-test
"""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_review_pack as RP                          # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
TCID = re.compile(r"NR1L-UserProfiles-(\d{3})")
LEAF = re.compile(r"SWE1-HMI-PROF-\d{3}(?:-\d{2})?(?:-[a-z]+)?")
BEGIN = "<!-- fingerprint:begin -->"
END = "<!-- fingerprint:end -->"
FP_ROW = re.compile(r"^\| `(NR1L-UserProfiles-\d{3})` \| `([0-9a-f]{12})` \|",
                    re.M)


def corpus() -> dict:
    """tc_id → (leaf 檔之 dict, tc)。"""
    out = {}
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out[t["tc_id"]] = (d, t)
    return out


def targets(text: str, corp: dict) -> list:
    """文件所轉錄之 tc_id（含經 leaf id 映射者），排序去重。"""
    ids = {f"NR1L-UserProfiles-{n}" for n in TCID.findall(text)}
    leaves = set(LEAF.findall(text))
    for tid, (_d, t) in corp.items():
        if t["req_id"] in leaves:
            ids.add(tid)
    return sorted(i for i in ids if i in corp)


def digests(text: str, corp: dict) -> dict:
    return {tid: RP.pack_digest(*corp[tid]) for tid in targets(text, corp)}


def block(dg: dict, rnd: int) -> str:
    lines = [BEGIN,
             f"## 語料指紋（G-F，45 包）—— 標記輪次：**{rnd}**",
             "",
             "> **本表是本檔之保鮮期。** 引用本檔前先跑："
             "`stamp_static_doc.py --verify <本檔>`；",
             "> **不符即「已過期，拒絕採信」**，須重出後再引。",
             "> 指紋之範圍為**全欄**（保守）—— 誤判過期只是多重出一次，"
             "誤判新鮮則是拿舊資料下判斷。",
             "",
             "| tc_id | digest |",
             "|---|---|"]
    lines += [f"| `{k}` | `{v}` |" for k, v in sorted(dg.items())]
    lines += ["", END, ""]
    return "\n".join(lines)


def stamp(path: Path, rnd: int = 45) -> int:
    corp = corpus()
    text = path.read_text(encoding="utf-8")
    dg = digests(text, corp)
    if not dg:
        print(f"{path.name}：未指涉任何語料條目 —— 不需指紋")
        return 0
    new = block(dg, rnd)
    if BEGIN in text:
        text = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?",
                      new, text, flags=re.S)
    else:
        lines = text.split("\n")
        i = next((k for k, l in enumerate(lines) if l.startswith("# ")), -1)
        at = i + 1 if i >= 0 else 0
        text = "\n".join(lines[:at + 1] + ["", new] + lines[at + 1:])
    path.write_text(text, encoding="utf-8")
    print(f"{path.name}：標記 {len(dg)} 條")
    return 0


def verify(path: Path) -> list:
    corp = corpus()
    text = path.read_text(encoding="utf-8")
    body = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), " ", text,
                  flags=re.S)
    stated = dict(FP_ROW.findall(text))
    if not stated:
        return [f"G-F `{path.name}` **無語料指紋** —— 一律視為過期，拒絕採信"]
    now = digests(body, corp)
    bad = []
    for tid, d in sorted(stated.items()):
        cur = now.get(tid)
        if cur is None:
            bad.append(f"G-F {tid}: 已不在語料內（或本檔已不再指涉之）")
        elif cur != d:
            bad.append(f"G-F {tid}: 指紋 `{d}` 與現況 `{cur}` 不符 "
                       f"—— **本檔之轉錄已過期，不得採信**")
    for tid in sorted(now):
        if tid not in stated:
            bad.append(f"G-F {tid}: 本檔指涉之而指紋表未載")
    return bad


def self_test() -> int:
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
        doc = Path(td) / "doc.md"
        doc.write_text("# 測試文件\n\n`NR1L-UserProfiles-135` 與 "
                       "`SWE1-HMI-PROF-037` 之轉錄。\n", encoding="utf-8")
        case("**未標記之文件 → 紅（一律視為過期）**",
             lambda: verify(doc), True)
        stamp(doc)
        case("**標記後 → 綠**", lambda: verify(doc), False)
        case("**護欄**：標記涵蓋 leaf id 所映射之條目",
             lambda: [] if len(FP_ROW.findall(
                 doc.read_text(encoding="utf-8"))) == 2 else ["映射數不符"],
             False)
        t = doc.read_text(encoding="utf-8")
        m = FP_ROW.search(t)
        doc.write_text(t.replace(f"`{m.group(2)}`", "`000000000000`", 1),
                       encoding="utf-8")
        case("**注入：某條指紋與語料不符 → 紅**", lambda: verify(doc), True)

        # 護欄：重複標記為冪等（不重複插入區塊）
        doc2 = Path(td) / "doc2.md"
        doc2.write_text("# 文件\n\n`NR1L-UserProfiles-135`\n", encoding="utf-8")
        stamp(doc2); stamp(doc2)
        n = doc2.read_text(encoding="utf-8").count(BEGIN)
        case("**護欄**：重複標記為冪等（只有一個指紋區塊）",
             lambda: [] if n == 1 else [f"指紋區塊 {n} 個"], False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stamp", default=None)
    ap.add_argument("--verify", default=None)
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if a.stamp:
        sys.exit(stamp(Path(a.stamp)))
    if a.verify:
        bad = verify(Path(a.verify))
        print(f"{Path(a.verify).name}：不符 {len(bad)} 條")
        for b in bad:
            print(f"  {b}")
        sys.exit(1 if bad else 0)
    ap.error("須給 --stamp／--verify／--self-test")
