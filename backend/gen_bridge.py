"""Generation bridge — single-requirement deep-decompose + TC fan-out, runnable
on the Claude subscription ($0) via the same export/assemble pattern as review.

Per requirement, Python assembles a SPEC-grounded context bundle (requirement +
domain pack + the SPEC PC rules linked to it + applicable L2 gaps). Claude does
the deep decomposition and generates one TC per scenario in-session; Python
assembles the TCs into a structured workbook-ready list.

Key intent (the project north star): decomposition is grounded in the SPEC
ORIGINAL, not only the derived requirement — so generated TCs cover behaviours
the requirement never decomposed (e.g. PC4's Repeat Off state).
"""
from __future__ import annotations

import json
from pathlib import Path

GEN_BUNDLE_SCHEMA = "gen-bundle/v1"

# Fields every generated TC must carry (the prompt_builder output contract).
TC_FIELDS = [
    "tc_title", "pre_conditions", "input_test_data", "test_procedure",
    "expected_result", "design_method", "priority", "test_item",
    "split_flag", "split_reason",
]

# The team's controlled Design Method vocabulary (docs/Test Case Design Method
# 判斷規則.md). design_method MUST be one of these exact bilingual labels —
# never a free-form technique name.
DESIGN_METHODS = [
    "功能測試 (Functional based ; no specific technique)",
    "狀態轉換 (State Transition Testing)",
    "決策表 (Decision Table Testing)",
    "等價劃分 (Equivalence Partitioning, EP)",
    "邊界值分析 (Boundary Value Analysis, BVA)",
    "組合測試 (Combinatorial Testing)",
    "情境 / 用例 (Scenario / Use Case Testing)",
    "負向測試 (Negative / Invalid)",
    "基礎故障注入 (Fault Injection Lite)",
]
# Quick-selection flow (判斷規則 §12) — first match wins.
_DESIGN_METHOD_FLOW = (
    "Design Method 必須從下列控制清單擇一(完整字串照貼),依序判斷:\n"
    "1. 錯誤輸入/不合法操作 → 負向測試 (Negative / Invalid)\n"
    "2. 模擬系統或環境故障(連線中斷/設備移除)→ 基礎故障注入 (Fault Injection Lite)\n"
    "3. 涉及系統狀態改變(模式/狀態切換、狀態相依 UI)→ 狀態轉換 (State Transition Testing)\n"
    "4. 多條件判斷邏輯 → 決策表 (Decision Table Testing)\n"
    "5. 測試輸入區間 → 等價劃分 (Equivalence Partitioning, EP)\n"
    "6. 測試邊界值 → 邊界值分析 (Boundary Value Analysis, BVA)\n"
    "7. 多參數組合 → 組合測試 (Combinatorial Testing)\n"
    "8. 驗證完整操作流程 → 情境 / 用例 (Scenario / Use Case Testing)\n"
    "9. 以上皆非 → 功能測試 (Functional based ; no specific technique)"
)


def _spec_pc_for_req(req_id: str, spec_rows: list[dict]) -> list[dict]:
    """SPEC PC rules linked to a requirement: explicitly cited OR best content
    match. These ground the decomposition in the SPEC original."""
    out = []
    for r in spec_rows:
        if req_id in (r.get("cited_by") or []) or r.get("best_req") == req_id:
            out.append({"pc": r["pc"], "text": r["text"],
                        "covered": r.get("req_covered", False)})
    return out


def _context_prompt(req: dict, domain_block: str | None,
                    spec_pc: list[dict]) -> str:
    """The per-requirement deep-decompose + generate instruction Claude answers."""
    parts = [
        "## 任務:單需求深拆 + 測試案例生成(ASPICE SWE.6)",
        "",
        "依序做兩件事,回 JSON:",
        "1. **深拆**:把需求拆成數個獨立 scenario,每個只有一個驗證點"
        "(partial-failure stress test:若兩種部分失敗會因不同原因 fail,代表還要再拆)。",
        "2. **生成**:每個 scenario 產一條完整 TC(欄位見下方 schema)。",
        "",
        "### 接地原則(重要)",
        "- Domain Pack 是 GROUND TRUTH:覆蓋其列舉的每個值/分支,但不得發明未定義狀態。",
        "- **拆解要看 SPEC 原文(下方 PC 規則),不只看需求**。SPEC 有、但需求沒寫的行為,"
        "也要拆出 scenario 並生成 TC(例如 Repeat Off 態)。標出哪些 scenario 來自 SPEC-only 行為。",
        "- 不要發明需求/SPEC 沒有的具體數值;有歧義就明確保留。",
        "",
        "### Design Method(必須用控制詞彙)",
        _DESIGN_METHOD_FLOW,
    ]
    if domain_block:
        parts += ["", "### Domain Pack(GROUND TRUTH)", domain_block]
    if spec_pc:
        parts += ["", "### SPEC 原文 PC 規則(此需求關聯;★ = 尚未被需求涵蓋,優先補)"]
        for p in spec_pc:
            star = "" if p["covered"] else " ★SPEC-only"
            parts.append(f"- [{p['pc']}]{star} {p['text']}")
    parts += [
        "", "### 需求",
        f"{req.get('id')}: {req.get('title','')}",
        (req.get("desc") or "").strip(),
        "",
        "### 輸出 JSON 結構",
        json.dumps({
            "decomposition": {
                "reasoning": "<繁中:如何拆、為何這樣拆>",
                "scenarios": [{"id": 1, "name": "<繁中>",
                               "verification_question": "<繁中 yes/no>",
                               "source": "requirement | spec-only",
                               "spec_ref": "<PCx.y 或 需求 id>"}],
            },
            "test_cases": [{
                "scenario_id": 1,
                "tc_title": "<source language, ≤14 words>",
                "test_item": "<需求/SPEC 規範句, source language>",
                "pre_conditions": "1. ...",
                "input_test_data": "1. ... 或 NA",
                "test_procedure": "1. ...\n2. ...(最後一步須 Check/Verify 可觀察結果)",
                "expected_result": "1. ...(具體可觀察,勿用『正常/如預期』)",
                "design_method": "<等價分割/邊界值/列舉/場景…>",
                "priority": "P1|P2|P3",
                "split_flag": False, "split_reason": "",
            }],
        }, ensure_ascii=False, indent=2),
    ]
    return "\n".join(parts)


def export_generation_bundle(
    swe1_reqs_path: str,
    domain_pack_path: str | None = None,
    spec_coverage_path: str | None = None,
    req_ids: list[str] | None = None,
) -> dict:
    """Build a SPEC-grounded generation bundle (zero API). Claude fills each
    `requirements[i]['answer']` with {decomposition, test_cases}."""
    from req_tracer import load_swe1_reqs
    reqs = load_swe1_reqs(swe1_reqs_path)
    if req_ids:
        wanted = set(req_ids)
        reqs = [r for r in reqs if r.get("id") in wanted]

    domain_block = None
    if domain_pack_path:
        from domain_pack import load_domain_pack, to_prompt_block
        domain_block = to_prompt_block(load_domain_pack(domain_pack_path))

    spec_rows = []
    if spec_coverage_path and Path(spec_coverage_path).is_file():
        spec_rows = json.loads(Path(spec_coverage_path).read_text(encoding="utf-8"))

    requirements = []
    for r in reqs:
        rid = r.get("id")
        spec_pc = _spec_pc_for_req(rid, spec_rows)
        requirements.append({
            "req_id": rid,
            "title": r.get("title", ""),
            "spec_pc_count": len(spec_pc),
            "spec_only_count": sum(1 for p in spec_pc if not p["covered"]),
            "context_prompt": _context_prompt(r, domain_block, spec_pc),
            "answer": None,
        })

    return {
        "schema": GEN_BUNDLE_SCHEMA,
        "swe1_reqs_path": str(swe1_reqs_path),
        "domain_pack_path": domain_pack_path,
        "system_prompt": (
            "你是 ASPICE SWE.6 測試分析師。深拆需求並生成測試案例。"
            "只回合法 JSON,不要 markdown fences。所有說明欄位用繁體中文,"
            "test_item / tc_title 保留來源語言。"
        ),
        "requirements": requirements,
    }


def assemble_generation(bundle: dict) -> dict:
    """Flatten Claude's per-requirement answers into a TC list with assigned IDs.

    Returns {test_cases:[...], stats:{...}}; each TC carries its req_id, scenario
    source (requirement vs spec-only) and a sequential tc_id."""
    if bundle.get("schema") != GEN_BUNDLE_SCHEMA:
        raise ValueError(f"unexpected gen-bundle schema: {bundle.get('schema')}")

    valid_methods = set(DESIGN_METHODS)
    tcs: list[dict] = []
    n_reqs_answered = 0
    n_spec_only = 0
    n_bad_method = 0
    seq = 1
    for req in bundle["requirements"]:
        ans = req.get("answer")
        if not ans:
            continue
        n_reqs_answered += 1
        scen_source = {s.get("id"): s.get("source")
                       for s in (ans.get("decomposition", {}) or {}).get("scenarios", [])}
        for tc in ans.get("test_cases", []) or []:
            src = scen_source.get(tc.get("scenario_id"), "requirement")
            if src == "spec-only":
                n_spec_only += 1
            row = {k: tc.get(k, "") for k in TC_FIELDS}
            method_ok = row.get("design_method") in valid_methods
            if not method_ok:
                n_bad_method += 1
            row.update({
                "tc_id": f"GEN-{seq:04d}",
                "req_id": req["req_id"],
                "scenario_id": tc.get("scenario_id"),
                "source": src,
                "design_method_valid": method_ok,  # off the controlled vocabulary?
            })
            tcs.append(row)
            seq += 1

    return {
        "test_cases": tcs,
        "stats": {
            "requirements_total": len(bundle["requirements"]),
            "requirements_answered": n_reqs_answered,
            "tcs_generated": len(tcs),
            "tcs_from_spec_only": n_spec_only,  # behaviours the requirement never decomposed
            "tcs_invalid_design_method": n_bad_method,  # off the controlled vocabulary
        },
    }
