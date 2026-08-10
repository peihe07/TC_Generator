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
- [ ] Browse · Presets · List Navigation · RDS Features · Station List ·
      Market Configuration · Engineering Mode · Diagnostics
- [ ] write-back invariants pass

| Batch | Leaves | TCs | P0/P1/P2/P3 | Design methods |
|---|---|---|---|---|
| Tuner Availability + Tune (pilot) | 8 | 13 | 0/8/5/0 | Functional 3, EP 4, BVA 4, Decision Table 2 |
| Seek | 11 | 22 | 0/19/3/0 | Decision Table 8, State Transition 5, Functional 4, BVA 4, EP 1 |

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
