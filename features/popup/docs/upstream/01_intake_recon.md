# 上繳包 01 — Popup Phase 0 intake ＋ Phase 1 RECON

日期：2026-08-27
對應下放包：`features/popup/docs/handoff/01_intake_recon.md`
執行層：Claude Code，repo `/Users/peihe/Work_Projects/TC_Generator`
分支：`feat/m1-stage7-scorecard`（**未執行任何 git 操作**，R-G5）

---

## 〇、一句話

下放包 §六 之六項作業全數完成，六項預期數字全數相符；
過程中開四件 anomaly（**A-POP2 使 DR-POP1／DR-POP2 之前提失效** ——
其標的文件在 repo `forms/` 內已存在），並修一件抽取工具之靜默資料遺失
（A-POP1）。四項待 Pei 裁定，作業面無停下。

---

## 一、預期數字對照（下放包 §六 表，相符者亦列）

| 項 | 預期 | 實測 | 判 | 量測條件（逐項揭露）|
|---|---|---|---|---|
| 037 Analysis Report 資料列 | 7 | **7** | 相符 | `Analysis_Report.tsv` r8–r14，逐列，A 欄 `.strip()` 後非空 |
| 其中 Functional Requirement leaf | 5 | **5** | 相符 | 同上母體，G 欄（`Categorization`）`.strip()` 後 == `Functional Requirement`，區分大小寫 |
| 其中 Heading | 2 | **2** | 相符 | 同上母體，G 欄 == `Heading` |
| SYS1 Basic Report 資料列 | 167 | **167** | 相符 | `Basic_Report.tsv` r2–r169（sheet 全域 A1:G169），A 欄非空 |
| SYS1 第 5 章項數 | 7 | **7** | 相符 | 同上母體，C 欄（`Outline Number`）`.strip()` 後 == `5` 或 `.startswith("5.")`，區分大小寫 |
| xlsx 指紋相符件數 | 2/2 | **2/2** | 相符 | 全檔 sha256（`shasum -a 256`），對 `_intake/Popup/` 投遞原檔實測 |

**指紋逐字**（`_intake/Popup/INTAKE.sha256`，本包新產）：

```
a9d0be2f13e4c44cc1f5086865d7f6bf0eb2a738a88640523ccf01737fca9c75  Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf
cdf0812fb9f74b710a723a73b72b141ade7f97a99f60d5059696f65477fb7eef  FM-WI-FSM-037-A03-N1L-SWE1-Popup-HMI-V0.2 STLA 報告.xlsx
d9a16eed89203e4c110fd4882f84124c4e6c86654ef3bc2cc6d99732456e2e11  SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023).xlsx
```

037 前 16 碼 `cdf0812fb9f74b71` = 下放包 §一-1 之值；
SYS1 前 16 碼 `d9a16eed89203e4c` = §一-2 之值。**兩件皆相符，未觸發 §八 升級**。
PDF 依 §一-3 警語**不比對**，僅登錄實測值 `a9d0be2f13e4c44c…`。

**投遞檔名與下放包所載之差異**（不阻斷，登錄）：

| # | 下放包所載（Project 附件名）| `_intake/Popup/` 實際 |
|---|---|---|
| 1 | `FMWIFSM037A03N1LSWE1PopupHMIV0_2_STLA_報告.xlsx` | `FM-WI-FSM-037-A03-N1L-SWE1-Popup-HMI-V0.2 STLA 報告.xlsx` |
| 2 | `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_February_2_2023.xlsx` | `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023).xlsx`（**有括號**）|
| 3 | `Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_February_2_2023.pdf` | `Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf`（**空白分隔**）|

下放包 §一-1 已預判「附件檔名之 `V0_2` 疑為上傳正規化」——
實測支持之，三件皆為底線／括號之正規化差異，sha 相符者其內容同一。

---

## 二、PDF 身分實測（下放包 §六-2，Tier 0）

| 量 | 值 | 工具與條件 |
|---|---|---|
| 檔型 | **真 PDF，version 1.5** | `file`（`PDF document, version 1.5`）|
| 頁數 | **21** | `pdfinfo` |
| 產生器 | `Power PDF Create`（Title `printhandler.ashx`，CreationDate 2023-02-02 23:24:28 CST）| `pdfinfo` |
| 頁面尺寸 | 612 × 792 pts (letter) | `pdfinfo` |
| 加密 | 否 | `pdfinfo` |
| **文字層** | **無** —— 非空白字元 **0** | `pdftotext -layout` 全檔輸出 21 bytes（每頁一個換頁字元），`tr -d '[:space:]' \| wc -c` = 0 |
| 文字層（第二工具）| **無** —— 21/21 頁 `extract_text()` 皆 0 行 0 字元 | `pdfplumber`，經 `extract_source.py` |
| 文字層（第三工具）| **無** —— `scanned (OCR path) — 0 chars via pymupdf` | `recon.py` 之 `survey_spec_text_layer` |

**三個獨立工具一致得 0**（R-G7-1：抽取機制本身亦須驗 —— 此處以三工具互為對照向）。

### spec_mode 定案

- **A 面成立**：SYS1 export 為文字權威（167 列 outline，第 5 章 7 項全有 `Description` 文字）
- **B 面不成立**：原檔無文字層，`pdftotext + section regex` 之管線在本 feature 無輸入
- **C 面成立**：PDF 為 21 張整頁掃描／渲染影像，圖面須以 render 取用

→ `feature.yaml` 之 `spec_mode` 定為 **`A+C`**（FO §3 明文「A feature may
combine modes (Home = A for text + C for figure pages)」）。

**與下放包之關係**：§一-3 稱「原檔是否具文字層未定 —— intake 時實測，
spec_mode 之 B／C 面據此定案」。本包定案為 **C，非 B**。
下放包 §一-3 另稱附件為 ZIP／21 JPEG —— 該判定針對 Project 附件副本，
與本機原檔為真 PDF 並不矛盾（附件管線之渲染產物，頁數 21 一致）。

---

## 三、`sources/` 落檔與 doc_id 定案（下放包 §六-3，R-G27）

doc_id 採下放包 §六-3 之 [DEFAULT] 提案**原字不動**：

| doc_id | raw 檔 | extracted 產物 |
|---|---|---|
| `popup_037_v0_2` | `FM-WI-FSM-037-A03-N1L-SWE1-Popup-HMI-V0.2 STLA 報告.xlsx` | 6 份 tsv（`封面`／`ChangeHistory 修訂履歷`／`Product Document 記錄封面頁`／`Analysis Report`／`Instructions`／`下拉選單設定處`）|
| `core_hmi_lf_sys1` | `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023).xlsx` | 3 份 tsv（`Basic Report`／`Polarion`／`_polarion`）|
| `core_hmi_lf_pdf` | `Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf` | 1 份 md（21 頁區塊，內容皆空 —— 無文字層之忠實記錄）|

- **原檔檔名逐字保留**（含空白與括號）—— 不改名。改名會使
  `MANIFEST.tsv` 之 `filename` 欄與 Pei 本機之檔失去對應
- `sources/MANIFEST.tsv`：由 `extract_source.py --refresh-manifest` 產
  doc_id／filename／sha256 三欄，`version`／`features`／`note` 三欄手填
- **落點無衝突**（下放包 §八 之升級條件三）：落檔前 `sources/raw`、
  `sources/extracted` 皆空目錄，`MANIFEST.tsv` 僅表頭一列 —— `find` 實測
- 三份 raw 之 sha256 於**複製後於落點重測**，與 `_intake/Popup/` 相同

### 抽取自驗（§F-6）

`extract_source.py` 對每個 sheet 比對「行數／非空儲存格數」，
9 個 sheet 全數相符，無 `ExtractionMismatch`。惟該自驗有結構性盲區 ——
見 **A-POP1**。

---

## 四、scaffold（下放包 §六-4）

`python3 scripts/new_feature.py Popup --root . --adopt-existing`

- 既存 `RULINGS.md`／`DATA_REQUESTS.md` **未被覆寫**（腳本回報
  `kept existing (not overwritten): DATA_REQUESTS.md, RULINGS.md`）
- 既存 `docs/handoff/01_intake_recon.md` 未受影響
- 新建：`RUNBOOK.md`／`ANOMALIES.md`／`DECISIONS.md`／`feature.yaml`／
  `PLAYBOOK.md`／`.gitignore`，目錄 `inputs data batches generated scripts docs`
- **`inputs/` 恆空**（R-G27／下放包 §六-4「不存原檔副本」）——
  `feature.yaml` 之 `paths.*` 以 `../../sources/raw/<doc_id>/*` 相對 glob 指向
- `feature.yaml` 另加 `sources:` 區塊記三個 doc_id。**現無任何腳本以 doc_id
  解析路徑**（`grep -n "doc_id" scripts/*.py` 除 `extract_source.py` 外命中 0）——
  故 doc_id 與 glob 並存，兩者所指為同一檔，本包已對三件逐一實測

---

## 五、RECON（下放包 §六-5）

`python3 scripts/recon.py --feature features/popup --root .`

### 5.1 assertions 4/4 PASS

```
PASS — leaf count == Functional Requirement rows: expected 5, measured 5
PASS — distinct spec sections after citation parse: expected 1, measured 1
PASS — citation stem is the ruled baseline, and only that
PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0
```

**首跑 FAIL 一項，成因為執行層自身之宣告錯誤，非素材不符** ——
執行層初填 `distinct_spec_sections: 2`（誤以全 7 列之 C 欄相異值計），
而 `recon.py` 之該統計**只取 leaf 列**。逐列實測後改為 `1` 並複跑。
逐列證據見 **A-POP3**；`_5.5` 之處置為待裁項。

### 5.2 workbook_state = **BLANK**

- done rows 0 / draft rows 0 / ambiguous rows 0
- authors present: (none)
- 版面判定：**Revision C**（有 `Estimated Test Time`）
- 欄位對映由 r9 表頭文字解析，15 欄全數解出，**與 `feature.yaml` 宣告 0 衝突**
  （`recon.py` 回報 `feature.yaml column conflicts: (none)`）

| 欄 | 字母 | | 欄 | 字母 |
|---|---|---|---|---|
| req_id | D | | tc_ref_id | O |
| test_group | G | | priority | P |
| test_set | H | | estimated_test_time | Q |
| test_item | I | | design_method | R |
| pre_conditions | J | | functional_safety | S |
| input_test_data | K | | author | AA |
| test_procedure | L | | remarks | AH |
| expected_result | M | | | |
| spec_reference | N | | | |

**注意**：`new_feature.py` 之 `feature.yaml` 模板預填 Revision A/B 之字母
（design_method Q／functional_safety R／author Z）。母本為 Revision C，
其後之欄整體右移一欄。本包已按實測改寫，模板未動（改之影響全 feature）。

### 5.3 下拉詞彙抽取

- `recon.py`：design-method vocabulary **9 strings**
- 母本 `下拉選單` sheet 之 A1:A9 逐字（A10／A11 為空）：

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

- **母本之 data validation 實測 3 條**（`openpyxl`，非 read_only）：
  `P10:Q1411` = `"P0,P1,P2,P3"`、`T10:Z1411` = `"0,1"`、
  `AF10:AF1411` = `"Pass, Fail, Pending,Block,NA"`。
  **design_method 欄（R）無 data validation** —— 其詞彙之強制力來自
  `feature.yaml` 之 `lint.design_method_source: dropdown_sheet`，
  非 Excel 本身。另 `P10:Q1411` 之範圍把 `Q`（Estimated Test Time，分鐘數）
  一併綁上 `P0~P3`，為母本既有之瑕疵，**本包不動母本**，登錄存查。

### 5.4 七列台帳（含 R-POP5 之 Heading 標記）

| 037 列 | req_id | Categorization | 引用章節 | TC 處置 |
|---|---|---|---|---|
| r8 | `SWE1-POP-001` | Heading | `_5.5` | **No TC** — Heading; duplicated of `SWE1-POP-002-02`（R-POP5，037 K8 逐字 `Duplicated feature of SWE1-POP-002-02`）|
| r9 | `SWE1-POP-002` | Heading | `_5.6` | **No TC** — Heading; refer to child IDs `-002-01..-05`（R-POP5）|
| r10 | `SWE1-POP-002-01` | Functional Requirement | `_5.6` | 生成（timeout 值落 `PENDING: DR-POP1`，惟見 A-POP2）|
| r11 | `SWE1-POP-002-02` | Functional Requirement | `_5.6` | 生成（device 軸拆分待評估，037 S11 逐字 `a physical hard button or a specific UI button`）|
| r12 | `SWE1-POP-002-03` | Functional Requirement | `_5.6` | 生成（受測 popup 選定繫 DR-POP1）|
| r13 | `SWE1-POP-002-04` | Functional Requirement | `_5.6` | 生成 |
| r14 | `SWE1-POP-002-05` | Functional Requirement | `_5.6` | 生成（例外實例繫 DR-POP1）|

- 覆蓋：037 leaves 5、headings 2；covered by done region 0；**regen targets 5**
- workbook req_ids ABSENT from 037（追溯孤兒）：done 0 / draft 0
- parent/child both-leaf duplications：無
- `data/recon_leaf_to_section.tsv` 已產（tracked；其 diff 即 export 位移之訊號）

### 5.5 `DECISIONS.md`

`recon.py` 因 `DECISIONS.md` 已存在而改寫 `DECISIONS.new.md`（A-TM15 路徑）。
執行層以 `diff` 實測既存者**逐字等於 `docs/fw036/templates/DECISIONS.md`
（僅 `{FEATURE}` → `Popup` 之代換）**，即 scaffold 當下之空白模板、
從未被人填寫、Sign-off 為未填佔位 —— 遂以 `mv` 取代之。
**未覆寫任何已簽署或已填寫之內容**。

---

## 六、工作簿起建（下放包 §六-6）

| 項 | 值 |
|---|---|
| 母本（R-G1）| `forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` |
| 母本 sha256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| 身分佐證（R-G1「以 SHA 認定，非檔名」）| 與 `FORMS.md` §母本表所載之 `6372fb6b…` 相符；另與 `_intake/SW_Update/`、`features/sw_update/inputs/`、`features/display/inputs/` 三處副本逐一實測相同 |
| 落點 | `features/popup/sandbox/base/`（R-G25：**xlsx 唯一可改之處**）|
| 手段 | `cp -p`。**未以 openpyxl 開啟寫入**（R-G3）——本包對母本之一切讀取皆 `read_only=True` 或 `data_only=True` 之唯讀載入 |
| 落點後 sha256 | `6372fb6be02f48dc…`（**與母本位元組相同**）|
| 檔名 | 逐字沿用母本檔名。**交付檔名屬 Pei（交付形式）**，作業副本不預先定名 |

`lint_paths.py --gate` PASS —— `sandbox/` 之 xlsx 為 R-G25 表列之合法落點。

---

## 七、四支 gate（下放包 §七；`gate_all.py` 實跑，實為五支）

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 463
PASS      exit 0   rulings_hash     OK: docs/fw036/RULINGS.sha.tsv 與現行條文相符（246 條）
PASS      exit 0   gates_tsv        OK: docs/runtime/GATES.tsv 相符（45 閘）
PASS      exit 0   lint_paths       PASS: 基線外違規 + delivered 不符 = 0

總判：**FAIL** —— 1 支未過：canon_refs
```

### canon_refs 之 FAIL 為既存狀態，非本包所致

- `canon_refs.py --waiver --report --top 2000` 之逐筆清單中，
  **`features/popup/` 命中 0 筆、`sources/` 命中 0 筆**（`grep -c` 實測）
- 463 筆之來源檔前五：`docs/fw036/RULINGS_LEDGER.md`(17)、
  `features/vehicle_category/docs/REASONING_sidecar.md`(7)、
  `features/display/docs/RETROSPECTIVE.md`(7)、
  `features/display/docs/INDEX.md`(7)、
  `features/display/docs/handoff/26_extraction_principle.md`(3) ——
  **全部為本包開工前即存在之檔**
- 本包新增之 md（`ANOMALIES.md`／`COVERAGE_GAPS.md`／`docs/INDEX.md`／
  本檔）**未使該數上升**：本包內三次跑 `gate_all.py`（落 `sources/` 後、
  scaffold＋RECON 後、全部落檔後）皆得 **463**
- **一次 462 之讀數已追因，非本包所致**：commit 前之一跑得 462，
  複測回 463。成因為 `features/popup/RULINGS.md` 於本包作業期間由分析層
  自另一 session 增寫 R-POP6～R-POP11（99 行，本包起跑時為 43 行）——
  **量測對象在兩次量測之間改變**。此為 §5a「跨輪次之累計量每輪自總量重算」
  之實例：463 與 462 各自對其量測當下之 repo 為真，兩者不可相減。
  現行讀數 463，連跑三次穩定
- **修正前段之陳述**：本包早先以 `grep -c "features/popup"` 對 `--report
  --top 2000/3000` 之輸出得 0，據以稱「popup 命中 0」。以 `--top 5000`
  重測，**popup 命中 1** —— `features/popup/RULINGS.md:76`
  （`item §9-16`，命中 `FO§9`／`IN§9` 而歧義）。該行屬 R-POP8，
  **由分析層寫入，非執行層產出**；且其寫入時點晚於本包之三次 463 量測。
  「本包產出物對該閘貢獻 0」仍成立；「popup 目錄命中 0」則不成立，此處更正。
  `sources/` 命中仍為 0（同一 `--top 5000` 量測）

**升級說明**：依 FO §8.2／26 包 §C 裁定 2，`gate_all.py` 總判 FAIL 者
「不得上繳，除非附升級說明」。本段即該說明 —— 本包對該閘之貢獻為 0，
其修復不在本包射程（跨 15+ feature 之歷史引用）。

### `lint_docs036` 之涵蓋實況

預設跑 `--feature power`。執行層另跑 `--feature popup` 亦 PASS。
**惟該工具之序號跳號檢查只認 `DR-PW`／`A-PW`／`A-PM` 三個硬寫前綴**，
本 feature 之 `DR-POP`／`A-POP` 不受檢 —— PASS 不代表已驗。見 **A-POP4**。

### `rulings_hash` 與 R-POP 系列

`--check` PASS（246 條），但其**預設範圍為
`docs/fw036/FEATURE_ONBOARDING.md` ＋ `features/vehicle_setting/RULINGS.md`
兩檔**（`SCOPE_DEFAULT`，W-P1 結構化範圍），**不含
`features/popup/RULINGS.md`**。下放包 §七 所期之「R-POP 系列 sha8 增列」
因此**未落入 tracked 之 `RULINGS.sha.tsv`** —— 擴大該範圍是政策性變更，
執行層不自裁。以 `--all-features` 對 scratch 目錄實測之值如下（供引用）：

| 條 | sha8 | 落點 |
|---|---|---|
| R-POP1 | `61145b5f` | `features/popup/RULINGS.md:7` |
| R-POP2 | `93a0e937` | `features/popup/RULINGS.md:14` |
| R-POP3 | `6f6a3531` | `features/popup/RULINGS.md:23` |
| R-POP4 | `1555a8f1` | `features/popup/RULINGS.md:29` |
| R-POP5 | `896b4b84` | `features/popup/RULINGS.md:36` |

### `pytest` 全跑（因本包動到共用腳本，額外自加之檢查）

```
8 failed, 1235 passed, 15 skipped
```

- `tests/test_extract_source.py`：**8 passed**（原 6 ＋ 本包新增 2）
- 8 個 failed 全數為**本包開工前即紅**，與 popup 無關：
  - `test_single_write_path.py` 2 支 —— `KNOWN_VIOLATIONS` 基線未涵蓋
    11 個既有 `openpyxl` save 呼叫點（`features/{time_management,user_profiles,
    vehicle_category,vehicle_setting}/scripts/*.py`），其中
    `vf230_wvf91_append.py` 為 session 起始時即在工作區之未追蹤檔
  - `test_intake_scaffold.py` 6 支 —— `new_feature.py` 於測試搭建之暫存
    repo 內 exit 2（模板缺件），本包未動 `new_feature.py` 與 `intake.py`
- **本包未使任一支由綠轉紅**

---

## 八、R-G13 引用回報

下放包 §七 令列本包引用之裁決及所讀 sha8。全域條文之 sha8 取自
`docs/fw036/RULINGS.sha.tsv`（本包 `--check` 已驗其與現行條文相符）：

| 條 | sha8 | 落點 | 本包如何用到 |
|---|---|---|---|
| R-G1 | `550ace4f` | `FEATURE_ONBOARDING.md:727` | 036 母本之選定與其 SHA 身分（§六）|
| R-G3 | `79860d4a` | `:736` | 全程未以 openpyxl 寫入任何 xlsx |
| R-G5 | `9814d24c` | `:747` | 未執行任何改狀態之 git |
| R-G7 | `bc6acec6` | `:757` | PDF 文字層以三工具互為對照向 |
| R-G11 | `894614b2` | `:776` | 盲區聲明（`COVERAGE_GAPS.md` 之 queue 掃描）|
| R-G13 | `abdc56e3` | `:788` | 本表本身 |
| R-G24 | `bd9a8cc0` | `:972` | `_intake/Popup/` 為暫存投遞區 |
| R-G25 | `50be5127` | `:1012` | 工作簿落 `sandbox/`；`lint_paths` 實跑 |
| R-G27 | `2bd39a12` | `:1049` | `sources/` 集中制；raw 落檔後不改 |
| R-POP1 | `61145b5f` | `popup/RULINGS.md:7` | slug／目錄（**非 tracked 指紋表**，見 §七）|
| R-POP2 | `93a0e937` | `:14` | 生成範圍 5 leaf；`COVERAGE_GAPS.md` |
| R-POP3 | `6f6a3531` | `:23` | DR 三件之登記狀態 |
| R-POP4 | `1555a8f1` | `:29` | `feature.yaml` 之 `test_group: Popup` |
| R-POP5 | `896b4b84` | `:36` | 七列台帳之 Heading 標記（§五-4）|

---

## 九、三分法清單（canon §1.2）

### defect（阻斷或已修）

| # | 內容 | 處置 |
|---|---|---|
| D1 | `extract_source.py` 撞名靜默覆蓋，`SYS1` 之 `Polarion` sheet 15 列被 `_polarion` 覆蓋而消失 | **已修 + 迴歸測試 + 重抽**（A-POP1）|

### style-divergence（形制不一致，不阻斷）

| # | 內容 | 處置 |
|---|---|---|
| S1 | `new_feature.py` 骨架用 `A-POnn`（`feature[:2].upper()`），與 `R-POP`／`DR-POP` 不同綴 | 本 feature 一律 `A-POP`；骨架未改（A-POP4）|
| S2 | `feature.yaml` 模板預填 Revision A/B 欄位字母，母本為 Revision C | 本 feature 按實測改寫；模板未動 |
| S3 | 下放包 §一-1 記「D4 Date = 2020/09/05」；實測該值在 **G4**，D4 為標籤 `Reviewer：` | 事實（日期早於規格 2023/02/02）成立，僅儲存格座標有誤，登錄不追改 |

### note（存查）

| # | 內容 |
|---|---|
| N1 | 三件投遞檔名與 Project 附件名有底線／括號／空白之正規化差異（§一表）；sha 相符者內容同一 |
| N2 | 母本 data validation `P10:Q1411 = "P0,P1,P2,P3"` 把 `Q`（分鐘數）一併綁上優先級詞彙 —— 母本既有瑕疵，未動 |
| N3 | design_method 欄（R）於母本無 data validation，詞彙強制力來自 lint 而非 Excel |
| N4 | `core_hmi_lf_pdf` 之 extracted md 內容全空 —— 為「無文字層」之忠實記錄，非抽取失敗 |
| N5 | 037 之 `SWE1-POP-002` VC（S9）逐字引用 `SWE1-POP-004-01`～`-05`，本簿確實無此五號（DR-POP3 前提實測成立）|
| N6 | 037 K12 逐字自陳 touch-outside「default to disable, requester should call the API to enable」，下放包 §四-3 之前提實測成立 |

---

## 十、新開 anomaly ／ DR 成對

| anomaly | 內容 | 對應 DR | 說明 |
|---|---|---|---|
| **A-POP1** | 抽取工具撞名靜默覆蓋 | **無 DR** | 執行層自身工具之缺陷，不缺任何外部檔案，故不開 DR。已修 |
| **A-POP2** | DR-POP1／DR-POP2 之標的在 `forms/` 內已存在 | **DR-POP1／DR-POP2（既有，狀態未改）** | 成對關係為「anomaly 指出既有 DR 之前提失效」，非新開 DR。**執行層未改其狀態** —— 素材納入屬 Pei |
| **A-POP3** | `_5.5` 無 leaf 依託 | **無 DR** | 缺的不是文件而是上游 SWE1 列，屬 RD-1 具名上報之範疇（`COVERAGE_GAPS.md`）|
| **A-POP4** | 治理三簿之序號檢查未涵蓋 `A-POP`／`DR-POP` 前綴 | **無 DR** | 工具涵蓋範圍問題 |

**未結 DR（IN §8.4.3，隨包附列）**：DR-POP1、DR-POP2、DR-POP3，
三件狀態皆「已登記，未送出」，本包未動。

---

## 十一、獨立判斷 —— 本包是否仍有該驗而未驗者

**有，五項。**

1. **`sources/extracted/` 之抽取物只驗了「量」，未驗「值」。**
   §F-6 比對行數與非空儲存格數；本包另加撞名守衛。但**沒有任何檢查
   確認 tsv 內的字元與原檔儲存格逐字相同** —— `cell_text()` 之跳脫
   （`\t`／`\n`／`\\`）若有反向歧義（例如原文本身就含字面 `\t` 兩字元），
   回讀時無從還原。本包引用之所有 037 值（K8／S9／S11／E10／K12）
   已另以 openpyxl 直讀原檔複核過，但**其餘儲存格未複核**。
2. **`_polarion` sheet 之 181 列 Revision／Checksum 未使用亦未驗。**
   下放包 §一-2 稱其「追溯對映用」。本包只確認它存在且被正確抽出，
   **未驗其 NRL 編號集合是否等於 `Basic Report` 之 167 列**（181 ≠ 167，
   差 14 未追因）。此差異在 Phase 4 建追溯表時會被迫面對。
3. **PDF 之 21 頁圖面內容完全未讀。** spec_mode C 已定，但 render／OCR
   管線一次都沒跑過。下放包 §一-3 稱「附件頁 8 之 GP1～GP4 圖面文字與
   SYS1 export 5.3～5.6 逐句相符（人工比對一次）」—— **該比對在分析層對
   附件副本為之，執行層未於原檔重現**。Mode A 掉句風險（FO §3 之
   Home A-H12/16/18 前例）於本 feature 尚未實測排除。
4. **037 之 `下拉選單設定處` sheet（78 列）未讀。** 本包之 design-method
   詞彙取自 **036 母本**之 `下拉選單`（9 值）。037 自帶的那份未比對 ——
   兩者若不同，lint 詞彙該以何者為準未定。
5. **`feature.yaml` 之 `write_back`／`done_region` 區塊為 BLANK 之綁定推導，
   非實測。** `author_value: "PeiPYHsu"`、`tc_ref_id_value: "NEW"` 沿他
   feature 慣例填入，**本 feature 無任何前例可據**，且工作簿無 done region
   可對照。這幾個值在 P7 寫回前必須經 Pei 確認，不得由本包之存在推定已裁。

---

## 十二、待裁清單（照 Pei 之裁定順序即可續作）

| 項 | 問題 | 影響 |
|---|---|---|
| **A-POP2** | `forms/Pop Up List HMI R1 (26PI).xlsx` 是否即 DR-POP1 之標的？Priority Matrix 之 `SR24 1A` 版次可否用？`forms/` 兩件之落點政策？ | 決定 `-002-01`／`-002-03`／`-002-05` 是落 PENDING 還是填實值 —— **5 個 TC 中有 3 個受影響** |
| **A-POP3** | Layer 3 `PC1` 改為「spec 5.6」？`-002-02` 之 `spec_reference` 是否併列 `_5.5`？ | framework Part N 之措辭；`spec_reference` 錨定協定 |
| **A-POP1** | 共用腳本之缺陷修正是否應先裁而非逕行？ | 追認即可；程式已綠 |
| **A-POP4** | `A-POP`／`DR-POP` 前綴是否納入 `lint_docs036.py`？ | 治理三簿之跳號檢查涵蓋率 |
| **R-POP5** | Heading 台帳處置之 [DEFAULT] 追認 | 七列台帳之最終形 |
| `RULINGS.sha.tsv` | `rulings_hash.py` 之預設範圍是否納入 `features/popup/RULINGS.md` | R-G13 引用之可查證性 |
| `DECISIONS.md` | [PROPOSED]／[PEI] 未裁，Sign-off 未填 | **P2 未過，P3 以後不得起跑** |

## 十二之二、覆核當下之新裁（Pei，2026-08-27）

**`sources/` 之版控範圍**：`sources/raw/` **不入 git**，`sources/extracted/`
與 `sources/MANIFEST.tsv` **入**。

- 起因：本包為 `sources/` 首次有內容，commit 前發現 `sources/raw/` 未受
  `.gitignore` 涵蓋，而其內容為客戶原檔（PDF 5.7 MB ＋ 兩份 xlsx）。
  `features/*/inputs/` 與 `forms/*` 之既有政策皆為「本體不入、身分入」，
  `sources/` 之對應規則此前未定 —— 版控政策屬 Pei（Operating Charter §觸點），
  執行層停下詢問，未自裁。
- 落實：`.gitignore` 增 `sources/raw/`（附理由段）；`sources/README.md`
  增「版控」一條。`git check-ignore` 實測 raw 被忽略、extracted 未被忽略。
- 身分之可查證性不因此下降：`MANIFEST.tsv` 逐檔載 sha256，
  `extracted/` 每份首列載 `source_sha256` —— **檔案在磁碟，身分在 git**。
- **本條尚無 R- 編號** —— 條文之取號與正式措辭屬分析層，
  請於下一包以 `R-G28`（或分析層另定之號）補立，執行層據以回填
  `.gitignore` 與 `README.md` 之引用。

---

## 十二之三、上繳後之覆核結果（Pei，2026-08-27）

分析層於本包上繳後落 **R-POP6 ～ R-POP11**，四件 anomaly 全數處分。
逐條對映表見 `features/popup/docs/INDEX.md` §2；下一包待辦七項見同檔 §3。

**本 commit 之內容早於該六條裁決** —— `feature.yaml` 之
`paths.popup_list` 仍為 `null`、`DATA_REQUESTS.md` 之 DR-POP1 仍記
「已登記，未送出」，皆為上繳當下之狀態，**非漏改**。落實屬 02 包。

---

## 十三、本包產生之新檔（全文掃描，非人工列舉）

```
_intake/Popup/INTAKE.sha256
sources/raw/{popup_037_v0_2,core_hmi_lf_sys1,core_hmi_lf_pdf}/   3 檔
sources/extracted/{同上三 doc_id}/                                10 檔
sources/MANIFEST.tsv                                             （表頭 → 3 列）
features/popup/{RUNBOOK,ANOMALIES,DECISIONS,PLAYBOOK}.md
features/popup/{feature.yaml,.gitignore,RECON.md,COVERAGE_GAPS.md}
features/popup/data/{recon.json,recon_leaf_to_section.tsv}
features/popup/sandbox/base/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx
features/popup/docs/INDEX.md
features/popup/docs/upstream/01_intake_recon.md               （本檔）
scripts/extract_source.py                                     （修改，A-POP1）
tests/test_extract_source.py                                  （修改，+2 測試）
```

**本包未新立任何裁決條文** —— R-POP1～R-POP5 為下放包同包新立，
本包只讀不寫 `RULINGS.md`。

**git**（R-G5、R-G6，唯讀與改狀態分列）：
- 改狀態之 git：**一項未為**（無 `add`／`commit`／`checkout`／`restore`／
  `stash`／`clean`／`tag`／`push`）
- 唯讀之 git：**執行層亦一次未跑**。本檔開頭之分支名取自 session 起始時
  由工具環境提供之 `git status` 快照，非執行層自行查詢
