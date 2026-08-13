"""R20-2 — ratchet guarding R18-3 rule 1 ("the only write path").

R18-3 rule 1 makes `backend/xlsx_surgical.py` the only sanctioned write path
and bars openpyxl's save path from producing any deliverable. Until this test
existed that was discipline, not mechanism: nothing stopped the next script
from calling `wb.save()`.

**Why a ratchet and not a clean bill.** The repo does not comply today — 11
call sites remain. R20-2: a mechanism must not wait for the ground to be
clean, because "clean first, then guard" leaves the period that most needs
guarding completely unguarded. So the current 11 are grandfathered by name
and count, and the test's job is to stop the 12th.

`KNOWN_VIOLATIONS` is **only ever allowed to shrink**. Remove a call site,
remove its entry — the list is itself the progress metric. A stale entry
(listed but no longer present) fails just as loudly as a new call site,
because a baseline nobody prunes stops meaning anything.

The scan is AST-based, not textual: only a name bound from
`openpyxl.load_workbook()` / `Workbook()` counts. `pixmap.save()` (PNG
render) and python-docx's `document.save()` therefore cannot masquerade as
violations — verified against `features/*/scripts/split_spec.py` and
`tests/test_amfm_cross_refs.py`, neither of which is flagged. This follows
R17-2's word-boundary discipline: a substring count would have been wrong
here in both directions.
"""
from __future__ import annotations

import ast
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------- whitelist
# Permanent exemptions. Each entry states WHY; "not a deliverable" is the
# only admissible reason.
WHITELIST = {
    "backend/xlsx_surgical.py":
        "the sanctioned path itself",
    "features/privacy/scripts/xlsx_roundtrip_probe.py":
        "not a deliverable — deliberately produces the LOSSY comparison arm",
}
WHITELIST_PREFIXES = {
    "tests/":
        "not a deliverable — fixtures and damage cases built in tmp_path",
}

# ------------------------------------------------------- grandfathered list
# ONLY EVER SHRINKS (R20-2 clause 4). Line numbers are documentation; the
# test compares counts, so ordinary edits above a call site do not produce
# spurious failures while a NEW call site still does.
#
# status:
#   QUARANTINED — script carries the R20-3 header and must not be executed
#   HAZARD      — R21-2: overwrites the SOURCE file, not just the output.
#                 A damaged output can be thrown away; a damaged source
#                 takes every comparison that ever used it down with it.
#   ACTIVE      — reachable in normal operation; the real remaining exposure
KNOWN_VIOLATIONS = {
    "features/home/scripts/write_back.py": {
        "calls": 1, "lines": [475], "status": "QUARANTINED",
        "nature": "deliverable producer (Home); frozen per R18-1",
    },
    "features/sxm/scripts/write_back.py": {
        "calls": 1, "lines": [478], "status": "QUARANTINED",
        "nature": "deliverable producer (SXM); frozen per R18-1",
    },
    "features/media/scripts/write_back.py": {
        "calls": 1, "lines": [349], "status": "QUARANTINED",
        "nature": "deliverable producer (Media); artefact state UNMEASURED",
    },
    "features/projection/scripts/writeback.py": {
        "calls": 1, "lines": [290], "status": "QUARANTINED",
        "nature": "deliverable producer (Projection); frozen per R18-1",
    },
    "backend/writer.py": {
        "calls": 4, "lines": [363, 404, 468, 487], "status": "ACTIVE",
        "nature": "app write path — write_generated_results / "
                  "write_framework_sheet / write_generated_tc_workbook x2",
    },
    "backend/api_server.py": {
        "calls": 2, "lines": [2370, 2410], "status": "HAZARD",
        "nature": "2370 export-for-download (ACTIVE). "
                  "2410 HAZARD (R21-2): overwrites the source file in place; "
                  "destroys the baseline that all structural comparisons "
                  "depend on, not merely the output. Every structural finding "
                  "in this repo — AMFM 21/10, Home 14/10, SXM 11/10 — is "
                  "measured against a file this path can silently rewrite.",
    },
    "scripts/translate_xlsx.py": {
        "calls": 1, "lines": [303], "status": "ACTIVE",
        "nature": "translated workbook output",
    },
}

SKIP_DIRS = {".venv", "archive", "__pycache__", ".git", "node_modules",
             "frontend", "frontend-modern", "spec-index"}
WB_FACTORIES = {"load_workbook", "Workbook"}


def _workbook_names(tree: ast.AST) -> set[str]:
    """Names bound from an openpyxl workbook factory."""
    names: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call):
            continue
        fn = node.value.func
        label = fn.attr if isinstance(fn, ast.Attribute) else getattr(fn, "id", "")
        if label in WB_FACTORIES:
            names.update(t.id for t in node.targets if isinstance(t, ast.Name))
    return names


def scan() -> dict[str, list[int]]:
    """Repo-relative path -> line numbers of openpyxl save calls."""
    found: dict[str, list[int]] = {}
    for path in sorted(REPO_ROOT.rglob("*.py")):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        rel = path.relative_to(REPO_ROOT).as_posix()
        if rel in WHITELIST or any(rel.startswith(p) for p in WHITELIST_PREFIXES):
            continue
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        names = _workbook_names(tree)
        if not names:
            continue
        lines = sorted(
            node.lineno for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "save"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id in names)
        if lines:
            found[rel] = lines
    return found


def test_no_new_openpyxl_save_call_sites():
    """The 12th call site fails the build. The 11th is grandfathered."""
    found = scan()
    new_files = sorted(set(found) - set(KNOWN_VIOLATIONS))
    assert not new_files, (
        "R18-3 rule 1 — openpyxl save in a file with no grandfathered "
        "allowance:\n" + "\n".join(f"  {f}:{found[f]}" for f in new_files)
        + "\nUse backend/xlsx_surgical.surgical_save instead.")

    grew = {f: (KNOWN_VIOLATIONS[f]["calls"], len(found[f]))
            for f in found if len(found[f]) > KNOWN_VIOLATIONS[f]["calls"]}
    assert not grew, (
        "R18-3 rule 1 — new openpyxl save call added to an already-known "
        "file (the baseline only shrinks):\n"
        + "\n".join(f"  {f}: allowed {a}, found {b} at {found[f]}"
                    for f, (a, b) in grew.items()))


def test_baseline_has_no_stale_entries():
    """R20-2 clause 4 — removing a call site means removing its entry.

    An unpruned baseline stops being a measure of anything, so drift in the
    forgiving direction fails too.
    """
    found = scan()
    gone = sorted(set(KNOWN_VIOLATIONS) - set(found))
    assert not gone, (
        "these files no longer call openpyxl save — delete their entries "
        "from KNOWN_VIOLATIONS (the list is the progress metric):\n"
        + "\n".join(f"  {f}" for f in gone))

    shrunk = {f: (KNOWN_VIOLATIONS[f]["calls"], len(found[f]))
              for f in found if len(found[f]) < KNOWN_VIOLATIONS[f]["calls"]}
    assert not shrunk, (
        "call sites were removed — lower the counts in KNOWN_VIOLATIONS:\n"
        + "\n".join(f"  {f}: listed {a}, found {b}"
                    for f, (a, b) in shrunk.items()))


def test_whitelisted_and_test_files_do_not_trip_the_scan():
    """Positive control — an always-failing scan would flunk here.

    Also pins the AST discrimination: `split_spec.py` calls `pixmap.save()`
    and is not flagged, so the scan is not matching on the method name alone.
    """
    found = scan()
    assert "features/privacy/scripts/xlsx_roundtrip_probe.py" not in found
    assert not any(f.startswith("tests/") for f in found)
    assert "features/home/scripts/split_spec.py" not in found
    assert "features/media/scripts/split_spec.py" not in found


def test_every_known_violation_states_its_nature_and_status():
    """A baseline entry without a reason is an unexplained exemption."""
    for path, entry in KNOWN_VIOLATIONS.items():
        assert entry["nature"].strip(), f"{path}: no nature recorded"
        assert entry["status"] in {"QUARANTINED", "HAZARD", "ACTIVE"}, (
            f"{path}: unknown status {entry['status']!r}")
