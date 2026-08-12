# FW036 SXM HMI — TC Generation Runbook

> **2026-08-11: directory moved `SXMHMI` → `features/sxm`.** Repo-wide reorganisation —
> all features now live under `features/`, lowercase and without the HMI
> suffix. Path strings in the body below are NOT rewritten: they are dated
> records, and they record what was true when they were written (same
> convention as the 2026-08-10 `AMFMHMI` → `AMFM` rename). Read any
> `SXMHMI/…` path in this file as `features/sxm/…`. `feature.yaml` paths are
> relative to the feature directory and were not affected.

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to SXM.

## Phase 0 — Intake
- [ ] Source files placed in `inputs/` (workbook, 037, spec, popup list)
- [ ] spec_mode classified: ___  (FEATURE_ONBOARDING §3)
- [ ] `feature.yaml` filled from `docs/fw036/templates/feature.yaml`

## Phase 1 — Recon (Tier 1, fully delegable)
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [ ] workbook_state: ___
- [ ] Coverage: ___ leaves total / ___ done / ___ regen targets

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_SXM_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [x] Batches generated → lint green → write-back invariants pass
      B1–B14, 202/202 leaves, 215 TCs, lint 0 findings, 952 tests

## Phase 7 — Delivery (Tier 3)
- [x] Release tag (xlsx SHA256 ↔ commit)
- [x] Submission drafted — `docs/fw036/RD1_sxm_submission.md`
- [ ] **RD-1 sent** — off-repo, Pei to send. Two documents go together: the
      SXM submission above and the AMFM one (`RD1_amfm_submission.md`), which
      gained an F5 FYI line about the TC ID prefix change and cannot be sent
      as previously reviewed.

## Close-out (2026-08-12)

**Tag `fw036-sxm-v1` on `3d6adb0`**, annotation from
`features/sxm/docs/tag-annotation-sxm-v1.txt`.

| | |
|---|---|
| output | `FM-WI-FSM-036-A01 …_SWQT_SXM_20260810.xlsx` |
| SHA256 | `7b6e760d524fb79e3e4f7cafb43be4b2c945d64b9063abb3974a5e9737538a02` |
| rows | 0 preserved / 215 new / 0 placeholder; rows 10–224 |
| coverage | 202/202 leaves, exact set equality |
| priority | P0=22 · P1=181 · P2=12 |
| form | revision C, ChangeHistory revision D |
| repo state | lint 0 findings · 952 tests |

**Re-running the delivery requires `--date 2026-08-12`.** Without it the writer
falls back to `date.today()`, the ChangeHistory date moves and the output hash
drifts daily — the reproducibility claim is void unless the flag is given.
This precondition is specific to SXM; the AMFM annotation carries no equivalent.

```
python features/sxm/scripts/write_back.py --feature-dir features/sxm \
  --date 2026-08-12 --write
```

The annotation records `produced at: da8b38e` while the tag sits on `3d6adb0`.
Both are correct and neither needs changing: `da8b38e` is the commit the
delivered file was actually written from, and it is a **docs-only** descendant
of `3d6adb0` — `git diff 3d6adb0 da8b38e -- features/sxm/generated
features/sxm/feature.yaml features/sxm/scripts` is empty, so the tagged commit
re-derives the same bytes. This mirrors the AMFM annotation, which records a
producing commit (`bf514e2`) and a second verification at a later one.

Still owed after this: RD-1 sending (above), and the two post-delivery canon
items — A-SX27 (framework Part IV `Source Availability` Set name vs its
content) and the `<Feature>HMI` scaffold convention in
`docs/fw036/templates/PLAYBOOK.md`, whose stale pointers already materialised
in `features/projection/PLAYBOOK.md`.
