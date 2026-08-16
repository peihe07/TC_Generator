#!/usr/bin/env python3
"""Corpus-wide verbatim survey (handoff 68 §4) — a MEASUREMENT, not a gate.

Two questions, asked over all TCs:

  1. How literally does each TC's first pre_condition quote the section it
     cites? Measured as the longest common verbatim run (autojunk=False, per
     profile §3.7.1) between the PC line and that section's full_text.
  2. Where do a TC's typographic characters differ from those of the section
     it belongs to? Measured as a SET DIFFERENCE in both directions against
     the section's own characters (69 §3.1) — no hand-listed pairs, so the
     coverage grows with the corpus rather than with the author's memory.

The first measurement produced 69 §1's ruling and is now enforced by the
`source-class-truthful` gate; this script keeps the distribution visible.
The second stays a measurement: a difference is a candidate, not a defect —
an ER that quotes a button name with " while the section happens to contain
a possessive apostrophe is a difference and nothing more.

Usage:
    python3 features/comfort/scripts/survey_verbatim.py
"""

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import lint_tcs as L

FEATURE = Path(__file__).resolve().parents[1]

# 69 §3.1 — no hand-listed pairs. The baseline is what the CITED SECTION
# actually contains: for each TC, take the set of non-ASCII / typographic
# characters in its section's full_text and the set in its own fields, and
# report the difference in both directions.
#
#   section has, TC lacks  -> possibly dropped (e.g. « » not carried through)
#   TC has, section lacks  -> possibly substituted (e.g. " written for ')
#
# The coverage grows with the corpus instead of with my memory of what to
# look for: 68 §4.5's six pairs were mine, and "zero hits" only meant zero
# hits among the six I had thought of.
TYPO_CLASS = {
    "«": "guillemet", "»": "guillemet",
    "\u2018": "curly quote", "\u2019": "curly quote",
    "\u201c": "curly quote", "\u201d": "curly quote",
    "\u2013": "dash", "\u2014": "dash", "\u2212": "dash",
    "\u2032": "prime", "\u2033": "prime",
    "\u00a0": "nbsp", "\u2026": "ellipsis", "\u00b0": "degree",
    "'": "straight quote", '"': "straight quote", "-": "hyphen",
}
# The pairs a substitution could plausibly involve, derived rather than
# enumerated: same class, different character.
def _same_class(a: str, b: str) -> bool:
    return (TYPO_CLASS.get(a) == TYPO_CLASS.get(b)
            or {TYPO_CLASS.get(a), TYPO_CLASS.get(b)}
            in ({"prime", "straight quote"}, {"curly quote", "straight quote"},
                {"dash", "hyphen"}))


def typographic(text: str) -> set:
    return {ch for ch in text if ch in TYPO_CLASS or ord(ch) > 127}


def main() -> int:
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted((FEATURE / "generated").glob("*.json"))]
    full = L.FULLTEXT_BY_OUTLINE

    rows = []
    for d in docs:
        for tc in d["tcs"]:
            head = tc["pre_conditions"].split("\n")[0]
            cite = re.search(r"\(([\d.]+)\)\s*$", head)
            src = cite.group(1) if cite else d["outline"]
            frag = re.sub(r"^\d+\.\s*\[[a-z-]+\]\s*", "", head)
            frag = re.sub(r"\s*\([\d.]+\)\s*$", "", frag)
            size, seg = L._longest_run(frag, full.get(src, ""))
            cls = head.split("]")[0].lstrip("0123456789. [")
            rows.append({"tc_id": tc["tc_id"],
                         "req_id": tc["req_id"].replace("SWE1-HVAC-", ""),
                         "outline": d["outline"], "cited": src,
                         "source_class": cls, "frag_len": len(frag),
                         "run": size, "ratio": round(size / max(1, len(frag)), 3),
                         "seg": seg})

    print(f"TCs measured: {len(rows)}\n")

    print("== 分佈：首行 PC 與其所引節之最長共同連續字串 ==")
    buckets = [(0, 9), (10, 19), (20, 39), (40, 59), (60, 99), (100, 10 ** 6)]
    for lo, hi in buckets:
        n = sum(1 for r in rows if lo <= r["run"] <= hi)
        label = f"{lo}–{hi}" if hi < 10 ** 6 else f"{lo}+"
        print(f"  run {label:>8} chars : {n:4}  {'#' * (n // 5)}")

    print("\n== 依 source class（首行 PC 之標記）==")
    for cls in sorted({r["source_class"] for r in rows}):
        sel = [r for r in rows if r["source_class"] == cls]
        runs = sorted(r["run"] for r in sel)
        med = runs[len(runs) // 2]
        print(f"  {cls:14} n={len(sel):4}  median run={med:4}  "
              f"min={runs[0]:4}  max={runs[-1]:4}")

    print("\n== 最短之 20 條（run 由小到大）==")
    for r in sorted(rows, key=lambda r: (r["run"], r["req_id"]))[:20]:
        print(f"  {r['req_id']:8} {r['tc_id']} {r['outline']:8} cited={r['cited']:8} "
              f"{r['source_class']:13} run={r['run']:3} / frag={r['frag_len']:3} "
              f"({r['ratio']:.2f})  seg={r['seg'][:34]!r}")

    print("\n== 字元層差集掃描（69 §3.1：基準為該節之實際字元集）==")
    dropped, substituted = [], []
    for d in docs:
        sec_chars = typographic(full.get(d["outline"], ""))
        for tc in d["tcs"]:
            blob = "\n".join((tc["pre_conditions"], tc["test_item"],
                               tc["test_procedure"], tc["expected_result"],
                               tc["tc_title"]))
            tc_chars = typographic(blob)
            for ch in sorted(sec_chars - tc_chars):
                dropped.append((tc["tc_id"], d["outline"], ch,
                                TYPO_CLASS.get(ch, "non-ascii")))
            for ch in sorted(tc_chars - sec_chars):
                near = [c for c in sec_chars if _same_class(c, ch)]
                substituted.append((tc["tc_id"], d["outline"], ch,
                                    TYPO_CLASS.get(ch, "non-ascii"), near))

    print(f"  節有而 TC 無（可能漏錄）：{len(dropped)} 筆")
    from collections import Counter
    for (o, ch, cls), n in Counter(
            (o, ch, cls) for _, o, ch, cls in dropped).most_common(12):
        rows_ = [t for t, oo, cc, _ in dropped if oo == o and cc == ch]
        print(f"    {o:8} {ch!r:8} {cls:14} {n:3} 條  {rows_[:4]}")

    risky = [x for x in substituted if x[4]]
    print(f"\n  TC 有而節無：{len(substituted)} 筆，"
          f"**其中 {len(risky)} 筆與該節之某字元同類（可能為代用）**")
    for tc_id, o, ch, cls, near in risky[:12]:
        print(f"    {tc_id} ({o}) TC 寫 {ch!r} [{cls}]，節用 {near}")
    if not risky:
        print("    （無同類代用之情形）")

    print(f"\n差集合計：漏錄 {len(dropped)} 筆、代用嫌疑 {len(risky)} 筆")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
