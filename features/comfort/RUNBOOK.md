# FW036 Comfort HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to Comfort.

Comfort 之裁決基線：**SR24 CR24879**（R-C1）。SR25 CR29359 為 out-of-scope
參考資料，**不得作為查得依據**。全部條文見 `RULINGS.md`；往返序見
`docs/INDEX.md`。

## Phase 0 — Intake  ✅ 2026-08-14
- [x] Source files placed in `inputs/`：037 + 036 空白範本（BLANK，取自
      `forms/`）。SR24 spec 三件**不搬移**，留在 `spec-index/`，
      `feature.yaml` 以 `../../spec-index/…` 回指。popup list 無（null）
- [x] spec_mode classified: **A**（SYS1 export 齊備）。intake 第一次跑提 `E`，
      因其只掃 drop folder —— 見 A-CF04
- [x] `feature.yaml` filled：含 `recon_assertions`（R-C3／R-C4 之機械期望值）
      與 `spec_reference_template`（SR24 全名 stem，R-C1）

## Phase 1 — Recon (Tier 1, fully delegable)  ✅ 2026-08-14
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [x] workbook_state: **BLANK**（done 0 列／draft 2 列，皆範本樣本，A-CF07）
- [x] Coverage: **403** leaves total / **0** done / **403** regen targets
- [x] Assertions（PASS/FAIL + 實測值，非僅印計數）：
      leaf 403 **PASS**；相異 section 129 **PASS**；citation stem 唯一且為
      SR24 **PASS**；129 節對 SR24 outline 查得 miss=0 **PASS**
- [x] outline map：`data/spec_id_to_outline.tsv`（403 列，追蹤入版控）

指令：
```
python3 scripts/new_feature.py Comfort --adopt-existing --root .
python3 scripts/intake.py  Comfort --root . --scaffold
python3 scripts/recon.py   --feature features/comfort --root .
```

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei
- 已凍結、**不在簽署範圍內**者：`test_group` = `Comfort`（R-C6）、
  `tc_id` = `NR1L-ComfortHMI-{NNN}`（R-C7）、baseline = SR24（R-C1）、
  UI label 拼寫依 SR24（R-C2）、leaf 判準（R-C3）
- open PENDING：**無**

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
