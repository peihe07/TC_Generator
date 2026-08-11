# FW036 Home HMI — TC Generation Runbook for Claude Code

> **2026-08-11: directory moved `HomeHMI` → `features/home`.** Repo-wide reorganisation —
> all features now live under `features/`, lowercase and without the HMI
> suffix. Path strings in the body below are NOT rewritten: they are dated
> records, and they record what was true when they were written (same
> convention as the 2026-08-10 `AMFMHMI` → `AMFM` rename). Read any
> `HomeHMI/…` path in this file as `features/home/…`. `feature.yaml` paths are
> relative to the feature directory and were not affected.

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

**Status 2026-08-09: Step 2 COMPLETE.** All 62 leaves generated, 72 TCs
(1.16 TC/leaf) including 4 placeholder rows, lint clean.

| Batch | Leaves | TCs | Notes |
|---|---|---|---|
| B1 CarPlay Template | 5 | 9 | |
| B2 Shortcuts Edit | 10 | 10 | |
| B3 Shortcuts Lockout + Exclusion | 9 | 9 | 055-03 placeholder (A-H02) |
| B4 Shortcut Availability + Actions | 7 | 13 | 061 = 7 TCs over the SW7 table |
| B5 Navigation Shortcuts | 12 | 12 | 066 / 070 / 071 placeholders |
| B6 Brand Pages + Locking | 4 | 4 | |
| B7 Last Mode | 15 | 15 | cites the Last Mode file name (A-H03) |

Priority spread P0/P1/P2/P3 = 10/37/19/2. Design methods: Functional 35,
State Transition 14, Equivalence Partitioning 13, Decision Table 3,
Negative 3 — the done region used Functional exclusively, so the other four
are new to this workbook and are the first thing to check in review
(Profile §3.3 assigns per §12 truthfully rather than matching precedent).
Model: Opus 4.8 for B1/B5/B6 (layout judgement, external-ref density);
Sonnet 4.6 acceptable for B2–B4 (templated, strong HSS exemplars).

## Pilot gate — PASSED (Pei, 2026-08-09) — pre-write-back tasks

Reviewed in chat: B1 complete + stratified samples across B3–B7 (11 parents,
20 TCs). Full record in ANOMALIES.md (pilot gate entry). Verdict: PASS with
one corpus-wide mechanical correction. The earlier "lint clean" predates the
A-H10 amendment, so lint must be re-run after:

1. **A-H10 amendment correction (corpus-wide)**: `Press <OK>` → `Press "OK"`
   etc. — PU tokens in the author's own prose (procedure press-targets,
   non-quoting ER lines) become double-quoted labels, matching Arif rows
   44/45. Verbatim-quote ER segments (`... as defined by PUxxxx ...`) and
   `test_item` keep PU notation.
2. **Narrow the `popup-token` gate to the amended scope** and add the
   matching negative test.
3. Re-run lint → green.
4. write_back.py per Step 4, tests first; `--dry-run` diff summary reviewed
   by Pei before `--write`.

Priority/design-method distributions and the placeholder set
{055-03, 066, 070, 071} are confirmed against the review expectations.
A-H25 records the inherited "(more than 8)" speed constant.

## Step 3 — Lint (hard gate)

```bash
python scripts/lint_tcs.py generated/ --json-report lint_report.json
```

Exit 0 = clean, 1 = at least one finding, 2 = bad invocation. Authorities are
read, never hard-coded: `feature.yaml` supplies the column indices, input
paths and `lint.popup_ids`; the Design Method whitelist comes from the
workbook's own `下拉選單` sheet (9 strings, exact match).

Gates: `unknown-req-id`, `keys`, `blank-convention`, `blank-column`,
`priority`, `design-method`, `spec-reference`, `step-count`,
`step-numbering`, `forbidden-verb`, `er-modal`, `popup-unknown`,
`popup-citation`, `popup-verbatim`, `popup-token`, `br-tag`.

Home-specific rulings baked in, each because the Media version would fail
Arif's own compliant rows:

- **No `trailing-period` gate.** 28% of done-region lines end with a period,
  72% do not — measured, not a convention, so not a rule.
- **`[...]` / `<...>` are not banned** (A-H10). In Home they are Pop Up List
  control tokens (`<X>`, `[OK, X]`, `[Reorder]`, present in 20 done-region
  rows). They are validated against the cited PU row instead. `test_item` is
  exempt entirely — Profile §3.1 makes it verbatim RD text, and the RD writes
  `[X]` where the Pop Up List writes `<X>`.
- **ER modal check strips double-quoted spans first** (A-H08), so
  `"Widget cannot be moved here."` passes.
- test_group / test_set must be EMPTY (Profile §2).
- spec_reference must resolve through `spec_id_to_outline.tsv` AND agree with
  the 037 section for that req_id. B7 rows use the Last Mode List Item form
  (A-H03) and are checked against the List Item number instead.

Negative tests live in `tests/test_home_lint_tcs.py` — every gate has a test
that mutates one field and asserts the rule fires. A gate that never fires is
indistinguishable from a gate that does not exist.

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
4. Re-emit the B (`=ROW()-9`) formula on every data row. **Column F carries
   no formula in this workbook** — it is blank on all 229 rows, unlike Media
   where it holds a TC ID formula. Do not invent one.
5. Column mapping (1-based, verified): D=req_id, G/H=blank, I=test_item,
   J=pre_conditions, K=input_test_data, L=test_procedure, M=expected_result,
   N=spec_reference, O=`NEW`, P=priority, Q=design_method, R=`NA`,
   Z=author(`PeiPYHsu`), **AG=Remarks** (verified against header row 9 —
   Media's AH lesson: dropping it silently drops all BLOCKED/anomaly notes).
   **S–Y (vehicle flags) stay BLANK**: they are empty on all 229 existing
   rows, Arif's and draft alike. Media writes 1 there; copying that would
   introduce a value this workbook has never carried. C, E and F are likewise
   blank throughout.
6. Traceability / completeness invariants as Media, with one scoping change:
   every req_id ∈ 037 applies to **regen rows only** — Arif's rows 129–130
   trace to 035, which 037 omits (A-H06). Regen leaves == 62 exactly;
   ChangeHistory revision row appended; xlsx normalization for stable
   SHA256.
7. Do NOT touch Arif's 13 blank-priority rows (A-H05 — recorded, not fixed).
8. **Header block is preserved with ONE exception**: the 範圍 Scope field
   (A-H26) named another deliverable's workbook and is rewritten to the 037
   report's filename. The cell is found by its label text, never by a
   coordinate, so the same code serves AM/FM. Row 5 is outside the D..AG data
   range the content hash covers, so invariant 2 is unaffected — the hash is
   identical before and after (`b40e56826e7d7d84…`).

`scripts/write_back.py` implements this. Dry run by default; `--write`
produces `output/<source name>.xlsx` plus a `.sha256` sidecar, after
normalising zip timestamps and `dcterms` dates so the digest is reproducible.

One trap found while building it: build_remaining identifies the done region
as "author is non-empty", which is only true of the pristine workbook — after
write-back the regen rows carry `PeiPYHsu` too. The hash must select on
`done_region.author_value` instead, or the invariant compares the wrong set of
rows and fails on a correct write. `tests/test_home_write_back.py` pins this.

Tests: `tests/test_home_write_back.py` — segment assignment (including the two
leaves with no draft row), placeholder cell guards, the content-hash selector,
and an integration dry run asserting the hash, the leaf count, the segment
order and determinism.

## Step 5 — Delivery

Same as Media: lint_report → ANOMALIES review → release tag binding xlsx
SHA256 to commit → controlled document submission + RD-1 questions
(A-H01, A-H02, A-H03 version-label confirmation, A-H06 missing 035) to
upstream. RD-1 package: `docs/fw036/RD1_questions_home.md`.

**Status 2026-08-09: Step 4 COMPLETE (v2).**

| | |
|---|---|
| Workbook | `output/FM-WI-FSM-036-A01 … _Home_20260720.xlsx` |
| SHA256 | `cfc007f33c58ba77b07e46d07518f770b20bb07f4b826484b1eec2712e6dddd4` |
| Rows | 238 → 225; 72 regen TCs over 62 leaves (4 placeholder) |
| Done region | 144 Arif rows, hash `b40e56826e7d7d84…` unchanged |
| Tag | `fw036-home-regen-v2` — Home's first tag; the pre-A-H26 build was never tagged (`fw036-regen-v1` is Media's), its digest lives in ANOMALIES A-H26 |

v1 → v2 differs only in the A-H26 Scope correction and its ChangeHistory
sentence. No TC content changed.
