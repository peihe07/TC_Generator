# FW036 AMFM HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to AMFM.

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
- [ ] Pilot batch: **Tuner Availability (2) + Tune (6) = 8 leaves** proposed —
      rationale and the alternative (Seek 003–008) in `docs/batches-amfm.md`.
      Contexts already built: `batches/tuner_availability.json`,
      `batches/tune.json`
- [ ] Blocking on Pei before generation: A-AM08's 029 id correction
      (`4872451` → `4872457`) — it changes that leaf's spec_reference, and
      029 is inside the proposed pilot
- [ ] Non-blocking but in-scope for the pilot: A-AM09's VR Command question
      (025/027 are in the Tune batch)
- [ ] → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
