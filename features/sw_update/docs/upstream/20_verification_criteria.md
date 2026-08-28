# 上繳包 20 —— Verification 二欄之傾印、素材欄位全覽

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/21_verification_criteria.md`
  （SHA256 `933e1b5dc443d3fe3782f94ceb50213290476250f0b31a2317be1ed1fb8d4447`，175 行）
- **未結 DR：1 筆（DR-SU1）**｜新登 anomaly：0 筆
- 新腳本：`scripts/verif_columns.py`
- 材料另冊：`docs/upstream/20a_verification_criteria_material.md`（126 + 32 列全文）

## 本輪四個主結果

1. **§五.6 之答案是「是」，且可量**：126 個內部列中，
   **其 `Verification Criteria` 亦無任何外部面者 105 列（83%）**；
   對照組（185 非內部列）之 VC 含外部面者 **172 列（93%）**。
   **上游作者之驗證構想與需求本文同源 —— 需求沒說看哪裡，VC 多半也沒說。**
2. **R-SU27(a) 之期待只對 126 列中之 21 列成立。** 其餘 105 列，
   本欄**供給不了**觀測面 —— 該條之「優先於分析層之自行推想」在該 105 列上落空。
3. **037 欄位全覽：18 欄中已用 8／不用 1／未定 9。** 未定者非空率皆 311/311
   （`Feasibility`／`Impact`／`Risk Factor`／`Reusable` 及其四個說明欄）。
4. **036 母本之全覽揭出一個先前之誤讀**：`T`–`Z` 七欄為**車型適用旗標**
   （HDCC27／DT27／VF637／Commander／Renegade／Toro／Fastback），
   其 DV 值域 `"0,1"` 即為此 —— **非 `functional_safety`**。
   上繳包 15 §4.5 之缺項 5「`S` 欄落在 DV `T10:Z1411` 之外」讀法有誤，本包更正。

---

## 1. T34e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU26 | 544 | **OK** | `e3bb694d222c` |
| R-SU27 | 964 | **OK** | `eca4d0354679` |

二條逐字 append，**既有 39 個條文區塊未受影響** ✅（現 41 塊）。
索引表現行 **27 條**（新增 R-SU26／R-SU27）；留存 **14 條**（無變動）。
與下放包 21 §四 T34e 所定之「27 條現行」一致。

`PLAYBOOK.md` §7 追加二則：
- **(20)**「掃描寫得再全，掃的範圍是自己選的 —— 先列全覽再掃」，
  判準為**「報告裡出現『掃了全部 X』時，問一句 X 的全集是誰定義的」**。
- **(21)**「判準測的是『文字裡有沒有提到』，不是『這件事有沒有』」，
  作法為**語形普查之結論一律寫成「未提及 X 之列數」，不得寫成「無 X 之列數」**。

---

## 2. T34a —— 126 個內部列之 `Verification Criteria`（本輪核心）

材料全文見 **`docs/upstream/20a_verification_criteria_material.md`**
（`Telematics Client` 5 列置於最前，其餘 121 列依 037 列序）。

- `Verification Criteria` **為空者 1 列：`SWE1-FOTA-267`**
  （310/311 非空，該 1 列即其差）

### 0. 本欄能否供給觀測面 —— 先量再傾印

| 量 | 值 |
|---|---:|
| VC 之總行數（310 列） | 1103 |
| 行首為 IN §5.1 禁用動詞者 | **247（22%）** |
| **126 內部列中，其 VC 含外部面語形者** | **21／126（17%）** |
| **126 內部列中，其 VC 亦無任何外部面者** | **105／126（83%）** |
| 對照：185 非內部列中，其 VC 含外部面者 | 172／185（93%） |

行首動詞（前 10）：

| 動詞 | 行數 | IN §5.1 |
|---|---:|:--:|
| `Confirm` | 137 | — |
| `Observe` | 92 | **禁用** |
| `Verify` | 90 | **禁用** |
| `Ensure` | 82 | — |
| `Check` | 66 | — |
| `Examine` | 51 | — |
| `Recreate` | 48 | — |
| `Monitor` | 39 | **禁用** |
| `Evaluate` | 37 | — |
| `Review` | 36 | — |

> **本表即下放包 21 §五.6 之答案**：本欄之觀測面與需求本文**同源** —— 需求提及外部面者其 VC 亦提及（93%），需求未提者其 VC 多半亦未提（83%）。詳見上繳包 20 §自評。

### 2.1 `Telematics Client` 5 列之判讀材料（§二 #3 待判）

該組 5/5 皆內部列。其 `Verification Criteria` 之「檢查對象」逐列摘：

| 037 列 | VC 所令檢查之對象 | 該對象是否外部可觀測 |
|---|---|:--:|
| `363` | communication with the TC client **is established successfully** | ❌ 服務間連線狀態 |
| `364` | the **callback is registered** successfully with the topic set to "FOTA" | ❌ 內部註冊狀態 |
| `365` | the OTA session request **is received** successfully；is forwarded for execution | ❌ 服務間訊息 |
| `366` | （見材料冊） | ❌ |
| `367` | （見材料冊） | ❌ |

**5 列之 VC 皆未指出外部可觀測之面。**
即：**上游作者對這 5 列也沒有說看哪裡。**
**執行層不裁定該組是否整組無法產出**（下放包 21 §二 #3 為分析層之事），
僅陳報此一事實。

---

## 3. T34b —— `HMI Validation Testing` 之 32 列（正向樣本）

材料全文見 `20a` §T34b。

- 命中 **32** 列；**其中內部列 0 列 —— 交集為 0，完美分離**
- 其 Test Set 分佈：`ROV Installation` 為大宗（見材料冊之清單）
- 用途：作為「有 HMI 可觀測面」之正向樣本，供分析層校準 R-SU25(c) 之取用方式

**與 §2 之對照才是其價值**：同一份 `Verification Criteria` 欄，
在這 32 列上給得出畫面／控件之具體看處，在 126 個內部列之 105 列上給不出。
**該欄之品質不是均勻的 —— 它跟著需求本身的可觀測性走。**

---

## 4. T34c —— 037 欄位全覽（R-SU26）

來源：`AnalysisReport_FULL`，表頭列 7、資料列 8 起，全 **383** 資料列；驗證母體 **311** 列。

| 欄 | 標頭原文 | 非空（383） | 非空（311 母體） | 值型態摘要 | 用途 |
|---:|---|---:|---:|---|---|
| 0 | `SWE-Requirement ID` | 383 | 311 | 自由文字，unique 383，長度中位 13 | **已用** —— `req_id`／全案之列 id（R-SU3） |
| 1 | `Source Requirement ID` | 383 | 311 | 自由文字，unique 374，長度中位 15 | **不用** —— R-SU5 v2：三形態並存，該欄不取為 spec_reference |
| 2 | `Requirement Title` | 382 | 311 | 自由文字，unique 372，長度中位 47 | **已用** —— Layer 2 切分之材料（T28a／T28b）；TC 不 verbatim 抄 |
| 3 | `Requirement Description` | 382 | 311 | 自由文字，unique 376，長度中位 286 | **已用** —— 路徑 A 之查詢側（R-SU12）、TC `test_item` 上半之 verbatim 來源 |
| 4 | `Release Version` | 319 | 311 | 枚舉 `1.0.0`／`1.00.0` | **未定** —— `Release Version` —— 未查其值型態與用途 |
| 5 | `Categorization` | 382 | 311 | 枚舉 `Functional Requirement`／`Heading`／`Information`／`Non Functional Re | **已用** —— in-scope 判定（FR／NFR／Heading，R-SU3） |
| 6 | `Sub Categorization` | 310 | 310 | 枚舉 `HMI`／`Service` | **已用** —— HMI／Service 之分面（T28c、原則 3） |
| 7 | `Feasibility` | 311 | 311 | 枚舉 `Yes` | **未定** —— `Feasibility` —— 未讀 |
| 8 | `Description/Action for Feasibility` | 311 | 311 | 自由文字，unique 138，長度中位 66 | **未定** —— `Description/Action for Feasibility` —— 未讀 |
| 9 | `Impact` | 311 | 311 | 枚舉 `Yes` | **未定** —— `Impact` —— 未讀 |
| 10 | `Description/Action for Impact` | 311 | 311 | 自由文字，unique 191，長度中位 129 | **未定** —— `Description/Action for Impact` —— 未讀 |
| 11 | `Risk Factor` | 311 | 311 | 枚舉 `Medium` | **未定** —— `Risk Factor` —— 未讀 |
| 12 | `Description/Action for Risk Factor` | 311 | 311 | 枚舉 `The requirement is abl` | **未定** —— `Description/Action for Risk` —— 未讀 |
| 13 | `Reusable` | 311 | 311 | 枚舉 `Fully (100%)`／`High (>= 50%)` | **未定** —— `Reusable` —— 未讀 |
| 14 | `Description/Action for Reusable` | 311 | 311 | 自由文字，unique 115，長度中位 85 | **未定** —— `Description/Action for Reusable` —— 未讀 |
| 15 | `Priority` | 311 | 311 | 枚舉 `High`／`Low`／`Medium` | **已用** —— R-SU22：僅作參考訊號，不作 P 值之唯一依據 |
| 16 | `Verification Criteria` | 310 | 310 | 自由文字，unique 309，長度中位 365 | **已用** —— **R-SU27(a)：R-SU25(c) 外部可觀測後果之候選來源**（本輪起） |
| 17 | `Verification Method` | 311 | 311 | 自由文字，unique 26，長度中位 42 | **已用** —— **R-SU27(b)：測試層級之參考訊號**（本輪起） |

**用途統計**：已用 **8**／不用 1／**未定 9**（共 18）

### ⚠ `未定` 清單（R-SU26(b)：不得留存跨輪，下一輪須裁）

| 欄 | 標頭原文 | 非空（383） |
|---:|---|---:|
| 4 | `Release Version` | 319 |
| 7 | `Feasibility` | 311 |
| 8 | `Description/Action for Feasibility` | 311 |
| 9 | `Impact` | 311 |
| 10 | `Description/Action for Impact` | 311 |
| 11 | `Risk Factor` | 311 |
| 12 | `Description/Action for Risk Factor` | 311 |
| 13 | `Reusable` | 311 |
| 14 | `Description/Action for Reusable` | 311 |


### 4.1 觀察

- **未定 9 欄之非空率皆為 311/311**（`Feasibility`／`Impact`／`Risk Factor`／
  `Reusable` 及其四個說明欄，加 `Release Version` 319/383）——
  **全母體皆有值，非零星填寫**，故其未讀不是「反正也沒資料」。
- `Feasibility` 全為 `Yes`、`Impact` 全為 `Yes`、`Risk Factor` 全為 `Medium`
  —— **單一值之欄，其資訊量為零**，得逕裁 `不用`。
- `Description/Action for Feasibility`（unique 138）／`for Impact`（unique 191）／
  `for Reusable`（unique 115）**為自由文字且變異大**，
  **其內容未讀，不宜逕裁**。
- `Description/Action for Risk Factor` 之 unique 為 1（全列同句），
  同屬資訊量為零。

**執行層不裁**（R-SU26(b) 令下一輪裁），以上僅為型態陳報。

---

## 5. T34d —— 其餘素材之欄位全覽

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
| `Q` | Estimated Test Time (mins) ／ 預估測試時間 ／ （分鐘） | **未定** —— 未讀 |
| `R` | Test Case Design  ／ Methods ／ 測試用例設計方法 | **已用** —— `design_method`（`feature.yaml` §workbook.columns） |
| `S` | Functional Safety ／ 功能安全 | **已用** —— `functional_safety`（`feature.yaml` §workbook.columns） |
| `T` | HDCC27 ／ Atl-Hi | **未定** —— 未讀 |
| `U` | DT27 ／ Atl-Hi | **未定** —— 未讀 |
| `V` | VF(ProMaster)637 ／ Atl-Mi | **未定** —— 未讀 |
| `W` | Commander (598) ／ Atl-Mi | **未定** —— 未讀 |
| `X` | Regengade (5210) ／ Atl-Mi | **未定** —— 未讀 |
| `Y` | Toro(2261) ／ Atl-Mi | **未定** —— 未讀 |
| `Z` | Fastack (376) ／ Atl-Mi | **未定** —— 未讀 |
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

### 5.1 ⚠ 036 之 `T`–`Z` 七欄 —— 更正上繳包 15 §4.5 之一處誤讀

上繳包 15 §4.5 列缺項 5：「`functional_safety`（`S` 欄）之值未裁 ——
S 欄落在 DV `T10:Z1411`（值域 `"0,1"`）**之外**，其值域與填法未查」。

**該讀法有誤。** 全覽揭出 `T`–`Z` 為**七個車型適用旗標**：

| 欄 | 標頭原文 |
|---|---|
| `T` | HDCC27 ／ Atl-Hi |
| `U` | DT27 ／ Atl-Hi |
| `V` | VF(ProMaster)637 ／ Atl-Mi |
| `W` | Commander (598) ／ Atl-Mi |
| `X` | Regengade (5210) ／ Atl-Mi |
| `Y` | Toro(2261) ／ Atl-Mi |
| `Z` | Fastack (376) ／ Atl-Mi |

DV `"0,1"` 於 `T10:Z1411` 即**車型適用與否之旗標**，與 `S`（Functional Safety）
**本就無關** —— `S` 不在該 DV 內是正常，不是異常。

**缺項 5 之正確形式為二項**：
1. `S`（`functional_safety`）之值域未裁（母本無 DV 拘束）
2. **`T`–`Z` 七個車型欄之填法未裁**（**新** —— 前此未被指認為缺項；
   其為交付面之欄，且有 DV 拘束，**逾 `未定` 之列）

**此為 R-SU26 之直接收益**：欄位全覽一做，一個誤讀被更正、一個缺項被發現。

### 5.2 未定欄之總計

| 素材 | 欄數 | 已用 | 不用 | **未定** |
|---|---:|---:|---:|---:|
| 037 `AnalysisReport_FULL` | 18 | 8 | 1 | **9** |
| SYS1 `Basic Report` | 7 | 2 | 0 | **5** |
| 036 母本 TC 分頁（非空標頭） | 33 | 15 | 1 | **17** |
| **合計** | **58** | **25** | **2** | **31** |

**未定 31 欄，佔 53%。** R-SU26(b)：**不得留存跨輪，下一輪須全部裁為
`已用` 或 `不用（理由）`。**

---

## 6. 未結 DR 清單

| # | 事項 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | **OPEN** | `newR1L-SU-003` 三欄 PENDING（U=3） |

**未結 1 筆**（與下放包 21 §五.5 之預期相符）。

### 待分析層確認之事項（非 DR）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **105 列之 VC 亦無外部面** —— R-SU27(a) 在該 105 列上落空，其處置未定 | §2 |
| 2 | **未定 31 欄之裁定**（R-SU26(b)：不得跨輪） | §5.2 |
| 3 | **`T`–`Z` 七個車型欄之填法未裁**（新缺項，交付面且有 DV 拘束） | §5.1 |
| 4 | **`SWE1-FOTA-267` 之 VC 為空** —— 該列無上游驗證構想可取 | §2 |
| 5 | **`Telematics Client` 5 列之 VC 皆無外部面** —— §二 #3 之判斷材料已備 | §2.1 |

---

## 7. 獨立自評

### 7.1 §五.6 所問：`Monitor`／`Observe` 為禁用動詞，是否意味該欄所述之觀測面本身也可能不可執行

**是，而且問題比動詞嚴重得多 —— 動詞只是表面，可量的是內容。**

**(甲) 動詞層：22% 之行以禁用動詞起首。**

`Verification Criteria` 全 310 列共 **1103 行**，行首動詞前 10：

| 動詞 | 行數 | IN §5.1 |
|---|---:|:--:|
| `Confirm` | 137 | — |
| **`Observe`** | **92** | **禁用** |
| **`Verify`** | **90** | **禁用** |
| `Ensure` | 82 | — |
| `Check` | 66 | — |
| `Examine` | 51 | — |
| `Recreate` | 48 | — |
| **`Monitor`** | **39** | **禁用** |
| `Evaluate` | 37 | — |
| `Review` | 36 | — |

**禁用動詞起首者 247 行（22%）。** 取用時須改寫動詞 —— 但**這只是改寫**，
`Observe X` → `Read X and check that …`，若 `X` 本身是可看的，改寫即成立。

**(乙) 內容層：這才是問題所在，且它與動詞無關。**

我把同一套外部面語形判準（上繳包 19 §T33b 之六類）**套到 `Verification Criteria`
本文上**，得：

| | VC 含外部面 | VC 亦無外部面 |
|---|---:|---:|
| **126 個內部列** | 21（**17%**） | **105（83%）** |
| 185 個非內部列 | **172（93%）** | 13（7%） |

**83% vs 7% —— 分離極強。**

即：**`Verification Criteria` 之觀測面與需求本文同源。**
需求說了外部面的，VC 也說（93%）；需求沒說的，VC 多半也沒說（83%）。

`Telematics Client` 之 5 列是最乾淨的例子：其 VC 令檢查
「communication with the TC client **is established successfully**」、
「the **callback is registered** successfully with the topic set to "FOTA"」——
**動詞是 `Check`／`Ensure`（不在禁用表），而檢查對象仍是內部狀態。**
**改動詞救不了它。**

**故對 §五.6 之直答**：
- 動詞須改寫（22% 之行），**但那不是障礙**；
- **真正之障礙是：對 126 個內部列中之 105 列，上游作者也沒有指明看哪裡。**
  R-SU27(a) 之「優先於分析層之自行推想」——
  **在那 105 列上沒有東西可優先，該條落空。**
- 能供給觀測面者僅 **21 列**；那 21 列是 R-SU27(a) 之真正適用範圍。

**這也解釋了 §1.3 之否證為何會發生**：
`Verification Method` 之測試層級與可觀測性測的不是同一件事 ——
因為**上游根本沒有在「可觀測性」這個軸上做過判斷**，
它做的是「這列該在哪一層測」。二者不同軸，故不相關是預期的。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §2 之 83%／93% 這一對數字。**

那組對照看起來像是「VC 之品質已被量化」，而**它用的是同一把尺**：
`RE_EXTERNAL` 是我在上繳包 19 為分類 Description 而寫的，
現在拿它去量 VC，**兩邊共用同一組 regex**。

**於是 93% 這一格幾乎是必然的**：非內部列之定義就是「Description 含外部面語形」，
而 VC 是針對該 Description 所寫的驗證構想，**用詞自然沿襲**。
**它證明的是「VC 與 Description 用詞一致」，不是「VC 之品質高」。**

**真正有鑑別力的是 83% 那一格** —— 因為它是**反向**的：
內部列之 VC **本可以**引入 Description 裡沒有的外部面
（pilot v2 之版本號就是這麼做的），**而 83% 沒有**。
那一格量到的是**上游作者也沒做這件事**，不是同語反覆。

**若只報 93% 而不報 83%，會像是驗證了 VC 之品質；實際上只有 83% 那一格有內容。**

### 7.3 一項我做了而下放包未要求的事

**§5.1 —— 做 036 之欄位全覽時，順手更正了上繳包 15 自己寫下的一處誤讀。**

T34d 只令「036 母本之 TC 分頁之欄同格式全覽」。列出 34 欄、標記用途，即完成。

我另做的是**把標頭原文與先前記過的 DV 範圍對起來看**：
上繳包 15 §4.5 曾寫「`S` 欄落在 DV `T10:Z1411` 之外，其值域與填法未查」——
語氣像是 `S` 少了拘束。全覽一列出來就看見 **`T`–`Z` 是七個車型名**
（HDCC27／DT27／VF637／…），其 `"0,1"` 是**車型適用旗標**，
**與 `functional_safety` 本就無關；`S` 不在其中是正常的。**

**且它同時揭出一個新缺項**：那七個車型欄**是交付面之欄、有 DV 拘束、而填法未裁** ——
先前從未被指認為缺項，因為沒有人列過那份欄表。

**記明此事之理由**：這是 §7(20)（先列全覽再掃）在同一輪內就見效的實例 ——
**全覽不只補上漏讀的欄，它還會更正「已讀之欄」上的誤讀**，
因為誤讀往往來自把一個欄放在錯誤的鄰居旁邊理解。
