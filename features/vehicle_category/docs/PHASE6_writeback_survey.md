# Phase 6 寫回前置勘查 —— 036 母本（下放包 27 T144）

- 日期：2026-08-27
- 母本：`inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
  Specification & Result_SWQT_20260817_ext.xlsx`
  （SHA256 `6372fb6be02f48dc…`，200,650 bytes）
- **只讀。母本未被開啟寫入、未被 save、未修改任何一格。**
  §5 之寫回實測於 `/tmp` 之副本上為之。

---

## (a) 分頁結構

| # | 分頁 | 用途 | dims | 合併 | DV |
|---|---|---|---|---|---|
| 1 | `Cover_old` | 舊版封面（殘留）| A1:J15 | 1 | 0 |
| 2 | `ChangeHistory_old` | 舊版履歷（殘留）| A1:J12 | 46 | 0 |
| 3 | `Cover 封面` | 現行封面 | A4:H30 | 10 | 0 |
| 4 | `ChangeHistory 修訂履歷` | 現行履歷 | A1:E17 | 1 | 0 |
| 5 | `Product Document 記錄封面頁` | 文件記錄 | A1:H16 | 9 | 1 |
| **6** | **`Test Case Specification 測試用例規範`** | **TC 本體** | **A1:AH1411** | **4** | **3 ＋ x14 1** |
| 7 | `Reference` | 9 種設計方法之說明與例 | B3:F20 | 0 | 0 |
| 8 | `QS Suggestion` | QS 之 9 項改版建議 | A1:B10 | 1 | 0 |
| 9 | **`下拉選單`** | **設計方法之值域（A1:A9）** | A1:A11 | 0 | 0 |

- **凍結窗格：全部分頁皆無**（`freeze_panes = None`）。
- **條件式格式：全部分頁皆無。**
- 分頁 6 之合併僅 4 處，皆在表頭區：`A1:AE1`／`B7:AA7`／`AB7:AH7`／`T8:Z8`
  —— **資料區（row 10 起）無合併儲存格**。
- 命名範圍：`Competencies` 一個。

**資料列起始**：表頭在 **row 9**，資料自 **row 10** 起，模板預備至 **row 1411**
（1402 列）。

---

## (b) 欄位映射 —— 逐欄

| 欄 | 表頭 | TC JSON 之來源 | 備註 |
|---|---|---|---|
| A | （無標題，寬 2.8）| — | 版面留白，不寫 |
| B | `No.#` 序號 | — | **公式** `=IF(ISBLANK($D{r}),"",ROW()-9)`，1402 列已預填。**不得覆寫** |
| C | `Requirement or Design ID (Polarion)` | `data/recon_leaf_to_section.tsv` 之 `polarion_id` | ⚠ **不在 TC JSON 內**，須自 recon 表帶入 |
| D | `Requirement or Design ID` | `leaf_id` | B 欄公式之判斷依據 |
| E | `Test Case ID (TestRail)` | — | **無來源** |
| F | `Test Case ID` | — | **無來源**，見 (f) |
| G | `Test Group` | `test_group` | |
| H | `Test Set` | `test_set` | |
| I | `Test Item` | `test_item` | 含空行之二段式 |
| J | `Pre-Conditions` | `pre_conditions` | |
| K | `Input Test Data` | `input_test_data` | |
| L | `Test procedure` | `test_procedure` | |
| M | `Expected Result` | `expected_result` | |
| N | `Specification Reference ` | `specification_reference` | 表頭末有一個尾隨空格 |
| O | `Test Case Reference ID` | — | **無來源** |
| P | `Test Case Priority` | `priority` | DV `"P0,P1,P2,P3"` —— **與我方值域完全相符** |
| Q | `Estimated Test Time (mins)` | — | **無來源**；⚠ 見 (d) 之模板缺陷 |
| R | `Test Case Design Methods` | `design_method` | ⚠ **x14 DV**，見 (d) |
| S | `Functional Safety` | `functional_safety` | 無 DV；我方值域僅 `NA` |
| T–Z | 7 個車型（`HDCC27`／`DT27`／`VF(ProMaster)637`／`Commander (598)`／`Regengade (5210)`／`Toro(2261)`／`Fastack (376)`）| — | **無來源**，DV `"0,1"` |
| AA | `Test Case Author` | — | **無來源** |
| AB–AH | `Test Version`／`Test Vehicle`／`Test Period`／`Tester`／`Test Result`／`Defect ID`／`Remarks` | — | **執行階段欄位，本次不寫**；AF 有 DV `"Pass, Fail, Pending,Block,NA"` |

### (b.1) TC JSON 有值而**母本無欄**者

| JSON 欄 | 狀態 |
|---|---|
| `reasoning` | **無對應欄**。唯一形式上可能之去處為 `AH 備註`，但那是執行階段欄位 |
| `distinguishing_axis` | **無對應欄** |
| `split_flag`／`split_reason` | **無對應欄**（且 profile §11 已裁本 feature 恆 `False`／空）|

**`reasoning` 是本次生成之主要判讀紀錄，而母本沒有它的位置。**
其去處須另裁 —— 併入 `AH`、另立側檔、或不隨工作簿交付。

### (b.2) 值域相符實測

- `design_method`：我方用 **6 種**，**6 種皆在 `下拉選單!A1:A9` 內**（逐字相符）。
- `priority`：我方 `P0`–`P3`，**與 P 欄 DV 逐字相符**。
- `functional_safety`：我方僅 `NA`，S 欄無 DV，不生衝突。

---

## (c) 既有內容之狀態

**母本為空模板。**

- C–AH 欄自 row 10 至 row 1411 **全空**（逐格掃描，0 格有值）。
- B 欄 1402 列**只有公式**，無值。
- 故**無既有 TC、無既有序號**，寫回不涉與他人資料之併存。

---

## (d) ⚠ 下拉／資料驗證 —— 本項為寫回之最大風險

### (d.1) 標準 `dataValidation`（openpyxl 讀得到）

| 分頁 | 範圍 | 型 | 值域 |
|---|---|---|---|
| `Product Document` | `B7:C7` | list | `"Confidential, Top Secret"` |
| **TC 本體** | `P10:Q1411` | list | `"P0,P1,P2,P3"` |
| **TC 本體** | `T10:Z1411` | list | `"0,1"` |
| **TC 本體** | `AF10:AF1411` | list | `"Pass, Fail, Pending,Block,NA"` |

### (d.2) ⚠⚠ **x14 擴充 `dataValidation`（openpyxl 讀不到）**

母本 `xl/worksheets/sheet6.xml` 之 `<extLst>` 內，逐字：

```xml
<x14:dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1">
  <x14:formula1><xm:f>下拉選單!$A$1:$A$9</xm:f></x14:formula1>
  <xm:sqref>R10:R1411</xm:sqref>
</x14:dataValidation>
```

**`R` 欄（Test Case Design Methods）之下拉是 x14 擴充，其清單來源為
`下拉選單` 分頁之 `$A$1:$A$9`（跨分頁 range）。**

- `openpyxl` **看不見它** —— `ws.data_validations` 只回報 3 條，不含此條。
- 載入時 openpyxl 直接警告：
  `UserWarning: Data Validation extension is not supported and will be removed`

**而 `R` 欄正是我方要寫入的欄之一。**

### (d.3) 模板缺陷（非我方造成，記明）

- **`P10:Q1411` 共用同一條 DV** —— `Q` 欄是「預估測試時間（分鐘）」，
  卻掛著 `"P0,P1,P2,P3"` 的下拉。**該欄之 DV 顯為誤設。**
- `Reference` 分頁第 6 項作 `Pair-wise / N-wise`，
  `下拉選單` 第 6 項作 `Pairwise / t-wise` —— **同一份活頁簿內二種寫法**。
  我方未用該項，不生影響，記明以免日後誤判。
- `QS Suggestion` 第 4 項：「Priority 與 SWRA 分法統一呈現，
  高 High、中 Medium、低 Low、不適用 NA」——
  **若該建議被採納，P 欄之值域將由 `P0–P3` 改為 `High/Medium/Low/NA`，
  我方 121 筆之 `priority` 全數須重映射。** 該建議日期為 25/10/15，狀態不明。

---

## (e) 合併／凍結／條件式格式

- 合併：資料區（row 10+）**無**；表頭區 4 處已列於 (a)。
- 凍結窗格：**無**（捲動時表頭不固定，非我方之事）。
- 條件式格式：**無**。
- row 9 列高 56；row 10 起未設列高（隨內容）。
- 資料格樣式（樣本 `J10`）：`wrap_text=True`、垂直置中、細框線 ——
  **模板已預設好格式，逐格寫入可直接繼承**。

---

## (f) TC ID 之既有形態

- `E`（TestRail）與 `F`（Test Case ID）**皆空，無既有序號**，故無「現有最大序號」。
- IN §10.3 之形態為 `{project}-{abbr}-{NNN}`。
  本 feature 之 `{project}`／`{abbr}` **未定** ——
  六批 JSON 之 `tc_id_status` 皆為 `provisional`，**且 JSON 內無 `tc_id` 欄**。
- **TC ID 之編定為寫回之前置，本包未做、未提案。**

---

## (g) 寫回方式之候選（**只列不選**）

### (g.1) 三個候選

| 案 | 作法 | 已實測之後果 |
|---|---|---|
| **甲** | `openpyxl` 載入 → 寫格 → `save()` 全量重寫 | ⚠ **見 (g.2)，實測有破壞** |
| **乙** | 逐格寫入後仍走 openpyxl `save()` | **與甲同** —— openpyxl 之破壞發生在 load／save，與寫幾格無關 |
| **丙** | 解壓 xlsx → 直接改 `xl/worksheets/sheet6.xml` 與 `sharedStrings` → 重新打包 | 未實測。保留 `extLst` 與所有 zip 項目，但須自行處理字串表與樣式索引 |

### (g.2) ⚠ 甲／乙之破壞已實測（副本上，母本未動）

以母本副本跑 `openpyxl.load_workbook()` → `save()`，**不改任何一格**，
比對前後之 zip 內容：

| 量 | 母本 | load→save 後 | 判 |
|---|---|---|---|
| 標準 `<dataValidation>` | 4 | 4 | 保留 |
| **`x14:dataValidation`（擴充）** | **2** | **0** | **全毀** |
| **`<extLst>`** | **1** | **0** | **全毀** |
| `xl/printerSettings/*.bin` | 5 | **0** | 列印設定全失 |
| `xl/calcChain.xml` | 有 | 無 | （可接受，Excel 會重算）|
| `xl/comments1.xml`／`vmlDrawing1.vml` | 有 | 改名重寫 | 註解形態改變 |
| 圖片 | `image2.jpeg` | `image2.png` ＋ 7 個新 jpeg | 圖片被重新編碼 |
| 檔案大小 | 200,650 | 205,856 | +5,206 |

**即：什麼都不改、只是開了再存，`R` 欄之設計方法下拉就消失了。**

> 這與下放包 §2.3 所述之「PM 線曾因下拉毀損而需外科式修改」**同一成因**。
> 本次是在寫回之前先量到，而不是寫壞之後才知道。

### (g.3) 未評估者（記明，不臆測）

- **丙案未實測** —— 其可行性、樣式索引之處理、`sharedStrings` 之增補
  皆未驗證。本包不主張它可行。
- 是否有第四條路（如以 Excel／LibreOffice 巨集寫入、或改用
  `xlsxwriter` 自零產生新檔並人工搬移格式）**未評估**。
- **母本是否為唯一交付形態**（能否改以另存新檔交付）未問 ——
  若可另存，甲案之破壞範圍需重新評估。

---

## 已知限制（R-G8）

- 本勘查以 `openpyxl` 讀取 ＋ 直接解 zip 讀 XML 為之。
  **`openpyxl` 讀不到的東西，只有在我另外去讀 XML 時才會出現** ——
  (d.2) 即為一例。**故不能排除還有其他 openpyxl 不解析、
  而本次也沒想到要去 XML 裡找的結構。**
- (g.2) 之實測為**同一支 openpyxl 版本**（本 repo `.venv`）之行為，
  非 openpyxl 之通則。換版本可能不同。
- 母本 SHA256 已記於檔頭；**本包未對母本做任何寫入**，
  實測皆在 `/tmp/036_probe.xlsx` 副本上。
