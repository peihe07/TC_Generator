# DECISIONS — Time Management (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

---

## 0. 裁決引用（手工維護 —— 見警告）

> **警告（A-TM15）**：`recon.py` 會**整份重寫**本檔（`recon.py:294` 自陳
> 「rewrites DECISIONS.md whole」），僅在本檔已簽核時才改寫入
> `DECISIONS.new.md`。**本節為手工維護，每次重跑 recon 後必須手動補回。**
> 條文全文之權威在 `RULINGS.md`，該檔不受 recon 影響。

| 條 | 形態 | 要旨 | 狀態 |
|---|---|---|---|
| R-TM1 | `[PEI]` | 目錄 slug `time_management`；`feature` = `"Time Management"` | 已套用 |
| R-TM2 | `[PEI]` | `test_group` 暫定值 + 推翻條件 | **由 R-TM8 取代** |
| R-TM3 | `[分析層自裁]` | CLI 參數帶底線；anomaly 縮寫 `TM` | 已套用 |
| R-TM4 | `[分析層自裁]` | 解析結果須附完整元素清單，**雙向適用** | 已套用 |
| R-TM5 | `[PEI]` | 036 以 R-G1 母本為之 → `workbook_state = BLANK` | 已套用 |
| R-TM6 | `[PEI]` | 覆蓋分母 = SYS2 FR **126**；A-TM02 分拆；48 筆**宣告非補生成** | 已記錄 |
| R-TM7 | `[分析層自裁]` | 下放包指令須先讀 argparse | 已知悉 |
| R-TM8 | `[PEI 授權]` | **Test Group 欄值 = `"Time and Date"`** | 已套用 |
| R-TM9 + A1 | `[PEI 授權]` + `[分析層]` | `D5` 識別段 = `"Time-and-Date-HMI-V0.1"`；**前綴段待決** | **D5 維持空白** |
| R-TM10 + A1 | `[PEI 授權]` + `[分析層]` | 跨 feature 樣式參照 → **全條 SUSPENDED** | **不得援引** |

### 對本檔 `[AUTO]` 值之覆寫關係

- §2 之 `test_group` 相關：**R-TM8 已實裁 `"Time and Date"`**，非 `[PROPOSED]`
- §3 之覆蓋分母：**R-TM6 定為 126**（SYS2 FR 全集），非 22（SWE leaf）。
  recon 之 `037 leaves: 22` 為**生成單位**，非稽核分母 —— 二者不可混用
- §4 之 `exemplar source`：recon 預填 `cross-feature: style only`，
  但 **R-TM10-A1 已 SUSPENDED 該路徑**，現無跨 feature 樣式來源可用
- §4 之 `spec_reference`：recon 預填 `<Spec Filename>_{outline}`，
  但 `{outline}` 之來源 map 為空（**A-TM12**），錨鏈路線待裁

## 1. Intake
- spec_mode: [AUTO] D
- spec text layer: [AUTO] text-layer: 106094 chars (via pymupdf)
- source files: [AUTO] 4 present (SHA256 in RECON.md)
- ruled-constant assertions: [AUTO] 0 checked, 0 PASS, 0 FAIL (measured values in RECON.md)

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 22
- safety attributes: [PROPOSED: ruled source carries no ASIL/FTTI column, so the SYS2/SYSRA safety layer does NOT enter the trace chain]
- regen targets: [AUTO] 22 (list in recon.json)
- covered nowhere: [AUTO] 22 = all leaves — expected under BLANK, not an anomaly; this is the Phase 4 work list, not a gap

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
- batch plan: [PROPOSED: group 22 targets by spec chapter, pilot = smallest coherent batch]

---

## Sign-off

- Reviewed by: ____  Date: ____
- Overridden items: ____
- Ruling notes:
