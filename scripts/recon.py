#!/usr/bin/env python3
"""Phase 1 Recon — automated feature survey per FEATURE_ONBOARDING.md.

Reads feature.yaml, surveys the FW036 workbook and the 037 report, and emits:

- RECON.md      — human-readable survey (evidence for every [AUTO] value)
- DECISIONS.md  — pre-filled decision sheet ([AUTO] filled, [PROPOSED]
                  suggested from per-state strategy bindings, [PEI] left open)
- data/recon.json — machine-readable results for downstream scripts

Tier 0/1 only: this script DETECTS and PROPOSES; it never rules. Ambiguity is
surfaced with row-level evidence, not resolved.

Regression-validated against HomeHMI (2026-08-09): reproduces the manually
verified survey exactly — PARTIAL_INTERLEAVED; 140 leaves; 62 regen targets;
done segments 10-86/91-124/129-161; uncovered {055-03, 066}; parent/child
dupe {066}; orphan done req {035} (A-H06); 9 design-method strings;
27 done-region compliance notes (14 single-step procedures + 13 blank
priorities).

NOTE on the spec text-layer probe: it measures the file it is given. A PDF
copy that has been re-rendered elsewhere may probe differently from the
original — always trust the probe run against the repo inputs/ copy.

Usage:
    python scripts/recon.py --feature HomeHMI --root .
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

import openpyxl
import yaml

# ---------------------------------------------------------------- helpers

PLACEHOLDER_PROCEDURES = {"test", "tbd", "todo", "na", "n/a", "-"}


def col_letter_to_idx(letter: str) -> int:
    """Excel column letter -> 0-based index."""
    n = 0
    for ch in letter.strip().upper():
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def numbered_steps(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(r"^\s*\d+[\.\)]", str(text), flags=re.M))


# ---------------------------------------------------------------- survey

def survey_workbook(cfg: dict, wb_path: Path) -> dict:
    wbc = cfg["workbook"]
    header_row = wbc["header_row"]
    cols = {k: col_letter_to_idx(v) for k, v in wbc["columns"].items()}

    wb = openpyxl.load_workbook(wb_path, read_only=True)
    if wbc["sheet"] not in wb.sheetnames:
        sys.exit(f"sheet {wbc['sheet']!r} not found in {wb_path.name}")
    ws = wb[wbc["sheet"]]
    rows = list(ws.iter_rows(values_only=True))

    # --- column mapping verification against header text
    header = rows[header_row - 1]
    expect = {
        "req_id": "Requirement or Design ID", "test_group": "Test Group",
        "test_set": "Test Set", "test_item": "Test Item",
        "pre_conditions": "Pre-Condition", "input_test_data": "Input Test Data",
        "test_procedure": "Test procedure", "expected_result": "Expected Result",
        "spec_reference": "Specification Reference", "priority": "Priority",
        "design_method": "Design", "author": "Author",
    }
    col_check = {}
    for key, needle in expect.items():
        idx = cols.get(key)
        cell = str(header[idx] or "") if idx is not None and idx < len(header) else ""
        col_check[key] = needle.lower() in cell.lower().replace("\n", " ")
    col_ok = sum(col_check.values())

    # --- row classification
    dr = cfg["done_region"]
    author_val = dr.get("author_value")
    row_class = []  # (excel_row, cls, req) cls in {EMPTY, DONE, DRAFT}
    for i, r in enumerate(rows[header_row:], start=header_row + 1):
        def cell(key):
            idx = cols.get(key)
            return r[idx] if idx is not None and idx < len(r) else None
        filled = bool(cell("test_item")) or bool(cell("req_id"))
        if not filled:
            row_class.append((i, "EMPTY", None))
            continue
        author = str(cell("author") or "").strip()
        proc = str(cell("test_procedure") or "").strip()
        # Done-region membership is about authorship + non-placeholder
        # content, NOT current-lint compliance (done region is frozen, not
        # re-linted; single-step done rows are compliance NOTES, below).
        is_placeholder = (proc.lower() in PLACEHOLDER_PROCEDURES
                          or (numbered_steps(proc) == 0 and len(proc) < 30))
        qualifies = (
            bool(author)
            and (author == author_val if dr.get("detection") == "author" else True)
            and bool(proc) and not is_placeholder
        )
        req = str(cell("req_id") or "").strip()
        row_class.append((i, "DONE" if qualifies else "DRAFT", req))

    # ambiguity: done-author rows carrying PLACEHOLDER content — genuine
    # segmentation doubt, surfaced not ruled
    ambiguous = []
    # compliance notes: done rows deviating from current rules (recorded,
    # never fixed — the done region is frozen; A-H05 pattern)
    compliance = []
    for i, cls, _ in row_class:
        r = rows[i - 1]
        author = str(r[cols["author"]] or "").strip()
        proc = str(r[cols["test_procedure"]] or "").strip()
        prio = str(r[cols["priority"]] or "").strip() if "priority" in cols else ""
        if cls == "DRAFT" and author_val and author == author_val:
            ambiguous.append((i, "done-author row with placeholder procedure"))
        if cls == "DONE":
            if numbered_steps(proc) < 2:
                compliance.append((i, "procedure < 2 numbered steps (§10.5)"))
            if not prio:
                compliance.append((i, "blank priority"))

    # --- segmentation
    segs = []
    for i, cls, _ in row_class:
        if cls == "EMPTY":
            continue
        if segs and segs[-1]["cls"] == cls and segs[-1]["end"] == i - 1:
            segs[-1]["end"] = i
            segs[-1]["n"] += 1
        else:
            segs.append({"cls": cls, "start": i, "end": i, "n": 1})

    done_segs = [s for s in segs if s["cls"] == "DONE"]
    draft_segs = [s for s in segs if s["cls"] == "DRAFT"]
    if not done_segs and not draft_segs:
        state = "BLANK"
    elif not draft_segs:
        state = "FULL"
    elif not done_segs:
        state = "BLANK"  # drafts only: no done region; treat drafts per ruling
    else:
        interleaved = any(d["start"] < done_segs[-1]["end"] for d in draft_segs)
        state = "PARTIAL_INTERLEAVED" if interleaved else "PARTIAL_CLEAN"

    done_reqs = sorted({req for i, cls, req in row_class if cls == "DONE" and req})
    draft_reqs = sorted({req for i, cls, req in row_class if cls == "DRAFT" and req})

    # --- design method vocabulary
    vocab = []
    if "下拉選單" in wb.sheetnames:
        for r in wb["下拉選單"].iter_rows(values_only=True):
            for c in r:
                if c:
                    vocab.append(str(c).strip())
    wb.close()

    return {
        "state": state, "col_check": col_check, "col_ok": col_ok,
        "col_total": len(expect), "segments": segs, "done_segments": done_segs,
        "draft_segments": draft_segs, "done_rows": sum(s["n"] for s in done_segs),
        "draft_rows": sum(s["n"] for s in draft_segs),
        "done_reqs": done_reqs, "draft_reqs": draft_reqs,
        "ambiguous_rows": ambiguous, "compliance_notes": compliance,
        "design_method_vocab": vocab,
    }


def survey_a03(a03_path: Path) -> dict:
    wb = openpyxl.load_workbook(a03_path, read_only=True)
    ws = wb["Analysis Report"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = next(i for i, r in enumerate(rows)
               if r[0] and "SWE" in str(r[0]) and "ID" in str(r[0]))
    leaves, headings, parent_child = [], [], []
    for r in rows[hdr + 1:]:
        if not r[0]:
            continue
        rid, cat = str(r[0]).strip(), str(r[6] or "").strip()
        (leaves if cat == "Functional Requirement" else headings).append(rid)
    leafset = set(leaves)
    for rid in leaves:
        if re.search(r"-\d\d$", rid) and rid.rsplit("-", 1)[0] in leafset:
            parent_child.append(rid.rsplit("-", 1)[0])
    wb.close()
    return {"leaves": leaves, "headings": headings,
            "parent_child_dupes": sorted(set(parent_child))}


def survey_spec_text_layer(pdf_path: Path | None) -> str:
    if not pdf_path or not pdf_path.exists():
        return "no-pdf"
    try:
        import pymupdf as fitz
    except ImportError:
        return "unknown (pymupdf not installed)"
    doc = fitz.open(pdf_path)
    chars = sum(len(p.get_text()) for p in doc)
    doc.close()
    return f"text-layer: {chars} chars" if chars > 500 else "scanned (OCR path)"


# ---------------------------------------------------------------- emit

def emit(feature_dir: Path, cfg: dict, wbres: dict, a03res: dict,
         textlayer: str, hashes: dict) -> None:
    state = wbres["state"]
    leaves = a03res["leaves"]
    targets = sorted(set(leaves) - set(wbres["done_reqs"]))
    uncovered = sorted(set(leaves) - set(wbres["done_reqs"])
                       - set(wbres["draft_reqs"]))
    all_037 = set(leaves) | set(a03res["headings"])
    # req_ids written in the workbook but absent from 037 (A-H06 pattern):
    # a traceability audit sees these as pointing at nothing
    orphan_done = sorted(set(wbres["done_reqs"]) - all_037)
    orphan_draft = sorted(set(wbres["draft_reqs"]) - all_037)

    seg_lines = "\n".join(
        f"  - rows {s['start']}-{s['end']}: {s['cls']} ({s['n']} rows)"
        for s in wbres["segments"])
    amb_lines = "\n".join(f"  - row {i}: {why}"
                          for i, why in wbres["ambiguous_rows"]) or "  (none)"
    comp_lines = "\n".join(f"  - row {i}: {why}"
                           for i, why in wbres["compliance_notes"]) or "  (none)"
    pc = a03res["parent_child_dupes"]

    recon = f"""# RECON — {cfg['feature']} (generated by recon.py)

## Inputs
{chr(10).join(f"- {k}: `{v['name']}` sha256={v['sha256'][:16]}…" for k, v in hashes.items())}
- spec text layer: {textlayer}

## Workbook
- workbook_state: **{state}**
- column mapping: {wbres['col_ok']}/{wbres['col_total']} headers matched
- design-method vocabulary: {len(wbres['design_method_vocab'])} strings
- segments:
{seg_lines}
- done rows: {wbres['done_rows']} / draft rows: {wbres['draft_rows']}
- ambiguous rows (Tier 2 if any):
{amb_lines}
- done-region compliance notes (recorded, not fixed):
{comp_lines}

## Coverage (vs 037)
- 037 leaves: {len(leaves)}; headings: {len(a03res['headings'])}
- covered by done region: {len(set(leaves) & set(wbres['done_reqs']))}
- regen targets: **{len(targets)}**
- covered nowhere (done nor draft): {len(uncovered)} {uncovered if uncovered else ''}
- parent/child both-leaf duplications: {pc if pc else '(none)'}
- workbook req_ids ABSENT from 037 (traceability orphans, RD-1 candidates):
  - done region: {orphan_done if orphan_done else '(none)'}
  - draft region: {orphan_draft if orphan_draft else '(none)'}
"""
    (feature_dir / "RECON.md").write_text(recon, encoding="utf-8")

    # ---- DECISIONS prefill from per-state strategy bindings (canon §2)
    blank = state == "BLANK"
    d = []
    d.append(f"# DECISIONS — {cfg['feature']} (FW036)\n")
    d.append("Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an\n"
             "unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at\n"
             "sign-off = binding as proposed.\n")
    d.append("## 1. Intake")
    d.append(f"- spec_mode: [AUTO] {cfg.get('spec_mode')}")
    d.append(f"- spec text layer: [AUTO] {textlayer}")
    d.append(f"- source files: [AUTO] {len(hashes)} present (SHA256 in RECON.md)")
    d.append("\n## 2. Workbook survey")
    d.append(f"- workbook_state: [AUTO] {state}")
    d.append(f"- column mapping: [AUTO] {wbres['col_ok']}/{wbres['col_total']} matched")
    if wbres["done_segments"]:
        d.append("- done segments: [AUTO] " + ", ".join(
            f"{s['start']}-{s['end']}" for s in wbres["done_segments"]))
    else:
        d.append("- done segments: [AUTO] none")
    if wbres["ambiguous_rows"]:
        d.append("- ambiguous rows: [PEI] see RECON.md — per-row disposition required")
    else:
        d.append("- ambiguous rows: [AUTO] none")
    if wbres["draft_rows"]:
        d.append("- draft disposition: [PROPOSED: discard & regenerate — lint"
                 " consistency cheaper than row salvage]")
    d.append(f"- design-method vocabulary: [AUTO] {len(wbres['design_method_vocab'])}"
             " exact strings from 下拉選單")
    if wbres["compliance_notes"]:
        d.append(f"- done-region compliance notes: [AUTO] "
                 f"{len(wbres['compliance_notes'])} recorded (frozen, not fixed)"
                 " — see RECON.md; register in ANOMALIES if new")
    d.append("\n## 3. Coverage")
    d.append(f"- 037 leaves: [AUTO] {len(leaves)}")
    d.append(f"- regen targets: [AUTO] {len(targets)} (list in recon.json)")
    if uncovered:
        d.append(f"- covered nowhere: [AUTO] {uncovered} — ANOMALIES entries required")
    if pc:
        d.append(f"- parent/child dupes: [PROPOSED: proportion test per case — {pc}]")
    if orphan_done or orphan_draft:
        d.append(f"- workbook req_ids absent from 037: [AUTO] done={orphan_done}"
                 f" draft={orphan_draft} — ANOMALIES + RD-1 required; scope the"
                 " write-back traceability invariant to regen rows only")
    d.append("\n## 4. Style bindings")
    if blank:
        d.append("- style authority: [PROPOSED: fallback chain — no done region]")
        d.append("- test item shape: [PROPOSED: standard §4.3 tc_title]")
        d.append("- test group/set columns: [PROPOSED: FILL per framework Part N]")
        d.append("- exemplar source: [PROPOSED: nearest sibling feature done"
                 " region, cross-feature: style only]")
    else:
        d.append("- style authority: [AUTO] done region")
        d.append("- test item shape: [PROPOSED: follow done-region first-row shape"
                 " — verify against profile]")
        d.append("- test group/set columns: [PROPOSED: match done-region"
                 " (blank if blank)]")
        d.append("- exemplar source: [AUTO] own done region")
    d.append(f"- author on new rows: [PROPOSED: {cfg['write_back']['author_value']}]")
    d.append(f"- spec_reference: [PROPOSED: {cfg['spec_reference_template']}]")
    d.append("\n## 5. Split & scope")
    d.append("- split_mode: [PROPOSED: standard]")
    d.append("\n## 6. Framework & profile")
    d.append("- Test Set table (Part N): [PEI — draft with Claude, Tier 2]")
    d.append("- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]")
    d.append("\n## 7. Execution")
    d.append(f"- batch plan: [PROPOSED: group {len(targets)} targets by spec"
             " chapter, pilot = smallest coherent batch]")
    d.append("\n---\n\n## Sign-off\n\n- Reviewed by: ____  Date: ____\n"
             "- Overridden items: ____\n- Ruling notes:\n")
    (feature_dir / "DECISIONS.md").write_text("\n".join(d), encoding="utf-8")

    (feature_dir / "data").mkdir(exist_ok=True)
    (feature_dir / "data" / "recon.json").write_text(json.dumps({
        "workbook_state": state, "segments": wbres["segments"],
        "done_reqs": wbres["done_reqs"], "draft_reqs": wbres["draft_reqs"],
        "leaves": leaves, "regen_targets": targets, "uncovered": uncovered,
        "parent_child_dupes": pc,
        "orphan_done_reqs": orphan_done, "orphan_draft_reqs": orphan_draft,
        "design_method_vocab": wbres["design_method_vocab"],
        "ambiguous_rows": wbres["ambiguous_rows"],
        "compliance_notes": wbres["compliance_notes"],
    }, ensure_ascii=False, indent=1), encoding="utf-8")


# ---------------------------------------------------------------- main

def resolve_glob(feature_dir: Path, pattern: str) -> Path | None:
    if not pattern:
        return None
    hits = sorted(feature_dir.glob(pattern))
    if not hits:
        sys.exit(f"input not found: {pattern} under {feature_dir}")
    if len(hits) > 1:
        sys.exit(f"ambiguous input {pattern}: {[h.name for h in hits]}")
    return hits[0]


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--feature", required=True,
                    help="feature directory (contains feature.yaml)")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    feature_dir = Path(args.root).resolve() / args.feature
    cfg = yaml.safe_load((feature_dir / "feature.yaml").read_text("utf-8"))

    paths, hashes = {}, {}
    for key in ("workbook", "a03_report", "sys1_export", "spec_pdf",
                "popup_list"):
        pat = cfg["paths"].get(key)
        p = resolve_glob(feature_dir, pat) if pat else None
        paths[key] = p
        if p:
            hashes[key] = {"name": p.name, "sha256": sha256_file(p)}

    wbres = survey_workbook(cfg, paths["workbook"])
    a03res = survey_a03(paths["a03_report"])
    textlayer = survey_spec_text_layer(paths["spec_pdf"])
    emit(feature_dir, cfg, wbres, a03res, textlayer, hashes)

    print(f"recon complete: state={wbres['state']}, "
          f"leaves={len(a03res['leaves'])}, "
          f"targets={len(set(a03res['leaves']) - set(wbres['done_reqs']))}",
          file=sys.stderr)
    if wbres["ambiguous_rows"]:
        print(f"WARNING: {len(wbres['ambiguous_rows'])} ambiguous rows — "
              "Tier 2 review required (see RECON.md)", file=sys.stderr)


if __name__ == "__main__":
    main()
