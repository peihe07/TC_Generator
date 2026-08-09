# FW036 Home HMI — TC Generation Runbook for Claude Code

## Scope (verified against real files, 2026-08-09)

- Workbook: `FMWIFSM036A01 ... SWQT_Home_20260720.xlsx`, sheet
  `Test Case Specification&Result`, header row 9, data from row 10.
- 037 report: 161 rows = 140 leaf FRs + 21 Headings.
- **Done region (KEEP, author=Arif, 144 rows, 78 leaves) — THREE segments:**
  rows 10–86, rows 91–124, rows 129–161.
- **Regen region (DISCARD, author blank, 85 rows, 60 leaves) — THREE segments:**
  rows 87–90 (020×3, 021), rows 125–128 (032, 033, 034×2), rows 162–238
  (048-01 onward). Draft rows have real content but fail lint (scope/wording);
  regenerate all.
- Not covered anywhere: 055-03, 066 → included in regen targets.
- **Total regen targets: 62 leaves, 7 batches (B1–B7), see `docs/batches-home.md`.**
- Estimated output: ~90–110 TCs (done-region ratio ≈1.85 TC/leaf).

## Key facts from background analysis

1. **Home PDF has a text layer** (unlike Media's scanned deck). Step 1 first
   runs `pdftotext` and diff-checks against SYS1 text; OCR pipeline is the
   fallback only. Images still required for anatomy/layout tables
   (VMB/HMB/LSW/SW/SNS figure pages) — render pages to PNG as in Media.
2. Spec TEXT authority = `SYS1_HMI_Home_Screen_...xlsx` Basic Report;
   its Outline Number IS the section numbering (verified HSD1→4.1,
   HSS→9.x). 104 outline rows, 76 carry a spec ID (HSD/HSS/SNS…);
   mapping built by `scripts/build_outline_map.py` →
   `data/spec_id_to_outline.tsv`. Lookup miss = fail loud → ANOMALIES.md.
3. Spec reference format (Arif precedent, verbatim):
   `Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023)_{outline}`
4. Design Method: 9 dropdown strings in 下拉選單 sheet; Arif used only
   `功能測試 (Functional based ; no specific technique)`. Follow §12 mapping
   but expect Functional to dominate; exact-match strings required.
5. **Test Group (G) / Test Set (H) columns are BLANK in the done region.
   Keep them blank on new rows.** Framework Test Sets are used only for
   batching/lint grouping (see `docs/fw036/framework.md` Home section).
   Workbook `Test Case Framework` sheet is empty — do not populate.
6. Last Mode spec (`Last Mode Table HMI Logic and Flow R1L-R (August 2 2021)`)
   is MISSING from inputs. B7 (076–090, 15 leaves) is BLOCKED until the file
   lands in `inputs/`. See ANOMALIES.md A-H03.

## Directory layout (mirrors mediaHMI/)

```
HomeHMI/
├── inputs/     # 5 source files + Last_Mode_Table_....pdf when obtained
├── data/       # derived: spec text/pages, outline map, exemplars, sibling map
├── batches/    # per-batch context JSON (B1–B7)
├── generated/  # per-parent output JSON (checkpoint/resume)
├── scripts/    # copied from mediaHMI/scripts + build_outline_map.py; adapt constants
├── docs/       # batches-home.md (execution plan)
├── ANOMALIES.md
└── RUNBOOK.md  # this file
```

Profile: `docs/runtime/profiles/FW036_R1L_Home_Profile.md` (overlay on the
generic ASPICE instruction). Framework: Home Test Group section appended to
`docs/fw036/framework.md` — one project, one framework.md.

## Step 0 — Pending rulings (Pei)

1. ~~A-H01~~ RESOLVED 2026-08-09: 066 → placeholder row, content on -01/-02
2. ~~A-H02~~ RESOLVED 2026-08-09: 055-03 → placeholder row, no independent TC
3. 020/021 Test Set attribution (Default Layout vs CarPlay Template) —
   batching only, no workbook impact
4. Obtain Last Mode spec (unblocks B7) — STILL OPEN, critical path

## Step 1 — Rebuild data artifacts (idempotent)

```bash
python scripts/build_outline_map.py --sys1 inputs/SYS1_*.xlsx --out data
python scripts/build_remaining.py --a03 inputs/FMWIFSM037*.xlsx \
    --fw036 inputs/FMWIFSM036*.xlsx --out data
python scripts/split_spec.py --sys1 inputs/SYS1_*.xlsx \
    --pdf inputs/Home_Screen_*.pdf --out data --try-text-layer
python scripts/extract_exemplars.py --fw036 inputs/FMWIFSM036*.xlsx --out data
```

Adaptations vs Media:
- `build_remaining.py`: done-region detection by author=="Arif" (three
  segments), NOT by row threshold
- `split_spec.py`: text-layer-first; PNG render kept for figure pages
- `extract_exemplars.py`: key exemplars by spec chapter (HSD/HSS/SNS/BSP)
  since Test Set column is blank

## Step 2 — Generation loop (one parent per turn)

Same contract as Media RUNBOOK Step 2. Home-specific holds:

- Test Item follows the done-region shape (see Profile §3.1)
- Popup text verbatim from Pop Up List fields: PU0091, PU0942, PU1274,
  PU1291 — `as defined by PUxxxx String/Popup Message`; never paraphrase
- Screen-size variants (7"/8.4"/10.1"/10.25"/12"/12.3"/Portrait) are a §8.3
  sibling axis; follow Arif's 001-01~03 granularity precedent (per-req-sub-id,
  not per-size explosion beyond what 037 already splits)
- Vehicle-in-motion lockouts: motion state is the spec trigger →
  valid Pre-Condition (§8.5 exception); popup + grey-out are the same
  trigger's consequential outcomes → one TC, multi-line ER (§5.7)
- BSP struck-through text (Know & Go Hub) is OUT of scope (A-H04)
- B7: BLOCKED placeholder rows only until Last Mode spec lands

Batch order: B1 pilot (5 leaves, CarPlay Template) → Pei review → B2→B6 → B7.
Model: Opus 4.8 for B1/B5/B6 (layout judgement, external-ref density);
Sonnet 4.6 acceptable for B2–B4 (templated, strong HSS exemplars).

## Step 3 — Lint (hard gate)

All Media gates, plus:
- test_group and test_set cells must be EMPTY (done-region convention)
- every PU citation resolves against Pop Up List; popup wording verbatim
- spec_reference resolves through `spec_id_to_outline.tsv`; unresolved → fail
- B7 rows: BLOCKED format only, no fabricated content

## Step 4 — Write-back (STRATEGY CHANGE vs Media)

Media used a positional boundary (rows 10–332 frozen). Home's regen rows are
INTERLEAVED between done segments, so:

1. Rewrite each of the three blank segments IN PLACE, in 037 document order;
   row insert/delete allowed WITHIN a segment (regen TC count ≠ 85).
2. **Done-region invariant is content-based, not positional**: the ordered
   sequence of 144 Arif row contents (col D..AH) is hashed before and after
   and must match exactly, regardless of absolute row indices after
   insertion/deletion.
3. Segment order invariant: Arif segment 1 < regen 1 < Arif 2 < regen 2 <
   Arif 3 < regen 3.
4. Re-emit B (=ROW()-9) and F formulas on every row below the first edit.
5. Column mapping (1-based, verified): D=req_id, G/H=blank, I=test_item,
   J=pre_conditions, K=input_test_data, L=test_procedure, M=expected_result,
   N=spec_reference, O=`NEW`, P=priority, Q=design_method, R=`NA`,
   S–Y=vehicle flags, Z=author(`PeiPYHsu`), Remarks column = verify header
   at adaptation time (Media's AH lesson: dropping it silently drops all
   BLOCKED/anomaly notes).
6. Traceability / completeness invariants as Media: every req_id ∈ 037;
   regen leaves == 62 exactly; ChangeHistory revision row appended;
   xlsx normalization for stable SHA256.
7. Do NOT touch Arif's 13 blank-priority rows (A-H05 — recorded, not fixed).

Extend `tests/test_write_back.py`: interleaved-segment fixture + content-hash
invariant + idempotency.

## Step 5 — Delivery

Same as Media: lint_report → ANOMALIES review → release tag binding xlsx
SHA256 to commit → controlled document submission + RD-1 questions
(A-H01, A-H02, Last Mode spec request) to upstream.
