# FW036 Projection HMI — TC Refinement Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what is
specific to Projection. The live status board is `PLAYBOOK.md` §6 — this file
does not duplicate it.

**This feature is a refinement, not a regeneration.** `workbook_state =
FULL_REFINE`, a state canon §2 does not define; it is defined in
`docs/runtime/profiles/FW036_R1L_Projection_Profile.md` §1. The base workbook
already carries 559 executed test cases covering 164 of 171 037 leaves. The
defect is that the steps are not executable, not that fields are empty.

## Phase 0 — Intake ✅ 2026-08-11
- [x] 25 source files in `inputs/` (R-P5 root), every SHA256 in DECISIONS §1
- [x] spec_mode classified: **[A, B, D]** — fixed by the workbook's own
      `Specification Reference` column (profile §7)
- [x] `feature.yaml` filled; columns resolved by header-text match 17/17
- [x] `data/signal_map.json` built, every entry verified by lookup
- [x] Profile written with O-1…O-4 verbatim and L-PJ1…L-PJ7

## Phase 1 — Recon (Tier 1) ✅ 2026-08-11
Run: `.venv/bin/python features/projection/scripts/recon_projection.py`
(outputs `data/recon.json`; the narrative is `RECON.md`).

The shared `scripts/recon.py` is **not** usable here — it assumes an
FM-WI-FSM-036 form (header row 9, done-region-by-author). This workbook is the
NR1L_GEN1(HDCC) execution workbook: header row 2, data from row 4, seven
vehicle-model columns, five build-result columns.

- [x] workbook_state: **FULL_REFINE**
- [x] Coverage: **171** leaves / **164** covered / **7** uncovered
- [x] Refine targets: 559 rows, of which **23 frozen** (R-P6) → 536 refinable
- [x] 預驗值對照完成 — `RECON.md` §14. 12 項不符，全部未自行調和

## Phase 2 — Rulings (Tier 2) ← 當前關卡
- [ ] DECISIONS.md signed by Pei
- [ ] 7 open items listed in `PLAYBOOK.md` §6 and `DECISIONS.md` §8

## Phase 3 — Framework & profile (Tier 2)
- [ ] Profile approved (written; awaiting review)
- [ ] `docs/fw036/framework.md` Part N — must address A-PJ06 (Test Group
      carries 10 module names, not one)

## Phase 4 — Data build (Tier 1)
- [x] `data/signal_map.json`
- [ ] Spec clause index — blocked on DR#6 / DR#7 / DR#8 rulings

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: **Vehicle Signal Forwarding** (22 rows) [PROPOSED] — it is
      the earliest batch that exercises CAN sends, PROXI pre-conditions and
      signal resolution together, so it falsifies the whole gate set soonest

## Phase 6 — Batch refinement (Tier 1)
- [ ] Batches refined → lint green → write-back invariants pass
- [ ] Append the 7 uncovered leaves at the tail

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent

---

## Feature-specific facts worth not re-deriving

- **Base workbook column letters are unique to this feature.** From column F
  onward they sit one letter left of every FM-WI-FSM-036 instance in the repo,
  because there is no `Test Case ID (TestRail)` column. Never inherit letters
  from another `feature.yaml`.
- **DBCs are ISO-8859 with CRLF.** Reading them as UTF-8 yields nothing, and a
  lint that finds nothing passes everything.
- **Both DBCs are required** — they share only 24 messages, and `$FuelLvlLow$`
  exists on CAN-B alone.
- **Mapping-table LIDs are UPPER CASE**; the workbook uses three casings of
  the same id. Look up case-insensitively.
- **`Projection_Mode_Selection = 0` does not disable projection** — it enables
  both CarPlay and Android Auto. Disabling needs `Projection_Mode = Absent`.
- **Only two columns are editable**: Pre-Conditions (I) and Test procedure
  (K). L-PJ4 (Expected Result frozen) beats L-PJ6 (clear vague language) on
  every collision.
