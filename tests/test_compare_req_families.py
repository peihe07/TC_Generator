"""Tests for scripts/compare_req_families.py.

The behaviour that carries the weight is axis discovery. AM/FM's 037-A03
carries the SWRA-A02's Description text in its Title field; a title-to-title
comparison finds zero matches and would have confirmed the prior assumption
that the two families are unrelated. The script must find the axis rather
than take one.

The second is what counts as "dropped": an old requirement whose descendant
is a paraphrase is still represented, and counting it as lost overstates the
number an assessor reads most closely.
"""
import importlib.util
import json
import sys
from pathlib import Path

import openpyxl
import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location(
    "tc_cmpfam", ROOT / "scripts" / "compare_req_families.py")
if _spec is None or _spec.loader is None:
    pytest.skip("compare_req_families.py not present", allow_module_level=True)
cmp_fam = importlib.util.module_from_spec(_spec)
sys.modules["tc_cmpfam"] = cmp_fam
_spec.loader.exec_module(cmp_fam)


HEADER = ["SWE-Requirement ID ", "Source Requirement ID", "Requirement  Title",
          "Requirement  Description", "Categorization"]


def report(tmp_path, name, rows):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Analysis Report"
    ws.append(["STLA Report_SWRA"])
    ws.append([])
    ws.append(HEADER)
    for r in rows:
        ws.append(r)
    p = tmp_path / name
    wb.save(p)
    return p


def run(tmp_path, new_rows, old_rows):
    new = report(tmp_path, "new.xlsx", new_rows)
    old = report(tmp_path, "old.xlsx", old_rows)
    out = tmp_path / "out"
    import argparse
    cmp_fam.run(argparse.Namespace(new=str(new), old=str(old), out=str(out),
                                   label_new="NEW", label_old="OLD"))
    return json.loads((out / "family_overlap.json").read_text(encoding="utf-8"))


BEHAVIOUR = ("When Browse button is pressed in AM and FM analog tuner mode, "
             "the HU shall display the browse category option for presets "
             "listed in numerical order including unset presets.")


def test_the_alignment_axis_is_discovered_not_assumed(tmp_path):
    """New.Title holds Old.Description; every other pairing finds nothing."""
    res = run(tmp_path,
              [["NEW-001", "s", BEHAVIOUR, "Elaborated Chinese prose here", "Functional"]],
              [["OLD-001", "s", "Browse Presets - Numerical Order", BEHAVIOUR, "Functional"]])
    assert res["axis"] == {"new_field": "title", "old_field": "description"}
    assert res["counts"]["strong"] == 1


def test_a_title_to_title_corpus_still_aligns_on_titles(tmp_path):
    res = run(tmp_path,
              [["NEW-001", "s", BEHAVIOUR, "d1", "Functional"]],
              [["OLD-001", "s", BEHAVIOUR, "totally different text", "Functional"]])
    assert res["axis"] == {"new_field": "title", "old_field": "title"}


def test_leaves_without_an_ancestor_are_counted_as_new_work(tmp_path):
    res = run(tmp_path,
              [["NEW-001", "s", BEHAVIOUR, "d", "Functional"],
               ["NEW-002", "s", "An entirely unrelated seek-up requirement", "d", "Functional"]],
              [["OLD-001", "s", "t", BEHAVIOUR, "Functional"]])
    assert res["counts"]["strong"] == 1
    assert res["unmatched_new"] == ["NEW-002"]


def test_a_paraphrased_ancestor_is_not_reported_as_dropped(tmp_path):
    """The band between plausible and strong is 'represented, not verbatim'."""
    near = BEHAVIOUR.replace("numerical order including unset presets.",
                             "numerical order.")
    res = run(tmp_path,
              [["NEW-001", "s", near, "d", "Functional"]],
              [["OLD-001", "s", "t", BEHAVIOUR, "Functional"]])
    assert res["orphaned_old"] == []
    assert res["counts"]["strong"] + res["counts"]["plausible"] == 1


def test_an_old_row_with_no_descendant_is_reported_as_dropped(tmp_path):
    res = run(tmp_path,
              [["NEW-001", "s", BEHAVIOUR, "d", "Functional"]],
              [["OLD-001", "s", "t", BEHAVIOUR, "Functional"],
               ["OLD-002", "s", "t2", "A preset save long-press requirement", "Functional"]])
    assert res["orphaned_old"] == ["OLD-002"]


def test_template_help_text_rows_are_not_treated_as_requirements(tmp_path):
    """Both templates carry a '< Mention the ID ... >' row under the header."""
    res = run(tmp_path,
              [["NEW-001", "s", BEHAVIOUR, "d", "Functional"]],
              [["< Mention the ID generated from the tool >", "", "", "", ""],
               ["OLD-001", "s", "t", BEHAVIOUR, "Functional"]])
    assert res["counts"]["old_rows"] == 1
    assert res["orphaned_old"] == []


def test_the_mapping_shape_is_reported(tmp_path):
    """A 1:1 mapping and a many-to-one mapping mean different things for a
    re-trace ruling, so the report must distinguish them."""
    res = run(tmp_path,
              [["NEW-001", "s", BEHAVIOUR, "d", "Functional"],
               ["NEW-002", "s", BEHAVIOUR, "d", "Functional"]],
              [["OLD-001", "s", "t", BEHAVIOUR, "Functional"]])
    assert res["counts"]["strong"] == 2
    assert len({s["old"] for s in res["strong"]}) == 1, "both map to one old row"
