# FW036 Remaining TC Generation — Runbook for Claude Code

## Scope (verified against real files, 2026-08-05)

- FW036 rows 10–332 = compliant human-authored region (188 leaves / ~323 TCs). KEEP AS IS.
- FW036 rows 333–755 = placeholder drafts (Procedure = "Test", ad-hoc Test Sets,
  Heading parent rows included as TC rows). DISCARD AND REGENERATE.
- Remaining work: **262 leaf FRs across 159 parents** (PLA 52 / COM 57 / RAD 93 / INT 60),
  all sourced from Media HMI spec chapters 11–23.
- Estimated output: ~420–480 TCs (done-region ratio 1.7 TC/leaf).

## Key facts discovered during background analysis

1. **Media HMI PDF is a scanned image deck** — zero extractable text. Spec TEXT
   therefore comes from `SYS1_HMI_Media_HMI_Logic_and_Flow_R1LL_Febuary_9th_2026.xlsx`
   (Polarion export; its Outline Number IS the section numbering 037 references —
   verified 158/158 remaining sections resolve, content matches verbatim).
2. The PDF supplies IMAGES only: render each page to PNG; section→page mapping is
   built by OCR-matching item codes (USB1, BT1.2.1, MW9, …). Verified 158/158
   remaining sections mapped after adjacent-code + phrase fallback.
3. Design Method must be one of the 9 dropdown strings in the workbook's 下拉選單
   sheet (e.g. `功能測試 (Functional based ; no specific technique)`). Exact match.
4. Test Case Framework sheet currently lists 10 Test Sets. Chapter 23 (Media
   Widget, 25 leaves) has no home → framework update required before generation.

## Inputs to place in the working directory

- `docs.md`, `docs-core.md`, `framework.md`, `test_case_priority.md`, `TEST_SET_POLICY.md`
- `FMWIFSM037A03N1LSWE1MediaHMIV0_1_STLA_報告.xlsx`
- `FMWIFSM036A01_..._MediaHMI_20260625.xlsx`
- `SYS1_HMI_Media_HMI_Logic_and_Flow_R1LL_Febuary_9th_2026.xlsx`
- `Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_July_25th_2023.pdf`
- `Pop_Up_List_HMI_R1_SR24_Post_2A_Dec_15_2023.xlsx`
- this package (`scripts/`, `data/`)

Dependencies: `pip install openpyxl pymupdf pytesseract pillow` + system `tesseract`.

## Step 0 — Framework rulings (RESOLVED by Pei, 2026-08-05)

`data/section_to_testset.json` is FINAL. Rulings:

| Chapter | Test Set | Ruling |
|---|---|---|
| 11 (BTSA) | Source Selection | per draft; **PLA-062 overridden to Source Tab** (USB label = Source Tab anatomy) |
| 17 (MPB) | Presets | capability over location |
| 18 (APP) | **Preset Management (NEW)** | split from Presets per §4.1.2 granularity; capability-named, not UI-widget-named |
| 22 (AP AutoPlay) | Play Controls | playback auto-start policy |
| 23 (MW) | **Media Widget (NEW)** | spec formal name kept |

Remaining actions before generation:
1. Add `Preset Management` and `Media Widget` to `framework.md` (Layer 2, under
   Test Group Media) with their Layer-3 spec sections (ch18 / ch23)
2. Add the same two rows to the workbook `Test Case Framework` sheet
3. New Sets have no done-region exemplars — `make_batch_context.py` auto-falls
   back (Preset Management -> Presets, Media Widget -> Playing Tab); review the
   first generated parent of each new Set extra carefully

## Step 1 — Rebuild data artifacts (idempotent)

```bash
python scripts/build_remaining.py --a03 <037.xlsx> --fw036 <036.xlsx> --out data
python scripts/split_spec.py --sys1 <SYS1.xlsx> --pdf <MediaHMI.pdf> --out data
python scripts/extract_exemplars.py --fw036 <036.xlsx> --out data
```

Outputs: `remaining_leaves.json`, `sibling_map.json`, `spec_sections.json`,
`section_manifest.json`, `page_index.json`, `exemplars.json`,
`spec_pages/*.png` (44), `page_ocr/*.txt`.

Note: Browse Tab has only ONE exemplar in the done region (row 267) but ch14+19+20
= 83 remaining leaves. Supplement its style with Playing Tab / Source Tab exemplars
and run the ch14 pilot review extra carefully.

## Step 2 — Generation loop (one parent per turn)

```bash
python scripts/make_batch_context.py --list --data data            # 159 parents
python scripts/make_batch_context.py --parent SWE1-MEDIA-PLA-063 \
    --data data --popup <PopUpList.xlsx>                           # -> batches/<parent>.json
```

Per turn, the generating model receives:
1. The batch context JSON (requirements, siblings, spec section text, PU refs, exemplars)
2. The referenced `spec_pages/page_NN.png` files — **Read them as images**; anatomy
   layouts and tables (preset bank sizes, folder structures) exist ONLY in the images
3. docs.md §4–§9 condensed rules + the §9 self-check checklist
4. Output contract: JSON per docs.md §10 (10 keys per TC + top-level `reasoning`
   in Traditional Chinese, `keywords`, `duplicate_of`, `distinguishing_axis`)

Rules the generator must hold (top failure modes of the draft region):
- Test Set comes from `section_to_testset.json` — never invent one
- Heading parent rows (e.g. `SWE1-MEDIA-PLA-062` without `-NN`) are NOT TC rows
- One RD sub-id may yield multiple TCs (§8.2.2); enumerated supported items get a
  negative pair (§7); ER transforms `shall` into observable present-tense (§6)
- PU citations use the Pop Up List's own field name, e.g.
  `as defined by PU0998 String/Popup Message` (§8.4)
- Spec reference format: `Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_(July_25th,_2023)_<section>`

Persist each parent's output JSON to `generated/<parent>.json` before moving on
(checkpoint/resume; anomalies appended to the anomaly tracker, never silently
worked around).

## Step 3 — Lint (hard gate before write-back)

Reject any TC failing:
- keys: all 10 present; `test_procedure` ≥ 2 numbered steps
- no trailing `.`/`。` at end of any line in PC / ITD / Procedure / ER
- UI labels in `"..."` double quotes; no `[...]`, `'...'`, `<...>`
- priority ∈ {P0,P1,P2,P3}; design_method ∈ the 9 dropdown strings (exact)
- test_set ∈ framework whitelist; test_group == `MediaHMI`
- forbidden main verbs (observe/verify/check whether…) absent from Procedure;
  no modal verbs (shall/will/should/would) in ER
- Procedure count == ER count (1:1, blank-line phase breaks allowed)

## Step 4 — Write-back

Produce `output/FW036_regen.xlsx`:
1. Copy the source workbook; keep rows 10–332 untouched
2. Delete rows 333–755; append generated TCs from row 333 grouped in 037
   document order (parent order), leaf order within parent
3. Column mapping (0-based): D=req_id(leaf sub-id), G=MediaHMI, H=test_set,
   I=test_item, J=pre_conditions, K=input_test_data, L=test_procedure,
   M=expected_result, N=specification_reference, O=`NEW`, P=priority,
   R=design_method, S=`NA`, T..Z vehicle-model flags `1`, AA=author
4. Re-copy the B / F column formulas from the template row
5. Re-run the linter against the written workbook as final verification

## Step 5 — Execution order & model assignment

1. Pilot: PLA-062~068 (7 parents, ch11) with **Opus 4.8** → Pei reviews → adjust prompt
2. COM (ch12–14 front) → RAD (ch14 rest, 16–20) → INT (ch21–23)
3. Model split: Opus 4.8 for ch11/13/14/23 (new patterns, image-heavy layout
   judgement); Sonnet 4.6 acceptable for ch16–18/21 (heavily templated, strong
   done-region exemplars) if quota is tight
4. Commit per-chapter; keep `generated/` JSONs in git for diffable review
