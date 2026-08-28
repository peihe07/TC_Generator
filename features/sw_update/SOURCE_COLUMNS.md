# SOURCE_COLUMNS — SW Update 素材欄位全覽（R-SU26）

**R-SU26(a)**：任一來源檔於首次使用前，須產出欄位全覽 ——
欄序、標頭原文、非空列數、值之型態摘要。
**R-SU26(b)**：逐欄標記 `已用`／`不用（理由）`／`未定`；
**`未定` 不得留存跨輪**，下一輪須裁為前二者之一。
**R-SU26(d)**：**掃描寫得再全，掃的範圍是自己選的。**
「掃了但沒命中」與「根本沒掃到那一欄」須可分辨 —— 本表即其分辨之依據。

> ⚠ **本檔為人手維護之台帳，非 `recon.py` 之產物。**
> `RECON.md` 檔首載明其由 `recon.py` 生成，**故不於該檔手改**
> （手改將於下次重生時失去，且違其生成物之語意）。
> `framework.md` 之射程為三層框架，非素材欄位，故亦不載本表。

---

## 用途統計（2026-08-28，R-SU28 裁定後）

| 素材 | 欄數 | 已用 | 不用 | **未定** |
|---|---:|---:|---:|---:|
| 037 `AnalysisReport_FULL` | 18 | **8** | **6** | **4** |
| SYS1 `Basic Report` | 7 | 2 | 0 | **5** |
| 036 母本 TC 分頁（非空標頭） | 33 | **17** | 1 | **15** |
| **合計** | **58** | **27** | **7** | **24** |

**未定 24 欄（41%）** —— R-SU26(b) 令下一輪全部裁為 `已用` 或 `不用（理由）`。
其中 037 之 4 欄已備抽樣材料（T35b）、036 之 `T`–`Z` 七欄已備他 feature 之填值實測（T35c）。

---

## 037 `AnalysisReport_FULL`（18 欄）

來源：`AnalysisReport_FULL`，表頭列 7、資料列 8 起，全 **383** 資料列；驗證母體 **311** 列。

| 欄 | 標頭原文 | 非空（383） | 非空（311 母體） | 值型態摘要 | 用途 |
|---:|---|---:|---:|---|---|
| 0 | `SWE-Requirement ID` | 383 | 311 | 自由文字，unique 383，長度中位 13 | **已用** —— `req_id`／全案之列 id（R-SU3） |
| 1 | `Source Requirement ID` | 383 | 311 | 自由文字，unique 374，長度中位 15 | **不用** —— R-SU5 v2：三形態並存，該欄不取為 spec_reference |
| 2 | `Requirement Title` | 382 | 311 | 自由文字，unique 372，長度中位 47 | **已用** —— Layer 2 切分之材料（T28a／T28b）；TC 不 verbatim 抄 |
| 3 | `Requirement Description` | 382 | 311 | 自由文字，unique 376，長度中位 286 | **已用** —— 路徑 A 之查詢側（R-SU12）、TC `test_item` 上半之 verbatim 來源 |
| 4 | `Release Version` | 319 | 311 | 枚舉 `1.0.0`／`1.00.0` | **不用** —— **R-SU28(a)**：值域為二（`1.0.0`／`1.00.0`）且其差為寫法之別，無鑑別力 |
| 5 | `Categorization` | 382 | 311 | 枚舉 `Functional Requirement`／`Heading`／`Information`／`Non Functional Re | **已用** —— in-scope 判定（FR／NFR／Heading，R-SU3） |
| 6 | `Sub Categorization` | 310 | 310 | 枚舉 `HMI`／`Service` | **已用** —— HMI／Service 之分面（T28c、原則 3） |
| 7 | `Feasibility` | 311 | 311 | 枚舉 `Yes` | **不用** —— **R-SU28(a)**：常數欄（全 `Yes`），無鑑別力 |
| 8 | `Description/Action for Feasibility` | 311 | 311 | 自由文字，unique 138，長度中位 66 | **未定** —— **R-SU28(b)：待抽樣後裁**（自由文字且 unique 高；「其母欄為常數」不蘊含「其說明欄無內容」） |
| 9 | `Impact` | 311 | 311 | 枚舉 `Yes` | **不用** —— **R-SU28(a)**：常數欄（全 `Yes`），無鑑別力 |
| 10 | `Description/Action for Impact` | 311 | 311 | 自由文字，unique 191，長度中位 129 | **未定** —— **R-SU28(b)：待抽樣後裁**（自由文字且 unique 高；「其母欄為常數」不蘊含「其說明欄無內容」） |
| 11 | `Risk Factor` | 311 | 311 | 枚舉 `Medium` | **不用** —— **R-SU28(a)**：常數欄（全 `Medium`），無鑑別力 |
| 12 | `Description/Action for Risk Factor` | 311 | 311 | 枚舉 `The requirement is abl` | **未定** —— **R-SU28(b)：待抽樣後裁**（自由文字且 unique 高；「其母欄為常數」不蘊含「其說明欄無內容」） |
| 13 | `Reusable` | 311 | 311 | 枚舉 `Fully (100%)`／`High (>= 50%)` | **不用** —— **R-SU28(a)**：SWE.1 之再用性評估，與 TC 之驗證內容無關 |
| 14 | `Description/Action for Reusable` | 311 | 311 | 自由文字，unique 115，長度中位 85 | **未定** —— **R-SU28(b)：待抽樣後裁**（自由文字且 unique 高；「其母欄為常數」不蘊含「其說明欄無內容」） |
| 15 | `Priority` | 311 | 311 | 枚舉 `High`／`Low`／`Medium` | **已用** —— R-SU22：僅作參考訊號，不作 P 值之唯一依據 |
| 16 | `Verification Criteria` | 310 | 310 | 自由文字，unique 309，長度中位 365 | **已用** —— **R-SU27(a)：R-SU25(c) 外部可觀測後果之候選來源**（本輪起） |
| 17 | `Verification Method` | 311 | 311 | 自由文字，unique 26，長度中位 42 | **已用** —— **R-SU27(b)：測試層級之參考訊號**（本輪起） |


### ⚠ `未定` 清單（037，4 欄）—— R-SU28(b)：待抽樣後裁

| 欄 | 標頭原文 | 非空（311 母體） | unique |
|---:|---|---:|---:|
| 8 | `Description/Action for Feasibility` | 311 | 138 |
| 10 | `Description/Action for Impact` | 311 | 191 |
| 12 | `Description/Action for Risk Factor` | 311 | 1 |
| 14 | `Description/Action for Reusable` | 311 | 115 |

抽樣材料見 `docs/upstream/21_coverage_split.md` §T35b。

### SYS1 export（`Basic Report`，120 資料列，7 欄）

| 欄 | 標頭原文 | 非空 | 值型態摘要 | 用途 |
|---:|---|---:|---|---|
| 0 | `ID` | 120 | 自由文字，unique 120 | **未定** —— 未讀 |
| 1 | `Space / Document` | 120 | 枚舉 `Requirements / SYS` | **未定** —— 未讀 |
| 2 | `Outline Number` | 120 | 自由文字，unique 120 | **已用** —— R-SU11：SYS1 之接點為 HMI 87 列；T18b 分群 |
| 3 | `Description` | 120 | 自由文字，unique 118 | **已用** —— T18b／T18d 之比對側 |
| 4 | `SYSRE_HMI_Source ID` | 120 | 自由文字，unique 120 | **未定** —— 未讀 |
| 5 | `Type` | 120 | 枚舉 `SYSRE_HMI` | **未定** —— 未讀 |
| 6 | `_polarion` | 120 | 自由文字，unique 120 | **未定** —— 未讀 |

### 036 母本（`Test Case Specification 測試用例規範`，表頭列 9，34 欄）

| 欄 | 標頭原文 | 用途 |
|---|---|---|
| `B` | No.# ／ 序號 | **不用** —— 共用公式之宿主（`t="shared"` 1401 處），賦值即毀 |
| `C` | Requirement or Design ／ ID (Polarion) ／ 設計/需求 ID (Po | **未定** —— 未讀 |
| `D` | Requirement or Design ID ／ 需求/設計 ID | **已用** —— `req_id`（`feature.yaml` §workbook.columns） |
| `E` | Test Case ID (TestRail) ／ 測試用例 ID (TestRail) | **未定** —— 未讀 |
| `F` | Test Case ID ／ 測試用例ID | **已用** —— TC ID（R-SU24；`feature.yaml` 未列，實測 `F9`） |
| `G` | Test Group ／ 測試組 | **已用** —— `test_group`（`feature.yaml` §workbook.columns） |
| `H` | Test Set ／ 測試集 | **已用** —— `test_set`（`feature.yaml` §workbook.columns） |
| `I` | Test Item ／ 測試項目 | **已用** —— `test_item`（`feature.yaml` §workbook.columns） |
| `J` | Pre-Conditions ／ 先前條件 | **已用** —— `pre_conditions`（`feature.yaml` §workbook.columns） |
| `K` | Input Test Data ／ 輸入條件 | **已用** —— `input_test_data`（`feature.yaml` §workbook.columns） |
| `L` | Test procedure ／ 測試程序 | **已用** —— `test_procedure`（`feature.yaml` §workbook.columns） |
| `M` | Expected Result ／ 預期結果 | **已用** —— `expected_result`（`feature.yaml` §workbook.columns） |
| `N` | Specification Reference  ／ 規格參考 | **已用** —— `spec_reference`（`feature.yaml` §workbook.columns） |
| `O` | Test Case Reference ID ／ 測項參考ID | **已用** —— `tc_ref_id`（`feature.yaml` §workbook.columns） |
| `P` | Test Case Priority ／ 測試用例優先級別 | **已用** —— `priority`（`feature.yaml` §workbook.columns） |
| `Q` | Estimated Test Time (mins) ／ 預估測試時間 ／ （分鐘） | **已用（工具側）** —— `RECON.md` §Workbook 已解析 `estimated_test_time = Q`；**`feature.yaml` 未列**，寫回是否填未裁 |
| `R` | Test Case Design  ／ Methods ／ 測試用例設計方法 | **已用** —— `design_method`（`feature.yaml` §workbook.columns） |
| `S` | Functional Safety ／ 功能安全 | **已用（欄已映射）** —— `functional_safety`；**母本無 DV**（T35c 實測）；他 feature 之交付本 5/6 填 `NA`。本 feature pilot 未填，值域未裁 |
| `T` | HDCC27 ／ Atl-Hi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `U` | DT27 ／ Atl-Hi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `V` | VF(ProMaster)637 ／ Atl-Mi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `W` | Commander (598) ／ Atl-Mi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `X` | Regengade (5210) ／ Atl-Mi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `Y` | Toro(2261) ／ Atl-Mi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `Z` | Fastack (376) ／ Atl-Mi | **未定** —— **車型適用旗標**，DV `T10:Z1411` = `"0,1"`（T35c）；他 feature 之交付本**全部留空**。填法未裁 |
| `AA` | Test Case Author ／ 測試案例作者 | **已用** —— `author`（`feature.yaml` §workbook.columns） |
| `AB` | Test Version ／ 測試版號 | **未定** —— 未讀 |
| `AC` | Test Vehicle ／ (Bench) ／ 測試車型(Bench) | **未定** —— 未讀 |
| `AD` | Test Period ／ 測試期間 | **未定** —— 未讀 |
| `AE` | Tester ／ 測試者 | **未定** —— 未讀 |
| `AF` | Test Result ／ 測試結果 | **未定** —— 未讀 |
| `AG` | Defect ID ／ 缺陷ID | **未定** —— 未讀 |
| `AH` | Remarks ／ 備註 | **已用** —— `remarks`（`feature.yaml` §workbook.columns） |

### 文字型素材之結構元素（CFTS_57／SYSAD／VF747／HMI PDF）

| 素材 | 已用之結構元素 | 未用之結構元素 |
|---|---|---|
| **CFTS_57**（docx） | heading style 1–4 之 `{7位}` 章節（87）；`[Artifact Type:Subsystem Functional Requirement]` 宣告之需求物件（487）；其後至下一宣告之全文（語料 v2） | **表格**（`<w:tbl>`）、**圖**（drawing）、註腳、`[Artifact Type:…]` 之**其他型別**（Description 137 已用其歸屬，其餘型別未列）、修訂標記 |
| **SYSAD**（docx） | 迄今**僅作 T33c 之全文語形掃描** | 章節結構、介面節、架構圖、**全部表格** |
| **VF747**（docx） | 已綁 `reference.vf747`；**內容未讀** | 全部 |
| **HMI 規格 PDF** | R-SU6 v2：真 PDF、68 頁全文字層；T5' 之 popup id 抽取（52 個） | 頁面版面、圖、**全文之語意內容** |
