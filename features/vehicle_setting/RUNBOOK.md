# FW036 Vehicle Setting HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to Vehicle Setting.

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
- [ ] `docs/runtime/profiles/FW036_R1L_Vehicle Setting_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent

---

## 分級覆寫層（R-VF20，2026-08-23）

**跑 `writability_driver.py --write` 之後必跑覆寫層**，否則 R-VF17 之
4 leaf 會被回復為 W2。

```bash
python3 scripts/writability_driver.py --write
python3 scripts/grade_overrides.py --apply     # ← 必跑
python3 scripts/grade_overrides.py --check     # 驗證；不符則 exit 1
```

覆寫清單為 `data/grade_overrides.tsv`。**新增覆寫須引用一條裁決編號**
（`ruling` 欄）與逐字來源（`source_verbatim` 欄），缺者腳本 `raise`。
**不得以程式碼內嵌之條件式代替清單**（R-VF20 第 2 項）。

`--check` 之可失敗性已實測（V08／W-VF23）：人為將任一覆寫標的改回原級，
`--check` 即報出該列並 `exit 1`。
