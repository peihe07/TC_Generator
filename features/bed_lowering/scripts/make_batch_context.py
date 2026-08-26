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






def _spec_reference_constant() -> str:
    """The 037's `HMI Source ID`, asserted to be a single distinct value."""
    import openpyxl
    a03 = FEAT / "inputs" / ("FM-WI-FSM-037-A03-N1L-SWE1-BedLoweringMode-HMI-V0.1"
                             " STLA 報告.xlsx")
    wb = openpyxl.load_workbook(a03, read_only=True, data_only=True)
    rows = list(wb["Analysis Report"].iter_rows(values_only=True))
    wb.close()
    header = [str(c).replace("\xa0", " ").strip() if c else "" for c in rows[6]]
    hmi = header.index("HMI Source ID")
    rid = header.index("SWE-Requirement ID")
    vals = {str(r[hmi]).strip() for r in rows[7:]
            if r[rid] not in (None, "") and r[hmi] not in (None, "")}
    if len(vals) != 1:
        sys.exit(f"R-BLM5 premise broken: HMI Source ID has {len(vals)} "
                 f"distinct values, expected 1: {sorted(vals)[:4]}")
    return vals.pop()


def _spec_context_for(spec_ref: str, signals: dict) -> str:
    """Per-row spec context: the ruled reference constant + verified signals.

    Kept identical for every row of the batch on purpose -- R-BLM5 makes the
    reference a single constant, and the signal set was looked up for the
    Test Set as a whole, not per leaf. Emitting it per row is what the
    prompt_builder contract requires, not a claim that it differs per row.
    """
    lines = [f"specification_reference (verbatim, R-BLM5): {spec_ref}"]
    if signals:
        lines.append("")
        lines.append("Verified CAN signals available for this Test Set "
                     "(R-BLM11 bound databases; use $MESSAGE.Signal$ = raw "
                     "(label) per IN 8.7.5(a), never invent a name):")
        for label, e in signals.items():
            cands = e.get("dbc") or []
            if cands:
                lines.append(f"- {label}: {', '.join(cands[:8])}")
    return "\n".join(lines)


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

    # R-BLM5: one constant for every row, taken VERBATIM from the 037's
    # `HMI Source ID` column.
    #
    # This used to read `cfg["recon_assertions"]["spec_reference_stem"]`.
    # R-BLM15(1) retired that key -- it declared a value recon measured
    # differently (parsed stem vs raw column value), which is why it could
    # never go green. Re-pointing at another declaration would repeat the
    # mistake in a new place, so this reads the SOURCE COLUMN itself and
    # asserts the ruling's premise (exactly one distinct value) while it is
    # at it. A declaration can drift from the file; the file cannot drift
    # from itself.
    spec_ref = _spec_reference_constant()

    pre = FEAT / "batches" / "pilot" / "signal_prelookup.json"
    signals = json.loads(pre.read_text(encoding="utf-8")) if pre.exists() else {}

    leaves = []
    for r in batch:
        leaves.append({
            "req_id": r["req_id"],
            # `test_item` 為 `backend.prompt_builder.build_batch_prompt` 之
            # **必要鍵**（`row['test_item']`，非 .get，缺鍵即 KeyError）。
            # 上繳 07 §三-1 之實跑才發現此契約 —— 在此之前 adapter 只餵
            # `requirement_text`，組 prompt 會當場炸掉。生成輸入取 037 之
            # Requirement Description（即 R-S4 上半之來源），不取已成品之
            # tc_title —— 那是輸出不是輸入。
            "test_item": r["description"],
            "heading_id": r["heading_id"],
            "test_set": r["test_set"],
            "requirement_title": r["title"],
            "requirement_text": r["description"],
            "verification_criteria": r["verification_criteria"],
            "verification_method": r["verification_method"],
            "sub_categorization": r["sub_categorization"],
            "priority_037": r["priority_037"],
            "spec_reference": spec_ref,
            # `build_batch_prompt` 只把 `_get_spec_context(row, spec_index)`
            # 之輸出放進 prompt，而該函式讀的是 `row["matched_spec_context"]`。
            # 不填此鍵，prompt 之每條 Spec 欄皆為 "N/A" —— 上繳 07 §三-1 實測。
            # 後果不是報錯而是**訊號資訊整段不進 prompt**：生成端看不到
            # $ASCM_FD_2.*$ 之候選與 VAL_ 列舉，只能省略訊號或造名（IN §8.4）。
            # 故本鍵承載本 feature 之兩項語料：R-BLM5 之 N 欄常數，
            # 與 R-BLM11 四庫預查所得之訊號候選。
            "matched_spec_context": _spec_context_for(spec_ref, signals),
        })

    in_batch = {r["req_id"] for r in batch}
    siblings = [{"req_id": r["req_id"], "heading_id": r["heading_id"],
                 "test_set": r["test_set"],
                 "requirement_title": r["title"]}
                for r in inv
                if r["heading_id"] in set(heads) and r["req_id"] not in in_batch]

    # `project` 為 build_batch_prompt 之必要鍵（`context['project']`）。
    # 取 `tc_id_format` 之前綴為單一真相源，不另立 `project:` 裸鍵 ——
    # 兩處各寫一次即可能不一致。
    project = cfg["tc_id_format"].split("-")[0]

    ctx = {
        "feature": cfg["feature"],
        "project": project,
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
    print(f"out        {out}  sha256 {sha256(out)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
