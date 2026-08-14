#!/usr/bin/env python3
"""Classify the SR24 baseline sections that the 037 does NOT cite (A-CF08).

Handoff 03 §3 asks for the 51 uncited sections of the ruled SR24 baseline to
be classified into exactly four values. These sections are NOT the R-C5 case:
R-C5 disposes of content in an out-of-scope document (SR25), while these sit
inside the in-scope baseline and are simply unanalysed by the 037.

Classification values and their handoff definitions:
  container    章級容器標題，其下層節已被引用
  assumption   1.x 類範圍聲明，非可驗證需求
  figure       內容僅為 image 參照，無行為敘述
  substantive  含行為敘述（含 shall／will／編號條款前綴如 C1.)、ICE2.)）
               而未被 037 引用

CLASSIFY ONLY. No TC disposition is made or implied here: nothing is
generated, nothing enters a coverage denominator, nothing is marked BLOCKED,
and no RD item is invented (§8.2, §8.4.2). What happens to the `substantive`
rows is Pei's to rule, after this list exists.

Usage:
    python3 features/comfort/scripts/classify_uncited_sections.py
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features" / "comfort"
SYS1 = (ROOT / "spec-index" / "cache" /
        "SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023).xlsx")
OUT_TSV = FEATURE / "data" / "sr24_uncited_sections.tsv"

# A numbered clause prefix as the spec writes them: C1.) ICE2.) CRB1.1)
# BCW2.) W0.) LCW1.) — a letter-run, digits, an optional dotted sub-number,
# then a closing paren. This is the spec's own marker for "this paragraph is
# a requirement", which is why it is the primary substantive signal.
CLAUSE_RE = re.compile(r"^[A-Z][A-Za-z]{0,4}\d+(?:\.\d+)*\.?\)")
# Deontic verbs. Deliberately NOT including "will" or "should": chapter 1 uses
# "Differences between the radios will be specified" and "the 12\" Portrait UI
# will be a scaled up version" — statements about the DOCUMENT and about
# scaling conventions, not about system behaviour. Treating a bare "will" as
# a requirement marker would move all eight Assumptions into `substantive`
# and destroy the distinction the classification exists to draw.
DEONTIC_RE = re.compile(r"\b(shall|must)\b", re.I)

TITLE_LIKE_MAX = 80   # chars of prose that still read as a heading/caption


def load_rows() -> list[tuple[str, str, str]]:
    wb = openpyxl.load_workbook(SYS1, read_only=True)
    rows = list(wb["Basic Report"].iter_rows(values_only=True))
    wb.close()
    return [(str(r[2]).strip(), str(r[0] or "").strip(), str(r[3] or ""))
            for r in rows[1:] if r[2]]


def bare_text(desc: str) -> str:
    """Description with image references and CRLF artefacts removed."""
    s = re.sub(r"\(image:[^)]*\)", " ", desc).replace("_x000D_", " ")
    return re.sub(r"\s+", " ", s).strip()


def classify(outline: str, desc: str, has_children: bool) -> tuple[str, str]:
    """Return (value, why). Order matters: substantive is tested first so a
    heading that also states a requirement is not filed away as a container."""
    bare = bare_text(desc)
    has_image = "(image:" in desc
    if CLAUSE_RE.match(bare):
        return "substantive", f"numbered clause prefix {bare.split(')')[0]})"
    if DEONTIC_RE.search(bare):
        m = DEONTIC_RE.search(bare)
        return "substantive", f"deontic verb '{m.group(1)}' in prose"
    if has_children and not has_image and len(bare) <= TITLE_LIKE_MAX:
        return "container", "heading with descendants, no prose of its own"
    if has_image and len(bare) <= TITLE_LIKE_MAX:
        return "figure", "image reference with title-length caption only"
    return "assumption", "scope/applicability statement, no behavioural claim"


def main() -> None:
    recon = json.loads((FEATURE / "data" / "recon.json").read_text("utf-8"))
    cited = set(recon["distinct_sections"])
    rows = load_rows()
    outlines = [o for o, _, _ in rows]

    def children(o: str) -> list[str]:
        return [x for x in outlines if x.startswith(o + ".")]

    uncited = [(o, pid, d) for o, pid, d in rows if o not in cited]

    out = ["outline\tpolarion_id\tdescription_80\tclassification\t"
           "cited_descendants\ttotal_descendants\twhy"]
    counts: Counter = Counter()
    deviations = []
    for o, pid, desc in uncited:
        kids = children(o)
        kids_cited = [k for k in kids if k in cited]
        value, why = classify(o, desc, bool(kids))
        counts[value] += 1
        # The handoff's `container` definition has two halves: "chapter-level
        # heading" AND "its sub-sections are cited". Five headings satisfy the
        # first and not the second — their whole subtree is uncited. They are
        # still headings, so they are filed as container, but the miss is
        # recorded per row rather than smoothed over.
        if value == "container" and not kids_cited:
            deviations.append(o)
        out.append("\t".join([
            o, pid, bare_text(desc)[:80].replace("\t", " "), value,
            str(len(kids_cited)), str(len(kids)), why]))

    OUT_TSV.write_text("\n".join(out) + "\n", encoding="utf-8")
    total = sum(counts.values())
    print(f"{total} uncited sections written to {OUT_TSV.relative_to(ROOT)}")
    for k in ("container", "assumption", "figure", "substantive"):
        print(f"  {k:<12} {counts[k]}")
    if total != len(uncited):
        sys.exit("count mismatch — every uncited section must get exactly one value")
    print(f"  container rows with ZERO cited descendants: {deviations}")


if __name__ == "__main__":
    main()
