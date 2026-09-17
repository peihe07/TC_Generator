# Diagnostics 交付本 —— 執行指引（EXEC_GUIDE）

對象：`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Diagnostics_20260917.xlsx`（**556 條 TC**）。

---

## ⚠ 一　佔位填入前不得執行

交付本 **386 條 TC（整列以 `FCE4D6` 著色）**之 `Test Procedure`／`Expected Result` 含 `<…>` 佔位。
測試者知道要送哪個服務、讀哪個 DID，**但不知道要送哪些位元組**。

| token | 行數 | 缺件 |
|---|--:|---|
| `DR-DIAG-6` | 269 | 不支援之 **SID 與 DID** 清單 |
| `DR-DIAG-5` | 197 | 資料位元組之值域與 record 版面 |
| `DR-DIAG-4` | 64 | I/O Control 之 controlOptionRecord／controlEnableMask 全表 |
| `DR-DIAG-8` | 16 | `SX-9830-0095` 之 Package Indication 編碼 |

逐行清單見 `placeholder_summary.tsv`（546 行）與 `placeholder_by_token.tsv`（依 token 彙整）。
**著色列在上述四件到齊前只可用於評審，不可派工。** 未著色之 **170 條**可直接執行。

另有 **2 條 TC／3 行**為 `PENDING: DR-DIAG-1`（NRC 值無來源），非佔位而是**無法書寫之步驟**，同樣不可執行。

---

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
- **環境／持久軸（重開機／電源循環／設定保存）未延伸** —— CFTS004 全文搜尋 `reboot`／`power cycle`／`persist`／`retain`／`ignition` **五詞全為 0**，037 之 VC／VM 亦零命中，無來源可據。若該行為存在，須由 CFTS004 補件後另行延伸。
