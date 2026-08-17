# Project Profile — FW036 / R1L SWE1 Power Management (CFTS009 + CFTS010, Stellantis newR1L)

> **建立 2026-08-17，依 R-P82（11 下放包）。** Power 原為八個 feature 中唯一
> 無 runtime profile 者（A-PW49）；§11 之 profile-scoped 例外因此懸空 ——
> 首批 TC 之 `[1h]` / `[0h]` 訊號值方括號係靠 lint 之硬編碼豁免，非靠條款。
> 本檔補上該依據。

> **PRECEDENCE：本 profile 於與泛用 ASPICE SWE.6 指令衝突處 OVERRIDE 之。**
> 泛用規則於本 profile 未觸及之處仍全部有效。標 **[OVERRIDE]** 者取代特定泛用規則
> （被取代者逐條引用）；標 **[ADD]** 者為專案特有之增補。
>
> 結構條款參照 `FW036_R1L_Privacy_Profile.md`（最近之同類 —— 同為 BLANK 工作簿）。
> **結構條款可繼承，內容條款不可。** Power 與 Privacy 無共同規格文件、無共同 037 家族，
> 故每一項內容條款皆自 Power 自身之裁決重新導出。

## 0. Project identity [ADD]

- Program：Stellantis newR1L；範圍 037-A03 Power Management，**115 leaf**
  `SWE-PM-001`…`115`（連續無斷點，G1）
- 交付工作簿：`FM-WI-FSM-036-A01 …_SWQT_PowerManagement_20260816.xlsx`，
  SHA256 `ce93174794d0d43c…`（G0 前置閘之權威，見 `docs/upstream/02_rebaseline.md` §二）
- **工作簿為 BLANK**（G10：c2–c35 × r10–r221 非空儲存格 = 0）—— 無 legacy region、
  無 done region
- **範本版本與 Comfort / Privacy 不同**（A-PW47）：分頁名 `Test Case Specification&Result`
  （另二者為 `Test Case Specification 測試用例規範`）、**35 欄**（另二者 34 欄）

### 0.1 欄位對應 [ADD]

自 P 起較 Comfort / Privacy 整體右移一格（A-PW40，已由 R-P73 之三方交叉佐證）：

| 語義 | 欄 | 語義 | 欄 |
|---|---|---|---|
| req_id | D | priority | **Q** |
| tc_id | **F** | design_method | **S** |
| test_group | G | functional_safety | **T** |
| test_set | H | 車型欄（7） | **U–AA** |
| test_item … tc_ref_id | I–O | author | **AB** |
| estimated_time（第一個） | P | remarks | **AI** |
| estimated_time（第二個） | R | | |

**本範本有兩個標頭逐字相同之 `Estimated Test Time` 欄**（P 與 R，A-PW41）——
二者皆留空（G53：Comfort 466 列、Privacy 11 列之該欄非空數皆為 0）。

### 0.2 範本自身之限制 [ADD]

- **B 欄無自動編號公式。** Comfort / Privacy 之範本於 B10 起帶
  `IF(ISBLANK($D10),"",ROW()-9)`；**Power 之 B 欄為純空儲存格**（11 包 B1 實測）。
  寫回時 No.# 欄不會自動填入。
- **DV 覆蓋範圍不齊**：`Q10:Q221`（priority）與 `U10:AA221`（車型欄）涵蓋全資料範圍，
  但 `P10:P11` / `R10:R11`（estimated_time）僅兩列、`AG10:AG13`（Test Result）僅四列。

## 1. Requirements authority chain [ADD]

- **spec_mode = D**（二進位文件抽取，R-P9 / R-P3′）。原 scaffold 之 `A` 為誤。
- 規格來源為**兩份** CFTS（R-P4）：CFTS009 Wake-up and Power-up、CFTS010 Power Down。
  任何宣稱「規格來源」之陳述須同時涵蓋兩份。
- 讀取方式依實測 magic bytes（R-P3′）：
  `50 4B 03 04`（OOXML `.docx`）→ `zipfile` 讀 `word/document.xml`；
  `D0 CF 11 E0`（OLE2 `.doc`）→ macOS 內建 `textutil -convert html`
- **文字層定義**（R-P17）：每段同時產出 `plain` 與 `bold` 兩種序列化；
  §C rule 1（章節錨點）套 `plain`，rule 2（需求錨點）套 `bold`，依段落索引對齊。
  理由：CFTS009 標題以段落樣式 `pStyle 1–8` 表達，CFTS010 標題為 run 層粗體，
  單一序列化不可能同時滿足兩條正則。

### 1.1 錨點層範圍上界 [ADD — R-P42]

某 leaf 之 TC 範圍上界為其 `Source Requirement ID` **所實際引用之需求錨點**。
未被引用之錨點一律不測，即使與被引用者位於同一章節、僅一行之隔。
黑名單由 `scripts/build_blacklist.py` 自動導出（**不得人工維護**，R-P52(c)），
現為 **814 個**，分三層風險（tier 1 = 182 / tier 2 = 133 / tier 3 = 499）。

## 2. Test Set vocabulary [OVERRIDE — 取代泛用之自由形式標籤]

Layer 1 Test Group = `Power Management`（R-P2）。
Layer 2 **已定版，五個值**（R-P35），分布不得變更：

| Test Set | leaf |
|---|---|
| `Power State` | 63 |
| `Startup Display` | 24 |
| `Branding and Theme` | 16 |
| `Timeout Settings` | 8 |
| `Power Down` | 3 |
| **合計** | **114**（＋`SWE-PM-089` 留空 = 115） |

逐 leaf 之歸屬以 `features/power/data/leaf_testset.tsv` 為權威。
Layer 3 記**全集**（R-P24，一 leaf 得對應多章節），見 `data/layer3_full.tsv`
（140 列、46 個相異章節）；Layer 3 不入工作簿（§4.1.5）。

## 3. FW036 Power house style（欄位規則）

### 3.1 Pre-Conditions [ADD]

僅述**狀態／環境**，不得含動作（§4.4）。動作動詞之判準以經驗基礎導出
（R-P83）：自 Comfort + Privacy 之已交付 `test_procedure` 取行首動詞聯集，
再以其已交付 `pre_conditions` 1823 行量偽陽性 —— **為 0**。

`[spec-derived]` 等 **source-class 標記得置於行首方括號內** ——
此為 §3.2 之既有慣例（Comfort 之已交付 TC 即如此書寫）。

### 3.2 Signal citations [ADD — §11 之 profile-scoped 例外]

**§11 禁止方括號於 TC 輸出欄位，本 profile 對下列情形 OVERRIDE：**

規格逐字所用之**訊號值記法** `[Nh]`（十六進位，如 `[1h]` / `[0h]`）
得於 `pre_conditions` / `input_test_data` / `test_procedure` / `expected_result`
中保留原記法。

依據：CFTS010 §1.7.2 之 `4942354` 逐字為
`STATUS_LIN.PN14_LS_Actv=[1h]`、`STATUS_LIN.Batt_ST_Crit=[1h]` ——
改寫為引號會失去與規格之逐字對應，而 §11 之立意為禁止**佔位語法**與
**UI 標籤誤用方括號**，非禁止逐字引用之來源記法（§11「Exception (profile-scoped)」）。

**UI 標籤仍一律用雙引號**，不得用方括號、單引號、角括號。

### 3.3 Design Method [OVERRIDE — 限制 §12 之輸出字串]

值須為 `下拉選單!A1:A9` 之**九詞條之一**（A-PV10 / R23-6；02 包實測 A10 / A11 為空）：

```
功能測試 (Functional based ; no specific technique)
狀態轉換 (State Transition Testing)
決策表 (Decision Table Testing)
等價劃分 (Equivalence Partitioning, EP)
邊界值分析 (Boundary Value Analysis, BVA)
組合測試 (Combinatorial Testing ; Pairwise / t-wise)
情境 / 用例 (Scenario / Use Case Testing)
負向測試 (Negative / Invalid)
基礎故障注入 (Fault Injection Lite)
```

**§12 之 first-match 走查須以 TLM 之具名 status 為準** ——
即 CFTS009 §1.6.2.1.1–.13 所列者（Full-Operation / Idle / Partial Operation /
Stolen Vehicle Mode / Timed / Standby / Sleep / Bench / Logistic Idle / Logistic
Standby / Logistic Sleep / Init ×2）。
不在該清單者（如 Load Shed、Battery Critical）**不構成 State Transition**，
應續往「multiple conditions → outcome」判為決策表。
依據：11 包 B5 於 CFTS010 全文實測 —— `Load Shed` 出現 29 次，
與 status / state / mode 之共現 **0 處**，僅作為章節標題（§1.4.1.6、§1.7.2）。

### 3.4 Spec Reference [ADD — §10.7 之檔名形態]

格式 `{spec_filename}_{section_id}`。**檔名部分得含空白**（§10.7 之範例即然）。
本 feature 之兩份規格檔名（去副檔名）：

```
R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658
R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658
```

（CFTS010 之檔名於 `Power Down` 後有一個空格，逐字保留。）

### 3.5 Priority [ADD]

依 §10.2 rubric 自 **TC 實際所寫之測項內容**判定 P0–P3。
037 `Priority` 欄之 `High` / `Medium` **不具映射權威**（R-P8），
不得以之推導；lint 之 G39 檢查二者是否呈一對一映射。

### 3.6 Estimated Test Time（P 欄與 R 欄）[ADD]

**兩欄皆留白。** 依據：G53 實測 Comfort 466 列、Privacy 11 列之對應欄非空數皆為 0。

### 3.7 Functional Safety（T 欄）[ADD]

一律 `NA`（沿用 Privacy R30-3）。

### 3.8 Vehicle Model 欄（U–AA）[ADD]

**一律留白**（R-P54；沿用 Privacy R30-4；A-PV15 之世代落差同樣適用 ——
範本七欄止於 27 世代）。

A-PW29 所登記之 EE Architecture 分布（被引用 238 個 item 中
`Atlantis Mid` 單值 13、`Atlantis High` 單值 1）為**填欄判準之能力**，
**非填欄授權**。改填須走另案裁定。

> **11 包 B2 之查證**：Comfort 之已交付件於該七欄逐列填 `1`（466/466），
> 但其 profile §3.9 明訂「T–Z 一律留白」、`write_back.py` 亦將 T–Z 列入
> `NEVER_WRITE`、其 baseline 工作簿該欄非空數為 0。
> **該等值非由 Comfort 管線產生。** 故不構成先例，Power 維持留白。

## 4. Split policy [ADD]

泛用 §8.2.2 / §8.3 適用。Power 特有之判準：

- **不同觸發即拆分**（§5.7）。例：CFTS010 §1.7.1.1.1 之「不得於轉往
  Standby status 或 Bench status 時顯示 splash」為**兩個不同觸發**，拆為兩條。
- **不同控制實體即拆分**。例：`4942354` 之 Load Shed（`PN14_LS_*`）與
  Battery Critical（`Batt_ST_Crit`）為不同訊號組，拆為獨立 TC。
- 各條件之**故障分支**與**回復分支**為獨立部分失效，各自再拆。

## 4.1 產出 JSON 之必附欄位 [ADD — R-P104]

每批之產出 JSON，其 `leaves` 陣列**每筆必附 `source_clause`** ——
該 leaf 所引用錨點之**規格原文子句**。

- 不得節錄至失去語意；若過長，須以 `...` 標明截斷處並另附全文檔。
- **理由**：無此欄位，覆核者僅能檢視 TC 自我證明之一致性，
  無法判斷其是否忠於規格。14 包即因該欄位而查出 `006` 之時序誤讀（R-P103）。
- **機械檢查：G79**（`check_source_clause`）—— 逐 leaf 檢查該欄存在且非空。
  **「是否忠於規格」本身不可機械檢查** ——
  該判斷須人讀規格原文與 TC 對照，即 R-P98 / R-P105 之覆核。
  G79 只保證**覆核所需之材料存在**，不保證覆核已做。

## 4.2 Final Step [ADD — R-P101]

`test_procedure` 之**末步須含驗證意圖措詞**（§5.2B：`check that ...` /
`to verify ...` / `and check ...`），得延伸至 **≤ 18 字**以承載該子句。
依 R-P96 合併步驟時**不得剝除**該子句。

- **機械檢查：G77**（`check_s52b_final_step_intent`）。
- **已登記之分歧（A-PW67）**：該措詞於 Comfort + Privacy 已交付之
  472 條末步中命中 **0** 次；其慣例為「Read <具體可觀察標的>」。
  Power 依 R-P101 採 §5.2B 措詞，末步慣例將與該二 feature 分歧。

## 4.3 `reasoning_note` [ADD — R-P110]

TC 層之欄位，**追認自 14 包**（R-P102 令「於各該 TC 之 `reasoning` 逐字記載」，
而 TC 層原無 `reasoning` 欄，執行層自行新增此欄）。

- **用途**：TC 層之**個案判斷記錄**，補 leaf 層 `reasoning` 之不足。
- **不寫入工作簿**，僅供覆核。
- **與 `split_reason` 之分工**：

  | 欄位 | 內容 | 是否寫入工作簿 |
  |---|---|---|
  | `split_reason` | **拆分理由**（本條與其 sibling 之區別軸） | **是** |
  | `reasoning_note` | **判斷依據**（為何如此斷言、規格未載之處如何處置） | **否** |

- 現有用例：`001` / `004` 之時序下界斷言依據（R-P102）、
  `006` 之順序斷言刪除依據（R-P108）。

## 4.4 `source_clause` 之截斷界線 [ADD — R-P109]

`source_clause` 得截斷，但**該 TC 之 `expected_result` 所斷言之每一項行為，
其規格依據必須完整出現於 `source_clause` 中**。
若因此過長，須另附全文檔並於 `source_clause` 標明檔名與位移。

- **機械檢查：G82**（`check_er_clause_coverage`）——
  ER 之**專有標的**（訊號名、`_Time` 類參數、全大寫識別子、數值）
  須出現於該 leaf 之 `source_clause`。
- **不可機械檢查者**：ER 之**一般英文措詞**與規格之對應 ——
  措詞本就不會逐字相同，強行比對只會產生雜訊。
  G82 只攔得住「截斷蓋掉具名標的」這一類，
  攔不住「截斷蓋掉某項以一般措詞表述之行為」。

## 4.5 tc_id 之兩階段指派 [ADD — R-P113]

| 階段 | 值 | 效力 |
|---|---|---|
| **產出**（依 Test Set 分批）| `NR1L-PowerManagement-{NNN}`，**批次內臨時編號** | **無最終效力**；批次檔頭須載 `"tc_id_status": "provisional"` |
| **寫回**（全部 114 leaf 完成後，單次）| 依 `(SWE-PM ID, split_index)` 序自 001 起連號 | 最終值；**工作簿列序即此序** |

- 產出仍依 Test Set 分批 —— §4.1.3 之價值於撰寫階段成立，不放棄（R-P113(a)）。
- **`split_index`**（R-P115，分析層自裁）：同一 `req_id` 之多條 TC，
  依其**規格原文子句出現序**排列，自 1 起。**不寫入工作簿**，僅供排序與稽核。
- **JSON 陣列序仍維持臨時 tc_id 之遞增序**（§10.3 / G38）；
  寫回列序另由排序鍵決定。**二者刻意分離** —— 若逕以排序鍵重排 JSON 陣列，
  G38 會判 tc_id 未單調遞增（16 包實測 3 項 FAIL）。
- 指派腳本：`features/power/scripts/assign_final_tc_id.py`（**只產對照表，
  不改寫批次 JSON**；G85 為其回歸斷言）。

## 5. Marker vocabulary [ADD]

- `[spec-derived]` 等 source-class 標記 —— 見 §3.1
- `[Nh]` 訊號值 —— 見 §3.2
- 其餘方括號一律禁止（G50 檢查）

## 6. 已知限制 [ADD]

- **Layer 3 之邊界由 SYS2 收錄規則決定，非獨立界定**（R-P50）。
  若有人問「為什麼某章沒有 TC」，正確答案是 R-P7，不是 Layer 3。
- **31 處懸空 `WrapperResource` 參照**（A-PW26）：CFTS009 16 處、CFTS010 15 處，
  分布 16 章；型別為 `.xls` 15 / `.rtf` 14 / `.xlsx` 1 / `.doc` 1。
  二份 CFTS 皆**零嵌入物件** —— 參照存在而資源不存在。
  影響面：僅 2 處落在被引用錨點下（CFTS009 §1.6.2.1），觸及 9 個 leaf，
  全屬 Power State（DR-PW6）。
- **`SWE-PM-089` 留空**（R-P1，DR-PW1）：其 `Source Requirement ID`
  為 `SWE1-PM-ANT-008`，非 SYS2 命名空間。

## 7. 不繼承自 Privacy 者 [ADD]

- Privacy 之 §3.5 Spec Reference 形態係其 CFTS022 之檔名慣例，本 feature 另定（§3.4）
- Privacy 之欄位對應（priority P / design_method R / functional_safety S /
  author AA / remarks AH）**不適用** —— 本範本自 P 起右移一格（§0.1）
- Privacy 無雙 CFTS 之情形，故其 spec 章節引用規則不含跨文件之考量
