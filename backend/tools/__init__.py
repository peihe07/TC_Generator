"""Tool layer for TC Generator.

每個 tool 是一個 pure function，同時被 FastAPI route 和未來的 Agent
dispatcher 呼叫，確保業務邏輯只有一份。
"""

from .errors import ToolError
from .registry import (
    SafetyLevel,
    ToolSpec,
    get_tool,
    list_tools,
    register_tool,
)
from .parse import parse_workbook_tool
from .group import group_tests_tool
from .match import match_spec_tool
from .validate import validate_tc_tool
from .write import write_excel_tool
from .generate import estimate_batch_cost, generate_tc_tool
from .inspect import inspect_workbook_tool
from .jobs import estimate_cost_tool, get_job_validation_tool, list_jobs_tool
from .schemas import ALL_SCHEMAS, get_schema, openai_tool_definitions

__all__ = [
    "ToolError",
    "SafetyLevel",
    "ToolSpec",
    "get_tool",
    "list_tools",
    "register_tool",
    "parse_workbook_tool",
    "group_tests_tool",
    "match_spec_tool",
    "validate_tc_tool",
    "write_excel_tool",
    "generate_tc_tool",
    "estimate_batch_cost",
    "inspect_workbook_tool",
    "list_jobs_tool",
    "estimate_cost_tool",
    "get_job_validation_tool",
    "ALL_SCHEMAS",
    "get_schema",
    "openai_tool_definitions",
]
