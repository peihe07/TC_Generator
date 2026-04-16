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
