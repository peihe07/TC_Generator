"""Tests for CLI entry point."""
import pytest
from openpyxl import Workbook
from unittest.mock import patch
from openpyxl import load_workbook

from main import parse_args, _filter_rows, _estimate_cost, run


@pytest.fixture
def sample_xlsx(tmp_path):
    """Create minimal TC xlsx for CLI testing."""
    filepath = tmp_path / "Test_SWQT_DeviceManager_20260408.xlsx"
    wb = Workbook()
    ws_pd = wb.active
    ws_pd.title = "Product Document"
    ws_pd.cell(row=3, column=2, value="newR1L")

    ws_tc = wb.create_sheet("Test Case Specification&Result")
    for col, name in {4: "Req ID", 6: "TC ID", 9: "Test Item"}.items():
        ws_tc.cell(row=9, column=col, value=name)

    ws_tc.cell(row=10, column=4, value="SWE1-HMI-DM-001-01")
    ws_tc.cell(row=10, column=9, value="PDM01 test feature A")
    ws_tc.cell(row=11, column=4, value="SWE1-HMI-DM-002-01")
    ws_tc.cell(row=11, column=9, value="PDM02 test feature B")

    wb.create_sheet("Test Case Framework")
    wb.save(filepath)
    return str(filepath)


class TestParseArgs:
    def test_required_input(self):
        args = parse_args(["--input", "test.xlsx"])
        assert args.input == "test.xlsx"
        assert args.mode == "full"
        assert args.dry_run is False

    def test_all_options(self):
        args = parse_args([
            "--input", "in.xlsx",
            "--sys1", "sys1.xlsx",
            "--spec", "spec.pdf",
            "--model", "claude-haiku-4-5-20251001",
            "--batch-size", "10",
            "--mode", "incremental",
            "--dry-run",
            "--budget", "2.5",
        ])
        assert args.sys1 == "sys1.xlsx"
        assert args.batch_size == 10
        assert args.mode == "incremental"
        assert args.dry_run is True
        assert args.budget == 2.5

    def test_strict_validation_flag(self):
        args = parse_args(["--input", "test.xlsx", "--strict-validation"])
        assert args.strict_validation is True


class TestFilterRows:
    def test_full_mode(self):
        rows = [{"row_num": 10}, {"row_num": 11}]
        assert len(_filter_rows(rows, "full", None)) == 2

    def test_incremental_skips_existing(self):
        rows = [
            {"row_num": 10, "tc_id": "p-A-001"},
            {"row_num": 11, "tc_id": ""},
            {"row_num": 12},
        ]
        result = _filter_rows(rows, "incremental", None)
        assert len(result) == 2
        assert result[0]["row_num"] == 11

    def test_regenerate_by_row_num(self):
        rows = [
            {"row_num": 10, "req_id": "R001"},
            {"row_num": 11, "req_id": "R002"},
            {"row_num": 12, "req_id": "R003"},
        ]
        result = _filter_rows(rows, "regenerate", "10,12")
        assert len(result) == 2
        assert result[0]["row_num"] == 10
        assert result[1]["row_num"] == 12

    def test_regenerate_by_req_id(self):
        rows = [
            {"row_num": 10, "req_id": "R001"},
            {"row_num": 11, "req_id": "R002"},
        ]
        result = _filter_rows(rows, "regenerate", "R002")
        assert len(result) == 1
        assert result[0]["req_id"] == "R002"


class TestEstimateCost:
    def test_nonzero(self):
        cost = _estimate_cost(10, "claude-sonnet-4-6", 5)
        assert cost > 0

    def test_haiku_cheaper(self):
        sonnet = _estimate_cost(10, "claude-sonnet-4-6", 5)
        haiku = _estimate_cost(10, "claude-haiku-4-5-20251001", 5)
        assert haiku < sonnet


class TestDryRun:
    def test_dry_run_exits_zero(self, sample_xlsx, tmp_path):
        args = parse_args([
            "--input", sample_xlsx,
            "--output-dir", str(tmp_path / "out"),
            "--dry-run",
        ])
        exit_code = run(args)
        assert exit_code == 0


class TestRunGeneration:
    @patch("main.generate_single_tc")
    def test_invalid_existing_tc_ids_do_not_crash(self, mock_generate_single_tc, sample_xlsx, tmp_path):
        wb = Workbook()
        # placeholder to silence linter-style expectations in some environments
        del wb

        from openpyxl import load_workbook

        loaded = load_workbook(sample_xlsx)
        ws = loaded["Test Case Specification&Result"]
        ws.cell(row=10, column=6, value="bad-id")
        loaded.save(sample_xlsx)
        loaded.close()

        mock_generate_single_tc.return_value.tc_data = {
            "test_item_rewrite": "(Condition → Outcome)",
            "pre_conditions": "NA",
            "input_test_data": "NA",
            "test_procedure": "1. Perform setup.\n2. Verify the result.",
            "expected_result": "1. Setup completes.\n2. Result is verified.",
            "design_method": "功能測試 (Functional based ; no specific technique)",
            "priority": "Medium",
            "split_flag": False,
            "split_reason": "",
        }
        mock_generate_single_tc.return_value.input_tokens = 10
        mock_generate_single_tc.return_value.output_tokens = 20
        mock_generate_single_tc.return_value.cost = 0.001

        args = parse_args([
            "--input", sample_xlsx,
            "--output-dir", str(tmp_path / "out"),
            "--mode", "incremental",
        ])
        exit_code = run(args)
        assert exit_code == 0

    @patch("main.generate_batch")
    def test_budget_limit_blocks_batch_before_api_call(self, mock_generate_batch, sample_xlsx, tmp_path):
        args = parse_args([
            "--input", sample_xlsx,
            "--output-dir", str(tmp_path / "out"),
            "--budget", "0.0001",
            "--batch-size", "2",
        ])

        exit_code = run(args)

        assert exit_code == 1
        mock_generate_batch.assert_not_called()

    def test_unsupported_spec_format_fails_fast(self, sample_xlsx, tmp_path):
        spec_path = tmp_path / "unsupported.txt"
        spec_path.write_text("not supported")

        args = parse_args([
            "--input", sample_xlsx,
            "--spec", str(spec_path),
            "--dry-run",
        ])

        with pytest.raises(ValueError, match="Unsupported spec format"):
            run(args)

    @patch("main.generate_single_tc")
    def test_strict_validation_fails_invalid_rows(self, mock_generate_single_tc, sample_xlsx, tmp_path):
        mock_generate_single_tc.return_value.tc_data = {
            "test_item_rewrite": "(Condition → Outcome)",
            "pre_conditions": "1. Open settings menu",
            "input_test_data": "NA",
            "test_procedure": "1. Perform setup.\n2. Execute action without verification.",
            "expected_result": "1. Setup completes.\n2. Works as expected.",
            "design_method": "invalid method",
            "priority": "Critical",
            "split_flag": False,
            "split_reason": "",
        }
        mock_generate_single_tc.return_value.input_tokens = 10
        mock_generate_single_tc.return_value.output_tokens = 20
        mock_generate_single_tc.return_value.cost = 0.001

        args = parse_args([
            "--input", sample_xlsx,
            "--output-dir", str(tmp_path / "out"),
            "--mode", "incremental",
            "--batch-size", "1",
            "--strict-validation",
        ])

        exit_code = run(args)

        assert exit_code == 1
        output_path = tmp_path / "out" / "Test_SWQT_DeviceManager_20260408_generated.xlsx"
        assert not output_path.exists()

    @patch("main.generate_single_tc")
    def test_non_strict_validation_keeps_warning_behavior(self, mock_generate_single_tc, sample_xlsx, tmp_path):
        mock_generate_single_tc.return_value.tc_data = {
            "test_item_rewrite": "(Condition → Outcome)",
            "pre_conditions": "1. Open settings menu",
            "input_test_data": "NA",
            "test_procedure": "1. Perform setup.\n2. Execute action without verification.",
            "expected_result": "1. Setup completes.\n2. Works as expected.",
            "design_method": "invalid method",
            "priority": "Critical",
            "split_flag": False,
            "split_reason": "",
        }
        mock_generate_single_tc.return_value.input_tokens = 10
        mock_generate_single_tc.return_value.output_tokens = 20
        mock_generate_single_tc.return_value.cost = 0.001

        args = parse_args([
            "--input", sample_xlsx,
            "--output-dir", str(tmp_path / "out"),
            "--mode", "incremental",
            "--batch-size", "1",
        ])

        exit_code = run(args)

        assert exit_code == 0
        output_path = tmp_path / "out" / "Test_SWQT_DeviceManager_20260408_generated.xlsx"
        assert output_path.exists()
