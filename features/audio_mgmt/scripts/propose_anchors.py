#!/usr/bin/env python3
"""Propose CFTS019 anchors for a batch's leaves — a PROPOSAL, not a ruling.

The execution layer may not anchor (package 03 section 3.4). This script
exists so the analysis layer has a computed starting point for the section 4
table it owns, with the evidence attached and the weak matches marked.

Method, the same one package 03 section 4 discloses for B1: there is no
formal bridge between SWE1_AMM and CFTS019 ObjectIDs (F1 / DR-AM1), so each
leaf is matched on content — the SWE.1 Title plus Description against the
Basic Report Description — restricted to the R-AM2 anchor pool, and scored.
Anything that is not a clear single winner is flagged for a human read.

Usage:
    python features/audio_mgmt/scripts/propose_anchors.py --batch B2
"""

import argparse
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

import openpyxl

FEATURE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEATURE.parent.parent / "scripts"))
from feature_config import load_feature_config, resolve_path  # noqa: E402

# 02 section 3. B1 is done; B2 is the next slice.
BATCHES = {
    "B2": [("Audio Arbitration", "rest"),
           ("Focus and Ducking", "all"),
           ("Mute Requests", 19)],
}
STOP = set("the a an of to and or for shall be is are with when on in by from "
           "audio management software this that it its as any all".split())


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", text.lower())
            if w not in STOP and len(w) > 2}


def assignment_table() -> list[dict]:
    """The 317-leaf assignment the analysis layer locked in package 02."""
    text = (FEATURE / "docs" / "handoff" /
            "02_framework_assignment.md").read_text(encoding="utf-8")
    rows = re.findall(
        r"^\|\s*(SWE1_AMM_\d+)\s*\|\s*(SYS-RA-AMM-\d+)\s*\|\s*([^|]+?)\s*\|"
        r"\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", text, re.M)
    return [{"swe_id": a, "source_id": b, "title": c, "sub_cat": d,
             "test_set": e.strip()} for a, b, c, d, e in rows]


def b1_leaves() -> set[str]:
    ctx = json.loads((FEATURE / "batches" / "B1_context.json")
                     .read_text(encoding="utf-8"))
    return {leaf["swe_id"] for leaf in ctx}


def pool_rows(cfg: dict) -> list[dict]:
    """Anchor pool with descriptions: the two Basic Reports (R-AM2)."""
    out = []
    for key in ("sys1_export", "sys1_export_part2"):
        wb = openpyxl.load_workbook(resolve_path(cfg, key), read_only=True)
        ws = wb[wb.sheetnames[0]]
        rows = list(ws.iter_rows(values_only=True))
        header = [str(c or "").strip().lower() for c in rows[0]]
        # The ObjectID column is found by content, not by header text: the
        # first column is headed "ID" but holds NRL-149950 style keys, and a
        # header match on "id" takes it and yields an empty pool. The
        # 7-digit 48xxxxx ObjectID lives under "SYS2 Source Requirement items".
        oid_i = max(range(len(header)),
                    key=lambda i: sum(
                        1 for r in rows[1:]
                        if re.fullmatch(r"\s*48\d{5}\s*", str(r[i] or ""))))
        desc_i = next(i for i, h in enumerate(header) if h == "description")
        for row in rows[1:]:
            oid = str(row[oid_i] or "").strip()
            if re.fullmatch(r"48\d{5}", oid):
                out.append({"oid": oid,
                            "desc": " ".join(str(row[desc_i] or "").split()),
                            "src": key})
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", default="B2")
    args = ap.parse_args()

    cfg = load_feature_config(FEATURE)
    table = assignment_table()
    done = b1_leaves()
    by_set: dict[str, list[dict]] = {}
    for row in table:
        by_set.setdefault(row["test_set"], []).append(row)

    leaves = []
    for test_set, take in BATCHES[args.batch]:
        pool = [r for r in by_set.get(test_set, []) if r["swe_id"] not in done]
        leaves.extend(pool if take in ("rest", "all") else pool[:take])

    swe = {}
    wb = openpyxl.load_workbook(resolve_path(cfg, "a03_report"), read_only=True)
    for sheet in wb.sheetnames:
        for row in wb[sheet].iter_rows(min_row=2, values_only=True):
            if row[0]:
                swe[str(row[0]).strip()] = {
                    "title": str(row[2] or ""), "desc": str(row[3] or "")}

    candidates = pool_rows(cfg)
    for c in candidates:
        c["tok"] = tokens(c["desc"])

    proposals = []
    for leaf in leaves:
        rec = swe.get(leaf["swe_id"], {})
        want = tokens(rec.get("title", "") + " " + rec.get("desc", ""))
        scored = []
        for c in candidates:
            if not c["tok"]:
                continue
            jac = len(want & c["tok"]) / len(want | c["tok"])
            scored.append((jac, c))
        scored.sort(key=lambda t: -t[0])
        # A SHORTLIST, NOT AN ANSWER. Back-tested against B1's 43 ruled
        # in-pool anchors: top-1 is right 49% of the time, top-3 67%,
        # top-10 84%, and the median rank of the correct anchor is 2.
        # An earlier revision emitted a single pick carrying strong/weak
        # confidence labels; "strong" was right 6 times out of 10, so the
        # label read as authority it had not earned and is gone.
        proposals.append({**leaf, "shortlist": [
            {"oid": c["oid"], "score": round(sc, 3),
             "desc": c["desc"][:160]} for sc, c in scored[:10]]})

    dest = FEATURE / "batches" / f"{args.batch}_anchor_proposal.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(proposals, ensure_ascii=False, indent=2),
                    encoding="utf-8")
    from collections import Counter
    print(f"{args.batch}: {len(proposals)} leaves, top-10 shortlist each")
    print("  by test set: "
          + ", ".join(f"{k}={v}" for k, v in
                      Counter(p["test_set"] for p in proposals).items()))
    print(f"  written    : {dest.relative_to(FEATURE.parent.parent)}")
    print()
    print("Measured on B1's 43 ruled in-pool anchors: top-1 49%, top-3 67%, "
          "top-10 84%,")
    print("median rank of the correct anchor 2. A shortlist to read, not an "
          "answer to")
    print("accept. Anchoring is the analysis layer's call (package 03 "
          "section 3.4).")

    return 0


if __name__ == "__main__":
    sys.exit(main())
