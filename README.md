# TC Generator

Automated test case generation tool for ASPICE SWE.6.

The tool reads a TC specification Excel file, optionally enriches context from SYS1 and supplementary spec documents, generates test cases with Claude, validates the generated fields, and writes results back into a new Excel file.

## Requirements

- Python `>=3.10`
- An Anthropic API key available in the environment

Example:

```bash
export ANTHROPIC_API_KEY=your_key_here
```

You can also place the key in a local `.env` file because the CLI loads dotenv on startup.

## Install

```bash
pip install -e .
```

For development:

```bash
pip install -e ".[dev]"
```

## Run Tests

```bash
pytest -q
```

## Basic Usage

```bash
python src/main.py --input path/to/SomeProject_SWQT_DeviceManager_20260408.xlsx --dry-run
```

Generate actual output:

```bash
python src/main.py \
  --input path/to/SomeProject_SWQT_DeviceManager_20260408.xlsx \
  --sys1 path/to/SYS1.xlsx \
  --spec path/to/spec.docx \
  --framework path/to/framework.json \
  --output-dir output \
  --model claude-sonnet-4-6 \
  --batch-size 5
```

## CLI Options

- `--input`: Required TC specification `.xlsx`.
- `--sys1`: Optional SYS1 spec `.xlsx` used for traceability matching.
- `--spec`: Optional supplementary spec document. Supported formats are `.pdf`, `.docx`, `.xlsx`.
- `--framework`: Optional confirmed `framework.json` for assigning `Test Set`.
- `--output-dir`: Directory for generated workbook output. Default is `output`.
- `--model`: Anthropic model name. Default is `claude-sonnet-4-6`.
- `--batch-size`: Number of TCs per API call. Default is `5`.
- `--mode`: One of `full`, `incremental`, `regenerate`.
- `--rows`: Comma-separated row numbers or requirement IDs for `regenerate` mode.
- `--dry-run`: Skip API calls and only print estimated cost.
- `--budget`: Maximum allowed spend in USD. Default is `5.0`.
- `--strict-validation`: Treat validation warnings as failures. Invalid rows are skipped and the process exits non-zero.

## Modes

- `full`: Process all parsed rows.
- `incremental`: Only process rows without an existing `tc_id`.
- `regenerate`: Only process rows selected by `--rows`.

## Output Behavior

- Output file name format: `{input_filename}_generated.xlsx`
- Generated fields are written back into the `Test Case Specification&Result` sheet.
- Column `I` keeps the original `Test Item` text and replaces the generated rewrite section on reruns.
- If `framework.json` is provided, the `Test Case Framework` sheet is also written or refreshed.
- Optional fields such as `Test Set` and `Specification Reference` are cleared when the latest run no longer provides a value.

## Validation Behavior

The generator validates:

- `tc_id`
- `test_item` rewrite format
- `pre_conditions`
- `test_procedure`
- `expected_result`
- `design_method`
- `priority`

Default behavior:

- Validation issues are printed as warnings.
- Rows are still written to the output workbook.

Strict behavior with `--strict-validation`:

- Invalid rows are marked as failed.
- Invalid rows are not written to the output workbook.
- The command exits with status `1` if any row fails.

## Cost and Budget

- `--dry-run` gives a rough estimate before any API call.
- During generation, the tool blocks a batch before sending it if the estimated next-batch cost would exceed `--budget`.
- Budget enforcement is conservative and based on internal token heuristics, not exact provider-side prebilling.

## Spec Inputs

- `--sys1` is used to build a PDM-based reference index for traceability.
- `--spec` is used as extra prompt context for generation.
- Unsupported `--spec` extensions fail fast with an error instead of being silently ignored.

## Common Workflows

Dry run before generation:

```bash
python src/main.py --input path/to/file.xlsx --dry-run
```

Incremental generation:

```bash
python src/main.py --input path/to/file.xlsx --mode incremental
```

Regenerate selected rows:

```bash
python src/main.py --input path/to/file.xlsx --mode regenerate --rows 10,12,SWE1-HMI-DM-002-01
```

Strict validation in CI or gated flows:

```bash
python src/main.py --input path/to/file.xlsx --strict-validation
```

## Notes

- The parser expects the TC workbook sheet names used by this project, especially `Product Document` and `Test Case Specification&Result`.
- The test group is derived from the input filename pattern `*_SWQT_{TestGroup}_YYYYMMDD.xlsx`.
- If the workbook contains blank rows between valid data rows, parsing continues and later rows are still processed.

## Related Docs

- [docs/RULES.md](/Users/peihe/Work_Projects/TC_Generator/docs/RULES.md)
- [docs/IMPLEMENTATION_PLAN.md](/Users/peihe/Work_Projects/TC_Generator/docs/IMPLEMENTATION_PLAN.md)
