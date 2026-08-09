# ANOMALIES — FW036 AMFM HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-AMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

## [A-AM01] Workbook Scope names the superseded requirement report — RESOLVED (R1/C1 + R6, 2026-08-09)

- Header cell `D5` (label `範圍 Scope` at `C5`) reads `FM-WI-SW-RAD-SWRA-A02`.
  Under ruling R1 that report is superseded; the field should name the
  037-A03. Identical defect class to Home A-H26, found in the same week —
  the field is hand-maintained upstream and has now been wrong in both
  instances the pipeline has looked at.
- Blocks nothing before write-back. `write_back.py` already corrects this
  field by label text (`write_back.scope_label`), so the fix is configuration,
  not code: set `write_back.scope_source` once the correct value is ruled.
- Proposed: correct to the 037-A03 filename stem, exactly as Home A-H26.
  Recorded as RULINGS C1.
- **Resolution**: fix at write-back via configuration — `write_back.scope_label:
  "範圍 Scope"` + `scope_source: "a03_report"` added to feature.yaml
  (2026-08-09). No code change.

## [A-AM02] The workbook covers none of the ruled requirement source — RESOLVED (R4, 2026-08-09)

- Recon (2026-08-09): the workbook holds **158 authored rows, all by
  `Wilson`, zero drafts** — `workbook_state = FULL`. Against the ruled source
  it covers **0 of 102** leaves; every row traces one of **57** `SWE-RAD-*`
  req_ids that the 037-A03 does not contain.
- "FULL" is therefore a statement about draft rows, not about done-ness. The
  canon's state machine cannot express this case; RECON.md names it in its
  own section rather than inventing a state.
- This is RULINGS C2. **Resolution — R4: 選項 (i)，凍結為 legacy region**，
  excluded from coverage/traceability invariants; RD-1 attached (see R4).
- Style note that survives any C2a outcome: those 158 rows are the workbook's
  only style precedent (test_group `Radio`, test_set `FM & AM`, tc_id
  `newR1L-Radio-nnn`, spec_reference `CFTS024-<id>`). Style may be borrowed
  from rows whose traceability is not adopted.

## [A-AM03] The two requirement families ARE related — RESOLVED (evidence consumed by R4)

- RULINGS C2a(iii) assumed "the two sets describe DIFFERENT content (user
  functions vs system behaviors), so a clean mapping is unlikely". Measured,
  that assumption does not hold in the form stated.
- **The 037-A03's `Requirement Title` column carries the SWRA-A02's
  `Requirement Description` text, frequently verbatim.** Comparing
  title-to-title finds zero matches and would have confirmed the assumption;
  the alignment axis had to be discovered, not chosen. Reproduce with
  `scripts/compare_req_families.py`; full output in `docs/family_overlap.md`.

  | | count | of |
  |---|---|---|
  | 037-A03 leaves with a near-verbatim ancestor (≥0.85) | **35** | 102 |
  | 037-A03 leaves with a plausible ancestor (0.60–0.85) | 6 | 102 |
  | 037-A03 leaves with no ancestor — new work | **61** | 102 |
  | SWRA-A02 rows with a near-verbatim descendant | 35 | 57 |
  | SWRA-A02 rows represented only by a paraphrase | 4 | 57 |
  | SWRA-A02 rows represented nowhere | **18** | 57 |

  The 35 strong matches consume 35 distinct SWRA-A02 rows — a **1:1** shape,
  not many-to-one.
- What this does and does not support: a re-trace under C2a(iii) is
  *mechanically screenable* for about a third of the leaves and would be
  1:1 where it applies. It is **not** a mapping — similarity is difflib on
  folded text, every pair needs human confirmation, and 61 leaves have no
  ancestor at all, so no C2a option avoids generating the majority from
  scratch.
- Registration is Tier 1. **Resolution**: evidence consumed by R4; re-map
  (iii) rejected — RD work, not TC-author work (§8.2), and 61/102 need
  generation from scratch regardless.

## [A-AM04] 18 SWRA-A02 requirements are represented nowhere — RESOLVED-CONDITIONAL (R5, 2026-08-09)

- Under R1 these lose their coverage claim in this workbook:
  `SWE-RAD-001-01`…`-06`, `SWE-RAD-040`, `040-001`…`-003`, `SWE-RAD-041`,
  `041-001`…`-003`, `SWE-RAD-042`, `043`, `044`, `045`.
- **The drop is not scattered.** It is a contiguous tail (`SWE-RAD-040`
  through `-045`, with their sub-items) plus the sub-decomposition of
  `SWE-RAD-001` — whose parent *is* represented, by `SWE-RA-RAD-014`
  (paraphrase, 0.764). A contiguous tail reads more like a report authored
  against an earlier revision, or a deferred block, than like 18 independent
  deletions. That is the sharper RD-1 question.
- Safety exposure is bounded and measurable: the SWRA-A02 is the only file in
  the corpus carrying `ASIL Level` / `FTTI`, and **all 57 rows are ASIL `QM`
  with FTTI `NA`**. R1 therefore drops no ASIL-rated requirement; what is
  lost is the record that these were assessed as QM.
- The 037-A03 carries **no ASIL/FTTI column at all**, so the SYS2/SYSRA
  safety-analysis layer has no attachment point on the ruled leaves and does
  not enter the trace chain (recorded as a `[PROPOSED]` in DECISIONS §3).
- **Resolution — R5 (verbatim): 「確認本 workbook 不承擔其覆蓋」.** Disposition
  question merged into the R4 RD-1 (`docs/fw036/RD1_questions_amfm.md`);
  closes fully when the RD-1 reply arrives or delivery deadline passes,
  whichever first.

## [A-AM05] feature.yaml priors disagree with the workbook — RESOLVED (R3, 2026-08-09)

- `done_region.author_value: Arif` (template residue from Home) matches **0**
  rows; the workbook's author is `Wilson` ×158. Recon surveyed with the
  detected value and raised it as `[PROPOSED]`.
- `columns.remarks: AH` disagrees with the header, which puts Remarks at
  `AG`. Media is the instance recorded as using `AH`; this one does not.
- Both are one-line corrections but neither is applied here: a done-region
  selector and a write-back column map are exactly the values that must be
  signed rather than inferred. See DECISIONS §2.
- **Resolution — signed (R3)**: `author_value: Wilson` (selects the frozen
  legacy region per R4), `remarks: AG` (header text is authority). Applied
  to feature.yaml 2026-08-09. Authorship principle recorded verbatim in R3.

## [A-AM06] CFTS011 referenced but not in inputs — PENDING (file supply)

- 9 leaves (`SWE-RA-RAD-087, 089–096`, Engineering Mode display / signal
  strength sampling) carry STLA ids `4942xxx` outside the CFTS024 anchor
  range. SYS3 SYSAD §4.4.2 c.3 explicitly attributes 4942534 to **CFTS011**
  (antenna connection status display) — the doc association is evidenced,
  the file is absent from `inputs/`.
- NOT blocking (R7-Q3): the 037 titles carry self-contained requirement
  text (blocked-parent proportion test). spec_reference `CFTS011-{id}` is
  written now; content verification against the CFTS011 text happens when
  Pei supplies the file. Verify Engineering Mode entry conditions (§3.2 of
  the profile) at that point.
- Resolution condition: CFTS011 file lands in `inputs/` and a consistency
  pass over the 9 leaves finds no wording conflict.

## [A-AM07] CFTS004 attribution is assumed, file absent — PENDING (file supply)

- 8 leaves (`SWE-RA-RAD-097–104`, Diagnostic DIDs) carry STLA ids
  `4939xxx`/`4940xxx` outside CFTS024. SYS3's reference list names
  `CFTS_004_General Diagnostic Requirements` — attribution is INFERRED,
  not evidenced per-id (unlike A-AM06).
- spec_reference `CFTS004-{id}` is written with `[ASSUMPTION A-AM07]` in
  the reasoning of every affected TC until the file confirms.
- NOT blocking (R7-Q3, same proportion test). Resolution condition: CFTS004
  file lands in `inputs/`, attribution confirmed or corrected per id.

## [A-AM08] 037-internal duplicate STLA ids and numbering gaps — PENDING (per-pair, Pei)

- Duplicate source ids inside the 037-A03:
  - 087 / 094 share `4942534` (087 lacks the `(Engineering Mode)` tag,
    094 carries it — possibly normal-display vs Engineering-Mode variants)
  - 089 / 095 share `4942540` (same pattern: 089 untagged, 095 tagged)
  - 090 / 096 near-identical text, distinct ids (`4942536` / `4942545`)
  - 028 / 029 share `4872451` (028 = ICS tune-down signal, 029 = Tune to
    a specific frequency — likely a copy error in one title's id tail)
- Numbering gaps: `086`, `088` absent from the 037's own sequence.
- Ruling R7-Q4 (verbatim): 「重複就是重複 但要標注起來我會自行判斷」 — each
  leaf still gets its own TC (§8.2, no consolidation); generation marks
  each affected TC's reasoning with `[A-AM08]` and states
  `duplicate_of`/`distinguishing_axis` honestly; Pei rules per pair at
  pilot/batch review.
- Candidate RD-1 material if review confirms true duplicates.

### 028 / 029 — resolved as evidence, awaiting Pei's per-pair call

Phase 4 turned this pair from "likely a copy error in one title's id tail"
into a measurement. Every CFTS024 requirement paragraph carries its own id, so
each leaf's declared id can be checked against the clause the leaf actually
describes (`build_stla_map.py`, `verify_ids`; output
`data/stla_id_suspects.json`):

| leaf | declared id | agreement with it | best-matching id | agreement |
|---|---|---|---|---|
| `SWE-RA-RAD-028` | 4872451 | **0.897** | 4872451 (itself) | 0.897 |
| `SWE-RA-RAD-029` | 4872451 | **0.036** | **4872457** | **0.909** |

028 is correct. 029's title describes *Tune by Direct Number Input* — CFTS024
§1.3.6 `{4872456}`, clause `4872457` — not the ICS-knob tune-down clause its
id points at. So the copy error is in **029**, and the pair is not a duplicate
requirement at all.

Consequence if unruled: 029 ships `spec_reference = CFTS024-4872451`, citing a
clause about a different function — a traceability defect, not a wording one.
The proposed correction is `CFTS024-4872457`. It does not move 029 between
batches (Tune already spans §1.3.4–1.3.6).

Nothing is corrected here: R7-Q4 leaves each pair to Pei. The other three
pairs (087/094, 089/095, 090/096) do not trigger the check — their declared
ids match their own clauses, so they are genuine same-id variants rather than
copy errors.

## [A-AM09] The 037 titles drop clauses the CFTS spec carries — PENDING

- The 037 title is meant to quote the CFTS clause verbatim, and for 65 of the
  85 in-corpus leaves it does. **20 diverge**, measured at context-build time
  (`make_batch_context.py` emits `wording_agreement` per leaf and warns).
  The divergence is one-directional — the CFTS says more — and falls into
  three classes:

  | class | n | what the 037 dropped |
  |---|---|---|
  | VR Command trigger | 4 | `or a VR Command` + the CFTS028 cross-reference (003, 009, 025, 027) |
  | Pointers to other documents | ~9 | `See 'CIP_Radio_Tables*' … worksheet`, `See HMI logic & flow documents`, `Refer to CFTS024-707`, `{See CFTS019-718}` |
  | Substantive caveats | ~6 | e.g. 020 `Note: This information may not be available in AM mode.`; 026/028 `(Example: … shall not be executed if HU is in browse screen)`; 061 disc-mode condition |
  | (029) | 1 | not a divergence — a wrong id, see A-AM08 |

- Why each class matters differently:
  - **VR Command** is a *trigger path* the spec grants and the 037 omits. If
    it is in scope, four leaves need an extra procedure path; if VR belongs to
    CFTS028's own deliverable, the 037's omission is correct scoping. Profile
    §8.6 says the source spec wins on wording, which as written would pull VR
    in — this is the case where that rule needs a scope answer, not a wording
    answer.
  - **Pointers** name documents not in `inputs/` (`CIP_Radio_Tables`,
    CFTS019, HMI logic & flow). They are the same class as A-AM06/A-AM07:
    file supply, not ambiguity. `CIP_Radio_Tables` is cited for SEEK
    cancel/stop transitions on leaves 005/006/010/011 — a state table, which
    is exactly the content a State Transition TC would need.
  - **Caveats** are behaviour and belong in the TCs. These need no ruling;
    generation reads the CFTS clause, which the batch context now carries in
    full alongside the 037 title.
- Proposed: generate from the CFTS clause (§8.6) for the caveat class; hold
  the four VR leaves' extra path until Pei answers the scope question; request
  `CIP_Radio_Tables` if State Transition coverage for SEEK is wanted.
- Per-leaf agreement scores are in each `batches/*.json`.

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-AMnn]`.
