# ANOMALIES — FW036 Popup HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-POPnn]`（與 `R-POP`／`DR-POP` 同綴；`new_feature.py`
之骨架寫 `A-POnn`，本 feature 不採，見 A-POP4）。PENDING entries block
their batch until a Pei ruling lands; RESOLVED entries record the ruling
verbatim. Registration is Tier 1 (record + propose); disposition is Tier 2.

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-POP1 | `extract_source.py` 之 `safe_name()` 剝前導底線，`_polarion` 與 `Polarion` 撞名；大小寫不敏感檔案系統下後寫者靜默覆蓋前者，§F-6 自驗結構上測不到 | **RESOLVED（R-POP9 追認；傳染性掃描已於下放包 02 §六-3 執行，見本檔 A-POP1 §四）** | — |
| A-POP2 | DR-POP1／DR-POP2 之標的文件已在 repo `forms/` 內；下放包 01 §四-1「該文件不在素材內」與 repo 現況不符 | **RESOLVED（甲半 R-POP6 納入、DR-POP1 結案；乙半 R-POP7 不納入、DR-POP2 續開）** | — |
| A-POP3 | 5 個 leaf 之引用一律 `_5.6`；`_5.5` 僅由 Heading `SWE1-POP-001`（標 No TC）引用 —— 下放包 §五 Layer 3「PC1 = spec 5.5～5.6」之 5.5 半無 leaf 依託 | **RESOLVED（R-POP8：-002-02 之 spec_reference 併列 `_5.5`＋`_5.6`）** | — |
| A-POP4 | `lint_docs036.py` 之序號跳號檢查僅認 `DR-PW`／`A-PW`／`A-PM` 三前綴，本 feature 之 `DR-POP`／`A-POP` 不受檢；骨架之 `A-POnn` 綴亦與裁決系列不一致 | **RESOLVED（R-POP10：改前綴自動抽取；下放包 02 §六-2 落實，迴歸兩向實跑）** | — |
| A-POP5 | 036 母本 design_method 欄（`R10:R1411`）之下拉為 **x14 擴充**，`openpyxl` 讀不到且 `save()` 會靜默刪除 —— 上繳包 01 §五-3 之「R 欄無 data validation」為誤述 | **RESOLVED（本包更正＋寫入路徑改 `xlsx_surgical`；輸出實測 x14 存活）** | Tier 1 |
| A-POP6 | R-POP10 之前綴自動抽取使既有台帳浮現 8 個 feature 之新命中；其中兩類為誤判（recap 表之 id 被判「編號重複」、`S` 為假前綴），四個 feature 抽不到任何前綴 | **RESOLVED（R-POP16：甲不代改入各 feature BACKLOG；乙採提案 1+2，首個表格為抽取界；丙登 G-D 並須明示 no series detected）** | Tier 2（判準精修範圍）|
| A-POP7 | `SWE1-POP-002-02` 之 device 軸（physical hard button／UI button）為真軸，但 Pop Up List 無「同一實體鍵開啟並關閉」之實例 —— 拆軸會有一分支無實例可填 | **RESOLVED（R-POP12：不拆，理由改採「規格側無此分支」；不開 DR；語料 reasoning 須改寫）** | Tier 2（拆軸與 RD-1）|
| A-POP8 | `SWE1-POP-002-05` 之 `search keyboard` 於 Pop Up List **查無對應列**（三 sheet 全欄實測），觸發下放包 02 §八 升級條件 —— 該 leaf 本包未生成 TC | **RESOLVED（R-POP14：採乙案改良，照 GP4-4 規格原句生成、不引 PU；另開 DR-POP4）** | Tier 2／3（改判例證或向上游索件）|
| A-POP9 | 下放包 02 之上繳回報與 repo 台帳於四點不符：(1) anomaly 編號錯置（回報之 A-POP5／6／7／8 ≠ 台帳之 A-POP5／6／7／8）；(2) 台帳 A-POP5（x14 下拉靜默刪除）回報未提；(3) 傳染性掃描結論相反（回報稱 intake.py 有同缺陷，台帳 A-POP1 §四 稱 `scripts/` D1∧D2 僅 extract_source 一支）；(4) TC ID 前綴回報稱 `PROJ-POP-*`，語料實為 `newR1L-POP-*` | **RESOLVED（R-POP17：上繳摘要改 live 產；`ledger_xref.py` 增包內引用對照檢。其 (4) 另由 R-POP13 處分 —— TC ID 前綴定值）** | Tier 2 |
| A-POP10 | R-POP16 乙之「首個表格」判準使數個 feature 之台帳**整本脫檢** —— 其登記主表不在檔內第一張表（sxm／audio_mgmt／projection），或被空行切成多段（power 之 A-PW）。放寬跨表誤傷的同時，也丟掉了真陽性 | **PENDING** | Tier 2（判準之辨識方式）|
| A-POP11 | R-POP16 甲所列之 sxm `A-SX18`／`A-SX19` **為假陽性** —— 該二號以 `## [A-SXnn]` 標題式登記於 `features/sxm/ANOMALIES.md`，實存；A-POP6 甲類係抽取器只看表格首格所致。§十 升級條件命中：未代改、未寫入 sxm BACKLOG，只回報 | **PENDING** | Tier 2 |

---

## A-POP1 —— 抽取檔名撞名之靜默覆蓋 —— **RESOLVED（待覆核）**

**登記時點**：下放包 01 §六-3 落 `sources/` 之後、§六-4 scaffold 之前。
**觸發**：FO §0 停下條款之「抽取機制本身未經驗證」面（R-G7-1：對照向
亦用於驗證定位／抽取機制本身）。

### 一、事實

`SYS1_..._(February_2_2023).xlsx` 有 3 個 sheet（`Basic Report`、
`Polarion`、`_polarion`）。首跑 `extract_source.py` 後
`sources/extracted/core_hmi_lf_sys1/` 只有 **2 份 tsv**，且
`Polarion.tsv` 之首列 sheet 欄逐字為 `_polarion`（181 列），
`Polarion` sheet 之 15 列**已不存在**。

成因：`safe_name()` 末句 `out.strip("._")` 兩端皆剝，
`_polarion` → `polarion`；macOS APFS 大小寫不敏感，
寫入 `polarion.tsv` 即覆蓋既存之 `Polarion.tsv`（檔名保留先建者之大小寫，
故 `ls` 上看不出異狀）。

**§F-6 自驗為何測不到**：其比對對象是「剛寫出的那份 tsv 回讀之量」與
「read_only 實測之量」。被覆蓋的是**前一個 sheet 的檔**，後一個 sheet
自己的兩個量完全相符 —— 這個自驗在設計上就看不到跨 sheet 的覆蓋。
腳本 docstring 明言「不重讀原檔，那只證明 openpyxl 兩次讀出同一份東西」，
其推論正確，但漏了「寫出物之集合是否與 sheet 之集合等勢」這一維。

### 二、量測條件揭露（R-G8）

- sheet 集合：`openpyxl.load_workbook(read_only=True).sheetnames`，3 個
- 抽取物集合：`ls -b sources/extracted/core_hmi_lf_sys1/*.tsv`，修正前 2、修正後 3
- 身分判定：各 tsv 首列 `# source_sha256\t<sha>\t sheet\t<name>` 之 sheet 欄逐字比對
- 檔案系統敏感性：macOS APFS（本機預設不敏感）——**此缺陷在敏感檔案系統上
  不會顯現為覆蓋，而會顯現為兩個檔**，故非全平台可重現

### 三、處分（Tier 1，執行層自為）

1. `safe_name()` 改為只剝**尾端** `._`；前導 `.` 另以 `sheet_` 前綴中和
   （`..`／`../../etc/passwd` 之逃逸防護不變，既有測試仍綠）
2. `extract_xlsx()` 增撞名守衛：同一 doc 內以 `casefold()` 比對抽取檔名，
   撞名即 `ExtractionMismatch`（**停**），不再靜默覆蓋
3. 迴歸測試兩支入 `tests/test_extract_source.py`：
   `test_前導底線不被剝掉`、`test_撞名之_sheet_停下而非靜默覆蓋`
4. `sources/extracted/core_hmi_lf_sys1/` 刪重抽，3 份齊備並逐份驗首列 sheet 欄

**影響範圍**：`sources/extracted/` 於本包之前為空（`MANIFEST.tsv` 僅表頭），
故無其他 feature 之既有抽取物受此缺陷影響 —— 已以 `find sources -type f`
實測確認本包三件為 `sources/` 之全部內容。

**追認（R-POP9，Pei 2026-08-27）**：修正照案追認，另派傳染性掃描入 02 包。

### 四、傳染性掃描（R-POP9 backlog，下放包 02 §六-3）—— 只掃只報

A-POP1 之資料遺失需**兩個條件同時成立**，缺一不可，故掃描分兩支獨立偵測器：

- **D1**：`(str) -> str` 且體內有**帶字元集**之 `strip('…')`／`lstrip('…')`
  或逐字元保留集 —— 即「名稱→檔名之映射非單射」。
  **裸 `.strip()` 不算**：去空白不會讓兩個有意義的相異名字撞在一起。
- **D2**：`for` 迴圈體內對「以迴圈變數推導之路徑」`write_text`／`write_bytes`，
  且該函式無撞名守衛（`casefold`／`.lower()` 比對，或 `seen`／`taken` 集合）。

**首版判準過鬆已作廢並重寫**：初版以「`.strip(` 出現且無 `rstrip`」判 D1，
於 `scripts/` 得 40 個 DEFECT —— 絕大多數是裸 `.strip()` 之假陽性。
**一個判準錯的掃描會給出很有信心的錯答案**（G-K 之命題）。收緊後結果如下。

| 範圍 | 檔數 | D1 | D2 | **D1 ∧ D2（A-POP1 同型）** |
|---|---|---|---|---|
| `scripts/`（R-POP9 明定範圍）| 24 | 1（`extract_source.safe_name`）| 2 | **1**（`extract_source.py`，**已修**）|
| `backend/` ＋ `features/*/scripts/`（範圍外，順帶）| 470 | 3 | 185 | **0** |

- `scripts/` 之 D2 另一支 `new_feature.scaffold`：檔名來自**字面常數字典**，
  無 sanitizer 參與；且其守衛為 `if target.exists(): skipped.append(...)`
  （人工複核 `scripts/new_feature.py:182-187`），不會覆蓋。判無缺陷。
- 範圍外之 D1 三支：`features/power/scripts/g113_buckets.py`、
  `features/power/scripts/or_branch_coverage.py`、
  `features/time_management/scripts/tm_rulings.py` —— 皆**不**在同檔迴圈寫多檔，
  半具備而未成災。**登記於此供日後該 feature 動到寫檔路徑時回看**，本包不改。
- 範圍外之 D2 185 支：無 sanitizer 參與，其檔名直接來自迴圈變數之字面值，
  非「非單射映射」之受害者。**本掃描不對它們宣稱任何事** —— 它們可能有別的
  問題，但不是 A-POP1 同型。
- **掃描器本身之侷限（G-D）**：D2 僅認 `write_text`／`write_bytes`，
  **不認 `open(..., "w")`／`json.dump`／`shutil.copy`／`DataFrame.to_csv`**；
  D1 僅認 `(str) -> str` 且**有型別註記**者。兩者皆為漏報方向。
  掃描器落 `scratchpad/sanitizer_scan.py`（非交付物，不入 repo）。

---

## A-POP2 —— DR-POP1／DR-POP2 之標的文件已在 repo 內 —— **RESOLVED（R-POP6／R-POP7）**

**登記時點**：下放包 01 §六-6 起建工作簿時（在 `forms/` 取 R-G1 母本）。
**觸發**：FO §0 逸出條款 —— 裁決所據之事實在執行層重測後不成立。

### 一、事實

`forms/` 內實測存在兩件（`ls -la` + `shasum -a 256`，2026-08-27）：

| 檔 | sha256 | bytes | mtime |
|---|---|---|---|
| `Pop Up List HMI R1 (26PI).xlsx` | `ff47b7be63e5824cafe35deda9f9ddd0a63f6ea458169ef73689a1c559ea13ea` | 2,951,835 | 2026-08-25 13:51 |
| `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `dc078763c67b52388eba8edf5c461515cfd2d92dd3a78dba0ce4e365e43ccc2f` | 1,035,049 | 2026-08-25 13:50 |

唯讀探測（openpyxl `read_only=True`／`pdfinfo`＋`pdftotext`）：

- `Pop Up List HMI R1 (26PI).xlsx`：sheet 3（`Main` A1:Q1344／`Templates`
  A1:E34／`Drop Down Fields` A1:H73）。`Main` **A1 逐字 = `SR24 Post 2A CR25802`**
  —— 與本 feature 之規格基線（`R1 SR24 Post 2A (February 2 2023)`）同版系。
  r2 表頭逐字含 **`Timeout (sec)`**（C 欄）、`Exit Conditions`（D）、
  `Category`（F）、`String/Popup Message`（G）、`Stored in Notifications Inbox`（K）。
  r4 起為 `PU0001`… 之 popup 逐條列。
- `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`：真 PDF，
  PowerPoint 2016 產出，**有文字層**（`pdftotext` 非空白字元 7,820）。
  **惟其基線為 `SR24 1A (May 3 2021)`，早於本 feature 之 `SR24 Post 2A
  (February 2 2023)`** —— 版次是否可用於本 feature 未經裁定。

### 二、與下放包之出入

下放包 01 §四-1 稱「該文件不在素材內」、§四-2／§四-3 稱例外清單與
touch-outside 啟用清單「無來源」，並據此令 `-002-01`／`-002-05`／`-002-03`
落 `PENDING: DR-POP1`。上表顯示 **DR-POP1 之標的（timeout 值、popup 逐條
屬性）在 repo 內即有一個具名候選**。DR-POP2 之標的亦有候選，惟版次較舊。

前例：`A-SU3`（sw_update）已以 `forms/Pop Up List HMI R1 (26PI).xlsx`
查驗 `PU971`／`PU0971` —— **同一檔在他 feature 已被當作可查驗之來源使用**。

### 三、執行層不自為之處（觸點）

「何者在／不在驗證範圍」與「素材補入」屬 Pei（Operating Charter §觸點）。
執行層**未**以該兩件填任何 TC 欄位、**未**改 DR-POP1／DR-POP2 之狀態、
**未**將其寫入 `feature.yaml`（`paths.popup_list` 仍為 `null`）。

### 四、提案（供 Pei 裁定，非自裁）

1. `Pop Up List HMI R1 (26PI).xlsx` 是否即 DR-POP1 之標的 —— 若是，
   DR-POP1 改「已到齊」，`paths.popup_list` 指向之，
   `-002-01` 之 timeout 值改由該檔逐條查得（不再落 PENDING）
2. Priority Matrix 之 `SR24 1A` 版次可否代 `SR24 Post 2A` —— 或維持 DR-POP2 未結
3. 兩件皆未登錄於 `forms/FORMS.md`（`grep -i "pop up" forms/FORMS.md` 命中 0），
   且 R-G2 之字面為「`forms/` 只保留 `…_SWQT_20260817_ext.xlsx`」。
   `forms/` 事實上已收 LID／DBC／PROXI／HMI Settings List 等共用參考件 ——
   其落點政策請一併裁示（是否移入 `sources/raw/` 並入 `MANIFEST.tsv`）

---

## A-POP3 —— `_5.5` 無 leaf 依託 —— **RESOLVED（R-POP8）**

**事實**（`sources/extracted/popup_037_v0_2/Analysis_Report.tsv`，逐列）：

| 037 列 | req_id | Categorization | C 欄（HMI Source ID）之章節號 |
|---|---|---|---|
| r8 | SWE1-POP-001 | Heading | `_5.5` |
| r9 | SWE1-POP-002 | Heading | `_5.6` |
| r10–r14 | SWE1-POP-002-01 ～ -05 | Functional Requirement | `_5.6`（五列皆是）|

`recon.py` 之 distinct-section 統計只取 leaf 列，故量得 **1**（非下放包
§六「預期數字」外之新量，該表未列此項）。

**後果**：下放包 §五 之 Layer 3 草案「`PC1` = spec 5.5～5.6（GP3／GP4 條族）」
之 5.5 半，其唯一入口是 `SWE1-POP-001`，而該列依 R-POP5 標
`No TC — Heading; duplicated of SWE1-POP-002-02`。亦即 **5.5 不會產出任何 TC**，
且 5 個 TC 之 `spec_reference` 一律為 `…_(February_2_2023)_5.6`（IN §10.7(b)
之一章節號一行規則下，本 feature 每列只會有一行）。

**5.5 與 5.6 之行為關係**（SYS1 export 逐字，`Basic_Report.tsv`）：

- 5.5（NRL-168287）＝ `GP3.) If a button opens a custom pop up (example:
  Status Bar Temperature/Comfort Controls Popup), pressing the button a
  second time will close the popup.`
- 5.6（NRL-168288）之第 2 途徑 ＝ `2) after pressing button that opened
  pop-up again (eg. Tracks popups)`

亦即 **5.5 與 5.6-2 為同一行為在規格內敘述兩次**，037 之
`SWE1-POP-001`（引 5.5）逐字自陳 `Duplicated feature of SWE1-POP-002-02`
（引 5.6）—— 037 的判定與規格原文對得上。**5.5 之行為並非未驗**，
只是其 TC 掛在 `-002-02` 且 `spec_reference` 記為 `_5.6`。

**提案**：Layer 3 之 `PC1` 敘述改為「spec 5.6（GP4 條族）」；5.5 之
「無 TC 直接引用」記入 `COVERAGE_GAPS.md` 作為**已知且已由 -002-02 涵蓋**
之項，而非未覆蓋缺口。若 Pei 認 spec_reference 應為 `_5.5` 與 `_5.6`
併列（IN §10.7(b) 一章節號一行、升冪），則 `-002-02` 一列須兩行 ——
此為錨定協定之變更，不自裁。

---

## A-POP4 —— 治理三簿之序號檢查未涵蓋本 feature 之前綴 —— **RESOLVED（R-POP10）**

`lint_docs036.py --gate --feature popup` 通過，但其 `check_series` 只認
`DR-PW`／`A-PW`／`A-PM` 三個硬寫前綴（`scripts/lint_docs036.py:179-181`），
故本 feature 之 `DR-POP{n}`／`A-POP{n}` **未受跳號檢查** —— 通過不代表已驗。
本包之 PASS 僅涵蓋台帳結構與表格列尾 `|` 兩項。

另 `new_feature.py` 之骨架以 `feature[:2].upper()` 產 `A-POnn`，
與 `R-POP`／`DR-POP` 不同綴。本 feature 之 ANOMALIES 一律用 `A-POP`；
骨架之字串未改（改之影響全 feature，非本包射程）。

**提案**：前綴由 `feature.yaml` 宣告，`lint_docs036.py` 讀之而非硬寫。
屬共用工具之政策性改動，不自裁。

---

## A-POP5 —— 母本 design_method 下拉為 x14 擴充 —— **RESOLVED**

**成因**：上繳包 01 §五-3 稱「design_method 欄（R）無 data validation」，
係以 `openpyxl` 之 `ws.data_validations` 量得（該屬性只讀 `<dataValidations>`，
不讀 `<extLst>` 內之 `<x14:dataValidation>`）。**該陳述為誤**。

**實測**（`zipfile` 直讀 `xl/worksheets/sheet6.xml`，正則抽 `x14:dataValidation`）：

| 項 | 值 |
|---|---|
| `<xm:sqref>` | `R10:R1411` |
| `<xm:f>` | `下拉選單!$A$1:$A$9` |
| openpyxl 載入時 | `UserWarning: Data Validation extension is not supported and will be removed` |

亦即 **`openpyxl` 之 `save()` 會刪掉整個工作簿唯一的設計方法下拉**，
且不報錯。與 `driver_distraction` 之 `feature.yaml` 所記（同一母本）同型。

**處分**：
1. 更正上繳包 01 §五-3 之 N3 記述
2. 本 feature 之工作簿寫入路徑一律 `backend/xlsx_surgical.surgical_save`
   （zip 層外科，逐 member 複製，只換被改之 sheet xml）—— 這不是偏好，
   是 R-G3 之所以存在的具體理由
3. 落檔後以 `zipfile` 直讀輸出檔複驗 x14 存活：
   `sandbox/pilot01/` 之輸出實測 `x14 DV 1，f=下拉選單!$A$1:$A$9，sqref=R10:R1411`，
   與來源逐字相同；`surgical_save` 之 `dv_counts` 亦報 `(3, 1)`

---

## A-POP6 —— R-POP10 新規使既有台帳浮現新命中 —— **RESOLVED（R-POP16）**

R-POP10 落實後（下放包 02 §六-2），對 19 個 feature 逐一實跑
`lint_docs036.py --feature <f>`。**`--feature power`（`gate_all.py` 之預設）
維持 PASS，故 gate 不因本次改動轉紅。** 其餘結果三分：

### 甲、真陽性（4 個 feature，5 筆）—— 非誤傷

| feature | 命中 | 佐證 |
|---|---|---|
| sxm | `A-SX18`／`A-SX19` 跳號 | 首格所見編號集為 `{15,16,17,20}`，18/19 確實不在 |
| audio_mgmt | `DR-AM7` 跳號 | 同法 |
| time_management | `A-TM2` 跳號 | 同法 |
| — | | 屬各該 feature 之台帳，本包**不代改** |

### 乙、假陽性（2 個 feature，2 筆）—— **誤傷，須修判準**

`編號重複` 之判定不分表：同一 id 出現在**回顧／狀態彙整表**時被判為重複。

- `power_moding`：`DR-PMH1` 於 `DATA_REQUESTS.md:15`（主表）與 `:150`
  （歷程彙整表）各一列
- `projection`：`A-PJ37` 於 `ANOMALIES.md:1436`（判準明細表）與 `:2182`
  （狀態表）各一列

**此非 R-POP10 新增之缺陷** —— `編號重複` 之邏輯在硬寫時代即如此，
只是從未套用到這兩個前綴。R-POP10 使其可見。

### 丙、抽取盲區（4 個 feature）—— G-D

`amfm`／`home`／`media`／`user_profiles` 抽得前綴集為**空**，
其 `ANOMALIES.md`／`DATA_REQUESTS.md` 之首格不是編號（版面不同）。
**PASS 在此不代表已驗**，代表沒東西受檢。被略過之首格數已逐檔印出
（如 `user_profiles` 99、`media` 64）。

另 `privacy` 抽得前綴 `S` —— 來源為 `ANOMALIES.md:194` 之
`| S10 | \`NA\`（Functional Safety）|`，是欄位值表而非系列登記簿。
**假前綴**，本次未產生 finding（單一編號無跳號可言），但會污染前綴集。

### 提案（不自裁）

1. `編號重複` 改為「同一表格內重複才判紅」，跨表重複降為 note
2. 前綴抽取限定於「該檔之**主登記表**」—— 主表之辨識方式待裁
   （表頭首欄字面？檔內首個表格？）
3. 丙類四個 feature 之台帳版面是否需統一，屬各該 feature 之事

---

## A-POP7 —— `-002-02` device 軸無 hard-button 實例 —— **RESOLVED（R-POP12）**

037 `SWE1-POP-002-02` 之 VC（S11）逐字：
`A specific pop-up is associated with a physical hard button or a specific
UI button on the screen.` —— 這是 IN §8.3 之 device 軸，兩分支皆為真。

**但 Pop Up List 只供得起一邊**：

| 分支 | 候選 | 判 |
|---|---|---|
| UI button | `PU0215`（Media）：`Exit Conditions = <Trks>`，`Description = Display when user is in Media screen and presses Track list button` | **成立** —— 開啟鍵與關閉鍵為同一鍵，來源明載 |
| physical hard button | `PU0229`（VR）：`Exit Conditions = Press of VR button again` | **不成立** —— 其 `Description = Displayed when the user asks to call for a number`，開啟者是語音請求而非該按鍵。指派給本分支是來源沒有承載之推定（IN §8.4.1）|

全表以 `again|second time|re-?press|toggle` 掃 `Exit Conditions`（不分大小寫）
命中 13 列，逐列人工判讀後，僅上述兩列與本 leaf 之命題有關。

**本包之處置**：**不拆軸**，`-002-02` 出一條 TC（`newR1L-POP-002`），
以 PU0215 為實例，procedure 與 ER 只說「開啟該 pop-up 的那個按鍵」，
不宣稱其實體型別。理由逐字入該 TC 之 `reasoning`。

**提案**：hard-button 分支之實例向上游索取（併入 RD-1），到件後補一條 TC，
同引 `SWE1-POP-002-02`（IN §8.2.2 一 leaf 多 TC）。

---

## A-POP8 —— `-002-05` 之 search keyboard 查無對應列 —— **RESOLVED（R-POP14）**

**觸發**：下放包 02 §六-5 令「`-002-05` 以 GP4 原文之 search keyboard 例為準，
自 (c) 類查對其 PU，**查無對應列即停下回報**」；§八 列為升級條件。

**量測條件與結果**（`forms/Pop Up List HMI R1 (26PI).xlsx`，
sha256 `ff47b7be63e5824c…`，三 sheet 全欄，不分大小寫子字串）：

| 量 | Main | Templates | Drop Down Fields |
|---|---|---|---|
| `search keyboard`（連續詞組）| **0** | 0 | 0 |
| `keyboard` | 22 | 0 | 0 |
| `search` | 44 | 0 | 0 |
| `qwerty` | 1 | 0 | 0 |
| `keypad` | 5 | 0 | 0 |
| **同列兼含 `keyboard` 與 `search` 之 PU 列** | **0** | — | — |

`keyboard` 之 PU 列 15 筆 —— **以 D／E／G 三欄判準與以 A–Q 全欄判準，
所得完全相同（15 = 15，差集空）**，故 §六-4 之三欄判準在此未失分。

**結論**：GP4-4 逐字所舉之 `search keyboard` 在納入之素材內無對應 popup。

**本包之處置**：`SWE1-POP-002-05` **不生成 TC**。
依 §六-5 明文「不改用他例」，未以 PU0022／PU0023（Media 字母鍵盤）或
PU0861（Camera App 全鍵盤）替代 —— 那需要先認定「該列即 search keyboard」，
正是被禁止的替代。依 IN §8.4.1 亦**不落 `PENDING:` 佔位、不造值**。

**提案（三選一，不自裁）**：
1. Pei 認 `PU0022`／`PU0023`（`ABC <Language Swap Buttons> <X>` ＋ 字母格）
   即 Media 之搜尋鍵盤 → 據以生成
2. 改以「multi-task popup」為判準（GP4-4 之命題本體，search keyboard 僅為 e.g.）
   → 需先裁何謂 multi-task，(c) 類之 Personal Account 八列（`b+c`，
   `Touch outside of popup, X, OK` ＋ keyboard）為候選
3. 向上游索 search keyboard 之 PU 具名（新 DR 或併入 RD-1）

---

## A-POP9 —— 上繳回報與 repo 台帳四點不符 —— **RESOLVED（R-POP17；(4) 另 R-POP13）**

**登記時點**：分析層覆核下放包 02 之上繳包時（2026-08-27），以 repo 台帳
逐點對照該回報所得。本節於下放包 03 由執行層補寫 —— R-POP17 明文
「詳 ANOMALIES.md」，而落檔時只寫了主表一列，明細節缺。
**該缺口係由本包新立之 `scripts/ledger_xref.py` 之 `ledger_shape` 檢
實測浮現，非人工複讀所得**（下放包 03 §五-3）。

### 一、四點（逐點）

| # | 回報所稱 | repo 台帳實況 | 型 |
|---|---|---|---|
| 1 | anomaly 編號錯置 —— 回報之 A-POP5／6／7／8 與台帳同號者所指非同一件事 | 台帳 A-POP5＝x14 下拉、A-POP6＝前綴新命中、A-POP7＝device 軸、A-POP8＝search keyboard | 轉抄摘要而未 live 查 |
| 2 | 未提 A-POP5 | 台帳 A-POP5（`openpyxl.save()` 靜默刪除 R10:R1411 之 x14 DV）為 Tier 1 已登記 | 漏報 |
| 3 | 傳染性掃描結論相反 —— 回報稱 `intake.py` 有同型缺陷 | 台帳 A-POP1 §四：`scripts/` 內 D1∧D2 僅 `extract_source.py` 一支（已修），範圍外 0 | 結論與實測相反 |
| 4 | TC ID 前綴稱 `PROJ-POP-*` | 語料 `generated/pilot_01.json` 實為 `newR1L-POP-*`；`feature.yaml` 之 `tc_id_format` 亦為 `newR1L-POP-{n:03d}` | 述值與語料不符 |

### 二、傳染

分析層落 R-POP12／13／14 時**轉抄了同一份摘要**，致三條條文各自掛錯
anomaly（R-POP12 掛 A-POP6、R-POP13 掛 A-POP8、R-POP14 掛 A-POP7），
落檔後更正為 A-POP7／A-POP9／A-POP8（下放包 03 §一）。
**同一根因跨層再現一次** —— 故 R-POP17 第 3 項明定分析層同受此規。

### 三、處分

R-POP17：(1) 上繳摘要一律自 repo 台帳 live 產；(2) `ledger_xref.py`
增包內引用對照檢；(3) 分析層同受。第 (4) 點另由 R-POP13 處分
（TC ID 前綴定值為 `NR1L-Popup-{NNN}`）。

### 四、下放包 03 §三第 1 項之連帶（執行層回報，未自為）

§三令「`feature.yaml` 之 `project` 模板殘值 `PROJ` → 正確值」。
**實測：`features/popup/feature.yaml` 內無 `project` 鍵，亦無 `PROJ`
字串**（全檔 grep 命中 0）。該項係承接本 anomaly 第 (4) 點之錯誤述值
而來 —— **修正對象本身不存在**。未自行造一個 `project` 鍵，
亦未改寫該指令，僅回報。詳上繳包 03 §一。

---

## A-POP10 —— 「首個表格」判準使數個 feature 之台帳整本脫檢 —— PENDING

**登記時點**：下放包 03 §五-1 落實 R-POP16 乙之後、迴歸兩向實跑之際。
**Tier 1（登記＋提案），不自裁** —— R-POP16 乙已明文把主表之辨識方式
定為「檔內首個表格」，改判準屬 Pei。

### 一、事實

R-POP16 乙之理由逐字為「首個表格為三簿體例之不變量」。
**實測不成立。** 逐檔取 `tables(text)[0]` 之首格，其是否為系列編號：

| feature | 檔 | 首個表格之表頭（前 3 欄） | 主表在第幾張 |
|---|---|---|---|
| popup | ANOMALIES | `A`／`內容`／`狀態` | **第 1 張**（成立）|
| power | DATA_REQUESTS | `#`／`主旨`／`Status` | 第 1 張（成立）|
| time_management | ANOMALIES | `#`／`標題`／`狀態` | 第 1 張（成立）|
| power_moding | DATA_REQUESTS | `#`／`主旨`／`Status` | 第 1 張（成立）|
| **sxm** | ANOMALIES | `token group`／`searched in`／`result` | 不在第 1 張（標題式登記）|
| **audio_mgmt** | ANOMALIES | `包內所記`／`inputs/ 實際` | 不在第 1 張（標題式登記）|
| **projection** | ANOMALIES | `family`／`count`／`leaf id 範圍` | 不在第 1 張 |
| **privacy** | ANOMALIES | `SHA256（前 8）`／`size`／`路徑` | 不在第 1 張 |
| **power** | ANOMALIES | 是登記表，**但被空行切成多段** | 第 1 段只含 `A-PW01`～`A-PW99` |

### 二、量測條件揭露（R-G8）

`python scripts/lint_docs036.py --feature <f>`，2026-08-27／28，
改判準前後各一跑，逐 feature 比對。新輸出之
「合系列形態但前綴不在主表而略過」即本條之量：
**sxm 4、audio_mgmt 7、projection 63、其餘 0**。

### 三、與 R-POP16 乙所令之迴歸兩向之關係

下放包 03 §五-1 所令之三項**皆達成**（`power_moding` DR-PMH1 紅→note、
`projection` A-PJ37 紅→消失、`privacy` 假前綴 `S` 消失），
注入向（主表內真重複仍 FAIL）亦達成。**本條不是那三項的反例**，
是那三項**沒有涵蓋到的第四件事**：判準同時也丟掉了真陽性。

### 四、何以不是靜默失效

改判準之同時，`main()` 依 R-POP16 丙加印
`no series detected …（G-D 盲區；PASS ≠ 已驗）`，且逐檔印出被丟棄之條數。
**受影響之四個 feature 現在會明說自己整本沒受檢**，不會與「真的沒跳號」
混同。故本條為**已知且看得見的覆蓋缺口**，非缺陷之隱藏。

### 五、提案（不自裁）

1. 主表改以「**首格為系列編號之列最多的那張表**」辨識，並將其
   **緊鄰之續段（被空行切開者）併入**——可同時解 power 之分段與
   sxm／audio_mgmt／projection 之非首張
2. 併認 `## [A-XXnn]` 標題式登記為主表之等價體例（sxm／audio_mgmt／
   driver_distraction 皆此式），此式在 `scripts/ledger_xref.py` 已認
3. 維持現狀（首個表格），把四個 feature 之覆蓋缺口留在 G-D 盲區清單上

---

## A-POP11 —— A-POP6 甲類之 sxm 兩筆為假陽性 —— PENDING

**登記時點**：下放包 03 §六（甲類清單寫入）執行時。
**§十 升級條件命中**：「甲類清單寫入時發現該 feature 之台帳與 popup 側
所見不符（勿代改，回報）」。**未代改，未寫入 sxm 之 BACKLOG。**

### 一、事實

下放包 03 §六令將四筆跳號逐筆寫入各該 feature 之 BACKLOG。
寫入前逐筆對該 feature 之台帳複驗（表格首格 ＋ `## [A-XXnn]` 標題式
兩式併計），結果：

| feature | 號 | 台帳實況 | 判 |
|---|---|---|---|
| sxm | `A-SX18` | `features/sxm/ANOMALIES.md:710` 逐字 ``## [A-SX18] `4872919` restates leaf 120's score-update branch and contradicts it — RESOLVED: 4872918 governs (2026-08-11)`` | **實存，假陽性** |
| sxm | `A-SX19` | `features/sxm/ANOMALIES.md:526` 逐字 `## [A-SX19] Five clauses carry a VR trigger path their 037 titles also declare — RESOLVED: …（2026-08-12）` | **實存，假陽性** |
| audio_mgmt | `DR-AM7` | `DATA_REQUESTS.md` 實存 1–6、8，缺 7；`RULINGS.md:238` 另有「A-AM07 ／ DR-AM7（分析層提出，Pei 裁發）」 | **真跳號**（已寫入其 BACKLOG）|
| time_management | `A-TM2` | `ANOMALIES.md` 全檔字串命中 0 | **真跳號**（已寫入其 BACKLOG）|

sxm 之 `A-SX` 實存編號集為 **1–30 連續**，無任何跳號。

### 二、成因

A-POP6 甲類係以 R-POP10 當時之抽取器所得，該抽取器只認**表格首格**；
sxm 以 `## [A-SXnn]` 標題登記，整本抽不到，於是「表格首格所見之 15／16／
17／20」被當成全集，18／19 被判跳號。**與 A-POP10 為同一根因之另一面**
（抽取器對登記體例的假設過窄），只是那裡表現為漏檢，這裡表現為誤報。

### 三、連帶：A-POP6 甲類之計數

A-POP6 §甲 之標題寫「**4 個 feature，5 筆**」，而其表列為 3 個 feature、
4 筆（sxm 2 ＋ audio_mgmt 1 ＋ time_management 1）。改判後真陽性為
**2 個 feature、2 筆**。三個數字互不相同，一併呈報，不自行改寫 A-POP6。

### 四、提案（不自裁）

1. A-POP6 甲類改列為 2 筆（audio_mgmt `DR-AM7`、time_management `A-TM2`），
   sxm 兩筆撤回並註明成因
2. 併同 A-POP10 提案 2 修抽取器（認標題式登記），則本型誤報自然消失
3. sxm 之 BACKLOG **本包未建**（無事可登）；若日後另有事由再建

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-POPnn]`.
