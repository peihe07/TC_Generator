# CS.00100 Annex A（NORMATIVE）—— NRC 處理流程圖逐節點轉錄（R-DIAG5(amend3)）

來源：`CS.00100.pdf`，81 頁，Change Level **D**，sha16 `c1f9c6d7c5a5f0a2`
（`1_Customer_Requirement/STLA Standard/`）。Annex A 於 **p61–p75**。

**浮水印濾除法**：全頁疊有斜向浮水印，其字元與內文交錯抽出（如 `C 7 1 5 5 7 F : d i r e m s u o c`）。
實測其字型為 **`Helvetica-Bold`**（20.0／25.2／26.3 pt），而內文一律 **`ArialMT`／`Arial-BoldMT`**（5–14 pt）。
故以 `page.filter(lambda o: o["object_type"]!="char" or not o["fontname"].startswith("Helvetica"))` 一式濾除，
**不依座標、不依字級**，濾後全頁文字連續可讀。

Annex A 前言（p61 逐字）：

```text
This section defines the NRC handling according to ISO 14229-1:2020. The NRC handling shall be
compliant to the section "7.5 Server response implementation rules" for physical and functional
answers / suppression rules.
```

> **順序即優先序** —— 各圖自上而下之判斷順序即 NRC 之取用優先序；本檔逐節點依圖序編號。
> 節點文字逐字取自 PDF，不改寫。`$XX` 之 `manufacturer/supplier specific` 逐字保留。

---

## Figure A-1 —— NRC General Handling（p62，**共 12 個判斷**）

| # | 判斷（逐字） | No → | 備註（逐字） |
|--:|---|---|---|
| 1 | `SID Supported` | `NRC $11` | |
| 2 | `SID Supported in current session` | `NRC $7F` | `If ECU is in programming session or boot-mode NRC $11 (SNS) is accepted` |
| 3 | `SID security level correct` | `NRC $33` | |
| 4 | `SID with subfunction` | → `Sub Tables` | `Note: "Sub Tables" are all below NRC tables referred to each single diagnostic service.` |
| 5 | `SID $31` | Yes → `SID_$31` | |
| 6 | `Received at least 2 bytes` | `NRC $13` | |
| 7 | `Sub-funtion supported` | `NRC $12` | （原文拼字 `Sub-funtion`，逐字保留）|
| 8 | `Sub-funtion supported in current session` | `NRC $7E` | |
| 9 | `Sub-function security level correct` | `NRC $33` | |
| 10 | `Expected lenght for sufunction correct` | `NRC $13` | `Only requested data for sub-function must be present. i.e. 10.02 OK – 10 02 55 KO / 27 01 32 43 KO / ---> NRC $13`（原文拼字 `lenght`／`sufunction` 逐字保留）|
| 11 | `All other conditions ok` | `Send proper NRC` | `1) The proper NRC will be assigned according to failed check or data readiness. I.e. SAD, requiredTimeDelayNotExpired, conditionsNotCorrect, requestOutOfRange, busyRepeatRequest, etc.` |
| 12 | `Response exceed buffer size` | Yes → `NRC $14` | |

`NOTE: If the client (tester) sends a request with suppressPosRspMsgIndicationBit NOT set (0x), the ECU shall send NRC $78 before sending a positive if the positive response is not available within P2Can.`

---

## Figure A-2 —— SID `$31`（p63，**8 個判斷**）

| # | 判斷（逐字） | No → |
|--:|---|---|
| 1 | `min. length check` ¹ | `NRC $13` |
| 2 | `RID supported in active session?` | `NRC $31` |
| 3 | `RID security check ok?` | `NRC $33` |
| 4 | `SubFunction supported for routineIdentifier?` | `NRC $12` |
| 5 | `total length check?` ² | `NRC $13` |
| 6 | `routineControlOptionRecord contains valid data for the requested RID` | `NRC $31` |
| 7 | `Condition check` | `NRC $22` |
| 8 | `Request sequence respected for the RID?` | `NRC $24` |
| — | `Manufacturer/supplier specific check`（`optional`） | `NRC $XX` |

`1 at least 4 (SI+SubFunction+RID Parameter)`
`2 1 byte SI + 1 byte SF + 2 byte RID + nth byte routineControlOptionRecord required for the specific RID`

---

## Figure A-4 —— SID `$22`（p66，**多 DID 迴圈**）

| # | 判斷（逐字） | No → |
|--:|---|---|
| 1 | `min. length check + modulo 2 division` ¹ | `NRC $13` |
| 2 | `max. length length` ² | `NRC $13` |
| 3 | 迴圈（`Loop (multiple DIDs)`，`Same check for each DID`）：`DID#n support service 0x22 in active session?` | → 續迴圈 |
| 4 | `DID#n security check ok?` | `NRC $33` |
| 5 | `DID#n condition check ok?` | `NRC $22` |
| 6 | `At least one DID is supported in the active session?` | `NRC $31` |
| 7 | `Total response length exceeded (available in the server)` | Yes → `NRC $14` |
| — | `Positive response` `With all supported DIDs in this active session` | |

`1 minimum length is 3 byte (SI + DID)`
`2 maximum length is 1 byte (SI) + 2*n bytes (DID(s))`

> **`$22` 之不支援 DID → `NRC $31`**（第 6 判斷）—— 印證 R-DIAG22(amend) 之「讀類第二軸為 unsupported DID，ER `7F 22 31`」。

---

## Figure A-9 —— SID `$2F`（p70，**6 個判斷**）

| # | 判斷（逐字） | No → |
|--:|---|---|
| 1 | `Minimum length check` ¹ | `NRC $13` |
| 2 | `DID supports service 0x2F in active session AND inputOutputControlParameter is supported` | `NRC $31` |
| 3 | `Total length check` ² | `NRC $13` |
| 4 | `ControlState is supported (if applicable) AND controlMask is supported (if applicable)` | `NRC $31` |
| 5 | `Security check ok for requested DID?` | `NRC $33` |
| 6 | `Condition check` | `NRC $22` |
| — | `Manufacturer/supplier specific check` | `NRC $XX` |

`1 at least 4 (SI + DID + IOCP)`
`2 if IOCP = shortTermAdjustment, 1 byte SI + 2 byte DID + 1 byte IOCP + nth byte controlState + nth byte controlMask (if applicable), if IOCO <> shortTermAdjustment, 1 byte SI + 2 byte DID + 1 byte IOCP + nth byte controlMask (if applicable)`

> **與 R-DIAG29 之交叉印證**：註 2 逐字確認請求式為 `SI + DID + IOCP [+ controlState] [+ controlMask]`，
> 且 `controlState` **只於 `IOCP = shortTermAdjustment`（`03`）時存在** —— 與 Table 51 NOTE 一致。
> **`$2F` 之最小長度為 4 bytes**（`SI + DID + IOCP`），故 R-DIAG22 之長度軸「省末 byte」得 `2F <DID> 03`（3 bytes）確實不足 4 → `NRC $13` 成立。

---

## Figure A-11 —— SID `$2E`（p72，**7 個判斷**）

| # | 判斷（逐字） | No → |
|--:|---|---|
| 1 | `Minimum length check` ¹ | `NRC $13` |
| 2 | `DID supports service 0x2E in active session` | `NRC $31` |
| 3 | `Total length check` ² | `NRC $13` |
| 4 | `DID security check ok?` | `NRC $33` |
| 5 | `DID condition check ok?` | `NRC $22` |
| 6 | `Data record is valid?` | `NRC $31` |
| 7 | `Was correctly altered into server's memory` | `NRC $72` |
| — | `manufacturer/supplier specific`（`optional`） | |

`1 minimum length is 4 byte (SI + DID + DREC)`
`2 total length is 1 byte (SI + 2 byte DID + nth byte DREC)`

---

## 其餘九圖（只列標題，未轉錄）

| 圖 | SID | 頁 |
|---|---|--:|
| Figure A-3 | `$14` | 64 |
| Figure A-5 | `$23` | 67 |
| Figure A-6 | `$37` | 68 |
| Figure A-7 | `$36` | 69 |
| Figure A-8 | `$34` | 69 |
| Figure A-10 | `$3D` | 71 |
| Figure A-12 | `$2A` | 73 |
| Figure A-13 | `$19` | 74 |
| Figure A-14 | `$27`（sub-function `0x11`／`0x12`） | 74 |

`Table A-2 - Negative Response Code Description`（p81）另載各 NRC 之名稱對照。

## Table A-1 —— Service overview（p61，本 feature 相關者）

| Service | With subfunction |
|---|---|
| `Read Data By Identifier - 22 hex` | **NO** |
| `Write Data By Identifier – 2E hex` | **NO** |
| `Input Output Control By Identifier - 2F hex` | **NO** |
| `Routine Control - 31 hex` | **YES** |
| `Security Access - 27 hex` | YES |
| `Diagnostic Session Control - 10 hex` | YES |
