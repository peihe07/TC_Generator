"""CLI entry point for TC Auto-Generation Tool (RULES.md §11)."""
import argparse
import json
import os
import sys
import time

from dotenv import load_dotenv

load_dotenv()

from parser import parse_tc_xlsx
from id_generator import generate_group_abbreviation, generate_tc_ids
from spec_matcher import build_spec_index, match_spec_references
from spec_parser import detect_format, parse_pdf, parse_docx, parse_xlsx, merge_indexes
from grouper import load_framework, save_framework, assign_test_sets, build_framework_sheet_data, build_grouping_prompt, parse_grouping_response
from prompt_builder import build_user_prompt, build_batch_prompt, REQUIRED_OUTPUT_KEYS
from generator import DEFAULT_MODEL, generate_single_tc, generate_batch, calculate_cost, GenerationError
from validator import validate_row
from writer import write_generated_results, write_framework_sheet, build_output_path
from rules_loader import load_rules


RULES_SECTIONS = load_rules()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="TC Auto-Generation Tool — ASPICE SWE.6",
    )
    p.add_argument("--input", help="TC Specification xlsx path (required except for --scorecard)")
    p.add_argument("--sys1", help="SYS1 Spec xlsx path (optional)")
    p.add_argument("--spec", help="Supplementary spec document path (optional)")
    p.add_argument("--framework", help="Path to confirmed framework.json (optional)")
    p.add_argument("--output-dir", default="output", help="Output directory (default: output/)")
    p.add_argument("--model", default=DEFAULT_MODEL, help=f"Model to use for generation/decomposition tasks (default: {DEFAULT_MODEL})")
    p.add_argument("--batch-size", type=int, default=5, help="TCs per API call (default: 5)")
    p.add_argument("--mode", choices=["full", "incremental", "regenerate"], default="full",
                   help="Generation mode (default: full)")
    p.add_argument("--rows", help="Comma-separated row numbers or req IDs for regenerate mode")
    p.add_argument("--dry-run", action="store_true", help="Show estimated cost without calling API")
    p.add_argument("--budget", type=float, default=5.0, help="Max budget in USD (default: 5.0)")
    p.add_argument(
        "--strict-validation",
        action="store_true",
        help="Treat validation warnings as failures and skip writing invalid rows",
    )
    p.add_argument(
        "--review",
        action="store_true",
        help="Audit existing TCs against ASPICE SWE.6 instead of generating new ones. "
             "Outputs findings.json + findings_report.md in --output-dir.",
    )
    p.add_argument(
        "--scorecard",
        action="store_true",
        help="Compute Stage 7 KPI scorecard from an existing findings.json "
             "(no AI). Use with --findings; writes scorecard.json + scorecard.md.",
    )
    p.add_argument(
        "--findings",
        help="Path to an existing findings.json for --scorecard "
             "(default: <output-dir>/findings.json).",
    )
    # Stage 2.5 — pre-flight budget checkpoint (no API, zero usage).
    p.add_argument(
        "--preflight",
        action="store_true",
        help="Estimate whether a batch fits the current 5h window (zero API). "
             "Use with --remaining-pct / --n-light / --n-deep.",
    )
    p.add_argument(
        "--calibrate",
        action="store_true",
        help="Record per-requirement window cost from a probe run (zero API). "
             "Use with --start-pct / --end-pct / --n-probe / --regime.",
    )
    p.add_argument("--remaining-pct", type=float,
                   help="Fraction 0..1 of the 5h window remaining (from /usage).")
    p.add_argument("--n-light", type=int, default=0, help="Light-regime requirement count.")
    p.add_argument("--n-deep", type=int, default=0, help="Deep-regime requirement count.")
    p.add_argument("--start-pct", type=float, help="Window % before the probe run.")
    p.add_argument("--end-pct", type=float, help="Window % after the probe run.")
    p.add_argument("--n-probe", type=int, help="Requirements processed in the probe run.")
    p.add_argument("--regime", choices=["light", "deep"], help="Calibration regime.")
    p.add_argument(
        "--domain-pack",
        help="Path to a Stage 1 domain_pack.json to ground the --review semantic "
             "rules (spec/domain truth + reality-gap detection).",
    )
    p.add_argument(
        "--swe1-reqs",
        help="Path to a SWE1 requirements JSON (id/title/desc). --review then "
             "anchors traceability by CONTENT match instead of the (possibly "
             "renumbered) req_id.",
    )
    p.add_argument(
        "--trace",
        action="store_true",
        help="Content-based traceability (zero API): match each TC to its SWE1 "
             "requirement by text. Use with --input and --swe1-reqs.",
    )
    return p.parse_args(argv)


# CLI flags that belong only to the generate path. When --review is passed,
# any of these (set to a non-default value) is rejected so the user does not
# silently mix modes.
_GENERATE_ONLY_DEFAULTS = {
    "sys1": None,
    "spec": None,
    "framework": None,
    "rows": None,
    "mode": "full",
    "batch_size": 5,
    "strict_validation": False,
}


def _reject_generate_flags(args: argparse.Namespace) -> str | None:
    """Return an error message if generate-only flags were used with --review."""
    bad = [
        flag for flag, default in _GENERATE_ONLY_DEFAULTS.items()
        if getattr(args, flag) != default
    ]
    if not bad:
        return None
    pretty = ", ".join(f"--{f.replace('_','-')}" for f in bad)
    return (
        f"--review does not accept generate-only flags: {pretty}. "
        "Run review separately or omit those flags."
    )


def run_review(args: argparse.Namespace) -> int:
    """Review-mode entry point. Mirrors `run` shape but routes through
    `review_engine.review_workbook`."""
    from review_engine import review_workbook  # local import to keep generate path lean

    print(f"\n{'='*60}")
    print("TC Review — ASPICE SWE.6")
    print(f"{'='*60}\n")
    print(f"Input: {args.input}")
    print(f"Output dir: {args.output_dir}")
    print(f"Model: {args.model}")
    print(f"Dry run: {args.dry_run}")

    os.makedirs(args.output_dir, exist_ok=True)
    report = review_workbook(
        workbook_path=args.input,
        output_dir=args.output_dir,
        model=args.model,
        dry_run=args.dry_run,
        domain_pack_path=args.domain_pack,
        swe1_reqs_path=args.swe1_reqs,
    )

    summary = report["batch_summary"]
    counts = summary["verdict_counts"]
    meta = report["batch_meta"]
    print(f"\n{'='*60}")
    print("Review Summary")
    print(f"  Source: {meta['source_file']}")
    print(f"  Total TCs: {meta['total_tcs']} across {meta['total_req_groups']} Req groups")
    print(f"  Pass: {counts['pass']}  Pass with issues: {counts['pass_with_issues']}  Fail: {counts['fail']}")
    print(f"  Tier 1 findings: {len(report['per_req_findings'])}")
    print(f"  Tier 2/3 TC entries: {len(report['per_tc_findings'])}")
    llm_stats = meta.get("llm_stats")
    if llm_stats:
        failed, total = llm_stats.get("llm_failed", 0), llm_stats.get("llm_batches", 0)
        if failed:
            print(f"  ⚠ LLM 語意層:{total} 批中 {failed} 批失敗(空/截斷回應)——"
                  f"這些批只剩 regex 結果。換 --model gpt-4.1 或檢查 model/額度。")
        else:
            print(f"  LLM 語意層:{total} 批全部成功")
    print(f"\n  Reasoning: {summary['reasoning']}")
    # Stage 7 — also emit a KPI scorecard from the findings we just produced.
    from scorecard import compute_scorecard, write_scorecard

    sc = compute_scorecard(report)
    write_scorecard(sc, args.output_dir)

    print(f"\n  Wrote: {args.output_dir}/findings.json")
    print(f"         {args.output_dir}/findings_report.md")
    print(f"         {args.output_dir}/scorecard.json")
    print(f"         {args.output_dir}/scorecard.md")
    print(f"  Gate: {'PASS' if sc.gate_passed else 'FAIL'}")
    print(f"{'='*60}\n")
    return 0


def run_scorecard(args: argparse.Namespace) -> int:
    """Standalone Stage 7 entry: recompute KPIs from an existing findings.json.

    No AI, zero cost. Used to take a baseline against existing review output.
    """
    from scorecard import compute_scorecard, write_scorecard

    findings_path = args.findings or os.path.join(args.output_dir, "findings.json")
    if not os.path.isfile(findings_path):
        print(f"Error: findings file not found: {findings_path}", file=sys.stderr)
        return 2

    with open(findings_path, encoding="utf-8") as fh:
        findings = json.load(fh)

    sc = compute_scorecard(findings)
    write_scorecard(sc, args.output_dir)

    print(f"\n{'='*60}")
    print("KPI Scorecard")
    print(f"  Source: {findings_path}")
    print(f"  Total TCs: {sc.total_tcs} across {sc.total_requirements} Req groups")
    print(f"  Gate: {'PASS' if sc.gate_passed else 'FAIL'}")
    print(f"  Wrote: {args.output_dir}/scorecard.json")
    print(f"         {args.output_dir}/scorecard.md")
    print(f"{'='*60}\n")
    return 0


def _filter_rows(rows: list[dict], mode: str, target_rows: str | None) -> list[dict]:
    """Filter rows based on generation mode."""
    if mode == "full":
        return rows

    if mode == "incremental":
        return [r for r in rows if not r.get("tc_id")]

    if mode == "regenerate" and target_rows:
        targets = [t.strip() for t in target_rows.split(",")]
        return [
            r for r in rows
            if str(r["row_num"]) in targets or r.get("req_id") in targets
        ]

    return rows


def _build_spec_index(sys1_path: str | None, spec_path: str | None) -> dict:
    """Build merged spec index from SYS1 and/or supplementary spec."""
    sys1_index = None
    slot_c_index = None

    if sys1_path:
        print(f"  Parsing SYS1 spec: {sys1_path}")
        sys1_index = build_spec_index(sys1_path)
        print(f"  → {len(sys1_index)} PDM codes indexed")

    if spec_path:
        fmt = detect_format(spec_path)
        if fmt is None:
            raise ValueError(f"Unsupported spec format: {spec_path}")
        print(f"  Parsing spec document ({fmt}): {spec_path}")
        parsers = {"pdf": parse_pdf, "docx": parse_docx, "xlsx": parse_xlsx}
        if fmt in parsers:
            slot_c_index = parsers[fmt](spec_path)
            print(f"  → {len(slot_c_index)} PDM codes extracted")

    return merge_indexes(sys1_index, slot_c_index)


def _estimate_cost(row_count: int, model: str, batch_size: int) -> float:
    """Rough cost estimate based on average token usage."""
    avg_input = 1500  # tokens per TC prompt
    avg_output = 800  # tokens per TC response
    calls = (row_count + batch_size - 1) // batch_size
    total_input = avg_input * row_count
    total_output = avg_output * row_count
    return calculate_cost(total_input, total_output, model)


def _would_exceed_budget(current_cost: float, batch_size: int, model: str, budget: float) -> bool:
    """Conservatively check whether the next batch would exceed the remaining budget."""
    estimated_batch_cost = _estimate_cost(batch_size, model, batch_size)
    return current_cost + estimated_batch_cost > budget


def _extract_existing_sequence_numbers(rows: list[dict]) -> list[int]:
    """Extract valid numeric suffixes from existing TC IDs."""
    sequences = []
    for row in rows:
        tc_id = row.get("tc_id")
        if not tc_id:
            continue

        parts = tc_id.rsplit("-", 1)
        if len(parts) != 2 or not parts[1].isdigit():
            continue

        sequences.append(int(parts[1]))

    return sequences


def run(args: argparse.Namespace) -> int:
    """Main execution flow. Returns exit code."""
    print(f"\n{'='*60}")
    print("TC Auto-Generation Tool")
    print(f"{'='*60}\n")

    # Step 1: Parse input xlsx
    print("[1/7] Parsing input file...")
    tc_data = parse_tc_xlsx(args.input)
    print(f"  Project: {tc_data['project']}")
    print(f"  Test Group: {tc_data['test_group']}")
    print(f"  Total rows: {tc_data['row_count']}")

    # Step 2: Filter rows by mode
    print(f"\n[2/7] Filtering rows (mode: {args.mode})...")
    rows = _filter_rows(tc_data["rows"], args.mode, args.rows)
    print(f"  Rows to process: {len(rows)}")

    if not rows:
        print("\n  No rows to process. Done.")
        return 0

    # Step 3: Build spec index
    print("\n[3/7] Building spec index...")
    spec_index = _build_spec_index(args.sys1, args.spec)
    if spec_index:
        print(f"  Merged index: {len(spec_index)} entries")
    else:
        print("  No spec files provided, skipping.")

    # Step 4: Spec matching (Layer 1)
    print("\n[4/7] Matching spec references (Layer 1)...")
    if spec_index:
        rows = match_spec_references(rows, spec_index)
        matched = sum(1 for r in rows if r.get("match_type") == "exact")
        print(f"  Matched: {matched}/{len(rows)}")
    else:
        print("  Skipped (no spec index).")

    # Step 5: Generate TC IDs
    print("\n[5/7] Generating TC IDs...")
    group_abbr = generate_group_abbreviation(tc_data["test_group"] or "TC")
    # Find max existing sequence for incremental mode
    existing_sequences = _extract_existing_sequence_numbers(tc_data["rows"])
    start = 1
    if existing_sequences:
        start = max(existing_sequences) + 1
    tc_ids = generate_tc_ids(tc_data["project"], group_abbr, len(rows), start=start)
    for row, tc_id in zip(rows, tc_ids):
        row["tc_id"] = tc_id
    print(f"  IDs: {tc_ids[0]} ~ {tc_ids[-1]}")

    # Step 6: Load/assign Test Sets
    print("\n[6/7] Assigning Test Sets...")
    framework = None
    if args.framework:
        framework = load_framework(args.framework)
    if framework:
        rows = assign_test_sets(rows, framework)
        print(f"  Loaded framework: {len(framework)} groups")
    else:
        print("  No framework provided. Test Set assignment skipped.")
        print("  (Use --framework to provide a confirmed framework.json)")

    # Dry run: show estimate and exit
    if args.dry_run:
        est_cost = _estimate_cost(len(rows), args.model, args.batch_size)
        print(f"\n{'='*60}")
        print("DRY RUN — Estimated Cost")
        print(f"  Rows: {len(rows)}")
        print(f"  Model: {args.model}")
        print(f"  Batch size: {args.batch_size}")
        print(f"  Estimated cost: ${est_cost:.4f}")
        print(f"  Budget limit: ${args.budget:.2f}")
        print(f"{'='*60}")
        return 0

    # Step 7: Generate TCs via API
    print(f"\n[7/7] Generating TCs (model: {args.model}, batch: {args.batch_size})...")
    context = {
        "project": tc_data["project"],
        "test_group": tc_data["test_group"],
        "test_set": "N/A",
    }

    total_cost = 0.0
    total_input_tokens = 0
    total_output_tokens = 0
    generated_rows = []
    failed_rows = []

    for i in range(0, len(rows), args.batch_size):
        batch = rows[i:i + args.batch_size]
        batch_num = (i // args.batch_size) + 1
        total_batches = (len(rows) + args.batch_size - 1) // args.batch_size

        print(f"\n  Batch {batch_num}/{total_batches} ({len(batch)} TCs)...")

        # Budget check
        if total_cost >= args.budget:
            print(f"\n  ⚠ Budget limit reached (${total_cost:.4f} >= ${args.budget:.2f}). Stopping.")
            failed_rows.extend(batch)
            continue
        if _would_exceed_budget(total_cost, len(batch), args.model, args.budget):
            print(
                f"\n  ⚠ Skipping batch: estimated cost would exceed budget "
                f"(${total_cost:.4f} + batch > ${args.budget:.2f})."
            )
            failed_rows.extend(batch)
            continue

        try:
            if len(batch) == 1:
                row = batch[0]
                context["test_set"] = row.get("test_set", "N/A")
                result = generate_single_tc(row, context, spec_index, RULES_SECTIONS, args.model)
                tc_data_list = [result.tc_data]
            else:
                result = generate_batch(batch, context, spec_index, RULES_SECTIONS, args.model)
                tc_data_list = result.tc_data

            total_input_tokens += result.input_tokens
            total_output_tokens += result.output_tokens
            total_cost += result.cost

            # Merge generated data into rows
            for row, tc in zip(batch, tc_data_list):
                merged = {
                    "row_num": row["row_num"],
                    "tc_id": row["tc_id"],
                    "test_group": tc_data["test_group"],
                    "test_set": row.get("test_set"),
                    "tc_title": tc["tc_title"],
                    "pre_conditions": tc["pre_conditions"],
                    "input_test_data": tc["input_test_data"],
                    "test_procedure": tc["test_procedure"],
                    "expected_result": tc["expected_result"],
                    "spec_reference": row.get("spec_reference"),
                    "priority": tc["priority"],
                    "design_method": tc["design_method"],
                }
                # Validate
                validation = validate_row({
                    "tc_id": merged["tc_id"],
                    "test_item": f"original\n\n{merged['tc_title']}",
                    "pre_conditions": merged["pre_conditions"],
                    "test_procedure": merged["test_procedure"],
                    "expected_result": merged["expected_result"],
                    "design_method": merged["design_method"],
                    "priority": merged["priority"],
                })
                issues = [v for v in validation.values() if not v.passed]
                if issues:
                    print(f"    ⚠ {row['tc_id']}: {len(issues)} validation warning(s)")
                    for issue in issues:
                        print(f"      - [{issue.check}] {issue.message}")
                    if args.strict_validation:
                        failed_rows.append(row)
                        continue
                else:
                    print(f"    ✓ {row['tc_id']}")

                generated_rows.append(merged)

            print(f"    Cost: ${result.cost:.4f} (total: ${total_cost:.4f})")

        except GenerationError as e:
            print(f"    ✗ Batch failed: {e}")
            failed_rows.extend(batch)

        # Rate limiting
        if i + args.batch_size < len(rows):
            time.sleep(0.5)

    # Write results
    print(f"\n{'='*60}")
    print("Writing results...")
    output_path = build_output_path(args.input, args.output_dir)
    os.makedirs(args.output_dir, exist_ok=True)

    if generated_rows:
        write_generated_results(args.input, generated_rows, output_path)
        print(f"  Output: {output_path}")

    # Write framework sheet if framework data exists
    if framework:
        fw_data = build_framework_sheet_data(tc_data["test_group"], framework)
        write_framework_sheet(output_path if generated_rows else args.input, fw_data, output_path)
        print("  Framework sheet updated.")

    # Summary
    print(f"\n{'='*60}")
    print("Summary")
    print(f"  Generated: {len(generated_rows)}/{len(rows)}")
    print(f"  Failed: {len(failed_rows)}")
    print(f"  Tokens: {total_input_tokens:,} in / {total_output_tokens:,} out")
    print(f"  Cost: ${total_cost:.4f}")
    if failed_rows:
        print(f"  Failed rows: {[r['row_num'] for r in failed_rows]}")
    print(f"{'='*60}\n")

    return 1 if failed_rows else 0


def run_preflight(args: argparse.Namespace) -> int:
    """Stage 2.5 pre-flight: does this batch fit the current window? Zero API."""
    from budget_planner import load_budget, fit_mixed

    if args.remaining_pct is None:
        print("Error: --preflight requires --remaining-pct (0..1 from /usage).",
              file=sys.stderr)
        return 2

    cfg = load_budget()
    result = fit_mixed(args.remaining_pct, args.n_light, args.n_deep, cfg)
    print(f"\n{'='*60}")
    print("Pre-flight Budget Checkpoint")
    print(f"  Remaining window: {args.remaining_pct:.0%}  (safety {cfg.safety:.0%})")
    print(f"  Batch: {args.n_light} light + {args.n_deep} deep")
    if result["decision"] == "wait":
        print("  Decision: WAIT — per_req_pct not calibrated yet.")
        print("  Run `--calibrate` after a probe run first.")
    else:
        print(f"  Projected window cost: {result['projected_pct']:.1%}")
        print(f"  Decision: {result['decision'].upper()}")
        if result["decision"] == "shrink":
            print(f"  Suggested caps: --n-light {result['max_light']} "
                  f"/ --n-deep {result['max_deep']}")
    print(f"{'='*60}\n")
    return 0


def run_calibrate(args: argparse.Namespace) -> int:
    """Stage 2.5 calibration: derive per_req_pct from a probe run. Zero API."""
    from budget_planner import record_calibration

    missing = [f"--{n.replace('_', '-')}" for n in
               ("start_pct", "end_pct", "n_probe", "regime")
               if getattr(args, n) is None]
    if missing:
        print(f"Error: --calibrate requires {', '.join(missing)}.", file=sys.stderr)
        return 2

    cfg = record_calibration(args.start_pct, args.end_pct, args.n_probe, args.regime)
    per = cfg.per_req_pct_light if args.regime == "light" else cfg.per_req_pct_deep
    print(f"\n{'='*60}")
    print(f"Calibrated {args.regime}: per_req_pct = {per:.4f} "
          f"({per:.2%} of window per requirement)")
    print(f"  Saved to config/budget.json at {cfg.calibrated_at}")
    print(f"{'='*60}\n")
    return 0


def run_trace(args: argparse.Namespace) -> int:
    """Content-based traceability (zero API): match TCs to SWE1 reqs by text."""
    from parser import parse_tc_xlsx
    from req_tracer import load_swe1_reqs, trace_tcs, summarize

    if not args.input or not args.swe1_reqs:
        print("Error: --trace requires --input and --swe1-reqs.", file=sys.stderr)
        return 2

    reqs = load_swe1_reqs(args.swe1_reqs)
    parsed = parse_tc_xlsx(args.input)
    rows = parsed["rows"] if isinstance(parsed, dict) else parsed
    results = trace_tcs(rows, reqs)
    s = summarize(results)

    os.makedirs(args.output_dir, exist_ok=True)
    with open(os.path.join(args.output_dir, "traceability.json"), "w",
              encoding="utf-8") as fh:
        json.dump({"summary": s, "results": [r.__dict__ for r in results]},
                  fh, ensure_ascii=False, indent=2)

    rate = s["content_traceability_rate"]
    lines = [
        "# Traceability (content-based)", "",
        f"- 總 TC:{s['total_tcs']}",
        f"- 內文可追溯:{s['traceable']} / 未追溯:{s['untraceable']}",
        f"- 內文可追溯率:{rate:.1%}" if rate is not None else "- 內文可追溯率:N/A",
        f"- **內文較傾向別的需求(建議查,suspect):{s['id_mismatch_count']}**",
        f"- 兄弟雙胞胎 / 平手(同模板,工具分不出,寫的 id 多半對):{s['ambiguous_twin_count']}",
        "",
        "> 注意:這是 token 比對的建議,不是定論。模板化需求只有語意 review 能確認。",
        "", "## 建議優先查的 TC(內文較傾向別的需求)", "",
        "| TC | 寫的 req_id | 內文較像 | score | 自身分 |", "|---|---|---|---|---|",
    ]
    for r in results:
        if r.confident_mismatch:
            lines.append(f"| {r.tc_id} | {r.tc_req_id} | {r.matched_req_id} | "
                         f"{r.score} | {r.written_score} |")
    twins = [r for r in results if r.ambiguous]
    if twins:
        lines += ["", "## 兄弟雙胞胎(同模板需求,工具分不出;寫的 id 多半正確)", "",
                  "| TC | 寫的 req_id | 內文像 | score / 自身分 |", "|---|---|---|---|"]
        for r in twins:
            lines.append(f"| {r.tc_id} | {r.tc_req_id} | {r.matched_req_id} | "
                         f"{r.score} / {r.written_score} |")
    untraceable = [r for r in results if not r.traceable]
    if untraceable:
        lines += ["", "## 內文對不到任何需求的 TC", ""]
        lines += [f"- {r.tc_id}(score {r.score})" for r in untraceable]
    with open(os.path.join(args.output_dir, "traceability.md"), "w",
              encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"\n{'='*60}\nContent-based Traceability")
    print(f"  TCs: {s['total_tcs']}  traceable: {s['traceable']}  "
          f"confident-mismatch: {s['id_mismatch_count']}  "
          f"ambiguous-twin: {s['ambiguous_twin_count']}")
    print(f"  Wrote: {args.output_dir}/traceability.json")
    print(f"         {args.output_dir}/traceability.md\n{'='*60}\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.trace:
        return run_trace(args)
    if args.preflight:
        return run_preflight(args)
    if args.calibrate:
        return run_calibrate(args)
    if args.scorecard:
        return run_scorecard(args)
    if not args.input:
        print("Error: --input is required (except for --scorecard).", file=sys.stderr)
        return 2
    if args.review:
        err = _reject_generate_flags(args)
        if err:
            print(f"Error: {err}", file=sys.stderr)
            return 2
        return run_review(args)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
