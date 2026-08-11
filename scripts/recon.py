#!/usr/bin/env python3
"""Phase 1 Recon — automated feature survey per FEATURE_ONBOARDING.md.

Reads feature.yaml, surveys the FW036 workbook and the 037 report, and emits:

- RECON.md      — human-readable survey (evidence for every [AUTO] value)
- DECISIONS.md  — pre-filled decision sheet ([AUTO] filled, [PROPOSED]
                  suggested from per-state strategy bindings, [PEI] left open)
- data/recon.json — machine-readable results for downstream scripts

Tier 0/1 only: this script DETECTS and PROPOSES; it never rules. Ambiguity is
surfaced with row-level evidence, not resolved.

Regression-validated against features/home (2026-08-09): reproduces the manually
verified survey exactly — PARTIAL_INTERLEAVED; 140 leaves; 62 regen targets;
done segments 10-86/91-124/129-161; uncovered {055-03, 066}; parent/child
dupe {066}; orphan done req {035} (A-H06); 9 design-method strings;
27 done-region compliance notes (14 single-step procedures + 13 blank
priorities).

NOTE on the spec text-layer probe: it measures the file it is given. A PDF
copy that has been re-rendered elsewhere may probe differently from the
original — always trust the probe run against the repo inputs/ copy.

Usage:
    python scripts/recon.py --feature features/home --root .
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


def norm(v) -> str:
    """Header text, comparable: lowered, newlines and runs of space collapsed."""
    return re.sub(r"\s+", " ", str(v or "")).strip().lower()


# --- workbook column resolution by header TEXT, not by letter ------------
#
# feature.yaml letters are a prior, not the authority. The FM-WI-FSM-036 form
# has at least two revisions in circulation: revision C (2026-01-21) inserted
# "Estimated Test Time (mins)" at Q, shifting design_method, functional_safety,
# the vehicle block, author and remarks one column right. An instance created
# after that date may still be built on the older layout — the AM/FM
# CFTS024_Radio workbook (2026-01-29) is, and its ChangeHistory stops at B. So
# the layout has to be read off the instance in front of us.
#
# Each entry is (required tokens, forbidden tokens); a field resolves only on
# exactly one matching column, because near-duplicate headers are the trap:
# "Requirement or Design ID" (D) vs "...ID (Polarion)" (C), "Test Case ID" (F)
# vs "Test Case ID (TestRail)" (E) vs "Test Case Reference ID" (O).
HEADER_SPEC = {
    "req_id": (("requirement or design id",), ("polarion",)),
    "test_group": (("test group",), ()),
    "test_set": (("test set",), ()),
    "test_item": (("test item",), ()),
    "pre_conditions": (("pre-condition",), ()),
    "input_test_data": (("input test data",), ()),
    "test_procedure": (("test procedure",), ()),
    "expected_result": (("expected result",), ()),
    "spec_reference": (("specification reference",), ()),
    "tc_ref_id": (("test case reference id",), ()),
    "priority": (("test case priority",), ()),
    "design_method": (("test case design", "methods"), ()),
    "functional_safety": (("functional safety",), ()),
    "author": (("test case author",), ()),
    "remarks": (("remarks",), ()),
    # Revision marker, not a pipeline field: present => rev C layout.
    "estimated_test_time": (("estimated test time",), ()),
}
OPTIONAL_COLUMNS = {"estimated_test_time"}


def resolve_columns(header: tuple) -> tuple[dict, list[str]]:
    """header row values -> {field: 0-based index}, plus unresolved notes."""
    resolved, notes = {}, []
    for key, (need, forbid) in HEADER_SPEC.items():
        hits = [j for j, v in enumerate(header)
                if all(t in norm(v) for t in need)
                and not any(t in norm(v) for t in forbid)]
        if len(hits) == 1:
            resolved[key] = hits[0]
        elif not hits and key in OPTIONAL_COLUMNS:
            continue
        else:
            notes.append(f"{key}: {len(hits)} header matches"
                         + (f" at {[idx_to_letter(h) for h in hits]}" if hits else ""))
    return resolved, notes


def idx_to_letter(idx: int) -> str:
    """0-based index -> Excel column letter."""
    s, n = "", idx + 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


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

    # --- columns resolved FROM the header text; feature.yaml is only a prior
    header = rows[header_row - 1]
    resolved, unresolved = resolve_columns(header)
    if unresolved:
        sys.exit("cannot resolve workbook columns from the header row "
                 f"{header_row}: {unresolved}")
    layout_rev = "C (has Estimated Test Time)" if "estimated_test_time" in \
        resolved else "A/B (no Estimated Test Time)"
    # Disagreements are reported, never silently honoured: a stale letter in
    # feature.yaml is exactly the defect this resolution exists to catch.
    col_conflicts = []
    for key, idx in resolved.items():
        want = cols.get(key)
        if want is not None and want != idx:
            col_conflicts.append(
                f"{key}: feature.yaml says {idx_to_letter(want)}, "
                f"header says {idx_to_letter(idx)}")
    cols = {k: v for k, v in resolved.items() if k != "estimated_test_time"}
    col_check = {k: True for k in cols}
    col_ok = len(cols)

    # --- who authored the existing rows? The configured value is a prior too;
    # a fresh feature.yaml carries the previous feature's name.
    dr = cfg["done_region"]
    author_val = dr.get("author_value")
    seen_authors = {}
    for r in rows[header_row:]:
        a = str(r[cols["author"]] or "").strip() if cols["author"] < len(r) else ""
        if a:
            seen_authors[a] = seen_authors.get(a, 0) + 1
    author_note = ""
    if seen_authors and author_val not in seen_authors:
        detected = max(seen_authors, key=seen_authors.get)
        author_note = (f"feature.yaml done_region.author_value={author_val!r} "
                       f"matches 0 rows; surveying with the dominant author "
                       f"{detected!r} ({seen_authors[detected]} rows) — "
                       "Tier 2 must confirm before Phase 4")
        author_val = detected
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
        "col_total": len(cols), "segments": segs, "done_segments": done_segs,
        "draft_segments": draft_segs, "done_rows": sum(s["n"] for s in done_segs),
        "draft_rows": sum(s["n"] for s in draft_segs),
        "done_reqs": done_reqs, "draft_reqs": draft_reqs,
        "ambiguous_rows": ambiguous, "compliance_notes": compliance,
        "design_method_vocab": vocab,
        "columns": {k: idx_to_letter(v) for k, v in resolved.items()},
        "col_conflicts": col_conflicts, "layout_rev": layout_rev,
        "authors": seen_authors, "author_used": author_val,
        "author_note": author_note,
    }


def survey_a03(a03_path: Path) -> dict:
    """Survey the requirement report — columns located by header text.

    The Analysis Report template is not stable across features: Home's
    Categorization sits at column 7 and its values read "Functional
    Requirement"/"Heading"; AM/FM's sits at column 31 (behind 24 review-
    criteria columns) and reads "Functional" with no Heading rows at all. The
    old positional read (`row[6] == "Functional Requirement"`) classifies every
    AM/FM row as a heading and reports zero leaves — silently, since an empty
    leaf list is a legal state for a workbook that is already complete.

    Safety attributes (ASIL / FTTI) are reported when the template carries
    them: whether the safety-analysis layer belongs in the trace chain is a
    property of the ruled requirement source, not of what files are present.
    """
    wb = openpyxl.load_workbook(a03_path, read_only=True)
    ws = wb["Analysis Report"]
    rows = list(ws.iter_rows(values_only=True))
    hdr = next((i for i, r in enumerate(rows)
                if any("requirement description" in norm(v) for v in r)), None)
    if hdr is None:
        sys.exit(f"{a03_path.name}: no header row (no 'Requirement Description'"
                 " cell) in the Analysis Report sheet")
    header = rows[hdr]

    def find(*need, forbid=()):
        hits = [j for j, v in enumerate(header)
                if all(t in norm(v) for t in need)
                and not any(t in norm(v) for t in forbid)]
        return hits[0] if len(hits) == 1 else None

    cat_i = find("categorization", forbid=("sub",))
    asil_i, ftti_i = find("asil"), find("ftti")

    leaves, headings, parent_child = [], [], []
    safety = {}
    for r in rows[hdr + 1:]:
        if not r[0]:
            continue
        rid = str(r[0]).strip()
        cat = str(r[cat_i] or "").strip() if cat_i is not None else ""
        # "Functional" (AM/FM) and "Functional Requirement" (Home) are the same
        # classification written two ways; anything else is a heading/other.
        (leaves if cat.lower().startswith("functional")
         else headings).append(rid)
        if asil_i is not None:
            val = str(r[asil_i] or "").strip()
            if val and len(val) < 12:      # skip the template's help text row
                safety[val] = safety.get(val, 0) + 1
    leafset = set(leaves)
    for rid in leaves:
        if re.search(r"-\d\d$", rid) and rid.rsplit("-", 1)[0] in leafset:
            parent_child.append(rid.rsplit("-", 1)[0])
    wb.close()
    return {"leaves": leaves, "headings": headings,
            "parent_child_dupes": sorted(set(parent_child)),
            "categorization_col": idx_to_letter(cat_i) if cat_i is not None else None,
            "has_safety_columns": asil_i is not None or ftti_i is not None,
            "asil_distribution": safety}


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

    def cap(items, n=8):
        """RECON.md is read by a human; recon.json carries the full list."""
        items = list(items)
        if len(items) <= n:
            return str(items) if items else "(none)"
        return (f"{items[:n]} … +{len(items) - n} more "
                "(full list in data/recon.json)")

    # A workbook can be FULL and still cover none of the ruled requirement
    # source — AM/FM 2026-08: 158 authored rows, all tracing a requirement
    # family that a ruling superseded. The state machine keys on draft rows, so
    # it cannot see this; naming it here keeps "FULL" from reading as "done".
    covered_n = len(set(leaves) & set(wbres["done_reqs"]))
    foreign = (wbres["done_rows"] > 0 and covered_n == 0 and bool(leaves))

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
- form layout revision: {wbres['layout_rev']}
- column mapping: {wbres['col_ok']} fields resolved from header text
  (authority; feature.yaml letters are only a prior)
{chr(10).join(f"  - {k} = {v}" for k, v in wbres['columns'].items())}
- feature.yaml column conflicts:
{chr(10).join(f"  - {c}" for c in wbres['col_conflicts']) or "  (none)"}
- authors present: {wbres['authors'] or '(none)'}
{("- **author detection**: " + wbres['author_note']) if wbres['author_note'] else ""}
- design-method vocabulary: {len(wbres['design_method_vocab'])} strings
- segments:
{seg_lines}
- done rows: {wbres['done_rows']} / draft rows: {wbres['draft_rows']}
- ambiguous rows (Tier 2 if any):
{amb_lines}
- done-region compliance notes (recorded, not fixed):
{comp_lines}

## Requirement report
- Categorization column: {a03res['categorization_col'] or 'NOT FOUND'}
- safety attributes (ASIL/FTTI) in the ruled source: {
    'PRESENT — ' + str(a03res['asil_distribution'])
    if a03res['has_safety_columns'] else '**ABSENT**'}
  - absent means the safety-analysis layer (SYS2/SYSRA) has no attachment
    point on these leaves and does NOT enter the trace chain. It says nothing
    about whether the requirements are safety-relevant — only that the ruled
    source does not claim they are.

## Coverage (vs 037)
- 037 leaves: {len(leaves)}; headings: {len(a03res['headings'])}
- covered by done region: {covered_n}
- regen targets: **{len(targets)}**
- covered nowhere (done nor draft): {len(uncovered)} {cap(uncovered)}
- parent/child both-leaf duplications: {cap(pc)}
- workbook req_ids ABSENT from 037 (traceability orphans, RD-1 candidates):
  - done region: {len(orphan_done)} {cap(orphan_done)}
  - draft region: {len(orphan_draft)} {cap(orphan_draft)}
{f'''
## Requirement-family mismatch — Tier 2

The workbook is **{state}** ({wbres['done_rows']} authored rows, no drafts) yet
covers **0 of {len(leaves)}** leaves in the ruled requirement source. Every
authored row traces a req_id the ruled source does not contain
({len(orphan_done)} distinct). Against the ruled source this workbook is
effectively BLANK, and "{state}" must not be read as "done".

This is not a state the canon's state machine can express — it keys on draft
rows, and there are none. Disposition of the existing rows (freeze as a legacy
region / replace / re-map) is a ruling, not a detection.
''' if foreign else ''}"""
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
    d.append(f"- form layout revision: [AUTO] {wbres['layout_rev']}")
    d.append(f"- column mapping: [AUTO] {wbres['col_ok']} fields resolved from"
             " header text")
    if wbres["col_conflicts"]:
        d.append("- feature.yaml column letters: [PEI] "
                 f"{len(wbres['col_conflicts'])} disagree with the header —"
                 " update feature.yaml before Phase 4 (see RECON.md)")
    if wbres["author_note"]:
        d.append(f"- done_region.author_value: [PROPOSED: {wbres['author_used']}"
                 f" — feature.yaml value matches 0 rows]")
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
    if foreign:
        d.append(f"- requirement-family mismatch: [PEI] the {wbres['done_rows']}"
                 f" authored rows cover 0 of {len(leaves)} ruled leaves and"
                 f" trace {len(orphan_done)} req_ids absent from the ruled"
                 " source. Rule their disposition (freeze as legacy /"
                 " replace / re-map) BEFORE the write-back strategy — it"
                 " defines what 'done region' and 'completeness' mean here")
    if a03res["has_safety_columns"]:
        d.append(f"- safety attributes: [AUTO] present — "
                 f"{a03res['asil_distribution']}; safety layer joins the chain")
    else:
        d.append("- safety attributes: [PROPOSED: ruled source carries no"
                 " ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT"
                 " enter the trace chain]")
    d.append(f"- regen targets: [AUTO] {len(targets)} (list in recon.json)")
    if uncovered:
        d.append(f"- covered nowhere: [AUTO] {len(uncovered)} {cap(uncovered)}"
                 " — ANOMALIES entries required")
    if pc:
        d.append(f"- parent/child dupes: [PROPOSED: proportion test per case — {pc}]")
    if orphan_done or orphan_draft:
        d.append(f"- workbook req_ids absent from 037: [AUTO] done="
                 f"{len(orphan_done)} {cap(orphan_done, 4)} draft="
                 f"{len(orphan_draft)} {cap(orphan_draft, 4)} — ANOMALIES +"
                 " RD-1 required; scope the write-back traceability invariant"
                 " to regen rows only")
    d.append("\n## 4. Style bindings")
    if blank:
        d.append("- style authority: [PROPOSED: fallback chain — no done region]")
        d.append("- test item shape: [PROPOSED: standard §4.3 tc_title]")
        d.append("- test group/set columns: [PROPOSED: FILL per framework Part N]")
        d.append("- exemplar source: [PROPOSED: nearest sibling feature done"
                 " region, cross-feature: style only]")
    else:
        if foreign:
            d.append("- style authority: [PROPOSED: the existing rows — they"
                     " are the workbook's only precedent — but they are NOT"
                     " the traceability authority; style may be borrowed from"
                     " rows whose req_ids the ruled source does not contain]")
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
        "columns": wbres["columns"], "layout_rev": wbres["layout_rev"],
        "col_conflicts": wbres["col_conflicts"],
        "authors": wbres["authors"], "author_used": wbres["author_used"],
        "has_safety_columns": a03res["has_safety_columns"],
        "asil_distribution": a03res["asil_distribution"],
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

    # Every declared input is hashed, not just the five the pipeline consumes:
    # a feature may declare its own (AM/FM's cfts_doc, sysra_export) and an
    # un-hashed input is one nobody can prove they surveyed.
    paths, hashes = {}, {}
    for key in dict.fromkeys(list(cfg["paths"]) + ["workbook", "a03_report",
                                                   "sys1_export", "spec_pdf",
                                                   "popup_list"]):
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
