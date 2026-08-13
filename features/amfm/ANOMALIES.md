# ANOMALIES — FW036 AMFM HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-AMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.
File-supply gaps additionally get a row in `DATA_REQUESTS.md` — the anomaly
records the gap, that file asks for the data.

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

## [A-AM06] CFTS011 referenced but not in inputs — RESOLVED (file supplied, 2026-08-10)

- 9 leaves (`SWE-RA-RAD-087, 089–096`, Engineering Mode display / signal
  strength sampling) carry STLA ids `4942xxx` outside the CFTS024 anchor
  range. SYS3 SYSAD §4.4.2 c.3 explicitly attributes 4942534 to **CFTS011**
  (antenna connection status display).
- **Resolution**: Pei supplied `R1LR_Atl-H_25PI3.5_Activation and
  Configuration_CFTS_011_Radio Engineering Mode_SR26_20250909-1658.docx`
  (2026-08-10, via Project files). Title confirms the attribution (Radio
  Engineering Mode); all 7 unique declared ids verified present
  (4942534/36/38/40/42/43/45). Residual: original docx to be copied into
  `AMFMHMI/inputs/` for pipeline access + delivery hash-binding;
  batch-time consistency pass over the 9 leaves at Engineering Mode batch.

## [A-AM07] CFTS004 attribution is assumed, file absent — RESOLVED (file supplied, attribution confirmed, 2026-08-10)

- 8 leaves (`SWE-RA-RAD-097–104`, Diagnostic DIDs) carry STLA ids
  `4939xxx`/`4940xxx` outside CFTS024. Attribution to CFTS004 was inferred
  from SYS3's reference list.
- **Resolution**: Pei supplied `R1LR_Atl-H_25PI3.5_Activation and
  Configuration_CFTS_004_General Diagnostic Requirements_SR26_20250909-1658.docx`
  (2026-08-10, via Project files). All 8 declared ids verified present
  (4939808/09/22/46/49, 4940333/34/37) — attribution CONFIRMED; the
  `[ASSUMPTION A-AM07]` marker is no longer required on generated TCs
  (profile §3.5 updated).
- Version note: SYS3 cites `26PI1.5 Mar Release … 20260310-1509` (newer);
  supplied file is `25PI3.5 SR26 20250909` (older). Ids match; per-clause
  wording check at Diagnostics batch; if a delta shows, re-request the
  Mar release.
- Residual: original docx into `AMFMHMI/inputs/`; the supplied per-
  requirement attachment `4874050_4595376_CFTSMV024_CIP_R3_O1965_Excel_
  Document.xls` (a DTC definition table, Vehicle Configuration Mismatch)
  also serves this batch.

## [A-AM08] 037-internal duplicate STLA ids and numbering gaps — PARTIALLY RESOLVED (028/029 per R9; three pairs pending per-pair review)

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

### Per-pair disposition — RULED (R14-C4, Pei, 2026-08-13)

All three pairs ruled. **No TC is removed; the delivered v1 is unchanged.**

| pair | ruling | status |
|---|---|---|
| 087 / 094 | 維持雙 TC (R14-C4-a) | **CLOSED** |
| 089 / 095 | 維持現況，不動 v1 (R14-C4-b) | **deferred to upstream** |
| 090 / 096 | 改分類 — 非 `duplicate_of` 議題 (R14-C4-c) | **moved out of A-AM08's ruling scope** |

- **087 / 094 — CLOSED.** `CFTS011-4942534` enumerates the connected /
  not-connected value classes. 087 verifies the four information items
  displayed in the normal state (Functional); 094 verifies the
  not-connected value class and the frequency field following a retune
  (EP). That is the §8.3 negative / value-class axis, so the two TCs are a
  real split rather than a manufactured difference. The earlier reading —
  「087 untagged vs 094 `(Engineering Mode)`」 — was a tag observation, not
  the axis that actually separates them.
- **089 / 095 — deferred, v1 untouched.** The split is itself sound under
  §8.2.2: `4942540` binds the input-sampling side and the display-update
  side, and those fail independently. But it is inconsistent with 090/096,
  which §5.7 keeps as one TC each. **The root of the inconsistency is
  upstream, not here**: the 037 allocates TWO leaves to the MW clause and
  ONE each to AM and FM. Any change on either side forces a re-issue of
  the already-tagged v1, and the correct cut depends on the upstream
  answer — so it is asked (R14-C4-d → Q-AM2 item 5) and the depth is
  unified in v2 once answered.
- **090 / 096 — out of scope for this anomaly's ruling.** Both carry an
  empty `duplicate_of`, their clause ids differ (AM `4942536` /
  FM `4942545`), and they sit on different bands' leaves — §8.2.1 forbids
  merging across leaves, so there is nothing to rule on the TC side. Moved
  to RD-1 Q-AM2 item 3 as FYI and removed from PLAYBOOK §6's per-pair
  ruling item.

**A-AM08 residual is now 087/094 and 089/095 only** (087/094 closed;
089/095 awaiting upstream). 028/029 remain RESOLVED per R9 below.

### 028 / 029 — RESOLVED (R9, Pei, 2026-08-10)

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

Nothing was corrected at registration time: R7-Q4 leaves each pair to Pei.
**R9 (2026-08-10) rules it**: 029 spec_reference = `CFTS024-4872457`; the
pair is reclassified from duplicate to upstream id-tail typo; RD-1 Q-AM2
reports the 037 defect. `build_stla_map.py` gets a declared-id override
for 029 (Claude Code side). The other three
pairs (087/094, 089/095, 090/096) do not trigger the check — their declared
ids match their own clauses, so they are genuine same-id variants rather than
copy errors; they stay PENDING for per-pair review at their batches.

## [A-AM09] The 037 titles drop clauses the CFTS spec carries — RESOLVED (R8 + file supply + §8.6, 2026-08-10)

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
- **Resolution (2026-08-10), per class**:
  - VR Command → **R8 (verbatim: 「不進去了」)**: out of scope for this
    workbook; 003/009/025/027 test the HU HMI main path only; delegation
    to CFTS028 noted in each TC's reasoning
  - Pointers → file supply completed/located (see `DATA_REQUESTS.md`):
    CIP_Radio_Tables v6.7 + CFTS019 + Pop Up List in `inputs/`; Market
    Config located; HMI L&F identity resolved (no standalone Radio deck)
  - Caveats → generate from the CFTS clause per §8.6 (proposed, unopposed);
    batch context carries the full clause text
  - (029) → **R9**: id-tail typo, spec_reference = `CFTS024-4872457`

## [A-AM10] CFTS clauses allocated to no leaf, absorbed by rule — RESOLVED-BY-RULE (R10-2, 2026-08-10)

- The 037-A03 allocates leaves against CFTS Description clauses but leaves
  some same-section Subsystem Functional Requirements unallocated. Known
  absorptions from the pilot (Tune, §1.3.4–1.3.6): `4872440`/`4872441`
  → leaf 025; `4872449`/`4872450` → leaf 027; `4872458` → leaf 029.
- **Full-corpus sweep done (2026-08-10)**: `build_stla_map.py` now emits
  `data/unallocated_clauses.json` — per used section, the claimed ids and
  every unallocated one with its `[Artifact Type:…] [ECU:…] [Radio:…]`
  scope tags and text, so a clause can be classified without reopening the
  docx. **95 unallocated clauses (91 SFR, 4 Description) across the 20
  sections the 037 uses.** This is the Q-AM3 attachment.

  | § | unallocated | claimed | section |
  |---|---|---|---|
  | 1.3.2 | 12 | 5 | Seek Down |
  | 1.3.1 | 11 | 6 | Seek Up |
  | 1.3.14 | 11 | 17 | Station List |
  | 1.3.13.1 | 10 | 3 | Traffic Announcements (TA) & PTY 31 |
  | 1.12.2.2.1 | 9 | 4 | Head unit Radio Configuration |
  | 1.3.4 / 1.3.5 / 1.3.6 | 6 / 6 / 5 | 2 / 2 / 2 | Tune Up / Down / Direct Number Input |
  | 1.3.13 | 5 | 8 | RDS/RBDS Features |
  | 1.3.3.2 | 4 | 1 | Browse Category- Genre |
  | 1.3.7 | 4 | 4 | Preset Select/Recall |
  | 1.3.8, 1.3.10, 1.3.11, 1.3.13.2 | 2 each | 5 / 3 / 3 / 1 | — |
  | 1.3, 1.3.3, 1.3.3.1, 1.12.1.3.1.5 | 1 each | 2 / 5 / 5 / 1 | — |
  | 1.3.12 | 0 | 6 | Enter or Item Select |

  Two things the distribution says. **Seek is the heaviest batch by
  absorption load** — §1.3.1 and §1.3.2 together carry 23 unallocated
  clauses against 11 claimed, so the R10-2 decision test runs more often
  there than anywhere else; that is where the rule earns or fails. And
  §1.3.12 at 0 shows the pattern is not uniform, so "the 037 always skips
  the SFRs" is not the right story to send upstream — the Q-AM3 wording
  should ask about the allocation policy, not assert a systematic omission.
- Absorption is not automatic: the ids in the table are candidates for the
  R10-2 decision test, not a to-do list. Signal-status clauses
  (`TGW_Src_Cab_Stat`) and `[ECU:ETM]` / `[Radio:noSys]`-scoped clauses are
  in the count and mostly fail the "elaborates the leaf's cited clause"
  half of the test.
- **Ruling R10-2**: absorption is legitimate iff (a) same spec section and
  (b) the clause elaborates the leaf's cited clause. On absorption:
  `[A-AM10]` marker in assumptions AND the absorbed id in
  `specification_reference` (multi-cite). Failing the test → coverage hole
  in reasoning + RD-1. Upstream notified via RD-1 Q-AM3 for
  acknowledgement or reallocation.

## [A-AM11] Rate-to-frequency-step mapping undefined — PENDING (upstream definition)

- CFTS024 `4872442` / `4872451` require the HU to increment/decrement
  "based on the rate recieved in the $ICS_KNOB2_VAL$ signal value"
  ([1 to 63]) but define no mapping from rate value to frequency steps.
- Generation (leaves 026/028, and 021 per R12-4) asserts a monotonic
  relation in ER (63 moves further than 1) rather than fabricating a step
  count (§8.4.1).
- Candidate RD-1 if a testable mapping is wanted; otherwise the monotonic
  assertion is the strongest spec-sourced check available. Marker
  `[A-AM11]` on affected TCs.

## [A-AM12] "Intelligent entry" is undefined beyond its two dependencies — PENDING

- `CFTS024-4872459` (leaf 030) requires intelligent entry "based on the market
  configuration and the current tuner mode" and defines neither the band plans
  nor what "intelligent" constrains (digit count? decimal placement? range
  rejection?).
- Pilot TCs 030-01 / 030-02 are written against the market configuration the
  tester holds rather than against literal frequencies, so nothing is
  invented, and the tuner-mode axis (FM vs AM) is taken from the requirement's
  own wording.
- Concrete band plans arrive with `SR24 R1 Market Configuration Table v1.6`
  (DATA_REQUESTS row 1b, now in `inputs/`) and are verified by the Market
  Configuration set, `SWE-RA-RAD-081–085`. Revisit 030's ER when that batch
  fixes the vocabulary. Not blocking.

## [A-AM13] Fast seek is specified but reaches no 037 leaf — PENDING (RD-1)

- `CFTS024-4872398` (Seek Up) and `CFTS024-4872416` (Seek Down) define a
  **fast seek** feature: a long press on the seek button advances continuously
  through the band rather than stopping on the next station. Neither is
  allocated to a 037 leaf, and neither passes the R10-2 absorption test —
  fast seek is a different trigger (long press) driving a different behaviour
  (continuous advance), not an elaboration of the short-press seek clause the
  leaves cite. Recorded as a coverage hole in the reasoning of leaves 003/009
  and raised here.
- The two clauses are also asymmetric: `4872416` states the threshold
  (`<Tpress>` greater than 500 milliseconds), `4872398` states none. A tester
  handed only `4872398` has no press duration to use.
- The `SEEK Cancel_Stop Transitions` worksheet carries a `Fast SEEK AM / MW /
  LW / FM` state row alongside the plain `SEEK` row, so the state exists in
  the companion spec too — this is a real feature, not stray prose.
- **Not covered by this workbook** unless a ruling says otherwise: with no
  leaf, generating TCs for it would invent coverage the 037 does not claim.
  RD-1 candidate (fold into Q-AM3): should fast seek have leaves, and is the
  500 ms threshold meant to apply in both directions?

## [A-AM14] Seek Up and Seek Down are not decomposed alike upstream — PENDING

- Seek Up has a dedicated leaf for the initiation behaviour —
  `SWE-RA-RAD-004` cites `4872384` "enter the Seek Up state and begin
  searching … starting at the next higher frequency". Seek Down has **no
  equivalent leaf**: `4872402` / `4872403` say the same for the downward
  direction and are unallocated.
- Consequence handled, not hidden: 009 absorbs `4872402` / `4872403` under
  R10-2 and cites them, so the behaviour is verified. But the two directions
  now have different leaf shapes — Seek Up spends two leaves (003 + 004) on
  what Seek Down spends one (009) — which a coverage reviewer comparing the
  two will notice.
- Same class as A-AM10 and reported with it (Q-AM3): the question upstream is
  the allocation policy, not this individual pair.

## [A-AM15] Cross-document citations use an id scheme no supplied file carries — RESOLVED-BY-RULE (R11, 2026-08-10)

- CFTS024 delegates behaviour to other documents with a short-id token:
  `{See CFTS019-718}` (§1.3.3, clause `4872420`, reached by
  **`SWE-RA-RAD-014`**), `{See CFTS028-1}` (§1.3.4/1.3.5/1.3.6 → 025/027/029),
  `{See CFTS024-605}` (§1.3.12 → 048), `{See CFTS024-707}` (§1.3.13 → 057).
  37 such tokens exist in the document.
- **The short ids resolve nowhere.** CFTS019's clauses are 7-digit
  (`486xxxx`); `718` is not among them, is in none of its 37 tables, and the
  same holds for CFTS024's citations of *itself* (`CFTS024-789`, `-605`).
  This is a foreign/legacy numbering, not the STLA anchor scheme — so no
  mechanical resolution is possible from the corpus we hold.
- Detection trap, now closed: the docx writes the token with non-breaking
  spaces inside it (`CFTS0\xa019-718`), so an ASCII pattern finds the two
  out-of-scope citations in §1.4.11/§1.5.12.1 and misses the one in §1.3.3
  that actually reaches a leaf.
- Handling: `build_stla_map.py` emits `data/cross_doc_citations.json` — every
  token, the clauses citing it, the leaves reached, and (where the cited
  document is in `inputs/`) ranked candidate clauses. `make_batch_context.py`
  puts this on the leaf as `cross_references`, carrying the R11 handling in
  words so the borrowed outcome is neither dropped nor silently adopted.
- **014 (Browse), in the batch about to run**: the scenario is this leaf's
  ("all presets deleted → access attempt"), the outcome is borrowed. Under R11
  the ER states the tone anchored to `CFTS019-718`; the tone's own definition
  (CFTS019 §1.3.2.6, candidates `4866062` / `4866060` / `4865971`) is not
  under test here.
- **Resolution (R11): cite-form, not absorption.** The token is cited verbatim
  as a second `specification_reference`; the ER states the borrowed outcome
  anchored to it (`as defined by CFTS019-718`); the cited document's own rule
  surface is not tested. No clause resolution is required, so the unresolvable
  short-id scheme stops being a blocker. `clause_citation_overrides` remains
  available (guarded by an evidence phrase) if a token is ever ruled onto a
  clause, but cite-form needs it for nothing.
- Still worth reporting upstream (RD-1): the citation scheme itself. CFTS024
  cites documents — and itself — with ids that appear in no released file, so
  no reader can follow a cross-reference mechanically.

## [A-AM16] The feature has no PLAYBOOK.md — RESOLVED (file written, 2026-08-11)

- The canon's entry-point convention is one `<Feature>/PLAYBOOK.md` per
  feature carrying the §6 status board. AMFM ran P0–P6 and reached a P7
  dry-run without one: `features/home/PLAYBOOK.md` and `features/sxm/PLAYBOOK.md`
  exist, `features/amfm/PLAYBOOK.md` did not. AMFM's directory was created before
  `new_feature.py` started copying the template.
- Consequence, and why it is registered rather than shrugged at: a handover
  reader had **no status board to read**. The run's state lived only in
  `RUNBOOK.md`, which is the feature-fact authority, not the operational
  entry point — so "which phase are we in, what is open, who rules it" had to
  be reconstructed from prose. Nothing generated is affected; the defect is in
  the entry surface, not the corpus.
- **Resolution**: `features/amfm/PLAYBOOK.md` written 2026-08-11 on the
  `features/home/PLAYBOOK.md` skeleton (§0–§4 the invariant sections, §5 the AMFM
  kickoff prompt, §6 the status board + Open PENDING). Content is taken from
  `RUNBOOK.md`, `ANOMALIES.md`, `DATA_REQUESTS.md` and
  `docs/fw036/RD1_questions_amfm.md` — nothing new is asserted. RUNBOOK stays
  the authority; PLAYBOOK §6 is maintained from it.

## [A-AM17] Two same-named, same-sized, byte-different O-attachments in `inputs/` — OPEN (registered per 下放包 01 §3.3, 2026-08-13)

- `features/amfm/inputs/` holds **two** files whose names differ only in the
  leading requirement id, and which are **identical in size but different in
  content**:

  | file | bytes | SHA256 (前 16) |
  |---|---|---|
  | `4874050- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls` | 37,376 | `55666213fdbef997` |
  | `4874049- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls` | 37,376 | `3fd31f9482b7d660` |

  量測條件：`stat -f%z` 取 bytes，`shasum -a 256` 取雜湊，對 `inputs/` 實際
  路徑實測（非沙箱副本）。
- **Why it is registered rather than explained**: 下放包 01 §3.3 required the
  coexistence be explained from existing records, else filed. A full-text
  scan of `features/amfm/` and `docs/fw036/` for `4874049` returns **zero
  hits outside this entry** — `DATA_REQUESTS.md` #2b and `A-AM07`'s residual
  note both name only `4874050`. **No record accounts for the second file.**
- **Why the pair is not benign on its face**: the two share a filename body
  (`4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls`) and an exact byte
  count, which reads as "the same attachment, cited from two requirements".
  But the hashes differ, so they are **not** the same attachment — and equal
  size with unequal content is the signature of a same-template, different-
  data pair, which is precisely the case where picking by filename picks
  wrong. This is the AMFM/SXM standing rule stated in Projection's
  `DATA_REQUESTS.md` §跨 feature 同源政策: 「檔名相同」不足以證明「內容相同」.
- **Consequence if unresolved**: R14-C3 marks `#2b` (the `4874050` DTC
  definition table) as 已入 `inputs/` and closes it. If the clause actually
  cited by the Diagnostics batch is the `4874049` one, the closure is
  attached to the wrong file. **Nothing generated is affected today** — the
  Diagnostics batch (097–104) is generated, lint green, zero placeholder,
  and neither file is read by any script; the exposure is to the audit
  trail, not the corpus.
- **Not disposed of here**: which of the two the requirement cites, and
  whether the other should stay, is a scope/source question — Tier 2/3.
  Execution layer registered and reported only.
- Related: `A-AM07` (CFTS004 attribution), `DATA_REQUESTS.md` `#2b` / `#2c`.

## [A-AM18] v1 交付件結構缺損 —— 21 個 zip 成員遺失、x14 dropdown 歸零 — **DEFERRED — 待 Pei 完成 Excel 實開驗證後決定交付時點（R18-2）**

**性質**：不是列內容缺陷。v1 的 301 列值全部正確、lint green、legacy
content hash 相符 —— 而交付出去的檔案已經不是客戶給的那個容器。
`openpyxl` 的 `Workbook.save()` 不是「存回讀進來的檔」，是「存出 openpyxl
能描述的檔」；凡在它物件模型之外的 zip 成員，一律丟棄或重建。

**量測**（`features/privacy/scripts/xlsx_roundtrip_probe.py`，執行層 2026-08-13 複現）：

| | 客戶原件 | v1（tag `fw036-amfm-regen-v1`）| v2（本次） |
|---|---|---|---|
| bytes | 136,004 | 171,631 | 153,485 |
| zip members | 59 | 48 | **59** |
| classic DV / x14 DV | 4 / 2 | 4 / **0** | 4 / **2** |
| SHA256 | `987cdead3775…` | `da18b5b0ca9e…` | `0daa6f29cecb…` |

v1 相對客戶原件 **lost 21 / added 10**：

```
LOST  xl/diagrams/{colors1,data1,drawing1,layout1,quickStyle1}.xml   ← SmartArt 整組
      xl/drawings/drawing7.xml + _rels/drawing7.xml.rels
      xl/printerSettings/printerSettings1..7.bin                     ← 列印設定
      xl/sharedStrings.xml, xl/calcChain.xml
      xl/comments1.xml, xl/drawings/vmlDrawing1.vml                  ← 舊式註解圖層
      xl/media/image2.jpeg
      xl/worksheets/_rels/sheet8.xml.rels, sheet9.xml.rels
ADDED xl/comments/comment1.xml, xl/drawings/commentsDrawing1.vml
      xl/media/image2.png（原 jpeg 重新編碼）, xl/media/image3..9.jpeg
```

**處置 —— 已裁（R18-2, Pei, 2026-08-13）**：

> v2 已產出，保留於 `output/`，**不打 tag、不送出、不再加工**。
> v1 tag `fw036-amfm-regen-v1` 維持不動。
> v2 附掛未驗標籤：**尚未經 Excel 實開驗證（R17-9）**，
> 交付前必須先由 Pei 完成該四點確認。時點由 Pei 決定。

v2 實測：zip 成員 59 = 59 零增零減、DV 4/2 完整保留、
TC 分頁逐格內容與 v1 **零差異**、lint PASS、連跑兩次 SHA256 相同
（`0daa6f29cecb…`）。

⚠️ **未驗標籤（R17-9，Tier 3，僅 Pei 可解）**：v2 的全部驗證都在程式層。
外科手術寫的是顯式 `<f>` 公式，而新增的 B243–B310 不在被逐 byte 保留的
`calcChain.xml` 內。Excel 通常會靜默重建，但這是推論不是實測。
交付前需人在 Excel 開啟 v2，確認：(a) 無「修復」提示、(b) R/P/AE 下拉可用、
(c) SmartArt 在、(d) 列印設定在。**此四點未完成前，v2 不得送出。**

狀態為 `DEFERRED` 而非 `PENDING`（R15-2）—— 已裁，等待對象是
Pei 的 Excel 實開驗證，不是等待裁決。

**§5a 教訓（R16-5）**：lint green 與內容 hash 相符，證明不了交付件結構完整。
前者量列內容，後者量 zip 結構，兩者正交。R14-C1 之 P7 追認即在此盲區內做出
——當時所驗七項數值全對，而交付件已缺 21 個 zip 成員。追認不撤回
（列內容確實正確），但其結論之涵蓋範圍加註本限制。

**相關**：R16 全文見 `RULINGS.md`；跨 feature 檢測結果見
`docs/upstream/02_integrity.md` §4；Home `A-H27`、SXM `A-SX01`、
Privacy `A-PV09`、Projection 對照組。

## [A-AM19] 交付件第 243–310 列無儲存格樣式 — **DEFERRED — 待下次內容變動時一併處理（R18-5）**

客戶原件的 template tail 只到第 242 列（`<row r="242" spans="2:33" s="154"
customFormat="1">`，各格帶 `s=` 樣式索引）。第 243 列起在原件中**不存在**，
是寫回時新建的列，因此沒有列樣式、格內也沒有 `s=` 屬性：

```
原件 row 242 : <row r="242" spans="2:33" s="154" customFormat="1">
                 <c r="B242" s="133" t="str">…  ← 帶樣式
v1/v2 row 243: <row r="243">
                 <c r="B243">…                  ← 無樣式
```

**影響**：交付件下半部 68 列（243–310，即 143 筆 regen 中的後 68 筆）
沒有框線與儲存格格式。內容正確，僅外觀不一致。

**這不是 R16 結構缺損所致。** 已逐列比對確認 **v1 與 v2 皆然** ——
v1 是 openpyxl `insert_rows()` 不複製樣式，v2 是外科手術路徑刻意沿用
v1 行為以保證「只換寫回方法、不夾帶內容變動」（下放包 02 §3.3）。
兩者同因不同路徑，是一個獨立於 R16 的既有缺陷。

**處置 —— 已裁（R18-5, Pei, 2026-08-13）**：

> 登記為 anomaly，**不修**。v1、v2 皆然，非結構缺損所致。
> 狀態 DEFERRED — 待下次內容變動時一併處理。

修復方向（記錄備用，不實作）：新建列時自最後一個 template 列
（第 242 列）繼承 `<row>` 屬性與各欄 `s=` 索引。屬外觀改動，
會改變交付件位元內容，故不宜與「只換寫回方法」的 v2 混在一起做。

⚠️ **修復方向未實測，日後採用前須先驗證（R19-5）**。上述做法是讀 sheet XML
後的紙上推論，**未寫過一行程式驗證**。特別未驗者：`s=` 索引跨列沿用是否
對所有欄都成立（第 242 列本身是 template tail 的最後一列，其樣式未必等同
資料列的常態樣式）、以及新增 `<row>` 屬性後 `spans` 與 `customFormat`
是否需同步。依 canon「檢查項須確認其在該階段確實可能失敗；不可能失敗者
標『未實測』而非 PASS」之同一精神，推論型處置建議同樣不得以「已有方向」
充作「已驗可行」。

**相關**：A-AM18；`RULINGS.md` R18-5；`docs/upstream/02_integrity.md` §7 末段。

## Assumption markers

None registered beyond the above. Inline format in generated JSON
reasoning/assumptions: `[ASSUMPTION A-AMnn]` or `[A-AMnn]`.
