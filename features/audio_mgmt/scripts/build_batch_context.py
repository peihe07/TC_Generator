#!/usr/bin/env python3
"""Assemble the generation context for an audio_mgmt batch.

For every leaf in the batch this pulls together, from ruled sources only:
  - the SWE.1 row (Requirement Description is the verbatim source for the
    upper half of test_item per package 03 section 3.2 / IN R-S4)
  - the CFTS019 anchor text, looked up by ObjectID in the full-text PDF
  - the sibling axis the leaf sits on (package 03 section 5)

Anchors are read from the package 03 section 4 table and never recomputed:
the execution layer may not re-anchor (package 03 section 3.4). Leaves whose
anchor falls outside the R-AM2 pool are carried with `anchor_in_pool: false`
so the generator can hold them back (A-AM03).

Usage:
    python features/audio_mgmt/scripts/build_batch_context.py --batch B1
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT.parent.parent / "scripts"))

from feature_config import load_feature_config, resolve_path  # noqa: E402

HANDOFF = {"B1": ROOT / "docs" / "handoff" / "03_batch_B1_handoff.md",
           "B2": ROOT / "docs" / "handoff" / "08_B2_final_anchors.md"}

# Package 03 section 5. Each leaf carries the axes it belongs to so the
# generator can differentiate tc_title tokens within a family.
SIBLING_AXES = {
    "Ent->Ent transition": ["SWE1_AMM_205", "SWE1_AMM_206", "SWE1_AMM_208",
                            "SWE1_AMM_209", "SWE1_AMM_212"],
    "Ent->Info transition": ["SWE1_AMM_156", "SWE1_AMM_224"],
    "Info1->Info2 transition": ["SWE1_AMM_157", "SWE1_AMM_241"],
    "activation/deactivation sequence": [
        "SWE1_AMM_132", "SWE1_AMM_133", "SWE1_AMM_134", "SWE1_AMM_135",
        "SWE1_AMM_136", "SWE1_AMM_137", "SWE1_AMM_138",
        "SWE1_AMM_142", "SWE1_AMM_143", "SWE1_AMM_144"],
    "SOS mute/restore near-duplicate pair": [
        "SWE1_AMM_198", "SWE1_AMM_199", "SWE1_AMM_218", "SWE1_AMM_219"],
    "queue determination, same text different anchor": [
        "SWE1_AMM_130", "SWE1_AMM_139"],
    "boundary value candidates (25ms/50ms)": [
        "SWE1_AMM_275", "SWE1_AMM_276", "SWE1_AMM_277", "SWE1_AMM_278"],
    # Package 08 section 3. The amplifier-type pairs carry the same clause
    # text at two anchors, so the distinguishing token has to name the
    # amplifier; 234/235 pair across batches with B1's 226/227.
    "1.3.3.17 non-amplifier / booster": [
        "SWE1_AMM_229", "SWE1_AMM_230", "SWE1_AMM_231", "SWE1_AMM_232",
        "SWE1_AMM_234", "SWE1_AMM_235"],
    "1.3.3.18 CAN amplifier": [
        "SWE1_AMM_236", "SWE1_AMM_237", "SWE1_AMM_238", "SWE1_AMM_239"],
    "navigation fade-out chain": [
        "SWE1_AMM_312", "SWE1_AMM_313", "SWE1_AMM_314", "SWE1_AMM_315",
        "SWE1_AMM_316", "SWE1_AMM_317"],
    "ENTMuted indication, same text different anchor": [
        "SWE1_AMM_058", "SWE1_AMM_066"],
    "VSIM mute group": ["SWE1_AMM_179", "SWE1_AMM_180", "SWE1_AMM_181",
                        "SWE1_AMM_182"],
    "VSIM unmute group": ["SWE1_AMM_184"],
    "source selection shared anchor (R-AM16)": [
        "SWE1_AMM_031", "SWE1_AMM_032"],
    "TLM mute without ICS node": ["SWE1_AMM_068", "SWE1_AMM_069",
                                  "SWE1_AMM_078", "SWE1_AMM_079"],
}

ROW_RE = re.compile(
    r"^\|\s*(SWE1_AMM_\d+)\s*\|\s*(SYS-RA-AMM-\d+)\s*\|\s*([^|]+?)\s*\|"
    r"\s*([^|]+?)\s*\|\s*CFTS019-(\d+)\s*\|\s*([^|]+?)\s*\|", re.M)
# Package 08 tabulates leaf, anchor, pool and coverage, under a heading per
# test set. A leaf may carry more than one anchor (SWE1_AMM_032 under R-AM16),
# so the anchor cell is parsed as a list rather than a single id.
ROW_RE_B2 = re.compile(
    r"^\|\s*(SWE1_AMM_\d+)\s*\|\s*((?:CFTS019-\d+[^|]*?))\|\s*([✓✗])\s*\|"
    r"\s*([^|]+?)\s*\|", re.M)
SET_RE = re.compile(r"^### (.+?)（\d+ 葉）", re.M)


def parse_handoff(batch: str) -> list[dict]:
    """Read the batch's leaf/anchor table out of its handoff package."""
    text = HANDOFF[batch].read_text(encoding="utf-8")
    if batch == "B1":
        return [{"swe_id": m.group(1), "source_id": m.group(2),
                 "title": m.group(3), "test_set": m.group(4),
                 "anchors": [m.group(5)], "coverage": "完整",
                 "anchor_note": m.group(6)}
                for m in ROW_RE.finditer(text)]

    section = text[text.index("## 一、定案錨表"):text.index("## 二、逐案處置")]
    # Walk the section so each row picks up the test set heading above it.
    bounds = [(m.start(), m.group(1)) for m in SET_RE.finditer(section)]
    out = []
    for m in ROW_RE_B2.finditer(section):
        test_set = next((name for pos, name in reversed(bounds)
                         if pos < m.start()), "")
        out.append({
            "swe_id": m.group(1),
            "anchors": re.findall(r"CFTS019-(\d+)", m.group(2)),
            "anchor_in_pool_ruled": m.group(3) == "✓",
            "coverage": " ".join(m.group(4).split()),
            "test_set": test_set.strip()})
    return out


def swe_rows(cfg: dict) -> dict[str, list[dict]]:
    """Every SWE.1 row across all four sheets, keyed by SWE ID.

    A list per key: SWE1_AMM_076 legitimately has two rows (R-AM6).
    """
    cols = {"swe_id": 0, "source_id": 1, "title": 2, "description": 3,
            "status": 4, "categorization": 6, "sub_categorization": 7,
            "priority": 16, "verification_criteria": 17,
            "verification_method": 18}
    wb = openpyxl.load_workbook(resolve_path(cfg, "a03_report"), read_only=True)
    out: dict[str, list[dict]] = {}
    for sheet in wb.sheetnames:
        for row in wb[sheet].iter_rows(min_row=2, values_only=True):
            if not row[0]:
                continue
            rec = {k: ("" if row[i] is None else str(row[i]).strip())
                   for k, i in cols.items()}
            rec["sheet"] = sheet.replace("Audio-Management ", "")
            out.setdefault(rec["swe_id"], []).append(rec)
    return out


def spec_blocks(cfg: dict) -> dict[str, str]:
    """ObjectID -> its clause text from the CFTS019 full-text PDF."""
    pdf = resolve_path(cfg, "spec_pdf")
    cache = ROOT / "data" / "cfts019_text.txt"
    if not cache.exists():
        subprocess.run(["pdftotext", str(pdf), str(cache)], check=True)
    text = cache.read_text(encoding="utf-8")
    return {m.group(1): m.group(2).strip() for m in re.finditer(
        r"^(48\d{5}): (\[.*?)(?=^\d{7}: \[|\Z)", text, re.M | re.S)}


def anchor_pool(cfg: dict) -> set[str]:
    """The R-AM2 anchor pool: ObjectIDs the two Basic Reports carry."""
    pool = set()
    for key in ("sys1_export", "sys1_export_part2"):
        wb = openpyxl.load_workbook(resolve_path(cfg, key), read_only=True)
        ws = wb[wb.sheetnames[0]]
        for row in ws.iter_rows(values_only=True):
            for cell in row:
                if cell is not None and re.fullmatch(r"\s*48\d{5}\s*",
                                                     str(cell)):
                    pool.add(str(cell).strip())
    return pool


def axes_for(swe_id: str) -> list[str]:
    return [name for name, ids in SIBLING_AXES.items() if swe_id in ids]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--batch", default="B1")
    args = ap.parse_args()

    cfg = load_feature_config(ROOT)
    leaves = parse_handoff(args.batch)
    swe = swe_rows(cfg)
    blocks = spec_blocks(cfg)
    pool = anchor_pool(cfg)

    out = []
    for leaf in leaves:
        rows = swe.get(leaf["swe_id"], [])
        # Match on Source Requirement ID: it disambiguates the 076 collision.
        want = leaf.get("source_id")
        if want:
            row = next((r for r in rows if r["source_id"] == want), rows[0])
        elif len(rows) > 1:
            # SWE1_AMM_076 collides (R-AM6). Package 06 states this batch
            # carries 076b = SYS-RA-AMM-246, the Part 02 row.
            row = next((r for r in rows if r["source_id"] == "SYS-RA-AMM-246"),
                       rows[-1])
        else:
            row = rows[0] if rows else None
        if row is None:
            raise SystemExit(f"{leaf['swe_id']} not found in SWE.1")
        anchors = leaf["anchors"]
        out.append({**leaf,
                    "source_id": leaf.get("source_id") or row["source_id"],
                    "title": leaf.get("title") or row["title"],
                    "anchor": anchors[0],
                    "anchor_in_pool": all(a in pool for a in anchors),
                    "swe": row,
                    "spec_text": "\n\n".join(
                        f"[{a}] {blocks.get(a, '')}" for a in anchors),
                    "sibling_axes": axes_for(leaf["swe_id"])})

    dest = ROOT / "batches" / f"{args.batch}_context.json"
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                    encoding="utf-8")

    held = [l["swe_id"] for l in out if not l["anchor_in_pool"]]
    no_text = [l["swe_id"] for l in out if not l["spec_text"]]
    print(f"wrote {dest.relative_to(ROOT.parent.parent)}  ({len(out)} leaves)")
    print(f"  anchor in R-AM2 pool   {len(out) - len(held)}/{len(out)}")
    print(f"  out-of-pool, carried per R-AM2. {held}")
    print(f"  no spec text found     {no_text or 'none'}")
    print(f"  test sets              "
          + ", ".join(sorted({l['test_set'] for l in out})))


if __name__ == "__main__":
    main()
