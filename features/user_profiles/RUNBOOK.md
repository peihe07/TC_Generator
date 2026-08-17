# FW036 User Profiles HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to User Profiles.

往返索引：`docs/INDEX.md`。裁決台帳：`RULINGS.md`（R-G1/R-G2/R-U1~R-U7）。
異常台帳：`ANOMALIES.md`（A-UP01~A-UP09）。

## Phase 0 — Intake（2026-08-17，上繳包 01；**部分完成**）
- [x] 036 母本依 R-G1 就位：`inputs/…_SWQT_20260817_ext.xlsx`（`6372fb6b…`）
- [x] spec 依 R-U3 就位（留在 `spec-index/`，雜湊由 `BASELINE.sha256` 保護）
- [ ] **037 未到齊 —— A-UP04，DR #1，BLOCKING**
- [ ] Pop Up List 未到齊 —— A-UP06，DR #2
- [x] spec_mode classified: **A**（R-U3；169 列單一 stem、0 unparsed）
- [x] `feature.yaml` filled（欄位字母為 **rev C** 實測值，非 scaffold 之 rev A/B）
- [x] `BASELINE.sha256` 建立並驗證 4/4 OK

## Phase 1 — Recon (Tier 1, fully delegable) — **停下**
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [x] workbook_state: **BLANK**（R-U6；母本 A–AH 全欄非空格 0、filled 列 0）
- [ ] Coverage: **未實測** —— 兩個獨立阻擋：
      (1) 037 不在 repo（A-UP04）
      (2) 預期值單位不一致，182（ID 前綴形態）vs 180（Categorization），
          01b 之判準下 182 不可能成立（**A-UP07，037 到齊亦不解除**）
- **執行順序**：先裁 A-UP07，再跑 recon。反了就會變成用實測值改期望值。

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_User_Profiles_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
