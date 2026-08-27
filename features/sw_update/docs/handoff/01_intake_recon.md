# 下放包 01 —— SW Update 開案（Phase 0 intake + Phase 1 recon）

- 日期：2026-08-27
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`sw_update`
- 對應上繳：`features/sw_update/docs/upstream/01_intake_recon.md`
- 前一包：無（本 feature 首包）
- 裁定狀態：Q1（slug）、Q2（範圍）、Q3（CFTS_57 錨）、Q4（HMI 索引）、
  Q5（不立 A／不發 DR）、Q6（test_group）、Q7（036 母本／BLANK）
  —— **全部已裁（Pei 2026-08-27），無待裁項**

---

## 一、本包之目的與界線

建立 `features/sw_update/` 之骨架、驗明六份素材、實測 037 需求母體與
`workbook_state`，並完成 Phase 1 recon。

**本包不產出任何 TC，不寫回工作簿，不動 git。**

界線宣告（canon §5a）：本包 §三、§四之全部數字量自 Claude Project 附件複本，
**非** repo 內複本。執行層須對 repo 內複本重測並記 SHA256 入素材台帳；
台帳建立後，後續各輪一律引用台帳所記之實測值，
**不得回頭引用本包之任何數字**。本包之數字僅供 T4 之比對基準。

本包落檔時 `features/sw_update/` 僅有 `docs/handoff/` 路徑與本檔。
T0 以 `--adopt-existing` 補齊骨架，該模式不覆寫既有檔（見腳本註）。

---

## 二、裁決條文（逐字抄入 `features/sw_update/RULINGS.md`）

> 抄錄時逐字，不改寫、不合併、不為欄寬而縮寫（R-G23）。抄畢於上繳包附逐條核對結果。

```
R-SU1（feature 身分與 test_group）

`feature` 為 `SW Update`，slug 為 `sw_update`，`test_group` 為
`SW Update`。（Pei 2026-08-27 裁定 Q1、Q6。）

命名依據：037 檔名作 `SoftwareUpdate`、SYSAD 作 `Software Update`、
CFTS 母件為 CFTS_57 Reflash —— 交付面統一取 `SW Update`，
由 Q6 裁定，不再援引來源檔名之拼寫。

裁決前綴為 `R-SU`、異常前綴為 `A-SU`、資料請求前綴為 `DR-SU`，
不與任何既有 feature 共用序號。

`scripts/new_feature.py` 之 abbr 推導（`feature[:2].upper()`）對
`SW_Update` 產出 `SW`，與規定前綴 `SU` 不符 —— 此為 A-VC4 / A-TM04
既已登記之同源缺陷，本 feature 不重複立案，以 T0b 字串更正處理。
```

```
R-SU2（036 母本與 workbook_state）

（Pei 2026-08-27 裁定 Q7 准。）

036 母本套用 R-G1 全域條文：
`forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
Specification & Result_SWQT_20260817_ext.xlsx`。

`workbook_state = BLANK`。無既有 done region，`done_region` 節不生效
（`detection: author`、`author_value: null` 為佔位，不得據以推論存在作者）。

配套三項：
(a) `write_back.fill_test_group_set = true`（canon §2.1，BLANK -> FILL）
(b) `write_back.author_value = "PeiPYHsu"`
(c) `write_back.tc_ref_id_value = "NEW"`

母本之 R 欄 design_method 下拉為 x14 擴充。**任何以 openpyxl 存回母本
之操作都會摧毀該下拉**（R-G1 註）。寫回一律採 XML 外科式修改：
以 zip 開檔、僅改 `xl/worksheets/sheet*.xml` 之目標儲存格、原樣重打包，
並於前後比對 `<dataValidation`、`x14:dataValidation`、
`<conditionalFormatting`、工作表數、drawing/chart rel 數之原始 XML 計數。

**本條之前提為「Pei 手上無既存之 SW Update 036」。** 若日後出現
含他人已填 done region 之既存 036，本條即失效，須重裁，且 §三之
母體全集須先與該工作簿之既有 req_id 集合做差集。
```

```
R-SU3（驗證母體 —— Q2 之落地）

（Pei 2026-08-27 裁定 Q2「按 037 有納入的範圍」；本條為其落地解讀，
Pei 2026-08-27 裁認。）

驗證母體為 037 `AnalysisReport_FULL` 之：

  `Functional Requirement`     307 列
+ `Non Functional Requirement`   4 列（SWE1-FOTA-281 ~ 284，
                                      皆 Service / High，內容可測）
= **311 列**

不入母體：
- `Heading` 45 列、`Information` 25 列
- `SWE1-FOTA-296`（`Categorization` 為空白；title `Regular Updates`，
  實為標題性質列）
- `SWE1-FOTA-335`（`Out of scope`；title 為空）

範圍以 037 實際納入為準 —— SYSAD 分解出之四線
（Software Update via USB / FOTA / ROV FOTA / TBM FOTA）中，
037 未納入之內容（見 §四 4.5 之觀察）**不補、不擴**，
不因 SYSAD 或 CFTS_57 有相應章節而外加需求單元（IN §8.2）。
```

```
R-SU4（spec_reference 之雙家族錨點）

（Pei 2026-08-27 裁定 Q3 准、Q4。）

本 feature 之 spec_reference 有兩個家族：

(a) CFTS 家族 —— IN §10.7(a)：`CFTS057-{ObjectID}`，ObjectID 為
    CFTS_57 Reflash 報告內之 7 位 Polarion 號碼（`{490xxxx}` 形態，
    衍生本實測 87 個 unique）。
    素材身分揭露：repo 所存之 CFTS_57 Reflash 為 **UTF-8 純文字
    衍生本**（副檔名 .docx 但非 OOXML），非權威二進位原件。
    Pei 裁定（Q3 准）：該衍生本之 ObjectID 可用作錨，
    不另發 DR 索取原件。

(b) HMI Logic and Flow 家族 —— IN §10.7(b)：
    `SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_(Aug_30_2023)_{章節號}`
    章節 token **逐字取 SYS1 export `Basic Report` 之
    `SYSRE_HMI_Source ID` 欄原值**，不構造、不改寫、不去括號、
    不重新 token 化（R-VC4 同理）。

排列一律依 IN §10.7：一個 ObjectID／章節號一行，前綴逐行重述，
禁用 `,`、`、`、`;` 串接，同文件內升冪；同一 TC 兼引兩家族時
CFTS 行在前、HMI 行在後（SWC 基準之家族排序）。

**本 037 為 18 欄舊版面，無 `HMI Source ID` 欄** —— 037 列與錨點之
對應無現成欄可抄，須於 Phase 2/3 建立錨定協定（候選錨表 + 雙路驗證，
R-AM15 之教訓適用）。本條只定家族形態，不定對應方法。

`feature.yaml` 之 `spec_reference_template: null`（查得，非構造）。
`spec_mode` 之字母由執行層依 FO §3 實測後填入，本條不逕定。
```

```
R-SU5（037 之 Source Requirement ID 欄）

037 之 `Source Requirement ID` 欄形態為 `SYS-RA-FOTA-{n}`，
分析層實測：非空 373 列、值域 1–526、unique 364，
**9 個 source id 被多列引用**（43, 68, 69, 112, 395, 411, 444, 475, 480）。

拘束三項：
(a) `spec_reference` 不得取本欄 —— 本欄指向之 SYS-RA 母體
    無對應規格檔可查，且與兩家族錨點（R-SU4）無字面關係。
(b) 本欄僅作 037 內部追溯保留，不進入任何 TC 欄位。
(c) §四 4.5 之三項 SYSAD 分配表錯位觀察，Pei 裁定（Q5）
    **不立 A 案、不發 DR** —— 記錄於下放包即止，
    不阻斷任何 Phase，後續不再重提。
```

```
R-SU6（HMI Logic and Flow 規格本文之可及性）

素材身分揭露：`Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_
post_2A_Aug_30_2023.pdf` **非 PDF** —— 實為 zip 容器，內含 137 張
JPEG 頁圖（1.jpeg ~ 137.jpeg），無文字層，不可檢索。
Pei 確認（Q4）：僅此圖檔版存在，無可檢索版。

處置：
(a) SYS1 export（`SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_
    R1_SR24_post_2A_Aug_30_2023.xlsx`）為本規格之**參考索引**
    （Pei 補入，Q4）：`Basic Report` 120 列含章節號 + 需求描述文字，
    為章節定位與描述文之第一查找來源。
(b) 規格內文之細節（畫面、流程圖、彈窗版面、SYS1 描述未載之值）
    須逐頁目視頁圖取得；**每次取用記頁碼**（`p.{n}` 形態）入
    reasoning 或工作檔，供覆核重走。
(c) 頁圖之目視屬 FO §3「Images are always rendered」之既定途徑，
    不因此違 R-G36（機器抽取優先）—— R-G36 針對可抽取而不抽取者；
    本件無文字層可抽。
(d) 值之判讀自圖而來者，判讀不確定時依 IN §8.4.1 保留模糊、
    登記待查，不得補值。
```

---

## 三、素材實測（分析層量測值，供 T4 比對）

### 3.1 素材清單

| # | 檔名（Project 附件） | 角色 | 實際格式 | 大小 |
|---|---|---|---|---|
| 1 | `SoftwareUpdate_FMWIFSM037A03_STLA_Report_SWRA.xlsx` | 037 A03 SWRA | 真 xlsx | 205,123 B |
| 2 | `SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_Aug_30_2023.xlsx` | SYS1 Polarion export（HMI 規格索引） | 真 xlsx | （附件後補，T1 實測） |
| 3 | `R1LR_Atl-H_25PI4_5_Dec_Release-xOTA_CFTS_57_Reflash_20251202-2111.docx` | CFTS_57 Reflash 報告（錨點來源） | **UTF-8 純文字**（非 OOXML） | 252,371 B |
| 4 | `SYS3_CFTS_057_FM-WI-FSM-011-A01_系統架構設計_System_Architectural_Design_SYSAD_V03_06042026_V3_0.docx` | SYSAD V03 | **UTF-8 純文字**（非 OOXML） | 123,925 B |
| 5 | `Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx` | 整車級 FOTA 管理（VF747） | **UTF-8 純文字**（非 OOXML） | 131,896 B |
| 6 | `Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_Aug_30_2023.pdf` | HMI 規格本文 | **zip 容器，137 張 JPEG 頁圖，無文字層** | 9,528,811 B |

> 檔名以 repo 內複本之實際檔名為準；本表之名可能因附件傳遞而經正規化。
> T1 須記實際檔名入台帳。#3–#5 之衍生本身分與 #6 之圖檔身分為
> **已裁認事實**（R-SU4(a)、R-SU6），非待處置異常。

### 3.2 037 工作簿結構

分頁：`封面` / `ChangeHistory 修訂履歷` / `Product Document 記錄封面頁` /
`AnalysisReport_FULL` / `Instructions` / `下拉選單設定處`。

⚠ **資料分頁名為 `AnalysisReport_FULL`（無空格），非 `Analysis Report`** ——
`scripts/intake.py` 之 `SHEET_SIGNATURES`（`"Analysis Report" in names`）
**預期不命中**。若 T2 實測確認不命中：依 Display R-DM5 之同型處置，
於 `feature.yaml` 設 `intake.kind_overrides` 與
`paths_meta.a03_sheet = "AnalysisReport_FULL"`，**不得改腳本使其命中**。

封面：Project Name `NR1L`、Reviewer `Arunraj`、Author `V M Bhuvanesh`、
文件號 `FM-WI-FSM-037-A03`。

**表頭列 = 7；資料列 = 8 起。18 欄版面**（無 `HMI Source ID`、無 `FROP`
—— 與 vehicle_category 之 20 欄 rev D 不同版）。欄序：
`SWE-Requirement ID` / `Source Requirement ID` / `Requirement Title` /
`Requirement Description` / `Release Version` / `Categorization` /
`Sub Categorization` / `Feasibility` / `Description…Feasibility` /
`Impact` / `Description…Impact` / `Risk Factor` / `Description…Risk` /
`Reusable` / `Description…Reusable` / `Priority` /
`Verification Criteria` / `Verification Method`。

### 3.3 需求母體

| 項目 | 數 |
|---|---|
| 資料列 | **383**（`SWE1-FOTA-001` ~ `383`，連號、無重號） |
| `Functional Requirement` | 307 |
| `Non Functional Requirement` | 4（281–284） |
| `Heading` | 45 |
| `Information` | 25 |
| `Categorization` 空白 | 1（296，title `Regular Updates`） |
| `Out of scope` | 1（335，title 空） |
| **驗證母體（R-SU3）** | **311** |

### 3.4 欄位分布（383 列）

| 欄 | 值分布 |
|---|---|
| `Sub Categorization` | `Service` 223、`HMI` 87、空白 73 |
| `Priority` | `High` 271、`Medium` 34、`Low` 6、空白 72 |
| `Source Requirement ID` | `SYS-RA-FOTA-{n}`，非空 373、值域 1–526、unique 364、9 個重複引用（R-SU5） |
| `Verification Method`（抽樣） | `Unit Test / Integration Test / System Test` |

> 本 037 之 `Priority` 欄**有值**（271H/34M/6L）—— 與 vehicle_category
> （全 `\xa0`）不同。Priority → P0–P3 之對應屬 Phase 3/4，本包不裁。

### 3.5 CFTS_57 Reflash（錨點池）

- TOC 式行 174；ObjectID `{7位}` 出現 174 次、**unique 87**
- 頂層結構：1 Reflash / 2 Common Reflash Requirements /
  3 Media Reflash Requirements / 4 FOTA Reflash Requirements
  （4.1 ~ 4.13，含 4.6 OTA download via Wi-Fi、4.10 Session Flows、
  4.11 UX/HMI、4.12 Interrupt Handling、4.13 OMA-DM MO Support）

### 3.6 SYS1 export（HMI 規格索引）

- `Basic Report` 資料列 **120**（列 2–121）；欄：`ID`（`NRL-######`）/
  `Space / Document` / `Outline Number` / `Description` /
  `SYSRE_HMI_Source ID` / `Type` / `_polarion`
- 頂層章 **28**（1 ~ 28）；深度分布：1 層 28、2 層 89、3 層 3
- `SYSRE_HMI_Source ID` 形態即 R-SU4(b) 之錨 token 原值

---

## 四、Recon 觀察（記錄即止 —— Q5 裁定不立案）

### 4.1 量測條件

- 037 全數字：openpyxl `read_only=True, data_only=True`，
  `AnalysisReport_FULL` 列 8 起、col1 非空者計入
- USB 掃描：title/desc 小寫子字串 `usb`
- SYSAD 分配表：§分配系統需求 表格列之 `SYS-RA-FOTA-\d+` 正則抽取
- 衍生文字檔：UTF-8 讀入、逐行

### 4.2 「via USB」於 037 內之分布

- title/desc 含 `usb` 者 **26 列**；核心為 Media Reflash 區
  （078–084：TBM via USB 2.0、更新來源仲裁）與
  Local Deployment（076–077）
- description 含 `USB Update Service` 者 20 列，多為安裝條件／HMI
  共用需求（145–183 區）

### 4.3 SYSAD 之系統分解

四線：**Software Update via USB**（13 態狀態機：IdleState →
ConsistencyCheck → UserInteraction → UpdateFileCopy → Unpacking →
Installation{MCPU,SXM,Tuner,Gnss,VCPU} → UpdateFinished → WhatsNew，
.swpkg 三層解包）／ FOTA ／ ROV FOTA ／ TBM FOTA。

### 4.4 037 之 Priority 空白 72 列

與 `Sub Categorization` 空白 73 列高度重合 —— 皆為 Heading /
Information 類非需求列（T4 一併驗證重合度）。

### 4.5 SYSAD 分配表與 037 之錯位（三項觀察，Q5 裁定不立 A、不發 DR）

1. SYSAD 將 `SYS-RA-FOTA-001~014` 分配給 `SYSAD_USB_Update_Service`，
   但 037 引用該區間之列（002–016 區）全為 Wi-Fi/FOTA 內容。
2. SYSAD 分配 `SYS-RA-FOTA-453~474` 給 TBM_Update_Service，
   037 引用該區間 **0 列**（ROV 區 475–504 則有 24 列引用）。
3. SYSAD 之 HMI 分配 44 個 SYS-RA id 中 11 個不在 037
   （148, 175, 176, 177, 221, 328, 360, 382, 383, 390, 391）。

**處置**：範圍以 037 為準（R-SU3），SYSAD 分配表不作範圍依據、
不作錨點依據；本三項後續不再重提。

---

## 五、執行層任務

| # | 任務 | Tier |
|---|---|---|
| T0 | `python scripts/new_feature.py SW_Update --adopt-existing` 建立骨架（本包已先落於 `docs/handoff/`，adopt 模式不覆寫）。回報實際建出之目錄名與 `kept existing` 清單 —— **若目錄名非 `sw_update`，停並回報** | 1 |
| T0b | 字串更正（vehicle_category 10.2 同法，附 diff）：(1) 骨架各 md 內 `SW_Update` → `SW Update`；(2) 標記前綴 `SW` → `SU`（`A-SW` → `A-SU` 等）；(3) profile 名 → `FW036_R1L_SWUpdate_Profile.md`（CamelCase）。`feature.yaml` 由 T9 直接填實，不入本項替換。完畢後 `grep -rn "SW_Update" --include="*.md" features/sw_update/ --exclude-dir=handoff` 與 `grep -rn "A-SW\|R-SW\|DR-SW" features/sw_update/ --exclude-dir=handoff` 命中數皆須為 0（本檔之引文不在規制內） | 1 |
| T1 | 六份素材置入 `_intake/SW_Update/`，記實際檔名 + SHA256 + mtime 入素材台帳；複製入 `features/sw_update/inputs/`，**搬入前後各記一次 SHA256**。來源目錄唯讀。**素材若尚未落於本機，停並向 Pei 取得**（檔案搬動屬 Pei） | 1 |
| T2 | 照跑 `scripts/intake.py`，如實回報分類結果。**預期 037 不命中 `swra_report`**（分頁名 `AnalysisReport_FULL` 無空格，見 §三 3.2）；不命中即依 R-DM5 同型於 `feature.yaml` 設 `intake.kind_overrides` + `paths_meta.a03_sheet`，**不得改腳本** | 1 |
| T3 | 跑 `scripts/recon.py` → `RECON.md` / `DECISIONS.md` / `recon.json`。036 母本欄位以**表頭字串實測**回報命中數（n/n），不得沿用他 feature 之欄位字母；037 之表頭列 = 7、18 欄版面一併實測確認 | 1 |
| T4 | 對 repo 內複本**重測**本包 §三、§四之全部數字（383 / 307 / 4 / 45 / 25 / 1+1 / 311；223 / 87 / 73；271 / 34 / 6 / 72；373 / 364 / 9-dup 名單；26 USB 列；CFTS_57 之 174 / 87；SYS1 之 120 / 28 / 深度 28-89-3；§四 4.4 之重合度），與本包逐項比對，逐項標 `=` 或 `≠`。**不符即停並回報** | 1 |
| T5 | 以正則 `PU\d+` 掃 037 全欄，列出全部彈窗 id 引用（含列號）；對 `forms/Pop Up List HMI R1 (26PI).xlsx` 查存在性。**查得與否皆如實回報**，查無不得代以語意相近者 | 1 |
| T6 | 對 SYS1 `Basic Report` 之 `SYSRE_HMI_Source ID` 120 值做唯一性與形態檢查（前綴逐字一致性、章節號與 `Outline Number` 欄互證），回報形態外者 | 1 |
| T7 | 建立 `DATA_REQUESTS.md` 台帳 —— **本包 0 筆**（Q5 裁定）。standing rule 照常生效：日後新外部引用之發現仍須登記 | 1 |
| T8 | 建立 `ANOMALIES.md` 台帳 —— **本包 0 筆**（Q5 裁定；§四 4.5 之三項為觀察記錄，不立案） | 1 |
| T9 | 依 §六草案填 `feature.yaml`。`reference:` 綁定判準照 R-G15 / R-DM37：其變動會使既有產出失效者一律綁定 | 1 |

**不在本輪範圍**：`framework.md`（Phase 3）、錨定協定（Phase 2/3）、
profile 檔、任何 TC、任何寫回、任何 git 操作。

**逸出即停**：遇 FO §0 之六項觸發任一者，停並填 `DECISIONS.md` 或
`ANOMALIES.md`（證據 + 提案處置），續作不受影響之項目。

---

## 六、`feature.yaml` 草案

> 路徑之 glob 以實際檔名為準（T1 記錄之名）。`paths:` 基準為本 feature
> 目錄（供腳本開檔）；`reference:` 基準為 repo 根（供綁定比對）。
> 素材一律複製入 `inputs/`（R-VC10 之教訓：`paths:` 填 forms/ 相對路徑
> 會使 recon.py 中止）。

```yaml
feature: "SW Update"
test_group: "SW Update"

paths:
  workbook: "inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx"   # R-G1 母本
  a03_report: "inputs/SoftwareUpdate_FMWIFSM037A03_STLA_Report_SWRA.xlsx"
  sys1_export: "inputs/SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_Aug_30_2023.xlsx"
  spec_pdf: "inputs/Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_Aug_30_2023.pdf"   # R-SU6：zip 容器 137 JPEG，無文字層
  cfts57_report: "inputs/R1LR_Atl-H_25PI4_5_Dec_Release-xOTA_CFTS_57_Reflash_20251202-2111.docx"   # R-SU4(a)：UTF-8 純文字衍生本
  sysad: "inputs/SYS3_CFTS_057_FM-WI-FSM-011-A01_系統架構設計_System_Architectural_Design_SYSAD_V03_06042026_V3_0.docx"
  vf747: "inputs/Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx"
  popup_list: "inputs/Pop Up List HMI R1 (26PI).xlsx"    # T5 之查核來源

# §三 3.2：資料分頁名 `AnalysisReport_FULL`（無空格），intake sniffer
# 預期不命中。T2 實測確認後填入：
# intake:
#   kind_overrides: { ... }
# paths_meta:
#   a03_sheet: "AnalysisReport_FULL"

spec_mode: "?"                    # 由執行層依 FO §3 實測後填入（R-SU4 不逕定）
spec_reference_template: null     # R-SU4：查得（CFTS ObjectID／SYS1 欄原值），非構造

workbook:
  sheet: "?"          # 實測自母本（T3），不得沿用他 feature 之值
  header_row: 9       # 實測覆核
  columns: {}         # T3 表頭實測結果填入

done_region:
  detection: "author"
  author_value: null            # R-SU2：workbook_state = BLANK，本節不生效
  invariant: "content_hash"

write_back:
  author_value: "PeiPYHsu"
  tc_ref_id_value: "NEW"
  fill_test_group_set: true     # R-SU2(a)：BLANK -> FILL

lint:
  design_method_source: "dropdown_sheet"
  popup_ids: []                 # T5 查得後填入
  extra_rules: []

# 只宣告 recon.py run_assertions() 真正實作之鍵（R-VC9 之教訓：
# 宣告不被讀取之鍵比不宣告更糟）。
# ⚠ 揭露義務：R-SU3 之母體 311 在對應 assertion 落地前僅靠 T4 重測
# 與上繳包交叉檢查守護，非機器保證，此事實須逐包揭露。
recon_assertions:
  functional_requirement_count: 307

reference:
  a03_report:
    file: "features/sw_update/inputs/SoftwareUpdate_FMWIFSM037A03_STLA_Report_SWRA.xlsx"
    sha256: "TBD-T1"
  sys1_export:
    file: "features/sw_update/inputs/SYS1_HMI_Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_Aug_30_2023.xlsx"
    sha256: "TBD-T1"
  spec_pdf:
    file: "features/sw_update/inputs/Software_Updates_FOTA_HMI_Logic_and_Flow_R1_SR24_post_2A_Aug_30_2023.pdf"
    sha256: "TBD-T1"
  cfts57_report:
    file: "features/sw_update/inputs/R1LR_Atl-H_25PI4_5_Dec_Release-xOTA_CFTS_57_Reflash_20251202-2111.docx"
    sha256: "TBD-T1"
  sysad:
    file: "features/sw_update/inputs/SYS3_CFTS_057_FM-WI-FSM-011-A01_系統架構設計_System_Architectural_Design_SYSAD_V03_06042026_V3_0.docx"
    sha256: "TBD-T1"
  vf747:
    file: "features/sw_update/inputs/Entire_Vehicle_FOTA_Management_VF747_V1_R3.docx"
    sha256: "TBD-T1"
  workbook_master:
    file: "forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx"
    sha256: "6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2"   # T9 對 forms/ 原件重測確認
  popup_list:
    file: "forms/Pop Up List HMI R1 (26PI).xlsx"
    sha256: "TBD-T9（對 forms/ 原件實測）"

# DBC / PROXI / LID：037 是否引用 CAN 訊號、PROXI 參數、VF 文件
# 由 T4 順帶掃描回報（`\$?[A-Z_]+\.[A-Za-z]+`、`PROXI`、`VF\d+`），
# 綁定與否依掃描結果於 T9 決定並記其依據 —— 少綁須是裁定，不是遺漏。
```

---

## 七、上繳包要求

`features/sw_update/docs/upstream/01_intake_recon.md` 須含：

1. **T0–T9 逐項結果**，含實際指令與其原始輸出（不得只寫「已完成」）
2. **R-SU1 ~ R-SU6 之逐條抄錄核對結果**（抄入位置 + 逐條字面一致確認）
3. **T4 之比對表**：本包 §三、§四之每個數字 vs repo 內實測值，逐項標 `=` 或 `≠`
4. **素材台帳**：實際檔名 + 絕對路徑 + SHA256（搬入前／後）+ mtime
5. **未結 DR 清單**（本包應為空表）
6. **獨立自評**：本包有無「應驗而未驗」之項（每包必答）
7. **量測條件揭露**（R-G8）：T4 / T5 / T6 各項所用之方法、工具與偽陽性風險
