"""Tests for Excel parser module."""
import os
import pytest
from openpyxl import Workbook

from parser import parse_tc_xlsx, parse_test_group_from_filename


@pytest.fixture
def sample_xlsx(tmp_path):
    """Create a sample TC xlsx file for testing."""
    filepath = tmp_path / "SomeProject_SWQT_DeviceManager_20260408.xlsx"
    wb = Workbook()

    # Product Document sheet
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="newR1L")

    # Test Case Specification&Result sheet
    ws_tc = wb.create_sheet("Test Case Specification&Result")
    # Header row 9
    headers = {
        2: "Test Level", 3: "Verification Criteria", 4: "Requirement or Design ID",
        5: "Functional Safety", 6: "Test Case ID", 7: "Test Group",
        8: "Test Set", 9: "Test Item", 10: "Pre-Conditions",
        11: "Input Test Data", 12: "Test Procedure", 13: "Expected Result",
        14: "Specification Reference", 15: "Remark", 16: "Test Case Priority",
        17: "Test Case Design Method",
    }
    for col, name in headers.items():
        ws_tc.cell(row=9, column=col, value=name)

    # Data rows (10, 11, 12)
    rows_data = [
        {
            "D": "SWE1-HMI-DM-001-01",
            "I": "PDM01.1) The Device Manager can be added to the status bar.",
            "L": "1. Old procedure",
            "M": "1. Old result",
        },
        {
            "D": "SWE1-HMI-DM-001-02",
            "I": "PDM01.2) The Device Manager icon shows connected device count.",
            "L": "",
            "M": "",
        },
        {
            "D": "SWE1-HMI-DM-002-01",
            "I": "PDM02) User can open Device Manager from the menu bar.",
            "L": "1. Some procedure",
            "M": "1. Some result",
        },
    ]
    col_map = {"D": 4, "I": 9, "L": 12, "M": 13}
    for i, row_data in enumerate(rows_data):
        row_num = 10 + i
        for col_letter, value in row_data.items():
            ws_tc.cell(row=row_num, column=col_map[col_letter], value=value)

    wb.save(filepath)
    return str(filepath)


@pytest.fixture
def empty_xlsx(tmp_path):
    """Create an xlsx with no data rows."""
    filepath = tmp_path / "Empty_SWQT_TestGroup_20260408.xlsx"
    wb = Workbook()
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="projX")

    ws_tc = wb.create_sheet("Test Case Specification&Result")
    ws_tc.cell(row=9, column=4, value="Requirement or Design ID")
    ws_tc.cell(row=9, column=9, value="Test Item")

    wb.save(filepath)
    return str(filepath)


class TestParseTestGroupFromFilename:
    def test_standard_filename(self):
        result = parse_test_group_from_filename(
            "SomeProject_SWQT_DeviceManager_20260408.xlsx"
        )
        assert result == "DeviceManager"

    def test_filename_with_path(self):
        result = parse_test_group_from_filename(
            "/path/to/SomeProject_SWQT_MediaPlayer_20260410.xlsx"
        )
        assert result == "MediaPlayer"

    def test_filename_no_match(self):
        result = parse_test_group_from_filename("random_file.xlsx")
        assert result is None


class TestParseTcXlsx:
    def test_project_name(self, sample_xlsx):
        result = parse_tc_xlsx(sample_xlsx)
        assert result["project"] == "newR1L"

    def test_test_group(self, sample_xlsx):
        result = parse_tc_xlsx(sample_xlsx)
        assert result["test_group"] == "DeviceManager"

    def test_row_count(self, sample_xlsx):
        result = parse_tc_xlsx(sample_xlsx)
        assert result["row_count"] == 3

    def test_rows_structure(self, sample_xlsx):
        result = parse_tc_xlsx(sample_xlsx)
        rows = result["rows"]
        assert len(rows) == 3

        row0 = rows[0]
        assert row0["row_num"] == 10
        assert row0["req_id"] == "SWE1-HMI-DM-001-01"
        assert "PDM01.1" in row0["test_item"]

    def test_column_fill_status(self, sample_xlsx):
        result = parse_tc_xlsx(sample_xlsx)
        fill = result["column_fill_status"]
        # Col D (req_id) should be 3/3 filled
        assert fill["D"] == 3
        # Col L (procedure) has 2 filled, 1 empty
        assert fill["L"] == 2

    def test_empty_file(self, empty_xlsx):
        result = parse_tc_xlsx(empty_xlsx)
        assert result["row_count"] == 0
        assert result["rows"] == []

    def test_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            parse_tc_xlsx("/nonexistent/file.xlsx")

    def test_skips_blank_rows_and_continues(self, tmp_path):
        filepath = tmp_path / "SomeProject_SWQT_DeviceManager_20260408.xlsx"
        wb = Workbook()
        ws_pd = wb.active
        ws_pd.title = "Product Document"
        ws_pd.cell(row=3, column=2, value="newR1L")

        ws_tc = wb.create_sheet("Test Case Specification&Result")
        ws_tc.cell(row=9, column=4, value="Requirement or Design ID")
        ws_tc.cell(row=9, column=9, value="Test Item")
        ws_tc.cell(row=10, column=4, value="SWE1-HMI-DM-001-01")
        ws_tc.cell(row=10, column=9, value="First row")
        ws_tc.cell(row=12, column=4, value="SWE1-HMI-DM-002-01")
        ws_tc.cell(row=12, column=9, value="Second row after blank line")
        wb.save(filepath)

        result = parse_tc_xlsx(str(filepath))
        assert result["row_count"] == 2
        assert [row["row_num"] for row in result["rows"]] == [10, 12]
