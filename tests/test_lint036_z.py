"""lint036 檢查 Z —— Vehicle Model 七欄 1／0（R-CAM2，Camera profile 專屬）。

判準三項逐一正反例；另驗其 feature 專屬之啟用面（`--profile camera` 才生效）
與「七欄不齊時每 sheet 記一筆」之粒度。
"""

from __future__ import annotations

import sys
from pathlib import Path

import openpyxl
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import lint036  # noqa: E402

VM = lint036.VEHICLE_MODEL_HEADERS
# 母本第 9 列之標頭形制（R-G48 實測）：首行為車型名，第二行為 EE
VM_HEADER_TEXT = {
    "HDCC27": "HDCC27\nAtl-Hi\n",
    "DT27": "DT27\nAtl-Hi\n",
    "VF(ProMaster)637": "VF(ProMaster)637\nAtl-Mi",
    "Commander (598)": "Commander (598)\nAtl-Mi",
    "Regengade (5210)": "Regengade (5210)\nAtl-Mi",
    "Toro(2261)": "Toro(2261)\nAtl-Mi",
    "Fastack (376)": "Fastack (376)\nAtl-Mi",
}
# 全合規之一列：五個有效車型全勾 1，598／5210 為 0
OK_ROW = {"HDCC27": "1", "DT27": "1", "VF(ProMaster)637": "1",
          "Commander (598)": "0", "Regengade (5210)": "0",
          "Toro(2261)": "1", "Fastack (376)": "1"}


def run_row(values: dict[str, str]) -> list[lint036.Violation]:
    """以母本欄序（T–Z＝索引 19–25）組一列，跑 check_vehicle_model。"""
    columns = {name: 19 + i for i, name in enumerate(VM)}
    raw = [None] * 26
    for name, idx in columns.items():
        raw[idx] = values.get(name)
    return lint036.check_vehicle_model(tuple(raw), columns, 10, "TC-001")


def details(values: dict[str, str]) -> list[str]:
    return [v.detail for v in run_row(values)]


# --- (a) 七欄每欄須為 1 或 0 -------------------------------------------------

def test_a_all_one_zero_passes():
    assert run_row(OK_ROW) == []


@pytest.mark.parametrize("bad", ["", "  ", "X", "Y", "N", "2", "1.0", "一"])
def test_a_non_one_zero_flags(bad):
    values = dict(OK_ROW, **{"HDCC27": bad})
    hits = run_row(values)
    assert len(hits) == 1
    assert hits[0].check == "Z"
    assert hits[0].field == "vehicle_model[HDCC27]"
    assert "R-CAM2(a)" in hits[0].detail


def test_a_nbsp_and_whitespace_are_stripped():
    """`\\xa0` 與前後空白不算違規 —— 不可見字元由 Q 管，Z 只判值。"""
    assert run_row(dict(OK_ROW, **{"DT27": " 1 "})) == []
    assert run_row(dict(OK_ROW, **{"DT27": "\xa01\xa0"})) == []


def test_a_numeric_cell_is_accepted():
    """儲存格為數值 1／0（非字串）時亦合規。"""
    assert run_row(dict(OK_ROW, **{"HDCC27": 1, "Commander (598)": 0})) == []


# --- (b) 598／5210 恆為 0 ----------------------------------------------------

@pytest.mark.parametrize("name", ["Commander (598)", "Regengade (5210)"])
def test_b_unsupported_model_must_be_zero(name):
    hits = run_row(dict(OK_ROW, **{name: "1"}))
    assert [v.check for v in hits] == ["Z"]
    assert "R-CAM2(b)" in hits[0].detail
    assert hits[0].field == f"vehicle_model[{name}]"


@pytest.mark.parametrize("name", ["Commander (598)", "Regengade (5210)"])
def test_b_empty_unsupported_reports_a_not_b(name):
    """空值先由 (a) 攔下，不重複記 (b)。"""
    hits = run_row(dict(OK_ROW, **{name: ""}))
    assert len(hits) == 1
    assert "R-CAM2(a)" in hits[0].detail


# --- (c) 五個有效車型欄至少一個 1 --------------------------------------------

def test_c_all_active_zero_flags():
    values = dict(OK_ROW, **{"HDCC27": "0", "DT27": "0",
                             "VF(ProMaster)637": "0", "Toro(2261)": "0",
                             "Fastack (376)": "0"})
    hits = run_row(values)
    assert [v.check for v in hits] == ["Z"]
    assert "R-CAM2(c)" in hits[0].detail


def test_c_single_active_one_passes():
    values = dict(OK_ROW, **{"HDCC27": "0", "DT27": "0",
                             "VF(ProMaster)637": "0", "Toro(2261)": "0"})
    assert run_row(values) == []          # Fastack 仍為 1


def test_c_not_reported_when_a_already_flagged():
    """(a) 已命中時不另報 (c) —— 值不合法即無從判「至少一個 1」。"""
    values = dict(OK_ROW, **{"HDCC27": "", "DT27": "0",
                             "VF(ProMaster)637": "0", "Toro(2261)": "0",
                             "Fastack (376)": "0"})
    assert [v.detail for v in run_row(values)] == [
        v for v in details(values) if "R-CAM2(a)" in v]


# --- 欄位對照 ----------------------------------------------------------------

def test_column_map_matches_mother_workbook_headers():
    header = [None] * 19 + [VM_HEADER_TEXT[n] for n in VM] + ["Test Case Author\n測試案例作者"]
    columns = lint036.build_vehicle_model_columns(header)
    assert columns == {n: 19 + i for i, n in enumerate(VM)}


def test_column_map_ignores_second_line_ee_variation():
    """第二行之 EE 換行位置不同不影響比對。"""
    header = [None] * 19 + [f"{n}\nAtl-Whatever" for n in VM]
    assert len(lint036.build_vehicle_model_columns(header)) == len(VM)


def test_column_map_rejects_prefix_only_match():
    """`HDCC27 Atl-Hi`（同一行）非母本形制，首行不等即不匹配。"""
    header = [None] * 19 + ["HDCC27 Atl-Hi"]
    assert lint036.build_vehicle_model_columns(header) == {}


# --- 啟用面（feature 專屬）---------------------------------------------------

def test_z_enabled_only_for_camera_profile():
    assert "Z" in lint036.check_order("camera")
    assert "Z" not in lint036.check_order("popup")
    assert "Z" not in lint036.check_order(None)


def test_z_has_report_metadata():
    for table in (lint036.CHECK_TITLES, lint036.CHECK_STATUS,
                  lint036.CHECK_GRANULARITY):
        assert "Z" in table


# --- sheet 層：七欄不齊時每 sheet 一筆 ---------------------------------------

HEADERS = ["No.#", "Requirement or Design ID", "Test Case ID", "Test Group",
           "Test Set", "Test Item", "Pre-Conditions", "Input Test Data",
           "Test procedure", "Expected Result", "Specification Reference",
           "Test Case Reference ID", "Test Case Priority",
           "Estimated Test Time", "Test Case Design Methods",
           "Functional Safety"]
BODY = ["1", "SWE-CAM-001", "NR1L-RVC-001", "Rear View Camera",
        "Startup and Shutdown",
        "The system shall display the camera image\n(camera image shown)",
        "1. The vehicle is in REVERSE", "NA",
        '1. Press "Apps" on Menu Bar to open App Drawer',
        "1. The camera image is displayed", "CFTS092_1.3.6", "NEW", "P1",
        "5", "Equivalence Partitioning", "NA"]


def build_workbook(path: Path, vm_rows: list[dict[str, str]] | None) -> Path:
    """造一本最小 FW036 工作簿；`vm_rows` 為 None 時不建 Vehicle Model 七欄。"""
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Test Case Specification 測試用例規範"
    header = list(HEADERS)
    if vm_rows is not None:
        header += [VM_HEADER_TEXT[n] for n in VM]
    header.append("Test Case Author\n測試案例作者")
    ws.append([None])                       # 列 1：留白，header 於列 2
    ws.append(header)
    for i in range(len(vm_rows) if vm_rows is not None else 3):
        row = list(BODY)
        if vm_rows is not None:
            row += [vm_rows[i].get(n) for n in VM]
        row.append("PeiPYHsu")
        ws.append(row)
    wb.save(path)
    return path


def test_sheet_without_vehicle_model_columns_reports_once(tmp_path):
    path = build_workbook(tmp_path / "no_vm.xlsx", None)
    result = lint036.lint_workbook(path, profile="camera")[0]
    z = [v for v in result.violations if v.check == "Z"]
    assert result.data_rows == 3
    assert len(z) == 1                      # 3 列，仍只記一筆
    assert "無完整之" in z[0].detail
    assert "缺 HDCC27" in z[0].snippet


def test_sheet_with_valid_vehicle_model_is_clean(tmp_path):
    path = build_workbook(tmp_path / "ok.xlsx", [OK_ROW] * 3)
    result = lint036.lint_workbook(path, profile="camera")[0]
    assert [v for v in result.violations if v.check == "Z"] == []


def test_sheet_reports_per_row_per_column(tmp_path):
    rows = [OK_ROW,
            dict(OK_ROW, **{"HDCC27": ""}),
            dict(OK_ROW, **{"Commander (598)": "1", "DT27": "X"})]
    path = build_workbook(tmp_path / "bad.xlsx", rows)
    result = lint036.lint_workbook(path, profile="camera")[0]
    z = [v for v in result.violations if v.check == "Z"]
    assert len(z) == 3                      # 第 2 列 1 筆、第 3 列 2 筆
    assert {v.row for v in z} == {4, 5}     # header 於列 2，資料自列 3


def test_sheet_z_silent_without_camera_profile(tmp_path):
    path = build_workbook(tmp_path / "no_vm2.xlsx", None)
    for profile in (None, "popup"):
        result = lint036.lint_workbook(path, profile=profile)[0]
        assert [v for v in result.violations if v.check == "Z"] == []
