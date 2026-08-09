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
6. Last Mode spec: 037 cites `... R1L-R (August 2 2021)`; `inputs/` holds
   `... R1 SR24 1A (August 2 2021).xlsx`, whose 359-row `Last Mode Table`
   resolves all 15 B7 `_{n}` suffixes exactly. **Ruled the same document
   (A-H03).** B7 spec_reference uses the ACTUAL file name, not 037's label:
   `Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021)_{n}`,
   `{n}` = List Item number. This is a deliberate divergence from the 037
   string so the reference names a document the tester can locate.
7. Remarks is column **AG (33)**, not AH as in Media. Header row is 9;
   the sheet is `Test Case Specification&Result` (no space before `&`).

## Directory layout (mirrors mediaHMI/)

```
HomeHMI/
├── inputs/     # 6 source files (incl. Last Mode Table xlsx — see A-H03)
├── data/       # derived, all regenerable — never hand-edit:
│               #   spec_id_to_outline.tsv  outline map
│               #   remaining_leaves.json   62 regen targets
│               #   sibling_map.json        parent -> all leaf sub-ids
│               #   row_segments.json       segments + done-region hash
│               #   spec_sections.json      SYS1 outline -> text
│               #   section_manifest.json   outline -> text/code/pages
│               #   spec_pages/ page_text/  PNG + extracted text per page
│               #   page_index.json         per-page codes
│               #   spec_diff.json          SYS1 <-> PDF code diff
│               #   exemplars.json          few-shot anchors by chapter
│               #   last_mode_items.json    List Item -> behavior (B7)
├── batches/    # per-batch context JSON (B1–B7)
├── generated/  # per-parent output JSON (checkpoint/resume)
├── feature.yaml # SINGLE SOURCE of constants: input path globs, sheet name,
│               # header row, column letters, done-region detection, lint
│               # inputs. Scripts read it via scripts/feature_config.py.
├── scripts/    # feature_config (loader) + build_outline_map /
│               # build_remaining / split_spec / extract_exemplars /
│               # build_last_mode / make_batch_context; lint_tcs +
│               # write_back TODO
├── docs/       # batches-home.md (execution plan)
├── ANOMALIES.md
└── RUNBOOK.md  # this file
```

Profile: `docs/runtime/profiles/FW036_R1L_Home_Profile.md` (overlay on the
generic ASPICE instruction). Framework: Home Test Group section appended to
`docs/fw036/framework.md` — one project, one framework.md.

## Step 0 — Rulings: ALL CLOSED (2026-08-09)

| # | Ruling | Effect |
|---|---|---|
| A-H01 | 066 fully decomposed → placeholder row, content on -01/-02 | B5 unblocked |
| A-H02 | 055-03 → placeholder row, no independent TC | B3 unblocked |
| A-H03 | `R1L-R` ≡ `R1 SR24 1A Post DCR19344`, same document | **B7 unblocked** |
| A-H09 | 020/021 attribute to CarPlay Template, not Default Layout | batching only |

Nothing blocks generation. **All 62 leaves have a path.** Two items remain as
RD-1 questions carried to delivery, neither gating: A-H06 (035 missing from
037) and the A-H03(c) residual risk (upstream to confirm the label
equivalence; if denied, only the `spec_reference` string changes).

## Step 1 — Rebuild data artifacts (idempotent)

```bash
python scripts/build_outline_map.py --sys1 inputs/SYS1_*.xlsx --out data
python scripts/build_remaining.py --a03 inputs/FM-WI-FSM-037*.xlsx \
    --fw036 inputs/FM-WI-FSM-036*.xlsx --out data
python scripts/split_spec.py --sys1 inputs/SYS1_*.xlsx \
    --pdf "inputs/Home Screen"*.pdf --out data
python scripts/extract_exemplars.py --fw036 inputs/FM-WI-FSM-036*.xlsx --out data
python scripts/build_last_mode.py --last-mode "inputs/Last Mode Table"*.xlsx \
    --out data
```

Then assemble batch contexts (Step 2 input):

```bash
for b in B1 B2 B3 B4 B5 B6 B7; do
  python scripts/make_batch_context.py --batch $b \
      --popup "inputs/Pop Up List"*.xlsx
done
```

All path arguments are **overrides**: omit them and the script resolves the
glob in `feature.yaml` `paths.*` (fail loud unless it matches exactly one
file). The commands above pass paths explicitly and still work unchanged.
No script carries its own column map — sheet name, header row and column
letters all come from `feature.yaml` through `scripts/feature_config.py`.

Adaptations vs Media:
- `build_remaining.py`: done-region detection by non-empty Test Case Author
  (col Z), three segments, NOT by row threshold. Asserts the expected shape
  (140 leaves / 62 remaining / 144 Arif rows) and fails loud if the inputs
  moved; `--no-assert` to override deliberately. Also emits
  `row_segments.json` (segment boundaries + done-region content hash) for
  Step 4, and reports orphan req_ids (A-H06).
- `split_spec.py`: text-layer-first, per-page OCR fallback; PNG render kept
  for figure pages. Chapter-heading and parent-outline fallbacks map the
  code-less "Please refer to the diagram" rows onto their figure page.
  `--force-ocr` reverts to the Media-style pipeline.
- `extract_exemplars.py`: keys exemplars by spec chapter (HSD/HSS/HS) via
  `spec_id_to_outline.tsv`, since the Test Set column is blank. Skips
  blank-priority rows (A-H05) so they are not learned as style.
- `build_last_mode.py` (new, Home-only): extracts the Last Mode Table into a
  List Item lookup for B7. Forward-fills the vertically merged Operation and
  Screen Display Status columns — a row read alone loses its trigger.
- `make_batch_context.py`: batch membership from `docs/batches-home.md`;
  refuses to resolve non-Home-spec leaves against the Home manifest (the
  `_{n}` namespaces collide); pulls chapter figure pages in via the
  image-only sibling rows; reports exemplar fallbacks instead of hiding them.

Verified output (2026-08-09 inputs):

```
037 leaves: 140  done: 78  remaining: 62 across 48 parents
segments: ARIF 10-86 (77)  REGEN 87-90 (4)  ARIF 91-124 (34)
          REGEN 125-128 (4)  ARIF 129-161 (33)  REGEN 162-238 (77)
spec_sections: 104 outline entries; 96 mapped to pages
text extraction: text-layer=18, ocr=1; 0 SYS1 codes absent from PDF
exemplars: 9 TCs across 3 spec chapters (HSD 116, HSS 23, HS 5 in pool)
last_mode_items: 352 List Items, exactly 15 with Screen Display Status = HOME
```

Those 15 HOME rows are a 1:1 match with B7's 15 leaves — independent
corroboration of the A-H03 ruling.

All 47 B1–B6 leaves resolve to a spec page. The 15 unresolved are B7 — they
trace to the Last Mode spec, not the Home Screen spec (see A-H03).
**No exemplars exist for SNS / BSP / SW**: Arif never wrote those chapters, so
B4–B6 must borrow HSS exemplars as the nearest analogue.

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
- B7 generates normally (A-H03 resolved). Its context comes from the Last
  Mode Table sheet, not the Home Screen spec — `make_batch_context.py`
  deliberately injects no Home spec text for those 15 leaves, because the
  `_{n}` suffixes are List Item numbers that collide with Home outline
  numbers.

Batch order: B1 pilot (5 leaves, CarPlay Template) → Pei review → B2→B6 → B7.
B7 is last only because its extraction artifact is the newest, not because it
is blocked.
Model: Opus 4.8 for B1/B5/B6 (layout judgement, external-ref density);
Sonnet 4.6 acceptable for B2–B4 (templated, strong HSS exemplars).

## Step 3 — Lint (hard gate)

`lint_tcs.py` is NOT yet written for Home. When it is, it must read its
inputs from `feature.yaml` rather than hard-coding them:
- `lint.popup_ids` for the PU allow-list
- the workbook `下拉選單` sheet for the Design Method whitelist (9 strings,
  exact match) — the sheet is the authority, `feature.yaml` only points at
  the workbook
- `workbook.columns` for every column index

It must also implement the A-H08 rule: strip double-quoted spans before the
ER modal-verb check, so verbatim popup text (`Widget cannot be moved here.`)
does not fail the gate.

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
   sequence of 144 Arif row contents (cols D..AG) is hashed before and after
   and must match exactly, regardless of absolute row indices after
   insertion/deletion. The baseline hash is emitted by `build_remaining.py`
   into `data/row_segments.json` (`ordered_content_hash`).
3. Segment order invariant: Arif segment 1 < regen 1 < Arif 2 < regen 2 <
   Arif 3 < regen 3.
4. Re-emit B (=ROW()-9) and F formulas on every row below the first edit.
5. Column mapping (1-based, verified): D=req_id, G/H=blank, I=test_item,
   J=pre_conditions, K=input_test_data, L=test_procedure, M=expected_result,
   N=spec_reference, O=`NEW`, P=priority, Q=design_method, R=`NA`,
   S–Y=vehicle flags, Z=author(`PeiPYHsu`), **AG=Remarks** (verified against
   header row 9 — Media's AH lesson: dropping it silently drops all
   BLOCKED/anomaly notes).
6. Traceability / completeness invariants as Media, with one scoping change:
   every req_id ∈ 037 applies to **regen rows only** — Arif's rows 129–130
   trace to 035, which 037 omits (A-H06). Regen leaves == 62 exactly;
   ChangeHistory revision row appended; xlsx normalization for stable
   SHA256.
7. Do NOT touch Arif's 13 blank-priority rows (A-H05 — recorded, not fixed).

Extend `tests/test_write_back.py`: interleaved-segment fixture + content-hash
invariant + idempotency.

## Step 5 — Delivery

Same as Media: lint_report → ANOMALIES review → release tag binding xlsx
SHA256 to commit → controlled document submission + RD-1 questions
(A-H01, A-H02, A-H03 version-label confirmation, A-H06 missing 035) to
upstream.
