#!/usr/bin/env python3
"""Layer 3 map — one row per spec section the 037 cites (handoff 10 §4.1).

This is the INPUT to Part N, not Part N itself. Layer 2 Test Set derivation
and granularity are Tier 2 (FEATURE_ONBOARDING §0): the analysis layer drafts
them and Pei signs. Nothing here groups, names, or proposes a Test Set — it
reports what sections exist, what they are called, and how many 037 leaves
land on each, because a granularity decision cannot be made without that
distribution in front of you.

Scope of the map: the 129 sections cited by the 403 leaves. The 17
in-baseline `substantive` sections are NOT here — per R-C16 they are RD-1
coverage-gap items pending upstream 037 analysis, and per handoff 10 §4 they
do not enter Part N's partitioning population.

Assertions are mechanical and fail loud (R-C3 pattern): a map that silently
drops a section or a leaf would understate the population Part N is cut from,
and an understated denominator is the failure mode nobody notices.

Usage:
    python3 features/comfort/scripts/build_layer3_map.py
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
SYS1 = (ROOT / "spec-index" / "cache" /
        "SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023).xlsx")
OUT = FEATURE / "data" / "layer3_map.tsv"

TITLE_CHARS = 60

# handoff 10 §4.1 — the per-chapter distribution this map must reproduce.
# Declared here rather than recomputed from the same source it is meant to
# check: a self-derived expectation cannot fail.
EXPECTED_CHAPTERS = {
    "2": 92, "3": 14, "6": 1, "7": 38, "9": 8, "10": 15, "11": 37,
    "12": 22, "13": 14, "14": 40, "15": 2, "16": 99, "17": 18, "18": 3,
}
EXPECTED_ROWS = 129
EXPECTED_LEAVES = 403


def outline_key(s: str) -> tuple:
    return tuple(int(p) if p.isdigit() else -1 for p in str(s).split("."))


def parent_id(leaf: str) -> str:
    """SWE1-HVAC-001-02 -> SWE1-HVAC-001; SWE1-HVAC-011 -> itself.

    34 of the 403 leaves are parent-shaped and ARE themselves the requirement
    (R-C3) — stripping a suffix they do not have would mangle them.
    """
    return leaf.rsplit("-", 1)[0] if re.search(r"-\d\d$", leaf) else leaf


def load_titles() -> dict:
    wb = openpyxl.load_workbook(SYS1, read_only=True)
    rows = list(wb["Basic Report"].iter_rows(values_only=True))
    wb.close()
    out = {}
    for r in rows[1:]:
        if not r[2]:
            continue
        # Strip image refs and CRLF artefacts before truncating, so a title
        # is not 60 characters of "(image: %E5%9C%96...)".
        txt = re.sub(r"\(image:[^)]*\)", " ", str(r[3] or "")).replace("_x000D_", " ")
        out[str(r[2]).strip()] = re.sub(r"\s+", " ", txt).strip()
    return out


def main() -> None:
    recon = json.loads((FEATURE / "data" / "recon.json").read_text("utf-8"))
    sections = recon["sections"]          # {leaf_req_id: outline}
    titles = load_titles()

    per_section_leaves: dict = defaultdict(list)
    for leaf, outline in sections.items():
        per_section_leaves[outline].append(leaf)

    rows = []
    for outline in sorted(per_section_leaves, key=outline_key):
        leaves = sorted(per_section_leaves[outline])
        chapter = outline.split(".")[0]
        parents = sorted({parent_id(l) for l in leaves},
                         key=lambda x: (len(x), x))
        rows.append({
            "chapter": chapter,
            "chapter_title": titles.get(chapter, "(not in export)"),
            "outline": outline,
            "section_title": titles.get(outline, "(not in export)")[:TITLE_CHARS],
            "leaf_count": len(leaves),
            "req_ids": ",".join(parents),
        })

    hdr = ["chapter", "chapter_title", "outline", "section_title",
           "leaf_count", "req_ids"]
    OUT.write_text(
        "\n".join(["\t".join(hdr)] +
                  ["\t".join(str(r[h]).replace("\t", " ") for h in hdr)
                   for r in rows]) + "\n", encoding="utf-8")

    # ------------------------------------------------------------ assertions
    got_chapters = Counter()
    for r in rows:
        got_chapters[r["chapter"]] += r["leaf_count"]
    total = sum(r["leaf_count"] for r in rows)

    checks = [
        ("leaf_count sum == 403", EXPECTED_LEAVES, total, ""),
        ("row count == 129", EXPECTED_ROWS, len(rows), ""),
    ]
    mismatched = {c: (EXPECTED_CHAPTERS.get(c), got_chapters.get(c))
                  for c in set(EXPECTED_CHAPTERS) | set(got_chapters)
                  if EXPECTED_CHAPTERS.get(c) != got_chapters.get(c)}
    checks.append((
        "per-chapter distribution matches upstream 01 §3",
        "all 14 chapters equal",
        "all 14 chapters equal" if not mismatched else f"mismatch {mismatched}",
        f"{len(EXPECTED_CHAPTERS)} chapters compared: "
        + "、".join(f"{c}:{got_chapters.get(c, 0)}"
                   for c in sorted(EXPECTED_CHAPTERS, key=int))))

    failed = 0
    print(f"{len(rows)} sections written to {OUT.relative_to(ROOT)}\n")
    print("assertions:")
    for name, expected, actual, note in checks:
        ok = expected == actual
        failed += not ok
        print(f"- {'PASS' if ok else '**FAIL**'} — {name}: "
              f"expected `{expected}`, measured `{actual}`"
              + (f" — {note}" if note else ""))
    if failed:
        sys.exit(f"\nFAILED: {failed} assertion(s); the map does not describe "
                 "the surveyed population and must not feed Part N.")


if __name__ == "__main__":
    main()
