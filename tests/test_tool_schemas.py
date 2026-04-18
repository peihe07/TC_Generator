"""Tool JSON schema 結構測試。

不依賴 jsonschema 套件；直接斷言 OpenAI function-calling 必備欄位齊全。
"""

from __future__ import annotations

import pytest

from backend.tools import (
    ALL_SCHEMAS,
    get_schema,
    list_tools,
    openai_tool_definitions,
)


EXPECTED_TOOL_NAMES = {
    "parse_workbook",
    "group_tests",
    "match_spec",
    "validate_tc",
    "write_excel",
    "generate_tc",
    "inspect_workbook",
    "list_jobs",
    "estimate_cost",
    "get_job_validation",
}


def test_all_expected_tools_have_schemas():
    assert set(ALL_SCHEMAS.keys()) == EXPECTED_TOOL_NAMES


def test_every_registered_tool_has_schema_attached():
    """`ToolSpec.input_schema` 在 register 時應已附帶 schema。"""
    for spec in list_tools():
        assert spec.input_schema, f"tool {spec.name} missing input_schema"
        assert spec.input_schema["name"] == spec.name


@pytest.mark.parametrize("name", sorted(EXPECTED_TOOL_NAMES))
def test_schema_shape(name):
    schema = get_schema(name)
    assert schema["name"] == name
    assert isinstance(schema["description"], str) and schema["description"]

    params = schema["parameters"]
    assert params["type"] == "object"
    assert "properties" in params
    assert isinstance(params["properties"], dict)
    assert "required" in params
    assert isinstance(params["required"], list)

    # required keys 必須存在於 properties
    for key in params["required"]:
        assert key in params["properties"], f"{name}: required '{key}' not in properties"


def test_parse_workbook_requires_paths():
    schema = get_schema("parse_workbook")
    assert set(schema["parameters"]["required"]) == {"raw_path", "raw_filename"}


def test_generate_tc_has_rules_text_required():
    schema = get_schema("generate_tc")
    assert "rules_text" in schema["parameters"]["required"]
    assert "rows" in schema["parameters"]["required"]


def test_openai_tool_definitions_shape():
    defs = openai_tool_definitions()
    assert len(defs) == len(EXPECTED_TOOL_NAMES)
    for tool_def in defs:
        assert tool_def["type"] == "function"
        assert "function" in tool_def
        assert tool_def["function"]["name"] in EXPECTED_TOOL_NAMES


def test_get_schema_unknown_raises():
    with pytest.raises(KeyError):
        get_schema("nope_tool")


def test_schema_descriptions_long_enough_for_llm():
    """description 太短 LLM 無從判斷何時該呼叫；下限設 40 字。"""
    for schema in ALL_SCHEMAS.values():
        assert len(schema["description"]) >= 40, (
            f"{schema['name']} description too short: {schema['description']!r}"
        )
