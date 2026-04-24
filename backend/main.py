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


RULES_SECTIONS = """
## ASPICE TC Writing Rules
- One behavior per TC, must match requirement intent
- Format: Condition/Trigger → Observable Outcome

## Pre-Conditions
- State or environment ONLY, never actions
- Minimum necessary state, numbered list or NA

## Input Test Data
- Explicit deterministic values, or NA

## Test Procedure
- Setup steps → Transition steps → Final Step (verification)
- Each step: executable action + purpose
- Final step must include action + verification target

## Expected Result
- 1:1 mapping with procedure steps
- Observable, judgeable, no vague language

## Design Method
- Use decision waterfall: Negative → Fault Injection → State Transition → Decision Table → EP → BVA → Combinatorial → Scenario → Functional

## Application Output Contract
- Priority is a workbook/tooling field, not an ASPICE rule in the instruction doc
- Return exactly P0 / P1 / P2
- P0: safety, core functionality, data loss risk
- P1: standard feature, user-facing behavior
- P2: UI cosmetic, edge cases
""".strip()


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="TC Auto-Generation Tool — ASPICE SWE.6",
    )
    p.add_argument("--input", required=True, help="TC Specification xlsx path")
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
    return p.parse_args(argv)


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


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
