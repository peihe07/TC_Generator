"""W-121（68 包 §3／§5）—— 適用性前言之判準結構化。

W-87 之判準自四式（初）→ 五式（A-VS109）→ 第六式（A-VS141），
**每次脫落都使 `generatable` 虛增，而修法一直是「再加一式」。**

新判準（68 包 §3）：
    該條文**無可測動詞** ∧ 含**條件性措辭**之任一

(1) 可測動詞之全集 —— 自**已交付 139 條之 `test_procedure`** 抽出其實際驗證之動詞
(2) 條件性措辭 —— `valid only if`／`applicable`／`applies`／`defines`／`covers`
(3) 錨點（R-VS54，**兩側皆須有標的**）
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

# 條件性措辭（68 包 §3 逐字）
CONDITIONAL = re.compile(
    r"valid\s+only\s+if|applicable|applies|defines|covers", re.I)

# 已知六式之實例（必命中錨點）—— 前五式由 W-87／A-VS109 立，第六式由 A-VS141 立
KNOWN_FORMS = [r"Following\s+requirements?\s+are\s+valid\s+only\s+if",
               r"The\s+requirements?\s+in\s+this\s+section\s+are\s+applicable",
               r"applicable\s+(?:for|to)\b[^.]{0,80}?\bonly\b",
               r"This\s+section\s+applies",
               r"This\s+section\s+defines",
               r"Also\s+the\s+requirements?\s+are\s+valid\s+only\s+if"]


def delivered_verbs() -> collections.Counter:
    """(1) 自已交付之 `test_procedure` 抽其實際驗證之動詞，成全集。

    取每個編號步驟之**主動詞**（`N. <Verb> …`），正規化為小寫原形。
    """
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    verbs: collections.Counter = collections.Counter()
    n = 0
    for v in groups.values():
        for tc in json.loads(max(v)[1].read_text(encoding="utf-8"))["tcs"]:
            n += 1
            for line in tc["test_procedure"].split("\n"):
                m = re.match(r"\s*\d+\.\s*([A-Za-z]+)", line)
                if m:
                    verbs[m.group(1).casefold()] += 1
    return verbs, n


def clause_verbs(text: str) -> set[str]:
    """條文側之可測動詞 —— `shall <verb>`／`has to <verb>` 之 verb。"""
    out = set()
    for m in re.finditer(r"\bshall\s+(?:not\s+)?([a-z]+)", text, re.I):
        out.add(m.group(1).casefold())
    for m in re.finditer(r"\bhas\s+to\s+([a-z]+)", text, re.I):
        out.add(m.group(1).casefold())
    return out


def is_preamble(text: str, testable: set[str]) -> bool:
    """新判準：無可測動詞 ∧ 含條件性措辭。"""
    flat = re.sub(r"\s+", " ", text)
    return not (clause_verbs(flat) & testable) and bool(CONDITIONAL.search(flat))


def main() -> None:
    verbs, ntc = delivered_verbs()
    # 條文側之動詞為 `shall <verb>`；procedure 側為祈使句主動詞。
    # 二者之交集即「該動詞確實被驗證過」—— 另補 procedure 所驗之同義形。
    proc_verbs = {v for v, c in verbs.items() if c >= 2}
    TESTABLE = proc_verbs | {"show", "send", "set", "display", "change", "maintain",
                             "activate", "enable", "disable", "update", "retain",
                             "transmit", "reflect", "behave", "close", "open"}
    print(f"(1) 已交付 **{ntc}** 條之 procedure 主動詞（出現 ≥2 次者 "
          f"{len(proc_verbs)}）：")
    for v, c in verbs.most_common(12):
        print(f"      {v:12s} ×{c}")
    print(f"\n    可測動詞全集（procedure 側 ∪ 條文側之 shall-動詞）："
          f"**{len(TESTABLE)}**\n")

    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"] for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}

    hit_new, hit_old = set(), set()
    old_re = [re.compile(p, re.I) for p in KNOWN_FORMS]
    for leaf in gen:
        qs = re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or ""))
        blks = [blocks[q] for q in qs if q in blocks]
        if not blks:
            continue
        if all(is_preamble(b["text"], TESTABLE) for b in blks):
            hit_new.add(leaf)
        if all(any(rx.search(re.sub(r"\s+", " ", b["text"])) for rx in old_re)
               for b in blks):
            hit_old.add(leaf)

    print(f"(3) 錨點")
    print(f"    必命中 —— 已知六式之實例 leaf **{len(hit_old)}**；"
          f"新判準涵蓋 **{len(hit_old & hit_new)}**   "
          f"{'PASS' if hit_old and hit_old <= hit_new else '⚠'}")
    for l in sorted(hit_old - hit_new):
        print("        未涵蓋:", l)
    # 必不命中：含可測動詞之條文
    ref = blocks.get("4858325")
    if ref:
        v = clause_verbs(re.sub(r"\s+", " ", ref["text"])) & TESTABLE
        ok = not is_preamble(ref["text"], TESTABLE)
        print(f"    必不命中 —— `4858325` 之可測動詞 {sorted(v)}；"
              f"判前言 = {not ok}   {'PASS，可失敗' if ok and v else '⚠'}")
    else:
        print("    必不命中 —— **`4858325` 不在母體，該側無標的**（R-VS54(2)）")
    print(f"\n    新判準命中之 leaf **{len(hit_new)}**；"
          f"其較舊式多 **{len(hit_new - hit_old)}**")
    for l in sorted(hit_new - hit_old):
        q = re.findall(r"\d{7}", l2r[l]["reqid_list"])[0]
        t = re.sub(r"\s+", " ", "\n".join(blocks[q]["text"].split("\n")[1:]).strip())
        print(f"        + {l:46s} {t[:78]}")
    (FEAT / "data/_w121_preamble.json").write_text(
        json.dumps({"new": sorted(hit_new), "old": sorted(hit_old),
                    "testable_verbs": sorted(TESTABLE)}, ensure_ascii=False, indent=1),
        encoding="utf-8")


if __name__ == "__main__":
    main()
