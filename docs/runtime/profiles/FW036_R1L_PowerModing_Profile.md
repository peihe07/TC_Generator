# Project Profile — FW036 / R1L SWE1 Power Moding HMI (Power Moding HMI Logic and Flow R1 SR24 2A, Stellantis newR1L)

> **建立 2026-08-24，依 10 下放包。** 交付夾名為 `Disclaimer screen`，
> 而規格文件為 Power Moding HMI —— 二者之關係見 §0。

> **PRECEDENCE：本 profile 於與泛用 ASPICE SWE.6 指令衝突處 OVERRIDE 之。**
> 泛用規則於本 profile 未觸及之處仍全部有效。標 **[OVERRIDE]** 者取代特定泛用規則
> （被取代者逐條引用）；標 **[ADD]** 者為專案特有之增補。

## 0. Project identity [ADD]

- Program：Stellantis newR1L；範圍 037-A03 Power Moding HMI，**48 leaf**
  —— **其中 1 條（`SWE1-HMI-PM-028`）為揭露列，不含可驗證行為，見 §6**（R-PMH47）
  （`Categorization == Functional Requirement` 之全集，R-PMH1；
  另 8 列為 `Heading`，不計）
- **交付夾**：`Disclaimer screen`（FROP 標籤）；**規格文件**：Power Moding HMI
  Logic and Flow R1 SR24 2A。二者不同層級，非衝突（R-PMH2）
- **交付基底**：`forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx`，
  SHA256 `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`
  （R-PMH7）。客戶交付夾之 `…_PowerModingHMI_20260819.xlsx` 為**來源複本**，
  其封面五頁**一律不得取用**（R-PMH23 —— 其 ChangeHistory 已被 AMFM 之
  中繼寫回註記覆寫）
- **workbook_state = BLANK**（R-PMH8）；write_back 自 r10 起 append；
  done invariant 不適用
- 分頁 `Test Case Specification 測試用例規範`，**34 欄（rev C）**，
  `last_capacity_row = 1411`

### 0.1 欄位對應 [ADD]

rev C 版面（與 `FW036_R1L_Power_Profile.md` §0.1 之 35 欄版面**不同**，
自 P 起左移一格）：

| 語義 | 欄 | 語義 | 欄 |
|---|---|---|---|
| req_id | D | priority | **P** |
| tc_id | F | estimated_time | **Q** |
| test_group | G | design_method | **R** |
| test_set | H | functional_safety | **S** |
| test_item … tc_ref_id | I–O | 車型欄（7） | **T–Z** |
| | | author | **AA** |
| | | remarks | **AH** |

四方交叉佐證：母本 ＋ User Profiles 20260820 ＋ Comfort 20260817 ＋
Time Management 20260822，r9 表頭 34/34 逐欄相等（R-PMH9）。

### 0.2 範本自身之限制 [ADD]

- **priority DV 之 sqref 為 `P10:Q1411`，跨 P、Q 兩欄**（A-PMH12(1)）——
  `Q` 欄為 `Estimated Test Time (mins)`，卻套用 `"P0,P1,P2,P3"` 之下拉。
  **任何寫入 `Q` 之數值都會被擋下**；`allowBlank=1` 是它至今未被發現的原因。
- **`AF` 之 test_result 列舉含前導空白**（A-PMH12(2)）：逐字為
  `"Pass, Fail, Pending,Block,NA"` —— `Fail` 與 `Pending` 各前置一個空格。
  **寫入 `Fail`（無空格）會被擋下**；任何對該值做 `.strip()` 之程式
  都會產出無法通過 DV 之值。
- 全簿 DV 為 **5 組**（`Test Case Specification` 分頁 4 組 ＋
  `Product Document 記錄封面頁!B7:C7` 1 組）。**分頁層與活頁簿層之計數
  須分別陳述**（R-PMH20）。
- x14 DV（`R10:R1411`）之 source 為 **`下拉選單!$A$1:$A$9`**。
  **不得以分頁名認定 source**（R-PMH25）—— 母體 16 檔中僅 4 檔指向此處，
  10 檔指向 `Reference!$C$4:$C$12`，而客戶那份之 `下拉選單` 為孤兒分頁。

## 1. Requirements authority chain [ADD]

- **spec_mode = A+B**（Home hybrid 前例）。
- **判讀基準為 PDF；SYS1 匯出為追溯用**（通則 3）。理由：PDF 文字層產出率
  11/11 = 100% 但可錨定編號章節 0（Visio 流程圖冊，無目次），
  故 `{outline}` 只能取自 SYS1 匯出（52 outline，037 引用之 29 章節命中 29/29）。
- **跨表列號一律以 id 實測比對，不以位移推算**（R-PMH12）——
  037 含 8 個 Heading 列而 036 之 48 列不含，位移非定值。
- **上游 037 報告之檔名一致性不在本 feature 範圍內**（R-PMH26）：
  不開 DR、不作為 anomaly、不得以「命名將趨於一致」為前提設計任何判準。

### 1.1 已登記之規格層偏離 [ADD]

- **A-PMH03**（PENDING）：SYS1 匯出相對 PDF 之內文偏離 —— 43 則可比對描述中
  39 則逐字命中，4 則缺口為重排（7.1）、拼字（`Starup`）、`-layout` 條列再流。
  **outline 7.1 為 Phase 4 之指名複核項** —— 該章 5 個 leaf（單章最大宗），
  且被移位改寫者正是動畫／splash 之時序子句（3 sec／1.5 each）。
  時序誤讀在 Power Management 出過一次（`006`，A-PW68），
  歷經兩輪修正與多次 lint 全綠而未被察覺。
- **A-PMH04**（PENDING）：SYS1 匯出有 6 則 outline 為圖片佔位，
  內容只在 PDF p3–p7 流程圖。render 能力實測：**150 DPI 足供流程圖判讀，
  300 DPI 方能辨讀內嵌 UI 截圖內文**。48 leaf 無一落在 p3–p7。

## 2. Test Set vocabulary [OVERRIDE §4.1.3／§4.2]

Layer 1 Test Group = **`Disclaimer screen`**（R-PMH13 —— 取**交付夾名**，
非規格模組名；依據為四份已交付件之 G 欄實測 4/4 皆為交付夾名，
含 Comfort 466/466 = `Climate Control Interface`）。

Layer 2 **已定版，八個值**（R-PMH36），分布不得變更：

| Test Set | leaf | Layer 3（規格章節） |
|---|---|---|
| `Splash Screen` | 3 | 7.1（部分）、7.9 |
| `Disclaimer Screen` | 7 | 7.1（部分）、7.2、7.3、7.4、10.4（部分） |
| `Startup Animation` | 9 | 7.5、7.5.1、7.6、7.7、7.8 |
| `Startup Sounds` | 6 | 8.1、8.2、8.2.1–8.2.3、8.3 |
| `Power Transitions` | 7 | 7.1.1、9.1、10.5 |
| `Power Off Behavior` | 8 | 10.1、10.2、10.3、10.4（部分）、10.6、10.7 |
| `Voice Assistant Key` | 5 | 11.1 |
| `Off Road Plus` | 3 | 12.1、12.2、12.3 |
| **合計** | **48** | 餘數 0 |

**其中 1 條（`SWE1-HMI-PM-028`）為揭露列，不含可驗證行為，見 §6**（R-PMH47）。**48 之總數不變** —— 該 leaf 仍在 R-PMH1 之範圍內。

逐 leaf 之歸屬以 `features/power_moding/data/layer3_sections.tsv` 為權威。
Layer 3 不入工作簿（§4.1.5）。

**§4.2 之明示例外**：Test Set `Disclaimer Screen` 與 Test Group
`Disclaimer screen` 字面重複。**其範圍嚴格限定為：本 feature、本組、
此一情形**（Test Group 取交付夾標籤而非能力名，致交付夾名恰等於其中
一個能力群之名稱）。**不得外推至他 feature，亦不得作為 §4.2 之一般性放寬**
（R-PMH36）。

granularity 判準（G1–G5 ＋ 六個 must-hit 錨點）見
`features/power_moding/framework.md`；**該判準對本例外之三個候選案
全部 PASS，即無鑑別力，不得引為支持本組名之理由**。本組名之依據為
**可過濾性**（客戶得以 H 欄過濾出 disclaimer 之 7 條）與**不造詞**
（規格自 7.1 SU1 至 10.4 PITA6.1 一律用 `disclaimer`）。

## 3. FW036 Power Moding house style（欄位規則）

### 3.1 Test Item [OVERRIDE — 取代 §4.3 之單段內容]

`test_item` 之下半括號（測試目的／區別 sibling 之標籤，獨立一行之 `(...)`）
為**硬規則**，於每一條產出與覆核時檢查，不因當輪提示未提及而豁免。

### 3.2 Pre-Conditions [ADD]

僅述狀態／環境（§4.4），不得含動作。本 feature 之常見合法型態：
車輛點火狀態（IGN OFF／ACC／RUN）、車型變體（Maserati／R1Low／
lower comfort screen 配備）、Power Button 狀態、設定值
（start-up sound = Always／Once a Day／Never）。

**變體條件須逐字取自規格**（§8.7.3）—— 本 feature 之變體詞為
`Maserati`、`GDPR`、`R1Low`，不得改寫為 `high-end`／`EU` 之類。

### 3.3 Design Method [OVERRIDE — 限制 §12 之輸出字串]

值須為 **`下拉選單!$A$1:$A$9` 之九詞條之一**（R-PMH25 —— source 取自
母本 x14 DV 之 `<xm:f>` 實測值，不取自同名分頁）：

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

**A-PMH10 之已登記分歧**：`Reference!$C$4:$C$12` 之第 6 項為
`Pair-wise / N-wise`（與上表之 `Pairwise / t-wise` 不同）。
本 feature 依 R-PMH25 取母本之值。母體 16 檔之 R 欄 996 個值
**無一使用 `Pair-wise / N-wise`**，故實務上零逸出。

### 3.4 Spec Reference [ADD — §10.7 之檔名形態]

格式 `{spec_filename}_{section_id}`，檔名部分取 037 `HMI Source ID` 欄之
逐字前綴：

```
Power Moding HMI Logic and Flow R1 SR24 2A
```

section_id 取 SYS1 匯出之 `Outline Number`（如 `7.1`、`8.2.1`、`10.4`）。
**不得引 037／SWE.1 分析報告本身為 spec 來源**（§10.7）。

### 3.5 Priority [ADD]

依 §10.2 rubric 自 **TC 實際所寫之測項內容**判定 P0–P3。
037 之 `Priority` 欄（`High`／`Medium`／`Low` 形態）**不具映射權威**
（同 Power `R-P8` 之形態）。

母本之 DV 列舉為 `"P0,P1,P2,P3"`，與 canon §10.2 完全相同；
母體 16 檔之 P 欄實際值逸出 **0**。

### 3.6 Estimated Test Time（Q 欄）[ADD]

**留白。** 除語料慣例外，本欄另有硬性理由：其 DV 為 priority 之
`"P0,P1,P2,P3"`（§0.2），**任何分鐘數都會被 Excel 擋下**。

### 3.7 Functional Safety（S 欄）[ADD]

一律 `NA`（沿用 Power／Privacy 之慣例）。

### 3.8 Vehicle Model 欄（T–Z）[ADD]

**一律留白。** 母體 16 檔中僅 Comfort 於該七欄逐列填 `1`（466×7 = 3262），
而其自身 profile §3.9 明訂「T–Z 一律留白」、其 baseline 該欄非空數為 0
—— **該等值非由該 feature 之管線產生，不構成先例**（Power `R-P54` 之同一論證）。

### 3.9 前言三欄（D3／D4／D5）[ADD]

**一律留空**（R-PMH27）。

依據為 R-PMH24 母體 16 檔之實測：`D3` 16/16 空、`D4` 16/16 空、
`D5` 9 空 / 7 非空。**本裁定不是多數決** —— 七個非空者中有兩者填錯
（`HomeHMI` 之值逐字等同 `AppDrawer` 之報告名；`Notifications HMI` 之值為
`FM-WI-FSM-036-A01`，即表單編號本身），且填法採五種不同格式。

日後若客戶要求填寫，其字串由 Pei 給定並另立新條取代，
**不得以「補上」之名逕行填寫**。

### 3.10 `Product Document 記錄封面頁` [ADD — 待裁]

**Q10 未裁前不寫入**。母本該分頁為「僅標籤、值全空」；
母體 16 檔中 12 檔**整張填**（B3 專案／B5 版本／B6 部門／B7 分類／修訂列皆有值）、
4 檔**一格未填** —— **全有全無，範圍是一張分頁而非一格**。

若裁為須填，須增補 11 項，其中 5 項須 Pei 給定字串
（`B3` `new R1L`(8) vs `NR1L`(4)、`B4` 文件名、`B5` `V1.0`(11) vs `Initial`(1)、
`B8` 日期格式不一、`A13:D13` 修訂列），
1 項與 R-PMH26(d) 相衝（`B4` 取檔名即依賴上游命名），
1 項與 R-PMH23 相衝（值不得自客戶那份複製），
1 項需擴充 `check_write_back.py`（`B7` 之 DV 約束不在現行三項內）。

## 4. Split policy [ADD]

泛用 §8.2.2 / §8.3 適用。本 feature 特有之判準：

- **變體即拆分**：`Maserati` 與非 `Maserati`、配備／未配備 lower comfort
  screen、`R1Low` 與非 `R1Low` 為不同輸入，各自成條（7.2／7.3／8.x）。
- **設定值列舉即拆分**：`Always`／`Once a Day`／`Never` 三值各自成條，
  且依 §7 須配一條負向（`Never` 情形下不播放）。
- **同一觸發之多個必然後果不拆**（§5.7）：例如 10.6 之「Phone call popup
  顯示於 Power Button Off 之上」與「忽略後回到 Power Button Off」為
  同一觸發之連續後果，寫成同一條之多行 ER。
- **不同觸發即拆分**：7.1 之「駕駛門關閉」與 7.1.1 之「按電源鍵」
  為兩個觸發。

## 5. Marker vocabulary [ADD]

本 feature 有**三個字面常數**，其大小寫與空白**刻意不同，不得統一**
（R-PMH18、R-PMH36）：

| 用途 | 值 |
|---|---|
| Test Group（G 欄） | `Disclaimer screen` —— screen 小寫 s |
| Test Set（H 欄之第 2 組） | `Disclaimer Screen` —— Screen 大寫 S |
| `tc_id` 之 `{abbr}` | `DisclaimerScreen` —— 去空白 PascalCase |

**任何將三者正規化為同一形態之處理即為缺陷**；lint 之比對須大小寫敏感。

`tc_id_format` = `NR1L-DisclaimerScreen-{NNN}`（R-PMH16）。
**已知反例須隨之保留**：Comfort 之 `{abbr}` 為 `ComfortHMI` 而其交付夾名為
`Climate Control Interface`，**不符本判準**，且它是唯一具鑑別力之語料
（R-PMH14）。故本規則為**本 feature 之裁定，不主張為全案慣例**。

方括號一律禁止（§11），本 feature **無 profile-scoped 之方括號例外**。

## 6. 已知限制 [ADD]

- **`SWE1-HMI-PM-028` 為一句轉介**（A-PMH13）：12.2 之內文逐字為
  `OFF2.) Please refer to CFTS009 for complete behavior.`，本身無可驗證行為；
  其 037 `Requirement Title` 逐字為 `CFTS009 Behavior Reference`
  —— **上游自己就把它命名為「參照」**。
  跨 feature 擴查（母體 15 個有內容交付件、3,023 資料列、11 個欄位、
  166 個相異 Test Set 全數人工核對）**零命中** —— 兩邊都沒有，
  **是全案缺口，不是分工**。處置待 Pei。
- **`Q` 欄與 `AF` 欄之 DV 瑕疵**（A-PMH12）為 **Phase 6／7 之前置阻斷項**
  —— 母體 16 檔之該二欄皆全空，故其 DV **從未被實際檢驗過**，
  首次填值時才會浮現。
- **granularity 檢查驗的是 leaf 分布，不是 TC 分布** —— TC 生成後某組
  TC 數暴增（例如 `Startup Animation` 之 9 leaf 展開為 30+ 條）須重驗。
  **Phase 4 之複驗項。**
- **`check_write_back.py` 三項檢查已實作並經故意失敗驗證，但尚未接上任何
  寫回路徑** —— 接線為 Phase 6 之交付項。**已知未完成，非 RESOLVED。**

## 7. 不繼承自 `FW036_R1L_Power_Profile.md` 者 [ADD]

- **欄位對應不適用** —— Power 為 35 欄版面（priority Q／design_method S／
  author AB／remarks AI），本 feature 為 rev C 34 欄（§0.1）。
- **規格族不同** —— Power 為 CFTS009／CFTS010（`spec_mode = D`，
  二進位文件抽取），本 feature 為 SYS1 HMI Logic and Flow ＋ PDF
  （`spec_mode = A+B`）。其 §1 之 magic bytes／雙序列化規則全部不適用。
- **`tc_id` 兩階段指派（Power §4.5）不繼承** —— 本 feature 之
  `tc_id_format` 由 R-PMH16 定，批次策略待 Phase 4 另定。
- **Power §3.2 之 `[Nh]` 方括號例外不繼承** —— 本 feature 之規格
  無十六進位訊號值記法（§5）。
