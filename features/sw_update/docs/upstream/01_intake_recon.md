# 上繳包 01 —— SW Update 開案（Phase 0 intake + Phase 1 recon）

- 日期：2026-08-27
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/01_intake_recon.md`（T0–T9）
  + `docs/handoff/02_asu1_rulings.md`（A-SU1 重裁、T1'–T10）
- 本輪 commit：`f44d022`（T0／T0b／A-SU1 登記）+ 本包之後續變更
- 未結 DR：**0 筆**
- 新登記 anomaly：**A-SU2、A-SU3**（皆 PENDING，皆不阻斷 Phase 1）

---

## 一、T0–T10 逐項結果

### T0 —— 骨架

```
$ python3 scripts/new_feature.py SW_Update --adopt-existing
scaffolded /Users/peihe/Work_Projects/TC_Generator/features/sw_update
next steps:
  1. drop source files into .../features/sw_update/inputs
  2. fill .../features/sw_update/feature.yaml (spec_mode, paths)
  3. run Phase 1 recon (Claude Code, Tier 1)
  4. review DECISIONS.md [PROPOSED] items and sign (Tier 2)
```

- 目錄名：**`features/sw_update`** ✅（符合 T0 之停止條件反面）
- `kept existing` 清單：**未印出**。既有之 `docs/handoff/01_intake_recon.md`
  位於子目錄，不與任何骨架檔同名，故 adopt 模式未觸及、亦無可跳過者。
- 建出：`ANOMALIES.md`／`RULINGS.md`／`DECISIONS.md`／`DATA_REQUESTS.md`／
  `PLAYBOOK.md`／`RUNBOOK.md`／`feature.yaml`／`.gitignore`
  ＋ `inputs data batches generated scripts docs` 六目錄。

### T0b —— 字串更正

三項替換（六份 md，`--exclude-dir=handoff`）：

| 替換 | 命中檔 |
|---|---|
| `FW036_R1L_SW_Update_Profile.md` → `FW036_R1L_SWUpdate_Profile.md` | RUNBOOK.md、PLAYBOOK.md |
| `A-SW` → `A-SU`（含 `[ASSUMPTION A-SWnn]`） | ANOMALIES.md ×2、PLAYBOOK.md ×1 |
| `SW_Update` → `SW Update` | 六份全部 |

`R-SW`／`DR-SW` 於骨架中無命中（替換規則仍照施，以防後續回填）。
`feature.yaml` 未動（依 T0b 註，交 T9）。

驗證閘（兩道皆須為 0）：

```
$ grep -rn "SW_Update" --include="*.md" features/sw_update/ --exclude-dir=handoff | wc -l
       0
$ grep -rn "A-SW\|R-SW\|DR-SW" features/sw_update/ --exclude-dir=handoff | wc -l
       0
```

**留存事實**：PLAYBOOK.md §5 之 kickoff 模板因此成為 `SW UpdateHMI/PLAYBOOK.md`
（含空格）。此為模板 `{FEATURE}HMI/` 之既有形態，vehicle_category 同位置作
`Vehicle CategoryHMI/PLAYBOOK.md`，故照前例保留，未另行修飾。

### T1' —— 素材台帳（搬入由 Pei 執行）

來源目錄（唯讀，未寫入）：
`~/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/SW Update via USB/`

| # | 實際檔名（repo 內） | size (B) | sha256 | mtime | 前/後 |
|---|---|---:|---|---|:--:|
| 1 | `SoftwareUpdate_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | 205,123 | `5d67ffc17b9847a10463e2eb7372e77af39742de6670d066d482db1669a99fbf` | 2026-08-22 15:44:53 | **=** |
| 2 | `SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_(Aug_30_2023).xlsx` | 69,245 | `76268e2b6282be85ac52b74985ff6b862260923411d1c4657025e2482575efd3` | 2026-08-17 03:02:00 | **=** |
| 3 | `R1LR_Atl-H_25PI4.5 Dec Release-xOTA_CFTS_57 Reflash_20251202-2111.docx` | 133,530 | `9aa9400b3c97bfd893d13a4ba583c402e39ef415f5c517bcc4a0c9fe47336fb6` | 2026-08-22 16:05:08 | **=** |
| 4 | `SYS3_CFTS_057_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_V03_06042026_V3.0.docx` | 3,764,644 | `93389691bf2fa217c26dfc2558fa21fd52478f054b1b38763bd9eb915fd23019` | 2026-08-16 06:32:00 | **=** |
| 5 | `Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx` | 865,472 | `8970eb04dbc158e841108ac7003b82c7fab52dabbb0e9e1a23ca9cfa1855a416` | 2026-05-22 01:41:00 | **=** |
| 6 | `Software Updates FOTA HMI Logic and Flow R1 SR24 post 2A (Aug 30 2023).pdf` | 4,955,682 | `faa58c3131df3ee4117ac880324af1de634b0bc3fc445f15519b825d0e75d11e` | 2026-06-19 07:49:00 | **=** |

六份之「搬入前（源資料夾）／搬入後（`inputs/`）」SHA256 **全部相同**，
mtime 亦保存。**實際檔名與下放包 01 §三 3.1 之名皆不同**（附件正規化所致），
以本表為準。

**執行層自行補入之兩份（非上述六份素材）**：

| 檔 | 來源 | sha256 | 一致 |
|---|---|---|:--:|
| `FM-WI-FSM-036-A01 …_20260817_ext.xlsx`（200,650 B） | `forms/` | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | **=** |
| `Pop Up List HMI R1 (26PI).xlsx`（2,951,835 B） | `forms/` | `ff47b7be63e5824cafe35deda9f9ddd0a63f6ea458169ef73689a1c559ea13ea` | **=** |

理由：`feature.yaml` §六 草案將二者填於 `inputs/`（R-VC10：填 `forms/` 相對
路徑會使 recon.py 中止），vehicle_category `inputs/` 亦同時存有二者。
二者為 **repo 內既有受版控檔**，非客戶素材之搬動，故未待 Pei。
036 之 SHA 與下放包 01 §六 `workbook_master` 之宣告值 **完全一致** ✅。

`_intake/SW_Update/` 由執行層自 `inputs/` 複製而成（供 T2 之 intake.py
讀取；該腳本只接受 `_intake/<Feature>/`）。此為 repo 內衍生複本，
非素材搬動。

### T2 —— intake.py

```
$ python3 scripts/intake.py SW_Update
- `Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx` → **cfts_doc**
- `FM-WI-FSM-036-A01 …_ext.xlsx` → **workbook** — Scope: 日期 Date：; no data rows
- `Pop Up List HMI R1 (26PI).xlsx` → **popup_list**
- `R1LR_Atl-H_25PI4.5 …_CFTS_57 Reflash_20251202-2111.docx` → **cfts_doc**
- `SYS1_HMI_Software_Updates_FOTA_…_(Aug_30_2023).xlsx` → **polarion_export** — SYS1 spec export (outline numbers)
- `SYS3_CFTS_057_…SYSAD_V03_06042026_V3.0.docx` → **cfts_doc**
- `Software Updates FOTA HMI Logic and Flow R1 SR24 post 2A (Aug 30 2023).pdf` → **spec_pdf** — text-layer on 63/68 pages
- `SoftwareUpdate_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` → **spec_xlsx** — 文件名 Document name:

## Documents cited by the requirement report (need list)
- **NO requirement report found** — cannot derive the need list
## Proposed spec_mode: **A** — SYS1 spec export present (with figure PDF)
```

**下放包之「預期不命中」成立** ✅ —— 037 落 `spec_xlsx` 而非 `swra_report`，
連帶使 need list 判為「無 requirement report」。依 R-DM5／R-DM24 同型處置，
於 `feature.yaml` 設 `intake.kind_overrides`（指名 `kind: a03_report`，
附 sha256 與理由）+ `paths_meta.a03_sheet: "AnalysisReport_FULL"`，
**未改腳本任何一行**。重跑後：

```
- `SoftwareUpdate_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` → **a03_report** [kind_source: override]
```

`spec_mode` 提案 **A**，實測採認（SYS1 spec export 在場 + 附圖形 PDF），
已填入 `feature.yaml`。

### T3 —— recon.py

```
$ python3 scripts/recon.py --feature features/sw_update
assertions:
- PASS — leaf count == Functional Requirement rows: expected 307, measured 307
- PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0
recon complete: state=BLANK, leaves=307, sections=0, targets=307
```

**0 failed / 2 checked.** 產出 `RECON.md`、`DECISIONS.md`、`data/recon.json`、
`data/recon_leaf_to_section.tsv`。

**036 母本欄位為表頭字串實測，未沿用他 feature**：

- 分頁：`Test Case Specification 測試用例規範`（母本九分頁，實測選定）
- **表頭列 = 9**，該列非空儲存格 **33** 個
- recon 之表頭解析：**15 欄命中 15**（`column mapping: 15 fields resolved
  from header text`），且 **`feature.yaml column conflicts: (none)`** ——
  即執行層先行實測填入之字母與 recon 之表頭解析**完全一致**
- form layout revision：**C**（has Estimated Test Time）

| 欄 | 字母 | 表頭原字串 |
|---|:--:|---|
| req_id | D | `Requirement or Design ID 需求/設計 ID` |
| test_group | G | `Test Group 測試組` |
| test_set | H | `Test Set 測試集` |
| test_item | I | `Test Item 測試項目` |
| pre_conditions | J | `Pre-Conditions 先前條件` |
| input_test_data | K | `Input Test Data 輸入條件` |
| test_procedure | L | `Test procedure 測試程序` |
| expected_result | M | `Expected Result 預期結果` |
| spec_reference | N | `Specification Reference  規格參考` |
| tc_ref_id | O | `Test Case Reference ID 測項參考ID` |
| priority | P | `Test Case Priority 測試用例優先級別` |
| design_method | **R** | `Test Case Design  Methods 測試用例設計方法` |
| functional_safety | **S** | `Functional Safety 功能安全` |
| author | **AA** | `Test Case Author 測試案例作者` |
| remarks | AH | `Remarks 備註` |

> ⚠ `new_feature.py` 之 `feature.yaml` 模板預設為 `design_method: Q`、
> `functional_safety: R`、`author: Z` —— 對本母本**全錯**（Q 實為
> `Estimated Test Time`）。此即「不得沿用他 feature 之欄位字母」之實例。
> R-SU2 所述「母本之 R 欄 design_method 下拉」與實測相符 ✅。

037 側：**表頭列 = 7、資料列 8 起、18 欄** 實測確認 ✅；
`AnalysisReport_FULL` 之 `Categorization` 欄 = F 欄。

`workbook_state = **BLANK**` ✅（done rows 0 / draft rows 0 / authors present: none），
與 R-SU2 相符。design-method 詞彙 9 字串（自 `下拉選單` 分頁）。

**A-TM15 處置**：recon 因 `DECISIONS.md` 已存在而改寫 `DECISIONS.new.md`。
既有檔為 `new_feature.py` 之**未填模板**（純標記語意說明，無任何實測內容），
故以 recon 實測稿取代之，`DECISIONS.new.md` 隨之消滅。無內容遺失。

**留存事實（既有全域 anomaly 之複現）**：`DECISIONS.md` 第 34 行作
`- spec_reference: [PROPOSED: None]` —— `spec_reference_template: null`
被顯示層印為字面 `None`。此即 A-VC11（PENDING，全域排程），
本 feature **不重複立案**。

### T4' —— 對 repo 內複本重測，逐項比對

見 §三。**36 項中 33 項 `=`、3 項 `≠`**，三項皆已查明成因並登記
（A-SU2 兩項、CFTS_57 TOC 行數一項）。

### T5' —— PU 掃描（兩源）

**(i) 037 全欄**（全分頁、含表頭列）：unique **4**

| PU | 列 |
|---|---|
| PU0303 | 94, 95 |
| PU0304 | 155 |
| PU0410 | 238, 243 |
| PU0416 | 102 |

**(ii) 規格 PDF 文字層逐頁**：unique **52**，逐一附頁碼（R-SU6 v2(b)）。
全清單見 §六。彈窗需求表位於 **p.10–p.20**，其餘為內文引用。

**對 `forms/Pop Up List HMI R1 (26PI).xlsx` 之存在性查核**：
檔案在場（三分頁 `Main`／`Templates`／`Drop Down Fields`，unique PU **1,341**）。
兩源聯集 52 個逐一查核：**51 個查得、1 個查無**。

- **查無者：`PU971`**（3 位數形態，僅見於 **p.46**）
- 同文件另有 `PU0971`（p.43、46、49），於清單內**查得**
- 依 T5「查無不得代以語意相近者」，**未代以 `PU0971`**，
  已登 A-SU3，並排除於 `lint.popup_ids` 之外（該鍵收 51 個）

### T6 —— SYS1 `SYSRE_HMI_Source ID` 形態檢查

`Basic Report` 120 列，逐項：

| 檢項 | 結果 |
|---|---|
| 空值 | **0** |
| unique | **120 / 120**（無重複值） |
| 前綴逐字一致性 | **120/120 同前綴**，皆為 `SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_(Aug_30_2023)_…` |
| 含空白或異常字元者 | **0** |
| 與 `Outline Number` 欄互證 | **不符 0 / 120** —— 每個 Source ID 皆以其列之 Outline Number 結尾 |

**形態外者：0 筆。** 該欄之值即 R-SU4 v2(b) 之錨 token 原值，
且其構成恰為 `{檔名 stem}_{Outline Number}`（抽樣：`…_(Aug_30_2023)_1`、
`…_1.1`、`…_1.2`）。惟依 R-SU4 v2(b)，仍**逐字取欄原值，不由 stem 構造**。

### T7 —— DATA_REQUESTS.md

**本輪 0 筆** ✅。已於該檔記逐項結案理由（CFTS_57／HMI 規格／VF747／
PROXI／Pop Up List／DBC／LID 七項皆不需 DR）。standing rule 照常生效。

### T8 —— ANOMALIES.md

- **A-SU1 → RESOLVED**（處分引用下放包 02 §一，R-G13 citation-by-reference）
- **A-SU2 新登**（PENDING）—— 037 `Source Requirement ID` 欄之三形態
- **A-SU3 新登**（PENDING）—— `PU971` 查無

§四 4.5 之三項 SYSAD 分配表錯位觀察：依 R-SU5(c)／Q5 **未立案**，本包不再提。

### T9 —— feature.yaml

已填實。`reference:` 綁定判準依 R-G15／R-DM37（其變動會使既有產出失效者一律綁定）：

| 綁定 | 依據 |
|---|---|
| a03_report、sys1_export、spec_pdf、cfts57_report、sysad、vf747 | 六份素材全綁 |
| workbook_master | `forms/` 原件，SHA 與下放包宣告值一致 ✅ |
| popup_list | `forms/` 原件，T5' 之查核來源 |
| **proxi**（新增） | SWE1-FOTA-208 引用 `<Brand_Configuration_2>`，於 `forms/PROXI_HDCC27_R3_20250424.xlsx` `Format` 表 row 566 **查得**（Infotainment_Configuration_13，byte 130，4 bit，0=Unbranded/1=Fiat/…）；列舉值變動會使該列預期結果失效 |
| **DBC —— 不綁（裁定，非遺漏）** | 037 之三個 `$FOTA_MASTER.*$` 皆經 CarProperty Manager 之 vehicle property 介面取得，非 CAN frame；`forms/` 兩份 .dbc 對 `FOTA` 之命中數 **0** |
| **LID —— 不綁** | 037 無 Logical Identifier 引用 |

`recon_assertions` 只宣告 `functional_requirement_count: 307`（R-VC9）。
`spec_reference_template: null`、`done_region.author_value: null`（R-SU2 佔位）。

### T10 —— 錨點池結構驗證（R-SU4 v2 (a2)）

產出：**`features/sw_update/ANCHOR_POOL.md`**

方法：以 `<w:p>` 切分 `word/document.xml`（**1,742 段**），取 `w:pStyle`
為結構判準。heading style `1`–`4` 之 `{7位}` 為章節物件；TOC style `10`–`40`
為其鏡像，**不獨立入池**；其餘段落之 7 位數依右鄰之 `: [Artifact Type:…]`
宣告或左鄰文句歸類。

| 類型 | unique id | 入池 |
|---|---:|---|
| 章節物件 | **87** | ✅ |
| 需求物件（`[Artifact Type:Subsystem Functional Requirement]`） | **478** | ✅ |
| Description 物件（`[Artifact Type:Description]`） | 135 | ❌ |
| 不可歸類 | 21 | ❌ |
| **合計** | **721** | 入池 **565** |

**錨點池 = 565**（章節 87 + 需求 478）。**只分類不對應** —— 037 對應屬 Phase 2/3。

不可歸類 21 筆之全清單見 `ANCHOR_POOL.md` §五，分四型：
內文交叉引用（`4907243`、`4907395`、`4907490`、`4907608`、`4762830` 等）、
圖檔名（`4615844`–`4615848`，形態 `{id}- CFTSMV057_CIP_R1_O…_inline.`）、
非 Polarion 之 `WS 3369439`／`WS 3440351`、以及一筆
`&lt;size&gt;1234567&lt;/size&gt;` 之標記外洩偽陽性。

> **須裁項**：R-SU4 v2 (a2) 只定三分類（章節／需求／不可歸類），
> 未預期 **Description 物件（135）** 這一類 —— 其為結構上可驗證之
> Polarion 物件（有 `[Artifact Type:Description]` 宣告、有 `[State:Approved]`），
> 但既非章節亦非需求。本包**依條文從嚴排除於池外**並全數列表，
> 是否另立第三入池類請裁。

---

## 二、R-SU1 ~ R-SU6 之逐條抄錄核對結果

抄入位置：`features/sw_update/RULINGS.md`。

抄錄依下放包 02 §三 之指示：R-SU1／R-SU2／R-SU3／R-SU5 取下放包 01 §二
原文，R-SU4／R-SU6 取下放包 02 §二 之 v2 全文（含沿革行）；v1 不入正本。

核對法：以程式自兩份下放包之 ``` 圍籬抽出區塊，寫入 RULINGS.md 後
**回讀該檔**，與來源區塊逐字元比對（非目視）。

| 條 | 來源 | 字元數 | 字面一致 | sha256[:12] |
|---|---|---:|:--:|---|
| R-SU1 | 01 §二 | 474 | **OK** | `78248cd16f79` |
| R-SU2 | 01 §二 | 835 | **OK** | `f2d1b7663a1a` |
| R-SU3 | 01 §二 | 620 | **OK** | `d01d11cb4f19` |
| R-SU4 | 02 §二（v2） | 1,331 | **OK** | `0fa953653415` |
| R-SU5 | 01 §二 | 412 | **OK** | `94791d3d5e0b` |
| R-SU6 | 02 §二（v2） | 673 | **OK** | `d99834f40411` |

**六條全部逐字一致，無改寫、無合併、無縮寫。**

---

## 三、T4' 比對表

基準：下放包 01 §三、§四；其中 §三 3.1 之 #3–#6 格式／大小改對
下放包 02 §一（A-SU1 repo 實測表）比對。

### 3.1 素材身分（對 A-SU1 表）

| 項 | 基準 | repo 實測 | |
|---|---|---|:--:|
| #3 CFTS_57 格式 | 真 OOXML docx | 真 OOXML docx（`file` + `word/document.xml` 可解） | **=** |
| #3 大小 | 133,530 B | 133,530 B | **=** |
| #4 SYSAD 格式／大小 | 真 OOXML／3,764,644 B | 同 | **=** |
| #5 VF747 格式／大小 | 真 OOXML／865,472 B | 同 | **=** |
| #6 PDF 版本 | PDF 1.6 | `%PDF-1.6` | **=** |
| #6 頁數 | 68 | 68 | **=** |
| #6 全文字層 | 68/68 | 68/68（判準 >0 字元） | **=** |
| #6 字元數 | 83,286 | 83,286（`.strip()` 法）／83,356（raw `len` 法） | **=**（見註） |
| #6 大小 | 4,955,682 B | 4,955,682 B | **=** |
| #1 037 大小 | 205,123 B | 205,123 B | **=** |

> **註（R-G8 量測條件差異，非不符）**：A-SU1 之 83,286 為逐頁
> `get_text().strip()` 之字元和；`recon.py`／`intake.py` 用未 strip 之
> `len(get_text())` 得 **83,356**，差 70 字元為頁尾空白。
> 另 intake.py 之文字層判準為「單頁 >100 字元」故報 **63/68 頁**，
> 5 頁落 1–100 區間（p.23=73、p.42=74、p.50=74、p.51=87、p.66=84）。
> 二法皆正確，差異純為門檻不同。**後續一律引用本台帳所記之實測值。**

### 3.2 037 母體（§三 3.3）

| 項 | 基準 | 實測 | |
|---|---:|---:|:--:|
| 資料列 | 383 | 383 | **=** |
| 連號、無重號（001–383） | 是 | 是 | **=** |
| Functional Requirement | 307 | 307 | **=** |
| Non Functional Requirement | 4 | 4 | **=** |
| Heading | 45 | 45 | **=** |
| Information | 25 | 25 | **=** |
| Categorization 空白 | 1 | 1 | **=** |
| Out of scope | 1 | 1 | **=** |
| **驗證母體（R-SU3）** | **311** | **311** | **=** |

### 3.3 欄位分布（§三 3.4）

| 項 | 基準 | 實測 | |
|---|---:|---:|:--:|
| Sub Cat `Service` | 223 | 223 | **=** |
| Sub Cat `HMI` | 87 | 87 | **=** |
| Sub Cat 空白 | 73 | 73 | **=** |
| Priority `High` | 271 | 271 | **=** |
| Priority `Medium` | 34 | 34 | **=** |
| Priority `Low` | 6 | 6 | **=** |
| Priority 空白 | 72 | 72 | **=** |
| SourceReqID 非空 | 373 | **383** | **≠** |
| SourceReqID 值域 | 1–526 | 1–526 | **=** |
| SourceReqID unique | 364 | **374** | **≠** |
| SourceReqID 重複引用數 | 9 | 9 | **=** |
| 重複名單 | 43,68,69,112,395,411,444,475,480 | 完全相同 | **=** |

> **兩項 `≠` 之成因（已登 A-SU2）**：該欄 383 列**全部非空**，
> 但 13 格不合 `SYS-RA-FOTA-{n}` 形態 —— 3 格以 `/` 併記兩 id、
> 10 格為 `SYS-RA-VF747_V2/V6-{n}` 族。下放包之 373／364
> **可完整重現**（每格 `re.search` 取首個 FOTA id：370+3=373；
> unique 361+{336,360,506}=364），即數字無誤而量測法靜默丟棄了
> 併記格之第二 id 與 10 個 VF747 格。詳見 `ANOMALIES.md` A-SU2。

### 3.4 037 版面（§三 3.2）

| 項 | 基準 | 實測 | |
|---|---|---|:--:|
| 分頁名 `AnalysisReport_FULL`（無空格） | 是 | 是 | **=** |
| intake 預期不命中 `swra_report` | 預期 | 實際落 `spec_xlsx` | **=** |
| 表頭列 | 7 | 7 | **=** |
| 資料列起 | 8 | 8 | **=** |
| 欄數 | 18 | 18 | **=** |
| 無 `HMI Source ID` 欄 | 是 | 是 | **=** |
| 無 `FROP` 欄 | 是 | 是 | **=** |

### 3.5 CFTS_57（§三 3.5）

| 項 | 基準 | 實測 | |
|---|---:|---:|:--:|
| ObjectID `{7位}` 命中 | 174 | 174 | **=** |
| ObjectID `{7位}` unique | 87 | 87 | **=** |
| TOC 式行 | 174 | **87** | **≠** |
| 頂層結構 1–4（4.1–4.13） | 是 | 是 | **=** |

> **`≠` 之成因**：TOC 實為 **87 行**（`PAGEREF` 次數 = 87，
> TOC style `10`–`40` 段落亦為 87）。174 是 brace 形之**總命中**
> = TOC 87 + 正文標題 87（同一批 ObjectID 出現兩次）。
> 下放包將二者等同。unique 87 不受影響，R-SU4 v2 (a2) 之
> 「TOC brace 形 87 個」所指之集合亦不受影響。

### 3.6 SYS1 export（§三 3.6）

| 項 | 基準 | 實測 | |
|---|---|---|:--:|
| `Basic Report` 資料列 | 120 | 120 | **=** |
| 欄序（7 欄） | ID / Space・Document / Outline Number / Description / SYSRE_HMI_Source ID / Type / _polarion | 完全相同 | **=** |
| 頂層章 | 28 | 28 | **=** |
| 深度分布 1/2/3 | 28 / 89 / 3 | 28 / 89 / 3 | **=** |

### 3.7 §四 之觀察

| 項 | 基準 | 實測 | |
|---|---:|---:|:--:|
| title/desc 含 `usb`（4.2） | 26 | 26 | **=** |
| desc 含 `USB Update Service`（4.2） | 20 | 20 | **=** |
| Priority 空白 ∩ SubCat 空白（4.4） | 「高度重合」 | **72 / 72 全重合**（Priority 空白 72 全在 SubCat 空白 73 之內） | **=** |
| 4.4 之空白列皆為 Heading/Information 類 | 是 | 是（72 列皆 Heading/Information/Out of scope/空白） | **=** |

§四 4.3（SYSAD 四線分解）與 4.5（三項錯位）為敘述性觀察，
依 R-SU5(c) 不再提，未列入比對。

**小計：36 項中 33 `=`、3 `≠`**，三項 `≠` 皆已查明成因並登記，
無一項為 repo 複本與素材不一致所致（A-VC5 之型態未再現）。

---

## 四、素材台帳

見 §一 T1'。六份素材 + 兩份 repo 內建檔，實際檔名、絕對路徑基準
（`features/sw_update/inputs/`）、搬入前後 SHA256、mtime 皆已記錄，
並同步寫入 `feature.yaml` 之 `reference:` 與 `RECON.md` 之 Inputs 節。

---

## 五、未結 DR 清單

**空表。** 本輪 0 筆，逐項結案理由見 `DATA_REQUESTS.md`。

---

## 六、T5' 之 PDF PU 全清單（含頁碼）

`PU0091` p.18,34,35,36 ／ `PU0152` p.10,26 ／ `PU0154` p.10,24 ／
`PU0155` p.10,25 ／ `PU0156` p.10,25 ／ `PU0157` p.10,24,25,26 ／
`PU0159` p.10 ／ `PU0195` p.11,24 ／ `PU0196` p.11,26 ／
`PU0276` p.11,25,26 ／ `PU0298` p.11,24,25,28,45,46 ／
`PU0301` p.11,26,33,48 ／ `PU0303` p.12,28,29,41 ／
`PU0304` p.12,27,31,32 ／ `PU0410` p.12,27,29,30,41,43,46,53,54,59,63 ／
`PU0411` p.12,30,31,46,49 ／ `PU0412` p.13,31,47,49 ／
`PU0413` p.13,27,30,32 ／ `PU0414` p.13,27,28 ／
`PU0415` p.13,27,28,32,33,41 ／ `PU0416` p.13,28,45 ／
`PU0481` p.18,34 ／ `PU0485` p.18 ／ `PU0486` p.18,38 ／
`PU0492` p.18,34 ／ `PU0499` p.19,53,56 ／ `PU0500` p.20,54,58 ／
`PU0501` p.20,53,54,57,61,64 ／ `PU0502` p.20,59,63,64 ／
`PU0950` p.14,33 ／ `PU0964` p.14,43,47,49 ／ `PU0965` p.14,43,44,47 ／
`PU0966` p.14,44,45 ／ `PU0967` p.14,45,48 ／ `PU0968` p.15,44,47 ／
`PU0969` p.15,48 ／ `PU0970` p.15,33,48,60,62,63,64 ／
`PU0971` p.15,43,46,49 ／ `PU0980` p.15 ／ `PU1195` p.16 ／
`PU1196` p.16,24 ／ `PU1197` p.16,27,31 ／ `PU1198` p.16,27,30 ／
`PU1199` p.16,27 ／ `PU1200` p.17,27,28,32,33 ／ `PU1211` p.19,53,56 ／
`PU1212` p.19,54,58 ／ `PU1213` p.20,53,54,57,61 ／
`PU1391` p.17,22,32,49 ／ `PU1392` p.17,47,49 ／ `PU1393` p.17,47,49 ／
**`PU971` p.46 —— 查無（A-SU3）**

---

## 七、量測條件揭露（R-G8）

| 項 | 方法／工具 | 偽陽性風險 |
|---|---|---|
| 037 全數字（T4'） | openpyxl `read_only=True, data_only=True`，`AnalysisReport_FULL` 列 8 起、col1 非空者計入 | `data_only=True` 取快取值；若工作簿曾以非 Excel 工具存過，公式格可能為 None。本檔全為字面值，抽樣覆核無公式格 |
| Source ID 形態（A-SU2） | `re.fullmatch(r"SYS-RA-FOTA-\d+")` 逐格；與 `re.search` 法對照 | `/` 以外之分隔符未掃 —— 已以 383−370−10=3 閉合，無殘餘 |
| PDF 文字層（T4'／T5'） | PyMuPDF `page.get_text()`；字元數兩法（strip／raw）並記 | 文字層抽取可能漏字（A-SU3 之 `PU971` 即無法由抽取結果自證是筆誤或漏字），故該項列 PENDING 待目視 |
| PU 掃描（T5'） | 正則 `PU\d+`；037 掃全分頁全儲存格、PDF 逐頁、清單掃三分頁全儲存格 | 位數不定之正則會同時命中 3 位與 4 位形態 —— 此為**刻意**，`PU971` 正因此被捕獲而非被靜默正規化 |
| CFTS_57 結構（T10） | `zipfile` 讀 `word/document.xml`，`<w:p>` 切段（1,742 段），`w:pStyle` 為結構判準 | `w:pStyle` 為版面屬性，理論上可手動套用而與語意脫節 —— 已以「章節物件 87 = TOC PAGEREF 87」交叉驗證 |
| SYS1 形態（T6） | openpyxl 讀 `Basic Report`；前綴、unique、字元集、與 `Outline Number` 互證四路 | 互證為字尾比對，若 Outline Number 為數值型會誤判 —— 已全部轉字串後 `rstrip` 比對，0 不符 |
| DBC／PROXI 掃描（T9） | `grep -ci FOTA` 兩份 .dbc；openpyxl 掃 PROXI 全分頁 `Brand_Configuration` | DBC 以純文字 grep，若訊號名經縮寫則漏 —— 已用 037 側之語意（CarProperty Manager／vehicle property）獨立佐證非 CAN |

---

## 八、獨立自評 —— 本包有無「應驗而未驗」之項

**有三項，逐項列明：**

1. **`spec_mode: A` 未做 FO §3 之逐條核對。** T2 之 A 為 intake.py 之
   自動提案（判準：SYS1 export 在場 + 附 PDF），執行層採認而未回到
   FO §3 逐條比對五種模式之定義。R-SU4 v2 末段稱「`spec_mode` 由執行層
   依 FO §3 實測後填入」—— 嚴格說本包填的是**腳本提案值**，不是
   逐條實測結果。風險低（A 之判準與本 feature 素材組成明顯相符），
   但形式上未足。

2. **R-SU3 之母體 311 仍無機器保證。** `recon_assertions` 只實作
   `functional_requirement_count: 307`，311（307 + NFR 4）無對應
   assertion 可宣告，目前僅靠 T4' 重測與本包交叉檢查守護。
   此為 `feature.yaml` 已明載之揭露義務，逐包重申。

3. **A-SU3 之 `PU971` 未做目視覆核。** R-SU6 v2(c) 已授權「文字層未載
   之內容以頁圖 render 目視」，本包**未**對 p.46 執行該步驟即登 PENDING。
   理由是判讀結果將直接決定 `lint.popup_ids` 之內容（屬 Tier 2 之
   id 認定），非執行層可逕定；但「先目視取得字面事實、再提請裁定」
   本可在本輪完成，未做屬本包之保守。若要，下輪可補。

**另聲明兩項非缺漏之處置**，避免被誤讀為漏做：

- `_intake/SW_Update/` 為執行層自 `inputs/` 複製之衍生複本
  （intake.py 只接受該路徑）。素材搬動仍由 Pei 執行，未違 T1' 之分工。
- 036 母本與 Pop Up List 由執行層自 `forms/` 複製入 `inputs/`。
  二者為 repo 內受版控檔，非客戶素材，且下放包 §六 之
  `feature.yaml` 草案本就將其路徑填在 `inputs/`。

---

## 九、待裁項彙總

| # | 項 | 出處 |
|---|---|---|
| 1 | **A-SU2** —— R-SU5 之形態陳述與 (a) 之理由對 13 格不成立；VF747 族 10 列是否另立第三錨點家族 | §三 3.3 |
| 2 | **A-SU3** —— `PU971` 是否認定為 `PU0971` 之筆誤（建議先目視 p.46） | §一 T5' |
| 3 | **Description 物件（135）** 是否入錨點池 —— R-SU4 v2 (a2) 之三分類未預期此類 | §一 T10 |
| 4 | `spec_mode: A` 是否要求執行層補做 FO §3 逐條核對 | §八 1 |
