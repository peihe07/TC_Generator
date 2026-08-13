# DECISIONS — Privacy (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] no-pdf
- source files: [AUTO] 3 present (SHA256 in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- feature.yaml column letters: [PEI] 3 disagree with the header — update feature.yaml before Phase 4 (see RECON.md)
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- draft disposition: [PROPOSED: discard & regenerate — lint consistency cheaper than row salvage]
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 10
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 10 (list in recon.json)
- covered nowhere: [AUTO] 10 ['SWE1-HMI-PRIVACY_FEATURES-001', 'SWE1-HMI-PRIVACY_FEATURES-002', 'SWE1-HMI-PRIVACY_FEATURES-003', 'SWE1-HMI-PRIVACY_FEATURES-004', 'SWE1-HMI-PRIVACY_FEATURES-005', 'SWE1-HMI-PRIVACY_FEATURES-006', 'SWE1-HMI-PRIVACY_FEATURES-007', 'SWE1-HMI-PRIVACY_FEATURES-008'] … +2 more (full list in data/recon.json) — ANOMALIES entries required
- workbook req_ids absent from 037: [AUTO] done=0 (none) draft=1 ['xxx'] — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only

## 4. Style bindings
- style authority: [PROPOSED: fallback chain — no done region]
- test item shape: [PROPOSED: standard §4.3 tc_title]
- test group/set columns: [PROPOSED: FILL per framework Part N]
- exemplar source: [PROPOSED: nearest sibling feature done region, cross-feature: style only]
- author on new rows: [PROPOSED: PeiPYHsu]
- spec_reference: [PROPOSED: <Spec Filename>_{outline}]

## 5. Split & scope
- split_mode: [PROPOSED: standard]

## 6. Framework & profile
- Test Set table (Part N): [PEI — draft with Claude, Tier 2]
- profile [OVERRIDE] clauses: [PEI — draft with Claude, Tier 2]

## 7. Execution
- batch plan: [PROPOSED: group 10 targets by spec chapter, pilot = smallest coherent batch]

---

## 8. Signed rulings (2026-08-13)

分批簽署。已簽者立即生效，未簽者不得以任何方式默認。

### R-PV01(c) — Amplified 在範圍內 · **SIGNED**
`Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx`
入 `inputs/`（SHA256 `49dd3c31…`）。依據為 037 內證：-007/-008/-010
（PROF-173/174/176）明文以「AMP is present」為前提。
ANC 兩份（V9_R3 / V11_R3）維持不索取。→ A-PV02

### R-PV01(a)(b)(d) — **DEFERRED to P2**
排除 ETM V3_R3 屬縮範圍，錯誤代價是漏驗；其證據（handoff §3.2/§3.4）為
單方掃描未經重驗。V3_R3 留在 `inputs/` **不引用**，零成本。
P2 重驗後再簽。(b)(d) 隨 (a) 一併延後，不擋路。→ A-PV03

### R-PV02 — abbr · **SIGNED**
- anomaly 前綴 `A-PV`，維持現況，**不改 `new_feature.py`**
- TC id `NR1L-Privacy-{NNN}`（已寫入 `feature.yaml` `tc_id_format`）
- 依據：範本第 10 列原廠樣本 `NR1L-AntiTheft-001` 為完整 feature 名、
  大小寫混合，非兩字母縮寫。照範本走。→ A-PV06

### x14 DV 往返實測 · **已執行**（原訂 P4 前，提前於 Phase 1 完成）
結論：openpyxl 存檔 = LOSSY（x14 DV 全失，另丟 5 個 printerSettings、
VML 註解圖層、內嵌 JPEG 重編碼、sharedStrings 消失）；
zip 層外科手術 = LOSSLESS（48 成員零增零減）。
**P7 一律走外科手術路徑。** 探針：`scripts/xlsx_roundtrip_probe.py`。→ A-PV09

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes: R-PV01(c) 與 R-PV02 已於 2026-08-13 分批簽署（見 §8）；
  R-PV01(a)(b)(d) 明示延後至 P2，未簽前不得縮限任何 spec 引用範圍。
