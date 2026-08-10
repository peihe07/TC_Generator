# FW036 AMFM HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to AMFM.

**Standing convention — data-request reminder (Pei, 2026-08-09)**: at every
session opener (「接手」) and at every batch gate, report the outstanding
rows of `DATA_REQUESTS.md` (by Urgency) and which upcoming batches the
missing files degrade or block. A batch gate summary that omits this check
is incomplete. When a requested file lands in `inputs/`, mark its row
supplied and advance the linked anomaly.

## Phase 0 — Intake
- [x] Source files placed in `inputs/` (workbook, 037, spec, popup list)
- [x] spec_mode classified: D  (FEATURE_ONBOARDING §3)
- [x] `feature.yaml` filled from `docs/fw036/templates/feature.yaml`

## Phase 1 — Recon (Tier 1, fully delegable)
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [x] workbook_state: FULL (against ruled source: effectively BLANK — R4)
- [x] Coverage: 102 leaves total / 0 done / 102 regen targets

## Phase 2 — Rulings (Tier 2)
- [x] DECISIONS.md signed by Pei (2026-08-09; RULINGS R3–R6)

## Phase 3 — Framework & profile (Tier 2)
- [x] `docs/fw036/framework.md` Part III appended (11 capability Test Sets,
      102/102 leaves allocated; R7-Q1/Q2)
- [x] `docs/runtime/profiles/FW036_R1L_AMFM_Profile.md` written (R7)

## Phase 4 — Data build (Tier 1) — DONE 2026-08-09

```bash
python AMFMHMI/scripts/build_stla_map.py --feature-dir AMFMHMI --check-batches
python AMFMHMI/scripts/extract_exemplars.py --feature-dir AMFMHMI
python AMFMHMI/scripts/make_batch_context.py --feature-dir AMFMHMI --pilot
python AMFMHMI/scripts/make_batch_context.py --feature-dir AMFMHMI --batch "<name>"
```

- [x] `data/stla_to_cfts.{json,tsv}` — the bracket map, now a script product
- [x] `data/exemplars.json` — Wilson style-only anchors
- [x] `batches/*.json` — all 11 batch contexts
- [x] Misses filed: A-AM08 (029's id), A-AM09 (037 title vs CFTS wording)

### What the map is and what it checks

Every 037 Requirement Title ends with its source STLA id; every CFTS024
heading and every CFTS024 requirement paragraph carries the same id family.
So a leaf resolves twice over: the **bracket** (largest heading anchor not
exceeding the id) gives its section, and the **paragraph anchor** gives its
exact clause. All 85 in-corpus leaves reach paragraph resolution; the 17
external-doc leaves resolve by the R7-Q3 allocation instead.

Three checks run on every build, each because the failure it catches is
silent:

| check | what it stops |
|---|---|
| every leaf must yield exactly one STLA id | full-width brackets `（…）` on 087/097 read as "untagged"; a partial map ships leaves with no spec_reference |
| ruled external allocation == measured out-of-range set | a bracket lookup pins every out-of-range id to the document's last section, resolving perfectly and wrongly |
| declared id must match the clause the leaf describes | a mistyped id tail resolves perfectly to the wrong clause — found `029` (A-AM08) |

Plus `--check-batches`: every leaf must bracket into a section its Test Set
declares in `docs/batches-amfm.md`. This makes the Phase 3 Part III table a
checked claim rather than an assertion — it currently passes 102/102.

### Conventions carried into the batch context

`column_conventions` is emitted as data, not left to the exemplars, because
the legacy rows contradict the rules: they write Test Group `Radio` and a
band-based Test Set, and R7-Q1/Q2 replaced both for new rows. Exemplars are
stripped of `req_id`, `spec_reference`, `test_group`, `test_set` and carry
`style_only` plus the reason each field was withheld (R4: borrow style, not
traceability).

## Phase 5 — Pilot (Tier 2)

- [x] Pre-conditions cleared: R8 (VR out of scope) and R9 (029 →
      `CFTS024-4872457`) signed 2026-08-10; the R9 correction is implemented as
      a **ruled** `stla_id_overrides` entry in `feature.yaml`, re-measured on
      every build (see below)
- [x] Pilot generated 2026-08-10: **Tuner Availability (001–002) + Tune
      (025–030) = 8 leaves → 13 TCs**, `generated/SWE-RA-RAD-0*.json`
- [x] → Pei review 2026-08-10 → **PASS with corrections (R10)**; corrections
      applied and lint green the same day. Gate closed.

| Leaf | TCs | Split axis | Priority | Design method |
|---|---|---|---|---|
| 001 | 1 | — | P1 | EP |
| 002 | 1 | — | P1 | EP |
| 025 | 2 | boundary (mid-band / band upper end) | P1, P1 | Functional, BVA |
| 026 | 2 | trigger_state (playing page / browse list) | P1, P2 | BVA, Decision Table |
| 027 | 2 | boundary (mid-band / band lower end) | P1, P1 | Functional, BVA |
| 028 | 2 | trigger_state (playing page / browse list) | P1, P2 | BVA, Decision Table |
| 029 | 1 | — | P1 | Functional |
| 030 | 2 | mode (FM / AM tuner mode) | P2, P2 | EP, EP |

Mechanical self-check clean: 13/13 TCs have ≥2 steps with 1:1 ER alignment, no
trailing periods, no modals in ER or tc_title, design methods exact-matched
against 下拉選單, spec_reference equal to the STLA map, no stray square
brackets outside source-quoted `$SIGNAL$ = [value]`, no duplicate tc_title.
(AMFM has no `lint_tcs.py` yet — that is Phase 6.)

### Declared-id overrides are ruled, and re-checked

`stla_id_overrides` in `feature.yaml` carries R9's correction with its
evidence. `build_stla_map.py` refuses an override that stops being true of the
files — if the 037 is reissued with a different declared id, or the corrected
clause no longer matches the leaf better than the declared one, the build
aborts instead of silently re-pointing a citation. Current run:
`SWE-RA-RAD-029 4872451 -> 4872457 (R9); agreement 0.036 -> 0.909`.

### R10 corrections applied (2026-08-10)

| Item | Change |
|---|---|
| 025-01, 025-02 | multi-cite `CFTS024-4872439; CFTS024-4872440` / `…; CFTS024-4872441`; Remarks cleared |
| 027-01, 027-02 | multi-cite `CFTS024-4872448; CFTS024-4872449` / `…; CFTS024-4872450`; Remarks cleared |
| 029 | multi-cite `CFTS024-4872457; CFTS024-4872458`; Remarks rewritten in external language |
| 026-02, 028-02 | Remarks cleared — the cited clause carries the suppression wording |
| 001 | step 5 ER softened to `The seek executes` (stop-on-station detail belongs to the Seek leaves) |

**The work order listed three multi-cites; the gate found five.** 025-01 and
027-01 also absorb a clause — their ER verifies "the tuned frequency is the
next higher/lower frequency in the band and that station is played", which is
`4872440` / `4872449`, not the Description clause they cited. Caught by
`absorption-cite` keying on the ids the `[A-AM10]` marker names rather than on
a citation count.

Citation separator for multi-cite is `"; "` (most-specific first, §10.7).
No legacy precedent exists — every Wilson row cites one clause — so this is a
pilot decision, cheap to change before the Seek batch.

### Phase 3 lint (`scripts/lint_tcs.py`, new 2026-08-10)

```bash
python AMFMHMI/scripts/lint_tcs.py --feature-dir AMFMHMI --json-report lint_report.json
```

Exit 0 = clean, 1 = findings. Authorities are read, never hard-coded: Test
Group and the spec_reference template from `feature.yaml`, the design-method
vocabulary from the workbook's own `下拉選單`, the legal clause ids from
`data/stla_to_cfts.json`. Gates: `step-count`, `er-alignment`,
`trailing-period`, `square-bracket` (source-quoted `$SIGNAL$ = [value]`
exempt), `er-modal`, `title-modal`, `title-length`, `priority`,
`design-method`, `test-group`, `test-set`, `spec-reference`,
`unknown-req-id`, `sibling-distinction`, `distinguishing-axis`, `reasoning`,
plus the two R10 gates:

- **`absorption-cite` (R10-2a)** — every clause id an `[A-AM10]` assumption
  names must be cited by some TC under that leaf, and a multi-cite must be
  explained by such an assumption
- **`remarks-internal` (R10-4)** — Remarks must not contain `R\d` / `A-AM\d\d`
  internal identifiers; `R1L`, the program name, is deliberately not matched

`tests/test_amfm_lint_tcs.py` mutates one field per gate and asserts it fires,
plus an integration test pinning the shipped pilot at 13 TCs clean.

### Review points this pilot deliberately raises

1. **EP vs Functional on 001/002.** The two leaves are the two equivalence
   classes of `$AM_Presence$`; each TC exercises one. Assigned EP on that
   reading. If the house reading is "one condition, one feature check", both
   become Functional — a one-line change across the corpus's configuration
   gates, so it is worth settling at the pilot.
2. **Folding unallocated CFTS clauses into the leaf they elaborate** (A-AM10).
   025-02 / 027-02 are wrap-around TCs sourced from `4872441` / `4872450`,
   which the 037 allocated to no leaf. Profile §4 authorises this for
   wrap-around specifically; the pilot generalises it. If that generalisation
   is not wanted, those two TCs come out and the behaviour goes to RD-1.
3. **Splitting the suppression branch** (026-02 / 028-02). The
   "not executed if HU is in a browse screen" clause is in the CFTS and absent
   from the 037 title (A-AM09 caveat class, §8.6). Generated as its own TC at
   P2; alternatively it collapses into an extra ER line on the main TC.
4. **029's Remarks** carries the R9 correction note. Confirm that is the right
   place for a ruled upstream correction versus leaving Remarks empty and
   keeping the record in ANOMALIES only.

## Phase 6 — Batch generation (Tier 1)

- [x] **Seek** (003–013, 11 leaves → 22 TCs), 2026-08-10, lint green
- [x] **Browse** (014–024, 11 leaves → 17 TCs), 2026-08-10, lint green —
      first batch under R11 cite-form (014-02)
- [x] **Presets** (031–039, 9 leaves → 13 TCs), 2026-08-10, lint green
- [x] **List Navigation** (040–051, 12 leaves → 16 TCs), 2026-08-10, lint green
- [x] **RDS Features** (052–063, 12 leaves → 17 TCs), 2026-08-10, lint green
- [x] **Station List** (064–080, 17 leaves → 22 TCs), 2026-08-10, lint green
- [x] **Market Configuration** (081–085, 5 leaves → 6 TCs), 2026-08-10, lint green
- [x] **Engineering Mode** (087, 089–096, 9 leaves → 9 TCs), 2026-08-10, lint green
- [x] **Diagnostics** (097–104, 8 leaves → 8 TCs), 2026-08-10, lint green
- [x] **ALL 102 LEAVES GENERATED — 143 TCs, lint green, no leaf without a file**
- [ ] write-back invariants pass

| Batch | Leaves | TCs | P0/P1/P2/P3 | Design methods |
|---|---|---|---|---|
| Tuner Availability + Tune (pilot) | 8 | 13 | 0/8/5/0 | Functional 3, EP 4, BVA 4, Decision Table 2 |
| Seek | 11 | 22 | 0/19/3/0 | Decision Table 8, State Transition 5, Functional 4, BVA 4, EP 1 |
| Browse | 11 | 17 | 0/15/2/0 | Functional 8, EP 8, BVA 1 |
| Presets | 9 | 13 | 0/13/0/0 | Functional 7, BVA 3, EP 2, Decision Table 1 |
| List Navigation | 12 | 16 | 0/16/0/0 | Functional 9, BVA 4, State Transition 2, EP 1 |
| RDS Features | 12 | 17 | 0/15/2/0 | Functional 9, EP 3, State Transition 2, Decision Table 2, Scenario 1 |
| Station List | 17 | 22 | 0/21/1/0 | Functional 12, BVA 4, EP 4, State Transition 1, Decision Table 1 |
| Market Configuration | 5 | 6 | 0/6/0/0 | EP 2, Functional 2, State Transition 1, BVA 1 |
| Engineering Mode | 9 | 9 | 0/9/0/0 | Functional 4, BVA 4, EP 1 |
| Diagnostics | 8 | 8 | 0/6/2/0 | Functional 5, EP 3 |
| **TOTAL** | **102** | **143** | **0/129/14/0** | Functional 63, EP 29, BVA 25, Decision Table 14, State Transition 11, Scenario 1 |

### Spec tables are injected, not summarised

Several CFTS clauses delegate their detail to a companion workbook — Seek's
cancel/stop behaviour is *only* in `CIP_Radio_Tables_v6.7.xlsx`, worksheet
`SEEK Cancel_Stop Transitions`. A batch cites one by writing
`[[table:NAME]]` in its row of `docs/batches-amfm.md`; `feature.yaml`
`spec_tables` maps the name to a file and sheet, and the context builder
injects the sheet as `{state, events{}}` records. `header_rows: 2` forward-
fills the merged banner row, so an event column keeps its group
(`EVENTS: Steering Wheel Control Hardkeys / A Seek Up`) instead of arriving
as a bare label. A cited sheet that is not in the file fails the build.

That table is what makes leaves 006/007/008/011/012/013 testable: it is the
only source for which events cancel a seek (return to the starting frequency)
and which stop it (remain at the displayed frequency). Generated without it,
those six leaves would have had to guess the event list.

### Cross-document citations are quoted, never resolved by guess (A-AM15)

`build_stla_map.py` now sweeps every CFTS024 clause for `{See CFTSnnn-mmm}`
tokens, repairing the non-breaking spaces the docx puts *inside* them
(`CFTS0\xa019-718` — the ASCII pattern silently misses the one citation in
§1.3.3 that reaches a leaf). Output: `data/cross_doc_citations.json`, keyed by
token, with the citing clauses, the leaves reached, and — where the cited
document is declared under `spec_docs.reference` and present in `inputs/` —
candidate clauses ranked by rarity-weighted overlap with the phrase the
citation hangs off ("HU shall play the rejection tone"), not by raw wording
similarity, which ranks `the HU shall` matches first.

The short ids resolve to nothing in the corpus: they are a foreign numbering
scheme, and CFTS024 uses it even for itself (`{See CFTS024-605}`). So the
resolver stops at candidates — and under **R11 that is enough**, because the
handling is cite-form rather than resolution: the token is cited verbatim as a
second `specification_reference`, the ER asserts the borrowed outcome anchored
to it (`as defined by CFTS019-718`), and the cited document's own rule surface
stays with that document's delivery. Each affected leaf carries the instruction
as `cross_references` in its batch context.

Three lint gates hold the line: `cross-reference` (a short-form token is
allowed only under the leaf whose clause writes it), `cross-reference-anchor`
(a cited token with no ER line anchoring to it), and the R10-2a absorption
count, from which cite-form citations are excluded — they claim no coverage,
so demanding an `[A-AM10]` marker would erase the distinction R11 draws.
`clause_citation_overrides` (ruling + `evidence_phrase`, refused when the
target clause stops carrying it) remains for a token someone later wants
resolved onto a clause; cite-form needs it for nothing.

Reached by a leaf today: `CFTS019-718` → 014 (Browse, rejection tone),
`CFTS028-1` → 025/027/029 (Tune — already handled correctly under R8: the VR
trigger path is out of scope and the generated TCs say so), `CFTS024-605` →
048, `CFTS024-707` → 057.

### External-document batches (Market Configuration / Engineering Mode / Diagnostics)

- **The three batches ran after CFTS011 / CFTS004 were wired in**, so their 17
  leaves carry section, section title and clause text like any CFTS024 leaf
  (`resolution: paragraph` on all 102). Generating them on the old
  `external-allocation` state would have produced 17 leaves whose acceptance
  criteria came from the 037 title alone.
- **093 is the case that justified the wiring on its own.** Its 037 title
  (agreement 0.575, the corpus low) compresses "Signal strength of combined
  AM/FM and FM2 tuners, measured once per second at a minimum" into "Signal
  strength for current frequency" and drops two per-tuner measurement fields
  plus the second-tuner Note. §8.6 puts the clause above the title, so three
  display items re-entered coverage that the title had removed.
- **A-AM08's two Engineering Mode pairs are now evidenced, not suspected.**
  087/094 both declare `4942534`, 089/095 both declare `4942540`. CFTS011 shows
  a regular three-clause pattern per band (display content / collect locally /
  sampling rate), and `4942535`, `4942539`, `4942544` — "The HU shall collect
  the information locally" — are unclaimed in all three bands. The count fits a
  mis-pointed id, but both leaves of each pair quote the display clause
  verbatim, so the text does not support that reading. Handled per R7-Q4: no
  consolidation, each leaf keeps its TC, `duplicate_of` set both ways, and the
  pair goes to Pei. Each pair's two TCs take different halves of their shared
  clause (087 the four items / 094 the antenna-not-connected value class; 089
  the display-update side / 095 the input-sampling side) so neither TC is
  content-free — and if a pair is ruled a true duplicate, the marked TC is the
  removable one.
- **097 carries the first cite-form citation found outside CFTS024**
  (`CFTS004-1316`, the method of determining the frequency step). It surfaced
  only after the citation sweep was extended to every owning document.
- **Upstream inconsistency for RD-1**: §1.6.1.10 is titled `$5009 - Frequency
  Step Selection` but its clause (102) requires tuning to a specific frequency;
  the read-direction `$5009` in §1.5.1.51 (097) does report the frequency step.
- **Values the clauses never define, left undefined**: Tuner status value range
  (099), carrier offset unit and encoding (100), the level thresholds behind
  the five signal-strength statuses (101). Each ER asserts membership or
  monotonicity instead of a number, and each goes to RD-1.

### Station List batch notes

- **The same CIP worksheet served a second clause.** `4872571` ("refer to the
  CIP Radio tables for actions that cancel station list update") points at the
  second block of `TA-PTY31 station list cancel` — the row keyed "Refresh
  Station list button is pressed; HU is currently updating Station List".
  Absorbed into 065-03: DIRECT TUNE / PRESET Save / PRESET Recall / knob rotate
  cancel the update, MUTE/PAUSE does not. The worksheet's own note (this does
  not apply to a dual tuner radio, whose update runs in the background) fixes
  the pre-condition to a single tuner.
- **065 carries four absorbed clauses across three TCs**, the largest
  absorption in the corpus: `4872553`/`4872554` (the two named softkeys "New
  List" and "Refresh List"), `4872550` (the update is a bandscan across the
  applicable wave bands at the hardware-defined sensitivity) and `4872571`.
- **066 is a §7 pair built from an absorbed opposite.** `4872552` (a dual
  tuner does not mute) is the other side of 066's own single-tuner clause;
  without it, an implementation that mutes on every variant passes.
- **Sensitivity and reception-quality thresholds are never given numbers.**
  `4872550` says the level is defined in the hardware spec, is software
  configurable and may change during development, so 065-02, 074 and 076 state
  relative relations (above / below the threshold, higher / lower quality)
  instead of dBµV values (§8.4.1).
- **Three near-identical sorting clauses carved by verification target**: 068
  (the sort-by-name option exists and applies), 069 (sort by Genre, with an ER
  that requires the result to differ from the name order), 078 (the sort key is
  the *visible* PS name, observable only when frequency-derived names from 077
  are mixed in).
- **Not absorbed → RD-1**: `4872546` and `4872569` are HD Radio content whose
  behaviour lives in §1.4, outside this batch's analog scope; `4872544`
  (section does not apply to NAFTA Refresh Radios) and `4872545` (applies to
  single and dual tuner in FM mode) are applicability statements, reflected in
  pre-conditions rather than absorbed.
- **Undefined term flagged**: 079's clause says "each active station" without
  defining active; the ER covers every station on the list and the term goes to
  RD-1 rather than being given a meaning here.

### RDS Features batch notes

- **A second CIP worksheet became the source of a decision table.** Clause
  `4872538` says only "refer to CIP Radio tables for actions that cancel TA or
  PTY 31 alerts"; that table is `TA-PTY31 station list cancel`, now registered
  as `ta_pty31_cancel` and absorbed into 062. Same shape as Seek's cancel/stop
  matrix: without it, 062-02 would have had to guess which events end an
  announcement (MUTE/PAUSE cancels, DIRECT TUNE continues until the customer
  picks a station).
- **061-02 exists only because §8.6 puts the spec above the 037 title.** The
  037 title for 061 (agreement 0.619) drops the exception sentence entirely —
  disc source shared with VES IR1/IR2 is NOT paused. Generating from the title
  alone would have lost a whole suppression branch.
- **057 is the third R11 cite-form TC** (`CFTS024-707`, radiotext behaviour),
  and it too reached the batch only via §8.6: the 037 title dropped the
  reference sentence (agreement 0.855).
- **Absorbed (R10-2)**: `4872528` → 060 (enabling TA on a station without TP
  starts a TA seek), `4872538` → 062, `4872541` → 063 (AF Local restricted to
  identical PI codes).
- **Not absorbed, and why** — the densest section in the corpus, so the rule
  had to do the work rather than judgement:
  - CAN signal clauses (`4872527` `$TA_STAT$`, `4872530`, `4872531`,
    `4872532`, `4872533`, `4872534`): CAN behaviour, not HMI — the Seek and
    Presets disposition, held here. `4872527` additionally serves the VR path
    (R8). `4872532`/`4872533` also cite A-AM15 short ids.
  - `4872537` (TA/TP icon appearance per the European RDS spec) elaborates
    054/055, whose clauses are in §1.3.13 — a **different section**, so R10-2's
    same-section condition fails. Coverage hole, not absorption.
  - `4872535` delegates audio arbitration to CFTS019 — another delivery.
  - `4872542` (AF switching inaudible) restates the last sentence of 053's own
    clause; absorbing it into 063 would count one behaviour twice.
  - `4872512`–`4872515`, `4872524`: section preamble, IEC 62106 conformance,
    market-applicability pointer, PI code and PTY/Genre definitions. No leaf
    claims `4872515`/`4872524` at all → coverage holes → RD-1.
- **056 (EON) is a capability description with no HMI outcome of its own.**
  Written as Scenario/Use Case with the ER narrowed to the one thing EON adds
  that TA switching does not: the announcement arrives from a *different*
  station of the network. The alternative was fabricating a search interface
  the clause never describes (§8.4.1).
- **059 skips its own `may` clause** ("HU may provide HMI to turn this feature
  ON or OFF") — optional behaviour has no pass criterion.

### List Navigation batch notes

- **Four wrap-around clauses absorbed** (`4872496`/`4872497` scroll,
  `4872502`/`4872503` page), each as the boundary TC of the leaf whose clause
  it bounds — Profile §4 classifies wrap-around as a boundary, not a function,
  and the Seek batch set the precedent for the same shape.
- **The `Radio:noSys` tag was checked, not waved through.** Browse declined to
  absorb `4872436`/`4872437` partly on that tag, so the disposition here had to
  be stated as a rule rather than a judgement: those two introduce a *new
  function* scoped `ECU:RRM`, while these four bound a function this leaf
  already owns and are scoped `ECU:ALL` with `EE Architecture: Atlantis High`,
  which is this program. The tag's inconsistency with the allocated clauses'
  `CTS1_2, allSys` is an upstream scope-hygiene item → RD-1.
- **048 is the second R11 cite-form TC.** `CFTS024-605` (the Seek Up behaviour
  Genre Seek inherits) is cited verbatim and anchored in the ER; what 048
  actually verifies is the clause's *exception* — a station of another genre is
  passed, a station of the selected genre is stopped on. Seek Up's own rules
  belong to leaves 003–008.
- **046 keeps only the menu-navigation branch.** Its clause states two possible
  outcomes; the "act upon the item" branch is owned concretely by 047, 049, 050
  and 051, so verifying both here would duplicate four siblings (§8.2.1).
- **051 vs 022 vs 034 is a three-way near-duplicate upstream** (Enter on a
  Preset List / short press in browse presets / preset button recall). Carve
  kept per R12-1: different trigger paths, so no TC-side consolidation
  (§8.2.2). Recorded for RD-1 as the same class as Q-AM2.
- **Concrete list used throughout §1.3.10–1.3.11**: the clauses are written for
  "a list of items" in the abstract, so the Tuner Station List is named in the
  pre-conditions to make the steps executable without inventing a list.

### Presets batch notes

- **The market configuration table is now an injected spec table.** Leaf 039's
  clause delegates the AF question to "the tuner configuration worksheet within
  market configuration table", so `SR24 R1 Market Configuration Table v1.6.xlsx`
  → `Radio Tuner Configuration` is registered in `spec_tables` and cited from
  the batch row. That sheet stacks two tables, which needed one new option:
  `first_row` selects the wanted table's own header (`load_spec_tables` now
  covered by `tests/test_amfm_batch_context.py`, which the injection mechanism
  did not have before).
- **Nine leaves, four overlapping clause families.** §1.3.7 states the same
  select-and-tune behaviour three times (031 Description, 033 trigger, 034
  outcome) and §1.3.8 twice (035 Description, 036/037 SFRs). Carve used, per
  §8.2.1: 031 keeps only what is unique to it (the steering-wheel Preset
  Advance order and its wrap-around); 033 the trigger identification; 034 the
  preset→station correspondence, tested across two presets so "always recalls
  the same one" fails; 035 only the HMI assignment update; 036 the two-second
  threshold; 037 assignment plus persistence across a power cycle.
- **036 tests both sides of the threshold.** A hold below two seconds must not
  save — without the negative side, an implementation that stores on every
  press passes, and that implementation overwrites a preset each time the user
  selects one.
- **037 uses a power cycle as a test step**, the only way to observe
  non-volatility. `HU is powered on` stays banned as a pre-condition; cycling
  power inside the procedure is an action, not a setup assumption.
- **Not absorbed, recorded as coverage holes → RD-1**: `4872469`–`4872472` and
  `4872479` (TGW / VES `IR1_PST_DSK` signal-status updates) are CAN behaviour
  rather than HMI behaviour — same disposition as the Seek batch's TGW
  clauses; `4872480` (associate a new preset with the current driver, "see
  Memory Seat, Chapter CFTS048-1") delegates to a document that is not in
  `inputs/`, and the citation is an A-AM15 short id.
- **031 leaves one branch ungenerated, deliberately**: for "no presets
  assigned" or "current frequency does not match any preset", the clause says
  only "follow the behavior defined in HMI" — no observable outcome to write
  an ER against (§8.4.1).

### Browse batch notes

- **014-02 is the first R11 cite-form TC.** The scenario is 014's (every
  preset deleted, then an access attempt from the HMI and from the steering
  wheel); the outcome is borrowed and anchored — `the key press rejection tone
  is played, as defined by CFTS019-718` — and cited as a second reference.
  Nothing about CFTS019's own rule surface is tested.
- **024 absorbs two clauses under R10-2** and cites both: `4872434`, the
  NAFTA/RBDS twin of the leaf's EMEA/RDS clause (market becomes an EP axis on
  `$Country_Code$` per R10-1), and `4872433`, "not available in AM, MW analog
  tuner modes" (R10-3 suppression TC — the Genre category is absent in AM and
  present in FM within the same TC's steps).
- **Two clauses deliberately NOT absorbed**, recorded in 024's reasoning and
  going to RD-1: `4872436` (genre knob scroll / enter to scan) and `4872437`
  (Genre Scan) carry `ECU:RRM` + `Radio:noSys` scope tags, inconsistent with
  this batch's `ECU:LTM, ETM, RRM` + `Radio:CTS1_2, allSys` leaves — absorbing
  them would claim coverage of behaviour whose applicability to this
  configuration is unsettled. `4872431` (§1.3.3.1) is likewise left as a
  coverage hole: its entire normative content is eight short-id
  cross-references (A-AM15), so absorbing it would produce no verifiable ER.
- **Scope kept off neighbouring batches**: 016/017 verify that the presets
  browse list scrolls line-by-line and page-by-page, not the general list
  navigation rules of §1.3.10–1.3.12 (leaves 040–051); 020's genre field is
  verified as displayed, not as a correct RDS Program Type mapping (§1.3.13).
- **021 carries A-AM11**: the `$ICS_KNOB2_VAL$` → line-count mapping is
  undefined upstream, so the ER asserts direction and monotonicity (a larger
  signal value advances further), never a specific number of lines.
- **023 tests the unset-preset path only.** Overwrite semantics for an
  already-set preset are not in `4872430`, and were not invented.

### Seek batch notes

- **006/011 pair the classes.** Testing only the Stop-class events would let
  an implementation that aborts the seek on *every* event pass, so each has a
  second TC on the Continue-class events (USB disconnect, SD card removal)
  asserting the search is unaffected.
- **007/008 and 012/013 are the landing-point contrast** — cancel returns to
  the starting frequency, stop remains at the displayed one. Their titles now
  name the direction; the first cut had Seek Up and Seek Down mirrors sharing
  a title, which `sibling-distinction` caught.
- **9 clauses absorbed under R10-2**, all cited: wrap-around both directions
  (`4872386`, `4872404`), two-pass termination (`4872387`, `4872405`), state
  exit (`4872391`, `4872409`), Seek Down initiation (`4872402`, `4872403`),
  PI seek ordering (`4872385`).
- **Two clause groups deliberately NOT absorbed**, recorded as coverage holes
  in reasoning per R10-2: the TGW signal-status clauses (they describe CAN
  updates, not HMI behaviour) and fast seek (A-AM13 — different trigger,
  different behaviour, no leaf).

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
