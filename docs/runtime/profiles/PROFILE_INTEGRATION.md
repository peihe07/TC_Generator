# Integration Notes — FW036 Profile & BT Domain Pack

Status: **implemented** (see "Changes applied"). Activation is opt-in via
environment variables, so projects other than FW036 see zero behavior change.

## Files

- `docs/profiles/FW036_R1L_BT_Profile.md` — project profile overlay, appended
  AFTER the generic ASPICE rules so its `[OVERRIDE]` sections win.
- `config/domain_packs/R1L_BT.json` — Stage 1 Domain Pack (schema-validated
  against `backend/domain_pack.py`; remaining Gate ① warnings are the 4 open
  questions + missing `reviewed_at` sign-off, both intentional until Pei
  reviews and stamps it).
- `tests/test_profile_wiring.py` — 22 pytest cases covering all five wiring
  points below.

## Activation (FW036 batch)

```bash
export TC_PROJECT_PROFILE="FW036_R1L_BT_Profile"          # rules overlay
export TC_DOMAIN_PACK="config/domain_packs/R1L_BT.json"   # ground-truth pack
export TC_FIXED_TEST_SETS="Adapter & Device|Connection|Pairing|Phonebook (PBAP)|Phone (HFP)|Media (A2DP)|Data Control|IVI Integration"
export TC_SPLIT_MODE="standard"        # or "max_granularity" (「极致拆」), per batch
```

Unset all four → identical behavior to before this change. Every wiring point
also accepts an explicit function parameter (param wins over env), so the API
layer can later expose these as job-config fields without touching the
env path.

## Changes applied

1. **`rules_loader.py`** — `load_rules(..., profile=None)`; profile markdown
   from `docs/profiles/{profile}.md` is appended LAST (recency + the profile's
   own precedence header make overrides stick). Env fallback:
   `TC_PROJECT_PROFILE`. `api_server.py` and `gen_bridge.py` needed no edits —
   their existing `load_rules()` calls pick up the env automatically.
2. **`prompt_builder.py`** — `remarks` added to `REQUIRED_OUTPUT_KEYS` (so
   every prompt's output contract lists it) and to new `OPTIONAL_OUTPUT_KEYS`
   (so parsers tolerate engines that omit it). Hard constraint 10c: remarks
   stays empty unless a profile mandates a note (OCR provenance, dead-code
   workaround, BLOCKED/RD-1).
3. **`prompt_builder.py`** — `build_test_set_classification_prompt(...,
   fixed_test_sets=None)`: closed-vocabulary mode replaces the free-form
   label-derivation rules with a copy-character-for-character instruction.
   Env fallback: `TC_FIXED_TEST_SETS` (`|`-separated).
4. **`prompt_builder.py`** — `build_multi_tc_user_prompt` /
   `build_multi_tc_batch_prompt` gained `split_mode` + `domain_block` params.
   `split_mode="max_granularity"` appends the 「极致拆」 addendum (uniform
   batch-wide, AVRCP triad exception preserved). Env fallback:
   `TC_SPLIT_MODE`.
5. **`prompt_builder.py`** — `domain_block` injection between Spec Context and
   Rules in both multi-TC prompts; when the param is absent the pack at
   `TC_DOMAIN_PACK` is loaded once via `domain_pack.to_prompt_block` and
   cached. (`build_decompose_prompt` already had `domain_block`; unchanged.)
6. **`generator.py`** — the four missing-key checks
   (`parse_tc_response`, `parse_batch_response`, `_validate_tcs_array`,
   single-TC degenerate branch) skip `OPTIONAL_OUTPUT_KEYS`;
   `_normalize_tc_dict` defaults `remarks` to `""` so downstream writers can
   rely on the key existing.

## Deliberately NOT changed

- **`validator.py`** — both FW036 design-method strings
  (`功能測試 (Functional based ; no specific technique)`,
  `基礎故障注入 (Fault Injection Lite)`) were ALREADY in
  `VALID_DESIGN_METHODS`, so they pass verbatim; the profile merely restricts
  the engine to emit only those two. Regression-guarded in the test file.
- **`api_server.py`** (109 KB) — zero edits; env-based activation avoids
  touching the request models and job pipeline. Exposing profile /
  split_mode / fixed_test_sets as per-job API fields is a follow-up.
- **`writer.py`** — `remarks` is not yet mapped to a workbook column.
  TODO(Pei): confirm the FW036 Remarks column index (WRITE_COLUMNS /
  parser.HEADER_PATTERNS have no remarks entry today), then add
  `"remarks": <col>` to `writer.WRITE_COLUMNS` and a header pattern so
  template-mode export resolves it by header name. Red highlight for
  BLOCKED/RD-1 remains a manual convention.

## Verification

`python3 -m pytest tests/test_profile_wiring.py` → 22 passed. Cases:
profile ordering + env selection + legacy no-profile path + FW036 key strings
present; remarks contract/tolerance/preservation + required-key still fails;
split-mode param/env/fallback + standard has no addendum; fixed test-set
param/env/closed-list wording + default stays free-form; domain pack
loads/renders/injects + param-beats-env + no-pack-no-section; design-method
verbatim pass.

## Residual watch items

- Calibration Example 1 in `prompt_builder.py` still shows "The HU is powered
  on" as a bad pre-condition. Profile §3.2 overrides it explicitly; if engines
  keep dropping the fixed opening line in FW036 batches, add a waiver note
  next to that example.
- Priority (P0–P3) untouched — FW036 context defines no priority rubric, so
  the generic one stays.
- `gen_bridge.py` builds its own context prompt and already supports a
  domain-pack path parameter; it now also inherits the profile via
  `load_rules()` env. Its `DESIGN_METHODS` post-check list is independent —
  verify it contains the two FW036 strings if the bridge path is used.
