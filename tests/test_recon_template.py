"""Tests for scripts/recon.py template adaptation — columns by header text.

Two template families are in play and neither is a superset of the other:

- the FM-WI-FSM-036 workbook exists in a pre-C layout (Home, AM/FM) and a
  revision-C layout (blank form 2026-01-21) that inserts "Estimated Test Time
  (mins)" at Q and pushes design_method..remarks one column right
- the 037 Analysis Report puts Categorization at column 7 with the value
  "Functional Requirement" for Home, and at column 31 with the value
  "Functional" for AM/FM, behind 24 review-criteria columns

Reading either by fixed offsets is silently wrong on the other: the AM/FM
report classifies all 102 leaves as headings and reports zero regen targets,
which is a legal state for a finished workbook and so passes unnoticed.
"""
import importlib.util
import sys
from pathlib import Path

import openpyxl
import pytest

ROOT = Path(__file__).resolve().parent.parent

_spec = importlib.util.spec_from_file_location("tc_recon", ROOT / "scripts" / "recon.py")
if _spec is None or _spec.loader is None:
    pytest.skip("scripts/recon.py not present", allow_module_level=True)
recon = importlib.util.module_from_spec(_spec)
sys.modules["tc_recon"] = recon
_spec.loader.exec_module(recon)


# Real header text, verbatim from the workbooks (newlines included — the
# bilingual second line is what breaks naive substring matching).
PRE_C_HEADER = [
    None,
    "No.#\n序號",
    "Requirement or Design\nID (Polarion)\n設計/需求 ID (Polarion)",
    "Requirement or Design ID\n需求/設計 ID",
    "Test Case ID (TestRail)\n測試用例 ID (TestRail)",
    "Test Case ID\n測試用例ID",
    "Test Group\n測試組",
    "Test Set\n測試集",
    "Test Item\n測試項目",
    "Pre-Conditions\n先前條件",
    "Input Test Data\n輸入條件",
    "Test procedure\n測試程序",
    "Expected Result\n預期結果",
    "Specification Reference \n規格參考",
    "Test Case Reference ID\n測項參考ID",
    "Test Case Priority\n測試用例優先級別",
    "Test Case Design \nMethods\n測試用例設計方法",
    "Functional Safety\n功能安全",
] + [f"Model{i}\nAtl-Hi" for i in range(7)] + [
    "Test Case Author\n測試案例作者",
    "Test Version\n測試版號",
    "Test Vehicle\n(Bench)\n測試車型(Bench)",
    "Test Period\n測試期間",
    "Tester\n測試者",
    "Test Result\n測試結果",
    "Defect ID\n缺陷ID",
    "Remarks\n備註",
]

REV_C_HEADER = (
    PRE_C_HEADER[:16]
    + ["Estimated Test Time (mins)\n預估測試時間\n（分鐘）"]
    + PRE_C_HEADER[16:]
)


def test_pre_c_layout_resolves_to_the_home_amfm_letters():
    cols, unresolved = recon.resolve_columns(tuple(PRE_C_HEADER))
    assert unresolved == []
    letters = {k: recon.idx_to_letter(v) for k, v in cols.items()}
    assert letters["req_id"] == "D"
    assert letters["design_method"] == "Q"
    assert letters["functional_safety"] == "R"
    assert letters["author"] == "Z"
    assert letters["remarks"] == "AG"
    assert "estimated_test_time" not in cols


def test_rev_c_layout_shifts_everything_after_priority():
    """The whole point of resolving by text: one inserted column moves five
    fields, and a stale letter map would write into the wrong cells."""
    cols, unresolved = recon.resolve_columns(tuple(REV_C_HEADER))
    assert unresolved == []
    letters = {k: recon.idx_to_letter(v) for k, v in cols.items()}
    assert letters["priority"] == "P", "unchanged: the insert is after it"
    assert letters["estimated_test_time"] == "Q"
    assert letters["design_method"] == "R"
    assert letters["functional_safety"] == "S"
    assert letters["author"] == "AA"
    assert letters["remarks"] == "AH"


def test_req_id_is_not_confused_with_the_polarion_column():
    """C and D both read 'Requirement or Design ID'; only C says Polarion."""
    cols, _ = recon.resolve_columns(tuple(PRE_C_HEADER))
    assert recon.idx_to_letter(cols["req_id"]) == "D"


def test_tc_reference_id_does_not_capture_the_two_test_case_id_columns():
    cols, _ = recon.resolve_columns(tuple(PRE_C_HEADER))
    assert recon.idx_to_letter(cols["tc_ref_id"]) == "O"


def test_a_missing_required_header_is_reported_not_guessed():
    header = list(PRE_C_HEADER)
    header[8] = "Something Else"          # was Test Item
    _, unresolved = recon.resolve_columns(tuple(header))
    assert any(u.startswith("test_item") for u in unresolved)


def test_a_duplicated_header_is_reported_not_arbitrated():
    header = list(PRE_C_HEADER)
    header[9] = "Test Item\n測試項目"       # now two Test Item columns
    _, unresolved = recon.resolve_columns(tuple(header))
    assert any(u.startswith("test_item") and "2 header matches" in u
               for u in unresolved)


# ------------------------------------------------------------ 037 report

def _a03(tmp_path, header, rows, name="a03.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Analysis Report"
    ws.append(["STLA Report_SWRA"])
    ws.append([])
    ws.append(header)
    for r in rows:
        ws.append(r)
    p = tmp_path / name
    wb.save(p)
    return p


HOME_SHAPE = ["SWE-Requirement ID ", "Source Requirement ID", "HMI Source ID",
              "Requirement  Title", "Requirement  Description",
              "Release Version", "Categorization", "FROP", "Sub Categorization"]

AMFM_SHAPE = ["SWE-Requirement ID ", "Source Requirement ID",
              "Requirement  Title", "Requirement  Description",
              "Requirement Status  ", "Release Version", "Feasibility",
              " Description/Action for Feasibility", "Categorization",
              "Sub Categorization", "Priority"]


def test_home_shape_leaves_and_headings(tmp_path):
    p = _a03(tmp_path, HOME_SHAPE, [
        ["SWE1-HMI-HOME-001", "s", "h", "t", "d", "1", "Functional Requirement", "", "NA"],
        ["SWE1-HMI-HOME-002", "s", "h", "t", "d", "1", "Heading", "", "NA"],
    ])
    res = recon.survey_a03(p)
    assert res["leaves"] == ["SWE1-HMI-HOME-001"]
    assert res["headings"] == ["SWE1-HMI-HOME-002"]


def test_amfm_shape_leaves_are_found_behind_the_review_columns(tmp_path):
    """'Functional' (AM/FM) and 'Functional Requirement' (Home) are the same
    classification written two ways, at columns 24 apart."""
    p = _a03(tmp_path, AMFM_SHAPE, [
        ["SWE-RA-RAD-001", "SYSAD_X", "t", "d", "New", "1.00.00", "Yes",
         "ok", "Functional", "NA", "High"],
        ["SWE-RA-RAD-002", "SYSAD_X", "t", "d", "New", "1.00.00", "Yes",
         "ok", "Functional", "NA", "High"],
    ])
    res = recon.survey_a03(p)
    assert res["leaves"] == ["SWE-RA-RAD-001", "SWE-RA-RAD-002"]
    assert res["headings"] == []
    assert res["categorization_col"] == recon.idx_to_letter(8)


def test_sub_categorization_never_wins_the_categorization_lookup(tmp_path):
    p = _a03(tmp_path, AMFM_SHAPE, [
        ["SWE-RA-RAD-001", "s", "t", "d", "New", "1", "Yes", "ok",
         "Functional", "NA", "High"],
    ])
    assert recon.survey_a03(p)["leaves"] == ["SWE-RA-RAD-001"]


def test_safety_attributes_are_reported_when_the_template_carries_them(tmp_path):
    header = ["ID", "ReqIF.ForeignID", "Source Id", "Title",
              "Requirement  Description", "Requirement Status  ",
              "Release Version", "ASIL Level", "FTTI", "Categorization"]
    p = _a03(tmp_path, header, [
        ["SWE-RAD-001", "4872420", "X", "t", "d", "New", "v", "QM", "NA", "Functional"],
        ["SWE-RAD-002", "4872421", "X", "t", "d", "New", "v", "ASIL B", "50ms", "Functional"],
    ])
    res = recon.survey_a03(p)
    assert res["has_safety_columns"] is True
    assert res["asil_distribution"] == {"QM": 1, "ASIL B": 1}


def test_absent_safety_columns_are_stated_as_absent(tmp_path):
    p = _a03(tmp_path, AMFM_SHAPE, [
        ["SWE-RA-RAD-001", "s", "t", "d", "New", "1", "Yes", "ok",
         "Functional", "NA", "High"],
    ])
    res = recon.survey_a03(p)
    assert res["has_safety_columns"] is False
    assert res["asil_distribution"] == {}


def test_a_report_without_a_header_row_fails_loud(tmp_path):
    p = _a03(tmp_path, ["A", "B", "C"], [["x", "y", "z"]])
    with pytest.raises(SystemExit):
        recon.survey_a03(p)
