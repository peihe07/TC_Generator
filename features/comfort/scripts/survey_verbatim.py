#!/usr/bin/env python3
"""Corpus-wide verbatim survey (handoff 68 §4) — a MEASUREMENT, not a gate.

Two questions, asked over all TCs:

  1. How literally does each TC's first pre_condition quote the section it
     cites? Measured as the longest common verbatim run (autojunk=False, per
     profile §3.7.1) between the PC line and that section's full_text.
  2. Where do the corpus's characters differ from the spec's — `12'` vs
     `12"`, straight vs curly quotes, the presence or absence of «».

No gate is created. "The PC must quote verbatim" is NOT a corpus-wide
obligation: R-C28 Q1 asks for an explicit correspondence, which a paraphrase
can satisfy; R-C42 一's verbatim requirement is limited to clause-carried
conditions. Measure first, then decide who the requirement should bind.

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

# The spec's own characters, and what the corpus sometimes writes instead.
CHAR_PAIRS = [
    ("12'", '12"', "inch mark: the spec writes an apostrophe"),
    ("«", "<<", "guillemets: the spec uses « »"),
    ("»", ">>", "guillemets: the spec uses « »"),
    ("’", "'", "curly apostrophe vs straight"),
    ("“", '"', "curly double quote vs straight"),
    ("”", '"', "curly double quote vs straight"),
]


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

    print("\n== 字元層訛誤掃描 ==")
    hits = 0
    for spec_form, corpus_form, why in CHAR_PAIRS:
        secs = [o for o, t in full.items() if spec_form in t]
        if not secs:
            print(f"  {spec_form!r:8} 不出現於任何節，略過（{why}）")
            continue
        bad_rows = []
        for d in docs:
            for tc in d["tcs"]:
                blob = "\n".join((tc["pre_conditions"], tc["test_item"],
                                  tc["test_procedure"], tc["expected_result"]))
                if corpus_form in blob and d["outline"] in secs:
                    bad_rows.append((tc["tc_id"], d["outline"]))
        hits += len(bad_rows)
        print(f"  spec {spec_form!r} / corpus {corpus_form!r} — {why}")
        print(f"      spec 端出現於 {secs}；corpus 端誤寫 {len(bad_rows)} 處"
              f"{': ' + str(bad_rows[:6]) if bad_rows else ''}")
    # « » presence: are the spec's guillemets carried through?
    g_secs = [o for o, t in full.items() if "«" in t]
    carried, dropped = [], []
    for d in docs:
        if d["outline"] not in g_secs:
            continue
        for tc in d["tcs"]:
            blob = "\n".join((tc["test_item"], tc["expected_result"]))
            (carried if "«" in blob else dropped).append(tc["tc_id"])
    print(f"\n  «» 之承載：spec 端 {len(g_secs)} 節使用之；"
          f"其 TC 中 {len(carried)} 條照錄、{len(dropped)} 條未含")
    print(f"      未含者：{dropped}")
    print(f"\n字元訛誤合計：{hits} 處")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
