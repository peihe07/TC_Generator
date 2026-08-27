# ANOMALIES — FW036 Popup HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-POPnn]`（與 `R-POP`／`DR-POP` 同綴；`new_feature.py`
之骨架寫 `A-POnn`，本 feature 不採，見 A-POP4）。PENDING entries block
their batch until a Pei ruling lands; RESOLVED entries record the ruling
verbatim. Registration is Tier 1 (record + propose); disposition is Tier 2.

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-POP1 | `extract_source.py` 之 `safe_name()` 剝前導底線，`_polarion` 與 `Polarion` 撞名；大小寫不敏感檔案系統下後寫者靜默覆蓋前者，§F-6 自驗結構上測不到 | **RESOLVED（本包修正 + 迴歸測試；待覆核）** | Tier 1 |
| A-POP2 | DR-POP1／DR-POP2 之標的文件已在 repo `forms/` 內；下放包 01 §四-1「該文件不在素材內」與 repo 現況不符 | PENDING | Tier 3（素材納入與範圍屬 Pei）|
| A-POP3 | 5 個 leaf 之引用一律 `_5.6`；`_5.5` 僅由 Heading `SWE1-POP-001`（標 No TC）引用 —— 下放包 §五 Layer 3「PC1 = spec 5.5～5.6」之 5.5 半無 leaf 依託 | PENDING | Tier 2（Layer 3 定義）|
| A-POP4 | `lint_docs036.py` 之序號跳號檢查僅認 `DR-PW`／`A-PW`／`A-PM` 三前綴，本 feature 之 `DR-POP`／`A-POP` 不受檢；骨架之 `A-POnn` 綴亦與裁決系列不一致 | PENDING | Tier 2（前綴政策）|

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

**待覆核處**：修正動到**共用腳本**與**共用測試**，非 popup 專屬檔。
執行層認其為缺陷修正（Tier 1）而逕行；若 Pei 認共用工具之改動應先裁，
請於覆核時指正，執行層照辦。

---

## A-POP2 —— DR-POP1／DR-POP2 之標的文件已在 repo 內 —— PENDING

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

## A-POP3 —— `_5.5` 無 leaf 依託 —— PENDING

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

## A-POP4 —— 治理三簿之序號檢查未涵蓋本 feature 之前綴 —— PENDING

`lint_docs036.py --gate --feature popup` 通過，但其 `check_series` 只認
`DR-PW`／`A-PW`／`A-PM` 三個硬寫前綴（`scripts/lint_docs036.py:179-181`），
故本 feature 之 `DR-POP{n}`／`A-POP{n}` **未受跳號檢查** —— 通過不代表已驗。
本包之 PASS 僅涵蓋台帳結構與表格列尾 `|` 兩項。

另 `new_feature.py` 之骨架以 `feature[:2].upper()` 產 `A-POnn`，
與 `R-POP`／`DR-POP` 不同綴。本 feature 之 ANOMALIES 一律用 `A-POP`；
骨架之字串未改（改之影響全 feature，非本包射程）。

**提案**：前綴由 `feature.yaml` 宣告，`lint_docs036.py` 讀之而非硬寫。
屬共用工具之政策性改動，不自裁。

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-POPnn]`.
