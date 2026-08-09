"""Tests for Step 4 write-back (mediaHMI/scripts/write_back.py).

The invariants under test are the ones row-level linting cannot see: a row with
an invented req_id is well-formed, a missing leaf leaves no trace in the file,
and a corrupted done region looks like a normal edit.
"""
import hashlib
import json
import shutil
import sys
import warnings
from pathlib import Path

import pytest

warnings.filterwarnings("ignore")
openpyxl = pytest.importorskip("openpyxl")

REPO = Path(__file__).resolve().parent.parent
SCRIPTS = REPO / "mediaHMI" / "scripts"
PKG = REPO / "mediaHMI"
sys.path.insert(0, str(SCRIPTS))

import write_back  # noqa: E402

SRC = next(iter((PKG / "inputs").glob("*036-A01*.xlsx")), None) if (PKG / "inputs").exists() else None
DATA = PKG / "data"
GENERATED = PKG / "generated"

needs_workbook = pytest.mark.skipif(
    SRC is None or not (DATA / "remaining_leaves.json").exists() or not GENERATED.exists(),
    reason="source workbook / derived data not present (they are gitignored; run RUNBOOK Step 1)",
)

FUNC = "功能測試 (Functional based ; no specific technique)"


def _leaf(req_id, parent, desc="The system shall do a thing."):
    return {"req_id": req_id, "parent": parent, "description": desc,
            "hmi_source_id": "Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_(July_25th,_2023)_1.1",
            "section": "1.1"}


def _tc(req_id, **over):
    tc = {"req_id": req_id, "test_group": "MediaHMI", "test_set": "Browse Tab",
          "test_item": "The system shall do a thing.\n\n(tag)",
          "pre_conditions": "1. The HU is on", "input_test_data": "NA",
          "test_procedure": '1. Press "Media"\n2. Read the screen',
          "expected_result": "1. The Media screen is displayed\n2. Content is shown",
          "specification_reference": "ref", "priority": "P1", "design_method": FUNC}
    tc.update(over)
    return tc


def _write_parent(tmp: Path, parent, tcs=None, **extra):
    body = {"parent": parent, "tcs": tcs or []}
    body.update(extra)
    (tmp / f"{parent}.json").write_text(json.dumps(body, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# invariant 1 — traceability
# ---------------------------------------------------------------------------

def test_invented_sub_id_aborts_the_write(tmp_path):
    """§8.2.2: several TCs share one sub-id. A new sub-id invents a requirement.

    This is the defect class the row-level linter structurally cannot catch —
    every such row is otherwise perfectly well-formed.
    """
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-074", [_tc("P-074-01"), _tc("P-074-02")])
    leaves = [_leaf("P-074-01", "P-074")]
    rows = write_back.collect_rows(gen, leaves)
    with pytest.raises(write_back.WriteBackError, match="invents a requirement"):
        write_back.assert_traceable_and_complete(rows, leaves)


def test_leaf_with_no_row_aborts_the_write(tmp_path):
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-001", [_tc("P-001-01")])
    leaves = [_leaf("P-001-01", "P-001"), _leaf("P-001-02", "P-001")]
    rows = write_back.collect_rows(gen, leaves)
    with pytest.raises(write_back.WriteBackError, match="no row"):
        write_back.assert_traceable_and_complete(rows, leaves)


def test_matching_sets_pass(tmp_path):
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-001", [_tc("P-001-01"), _tc("P-001-01")])
    leaves = [_leaf("P-001-01", "P-001")]
    rows = write_back.collect_rows(gen, leaves)
    write_back.assert_traceable_and_complete(rows, leaves)  # must not raise


def test_blocked_parent_without_emit_row_aborts(tmp_path):
    """A blocked leaf that emits nothing would silently vanish from the deliverable."""
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-051", [], blocked={
        "reason": "r", "anomaly": "A-009", "req_ids": ["P-051-01"],
        "write_back": {"emit_row": False}})
    with pytest.raises(write_back.WriteBackError, match="traceability"):
        write_back.collect_rows(gen, [_leaf("P-051-01", "P-051")])


def test_blocked_req_id_must_be_a_real_leaf(tmp_path):
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-051", [], blocked={
        "reason": "r", "anomaly": "A-009", "req_ids": ["P-051-99"],
        "write_back": {"emit_row": True, "test_set": "Browse Tab", "remarks": "x"}})
    with pytest.raises(write_back.WriteBackError, match="not a leaf"):
        write_back.collect_rows(gen, [_leaf("P-051-01", "P-051")])


# ---------------------------------------------------------------------------
# row shape
# ---------------------------------------------------------------------------

def test_illegal_dropdown_value_aborts(tmp_path):
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-001", [_tc("P-001-01", priority="High")])
    rows = write_back.collect_rows(gen, [_leaf("P-001-01", "P-001")])
    with pytest.raises(write_back.WriteBackError, match="illegal dropdown"):
        write_back.assert_row_shape(rows)


def test_blocked_row_must_leave_priority_blank(tmp_path):
    gen = tmp_path / "gen"; gen.mkdir()
    _write_parent(gen, "P-051", [], blocked={
        "reason": "r", "anomaly": "A-009", "req_ids": ["P-051-01"],
        "write_back": {"emit_row": True, "test_set": "Browse Tab",
                       "priority": "P1", "remarks": "x"}})
    rows = write_back.collect_rows(gen, [_leaf("P-051-01", "P-051")])
    with pytest.raises(write_back.WriteBackError, match="blank"):
        write_back.assert_row_shape(rows)


def test_parent_order_follows_037_document_order():
    leaves = [_leaf("B-01", "B"), _leaf("A-01", "A"), _leaf("B-02", "B")]
    assert write_back.parent_order(leaves) == ["B", "A"]


# ---------------------------------------------------------------------------
# end-to-end against the real workbook
# ---------------------------------------------------------------------------

@needs_workbook
def test_write_back_is_idempotent(tmp_path):
    """Re-running must produce a byte-identical workbook.

    Three rework passes are queued behind pending RD-1 rulings; each one
    regenerates this file, and a diff must show only what the ruling changed.
    """
    import time

    a, b = tmp_path / "a.xlsx", tmp_path / "b.xlsx"
    kw = dict(src=SRC, data=DATA, generated=GENERATED, revision="Z", when="2026-01-01")
    r1 = write_back.run(out=a, **kw)
    # xlsx embeds wall-clock timestamps in the zip entries and docProps; without
    # a gap here the test passes whenever both runs land in the same second,
    # which is how an earlier version of this test passed while the
    # normalisation it was meant to cover was not wired in at all.
    time.sleep(1.1)
    r2 = write_back.run(out=b, **kw)
    assert r1["sha256"] == r2["sha256"], "write-back is not reproducible"
    assert a.read_bytes() == b.read_bytes()


@needs_workbook
def test_done_region_is_untouched(tmp_path):
    """Rows 10-332 are out of scope for this regeneration (A-005)."""
    out = tmp_path / "out.xlsx"
    result = write_back.run(src=SRC, data=DATA, generated=GENERATED, out=out,
                            revision="Z", when="2026-01-01")
    src_wb = openpyxl.load_workbook(SRC)
    out_wb = openpyxl.load_workbook(out)
    before = write_back.hash_region(src_wb[write_back.SHEET], 10, 332)
    after = write_back.hash_region(out_wb[write_back.SHEET], 10, 332)
    assert before == after == result["done_region_sha256"]


@needs_workbook
def test_every_remaining_leaf_reaches_the_workbook(tmp_path):
    out = tmp_path / "out.xlsx"
    result = write_back.run(src=SRC, data=DATA, generated=GENERATED, out=out,
                            revision="Z", when="2026-01-01")
    leaves = {l["req_id"] for l in write_back.load_leaves(DATA)}
    ws = openpyxl.load_workbook(out)[write_back.SHEET]
    written = {ws.cell(r, write_back.COL["req_id"]).value
               for r in range(write_back.FIRST_NEW_ROW, ws.max_row + 1)}
    assert written == leaves
    assert result["blocked"] == 2


@needs_workbook
def test_framework_sheet_and_history_are_synced(tmp_path):
    out = tmp_path / "out.xlsx"
    write_back.run(src=SRC, data=DATA, generated=GENERATED, out=out,
                   revision="Z", when="2026-01-01")
    wb = openpyxl.load_workbook(out)
    fw = wb[write_back.FRAMEWORK_SHEET]
    for row, label in write_back.NEW_TEST_SETS.items():
        assert fw.cell(row, 1).value == label
    hist = wb[write_back.HISTORY_SHEET]
    rows = [hist.cell(r, 1).value for r in range(5, 20)]
    assert "Z" in rows, "ChangeHistory has no row for this revision"
