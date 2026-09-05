# DECISIONS — Vehicle Setting (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] text-layer: 762967 chars (via pymupdf)
- source files: [AUTO] 4 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 0 checked, 0 PASS, 0 FAIL (measured values in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- draft disposition: [PROPOSED: discard & regenerate — lint consistency cheaper than row salvage]
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 46
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 46 (list in recon.json)
- workbook req_ids absent from 037: [AUTO] done=0 (none) draft=191 ['SWE1-VC-HeatedSteeringWheel-003', 'SWE1-VC-HeatedSteeringWheel-004', 'SWE1-VC-HeatedSteeringWheel-005', 'SWE1-VC-HeatedSteeringWheel-006'] … +187 more (full list in data/recon.json) — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only. NOTE: under BLANK these are template sample rows before they are anything else — check the rows themselves before filing an RD-1

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
- batch plan: [PROPOSED: group 46 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:

---

## 版本綁定（R-G45，2026-09-05）

依 `down/20260905_GC-02.md` §一-3 落檔。本節所列為本 feature 之 `inputs/` 內、
屬 R-G45 六類共用參考檔而其 sha256 **不在** `forms/` 同類現行版之 sha 集合者。

| `inputs/` 檔名 | sha8 | `forms/` 同類現行版 | sha8 | 是否影響已交付 TC |
|---|---|---|---|---|
| `PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec98` | `P363_BH-CAN [07338]_3A_R2.dbc`<br>`PDT27_E2A_R1_BHCAN2.dbc`<br>`PDT27_E2A_R1_FDCAN8.dbc`<br>`Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc` | `a51079be`<br>`46cb73f3`<br>`2a86c4bf`<br>`5cac2abc` | ~~**PENDING 分析層判**~~ → **高風險，版本由 Pei 裁** —— GC-04 只量不判。本線最新工作簿之 48 個相異 `$MESSAGE.Signal$` token 對 `forms/PDT27_E2A_R1_BHCAN2.dbc` 與本份 `R4_BHCAN` 之四象限：兩邊皆有 **0**、只在 forms R1 **0**、只在 inputs R4 **1**（`IPC_VEHICLE_SETUP2.Power_Tailgate_Enable`）、兩邊皆無 **47**。即本簿所用之訊號幾乎不在任一 BHCAN 檔內（其落點見下一列之 FDCAN8）。 |
| `PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd60` | `P363_BH-CAN [07338]_3A_R2.dbc`<br>`PDT27_E2A_R1_BHCAN2.dbc`<br>`PDT27_E2A_R1_FDCAN8.dbc`<br>`Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc` | `a51079be`<br>`46cb73f3`<br>`2a86c4bf`<br>`5cac2abc` | ~~**PENDING 分析層判**~~ → **高風險，版本由 Pei 裁** —— 同上 48 token 對 `forms/PDT27_E2A_R1_FDCAN8.dbc` 與本份 `R5_FDCAN8` 之四象限：**兩邊皆有 48**、其餘三象限皆 **0**。**就本簿實際使用之訊號而言，R1 與 R5 無差異**；R5 多出之 122 個 `SG_` 未被本簿使用。 |
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `0a37121f` | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `8d04e51a` | ~~**PENDING 分析層判**~~ → **不影響（key 級）** —— key 逐列相同。盲區（R-G11）：非 key 分頁（Notes、Brand-Specific Names、Options 文字）之差未查；若本線 TC 引用此類欄位，本判須重開。 |
| `Logical Identifiers and CAN Mapping v1_76.xlsx` | `ffceac36` | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679` | ~~**PENDING 分析層判**~~ → **待證 → 傾向不影響** —— 4 個值異 signal 命中 **0/4**；對照向：該簿引用 LID signal 18/2548，**變動之 4 個不在該 18 之內**。 |

**配對（R-G45 補充，GC-02 審閱 §二-1）**：DBC／LID 一類以**網段 token** 為配對鍵，
版本 token（`R1`／`R4`／`R5`）不入配對 ——
`PDT27_E2A_R4_BHCAN.dbc` ↔ `forms/PDT27_E2A_R1_BHCAN2.dbc`（`46cb73f3`）；
`PDT27_E2A_R5_FDCAN8.dbc` ↔ `forms/PDT27_E2A_R1_FDCAN8.dbc`（`2a86c4bf`）。
上表之四份並列**保留**（GC-02 審閱裁），本註為其配對鍵。


**「是否影響已交付 TC」之判（分析層，`down/20260905_GC-03_review.md` §四；GC-04 §一-4 抄回）**。前提：本 feature 之 `delivered/` 為空，故以「現存最新工作簿」為對象。原 `PENDING 分析層判` 依 R-TM13 以刪除線保留。

**本 feature 待記 4 檔次**（全域 5 個 feature／13 檔次）。
「是否影響已交付 TC」執行層不判（GC-02 §一-3 明文）；分析層已於 2026-09-05 逐列判訖，見上表右欄。

**查詢式與命中數（R-G50）**——

```text
母體：docs/reports/source_identity_20260905.tsv（220 列，GC-01 §二-1）
篩選：path 符合 ^features/<feat>/inputs/
      且 filename 屬 R-G45 六類之一（DBC=*.dbc；LID=前綴 'Logical Identifiers and CAN Mapping'；
      PROXI=前綴 'PROXI_'；HMI Settings List／Pop Up List=同名前綴；
      Market Config=含 'Market Configuration Table'）
      且 sha256 不在 forms/ 同類之 sha 集合內
命中：4 列（本 feature）／13 列（全域，跨 5 個 feature）
腳本：GC-02 執行層量測腳本，與 up/20260905_GC-01.md 11-3 節同一判準
```
