# FW036 Phone HMI — TC Generation Runbook

Process canon: `docs/fw036/FEATURE_ONBOARDING.md` (authority for phases,
decision tiers, workbook_state strategies). This runbook records only what
is specific to Phone.

本 feature 走 **R-G66 來源集中制**：原檔落 `sources/raw/<doc_id>/`，
`inputs/` 恆空。下放包 `docs/fw036/handoff/down/20260907_PH-01.md`（PH-01）。

## Phase 0 — Intake（2026-09-07 完成，PH-01）
- [x] Source files 登錄 `sources/raw/`（4 件；SYS1 **未登錄**，見下）
      —— `phone_037_v0_1`／`phone_hmi_lf_pdf_2022`／`phone_hmi_lf_pdf_26pi`／`phone_changelog_26pi`
- [x] R-G67 嵌入物件檢查：**已查、無此目錄**（母體為 HMI L&F 非 CFTS；
      `…/CFTS Embedded Objects/` 實測 9 目錄，無 CFTS026 亦無 Phone 相關）
- [ ] spec_mode classified: **BLOCKED** —— `intake.py` 提案 `A`，
      惟 SYS1 權威版本未定（A-PH01／DRAFT-PH-a）
- [x] `feature.yaml` 填妥（`paths.sys1_export: null`）
- [x] `sandbox/base/` 自 R-G1 母本複製（sha256 與母本全等）

## Phase 1 — Recon (Tier 1, fully delegable)（2026-09-07 執行）
Run recon; outputs `RECON.md` + pre-filled `DECISIONS.md`.
```
python scripts/recon.py --feature features/phone --root .
```
- [x] workbook_state: **BLANK**（authored 0／draft 0）
- [x] Coverage: **754** leaves total / **0** done / **754** regen targets
      （037 資料列 911＝754 Functional ＋ 157 Heading）
- [x] `RECON.md` 已產出
- [ ] `DECISIONS.md` —— **`recon.py` 因斷言 FAIL 拒絕產出**（如實留著）；
      現行檔為人工補寫，其首節具名此事。斷言轉綠後**須重跑 recon 並以其產出為準**。

## ⛔ 現行阻斷 — `DRAFT-PH-a`（SYS1 權威版本）
`ANOMALIES.md` A-PH01／`DATA_REQUESTS.md` §1。**Phase 2 以後不得啟動。**

## Phase 2 — Rulings (Tier 2)
- [ ] DECISIONS.md signed by Pei

## Phase 3 — Framework & profile (Tier 2)
- [ ] `docs/fw036/framework.md` Part N appended
- [x] `docs/runtime/profiles/FW036_R1L_Phone_Profile.md` **骨架已建**（PH-01 §任務 4）
      —— lint `P`(v4)＋`X` 已宣告啟用（`--profile phone`）；條文內容待本階段

## Phase 4 — Data build (Tier 1)
- [ ] Data artifacts built per feature.yaml; misses filed to ANOMALIES.md

## Phase 5 — Pilot (Tier 2)
- [ ] Pilot batch: ___  → Pei review → prompt adjustments recorded here

## Phase 6 — Batch generation (Tier 1)
- [ ] Batches generated → lint green → write-back invariants pass

## Phase 7 — Delivery (Tier 3)
- [ ] Release tag (xlsx SHA256 ↔ commit) · submission · RD-1 sent
