# 上繳包 01 —— Power Moding HMI 開案（Phase 0 intake）

- 日期：2026-08-22
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/power_moding/docs/handoff/01_intake.md`
  （SHA256 `0f11160c8efcac11423a43c2cc86fe387ce99155b4366c6a4600fbfe0b914838`）
- 執行狀態：**步驟 1–8 全部執行完畢**；步驟 6 依停止條件 2 停於「不自行歸類」，
  步驟 4 之差異已查明並登記 A-PMH01。**無任何寫回、無任何 git 狀態變更。**

---

## 1. 素材台帳（步驟 3，R-PMH4 / G0 / §9.1 通則 9）

來源目錄（唯讀）：
`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Disclaimer screen/`
目的目錄：`features/power_moding/inputs/`

**來源目錄之檔案清單與下放包 §四步驟 3 所列逐一相符，無多餘檔案**
（停止條件 8 未觸發）。

| # | 檔名 | 大小 | mtime | SHA256 |
|---|---|---|---|---|
| 1 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerModingHMI_20260819.xlsx` | 89,585 | 2026-08-19T18:00:22 | `2be63febf005dd87ad302b78989ee7800a1a90c60f1f6673f9b455e664625a54` |
| 2 | `FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1 STLA 報告.xlsx` | 82,726 | 2026-08-19T17:15:56 | `e896a32ac9efef8a3eb8e77e6aa98f1eb1eec8229f70ab4172a2ff6202e8cf9a` |
| 3 | `Power Moding HMI Logic and Flow R1 SR24 2A DCR22412 (January 24 2023).pdf` | 529,984 | 2026-06-19T07:49:00 | `ff43664eec22691a9e6e35702e0692ce2b8c09d53cb878a541d5f8c436b2e786` |
| 4 | `SYS1_HMI_Power_Moding_HMI_Logic_and_Flow_R1_SR24_2A.xlsx` | 38,722 | 2026-08-17T03:02:00 | `9c5cc28974f3fcbbfd3cc913532a1d3c64015981d3f2c07425cd9e61fa951f34` |

- **搬入前後之 SHA256 與 mtime 四份全部相同**（`cp -p` 保留 mtime）。
- **搬入後對來源目錄再測一次**，四份雜湊未變 —— 來源唯讀之宣稱經實證。
- 雜湊檔 `inputs/MANIFEST.sha256` 已產生，`shasum -c` **四份全 OK**。
  （`inputs/` 於 `.gitignore` 內，雜湊檔本身亦在其中 —— 見 §7 之
  `A-PMH05` 待議項。）

---

## 2. §二六條之抄錄核對表（步驟 2）

抄錄方式：以 `re.findall` 自 handoff §二之 fenced block **直接取字串寫入**，
未經人工重打；核對時對 handoff 原文與 `RULINGS.md` 落地文**各自獨立再抽取**
後計 SHA256。

| 條號 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|
| R-PMH1 | 441 | `468fc43132ac1b9f` | `468fc43132ac1b9f` | 逐字相符 |
| R-PMH2 | 287 | `19f57d23b1cf9800` | `19f57d23b1cf9800` | 逐字相符 |
| R-PMH3 | 464 | `84acd49a1fc7f6ae` | `84acd49a1fc7f6ae` | 逐字相符 |
| R-PMH4 | 277 | `04d87eb139a11e2b` | `04d87eb139a11e2b` | 逐字相符 |
| R-PMH5 | 555 | `e589281f93426f27` | `e589281f93426f27` | 逐字相符 |
| R-PMH6 | 278 | `5bb6ebe395b25187` | `5bb6ebe395b25187` | 逐字相符 |

R-PMH6 條後另附**執行層勘誤附註**（原條文不改字，R19-2），內容見 §3.2。

---

## 3. 037 全表解析（步驟 4）

**量測條件（R-G8 / §9.1 通則 5）**：對 `features/power_moding/inputs/` 之
**有雜湊複本**（`e896a32a…02e8cf9a`，`shasum -c` OK）以 `openpyxl`
（`data_only=True`）讀取；分頁 `Analysis Report`，表頭 r7，資料自 r8。
**先算後比** —— 下列數字產出時未讀取 handoff §3.1 之值。

### 3.1 四項數字

| 項 | 分析層 §3.1 | 執行層實測 | 結果 |
|---|---|---|---|
| `Categorization == Functional Requirement` | 48 | **48** | 相符 |
| `Categorization == Heading` | 8 | **8** | 相符 |
| `FROP` 相異值 | 13 | **12** | **不符 → A-PMH01** |
| `HMI Source ID` 之文件 stem 相異數 | 1（全 48 列同一份） | **1**（`Power Moding HMI Logic and Flow R1 SR24 2A`） | 相符 |

**R-G10 餘數驗證**：非空資料列 r8–r63 共 **56** 列（連續，無空洞）。
`56 − 48（FR） − 8（Heading） = 0`。`Categorization` 之相異值恰為
`{Functional Requirement, Heading}` 二者，**餘數為空，通過**。

### 3.2 `FROP` 相異值之差異歸因（A-PMH01）

| 量測口徑 | 結果 |
|---|---|
| 全 56 列取 `set()`，**未排除空值** | **13**（其一為 `None`，來自 8 個 Heading 列） |
| 全 56 列取 `set()`，排除空值 | 12 |
| 48 個 FR 列取 `set()`（未 strip） | 12 |
| 48 個 FR 列取 `set()`（strip 後） | 12 |

即 `13 = 12 個實質標籤 + 空值一類`。**分析層自身所列之分布明細即為 12 項**
（Customizable Splash Screen / Animations 12、Disclaimer screen 7、
Audio Management 7、Power Management 5、Steering Wheel Controls 5、
Bluetooth 3、FOTA Via Wi-fi 2、Rear View Camera 2、Climate Control 2、
WiFi 1、EV/PHEV Pages 1、e-call (private) 1；合計 48，餘數 0），
**執行層逐項逐數複算全部相符**。故此為 §3.1 表格之量測口徑瑕疵，
其分布明細無誤。

R-PMH6 引用之「13 個相異值」須讀為 **12**；已以勘誤附註形式附於
`RULINGS.md` 之 R-PMH6 條後，原條文未改字。**待 Pei 核可。**

**採認之口徑定義**（供往後引用）：`FROP` 相異值 =
「`Categorization == Functional Requirement` 之列，`FROP` 欄非空值之相異數」。

### 3.3 §3.1 之工作簿列號表 —— 經 036 實測複驗，全數正確

執行層曾以「037 列號 +1」推算 `SWE1-HMI-PM-022-02` 之工作簿列為 r49，
與 handoff 所記之 r44 不符。**該推算錯誤在執行層**：037 之 56 列含 8 個
Heading 列，036 之 48 列不含之，故位移非定值。改以 036 之 D 欄實測，
`SWE1-HMI-PM-022-02` 確在 **wb r44**。handoff §3.1 之七列列號
（12/13/14/16/17/18/44）**全部正確**，此項無差異。

### 3.4 037 ↔ 036 之 1:1 對應（額外驗證）

037 之 48 個 FR 之 `SWE-Requirement ID`，與 036 r10–r57 之 D 欄 48 值
**依序逐一相符（`==` 為 True）**，且 037 側無重複 id。R-PMH5 所稱之
「1:1」經實證。

---

## 4. 036 實測（步驟 5、6）

**量測條件**：對複本 `2be63feb…664625a54`（`shasum -c` OK），`openpyxl`
`data_only=True`，分頁 `Test Case Specification 測試用例規範`。

### 4.1 版面 —— **A–AI 共 35 欄**，非 rev C 之 34 欄

r9 表頭 34 格非空。唯一之重複表頭為 `Estimated Test Time (mins)`，
出現於 **P 與 R** 兩欄。故自 `priority` 起，每欄較 rev C
（`user_profiles` / `time_management`）**再右移一格**：

| 鍵 | 本 feature | rev C | 差 |
|---|---|---|---|
| priority | **Q** | P | +1 |
| design_method | **S** | R | +1 |
| functional_safety | **T** | S | +1 |
| author | **AB** | AA | +1 |
| remarks | **AI** | AH | +1 |

⚠ **AH 於本版面實為 `Defect ID`** —— 沿用 rev C 之 `remarks: AH` 會把備註
寫進 Defect ID 欄。

### 4.2 欄位對應：**16/16**

比對方法：取 r9 表頭之**換行前英文段**、`\s+`→單空白、`.strip()`、`.lower()`
後與目標字串**逐字相等**；每鍵**命中唯一欄，零歧義**。

| 鍵 | 欄 | r9 表頭（英文段） |
|---|---|---|
| req_id | D | Requirement or Design ID |
| tc_id | F | Test Case ID |
| test_group | G | Test Group |
| test_set | H | Test Set |
| test_item | I | Test Item |
| pre_conditions | J | Pre-Conditions |
| input_test_data | K | Input Test Data |
| test_procedure | L | Test procedure |
| expected_result | M | Expected Result |
| spec_reference | N | Specification Reference |
| tc_ref_id | O | Test Case Reference ID |
| priority | Q | Test Case Priority |
| design_method | S | Test Case Design (Methods) |
| functional_safety | T | Functional Safety |
| author | AB | Test Case Author |
| remarks | AI | Remarks |

**盲區聲明（R-G11）**：本比對只認「換行前英文段逐字相等」。若某欄之英文段
被改寫（如加註記、改大小寫以外之字元），本法會判為未命中而非誤命中 ——
**其失效方向是漏，不是錯配**；16/16 全命中故本輪無漏。近似欄之排除向
（R-G9）：`C` = `Requirement or Design`（其後 `ID (Polarion)` 在次行）
與 `E` = `Test Case ID (TestRail)` **皆未被誤配**至 `req_id` / `tc_id`。

**R-PMH3(a) 之遵守聲明**：本欄位表產出於 r9 表頭之 dump 與程式化比對，
**產出後**方比對既有 feature。比對結果：與 `features/power/feature.yaml`
之欄字母**巧合一致**（同為兩個 `Estimated Test Time` 之版面），但二者
**分頁名不同**（本 feature `Test Case Specification 測試用例規範`；
`features/power` 為 `Test Case Specification&Result`），非同一份版面。
此為**獨立實測之相互佐證**，不是沿用。

### 4.3 `workbook_state` 逐列判定（canon §2 三步）

**步驟一 —— filled row**（`Test Item(I)` 或 `TC ID(F)` 非空）：
掃 r10 至 `max_row`（221），得 **48 列**，列號集合 = `{10, 11, …, 57}`，
連續無空洞。r58 以下全空。

**步驟二 —— qualifying done row**（三條件皆須成立）：

| 條件 | 結果 |
|---|---|
| (a) `author(AB)` 非空 | **0 / 48** |
| (b) `Procedure(L)` 具 ≥2 編號步驟（`(?m)^\s*\d+[.)]\s`） | **0 / 48** |
| (c) 內容非 placeholder | — 未及判定（(a)(b) 已否決） |

→ **qualifying done row = 0**，列號集合為空集。

**各欄非空計數（r10–57，48 列）**：

| 欄 | 計數 | 欄 | 計數 |
|---|---|---|---|
| B No.# | 48 | O tc_ref_id | 0 |
| D req_id | **48** | Q priority | 0 |
| F tc_id | **0** | S design_method | 0 |
| G test_group | **48** | T functional_safety | 0 |
| H test_set | **48** | AB author | **0** |
| I test_item | **48** | AI remarks | 0 |
| J pre_conditions | 0 | L test_procedure | **48** |
| K input_test_data | 0 | M expected_result | **48** |
| | | N spec_reference | **48** |

**與 handoff §3.2 之對照**：非空欄集合 `{B,D,G,H,I,L,M,N}` **完全相符**；
`F` 非空 = 0 相符；`AB` 非空 = 0 相符；`L` 具 `^1.` 編號步驟 = 0 相符；
合併儲存格 `{A1:AF1, B7:AB7, U8:AA8, AC7:AI7, D5:F5}` **五者逐一相符**；
`D5`（範圍 Scope）**確為空白**；分頁清單 10 個逐一相符。

**步驟三 —— 分類**：
- 不是 `BLANK`：其定義為 zero filled rows，此處 filled = 48。
- 不是 `PARTIAL_CLEAN`：其定義需 contiguous **done** region，此處 done = 0。
- 不是 `PARTIAL_INTERLEAVED`：需 done 與 regen 交錯，此處無 done 段。
- 不是 `FULL`：需全列 qualify，此處 0 列 qualify。

→ **四類皆不合**，canon §2 末句「Ambiguous segmentation → Tier 2」成立。
**依停止條件 2，不自行歸入四類之一**；`feature.yaml` 記
`workbook_state: PENDING_RULING`。處置提案見 §6 Q1。

### 4.4 R-PMH5 之「機械搬運」宣稱 —— 逐格驗證通過

對 48 列 × 7 欄 = **336 格**逐字比對（`str().strip()` 後 `==`）：

| 036 欄 | ← 037 欄 | 逐字相符 |
|---|---|---|
| D | SWE-Requirement ID | 48 / 48 |
| G | FROP | 48 / 48 |
| H | Requirement Title | 48 / 48 |
| I | Requirement Description | 48 / 48 |
| L | Verification Method | 48 / 48 |
| M | Verification Criteria | 48 / 48 |
| N | HMI Source ID | 48 / 48 |

**336/336 全部逐字相符** —— R-PMH5 之宣稱經實證，該 48 列確為 037 之機械
搬運，無任何人為加工。`B` 欄為序號 1…48。

**此結果強化 R-PMH5 之判定**：`I`（Test Item）欄雖非空，其內容為
037 之 `Requirement Description`（完整需求敘述句），**不是 TC 標題**；
`L`（Test procedure）欄之內容為 037 之 `Verification Method`（散文，
無編號步驟）。二者皆為待改寫之草稿，不具 style authority。

---

## 5. spec_mode 分類（步驟 7，§9.1 通則 3 / 6）

**依 §9.1 通則 6，判「不可讀」前已跨 xlsx／PDF 兩形式各自實跑抽取。**

### 5.1 PDF 文字層抽取

工具：`pdftotext 25.05.0`（poppler），`-layout`。
PDF 之 Producer 為 `Microsoft® Visio® piano 2` —— **本規格為 Visio 流程圖冊，
非文件式規格**。

| 項 | 值 |
|---|---|
| 頁數 | 11 |
| 具文字之頁 | 11 |
| **文字層產出率** | **100%**（分子＝抽出非空白文字之頁數，分母＝總頁數） |
| 抽出字元 | 39,779（`-layout` 原樣）／ 15,167（空白正規化後） |
| **可錨定之編號章節** | **0** |

⚠ 正規表示式偵得之「章節號」僅頂層 `1`–`10`，經人工核對**全為誤命中**
（條列編號與圖標籤）。11 頁之頁首為敘述性標題（`Headunit Startup –
Non-GDPR/NonMaserati`、`Power Moding`、`Power Moding – Off Road+` 等），
**無 `7.1` / `10.4` 形態之編號目次**。故 **spec_reference 不可由 PDF 之
section regex 構造**（canon §3 Mode B 之前提不成立）。

### 5.2 SYS1 匯出抽取

分頁：`Basic Report`（54×7）／`Polarion`（15×2）／`_polarion`（66×6）。
`Basic Report` r1 表頭：`ID` / `Space / Document` / `Outline Number` /
`Description` / `SYSRE_HMI_Source ID` / `Type` / `_polarion`。

| 項 | 值 |
|---|---|
| 資料列 | 52（r2–r53，`ID` 形態 `NRL-nnnnnn`） |
| `Outline Number` 相異值 | **52**（1:1，無重複） |
| `Type` 相異值 | 1（`SYSRE_HMI`） |
| `Description` 字元合計 | 8,589 |
| **涵蓋之章節數** | **52** |
| **037 引用之 29 章節之命中** | **29 / 29** |

`SYSRE_HMI_Source ID` 欄之值形態為
`Power Moding HMI Logic and Flow R1 SR24 2A_{outline}`，
**與 037 之 `HMI Source ID` 欄完全同構** —— 故
`spec_reference_template` 非構造而是**複現**，可逐字驗證。

### 5.3 兩者之涵蓋比較與分工指定（通則 3）

| | `spec_pdf` | `sys1_export` |
|---|---|---|
| 涵蓋之章節數 | **0**（無編號目次） | **52** |
| 037 之 29 章節命中 | 不適用 | 29/29 |
| 內文字元（正規化） | **15,167** | 8,589 |
| 流程圖內容 | **11 頁全含** | 6 則為圖片佔位 |

**指定（§9.1 通則 3）**：
- **判讀基準（內文面）= `spec_pdf`** —— 內文完整，含 export 以圖片佔位
  取代之 6 則，且流程之語句順序以其為準。
- **追溯用（結構面）= `sys1_export`** —— `Outline Number` 為
  `spec_reference` 之唯一來源。

**依 §9.1 通則 7「增欄，不取代」二者並存**：`-layout` 對多欄流程圖會誤切
（誤切之來源），export 之 6 則圖片佔位為少內容之來源 —— 任一方皆不得整份
取代對方。

**已知例外（通則 3 要求載明，已寫入 `feature.yaml` `spec_baseline`）**：
四項，逐條見 `feature.yaml` 之 `known_exceptions` 與 A-PMH03 / A-PMH04。

**spec_mode 提案：`A+B`**（Home 之 hybrid 前例；A = export 之 outline map，
B = PDF 文字層），**並含 canon §3 之圖像 render 義務**（圖頁 render 不因
mode 而免）。

### 5.4 export ↔ PDF 之句級 diff（canon §3 Mode A blind spot 之緩解）

**分母定義（R-G8）**：52 則中排除 6 則圖片佔位、3 則長度 <15 字之標題
（outline `1` / `7` / `9`），**可比對者 43 則**。
**分子**：去除 `_x000D_` 字面量並正規化後，為 PDF 全文子字串者。

**結果：43 則中 39 則逐字命中（90.7%）**，4 則未命中。逐項歸因見
`ANOMALIES.md` A-PMH03。要點：

- **canon 所述之 Home 型漏句，於本 feature 未觀察到。** 覆蓋率最低者為
  84%，缺口全為 `-layout` 之條列再流，非漏句。
- 唯一之實質偏離為 outline **7.1 之重排**：內容 777 字 100% 見於 PDF，
  惟切成兩段落於不同位置；PDF 原文之
  「…presented (3 sec), **after the animation (3 sec) a splash screen is
  presented timeout (1.5 each).** If ignition remains off…」
  於 export 中該子句被移至後段並改寫。**本 feature 有 5 個 leaf 引 `_7.1`
  （單一章節之最大宗）**，Phase 4 須逐 leaf 以 PDF 複核。
- outline `8` 之標題為 `Starup R1Low Only`（缺 `t`），PDF 為
  `Startup R1Low Only` —— export 側之拼字錯誤。

---

## 6. `feature.yaml` 草案

全文見 `features/power_moding/feature.yaml`（YAML 可解析，`columns` 16 鍵）。
**宣告值與生效值分開記（G-C）**：

| 鍵 | 值 | 身分 |
|---|---|---|
| `feature` | `Power Moding` | **生效**（R-PMH2） |
| `slug` | `power_moding` | **生效**（R-PMH2，= 實際目錄名） |
| `test_group` | `Power Moding` | **宣告** —— Phase 3 之 Layer 1 定版前不寫回；現工作簿 G 欄之值為 FROP 標籤（R-PMH6） |
| `tc_id_pattern` | `TBD` | 未實測（F 欄 48 列全空） |
| `paths.workbook` | 交付夾之現有 036 | **暫定** —— 待 Q2 |
| `spec_mode` | `A+B` | **提案** —— §5.3 |
| `spec_reference_template` | `Power Moding HMI Logic and Flow R1 SR24 2A_{outline}` | **生效** —— 與 037 `HMI Source ID` 及 export `SYSRE_HMI_Source ID` 三方同構，已驗 |
| `workbook.columns`（16 鍵） | §4.2 | **生效** —— 16/16 實測 |
| `workbook.last_capacity_row` | `TBD` | 未實測 |
| `workbook.data_validation` | `TBD` | 未實測（隨 Q2 定案後一併測） |
| `workbook_state` | `PENDING_RULING` | **待裁** —— Q1 |
| `done_region.author_value` | `null` | **生效** —— AB 欄 48 列全空 |
| `write_back.fill_test_group_set` | `TBD` | 待 Q1／Phase 3 |
| `lint.popup_ids` | `[]` | **生效** —— 交付夾無 Pop Up List，037 亦無 PU-number id |

交付夾名 `Disclaimer screen` 僅出現於**檔頭註解之交付路徑**，
不在任何 `test_group` / TC 欄位（R-PMH2 遵守）。

---

## 7. 異常清單（`A-PMH{n}`）

| 條號 | 主旨 | 狀態 |
|---|---|---|
| A-PMH01 | 037 `FROP` 相異值 13 vs 12 —— 空值計入之口徑瑕疵 | **PENDING**（提案：R-PMH6 引用數改 12，原條文不改字） |
| A-PMH02 | scaffold 產生之 marker 前綴 `A-PO` 與 R-PMH3(b) 不合 | **RESOLVED**（已就地改為 `A-PMH`；腳本未改） |
| A-PMH03 | SYS1 匯出相對 PDF 之內文偏離（7.1 重排、8 拼字、9.1/11.1 條列再流） | **PENDING**（提案：通則 3 分工 + 通則 7 並存 + Phase 4 逐 leaf 複核） |
| A-PMH04 | SYS1 匯出 6 則 outline 為圖片佔位，內容僅存於 PDF 流程圖 | **PENDING**（提案：Phase 4 圖像 render；不判 export 不可讀） |
| A-PMH05 | `inputs/MANIFEST.sha256` 落在 `.gitignore` 之 `inputs/` 內，**雜湊檔本身未入版控**，違 §9.1 通則 9 | **PENDING**（提案見下） |

**A-PMH05 補述**：`scripts/new_feature.py` 之 `GITIGNORE` 以 `inputs/`
整夾排除，而通則 9 要求「歸檔之檔案須有可執行之 `shasum -c`，
**且該雜湊檔本身須入版控**」。二者直接衝突，且**非本 feature 專屬**。
提案（不裁定）：於 `.gitignore` 加 `!inputs/MANIFEST.sha256` 之否定規則，
或改置於 `features/power_moding/BASELINE.sha256`（`user_profiles` 之前例
使用 `BASELINE.sha256` 一詞，其落點未於本輪查核）。**本包未動 `.gitignore`**
—— 屬 canon 層之通則衝突，請分析層裁定後再改。

---

## 8. 資料請求（`DR-PMH{n}`）

**本輪無新增 `DR-PMH`。** 理由（逐項排除）：
- 四份素材已到齊且 `shasum -c` 通過；
- 037 引用之 29 章節於 SYS1 匯出命中 29/29，無缺章；
- PDF 文字層產出率 100%，無須 OCR；
- 無 Pop Up List 之需求（037 無 PU-number id、無 String/Popup Message 表頭）。

唯 A-PMH04 之圖像 render 為**執行層自行可辦**（PDF 在手），不構成資料請求。

---

## 9. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，六項。** 逐項列出（不省略）：

1. **`workbook.last_capacity_row` 與 `data_validation` 未實測。**
   `user_profiles` 之前例載明其為「B 欄公式與各 DV 之實測上界」，且 DV 含
   `x14` 擴充（`openpyxl` 讀取時已見 `Data Validation extension is not
   supported and will be removed` 警告 —— **本輪三次讀取皆出現此警告**）。
   未測之原因：Q2 未定案，母本身分未定即測會測到將被替換之對象。
   **風險**：若 Q2 裁為沿用交付夾之 036，此二值仍須補測方能寫回。

2. **`openpyxl` 之 DV 擴充警告未追。** 上述警告表示本工作簿**帶有 x14
   擴充之資料驗證**，而 `openpyxl` 讀時即丟棄。**任何以 `openpyxl` +
   `wb.save()` 之寫回都會毀掉這些 DV** —— R-G3 正為此而立
   （須用 `xlsx_surgical` splice）。本輪未寫回故無害，但**Phase 6 之寫回
   路徑必須先驗此點**。已記於此，未另立異常（R-G3 已涵蓋）。

3. **`下拉選單` 分頁之內容未實測。** `feature.yaml` 之
   `lint.design_method_source: dropdown_sheet` 為**沿用預設而非實測**。
   該分頁存在（10 分頁清單中確有），但其 vocabulary 未讀。Phase 4 之 lint
   會依賴它。

4. **封面之三個署名欄未複驗。** handoff §3.2 記「核准者 劉安哲
   AllenACLiu、審查者 張愷霏 ErinKFChang、作者欄空白」，本輪**未查證**
   —— 步驟清單未列，且 Q3（`D5` 範圍欄）之提案與封面相鄰。
   建議與 Q3 一併處理時複驗。

5. **PDF 之圖像 render 未執行。** A-PMH04 已登記為 Phase 4 目標，但
   canon §3 之「Images are always rendered for figure/table pages
   regardless of mode」是**無條件**義務。本輪只驗了文字層產出率，
   **未驗 render 之可行性**（解析度、向量圖轉點陣之可讀性）。
   嚴格說，§9.1 通則 6 之「先驗抽取能力」對圖像形式**尚未跨過**。

6. **`Reference` / `Test Case Framework` / `QS Suggestion` 三分頁未讀。**
   036 之 10 個分頁中，本輪只讀了 `Test Case Specification 測試用例規範`。
   `Test Case Framework` 分頁之名稱直指 Phase 3 之 framework 產物，
   **可能已含客戶側之 Test Group / Test Set 期望** —— 若如此，R-PMH6 之
   「G/H 兩欄延後至 Phase 3」之輸入就不只 FROP 與規格目次兩項。
   **此項為本節中風險最高者**，建議列為下一包之首要步驟。

另附一項**方法層之自我更正**（§3.3）：執行層曾以「037 列號 +1」推算
036 之列號而誤判 handoff 有誤。成因為未察 037 含 8 個 Heading 列。
**教訓**：跨表之列號對應一律以 id 實測比對，不以位移推算 —— 位移在有
過濾之表上不是定值。

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**，R-G5 / R-G12）

```
feat(power_moding): intake package 01 — scaffold, rulings, 037/036 recon
```

```
git add -- features/power_moding/.gitignore \
           features/power_moding/ANOMALIES.md \
           features/power_moding/DATA_REQUESTS.md \
           features/power_moding/DECISIONS.md \
           features/power_moding/PLAYBOOK.md \
           features/power_moding/RULINGS.md \
           features/power_moding/RUNBOOK.md \
           features/power_moding/feature.yaml \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/01_intake.md \
           features/power_moding/docs/upstream/01_intake.md

git commit -- features/power_moding/.gitignore \
              features/power_moding/ANOMALIES.md \
              features/power_moding/DATA_REQUESTS.md \
              features/power_moding/DECISIONS.md \
              features/power_moding/PLAYBOOK.md \
              features/power_moding/RULINGS.md \
              features/power_moding/RUNBOOK.md \
              features/power_moding/feature.yaml \
              features/power_moding/docs/INDEX.md \
              features/power_moding/docs/handoff/01_intake.md \
              features/power_moding/docs/upstream/01_intake.md
```

- `inputs/`（四份素材 + `MANIFEST.sha256`）依 `.gitignore` 被忽略；
  **`sandbox/` 不在 `.gitignore` 內**（`git check-ignore` 對
  `sandbox/spec.txt` 無命中），其未入 commit 是靠上列 pathspec 逐項寫全名，
  非靠 `.gitignore`。二者皆記於 A-PMH05。
- **pathspec 逐項寫全名，未用 `features/power*` 形態之萬用字元**
  —— 該 glob 自本日起會同時命中 `features/power`（R-PMH3(c)）。
- **執行層未執行任何 git 指令**（R-G5）。

### git 動作揭露（R-G6）

| 類別 | 本輪執行者 |
|---|---|
| 唯讀 git | `git check-ignore -v`（一次，用於 A-PMH05 之取證）。未執行 `git status` / `git log` / `git diff` / `git add` |
| 改狀態 git | **無** |

工作區之檔案異動全部由 `python scripts/new_feature.py --adopt-existing`、
`cp -p`、`mkdir -p`、`sed -i ''`、heredoc 寫檔造成，逐項列於 §11。

---

## 11. 本輪之全部工作區動作（供 §10 之一致性核對，R-G6）

| # | 動作 | 對象 |
|---|---|---|
| 1 | `python scripts/new_feature.py Power_Moding --adopt-existing` | 建 `features/power_moding/` 之 8 檔 + 6 目錄（`docs/handoff/01_intake.md` 之 SHA256 前後同為 `0f11160c…`，未被覆寫） |
| 2 | `mkdir -p sandbox docs/upstream` | scaffold 之 `DIRS` 不含二者 |
| 3 | heredoc 寫檔 | `RULINGS.md`（六條逐字 + 核對表 + 勘誤附註） |
| 4 | `cp -p` × 4 | 四份素材 → `inputs/` |
| 5 | `shasum -a 256 * > MANIFEST.sha256` | `inputs/MANIFEST.sha256` |
| 6 | `sed -i '' s/A-POnn/A-PMHnn/g` | `ANOMALIES.md`、`PLAYBOOK.md` |
| 7 | heredoc 寫檔 | `ANOMALIES.md`（A-PMH01–05 + 介面實測記錄） |
| 8 | heredoc 寫檔 | `feature.yaml` |
| 9 | `pdftotext -layout` | `sandbox/spec.txt`（暫存，不入版控） |
| 10 | heredoc 寫檔 | `docs/upstream/01_intake.md`（本檔） |
| 11 | heredoc 寫檔 | `docs/INDEX.md` |
| 12 | `git check-ignore -v`（唯讀） | 取證用，不改狀態；見 §10 之 git 揭露 |

**對工作簿之寫入：無**（停止條件 3 未觸發）。
**對來源目錄之寫入：無**（搬入後複測雜湊未變）。

---

## 12. 停止條件逐條檢查（canon §0 六條 + 本包二條）

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 —— 29/29 章節命中，PDF 產出率 100% |
| 2 | `workbook_state` 分段有歧義 | **觸發**（如下放包所預期）—— 已停於「不自行歸類」，記 `PENDING_RULING`，提案見 Q1 |
| 3 | 寫回不變量違反 | 未觸發 —— 本包零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | **觸發**（A-PMH05）—— 通則 9 之「雜湊檔須入版控」與 scaffold `.gitignore` 之 `inputs/` 整夾排除直接衝突，canon 無解 |
| 5 | 造值壓力 | 未觸發 —— 未實測者一律留 `TBD`／`null`／`PENDING_RULING` |
| 6 | done region 與規格矛盾 | 未觸發 —— 無 done region（AB 欄 0/48） |
| 7 | scaffold 覆寫既有檔 | 未觸發 —— `--adopt-existing` 之 SHA256 前後一致 |
| 8 | 素材清單不符 | 未觸發 —— 四份逐一相符，無多餘檔 |

---

## 13. 待裁清單之執行層回應

| # | 事項 | 執行層之實測補充 |
|---|---|---|
| Q1 | `workbook_state` 分類 | **支持另立 `PREFILLED_DRAFT`**，並補一項理由：該 48 列不僅「非空」，其 `I`（Test Item）欄之內容為 037 之 `Requirement Description` 完整敘述句、`L`（Procedure）欄為 `Verification Method` 散文（336/336 逐字驗證）。即**每一列都佔著 TC 欄位卻不是 TC** —— 寫回策略必須是「就地改寫既有 48 列」，`BLANK` 之「append from first data row」會在既有內容之後追加，產生 96 列。此為 `BLANK` 策略**實際會出錯**之處，不只是概念不合。 |
| Q2 | 036 母本身分 | **已測結構差異之一部分**：本檔為 **A–AI 35 欄**（P/R 兩個 `Estimated Test Time`），而 R-G1 母本 `_20260817_ext` 為 rev C **A–AH 34 欄**（依 `user_profiles`/`time_management` 之實測記載）。**二者版面不同，欄位表不可共用。** 另二項（DV 含 x14、B 欄公式）尚未實測 —— `openpyxl` 已對本檔丟出 x14 DV 警告，確認本檔**帶有** x14 擴充。傾向支持分析層提案（用交付夾之現有檔），因該檔已含 48 列 req 對應且已在客戶手上；惟裁定前不動 `paths.workbook`。 |
| Q3 | `D5` 範圍 Scope 空白 | **實測確認 `D5` 為 `None`**，合併範圍 `D5:F5`。支持填規格文件全名，與 037 `HMI Source ID` 及 SYS1 `SYSRE_HMI_Source ID` 三方一致。**惟本包不寫回**，待裁。附帶：封面之三個署名欄本輪未複驗（§9 第 4 項），建議一併處理。 |
| Q4 | G/H 欄最終值 | 依 R-PMH6 延後。**新增輸入一項**：036 之 `Test Case Framework` 分頁本輪未讀（§9 第 6 項），可能已含客戶側之期望值。建議下一包先讀該分頁再談 Layer 1/2。 |
| Q5 | `Verification Criteria`/`Method` 之地位 | **支持「參考輸入而非權威」**，並補證：該二欄之內容已 336/336 逐字證實為 037 之機械搬運，而 037 之該二欄本身即上游推導物；且其 `L` 欄形態為散文（0/48 具編號步驟），本就不能充當 `Test procedure`。 |
| Q6 | slug 相鄰性 | 已裁 R-PMH3(c)。**本包之 pathspec 已逐項寫全名，未用萬用字元**（§10）。 |
