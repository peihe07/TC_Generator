# FW036 R1L Bed Lowering — Profile

- 設立依據：**R-BLM5**（Pei 2026-08-26，chat 裁定「乙」）
- 命名依既有慣例（CamelCase 無分隔，同 `VehicleCategory`／`VehicleSetting`／
  `PowerModing`／`UserProfiles`）
- **本檔只寫當前需要者，不預先設計未來條款**（沿 R-VC19 §2.3 之精神）
- 母體標註：本檔凡引用計數必標母體，限 `218 列` ／ `176 leaf` ／
  `42 Heading` ／ `70 outline`（SYS1 側）四者

---

## 0. 適用範圍

| 項 | 值 | 權威 |
|---|---|---|
| feature | `Bed Lowering Mode` | R-BLM1 |
| slug | `bed_lowering` | R-BLM1 |
| `test_group`（工作簿 G 欄）| `Bed Lowering Mode` | R-BLM1 |
| Layer 2 Test Set（H 欄）| 9 組 | `framework.md` Part II |
| `spec_reference`（N 欄）| 逐字取 037 `HMI Source ID` 欄原值，不構造、不補章節號 | **R-BLM5（本檔 §1）** |
| 驗證母體 | **176 leaf** | R-BLM2 |
| 規格 PDF 來源本 | `features/bed_lowering/inputs/Bed Lowering Mode HMI Logic and Flow R1 SR24 1A (June 21 2021).pdf`（無後手標註之原始輸出）| R-BLM4 |
| `workbook_state` | `BLANK` | R-BLM3 |

---

## 1. `[OVERRIDE IN §10.7(b)]` — spec_reference 不帶章節號

IN §10.7(b) 規定 HMI Logic and Flow 類之 `specification_reference` 為
`{檔名}_{章節號}`，一章節一行。

**本 feature 之該欄不帶章節號**，其值為單行常數：

```
SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021)
```

### 1.1 override 之事實依據（全表實測，2026-08-26）

| 項 | 實測值 |
|---|---|
| 037 `HMI Source ID` 相異值數 | **1**（218/218 列，無章節號後綴）|
| 037 `Source Requirement ID` 相異值數 | 42（`SYS-HMI-RA-BLM-001` ~ `-066`，每 Heading 一個）|
| SYS1 `SYSRE_HMI_Source ID` 格式 | `{檔名}_{章節號}`，70 列各異 |
| 兩者之相交 | **空**（SYS-HMI-RA 號不在 SYS1 任一欄；NRL 號與章節號不在 037 任一欄）|

上游正式欄給得出檔名，給不出章節號。錨定原則（上游交付物之正式欄為第一
來源，非本地演算輸出）禁止分析層自行推定章節號。**故本 override 之成因
為來源缺件，非規則鬆綁。**

### 1.2 本 override 不及之事

- **不及於其他欄位。** `Requirement or Design ID` 仍填 leaf 之
  `SWE1-HMI-BLM-{nnn}-{mm}`，逐字沿用上游，追溯粒度不受影響
- **不及於其他 feature。** 本條為 feature-scoped，不得類推。他 feature
  之 037 若帶章節號，仍依 IN §10.7(b) 原文
- **不及於 CFTS 家族。** 本 feature 無 CFTS 母文件，§10.7(a) 不生效

### 1.3 交付面之代價（須於交付說明揭露）

全簿 176 列之 N 欄值完全相同，**追溯粒度為文件級**。
審查者無法自該欄定位到規格章節；定位須經
`Requirement or Design ID` → 037 → `Requirement Description` 之路徑。

**此為已知代價，非缺陷。** 其成因（A-BLM4）與裁定（R-BLM4）皆有紀錄。

---

## 2. 範圍條款 — SYS 側 24 個缺號不入範圍

依 **R-BLM6**：`SYS-HMI-RA-BLM` 之 24 個缺號判定為 SYS 側非 HMI 項
（底盤、電氣），不生成 TC、不列 coverage gap、不登 DR。

該裁定之依據為 Pei 之領域判斷，非自手邊文件驗得（R-BLM6 末段之註記）。

---

## 3. Heading 列之處置

依 **R-BLM2**：42 個 Heading 列入覆蓋台帳並標
`No TC — Heading; refer to child IDs`，不生成 TC。
TC 生成母體為 176 leaf。

---

## 4. `[OVERRIDE IN §10.4]` — reasoning 單位（R-BLM14(2)）

IN §10.4 定 reasoning 為 top-level field（"not per-TC"）。本 feature：

- **top-level reasoning**：批次摘要，必有。
- **per-TC reasoning**：僅於裁定要求逐 leaf 內容時存在 ——
  R-BLM13(b) 之委派句、IN §8.2.1 之縮窄委派。其餘 TC 不補。
- per-TC reasoning 之存在本身即為「本條涉及委派」之訊號；
  審查者見該欄即知需對照持有 leaf。
- reasoning 不入交付欄（工作簿無此欄），本 override 只管批次
  JSON 工件與審查流程。
