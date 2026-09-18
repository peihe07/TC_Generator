# Diagnostics 交付本 —— 執行指引（EXEC_GUIDE）

對象：`…_SWQT_Diagnostics_20260917_v02.xlsx`（**558 條 TC**）。v01（556 條）由本版取代，依 R-G72 不就地改。

---

## ⚠ 一　執行前提：診斷工具須已載入本 ECU 之 CDD 檔（R-DIAG33）

**本交付本 565 條中，547 條可直接執行；不可派工者只有 18 條。**

### 1.1　佔位之兩類

| class | 條數 | 意義 |
|---|--:|---|
| **`TOOL_RESOLVED`** | **427** | 值定義於本 ECU 之 **CDD 檔（CANdela）**。執行前於診斷工具載入該檔，工具即以人可讀之名稱呈現這些值，**TC 保留 `<…>` 佔位即為可執行** |
| **`ASSET_MISSING`** | **18** | 值不在 CDD 檔，需 RD 另供。**交付本中整列以 `FCE4D6` 著色者即此 18 條**，在 `SX-9830-0095` 與 PkgIndex 對照到件前**只可評審，不可派工** |

逐行清單見 `placeholder_summary.tsv`（**592 行**，`class` 欄）與 `placeholder_by_token.tsv`。

### 1.2　`TOOL_RESOLVED` 佔位之解讀（各舉一例）

| 佔位型 | TC 中之寫法 | 執行時如何取得 |
|---|---|---|
| **controlState**（`DR-DIAG-4`） | `$ 2F 50 00 03 <controlState for "buzzer control tone">` | 工具之 `$5000` I/O 控制畫面列出可選音調（7 kHz Tool controlled 等），選取即送出對應位元組 |
| **值域／版面**（`DR-DIAG-5`） | `1. The positive response 62 28 43 <module version record> is received, and the record contains the SXI Rev Minor` | 工具依 CDD 之 `$2843` 版面拆解回應，逐子欄位顯示；比對 `SXI Rev Minor` 該欄即可 |
| **不支援之 SID／DID**（`DR-DIAG-6`） | `$ 22 <unsupported DID>` | 工具之 DID 清單即本 ECU 支援者之全集；**取任一不在清單中之 DID** 送出即可 |

### 1.3　另有 `PENDING` 者

**無** —— 全本 `PENDING` 行數為 **0**（NRC 值已依 `CS.00100` Annex A 取定）。

## 二　一次性環境（全 556 條共用）

以下三項為**每條 TC 之 Pre-Condition 前三行**所述之環境，只需在測試開始時建立一次。
**本節只寫來源明載者，逐行附出處；未載者不寫。**

| # | 環境 | 來源（逐字） |
|---|---|---|
| 1 | ECU 處於預設診斷 session（Default Session） | `SYS3_CFTS_004_General Diagnostics_System Architectural Design_SYSAD.docx` §4.5 Session & Security Assumptions：`ECU starts in Default Session` |
| 2 | 診斷工具經 OBD-II 診斷接頭連線 | 同上 §4.5 Hardware Dependencies：`Diagnostic connector (OBD-II)` |
| 3 | 已取得 Security access `0x27` | 同上 §4.5：`Security access (0x27) is required for: Write DID / Routine execution / DTC clearing` |

**第 3 項只適用於 Write DID（`0x2E`）／I/O Control（`0x2F`）／Routine（`0x31`）之 TC**；
純讀取（`0x22`）之 TC 其 Pre-Condition 不含該行 —— 依 SYSAD §4.5 之列舉，讀取不在需要 security access 之列。

第三行為其他內容者（如 `The Sirius XM chipset is powered and responding`／`The antenna is in the "OK" condition`），
為該條 TC 自身之狀態前提，來源記於該 TC 之 `Specification Reference` 欄。

**本指引不含 SYSAD §4.5 以外之環境設定。** 診斷工具型號、CAN 速率、電源供應條件等三處來源
（CFTS004／037／SYSAD）皆未載，**不在此擬定**。

---

## 三　位元組式讀法

| 式 | 意義 |
|---|---|
| `$ 22 <DID hi> <DID lo>` | ReadDataByIdentifier |
| `$ 2E <DID hi> <DID lo> <data>` | WriteDataByIdentifier |
| `$ 2F <DID hi> <DID lo> <controlOptionRecord>` | InputOutputControlByIdentifier |
| `$ 31 01\|02\|03 <RID hi> <RID lo> [<option>]` | RoutineControl：start／stop／requestRoutineResults（R-DIAG20） |
| `$ 7F <SID> <NRC> (<label>)` | 負回應 |

**負向測試之兩軸**（R-DIAG22／R-DIAG22(amend)）：

- **長度軸** —— 請求為合法請求**省去最後一個 byte**，描述行綴 `with the last byte omitted`，回 `7F <SID> 13`。
- **不支援 DID／值域軸** —— `0x22` 讀類送 `22 <unsupported DID>`；`0x2E`／`0x2F`／`0x31` 保留完整長度並帶越界資料 byte，回 `7F <SID> 31`。

---

## 四　範圍說明

- 母體為 `SWE1_Diagnostics_V1 (3).xlsx` 之 **389 列**，**389/389 全數對映**（`coverage.tsv`）。
- 其中 **1 列**（`SWE1-Diagnostics-057`）之 CFTS004 Category 為 `Out of Scope`，依裁定保留原內容並於處置欄註記，**不執行**。
- `$0307` MPFA Validate／`$0309` MPFA Select 兩常式之重試路徑，依 `CIP_Radio_Tables_v6.7` 之兩張流程圖 NOTE 產出五種結局各一條
  （600 ms timeout ×3 → `$FF`；`$03`／`$0D`／`$0F` 各 ×3 → 該碼；混合 → `$FF`）。逐節點轉錄見 `features/diagnostics/data/cip_mpfa_flowcharts.md`。
- **環境／持久軸（重開機／電源循環／設定保存）未延伸** —— CFTS004 全文搜尋 `reboot`／`power cycle`／`persist`／`retain`／`ignition` **五詞全為 0**，037 之 VC／VM 亦零命中，無來源可據。若該行為存在，須由 CFTS004 補件後另行延伸。
