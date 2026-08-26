#!/usr/bin/env python3
"""Assemble the generator's batch context for bed_lowering.

Ported from `features/amfm/scripts/make_batch_context.py` -- amfm is the
closest of the four candidates (amfm/home/media/sxm) because it is the other
`spec_mode: D` feature, so it already treats the 037 as the text authority
rather than reading an outline export.

What was DROPPED in the port, and why: amfm's context is keyed on
(doc, section) because its references are CFTS clauses, and it carries
`stla_id`, `section_title`, `spec_paragraph` and a `wording_agreement` diff
between the 037 title and the CFTS clause. bed_lowering has no CFTS family
and no section anchor at all -- R-BLM5 makes `specification_reference` a
single constant for all 176 rows -- so every one of those fields would be
either absent or a constant. Porting them would produce a context that looks
richer than the source actually is.

What was ADDED: `signal_candidates`, from the R-BLM11 databases. amfm has no
analogue because its 037 carries no CAN vocabulary.

Siblings: amfm brackets by (doc, section). Here the equivalent bracket is the
037 heading (母號) -- that IS this feature's Layer 3 unit per framework.md
Part III, and it is an upstream verbatim column rather than a derived one.
"""
import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

import yaml

FEAT = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]


def load_tsv(p: Path) -> list[dict]:
    with p.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def build(test_set: str) -> dict:
    cfg = yaml.safe_load((FEAT / "feature.yaml").read_text(encoding="utf-8"))
    inv = load_tsv(FEAT / "data" / "leaf_inventory.tsv")
    tsm = load_tsv(FEAT / "data" / "test_set_map.tsv")

    batch = [r for r in inv if r["test_set"] == test_set]
    if not batch:
        sys.exit(f"no leaves for test_set {test_set!r}")
    heads = sorted({r["heading_id"] for r in batch})
    declared = sorted(r["heading_id"] for r in tsm if r["test_set"] == test_set)
    if heads != declared:
        sys.exit(f"heading mismatch: inventory {heads} vs test_set_map {declared}")

    # R-BLM5: one constant for every row. Read it from the recon assertion so
    # the context cannot drift from what the ruling pinned.
    spec_ref = cfg["recon_assertions"]["spec_reference_stem"]

    pre = FEAT / "batches" / "pilot" / "signal_prelookup.json"
    signals = json.loads(pre.read_text(encoding="utf-8")) if pre.exists() else {}

    leaves = []
    for r in batch:
        leaves.append({
            "req_id": r["req_id"],
            "heading_id": r["heading_id"],
            "test_set": r["test_set"],
            "requirement_title": r["title"],
            "requirement_text": r["description"],
            "verification_criteria": r["verification_criteria"],
            "verification_method": r["verification_method"],
            "sub_categorization": r["sub_categorization"],
            "priority_037": r["priority_037"],
            "spec_reference": spec_ref,
        })

    in_batch = {r["req_id"] for r in batch}
    siblings = [{"req_id": r["req_id"], "heading_id": r["heading_id"],
                 "test_set": r["test_set"],
                 "requirement_title": r["title"]}
                for r in inv
                if r["heading_id"] in set(heads) and r["req_id"] not in in_batch]

    ctx = {
        "feature": cfg["feature"],
        "test_group": cfg["test_group"],
        "test_set": test_set,
        "spec_mode": cfg["spec_mode"],
        "spec_reference_constant": spec_ref,
        "spec_reference_note": (
            "R-BLM5 [OVERRIDE IN §10.7(b)]: every row carries this one value. "
            "The 037's HMI Source ID column has exactly 1 distinct value and "
            "no section suffix, so there is no section anchor to cite. "
            "Traceability is document-level by ruling, not by omission."
        ),
        "pdf_excluded": ("R-BLM7 spec_mode=D: the specification PDF is a "
                         "human reference and is NOT part of this context"),
        "heading_ids": heads,
        "leaf_count": len(leaves),
        "leaves": leaves,
        "siblings": siblings,
        "signal_candidates": signals,
        "sources": {
            "leaf_inventory.tsv": sha256(FEAT / "data" / "leaf_inventory.tsv"),
            "test_set_map.tsv": sha256(FEAT / "data" / "test_set_map.tsv"),
            "feature.yaml": sha256(FEAT / "feature.yaml"),
        },
    }
    return ctx


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--test-set", default="Fault Handling")
    ap.add_argument("--out", default=str(FEAT / "batches" / "pilot" / "context.json"))
    a = ap.parse_args()
    ctx = build(a.test_set)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(ctx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"test_set   {ctx['test_set']}")
    print(f"headings   {ctx['heading_ids']}")
    print(f"leaves     {ctx['leaf_count']}")
    print(f"siblings   {len(ctx['siblings'])}")
    print(f"spec_ref   {ctx['spec_reference_constant']}")
    print(f"out        {out.relative_to(ROOT)}  sha256 {sha256(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
