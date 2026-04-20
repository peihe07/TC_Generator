"""Tests for Excel writer module (RULES.md §10.3)."""
import os
import pytest
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment

from writer import (
    write_generated_results,
    write_framework_sheet,
    build_output_path,
)


@pytest.fixture
def input_xlsx(tmp_path):
    """Create a minimal input xlsx to write results into."""
    filepath = tmp_path / "SomeProject_SWQT_DeviceManager_20260408.xlsx"
    wb = Workbook()

    # Product Document sheet
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="newR1L")

    # TC sheet with header + 2 data rows
    ws_tc = wb.create_sheet("Test Case Specification&Result")
    headers = {
        4: "Requirement or Design ID", 6: "Test Case ID", 7: "Test Group",
        8: "Test Set", 9: "Test Item", 10: "Pre-Conditions",
        11: "Input Test Data", 12: "Test Procedure", 13: "Expected Result",
        14: "Specification Reference", 16: "Test Case Priority",
        17: "Test Case Design Method",
    }
    for col, name in headers.items():
        ws_tc.cell(row=9, column=col, value=name)

    # Row 10: has req_id and original test item
    ws_tc.cell(row=10, column=4, value="SWE1-HMI-DM-001-01")
    ws_tc.cell(row=10, column=9, value="PDM01.1) Original text here.")

    # Row 11: second row
    ws_tc.cell(row=11, column=4, value="SWE1-HMI-DM-002-01")
    ws_tc.cell(row=11, column=9, value="PDM02) Another original text.")

    # Untouched column B with data (should be preserved)
    ws_tc.cell(row=10, column=2, value="SWE6")
    ws_tc.cell(row=11, column=2, value="SWE6")

    # Test Case Framework sheet (empty)
    wb.create_sheet("Test Case Framework")

    wb.save(filepath)
    return str(filepath)


@pytest.fixture
def generated_rows():
    return [
        {
            "row_num": 10,
            "tc_id": "newR1L-DMR-001",
            "test_group": "DeviceManager",
            "test_set": "Access & Entry",
            "test_item_rewrite": "(User adds DM → DM icon displayed)",
            "pre_conditions": "1. BT enabled on HU",
            "input_test_data": "Status bar menu",
            "test_procedure": "1. Open settings to access.\n2. Add DM and verify icon appears.",
            "expected_result": "1. Settings shown.\n2. DM icon displayed.",
            "spec_reference": "Device_Manager_HMI Logic_2.3",
            "priority": "Medium",
            "design_method": "功能測試 (Functional based ; no specific technique)",
        },
        {
            "row_num": 11,
            "tc_id": "newR1L-DMR-002",
            "test_group": "DeviceManager",
            "test_set": "Access & Entry",
            "test_item_rewrite": "(User opens DM from menu → DM screen shown)",
            "pre_conditions": "NA",
            "input_test_data": "Menu bar icon",
            "test_procedure": "1. Tap menu bar to open.\n2. Select DM and verify it opens.",
            "expected_result": "1. Menu bar expanded.\n2. DM main screen displayed.",
            "spec_reference": "Device_Manager_HMI Logic_3.1",
            "priority": "Medium",
            "design_method": "功能測試 (Functional based ; no specific technique)",
        },
    ]


@pytest.fixture
def framework_data():
    return [
        {"test_group": "DeviceManager", "test_set": "Access & Entry", "req_count": 5},
        {"test_group": "DeviceManager", "test_set": "Device List", "req_count": 3},
    ]


class TestBuildOutputPath:
    def test_default(self):
        path = build_output_path("/data/input.xlsx")
        assert path.endswith("input_generated.xlsx")

    def test_output_dir(self):
        path = build_output_path("/data/input.xlsx", output_dir="/out")
        assert path.startswith("/out/")
        assert path.endswith("input_generated.xlsx")

    def test_strips_macos_duplicate_suffix_tc(self):
        # macOS Finder duplicates as "foo 拷貝.xlsx" — must not leak into output.
        path = build_output_path("/data/Project_SWQT_DeviceManager_20260408 拷貝.xlsx")
        assert path.endswith("Project_SWQT_DeviceManager_20260408_generated.xlsx")

    def test_strips_macos_duplicate_suffix_no_space(self):
        # Chinese duplicate marker without separating space.
        path = build_output_path("/data/foo拷貝.xlsx")
        assert path.endswith("foo_generated.xlsx")

    def test_strips_windows_copy_suffix(self):
        path = build_output_path("/data/report - Copy.xlsx")
        assert path.endswith("report_generated.xlsx")

    def test_strips_windows_copy_with_index(self):
        path = build_output_path("/data/report - Copy (2).xlsx")
        assert path.endswith("report_generated.xlsx")

    def test_strips_macos_english_copy(self):
        path = build_output_path("/data/foo copy 3.xlsx")
        assert path.endswith("foo_generated.xlsx")

    def test_keeps_clean_basename_unchanged(self):
        path = build_output_path("/data/Project_SWQT_DeviceManager_20260408.xlsx")
        assert path.endswith("Project_SWQT_DeviceManager_20260408_generated.xlsx")


class TestWriteGeneratedResults:
    def test_writes_tc_id(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert ws.cell(row=10, column=6).value == "newR1L-DMR-001"
        assert ws.cell(row=11, column=6).value == "newR1L-DMR-002"

    def test_writes_test_group(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert ws.cell(row=10, column=7).value == "DeviceManager"

    def test_appends_test_item_rewrite(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        cell_value = ws.cell(row=10, column=9).value
        # Original text preserved, rewrite appended
        assert "PDM01.1) Original text here." in cell_value
        assert "(User adds DM → DM icon displayed)" in cell_value

    def test_dedupes_rewrite_across_rows_sharing_req_id(self, input_xlsx, tmp_path):
        """A requirement split into multiple TC rows should only get the
        `()` summary appended on the first row — repeating it on every row
        is redundant since the summary describes the same requirement."""
        rows = [
            {
                "row_num": 10,
                "req_id": "SWE1-HMI-DM-001-01",
                "tc_id": "newR1L-DMR-001",
                "test_item_rewrite": "(Trigger → Outcome)",
            },
            {
                "row_num": 11,
                "req_id": "SWE1-HMI-DM-001-01",  # same requirement, split TC
                "tc_id": "newR1L-DMR-002",
                "test_item_rewrite": "(Trigger → Outcome)",
            },
        ]
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        # Row 10 keeps original + appended rewrite.
        assert "(Trigger → Outcome)" in ws.cell(row=10, column=9).value
        # Row 11 keeps its original Col I untouched (no rewrite appended).
        row11_value = ws.cell(row=11, column=9).value or ""
        assert "(Trigger → Outcome)" not in row11_value
        assert "PDM02) Another original text." in row11_value

    def test_rewrite_applied_once_per_distinct_req_id(self, input_xlsx, tmp_path):
        """Different req_ids each get their own rewrite even if text matches."""
        rows = [
            {
                "row_num": 10,
                "req_id": "SWE1-HMI-DM-001-01",
                "tc_id": "newR1L-DMR-001",
                "test_item_rewrite": "(First → A)",
            },
            {
                "row_num": 11,
                "req_id": "SWE1-HMI-DM-002-01",  # different req_id
                "tc_id": "newR1L-DMR-002",
                "test_item_rewrite": "(Second → B)",
            },
        ]
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert "(First → A)" in ws.cell(row=10, column=9).value
        assert "(Second → B)" in ws.cell(row=11, column=9).value

    def test_writes_procedure(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert "Open settings" in ws.cell(row=10, column=12).value

    def test_wrap_text_enabled(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert ws.cell(row=10, column=12).alignment.wrap_text is True

    def test_preserves_untouched_columns(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        # Col B should be untouched
        assert ws.cell(row=10, column=2).value == "SWE6"
        # Col D (req_id) should be untouched
        assert ws.cell(row=10, column=4).value == "SWE1-HMI-DM-001-01"

    def test_writes_all_generated_columns(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, generated_rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        row = 10
        assert ws.cell(row=row, column=10).value is not None  # Pre-Conditions (J)
        assert ws.cell(row=row, column=11).value is not None  # Input Test Data (K)
        assert ws.cell(row=row, column=13).value is not None  # Expected Result (M)
        assert ws.cell(row=row, column=14).value is not None  # Spec Reference (N)
        assert ws.cell(row=row, column=16).value == "Medium"  # Priority (P)
        assert "功能測試" in ws.cell(row=row, column=17).value  # Design Method (Q)

    def test_replaces_existing_rewrite_instead_of_appending_again(self, input_xlsx, generated_rows, tmp_path):
        first_output = str(tmp_path / "first.xlsx")
        second_output = str(tmp_path / "second.xlsx")

        write_generated_results(input_xlsx, generated_rows, first_output)
        write_generated_results(first_output, generated_rows, second_output)

        wb = load_workbook(second_output)
        ws = wb["Test Case Specification&Result"]
        cell_value = ws.cell(row=10, column=9).value
        assert cell_value.count("(User adds DM → DM icon displayed)") == 1

    def test_clears_stale_optional_fields(self, input_xlsx, tmp_path):
        output = str(tmp_path / "output.xlsx")
        rows = [{
            "row_num": 10,
            "tc_id": "newR1L-DMR-001",
            "test_group": "DeviceManager",
            "test_set": "Access & Entry",
            "test_item_rewrite": "(User adds DM → DM icon displayed)",
            "pre_conditions": "NA",
            "input_test_data": "NA",
            "test_procedure": "1. Open settings.\n2. Verify the result.",
            "expected_result": "1. Settings shown.\n2. Result verified.",
            "spec_reference": "Spec_1",
            "priority": "Medium",
            "design_method": "功能測試 (Functional based ; no specific technique)",
        }]
        write_generated_results(input_xlsx, rows, output)

        rows[0]["test_set"] = None
        rows[0]["spec_reference"] = None
        write_generated_results(output, rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert ws.cell(row=10, column=8).value is None
        assert ws.cell(row=10, column=14).value is None

    def test_respects_selected_fields_when_writing(self, input_xlsx, generated_rows, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_generated_results(
            input_xlsx,
            generated_rows,
            output,
            selected_fields={"expected_result", "priority"},
        )

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        assert ws.cell(row=10, column=6).value is None  # TC ID untouched
        assert ws.cell(row=10, column=9).value == "PDM01.1) Original text here."  # no rewrite appended
        assert ws.cell(row=10, column=10).value is None  # Pre-Conditions untouched
        assert ws.cell(row=10, column=13).value == "1. Settings shown.\n2. DM icon displayed."
        assert ws.cell(row=10, column=16).value == "Medium"


    def test_multi_tc_per_row_inserts_rows(self, input_xlsx, tmp_path):
        """AI 把 1 個 req 拆成 3 筆 TC 時，writer 應該在原列下方插 2 列，
        複製 C/D/I 欄，然後各列寫入自己的 TC 內容。"""
        rows = [
            {
                "row_num": 10,
                "req_id": "SWE1-HMI-DM-001-01",
                "tc_id": "newR1L-DMR-001",
                "test_item_rewrite": "(Trigger → Outcome A)",
                "pre_conditions": "pre-A",
                "test_procedure": "1. step A",
                "expected_result": "1. result A",
                "priority": "High",
                "design_method": "Functional",
            },
            {
                "row_num": 10,
                "req_id": "SWE1-HMI-DM-001-01",
                "tc_id": "newR1L-DMR-002",
                "test_item_rewrite": "(Trigger → Outcome B)",
                "pre_conditions": "pre-B",
                "test_procedure": "1. step B",
                "expected_result": "1. result B",
                "priority": "Medium",
                "design_method": "Functional",
            },
            {
                "row_num": 10,
                "req_id": "SWE1-HMI-DM-001-01",
                "tc_id": "newR1L-DMR-003",
                "test_item_rewrite": "(Trigger → Outcome C)",
                "pre_conditions": "pre-C",
                "test_procedure": "1. step C",
                "expected_result": "1. result C",
                "priority": "Low",
                "design_method": "Functional",
            },
            # 第二個 req 放在原本的 row 11，確認 insert 後的 offset 正確。
            {
                "row_num": 11,
                "req_id": "SWE1-HMI-DM-002-01",
                "tc_id": "newR1L-DMR-004",
                "test_item_rewrite": "(Other trigger → outcome)",
                "pre_conditions": "pre-D",
                "test_procedure": "1. step D",
                "expected_result": "1. result D",
                "priority": "High",
                "design_method": "Functional",
            },
        ]
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        # Row 10–12 都屬於第一個 req，C/D/I 欄位值應相同。
        for r in (10, 11, 12):
            assert ws.cell(row=r, column=4).value == "SWE1-HMI-DM-001-01"
            assert "PDM01.1) Original text here." in (ws.cell(row=r, column=9).value or "")
        # 三個 TC ID 各自寫入各自的列。
        assert ws.cell(row=10, column=6).value == "newR1L-DMR-001"
        assert ws.cell(row=11, column=6).value == "newR1L-DMR-002"
        assert ws.cell(row=12, column=6).value == "newR1L-DMR-003"
        # procedure / expected 各自分開。
        assert ws.cell(row=10, column=12).value == "1. step A"
        assert ws.cell(row=11, column=12).value == "1. step B"
        assert ws.cell(row=12, column=12).value == "1. step C"
        assert ws.cell(row=10, column=13).value == "1. result A"
        assert ws.cell(row=12, column=13).value == "1. result C"
        # rewrite 只 append 在第一筆（row 10），其餘列保留原始 test_item。
        row10_i = ws.cell(row=10, column=9).value
        assert "(Trigger → Outcome A)" in row10_i
        row11_i = ws.cell(row=11, column=9).value or ""
        assert "(Trigger → Outcome B)" not in row11_i
        # 第二個 req 被 offset 後應該落在 row 13（10 + 2 extras + 1）。
        assert ws.cell(row=13, column=4).value == "SWE1-HMI-DM-002-01"
        assert ws.cell(row=13, column=6).value == "newR1L-DMR-004"

    def test_does_not_overwrite_template_with_empty_values(self, input_xlsx, tmp_path):
        """Template 既有內容（例如 spec 帶進來的 test_procedure）不應該被
        空字串 / None 覆蓋。"""
        # 先模擬 template 原本就有 procedure/expected 內容。
        wb = load_workbook(input_xlsx)
        ws = wb["Test Case Specification&Result"]
        ws.cell(row=10, column=12, value="template procedure from spec")
        ws.cell(row=10, column=13, value="template expected from spec")
        wb.save(input_xlsx)

        rows = [{
            "row_num": 10,
            "req_id": "SWE1-HMI-DM-001-01",
            "tc_id": "newR1L-DMR-001",
            "test_item_rewrite": "(X → Y)",
            "pre_conditions": "",         # 空字串：不應蓋掉 template
            "test_procedure": "",
            "expected_result": "",
            "priority": "Medium",
            "design_method": "Functional",
        }]
        output = str(tmp_path / "output.xlsx")
        write_generated_results(input_xlsx, rows, output)

        wb = load_workbook(output)
        ws = wb["Test Case Specification&Result"]
        # Template 原本的內容保留。
        assert ws.cell(row=10, column=12).value == "template procedure from spec"
        assert ws.cell(row=10, column=13).value == "template expected from spec"
        # 非空欄位仍有寫入。
        assert ws.cell(row=10, column=16).value == "Medium"


class TestWriteFrameworkSheet:
    def test_writes_data(self, input_xlsx, framework_data, tmp_path):
        output = str(tmp_path / "output.xlsx")
        write_framework_sheet(input_xlsx, framework_data, output)

        wb = load_workbook(output)
        ws = wb["Test Case Framework"]
        assert ws.cell(row=1, column=1).value == "Test Group"
        assert ws.cell(row=2, column=1).value == "DeviceManager"
        assert ws.cell(row=2, column=2).value == "Access & Entry"
        assert ws.cell(row=2, column=3).value == 5
        assert ws.cell(row=3, column=2).value == "Device List"
