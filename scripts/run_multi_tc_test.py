"""Standalone multi-TC test runner — 跑 N 筆 req 驗證新的 auto-split 路徑。

用途：在全量 job 之前先用少量 rows（--limit）確認 prompt / parser / writer 的
多筆拆分流程在真實 AI 下表現正常。

Usage:
    .venv/bin/python scripts/run_multi_tc_test.py \
        --input "docs/test/....xlsx" \
        --limit 3 \
        --output-dir output

Output:
    {output_dir}/{basename}_generated.xlsx
    stdout 會印出每個 req 拆成幾筆、reasoning、keywords。
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# 把 backend/ 加入 sys.path，讓我們能從 project root 直接跑。
_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(_ROOT / "backend"))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(_ROOT / ".env")

from parser import parse_tc_xlsx  # noqa: E402
from generator import generate_tcs_for_row, GenerationError  # noqa: E402
from writer import write_generated_results, build_output_path  # noqa: E402
from api_server import RULES_SECTIONS  # noqa: E402 — 重用同一份 ASPICE 規則


def _short(text: str, n: int = 80) -> str:
    text = (text or "").replace("\n", " | ")
    return text if len(text) <= n else text[: n - 1] + "…"


def main() -> int:
    p = argparse.ArgumentParser(description="Multi-TC smoke test runner")
    p.add_argument("--input", required=True)
    p.add_argument("--limit", type=int, default=3, help="Number of req rows to process")
    p.add_argument("--offset", type=int, default=0, help="Skip first N rows")
    p.add_argument("--model", default="gpt-4.1")
    p.add_argument("--output-dir", default="output")
    args = p.parse_args()

    parsed = parse_tc_xlsx(args.input)
    all_rows = parsed["rows"]
    total = len(all_rows)
    start = args.offset
    end = min(start + args.limit, total)
    rows = all_rows[start:end]

    print(f"Parsed {total} rows total — running {len(rows)} ({start}..{end - 1})")
    print(f"Project: {parsed['project']}  Test Group: {parsed['test_group']}\n")

    context = {
        "project": parsed["project"] or "UnknownProject",
        "test_group": parsed["test_group"] or "UnknownGroup",
        "test_set": "N/A",
    }

    generated_export_rows: list[dict] = []
    total_cost = 0.0
    total_tc_count = 0

    for i, row in enumerate(rows, start=1):
        print(
            f"[{i}/{len(rows)}] row_num={row['row_num']} req={row.get('req_id')}  "
            f"test_item={_short(row.get('test_item', ''))}"
        )
        try:
            result = generate_tcs_for_row(
                row=row, context=context, spec_index=None,
                rules_text=RULES_SECTIONS, model=args.model,
            )
        except GenerationError as exc:
            print(f"    ✗ GenerationError: {exc}")
            continue

        tcs = result.tc_data if isinstance(result.tc_data, list) else [result.tc_data]
        meta = result.split_meta[0] if result.split_meta else {}
        total_cost += result.cost
        total_tc_count += len(tcs)

        print(f"    ✓ AI 回 {len(tcs)} 筆 TC   cost=${result.cost:.4f}")
        if meta.get("reasoning"):
            print(f"    reasoning: {_short(meta['reasoning'], 120)}")
        for k in (meta.get("keywords") or []):
            cb = k.get("covered_by") or k.get("scenarios") or []
            print(f"      [§1.3 keyword] {k.get('keyword')}: {_short(k.get('meaning', ''), 50)} → TC {cb}")

        # 準備寫入 Excel 的 row 資料
        for tc in tcs:
            generated_export_rows.append({
                "row_num": row["row_num"],
                "req_id": row.get("req_id", ""),
                "tc_id": row.get("tc_id", ""),  # 可能為空；writer 不強制
                "test_group": context["test_group"],
                "test_item_rewrite": tc.get("test_item_rewrite", ""),
                "pre_conditions": tc.get("pre_conditions", ""),
                "input_test_data": tc.get("input_test_data", ""),
                "test_procedure": tc.get("test_procedure", ""),
                "expected_result": tc.get("expected_result", ""),
                "priority": tc.get("priority", ""),
                "design_method": tc.get("design_method", ""),
            })
        print()

    os.makedirs(args.output_dir, exist_ok=True)
    output_path = build_output_path(args.input, output_dir=args.output_dir)
    write_generated_results(args.input, generated_export_rows, output_path)

    print("=" * 60)
    print(f"Done. {len(rows)} req → {total_tc_count} TCs")
    print(f"Total cost: ${total_cost:.4f}")
    print(f"Output: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
