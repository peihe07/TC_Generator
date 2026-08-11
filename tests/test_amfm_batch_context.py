"""Tests for the spec-table and cross-reference injection in make_batch_context.py.

Both mechanisms exist to stop a batch being generated from a guess, so their
failure modes are silent by nature: a sheet that parses into the wrong columns
still produces a context file, and a leaf whose citation is dropped still
produces test cases. What is pinned here is the parsing that is easy to get
subtly wrong (merged banner rows, a sheet holding more than one table) and the
per-leaf scoping of citations.
"""
import importlib.util
import sys
from pathlib import Path

import openpyxl
import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    "amfm_batch_ctx", ROOT / "features" / "amfm" / "scripts" / "make_batch_context.py")
if _spec is None or _spec.loader is None:
    pytest.skip("make_batch_context.py not present", allow_module_level=True)
mbc = importlib.util.module_from_spec(_spec)
sys.modules["amfm_batch_ctx"] = mbc
_spec.loader.exec_module(mbc)


def workbook(tmp_path, rows, sheet="Sheet1"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = sheet
    for r in rows:
        ws.append(r)
    p = tmp_path / "tables.xlsx"
    wb.save(p)
    return p


def cfg_for(tmp_path, path, **table):
    return {"root": tmp_path, "paths": {"src": path.name},
            "spec_tables": {"t": {"source": "src", "sheet": "Sheet1", **table}}}


# A sheet that stacks two tables: a feature grid, then the tuner configuration
# table with its own merged banner. Exactly the shape of the market
# configuration workbook.
STACKED = [
    ["", "US", "Canada"],
    ["AM/FM", "X", "X"],
    [None, None, None],
    ["", "Tuner Config Name", ""],
    ["Broadcast Band", "Europe", "North America"],
    ["Tuner with AF Capability", "PI, PS, AF, TA", "PI, PS, PTY"],
    ["Tuner without AF Capability", "PI, PS, PTY", ""],
]


def test_first_row_selects_the_wanted_table_on_a_stacked_sheet(tmp_path):
    p = workbook(tmp_path, STACKED)
    got = mbc.load_spec_tables(cfg_for(tmp_path, p, header_rows=2, first_row=3),
                               tmp_path, ["t"])["t"]
    assert got["row_label"] == "Broadcast Band"
    assert [r["state"] for r in got["rows"]] == ["Tuner with AF Capability",
                                                 "Tuner without AF Capability"]


def test_a_merged_banner_row_is_forward_filled_into_the_column_key(tmp_path):
    """A lone column label loses its group; `Europe` alone is not the answer."""
    p = workbook(tmp_path, STACKED)
    got = mbc.load_spec_tables(cfg_for(tmp_path, p, header_rows=2, first_row=3),
                               tmp_path, ["t"])["t"]
    assert got["rows"][0]["events"]["Tuner Config Name / Europe"] == "PI, PS, AF, TA"


def test_an_empty_cell_is_omitted_rather_than_carried_as_blank(tmp_path):
    p = workbook(tmp_path, STACKED)
    got = mbc.load_spec_tables(cfg_for(tmp_path, p, header_rows=2, first_row=3),
                               tmp_path, ["t"])["t"]
    assert "Tuner Config Name / North America" not in got["rows"][1]["events"]


def test_first_row_past_the_end_fails_loud(tmp_path):
    p = workbook(tmp_path, STACKED)
    with pytest.raises(mbc.ContextError, match="past the last row"):
        mbc.load_spec_tables(cfg_for(tmp_path, p, header_rows=2, first_row=99),
                             tmp_path, ["t"])


def test_a_sheet_that_is_not_in_the_file_fails_loud(tmp_path):
    p = workbook(tmp_path, STACKED)
    cfg = cfg_for(tmp_path, p, header_rows=1)
    cfg["spec_tables"]["t"]["sheet"] = "Missing"
    with pytest.raises(mbc.ContextError, match="no worksheet"):
        mbc.load_spec_tables(cfg, tmp_path, ["t"])


def test_a_batch_citing_an_undeclared_table_fails_loud(tmp_path):
    p = workbook(tmp_path, STACKED)
    with pytest.raises(mbc.ContextError, match="no such entry"):
        mbc.load_spec_tables(cfg_for(tmp_path, p, header_rows=1), tmp_path,
                             ["not_declared"])


# ----------------------------------------------------------- cross-references

CITATIONS = {
    "CFTS019-718": {"doc": "CFTS019", "status": "unresolved-scheme-mismatch",
                    "req_ids": ["SWE-RA-RAD-014"],
                    "citing_clauses": [{"clause_id": 4872420,
                                        "context": "play the rejection tone"}]},
    "CFTS028-1": {"doc": "CFTS028", "status": "document-not-supplied",
                  "req_ids": ["SWE-RA-RAD-025"],
                  "citing_clauses": [{"clause_id": 4872439, "context": "VR"}]},
}


def test_only_the_citing_leafs_own_tokens_are_attached():
    got = mbc.leaf_citations(CITATIONS, "SWE-RA-RAD-014")
    assert [c["token"] for c in got] == ["CFTS019-718"]
    assert mbc.leaf_citations(CITATIONS, "SWE-RA-RAD-999") == []


def test_an_unresolved_citation_carries_the_cite_form_instruction():
    got = mbc.leaf_citations(CITATIONS, "SWE-RA-RAD-014")[0]
    assert got["handling"].startswith("cite-form")
    assert "CFTS019-718" in got["instruction"]
    assert "referenced_text" not in got


def test_a_ruled_citation_carries_the_clause_text_instead_of_candidates():
    ruled = {"CFTS019-718": dict(CITATIONS["CFTS019-718"],
                                 status="resolved-by-ruling",
                                 resolved_clause=4866062, ruling="R11",
                                 resolved_section="1.3.2.6",
                                 resolved_text="The key press rejection tone "
                                               "shall be applied")}
    got = mbc.leaf_citations(ruled, "SWE-RA-RAD-014")[0]
    assert got["referenced_text"].startswith("The key press rejection tone")
    assert got["ruling"] == "R11"
