"""Tests for Test Set grouper module (RULES.md §2.3)."""
import json
import pytest

from grouper import (
    load_framework,
    save_framework,
    assign_test_sets,
    build_framework_sheet_data,
    build_grouping_prompt,
    parse_grouping_response,
)


@pytest.fixture
def sample_framework():
    return {
        "Access & Entry": ["SWE1-HMI-DM-001-*", "SWE1-HMI-DM-002-*"],
        "Device List & Recognition": ["SWE1-HMI-DM-003-*", "SWE1-HMI-DM-004-*"],
        "Function Connection": ["SWE1-HMI-DM-005-*"],
    }


@pytest.fixture
def framework_json(tmp_path, sample_framework):
    filepath = tmp_path / "DeviceManager_framework.json"
    filepath.write_text(json.dumps(sample_framework, indent=2))
    return str(filepath)


@pytest.fixture
def sample_rows():
    return [
        {"req_id": "SWE1-HMI-DM-001-01", "test_item": "PDM01 access Device Manager"},
        {"req_id": "SWE1-HMI-DM-001-02", "test_item": "PDM01.1 add to status bar"},
        {"req_id": "SWE1-HMI-DM-003-01", "test_item": "PDM03 device list display"},
        {"req_id": "SWE1-HMI-DM-005-01", "test_item": "PDM05 connect function"},
        {"req_id": "SWE1-HMI-DM-999-01", "test_item": "PDM99 unknown feature"},
    ]


class TestLoadSaveFramework:
    def test_load(self, framework_json, sample_framework):
        result = load_framework(framework_json)
        assert result == sample_framework

    def test_save_and_load(self, tmp_path):
        filepath = str(tmp_path / "test_fw.json")
        data = {"Group A": ["R001", "R002"]}
        save_framework(data, filepath)
        assert load_framework(filepath) == data

    def test_load_not_found(self):
        assert load_framework("/nonexistent/file.json") is None


class TestAssignTestSets:
    def test_exact_match(self, sample_framework, sample_rows):
        results = assign_test_sets(sample_rows, sample_framework)
        assert results[0]["test_set"] == "Access & Entry"
        assert results[1]["test_set"] == "Access & Entry"
        assert results[2]["test_set"] == "Device List & Recognition"
        assert results[3]["test_set"] == "Function Connection"

    def test_unmatched_gets_none(self, sample_framework, sample_rows):
        results = assign_test_sets(sample_rows, sample_framework)
        assert results[4]["test_set"] is None

    def test_preserves_original_data(self, sample_framework, sample_rows):
        results = assign_test_sets(sample_rows, sample_framework)
        assert results[0]["req_id"] == "SWE1-HMI-DM-001-01"
        assert results[0]["test_item"] == "PDM01 access Device Manager"


class TestBuildFrameworkSheetData:
    def test_structure(self, sample_framework):
        data = build_framework_sheet_data("DeviceManager", sample_framework)
        assert len(data) == 3
        assert data[0] == {
            "test_group": "DeviceManager",
            "test_set": "Access & Entry",
            "req_count": 2,
        }

    def test_order_preserved(self, sample_framework):
        data = build_framework_sheet_data("DM", sample_framework)
        sets = [d["test_set"] for d in data]
        assert sets == ["Access & Entry", "Device List & Recognition", "Function Connection"]


class TestBuildGroupingPrompt:
    def test_contains_test_items(self, sample_rows):
        prompt = build_grouping_prompt(sample_rows)
        assert "PDM01 access Device Manager" in prompt
        assert "PDM05 connect function" in prompt

    def test_contains_instructions(self, sample_rows):
        prompt = build_grouping_prompt(sample_rows)
        assert "JSON" in prompt
        assert "Test Set" in prompt or "sub-feature" in prompt


class TestParseGroupingResponse:
    def test_valid_json(self):
        raw = '{"Access & Entry": ["SWE1-HMI-DM-001-*"], "Connection": ["SWE1-HMI-DM-005-*"]}'
        result = parse_grouping_response(raw)
        assert "Access & Entry" in result
        assert result["Connection"] == ["SWE1-HMI-DM-005-*"]

    def test_json_in_markdown_fence(self):
        raw = '```json\n{"Group A": ["R001"]}\n```'
        result = parse_grouping_response(raw)
        assert result == {"Group A": ["R001"]}

    def test_invalid_json(self):
        with pytest.raises(ValueError):
            parse_grouping_response("not json at all")
