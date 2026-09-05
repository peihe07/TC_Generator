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

---

## 版本綁定（R-G45，2026-09-05）

依 `down/20260905_GC-02.md` §一-3 落檔。本節所列為本 feature 之 `inputs/` 內、
屬 R-G45 六類共用參考檔而其 sha256 **不在** `forms/` 同類現行版之 sha 集合者。

| `inputs/` 檔名 | sha8 | `forms/` 同類現行版 | sha8 | 是否影響已交付 TC |
|---|---|---|---|---|
| `HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx` | `a2533bf3` | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `8d04e51a` | **PENDING 分析層判** |
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `41daac00` | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `8d04e51a` | **PENDING 分析層判** |
| `Logical Identifiers and CAN Mapping v1_76.xlsx` | `9a751a72` | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679` | **PENDING 分析層判** |
| `SR24 R1 Market Configuration Table v1.6.xlsx` | `ae4cf0b9` | `SR24 R1 Market Configuration Table v1.6.xlsx` | `7e865d55` | **PENDING 分析層判** |

**本 feature 待記 4 檔次**（全域 5 個 feature／13 檔次）。
「是否影響已交付 TC」**執行層不判**（GC-02 §一-3 明文），逐列留 `PENDING 分析層判`。

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
