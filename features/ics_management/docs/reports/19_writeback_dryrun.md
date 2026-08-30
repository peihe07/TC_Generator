# 作業 B — 寫回 dry-run（FO §6）｜2026-08-30

**本報告不產出任何 xlsx。** repo 內未新增任何 xlsx，`features/ics_management/sandbox/` **未建立**。
DV 保留之實測其輸出寫於 session scratchpad 並於驗畢後刪除（見 §5）。

## §1 母本

| 項 | 值 |
|---|---|
| 檔 | `forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` |
| sha256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| bytes | **200,650** |
| `forms/FORMS.md` 登錄行 | `\| **\`…_SWQT_20260817_ext.xlsx\`（母本）** \| \`6372fb6b…fb825b2\` \| 200,650 \| **\`forms/\`（留置）** \|` |

**與 `feature.yaml` 之 `reference.workbook_master` 宣告值相符**（`verify_reference_binding` 11／11 之一）。

## §2 workbook_state（**現場複驗，未沿用記憶**）

- 工作表 **9 個**：`Cover_old`／`ChangeHistory_old`／`Cover 封面`／`ChangeHistory 修訂履歷`／
  `Product Document 記錄封面頁`／**`Test Case Specification 測試用例規範`**／`Reference`／
  `QS Suggestion`／`下拉選單`
- 目標工作表：`Test Case Specification 測試用例規範`，`max_row=1411`、`max_col=34`
- **表頭列 = 第 9 列**；**資料區自第 10 列起**（與 memory 相符，且已現場複驗）
- **既有資料列 = 0**：第 10 列僅 `B10 = "1"`（序號模板），其餘 33 欄全空；
  第 11～60 列**全部無任何非空格**。
- **`workbook_state` 判定：空白，自第 10 列 append。**

## §3 dry-run 之列數對帳

| 面 | before | after | 差 |
|---|---|---|---|
| 資料列（有 TC 內容者）| **0** | **31** | +31 |
| 佔用列 | 第 10 列（僅序號）| 第 10～40 列 | — |

**算術**：0 ＋ 31 ＝ 31 ✓。第 10 列之既有序號 `1` 由第 1 條覆蓋（同為序號 1），**不新增列**。

## 欄位對映（34 欄逐欄）

| 欄 | 表頭 | 來源 |
|---|---|---|
| `B` | No.# | 序號（1..31） |
| `C` | Requirement or Design ID (Polarion) | **空白約定**：無 Polarion ID |
| `D` | Requirement or Design ID | `req_id` |
| `E` | Test Case ID (TestRail) | **空白約定**：無 TestRail |
| `F` | Test Case ID | **E42：json 無 tc_id** |
| `G` | Test Group | `test_group` |
| `H` | Test Set | `test_set` |
| `I` | Test Item | `test_item` |
| `J` | Pre-Conditions | `pre_conditions` |
| `K` | Input Test Data | `input_test_data` |
| `L` | Test procedure | `test_procedure` |
| `M` | Expected Result | `expected_result` |
| `N` | Specification Reference | `specification_reference` |
| `O` | Test Case Reference ID | **空白約定** |
| `P` | Test Case Priority | `priority` |
| `Q` | Estimated Test Time | **空白約定**：未估 |
| `R` | Test Case Design Methods | `design_method`（**x14 DV，R10:R1411**） |
| `S` | Functional Safety | **空白約定** |
| `T~Z` | 車型欄 7 欄 | **空白約定**：本 feature 未判車型適用面 |
| `AA` | Test Case Author | **空白約定**：屬 Pei |
| `AB` | Test Version | **空白約定** |
| `AC` | Test Vehicle (Bench) | **空白約定**：台架未定案 |
| `AD` | Test Period | **空白約定**：未執行 |
| `AE` | Tester | **空白約定**：未執行 |
| `AF` | Test Result | **空白約定**：未執行（DV AF10:AF1411） |
| `AG` | Defect ID | **空白約定** |
| `AH` | Remarks | **空白約定**：中文備註不入交付欄（IN §1） |

**空白約定欄共 14 項**（`T~Z` 計為一項含 7 欄）。

## 31 條之投影（摘要欄）

| # | 批 | req_id | Test Set | tc_title | 錨行 | design_method | priority | PENDING |
|---|---|---|---|---|---|---|---|---|
| 1 | b01 | SWE-ICS-010 | Stuck Button | Stuck button held over 120 s | 1 | Fault Injection | P0 |  |
| 2 | b01 | SWE-ICS-010 | Stuck Button | Stuck fault held until de-bounced not-pressed | 2 | Fault Injection | P1 |  |
| 3 | b01 | SWE-ICS-010 | Stuck Button | Button held exactly 120 s | 1 | Boundary Value Analysis | P1 |  |
| 4 | b01 | SWE-ICS-001 | Volume Control | VOLUME knob rotated clock-wise **[V1]** | 2 | Functional Based | P0 |  |
| 5 | b01 | SWE-ICS-001 | Volume Control | VOLUME knob rotated counter clock-wise **[V2]** | 2 | Functional Based | P0 |  |
| 6 | b01 | SWE-ICS-002 | Volume Control | Three detents rotated clock-wise **[V3]** | 3 | Functional Based | P1 | 1 |
| 7 | b02 | SWE-ICS-010 | Stuck Button | Press ignored during stuck condition | 2 | Fault Injection | P1 |  |
| 8 | b02 | SWE-ICS-010 | Stuck Button | Button responsive after release | 2 | Fault Injection | P1 |  |
| 9 | b03 | SWE-ICS-006 | Display Control | Power hardkey pressed while HU screen on | 1 | State Transition | P0 |  |
| 10 | b03 | SWE-ICS-006 | Display Control | Power hardkey pressed at Telematic Power full operation | 1 | State Transition | P1 |  |
| 11 | b03 | SWE-ICS-006 | Display Control | Power hardkey pressed while HU screen off | 1 | State Transition | P0 |  |
| 12 | b03 | SWE-ICS-006 | Display Control | Power hardkey pressed at Telematic Power idle | 1 | State Transition | P1 |  |
| 13 | b03 | SWE-ICS-007 | Display Control | Screen off hardkey starts the three second timer | 2 | Functional Based | P1 |  |
| 14 | b03 | SWE-ICS-007 | Display Control | Screen off hardkey pressed again within three seconds | 1 | State Transition | P1 |  |
| 15 | b03 | SWE-ICS-007 | Display Control | Three second period completed after screen off hardkey | 2 | State Transition | P0 |  |
| 16 | b03 | SWE-ICS-007 | Display Control | Screen off hardkey pressed while HU screen off | 2 | State Transition | P0 |  |
| 17 | b04 | SWE-ICS-003 | Browse Control | Knob 2 rotated clock-wise | 4 | Functional Based | P0 |  |
| 18 | b04 | SWE-ICS-003 | Browse Control | Knob 2 rotated counter clock-wise | 4 | Functional Based | P0 |  |
| 19 | b04 | SWE-ICS-003 | Browse Control | Knob 2 held stationary | 4 | Functional Based | P1 |  |
| 20 | b04 | SWE-ICS-003 | Browse Control | Knob 2 no change sent periodically | 5 | Functional Based | P1 |  |
| 21 | b04 | SWE-ICS-004 | Browse Control | Three detents counted in one rotation **[B5]** | 5 | Functional Based | P1 |  |
| 22 | b04 | SWE-ICS-004 | Browse Control | Knob 2 signals acted on by the HU | 2 | Functional Based | P0 | 1 |
| 23 | b04 | SWE-ICS-008 | Menu Navigation | Enter button pressed | 2 | Functional Based | P0 | 1 |
| 24 | b05 | SWE-ICS-004 | Browse Control | Knob 2 rotated on a scrollable screen | 2 | Functional Based | P1 | 1 |
| 25 | b05 | SWE-ICS-004 | Browse Control | Knob 2 rotated on a tuner source | 2 | Functional Based | P1 | 1 |
| 26 | b06 | SWE-ICS-005 | Volume Control | Mute hardkey pressed while audio unmuted | 2 | State Transition | P0 |  |
| 27 | b06 | SWE-ICS-005 | Volume Control | Mute hardkey pressed while audio muted | 2 | State Transition | P0 |  |
| 28 | b07 | SWE-ICS-009 | Menu Navigation | Back button pressed | 2 | Functional Based | P0 | 1 |
| 29 | b07 | SWE-ICS-006 | Display Control | Two ICS buttons pressed at the same time | 1 | Combinatorial | P1 |  |
| 30 | b07 | SWE-ICS-007 | Display Control | Button event change reported within Tbutton | 1 | Functional Based | P1 |  |
| 31 | b07 | SWE-ICS-001 | Volume Control | Knob 1 status sent on BH-CAN | 1 | Functional Based | P1 |  |

**合計 31 條；錨行 65；Test Set 相異 5。**

## PENDING 6 處逐字

| # | tc_title | 欄位 | 逐字 |
|---|---|---|---|
| 1 | Three detents rotated clock-wise | `pre_conditions` | `PENDING: DR-ICS4 <CFTS019 volume level range>` |
| 2 | Knob 2 signals acted on by the HU | `pre_conditions` | `PENDING: DR-ICS6 <HMI Logic and Flow browse mapping for ICS_KNOB2>` |
| 3 | Enter button pressed | `pre_conditions` | `PENDING: DR-ICS6 <HMI Logic and Flow screen mapping for Enter_Button>` |
| 4 | Knob 2 rotated on a scrollable screen | `pre_conditions` | `PENDING: DR-ICS6 <HMI Logic and Flow scroll mapping for ICS_KNOB2>` |
| 5 | Knob 2 rotated on a tuner source | `pre_conditions` | `PENDING: DR-ICS6 <HMI Logic and Flow tune mapping for ICS_KNOB2>` |
| 6 | Back button pressed | `pre_conditions` | `PENDING: DR-ICS6 <HMI Logic and Flow screen mapping for Back_Button>` |

**合計 6 處。**

## specification_reference 之排列檢查（IN §10.7 ＋ R-ICS40(c)）

- 逐行一 ObjectID、格式合式、升序：**違規 0**
- **跨家族混排（b06）**：3 條
    - Three detents rotated clock-wise：CFTS020-4819541 ⏎ CFTS020-4821701 ⏎ CFTS022-4914975
    - Mute hardkey pressed while audio unmuted：CFTS020-4821709 ⏎ CFTS022-4914993
    - Mute hardkey pressed while audio muted：CFTS020-4821709 ⏎ CFTS022-4914993
- **錨行 ≥3 者（b12 加錨可見）**：6 條

## §5 【E43 判定點】R 欄之 x14 DV —— **保留，未觸發**

母本 DV 實測（`xlsx_surgical._dv_counts`，classic／x14）：

| 成員 | classic | x14 |
|---|---|---|
| `xl/worksheets/sheet5.xml` | 1 | 0 |
| **`xl/worksheets/sheet6.xml`**（目標表）| **3** | **1** |

`sheet6` 之 classic DV 三處 sqref：`P10:Q1411`、`T10:Z1411`、`AF10:AF1411`；
**x14 DV 之 `xm:sqref` 為 `R10:R1411`** —— 即 R-G1 所警告之設計方法欄。

**實測**：以 `xlsx_surgical.surgical_save(verify=True)` 作單格試改，
`verify_structure` 通過（**未拋 `StructureError`**）：

- zip 成員 **48 個，前後一致**（無 lost／added）；
- **DV 計數前後完全相同**（`sheet6` 仍為 classic 3、x14 1）；
- **僅 `xl/worksheets/sheet6.xml` 一個成員有差異**，其餘 47 個 byte 相同。

**E43 未觸發。** 併記一項實況：`openpyxl.load_workbook` 於載入時發出
`UserWarning: Data Validation extension is not supported and will be removed`
—— **此即 R-G3 禁止以 openpyxl 寫入之原因**；`surgical_save` 自母本 zip 逐成員複製，
故該警告不影響輸出。

## §6 done-region hash

母本目標表**既有資料列 0**，**無 done region** → **`N/A`**（具名，非略過）。

## §7 不可出貨之四條（**標明，不寫入工作簿任何註記**）

| 標號 | tc_title | 阻因 | 所繫 |
|---|---|---|---|
| **V1** | VOLUME knob rotated clock-wise | `VOLUME POP_UP` 顯示條件於 CFTS022／020／019 與所有 HMI L&F **查無** | **DR-ICS9** |
| **V2** | VOLUME knob rotated counter clock-wise | 同 V1 | DR-ICS9 |
| **V3** | Three detents rotated clock-wise | 同族 | DR-ICS9 |
| **B5** | Three detents counted in one rotation | 同族阻因 | **DR-ICS2** |

標號對映取自 `docs/upstream/01_*.md` §表（V1～V3）與 `docs/upstream/04_*.md` §表（B5），**非本包自行指派**。

**四條之特性**：V1／V2／V3 **無佔位**（V3 之 1 處佔位繫於 DR-ICS4，非其阻因），
故 `pending_census` 不報、`selfcheck` 全綠。**只有本表與凍結記錄 §2 會提醒。**

**依令仍寫入工作簿**（R-ICS54(a) 為依現狀寫回），**但於本清單標明**；
**工作簿內不加任何註記**（IN §1 English only；且加註等同改內容）。

## §8 【E44 判定點】投影與 json 之逐字性

本 dry-run 之每一欄皆自 `generated/b*/b*_tcs.json` **直接讀取並原樣輸出**，
無任何字串處理（無 strip、無正規化、無換行轉換）。
**投影 ≠ 編輯之要求在本報告中以「不經手」保證，而非以「比對後相同」保證。**

**E44 未觸發**（無任何欄經改寫）。
作業 C 之讀回比對（`read_only=True, data_only=True` 逐條逐欄）為其真正之驗證點，**本包未做**。
