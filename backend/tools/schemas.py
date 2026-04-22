"""Tool JSON schemas（OpenAI function calling 格式）。

這份檔案是 Agent dispatcher 在組 `tools=[...]` 參數時的唯一資料來源。
每個 schema 只暴露「Agent 可傳的參數」；像 `job_store` 這種 caller-injected
依賴由 dispatcher 注入，不列在 schema 裡。
"""

from __future__ import annotations

from typing import Any

# ---------------------------------------------------------------------------
# Shared sub-schemas
# ---------------------------------------------------------------------------

_ROW_BASIC: dict[str, Any] = {
    "type": "object",
    "description": "Minimal per-row shape used by read-only tools.",
    "properties": {
        "id": {"type": "string"},
        "reqId": {"type": "string"},
        "testItem": {"type": "string"},
        "testSet": {"type": ["string", "null"]},
    },
    "required": ["id", "reqId"],
}

_ROW_FOR_MATCH: dict[str, Any] = {
    "type": "object",
    "description": "Row shape accepted by match_spec (snake_case).",
    "properties": {
        "id": {"type": "string"},
        "req_id": {"type": "string"},
        "test_item": {"type": "string"},
    },
    "required": ["id", "req_id"],
}

_ROW_FOR_GENERATE: dict[str, Any] = {
    "type": "object",
    "description": "Row shape accepted by generate_tc (snake_case).",
    "properties": {
        "id": {"type": "string"},
        "row_num": {"type": "integer"},
        "tc_id": {"type": "string"},
        "req_id": {"type": "string"},
        "test_item": {"type": "string"},
        "original_requirement": {"type": "string"},
        "test_set": {"type": ["string", "null"]},
        "spec_reference": {"type": ["string", "null"]},
        "priority": {"type": ["string", "null"]},
    },
    "required": ["id", "req_id", "test_item"],
}

_TC_SHAPE: dict[str, Any] = {
    "type": "object",
    "description": "Generated TC dict for validator.",
    "properties": {
        "tc_id": {"type": "string"},
        "test_item": {"type": "string"},
        "pre_conditions": {"type": "string"},
        "test_procedure": {"type": "string"},
        "expected_result": {"type": "string"},
        "design_method": {"type": "string"},
        "priority": {"type": "string"},
    },
    "required": [
        "tc_id",
        "test_item",
        "pre_conditions",
        "test_procedure",
        "expected_result",
        "design_method",
        "priority",
    ],
}


# ---------------------------------------------------------------------------
# Per-tool schemas
# ---------------------------------------------------------------------------

PARSE_WORKBOOK_SCHEMA: dict[str, Any] = {
    "name": "parse_workbook",
    "description": (
        "Parse an ASPICE SWE.6 TC workbook (.xlsx / .xlsm) into structured rows "
        "and register a job. Returns jobId for downstream tools. The dispatcher "
        "injects job_store; the agent only supplies paths."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "raw_path": {
                "type": "string",
                "description": "Absolute path to the uploaded TC workbook.",
            },
            "raw_filename": {
                "type": "string",
                "description": "Original filename (used for downstream export).",
            },
            "reference_path": {
                "type": ["string", "null"],
                "description": "Optional SYS1 reference .xlsx absolute path.",
            },
            "reference_filename": {"type": ["string", "null"]},
            "spec_path": {
                "type": ["string", "null"],
                "description": "Optional supplementary doc (.pdf/.docx/.xlsx).",
            },
            "spec_filename": {"type": ["string", "null"]},
        },
        "required": ["raw_path", "raw_filename"],
    },
}


GROUP_TESTS_SCHEMA: dict[str, Any] = {
    "name": "group_tests",
    "description": (
        "Derive Test Set assignments from rows using existing value, PDM code, "
        "or REQ ID prefix fallback. Returns groups, framework map, and "
        "per-row assignments."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "rows": {
                "type": "array",
                "items": _ROW_BASIC,
                "description": "Rows to group (camelCase or snake_case both accepted).",
            },
        },
        "required": ["rows"],
    },
}


MATCH_SPEC_SCHEMA: dict[str, Any] = {
    "name": "match_spec",
    "description": (
        "Match each Test Item against a SYS1 reference workbook using PDM exact "
        "match (Layer 1) + token Jaccard fallback (Layer 1.5). Without a "
        "reference_workbook_path every row is returned as unmatched."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "rows": {
                "type": "array",
                "items": _ROW_FOR_MATCH,
            },
            "reference_workbook_path": {
                "type": ["string", "null"],
                "description": "Absolute path to the SYS1 reference .xlsx.",
            },
        },
        "required": ["rows"],
    },
}


VALIDATE_TC_SCHEMA: dict[str, Any] = {
    "name": "validate_tc",
    "description": (
        "Run programmatic ASPICE SWE.6 validation on a single generated TC. "
        "Returns per-check issues and a hasWarnings flag."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "tc": _TC_SHAPE,
        },
        "required": ["tc"],
    },
}


WRITE_EXCEL_SCHEMA: dict[str, Any] = {
    "name": "write_excel",
    "description": (
        "Write generated TC rows back to an .xlsx file using the original "
        "workbook as template. Optionally populates the Test Case Framework "
        "sheet. DESTRUCTIVE — may overwrite output_path."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "source_path": {"type": "string"},
            "output_path": {"type": "string"},
            "rows": {
                "type": "array",
                "items": {"type": "object"},
                "description": "Export rows; fields match writer.write_generated_results.",
            },
            "selected_fields": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Whitelist of generated fields; null = write all.",
            },
            "framework_rows": {
                "type": ["array", "null"],
                "items": {
                    "type": "object",
                    "properties": {
                        "test_group": {"type": "string"},
                        "test_set": {"type": "string"},
                        "req_count": {"type": "integer"},
                    },
                },
                "description": "Optional framework sheet rows; null = skip.",
            },
        },
        "required": ["source_path", "output_path", "rows"],
    },
}


GENERATE_TC_SCHEMA: dict[str, Any] = {
    "name": "generate_tc",
    "description": (
        "Generate test cases for one batch (1-N rows) via a single OpenAI call. "
        "Returns tc_data plus token/cost accounting. WRITE_COSTLY — each call "
        "consumes LLM tokens; caller is expected to budget gate."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "rows": {
                "type": "array",
                "items": _ROW_FOR_GENERATE,
                "minItems": 1,
            },
            "context": {
                "type": "object",
                "properties": {
                    "project": {"type": "string"},
                    "test_group": {"type": "string"},
                    "test_set": {"type": "string"},
                },
                "required": ["project", "test_group"],
            },
            "spec_index": {
                "type": ["object", "null"],
                "description": "Optional PDM code → spec entry map.",
            },
            "rules_text": {
                "type": "string",
                "description": "ASPICE SWE.6 rules markdown to embed in system prompt.",
            },
            "model": {
                "type": "string",
                "description": "OpenAI model id, e.g. gpt-5.4-mini, gpt-5.4, gpt-5.4-nano.",
            },
        },
        "required": ["rows", "context", "rules_text"],
    },
}


INSPECT_WORKBOOK_SCHEMA: dict[str, Any] = {
    "name": "inspect_workbook",
    "description": (
        "Lightweight preview of a TC workbook: lists sheets, derives test group "
        "from filename, and estimates row count without registering a job. Use "
        "this before parse_workbook when the user asks about file size / scope."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "path": {"type": "string", "description": "Absolute path to the .xlsx"},
        },
        "required": ["path"],
    },
}


LIST_JOBS_SCHEMA: dict[str, Any] = {
    "name": "list_jobs",
    "description": (
        "List recent jobs from the registry. Optional status_filter "
        "(parsed / queued / running / completed). Returns jobId, fileName, "
        "status, rowCount, testGroup, project."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "status_filter": {
                "type": ["string", "null"],
                "description": "Return only jobs in this status.",
            },
            "limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 20},
        },
        "required": [],
    },
}


ESTIMATE_COST_SCHEMA: dict[str, Any] = {
    "name": "estimate_cost",
    "description": (
        "Estimate the USD cost of generating all rows in a job. Uses average "
        "input/output token heuristics; actual spend may vary with prompt "
        "caching. Returns rowCount and estCostUsd."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "job_id": {"type": "string"},
            "model": {
                "type": "string",
                "description": "OpenAI model id, e.g. gpt-5.4-mini, gpt-5.4, gpt-5.4-nano.",
            },
            "batch_size": {"type": "integer", "minimum": 1, "default": 5},
        },
        "required": ["job_id"],
    },
}


GET_JOB_DETAIL_SCHEMA: dict[str, Any] = {
    "name": "get_job_detail",
    "description": (
        "Fetch a summary of one registered job without exposing raw binary "
        "content. Returns core fields (jobId, fileName, status, rowCount, "
        "project, testGroup, timestamps) and optional match/group/generated "
        "summaries when those phases have run. Use this when the user asks "
        "about a specific job beyond what list_jobs returns."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "job_id": {"type": "string", "description": "Target job id."},
        },
        "required": ["job_id"],
    },
}


DIFF_JOBS_SCHEMA: dict[str, Any] = {
    "name": "diff_jobs",
    "description": (
        "Compare two jobs side-by-side. Returns each job's summary (same shape "
        "as get_job_detail) plus a `diff` block with deltas for rowCount, "
        "costUsd, matched / unmatched counts, and a statusChanged flag. Use "
        "when the user asks how one run differs from another."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "job_a_id": {"type": "string", "description": "Baseline job id."},
            "job_b_id": {"type": "string", "description": "Comparison job id."},
        },
        "required": ["job_a_id", "job_b_id"],
    },
}


AGGREGATE_METRICS_SCHEMA: dict[str, Any] = {
    "name": "aggregate_metrics",
    "description": (
        "Aggregate counters across many jobs: total / average rowCount and "
        "costUsd, overall spec match rate (matched rows / total match-phase "
        "rows). Pass job_ids to scope; omit to cover every job in the store. "
        "Use when the user asks about trends, totals, or \"how much have I "
        "spent this month\"."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "job_ids": {
                "type": ["array", "null"],
                "items": {"type": "string"},
                "description": "Explicit subset; null/empty = all jobs in store.",
            },
        },
        "required": [],
    },
}


GET_JOB_VALIDATION_SCHEMA: dict[str, Any] = {
    "name": "get_job_validation",
    "description": (
        "Run programmatic validation across an array of generated rows and "
        "aggregate counts. Each row must carry a `generated` sub-object "
        "(testItemRewrite/preConditions/testProcedure/expectedResult/...). "
        "Rows without generated content are marked skipped."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "rows": {
                "type": "array",
                "items": {"type": "object"},
            },
        },
        "required": ["rows"],
    },
}


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

ALL_SCHEMAS: dict[str, dict[str, Any]] = {
    "parse_workbook": PARSE_WORKBOOK_SCHEMA,
    "group_tests": GROUP_TESTS_SCHEMA,
    "match_spec": MATCH_SPEC_SCHEMA,
    "validate_tc": VALIDATE_TC_SCHEMA,
    "write_excel": WRITE_EXCEL_SCHEMA,
    "generate_tc": GENERATE_TC_SCHEMA,
    "inspect_workbook": INSPECT_WORKBOOK_SCHEMA,
    "list_jobs": LIST_JOBS_SCHEMA,
    "estimate_cost": ESTIMATE_COST_SCHEMA,
    "get_job_detail": GET_JOB_DETAIL_SCHEMA,
    "diff_jobs": DIFF_JOBS_SCHEMA,
    "aggregate_metrics": AGGREGATE_METRICS_SCHEMA,
    "get_job_validation": GET_JOB_VALIDATION_SCHEMA,
}


def openai_tool_definitions() -> list[dict[str, Any]]:
    """回傳 OpenAI Chat Completions `tools=` 參數用的列表。"""
    return [
        {"type": "function", "function": schema}
        for schema in ALL_SCHEMAS.values()
    ]


def get_schema(name: str) -> dict[str, Any]:
    """取得單一 tool 的 schema，找不到就丟 KeyError。"""
    if name not in ALL_SCHEMAS:
        raise KeyError(f"no schema for tool: {name}")
    return ALL_SCHEMAS[name]
