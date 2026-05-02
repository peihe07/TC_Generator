# Review Feature Integration — TC Generator

This drop-in folder contains v2.2 of the ASPICE SWE.6 review spec, organised to match the `tc-generator` project layout.

## What this adds

The TC Generator currently produces TCs (`docs/ASPICE_SWE6_AI_Instruction.md` is auto-loaded into the generate prompt). This integration adds a **parallel review capability** — same spec, same data structures, but the AI is auditing existing TCs instead of producing new ones.

The review feature does NOT replace any generate functionality. Generate prompt and rules stay untouched.

## Files in this drop

| File | Drop into | Purpose |
|---|---|---|
| `docs/ASPICE_SWE6_AI_Review.md` | `docs/` | Auto-loaded into review prompt (mirrors `ASPICE_SWE6_AI_Instruction.md`) |
| `backend/rules/review_rules.yaml` | `backend/rules/` | Structured rule table for the rule engine |

## Why two files

Same dual-format reasoning as the existing project's generate side:

- **`ASPICE_SWE6_AI_Review.md`** — the human-readable spec. `review_prompt_builder.py` (you'll create this) reads it at runtime and injects it into the LLM call, exactly like `prompt_builder.py` does today.
- **`review_rules.yaml`** — the machine-readable companion. The new rule engine iterates this for fast pre-checks before LLM call. 20 of 31 rules don't need LLM at all (`requires_llm: false`); these run as a cheap regex pass first.

## Suggested integration steps

In suggested order — earlier steps unblock later ones:

### 1. Drop the docs in place

```bash
cp docs/ASPICE_SWE6_AI_Review.md <repo>/docs/
mkdir -p <repo>/backend/rules
cp backend/rules/review_rules.yaml <repo>/backend/rules/
```

Update the README's "Reference docs" section to add:

```
- [docs/ASPICE_SWE6_AI_Review.md](docs/ASPICE_SWE6_AI_Review.md) — ASPICE SWE.6 AI Review spec (auto-loaded into review prompt)
```

### 2. Backend — new module mirrors `prompt_builder.py`

Create `backend/review_prompt_builder.py` following the existing `prompt_builder.py` pattern:

- Read `docs/ASPICE_SWE6_AI_Review.md` once at import time (same as Instruction)
- Build per-batch review prompts:
  - input: list of TC dicts (parsed from workbook by existing parser)
  - output: chat messages array for OpenAI call
- Output schema matches §9 of the spec — `per_req_findings` + `per_tc_findings` + `batch_summary`

### 3. Backend — new rule engine

Create `backend/review_engine.py`:

- Load `backend/rules/review_rules.yaml` at import
- Iterate Tier 1 → Tier 2 → Tier 3
- For rules with `requires_llm: false`, run regex/keyword detection directly
- For rules with `requires_llm: true`, batch up TC + rule context and call OpenAI via `review_prompt_builder.py`
- Apply `interactions` (mutual_exclusions, suppressions, tier_skip_conditions) before emitting findings
- Return findings in the §9 schema

### 4. Backend — CLI flag

Add `--review` mode in `backend/main.py`:

```bash
python backend/main.py --review --input path/to/existing_tcs.xlsx --output-dir output
```

Reuse existing Excel parser; emit `findings.json` + `findings_report.md` to `--output-dir`.

### 5. Backend — API route

Add `POST /review` to `backend/api_server.py` mirroring the generate endpoint shape (job-based async pattern).

### 6. Frontend — proxy + module

- New proxy: `frontend/app/api/review/route.ts` (mirrors `frontend/app/api/generate/route.ts`)
- New module: `frontend/src/modules/ReviewModule.tsx`
- Extend `frontend/src/services/jobAdapter.ts` with a review job type
- Reuse upload + workbook display components from existing modules

### 7. Tests

- Backend: `pytest backend/tests/test_review_engine.py` covering 4 deep-dive cases:
  - rows 52-55 (§7.4 fabricated value)
  - row 480 (§6.7 multi-Req-ID + §7.5 tool launch)
  - rows 526-532 (§6.6 tier1_skipped + §8.3.6 fallback)
  - rows 10-12 (Tier 1 pass + Tier 3 only)
- Frontend: typecheck only (no behavioural tests for new module yet)

## Integration touch points to verify

Before merging:

1. **Workbook parser shared**: existing `parser` module reads the same sheet (`Test Case Specification 測試用例規範`). Confirm it handles **multi-Req-ID cells** (newline-separated) — the v2.2 spec §6.7 relies on this. Existing generate path may have stripped or normalised this; review path needs the raw value.
2. **Spec ref column access**: review's §7.4 detection requires reading the `Specification Reference` column. Generate path may not surface this in its parsed dict — extend if missing.
3. **`docs/RULES.md` vs `docs/ASPICE_SWE6_AI_Review.md` overlap**: the existing `RULES.md` contains tool-side rules (column mapping, ID format). The Review spec only references `docs/test_case_priority.md` (P0–P3 rubric in §8.5.1). If that file exists, review can reference it directly.
4. **Model selection**: review default model should match generate (`gpt-5`); rule-engine pre-pass needs no model. Add `--review-model` CLI flag if needed.

## What I have NOT included (intentional)

These need access to the actual repo to write correctly:

- `backend/review_prompt_builder.py` — depends on existing `prompt_builder.py` shape
- `backend/review_engine.py` — depends on existing parser dict shape
- `frontend/app/api/review/route.ts` — depends on existing proxy patterns
- `frontend/src/modules/ReviewModule.tsx` — depends on existing module conventions and Zustand store shape
- `backend/tests/test_review_engine.py` — depends on existing test fixtures

If you want me to write any of these, push the relevant existing file(s) and I'll pattern-match them.

## Open question

Generate-side `docs/ASPICE_SWE6_AI_Instruction.md` is currently auto-loaded into prompts. The version we built in this thread was a v1 → v2 → v2.1 → v2.2 evolution that diverged from your live `Instruction.md`. **The review spec assumes you keep generate-side and review-side as two separate docs**, not one merged file. If you'd rather have a single shared spec with `[GENERATE]` and `[REVIEW]` sections, that's a different (larger) change worth deciding before integration.
