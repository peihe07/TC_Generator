# FORMS — FW form-revision manifest

Purpose: canonical registry of the FM-WI form layouts (036 workbook and
related) used across features. The xlsx form files in this directory are
NOT committed (same policy as `<Feature>/inputs/`); this manifest IS
committed and records each form revision's structural facts so that:

1. recon can validate a feature workbook's column mapping against a known
   layout instead of re-deriving it from scratch
2. a missing per-feature workbook (cf. AMFM 2026-08) has a structural
   backup even when the pre-filled instance must be re-obtained
3. layout drift between form revisions is detected as a manifest diff

Rules:
- One entry per form revision / layout variant, keyed by filename stem
- SHA256 binds the manifest entry to the exact file placed here
- Column letters are recorded ONLY after verification (recon header match
  or manual probe) — no guessed values; unverified fields stay `TBD`
- Per-feature deviations from a form entry (e.g. remarks column extent)
  are recorded in the entry's Notes, and always re-verified per feature
  in that feature's `feature.yaml`
- The pre-filled workbook delivered per feature stays in
  `<Feature>/inputs/`; this directory holds blank/reference copies only

---

## 036 母本條文（R-G1／R-G2，Pei 2026-08-17 裁定，全域）

```text
R-G1  036 母本（全域，跨 feature）
      自 2026-08-17 起，所有新 feature 一律以
      forms/…_SWQT_20260817_ext.xlsx 為 036 母本，不再逐 feature 詢問。
      母本選擇自此為 Tier 0 AUTO；既有 feature 之已交付件不因本條改變。
      執行層須將本條寫入 FORMS.md 與 FEATURE_ONBOARDING.md。
```

```text
R-G2  forms/ 舊檔處置（全域，Pei 2026-08-17 裁定：歸檔）
      forms/ 只保留 …_SWQT_20260817_ext.xlsx。其餘三份
      （…_SWQT_20260121.xlsx、…_SWQT_20260816_ext.xlsx、
      …_SWQT_Home_20260809.xlsx）以 mv 移入
      archive/forms_superseded/，**不得刪除**。
      移動前後各記錄 shasum -a 256，證明內容未變。
      歸檔後 FORMS.md 之各條目須改指 archive/ 路徑，條目本身保留。
```

條文全文見 `features/user_profiles/RULINGS.md`（含 R-G2 之理由段）。

**執行狀態（2026-08-17，user_profiles Phase 0）**：三份舊檔已以 `mv` 移入
`archive/forms_superseded/`，移前移後 SHA256 各記錄一次且完全一致，
未使用 `rm`。`forms/` 現僅餘 `…_SWQT_20260817_ext.xlsx` ＋ 本 manifest
＋ `.gitkeep`。以下各條目之 File／Reference file 路徑已依 R-G2 改指
`archive/forms_superseded/`，條目本身未刪。

| 檔 | SHA256（移前 = 移後）| bytes | 現位置 |
|---|---|---|---|
| `…_SWQT_20260121.xlsx` | `cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d` | 65,823 | `archive/forms_superseded/` |
| `…_SWQT_20260816_ext.xlsx` | `4b3d447051f914eb41cc9754abaa5ed89bc0f06251baf01681a18bf884b6bcf7` | 200,654 | `archive/forms_superseded/` |
| `…_SWQT_Home_20260809.xlsx` | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` | 119,885 | `archive/forms_superseded/` |
| **`…_SWQT_20260817_ext.xlsx`（母本）** | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | 200,650 | **`forms/`（留置）** |

---

## Form: FM-WI-FSM-036-A01 (Test Case Specification & Result)

The form's own revision letter lives in the `ChangeHistory 修訂履歷` sheet
and the form id in the header row-5 cell at the far right of the data block.
**Two layouts are in circulation**, and the revision letter — not the file
date — tells them apart. Revision C inserted one column mid-table, which
moves five fields; that is why a column map is never reusable unverified.

### Revision C — with Estimated Test Time (the original blank form)

- File: **`archive/forms_superseded/`**`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
  Specification & Result_SWQT_20260121.xlsx`
  （2026-08-17 依 R-G2 歸檔；原位置 `forms/`。**已非母本** —— 母本見本檔
  末節 `…_SWQT_20260817_ext.xlsx`）
- SHA256: `cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d`
  （歸檔前後各實測一次，一致）
- Captured: 2026-08-09 (blank form, 3 template rows at 10–12)
- Sheet: **`Test Case Specification 測試用例規範`** — note: NOT the
  `…&Result` name the instances use
- Header row: `9` · data from `10` · columns A–**AH** (34)
- Form-id cell: `AH5` = `FM-WI-FSM-036-A01`
- ChangeHistory: A (2025-10-20) · B (2025-12-08) · **C (2026-01-21)** —
  "新增欄位：預估測試時間(分鐘) / Add new column: Estimated Test Time (mins)"
- Column mapping (probed):

  | Field | Col | | Field | Col |
  |---|---|---|---|---|
  | No.# | B | | **Estimated Test Time** | **Q** |
  | req_id (Polarion) | C | | design_method | R |
  | req_id | D | | functional_safety | S |
  | tc_id (TestRail) | E | | vehicle models ×7 | T–Z |
  | tc_id | F | | author | AA |
  | test_group | G | | test_version | AB |
  | test_set | H | | test_vehicle | AC |
  | test_item | I | | test_period | AD |
  | pre_conditions | J | | tester | AE |
  | input_test_data | K | | test_result | AF |
  | test_procedure | L | | defect_id | AG |
  | expected_result | M | | remarks | AH |
  | spec_reference | N | | | |
  | tc_ref_id | O | | | |
  | priority | P | | | |

- Column B formula: `=IF(ISBLANK($D10),"",ROW()-9)`
- Design method vocabulary: `下拉選單`, 9 exact strings
- `Test Case Framework` sheet: **absent** (9 sheets total)
- Notes: no feature has been generated on this layout yet. A workbook dated
  after 2026-01-21 is NOT necessarily revision C — the AM/FM instance below
  is dated 2026-01-29 and is revision B.

### Revision A/B — no Estimated Test Time (every instance in the repo)

- Reference file: **`archive/forms_superseded/`**`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test
  Case Specification & Result_SWQT_Home_20260809.xlsx`
  （2026-08-17 依 R-G2 歸檔；原位置 `forms/`。R-G2 之理由具名此檔為
  Home 225 列工作簿在 repo 內之唯一載體、R-U6 style authority
  （Arif 144 列 done region）之唯一來源、rev A/B 版面 A–AG 之唯一結構參照，
  **故歸檔而不刪除**）
- SHA256: `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72`
  （歸檔前後各實測一次，一致）
- Captured: 2026-08-09 (pre-filled Home instance, 225 rows — see the
  provenance warning below before treating it as a reference)
- Sheet: `Test Case Specification&Result` · header row `9` · A–**AG** (33)
- Form-id cell: `AG5` = `FM-WI-FSM-036-A01`
- Column mapping (verified independently by `recon.py` header-text resolution
  against Home and AM/FM — both resolve to identical letters):

  | Field | Col | | Field | Col |
  |---|---|---|---|---|
  | No.# | B | | design_method | Q |
  | req_id (Polarion) | C | | functional_safety | R |
  | req_id | D | | vehicle models ×7 | S–Y |
  | tc_id (TestRail) | E | | author | Z |
  | tc_id | F | | test_version | AA |
  | test_group | G | | test_vehicle | AB |
  | test_set | H | | test_period | AC |
  | test_item | I | | tester | AD |
  | pre_conditions | J | | test_result | AE |
  | input_test_data | K | | defect_id | AF |
  | test_procedure | L | | remarks | AG |
  | expected_result | M | | | |
  | spec_reference | N | | | |
  | tc_ref_id | O | | | |
  | priority | P | | | |

- Design method vocabulary: `下拉選單`, 9 exact strings (identical to rev C)
- `Test Case Framework` sheet: present, empty (10 sheets total)
- Column B formula: varies by instance — Home `=ROW()-9`,
  AM/FM `=IF(ISBLANK($D10),"",ROW()-9)`. Not a layout discriminator.
- Vehicle model block (both revisions, same 7 in the same order):
  HDCC27 Atl-Hi · DT27 Atl-Hi · VF(ProMaster)637 Atl-Mi · Commander (598)
  Atl-Mi · Regengade (5210) Atl-Mi · Toro(2261) Atl-Mi · Fastack (376) Atl-Mi
- Scope field: header cell found by the label text `範圍 Scope` (`C5`, value
  in the merged `D5:H5`). Hand-maintained upstream and **wrong in both
  instances captured so far** — Home A-H26, AMFM RULINGS C1.
- Notes: Media's remarks column is recorded elsewhere as `AH`. That is one
  column past this layout's last column and has not been re-probed here;
  treat it as unverified until a Media instance is captured.

#### Provenance warning on the Home reference file

This copy is **not** the Home v2 deliverable and must not be submitted as
one. Diffed cell-by-cell against `features/home/output/…_Home_20260720.xlsx`
(SHA256 `cfc007f3…`, tag `fw036-home-regen-v2`), it is the pre-A-H26 build
with four editorial passes applied on top:

| Cell / column | This copy | Home v2 |
|---|---|---|
| `D5` Scope | `…AppDrawer-Projection-SWE1HMI-V0.1` — **uncorrected** | `…Home-HMI-V0.1` |
| `F` Test Case ID | `NR1L-HomeHMI-001…` on all 216 rows | blank |
| `G` Test Group | `CoreHMI` on all 216 rows | blank |
| `K` Input Test Data | `NA` on all 216 rows | blank where generation left it so |
| `Z` Author (done region) | `ArifChen` ×144 | `Arif` ×144 |

Two consequences worth carrying forward:

1. **It carries the defect A-H26 fixed.** Whatever pipeline produced this
   file branched before the Scope correction.
2. **`Z` = `ArifChen` breaks the Home done-region selector.** `feature.yaml`
   sets `done_region.author_value: Arif`; against this file that matches 0
   rows, so `build_remaining.py` and `write_back.py`'s content-hash invariant
   would both mis-select. If this row-author spelling is what upstream
   expects, it is a `feature.yaml` change plus a fresh baseline hash, not a
   silent edit.

Neither is resolved here — the manifest records structure and states what it
found.

### Instance register (pre-filled workbooks, layout confirmed by recon)

| Feature | Instance | Revision | Layout | Author | Rows |
|---|---|---|---|---|---|
| Home | `…_SWQT_Home_20260720.xlsx` | ChangeHistory C (ours) | A/B | `Arif` (done) | 225 |
| AMFM | `…_SWQT_CFTS024_Radio_20260129.xlsx` | ChangeHistory **B** | A/B | `Wilson` | 167 |

AM/FM was expected to need "template adaptation" because its layout differed.
**It does not** — recon's header-text resolution returns the same letters as
Home, D through AG. What differs is content convention, not geometry:
`test_group`/`test_set` are populated (`Radio` / `FM & AM`), `tc_id` carries
`newR1L-Radio-nnn`, `tc_ref_id` reads `New` rather than `NEW`, and
`spec_reference` is `CFTS024-<ReqIF.ForeignID>` rather than a document/section
string. The adaptation that was actually required was in the **037 Analysis
Report**, not the workbook — see below.

---

## Form: FM-WI-FSM-037-A03 / FM-WI-SW-…-SWRA (Analysis Report)

No blank copy captured. Structure recorded from instances because the
positional read that worked for Home returns **zero leaves** on AM/FM, and an
empty leaf list is indistinguishable from a finished feature.

| | Home 037-A03 | AMFM 037-A03 | AMFM SWRA-A02 |
|---|---|---|---|
| Sheet | `Analysis Report` | `Analysis Report` | `Analysis Report` |
| Header row | 7 | 8 | 7 |
| ID column header | `SWE-Requirement ID ` | `SWE-Requirement ID ` | `ID` |
| req family | `SWE1-HMI-HOME-*` | `SWE-RA-RAD-*` | `SWE-RAD-*` |
| Categorization | col 7 | col **31** | absent |
| Categorization values | `Functional Requirement` / `Heading` | `Functional` only | — |
| Source column | `HMI Source ID` (document names) | `Source Requirement ID` (SYSAD components) | `Source Id` + `ReqIF.ForeignID` |
| ASIL / FTTI | absent | **absent** | present (`QM` ×57, FTTI `NA` ×57) |
| Leaves | 140 (+21 headings) | 102 (0 headings) | 57 |

Capture rules this produced, now implemented in `scripts/recon.py`:

- header row = the row containing a `Requirement Description` cell
- `Categorization` located by header text, excluding `Sub Categorization`
- a leaf is any row whose Categorization **starts with** `Functional` —
  `Functional` and `Functional Requirement` are the same classification
  written two ways
- ASIL / FTTI located by header text; their absence in the ruled requirement
  source is the finding that keeps the SYS2/SYSRA safety layer out of the
  trace chain

---

## Capture procedure (when adding a form)

1. Place the blank/reference xlsx in `forms/`
2. Compute SHA256 (`shasum -a 256 <file>`) and record it here
3. Probe sheet name, header row, column headers; fill the mapping table
4. Record design-method dropdown vocabulary source
5. Record the ChangeHistory revision letter — it, not the filename date,
   identifies the layout
6. If the file is a pre-filled instance rather than a blank form, diff it
   against the known-good deliverable and record the provenance
7. Commit the manifest change (xlsx stays untracked)

---

## `…_SWQT_20260816_ext.xlsx` —— 容量擴充版（2026-08-16）

> **A-UP03／A-UP05（2026-08-17，user_profiles Phase 0）：本節以下之結構數值，
> 其量測對象在 repo 內已不存在。**
> 本節原記 123,717 bytes／`6d53056e…`／B 欄公式 row 10–601。2026-08-17 對
> 同檔名之磁碟檔實測為 **200,654 bytes／`4b3d447051f914eb41cc9754abaa5ed89bc0f06251baf01681a18bf884b6bcf7`／
> B 欄公式 row 10–1411**、DV 至 1411。**601 與 1411 是兩份不同的檔**，
> 非同一檔之記載誤差；原 123,717-byte 檔已不在磁碟上，xlsx 未入 git，無從還原。
> 故「與原範本之逐格差異 547 格」等數值一律視為**歷史記載**，
> 不得引為現行磁碟檔或現行母本之屬性。正式裁定待 Pei（A-UP05，Tier 2）。
>
> 磁碟檔已依 R-G2 移入 `archive/forms_superseded/`（移前移後 SHA 一致）。

| | 原 manifest 記載（量測對象已不存在） | **2026-08-17 磁碟實測** |
|---|---|---|
| 檔名 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260816_ext.xlsx` | 同（位於 `archive/forms_superseded/`）|
| SHA256 | `6d53056e559bd0c13d26d38f16754536ede0230a5ce69c8596cce8e8b28b9d4c` | `4b3d447051f914eb41cc9754abaa5ed89bc0f06251baf01681a18bf884b6bcf7` |
| bytes | 123,717 | 200,654 |
| mtime | （未記）| 2026-08-17 09:45:54 |
| B 欄公式範圍 | row 10–601 | **row 10–1411** |

| | |
|---|---|
| 來源 | `…_SWQT_20260121.xlsx`（`cd876c202c71e74b…`）→ Comfort 之 ENTRY 001 清列 → **Pei 於 Excel 擴充**（Comfort ENTRY 022 驗證通過）|
| 原範本 | `…_SWQT_20260121.xlsx` **未覆寫**，2026-08-17 依 R-G2 移入 `archive/forms_superseded/`。註：Comfort 之 `BASELINE.sha256` 所涵蓋者為 `features/comfort/inputs/` 內之另一份複本（同 SHA `cd876c20…`），非 `forms/` 這一份；歸檔後之三檔目前不在任何 `BASELINE.sha256` 涵蓋範圍內，其雜湊僅記於本 manifest |

### 擴充範圍（資料工作表 `Test Case Specification 測試用例規範`）

| 項 | `20260121` | **`20260816_ext`** |
|---|---|---|
| B 欄編號公式 `=IF(ISBLANK($Dn),"",ROW()-9)` | row 10–59 | **row 10–601** |
| R 欄 design_method 下拉（x14 DV）| `R10` ＋ `R11:R59` | **`R10:R601`** |
| P 欄 priority DV | `P10:Q11` | **`P10:Q601`** |
| T–Z DV | `T10:Z11` | **`T10:Z601`** |
| AF DV（測試結果）| `AF10:AF11` | **`AF10:AF601`** |

R 欄之下拉來源亦統一為 `下拉選單!$A$1:$A$9`（原 `R11:R59` 指向 `$A$1:$A$11`，
多含兩個空選項）。zip member 48 = 48。

### 與原範本之逐格差異 —— 547 格，逐項具名

| 差異 | 格數 | 說明 |
|---|---|---|
| B 欄 row 60–601 之編號公式 | 542 | **即擴充本身**（601 − 60 + 1 = 542）|
| `D10`／`D11` = `xxx`，`F10` = `NR1L-AntiTheft-001`，`G10` = `AntiTheft`，`S10` = `NA` | 5 | **原範本所帶之他 feature 範例列**，於本版為空 |

**feature 專屬之值：0 格。** 全檔（9 個工作表）搜尋 `Comfort`／`HVAC`／
`AntiTheft` 等字樣**無任何命中**；`D5`（範圍 Scope）之值格於兩版皆為空
（`C5` 之標籤 `範圍 Scope：` 兩版相同）；`D2` = `newR1L` 為原範本既有之值，
非 Comfort 所填。

**該 5 格為本版唯一之非擴充性差異，且方向是「更空」而非「更滿」** ——
其來源是 Comfort 之 ENTRY 001 清列步驟，清掉的是 AntiTheft 之範例資料。
若日後認為空白範本應保留該範例列，**還原為單一動作**（填回上表五格之值）。

### 用法

新 feature 以本版為母本，即免去範本容量之處置（Comfort 之 DR #35 / A-CF26
歷 19 次寫回、三項 assertion 持續 FAIL 之成因即此）。
**privacy 等既有 feature 之已交付件不因本版而改變** —— 一份新版範本不會回頭
修好已經交出去的檔（DR #36）。

---

## `…_SWQT_20260817_ext.xlsx` —— **現行 036 母本**（R-G1，2026-08-17）

依 R-G1，自 2026-08-17 起所有新 feature 一律以本檔為母本。以下全部欄位
為 2026-08-17 於 `forms/` 實測（唯讀探測；**全程未執行 openpyxl save**，
母本未被覆寫，R16/R18-3）。首個採用者：`features/user_profiles/`。

| | |
|---|---|
| 檔名 | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` |
| 位置 | `forms/`（母本）；複本於 `features/user_profiles/inputs/`，同 SHA |
| SHA256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| bytes | 200,650 |
| mtime | 2026-08-17 09:46:09（`dcterms:modified` 2026-08-17T01:46:09Z）|
| zip members | 48 |
| 工作表 | **9**：`Cover_old`／`ChangeHistory_old`／`Cover 封面`／`ChangeHistory 修訂履歷`／`Product Document 記錄封面頁`／**`Test Case Specification 測試用例規範`**／`Reference`／`QS Suggestion`／`下拉選單` |
| `Test Case Framework` 分頁 | **absent**（與 rev C `20260121` 同，rev A/B 之 10 分頁版面才有）|
| ChangeHistory 修訂履歷 | A (2025-10-20)／B (2025-12-08)／**C (2026-01-21)** —— 修訂人 張愷霏 ErinKFChang，核准 劉安哲 AllenACLiu。**版面 = revision C** |
| 表單 id 格 | `AH5` = `FM-WI-FSM-036-A01` |

### 資料工作表 `Test Case Specification 測試用例規範`

| 項 | 實測 |
|---|---|
| dimensions | `A1:AH1411` |
| 表頭列 | **9**（`B9`=`No.#/序號` 起，共 33 個非空表頭格；A 欄無表頭）|
| 資料列起點 | **10** |
| 欄範圍 | A–**AH**（34 欄）|
| `D2` 專案名稱 | `newR1L`（原範本既有之值）|
| `C5` 範圍 Scope 標籤 | `範圍 Scope：`；**值格 `D5` 為空** |
| `J5` 日期 | `2025/10/17` |
| workbook_state | **BLANK** —— Test Item(`I`) 或 Test Case ID(`F`) 非空之列 = **0**；資料區（row ≥ 10）除 B 欄公式外之非空格 = **0**（掃描 A–AH 全 34 欄）|

### 欄位對映（依表頭列 9 之表頭文字實測，A–AH）

| Field | Col | | Field | Col |
|---|---|---|---|---|
| No.# 序號 | B | | Estimated Test Time (mins) | Q |
| req_id (Polarion) | C | | design_method | R |
| req_id | D | | functional_safety | S |
| tc_id (TestRail) | E | | HDCC27 Atl-Hi | T |
| tc_id | F | | DT27 Atl-Hi | U |
| test_group | G | | VF(ProMaster)637 Atl-Mi | V |
| test_set | H | | Commander (598) Atl-Mi | W |
| test_item | I | | Regengade (5210) Atl-Mi | X |
| pre_conditions | J | | Toro(2261) Atl-Mi | Y |
| input_test_data | K | | Fastack (376) Atl-Mi | Z |
| test_procedure | L | | author | AA |
| expected_result | M | | test_version | AB |
| spec_reference | N | | test_vehicle (Bench) | AC |
| tc_ref_id | O | | test_period | AD |
| priority | P | | tester | AE |
| | | | test_result | AF |
| | | | defect_id | AG |
| | | | remarks | AH |

車型 7 欄（T–Z）順序與 rev A/B 相同。**與 rev A/B 之差異僅 Q 欄插入**，
其後各欄整體右移一格（rev A/B 之 remarks 為 AG，本版為 AH）。

### B 欄編號公式

- 範圍：**`B10`–`B1411`**，連續無斷點，共 **1402** 格
- 式樣：`=IF(ISBLANK($D10),"",ROW()-9)`（逐列相對位移，末列
  `=IF(ISBLANK($D1411),"",ROW()-9)`）

### 資料驗證（DV）範圍

| 欄 | 型別 | 來源／清單 | 範圍 |
|---|---|---|---|
| P（priority）| list | 內嵌 `"P0,P1,P2,P3"` | `P10:Q1411` |
| R（design_method）| list（**x14 擴充**）| `下拉選單!$A$1:$A$9` | **`R10:R1411`** |
| T–Z（車型）| list | 內嵌 `"0,1"` | `T10:Z1411` |
| AF（test_result）| list | 內嵌 `"Pass, Fail, Pending,Block,NA"` | `AF10:AF1411` |

**R 欄之 DV 為 x14 擴充**，openpyxl 讀取時會發出
`Data Validation extension is not supported and will be removed` 並丟棄之。
其範圍係自 `xl/worksheets/sheet6.xml` 之 `<x14:dataValidation>` 直接讀出。

**任何以 openpyxl 開啟並存回本版之操作，都會摧毀 R 欄下拉 —— 已實測，
非推論**（2026-08-17，於 repo 外之 scratchpad 複本上；母本 SHA 前後一致）：

| 項 | 存回前 | 存回後 |
|---|---|---|
| `<x14:dataValidation>` 節點數 | **1**（`R10:R1411`）| **0** |
| legacy DV（P／T–Z／AF）| 3 | **3，存活** |
| zip members | **48** | **47** |
| 工作表數／B 欄公式末列 | 9／1411 | 9／1411（不變）|

損壞是**選擇性**的，且工作表數、列數、公式、其他 DV 全部不變、
zip member 只少 1 —— **表面上像無害的重新封裝，任何只比對這些項目的檢查
都會全綠**。這是母本禁止覆寫（R16/R18-3）之外的第二個獨立理由，
亦是寫回實作之硬約束（見 `features/user_profiles/ANOMALIES.md` A-UP09）。

**注意**：本檔 Part I 之 `framework.md` §`Workbook sync` 節所示範例即
`openpyxl` + `wb.save()`。該範例跑在 rev A/B 版面上（無 x14 DV），
**照抄到本母本會摧毀 R 欄下拉**。

### 設計方法詞彙（`下拉選單` A1:A9，9 條逐字）

1. `功能測試 (Functional based ; no specific technique)`
2. `狀態轉換 (State Transition Testing)`
3. `決策表 (Decision Table Testing)`
4. `等價劃分 (Equivalence Partitioning, EP)`
5. `邊界值分析 (Boundary Value Analysis, BVA)`
6. `組合測試 (Combinatorial Testing ; Pairwise / t-wise)`
7. `情境 / 用例 (Scenario / Use Case Testing)`
8. `負向測試 (Negative / Invalid)`
9. `基礎故障注入 (Fault Injection Lite)`

`下拉選單` 工作表 dimensions 為 `A1:A11`，但 **A10／A11 為空** ——
DV 來源已為 `$A$1:$A$9`，不含空選項。

### 與 `20260816_ext`（磁碟版）之關係 —— 逐格差異 0

`20260817_ext` 是磁碟上 `20260816_ext` 之一次「另存新檔」：

| 比對項 | 結果 |
|---|---|
| 逐格值比對（34 欄 × 1411 列 = 47,974 格，含公式字串）| **差異 0 格** |
| 工作表名稱與順序 | 相同（9 分頁）|
| dimensions | 兩版皆 `A1:AH1411` |
| B 欄公式末列 | 兩版皆 1411 |
| DV 範圍（P／T–Z／AF）| 兩版相同 |
| zip members | 48 = 48 |
| 差異之 zip member | **僅 2 個**：`xl/workbook.xml`（Excel `documentId` GUID）、`docProps/core.xml`（`dcterms:modified` 01:45:54Z → 01:46:09Z，相隔 15 秒）|
| bytes | 200,654 → 200,650（差 4 bytes，全部來自上列兩個 metadata member）|

**故本版相對於磁碟上之 `20260816_ext` 無任何結構或內容變更。**
本版之實質差異是相對於 **rev C 原範本 `20260121`**（B 欄 row 10–59、
DV 至 59）之容量擴充至 1411 列 —— 但 FORMS.md 原記載之「601 列」版本
在 repo 內已不存在（A-UP05），故本節不沿用該中間版之任何數值。

---

## 參考資料庫（DBC / PROXI / LID）

依 **R-G12**（Pei 2026-08-24，全域）：DBC、PROXI 表、LID 對照表一律置於
`forms/`，不另立 `reference/`。`forms/*` 已由根 `.gitignore` 排除、
`FORMS.md` 已 tracked，形狀未變更（檔案不入 git，manifest 入 git）。

每檔六項必填欄位：(a) 檔名／SHA256／bytes／mtime　(b) 涵蓋範圍
(c) 版次與其來源　(d) 已知不涵蓋者　(e) 取代關係　(f) 首個採用之 feature
與日期。(b) 為必填之理由見 **R-G13**：無涵蓋範圍之登錄，「查無」不構成發現。

涵蓋範圍(b) 一律為執行層實測所得，量測條件見
`features/display/docs/upstream/04_reference_store.md` §4。

### `PDT27_E2A_R1_BHCAN2.dbc`

> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM19 選定為其 B-CAN 資料庫）、`ics_management`（R-ICS46，Pei 裁定之台架觀察匯流排）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256.

- **(a)** SHA256 `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`
  · 167,226 bytes · mtime 2026-08-24T19:59:45
- **(b) 涵蓋範圍**：B-CAN（BHCAN2）。訊號定義列 **344**（相異訊號名 342）、
  訊息 **63**。編碼非 UTF-8（以 cp1252 解讀）；行尾 CRLF 3,359 + 裸 LF 8
- **(c) 版次**：`R1`（檔名所載，非推定）
- **(d) 已知不涵蓋**：FD-CAN 上之訊號。例：`CM_TCH_STAT` 於本檔 0 命中，
  但 LID r368 載其為 `TELEMATIC_FD_5.CM_TCH_STAT`、`CAN` 欄為 `FD` ——
  **本檔本就不該有，不得記為缺漏**（R-G13 之教案）
- **(e) 取代關係**：與 `PDT27_E2A_R4_BHCAN.dbc`
  （`features/vehicle_setting/inputs/`）**並非版次關係**。訊號名集合
  三分實測：兩者皆有 310、僅 R4 有 **573**、僅 BHCAN2 有 **32**。
  何者適用於本專案**未裁定**（A-DM14）
- **(f) 首個採用**：`display`，2026-08-24

### `PDT27_E2A_R1_FDCAN8.dbc`

> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM19）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256。

- **(a)** SHA256 `2a86c4bf3e670d71b362d430b446d8d157c74b94429e833362f81f4a48f6a22e`
  · 1,106,532 bytes · mtime 2026-08-24T19:59:52
- **(b) 涵蓋範圍**：FD-CAN（FDCAN8）。訊號定義列 **1,916**（相異訊號名
  1,634）、訊息 **318**。cp1252；CRLF 19,805 + 裸 LF 2
- **(c) 版次**：`R1`（檔名所載）
- **(d) 已知不涵蓋**：B-CAN 上之訊號。例：`DCSD_DISP_STAT`、
  `RQ_DISP_INTS` 於本檔 0 命中，二者皆在 B-CAN 上
- **(e) 取代關係**：與 `PDT27_E2A_R5_FDCAN8.dbc`（vehicle_setting）並存；
  R5 有訊號定義列 2,037／訊息 323，較 R1 多。兩者之差異本輪未逐一比對
- **(f) 首個採用**：`display`，2026-08-24

### `Logical Identifiers and CAN Mapping v1_78.xlsx`

> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM17 之解析鏈）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256。

- **(a)** SHA256 `a01e1679c706cd454daf82573a732fe5ad5eedb3865083897cb18c970b312433`
  · 623,612 bytes · mtime 2026-08-24T20:02:03
- **(b) 涵蓋範圍**：14 個分頁。主分頁 `CAN Mapping` 為 2,627 列 × 35 欄，
  r1 標題／r2 架構分組／r3 欄名／**資料自 r4 起共 2,624 列**。
  架構欄組七個（r2 所載之起始欄）：`LID Information`(c1)／`Powernet`(c6)／
  `CUSW`(c11)／`Atlantis`(c16)／`Compact`(c21)／**`Atlantis High`(c26)**／
  `Comments`(c31)；`Atlantis High` 之 r3 欄名為
  `Signal Name`／`CAN`／`Format`／`SNA`／`VFs`。
  另 `Proxi & Configuration` 449 列 × 31 欄、`Rev History` 108 列，
  及 10 個車型專屬訊號分頁（3–35 列不等）
- **(c) 版次**：`v1_78`（檔名所載）
- **(d) 已知不涵蓋**：LID 之左欄為 Logical Identifier，**不是 CAN 訊號名**。
  以 LID 名直接查 DBC 必然 0 命中（例 `ICSPowerButton` → 實際 CAN 名為
  `CLIMATIC_PANEL.Radio_btn0`／`DIS_CENTERSTACK.DCSD_Power`）。
  一列可載多個 `MESSAGE.Signal`，本檔不指定何者適用
- **(e) 取代關係**：`features/vehicle_setting/inputs/` 之
  `…v1_76.xlsx` 為較舊版次。**兩版差異本輪未測**；依既有慣例
  （同 R-G1），vehicle_setting 之已交付件不因新版而改
- **(f) 首個採用**：`display`，2026-08-24（R-DM17 之三段解析鏈）

### `PROXI_HDCC27_R3_20250424.xlsx`

> **使用中之 feature（R-G15 反向記載）**：`display`（R-DM20 起 in scope）。各該 feature 之 `feature.yaml` `reference:` 節載其 SHA256。

- **(a)** SHA256 `e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2`
  · 743,785 bytes · mtime 2026-08-24T20:00:27
- **(b) 涵蓋範圍**：13 個分頁。`Format` 1,060 列 × 24 欄（參數主表）、
  `Country Code` 224 列、`Revision Notes` 483 非空列、
  `EPS_Configuration_Families` 50 列、`ANC Table` 23 列、
  `Projection Mode Selection` 11 非空列、`Additional Languages` 10 列、
  `Acoustic Configuration` 12 列、`Allowed Conditions` 6 非空列、
  `Checks` 9 非空列、`Help` 16 列、`Cover` 10 非空列、`Header` 4 非空列
- **(c) 版次**：`R3`，日期碼 `20250424`（檔名所載）
- **(d) 已知不涵蓋**：本輪**未解析其內容**（下放包 04 步驟 11：與本
  feature 之關聯尚未確立，逕行解析屬無據之工）。故其參數與 Display
  之關聯**未知**，不得以本條目為據主張任何 PROXI 參數存在或不存在
- **(e) 取代關係**：`features/vehicle_setting/` 另有其自用之 PROXI 取值
  （`data/_vf230_proxi_values.json`），來源檔非本檔，兩者關係未測
- **(f) 首個採用**：**尚無**。本輪僅登台帳

---

## 共用參考件 —— Pop Up（R-POP25 第 3 點）

依 **R-POP25**（分析層裁 [DEFAULT]，2026-08-28）：`forms/` 定位為
「跨 feature 共用參考件之單一落點」，**每一項須登錄於本檔**。
本節補登兩件 Pop Up —— 補登前 `grep -i "pop up" forms/FORMS.md` 命中 **0**。
**R-POP25 之實作限於「登錄」：本輪不移動、不刪除、不改任何檔。**

欄位形制沿上節「參考資料庫（DBC / PROXI / LID）」之六項 (a)–(f)。

### `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`

> **使用中之 feature（R-G15 反向記載）**：`power`（R-P375(a)(b) 之段 1 入口）；
> **`vsm_v42`／`vsm_v43`**（2026-09-02，R-VL6(a)／R-P375(a) 之段 1 入口 —— 下放包 04 W-9）。
> vsm_v42 之 W-5′ 實測：`Settings` 分頁 **B／C 欄**（設定名）命中 **10** 個訊號名，
> 比對規則含第五規則（去 `_Menu`／`_Setting`）；結果為 `UI路徑(R-P375b)` 3 列與
> `UI+PROXI 雙路徑` 4 列之依據（`features/vsm_v42/data/signal_chain_v42_v3.tsv`）。

- **(a)** SHA256 `41daac0048d2afe15fe9aeee52a6197a28efdd2a71da44d2b836b4da3e9d4cf9`
  · 295,635 bytes · mtime 2026-08-25T09:15:30
- **(b) 涵蓋範圍**：3 分頁 —— `Title`（1,000 × 2）、**`Settings`（1,015 × 26）**、
  `Brand-Specific Names`（1,001 × 26）。`Settings` 為設定條目之主表；
  power 之段 1 命中落於 r96–97 c2/c4（`Auto-On Comfort` /
  `Auto_On_Comfort_Remote` / `Auto_On_Comfort_No_Remote`）
- **(c) 版次**：`R1 SR25 Post R1L-R (Feb 13 2026)`（檔名所載，非推定）
- **(d) 已知不涵蓋**：CAN 訊號名與 PROXI 參數名 —— 本檔為 **HMI 設定條目**之清單，
  其欄位為設定之顯示名與可選值，**不含訊號層資訊**。以訊號名查本檔必然低命中，
  不得記為缺漏（R-G13）
- **(e) 取代關係**：無已知前版於本 repo
- **(f) 首個採用**：`power`，2026-08-30（R-P375）

### `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx`

> **使用中之 feature（R-G15 反向記載）**：`power`（R-P375(a)(c)）；
> **`vsm_v42`／`vsm_v43`**（2026-09-02，下放包 04 W-9）。
> vsm_v42 之 W-5′ 實測：`Default Parameters` 分頁命中 **1** 個名，
> 屬 (d) 所述之靜態組態範圍，未用以代運行時狀態（R-P375(e)）。

- **(a)** SHA256 `8f3ae50edd9e8355d1e300bc71980dd099c2ad8e2a1b3de04ec329ff7c34126c`
  · 69,667 bytes · mtime 2026-08-27T20:56:49
- **(b) 涵蓋範圍**：3 分頁 —— `Revision History`（30 × 4）、
  **`Default Parameters`（268 × 109）**、`PNET ECU Master Configurations`（122 × 16,384）。
  power 之段 1 命中落於 `Default Parameters` r14–15 c12（`Rear Camera Present`）
- **(c) 版次**：`v1_0`（檔名所載）
- **(d) 已知不涵蓋**：執行期狀態 —— 本檔為**出廠預設值**與 ECU 組態，
  其值為靜態組態而非運行時狀態。**存在性參數不得代狀態**（R-P375(e)）
- **(e) 取代關係**：無已知前版於本 repo
- **(f) 首個採用**：`power`，2026-08-30（R-P375）

### `SR24 R1 Market Configuration Table v1.6.xlsx`

> **使用中之 feature（R-G15 反向記載）**：`power`（R-P375(a) 之段 1 入口；本輪 0 命中）；
> **`vsm_v42`／`vsm_v43`**（2026-09-02，下放包 04 W-9）。
> vsm_v42 之 W-5′ 實測亦為 **0 命中** —— 與 power 同，屬 (d) 之預期範圍，**非缺漏**（R-G13）。
> 本線 251 個訊號名對 `Market Config - R1` 分頁零交集，登記為**已查之檔**。

- **(a)** SHA256 `7e865d557e42c8b00fbb92ed58ae4e94bb1d561c5fdf01c6af32a70821fe7dc9`
  · 274,486 bytes · mtime 2026-08-27T20:56:49
- **(b) 涵蓋範圍**：8 分頁 —— `Revision Log`（43 × 10）、`ReadMe(Instruction)`（19 × 3）、
  **`Market Config - R1`（1,001 × 61）**、`R1 Tuner Layout`、`Radio Tuner Configuration`、
  `Measurement Units`、`Language Sets`、`R1 Navi MAP Sets`
- **(c) 版次**：`SR24 R1 … v1.6`（檔名所載）
- **(d) 已知不涵蓋**：訊號名與內部變數 —— 本檔為**市場組態**（語言、單位、tuner 配置），
  與電源狀態無交集。power 本輪 **0 命中**，屬 (d) 之預期範圍，**非缺漏**（R-G13）
- **(e) 取代關係**：無已知前版於本 repo
- **(f) 首個採用**：`power`，2026-08-30（R-P375；本輪 0 命中，登記為已查之檔）

### `Pop Up List HMI R1 (26PI).xlsx`

> **使用中之 feature（R-G15 反向記載）**：`popup`（**R-POP6** 裁定納入為素材，**引用原位不搬**；`features/popup/feature.yaml` 之 `paths.popup_list` 以相對 glob 指向本檔）。

- **(a)** SHA256 `ff47b7be63e5824cafe35deda9f9ddd0a63f6ea458169ef73689a1c559ea13ea`
  · 2,951,835 bytes · mtime 2026-08-25T13:51:21
- **(b) 涵蓋範圍**（執行層 2026-08-28 實測，`openpyxl` read_only／data_only）：
  3 個分頁。主分頁 `Main` 1,344 列 × 17 欄 —— **r1 = 基線字串
  `SR24 Post 2A CR25802`**、r2 為欄名、**資料自 r3 起，`^PU\d` 之 ID 列
  共 1,340 筆**（`PU0001` ～ `PU1579`，編號不連續）。
  r2 之 12 個具名欄逐字：`ID Number`／`Module`／`Timeout (sec)`／
  `Exit Conditions`／`Description`／`Category`／`String/Popup Message`／
  `Template 8.4" 10.1" 12"`／`Template 7"`／`Template 10.25"/12.3"`／
  `Stored in Notifications Inbox`／`Reference Documentation`（其後 5 欄無欄名）。
  另 `Templates` 34 列 × 5 欄、`Drop Down Fields` 73 列 × 8 欄
- **(c) 版次**：`Main!A1` 逐字 `SR24 Post 2A CR25802`；檔名另載 `HMI R1 (26PI)`
- **(d) 已知不涵蓋**：
  1. **popup 只取規格明文委派之欄位**（GP4 timeout／touch-outside 啟用／
     multi-task 例外），**不吸收本表之其他規則**
     （`features/popup/feature.yaml` `paths.popup_list` 註；IN §8.4.2）
  2. **`search keyboard` 無對應列** —— 三分頁全欄實測：連續詞組命中 **0**、
     同列兼含 `keyboard` 與 `search` 之 PU 列 **0**（詳
     `features/popup/ANOMALIES.md` A-POP8）。故不得以本檔為據主張
     GP4-4 所舉之 search keyboard popup 存在或不存在
  3. **hard-button 分支無實例** —— 以 `again|second time|re-?press|toggle`
     掃 `Exit Conditions`（不分大小寫）命中 13 列，逐列判讀後僅
     `PU0215`（UI button）與本命題相關；`PU0229` 之開啟者為語音請求而非
     該按鍵（詳 A-POP7）
- **(e) 取代關係**：與同目錄之
  `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` **非同一文件**
  且**非同代**（該件為 SR24 1A，早於本檔之 SR24 Post 2A 兩代）。
  兩者不互相取代。本檔亦非 `forms/` 之 036 母本，與 R-G1／R-G2 無涉
- **(f) 首個採用**：`popup`，2026-08-27（R-POP6；DR-POP1 據此結案）。
  殘留兩點隨 RD-1 確認：CR 版位（`CR25802` vs `CR22510`）與 `(26PI)` 之適用性

### `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`

> **使用中之 feature（R-G15 反向記載）**：**無** —— `popup` 於 **R-POP7** 裁定**不納入**（版次早於基線兩代）；`DR-POP2` 續開，向上游索 SR24 Post 2A 現版。

- **(a)** SHA256 `dc078763c67b52388eba8edf5c461515cfd2d92dd3a78dba0ce4e365e43ccc2f`
  · 1,035,049 bytes · mtime 2026-08-25T13:50:34
- **(b) 涵蓋範圍**（執行層 2026-08-28 實測，**只取結構事實**）：
  **10 頁**（`/Type /Pages` 之 `/Count` 與 `/Type /Page` 計數皆為 10）。
  含字型物件（`/Font` 79 處）與影像物件（`/Image` 66 處）。
  **內容未解析** —— 見 (d)
- **(c) 版次**：`SR24 1A`，日期 `May 3 2021`（皆檔名所載）。
  popup 之規格基線為 `SR24 Post 2A (February 2 2023)`，**本件早兩代**
- **(d) 已知不涵蓋**：**本輪未解析其內容，且不得解析** ——
  R-POP7 已裁定不納入為素材；逕行解析即等於把被裁定排除之件讀進判斷。
  故 popup 之 queue／priority 行為**不以本件為據**，
  spec 5.1 所引之 Priority Matrix 仍為缺件（DR-POP2）
- **(e) 取代關係**：**被上游之 SR24 Post 2A 現版取代**（該現版尚未到件，
  即 DR-POP2 之標的）。與同目錄之 `Pop Up List HMI R1 (26PI).xlsx`
  非同一文件，不互相取代
- **(f) 首個採用**：**尚無**。本輪僅登台帳（R-POP25 第 3 點）

### 本節之範圍限制（誠實揭露）

本輪只補登上列**兩件**（Pei 2026-08-28 指定）。
`forms/` 尚有 **3 件未登錄**，依 R-POP25 第 3 點皆應補，但不在本包指定範圍：

| 未登錄檔 | 目測用途 | 誰該補 |
|---|---|---|
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | HMI 設定清單 | 其首個採用之 feature |
| `SR24 R1 Market Configuration Table v1.6.xlsx` | 市場配置表 | 同上 |
| `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | 預設值／PNet ECU 配置 | 同上 |

> **[已失效 —— 2026-09-02，vsm_v42 下放包 04 W-9 執行時實測]**
> 上表三件**皆已於本檔登錄**，(a)–(f) 齊全，**首個採用 = `power`（2026-08-30，R-P375）**，
> 條目見本檔 §`共用參考件 —— Pop Up` 之三小節。本表與該三小節同存於本檔而互相矛盾，
> 成因為本節（範圍限制）落檔於補登之前而未隨補登更新。
> **本表保留不刪（R-TM13），加註失效。**
> 下放包 04 W-9 令 vsm_v42 補登該三件並將 (f) 首個採用填為 `vsm_v42,vsm_v43` ——
> **未照辦**：其 (f) 已由 `power` 於更早日期佔用，覆寫即抹除他線之正確記載。
> 執行層改補 **R-G15 反向記載**（在使用之 feature），為加法不為覆寫。

**未代登** —— 六項 (a)–(f) 之 (b) 涵蓋範圍與 (f) 首個採用須由實際使用者
實測填寫，由未使用它的 feature 代填會產出無人負責的登錄。

---

## ATL-Mi DBC 兩件（vsm_v42／vsm_v43，分析層登錄 2026-09-02，R-VL14／R-VT15）

### `Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`

- **(a)** sha256 `5cac2abcecdf37e2f07991e26dc4cf748fe24874fde93af77a85ea8936d3ed16` · 425,072 bytes · Pei 放件 2026-09-02
- **(b) 涵蓋**（分析層與執行層兩方實測一致）：`BO_` 139／`SG_` 定義行 844（相異 794）／`VAL_` 619。
  ISO-8859＋CRLF，解析以 latin-1 讀、行首錨定（`BA_` 屬性行內含 `SG_` 字串，不得入索引，A-VL11）
- **(c) 版次**：`R1 (29_01_2025) plusCR19670`（檔名所載）；637MCA = ProMaster（ATL-Mi）BH-CAN
- **(d) 已知不涵蓋**：CAN-C 之訊號；`RFHUB3.RFReq`（LID Atlantis 欄所指，本件查無）
- **(e) 取代關係**：對 vsm_v42 為段 3 主件；`PDT27_E2A_R1_BHCAN2`／`R1_FDCAN8`（Atlantis High）對該線降旁證，不取代其於 PM 等 Atlantis High 線之地位
- **(f) 首個採用**：`vsm_v42`（R-VL14，上繳 03 v3）

### `P363_BH-CAN [07338]_3A_R2.dbc`

- **(a)** sha256 `a51079be6e98e6e5d907b7c44bc77663daadbed60e63418dd9dd9f2b07188abd` · 332,522 bytes · Pei 放件 2026-09-02
- **(b) 涵蓋**：`BO_` 99／`SG_` 定義行 688（相異 655）／`VAL_` 503（有 VAL_ 之相異訊號 496）。
  ISO-8859＋CRLF，latin-1、行首錨定（A-VT28）
- **(c) 版次**：`3A_R2`，[07338]；P363（ATL-Mi）BH-CAN
- **(d) 已知不涵蓋**：CAN-C 之訊號（上繳 04 實測 6 列真缺＋2 列規格拼字疑誤）；`BRAKE1` 訊息不在本件（上游弧，R-VT13(c)）
- **(e) 取代關係**：對 vsm_v43 為段 3 主件；Atlantis High R1 DBC 對該線降旁證
- **(f) 首個採用**：`vsm_v43`（R-VT15，上繳 04 v4）

另：上表三件未登錄 xlsx（HMI Settings List／SR24／SR26）之首個採用實際已發生
（vsm 兩線 W-5 段 1），其 (a)–(f) 登錄排入 vsm 線 P3 包，由執行層實測填寫。
