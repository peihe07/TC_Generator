# FW036 Vehicle Category HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to Vehicle Category.

## Phase 0 — Intake
- [x] Source files placed in `inputs/` (036 母本、037、SYS1 export、規格 PDF)
      —— Pop Up List / HMI Settings List 僅於 `reference:` 綁定，未複製（待裁）
- [x] spec_mode classified: **A**  (FEATURE_ONBOARDING §3；01 包 T9 實測)
- [x] `feature.yaml` filled  —— `recon_assertions` 與二個 `paths` 鍵待裁

## Phase 1 — Recon (Tier 1, fully delegable)
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
- [x] workbook_state: **BLANK**（done 0 / draft 0 / authors none）
- [x] Coverage: **117 leaf 全集**（R-VC3）/ 0 done / 145 regen targets
      —— `recon.py` 之 leaf 判準為 `Categorization` 之 145，與 R-VC3 之 117
      不同量，二者並存而只有前者進機器護欄（01 包 §1 T3 已揭露，待裁）
- [ ] `data/recon.json`、`data/recon_leaf_to_section.tsv`、`DECISIONS.md`
      —— **未產出**，待 A-VC6 之腳本修法裁定

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [ ] `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md` written

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md
- [ ] **R-VC6(b)** —— 037 欄 11／13／15／17（Description-Action for
      Feasibility／Impact／Risk Factor／Reusable）之描述文字納入資料建置，
      作為 `reasoning` 與 test_item 括號下半之素材來源
- [ ] **R-VC6(a)** —— 037 欄 18 `Priority`（leaf 上為 Medium 88 / High 28 /
      Low 1）對 TC `priority`（IN §10.2 之 P0–P3）之映射規則
      **待裁**；在裁定前不得忽略該欄本地推導

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
