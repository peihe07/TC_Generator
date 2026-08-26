# 下放包 02 — Bed Lowering Mode：feature 佈線與工作簿起建

日期：2026-08-26
Feature slug：`bed_lowering`
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 僅有 `01_intake_recon.md`，故取 02（R-G23′ live 取號）
對象：執行層（Tier 1）
前置狀態：**阻斷項已全數清空**（A-BLM4 已裁、A-BLM3 已驗、framework 已鎖並通過 R-G10）

---

## 一、本包之前提（分析層已完成，執行層不需重做）

| 項 | 狀態 | 落點 |
|---|---|---|
| 裁決 R-BLM1 ~ R-BLM6 | 已落檔 | `features/bed_lowering/RULINGS.md` |
| framework 三層 | **LOCKED**，Part III 通過 R-G10 | `features/bed_lowering/framework.md` |
| profile（含 `[OVERRIDE IN §10.7(b)]`）| 已落檔 | `docs/runtime/profiles/FW036_R1L_BedLowering_Profile.md` |
| 異常 A-BLM1 ~ A-BLM5 | 3 RESOLVED／1 ACCEPTED／1 PENDING（A-BLM2）| `features/bed_lowering/ANOMALIES.md` |
| 來源檔與雜湊 | 三檔齊，`INPUTS.sha256` 已入版控 | `features/bed_lowering/inputs/` |

---

## 二、`feature.yaml` 佈線

於 `features/bed_lowering/feature.yaml` 建立，鍵值如下。
**G-C：宣告與生效須分得開** —— 凡本檔宣告而工作簿不帶之值，記 `{value, applied, why}`。

```yaml
feature: Bed Lowering Mode          # R-BLM1
slug: bed_lowering                  # R-BLM1
test_group: Bed Lowering Mode       # R-BLM1，工作簿 G 欄
frop: Vehicle Settings              # R-BLM1：上游程式歸類，不入任何 TC 欄位

profile: FW036_R1L_BedLowering_Profile

workbook_state: BLANK               # R-BLM3
form_template: forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx   # R-G1

spec_mode: hmi_logic_and_flow
spec_pdf: features/bed_lowering/inputs/Bed Lowering Mode HMI Logic and Flow R1 SR24 1A (June 21 2021).pdf   # R-BLM4：無後手標註之原始輸出
spec_sys1: features/bed_lowering/inputs/SYS1_HMI_Bed_Lowering_Mode_HMI_Logic_and_Flow_R1_SR24_1A_(June_21_2021).xlsx
rd_037: features/bed_lowering/inputs/FM-WI-FSM-037-A03-N1L-SWE1-BedLoweringMode-HMI-V0.1 STLA 報告.xlsx

spec_reference_template: literal_037_hmi_source_id   # R-BLM5，不構造、不補章節號

write_back:
  fill_test_group_set: true         # canon：BLANK -> FILL
  author_value: "PeiPYHsu"
  tc_ref_id_value: "NEW"

tc_id_pattern: "{project}-BLM-{NNN}"   # IN §10.3
```

**`spec_reference_template` 之值為新增枚舉**（既有 feature 用
`{檔名}_{章節號}` 或 CFTS 式）。若 `feature.yaml` schema 或
`prompt_builder` 不認得該值，**停下回報，不自行改 schema**（FO §0 escalation 4）。

---

## 三、工作簿起建

1. 自 R-G1 母本複製為 `features/bed_lowering/workbook/bed_lowering_00.xlsx`
2. **母本之 R 欄 design_method 下拉為 x14 擴充。以 `openpyxl` 存回即摧毀該下拉**
   （R-G1 註、A-UP09）。起建與後續寫回**一律採 XML 外科式修改**：
   zip 開檔 → 僅改 `xl/worksheets/sheet*.xml` 之目標儲存格 → 原樣重打包
3. 起建前後比對並回報原始 XML 計數：`<dataValidation`、`x14:dataValidation`、
   `<conditionalFormatting`、工作表數、drawing/chart rel 數。
   **只比對列數／公式／工作表數之檢查會全綠而漏掉 x14 損壞**（R-G1 註之實測）
4. 起建後回報 sha256

---

## 四、資料工件

1. `data/leaf_inventory.tsv` —— 176 leaf，欄位：`req_id`、`heading_id`(母號)、
   `test_set`、`title`、`description`、`sub_categorization`、`priority_037`、
   `verification_criteria`、`verification_method`
2. `data/heading_ledger.tsv` —— 42 Heading，標
   `No TC — Heading; refer to child IDs`（R-BLM2）
3. `data/test_set_map.tsv` —— 母號 → Test Set，**逐字取自 `framework.md` Part III**
   （FO §0 Tier 0「照抄不是判斷」）

**驗算（R-G10，執行層須自行重跑並附結果）**：
合計 leaf = 176、Heading = 42、餘數空、溢出空、無重複指派。
分析層之實測值見 §六，供對帳。**不符即停下回報，兩側皆查**（R-G16 精神）。

---

## 五、Pilot 批

- 範圍：**`Fault Handling` 全組 13 leaf**（母號 011／037／038）
- 選此組之理由：三個母號互相咬合（EVIC 失敗訊息、highlight 撤除、
  unsuccessful 訊息），能同時壓到 fault injection 設計法、
  §8.2.1 sibling 邊界、以及 R-BLM5 之 N 欄新寫法；規模小、缺件少
- **Pilot 為 Tier 2**（FO §0）：生成後停，不續批，交 Pei 逐 TC 審
- 退出準則依 R-G15
- 批次 manifest 須記 prompt 模板 sha256 與 exemplar 集 sha256（R-G19）
- 回報 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 現行 sha256（R-G20）

Pilot 通過後之批量與順序另包下放，不在本包預先配置。

---

## 六、預期數字（供對帳，R-G16／R-G8）

分子分母皆標明。母體限 `218 列`／`176 leaf`／`42 Heading`／`70 outline`(SYS1)。

| 指標 | 值 | 分母 |
|---|---|---|
| 037 資料列 | 218 | — |
| Heading | 42 | 218 |
| leaf（TC 生成母體）| 176 | 218 |
| Sub Categorization = HMI | 134 | 176 |
| Sub Categorization = Service | 42 | 176 |
| Test Set 數 | 9 | — |
| 各 Test Set leaf 數 | 31／28／33／20／13／13／9／22／7 | 176 |
| SYS1 Polarion 物件 | 70 | — |
| N 欄相異值數（預期）| **1** | 176（R-BLM5）|

---

## 七、已知缺件與生成期注意

1. **DR-1 速度門檻**：規格 `*XX MPH`，明載由 chassis engineering 定義。
   受影響 leaf 約 13（BLM-007-01~04、BLM-021、BLM-022 等，**生成時逐列確認，
   此數為估算未逐列驗**）。依 IN §8.4.3 落 `PENDING: DR-1 BLM operating speed
   threshold value`，不造值
2. **DT vs DJ/D2 變體軸**：BLM-001／002／041。PROXI 車型參數寫法待查
   `forms/` 對照；查無即登 DR，不自造
3. **人因群**（BLM-013~017、023，共 29 leaf）：可功能化者生成；
   純設計驗證者入 coverage gap disclosure table（R-BLM2）
4. **訊號寫法**：依 IN §8.7.5 v3。DBC 查無者依 (d)／(g) 保留來源名，不代以近似訊號
5. **EVIC 文案**：規格 slide 7 有連續雙引號瑕疵；以 SYS1 Basic Report
   （NRL-193702）之正規化文字為準

---

## 八、未結 DR 清單（IN §8.4.3，每包附列）

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value（spec `*XX MPH`，owner: chassis engineering）| 已登記，未送出 |

---

## 九、分析層自陳 —— 本包應驗而未驗者

**「這一項現在驗得了嗎？」逐項自問之結果**（FO 之自陳規則）：

1. **`feature.yaml` schema 是否接受 `spec_reference_template: literal_037_hmi_source_id`**
   —— **未驗，且驗不了**：schema 定義在 `backend/`，分析層無執行環境。
   已於 §二寫明「不認得就停下回報」，不預設它會過
2. **DR-1 受影響 leaf 數「約 13」** —— **驗得了而未驗**。
   該數字來自下放包 01 之估算，本包沿用未重算。
   理由：其精確值不影響本包之任何動作（工作簿起建與 pilot 批皆不含該群），
   生成期逐列確認即可。**但它現在是個未驗數字，不得被當作已驗引用**
3. **Pilot 選 `Fault Handling` 是否為最佳選擇** —— 屬判斷，非可驗項。
   已於 §五寫明選擇理由，Pei 得改指定他組
4. **`forms/` 之 PROXI 車型參數對照是否存在** —— **驗得了而未驗**：
   分析層可讀 `forms/`，但本包不含生成動作，且該查詢屬生成期。
   **具名留在此處**，生成期首批須先查再寫，不得到時才發現
