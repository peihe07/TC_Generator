# CIP Radio Tables v6.7 —— MPFA 兩流程圖之逐節點轉錄（R-DIAG28(b)）

來源：`forms/CIP_Radio_Tables_v6.7.xlsx`（sha16 `71f5ea4043992475`），
分頁 `MPFA Validate Process(X65, X40)`（圖 `xl/media/image3.emf`，sha16 `d3cccfdac8be2cbd`）與
`MPFA Select Process(X65, X40)`（圖 `xl/media/image4.emf`，sha16 `8f8f13572a6d86d0`）。
圖以 `soffice --headless --convert-to png` 轉出後逐節點目視轉錄。

**錨記法**：`CIP_Radio_Tables_v6.7:MPFA Validate Process` ／ `CIP_Radio_Tables_v6.7:MPFA Select Process`。
`specification_reference` 欄仍填 CFTS004 ObjectID（CFTS004-4940451／-4940462 等已明引本流程），
本錨只入 Remarks 與 `split_reason`。

> **本檔只轉錄，不改寫語意、不補圖上沒畫的節點、不由流程圖推算 CFTS004 未載之數值（下放包 §0）。**

---

## 一　`MPFA Validate Process` —— 標題 `MPFA VALIDATE PROCESS`，`Version 1.2 – Edited by Jim Witek`

分頁唯一文字格：`Note: This applies to HU equipped with Sirius XM X 65/40 chipset only`

| # | 形狀 | 文字（逐字） | 出邊 |
|--:|---|---|---|
| 1 | 起點（實心圓） | — | → 2 |
| 2 | 標註 | `Set Retry Flag = 0` | → 3 |
| 3 | 流程 | `Determine package index # to be validated based on vehicle sales codes` | → 4（邊標 `PkgIndex`） |
| 4 | 流程（雙側框） | `TX PkgCmd message with TransactionID = 0x02, Option = 0x02, & PkgIndex = value determined above` | → 5 |
| 5 | 判斷 | `PkgInd received within 600 ms with TransactionID = 0x02 & Option = 0x02?` | `Yes` → 7；`No` → 6 |
| 6 | 判斷 | `Retry Flag < 3?` | `Yes` → 13（`Retry Flag ++`）→ 回 4；`NO` → 12 |
| 7 | 判斷 | `IndCode = 0x03?` | `Yes` → 6；`No` → 8 |
| 8 | 判斷 | `IndCode = 0x0D or 0x0F?` | `Yes` → 6；`No` → 9 |
| 9 | 判斷 | `IndCode = 0x0C or 0x0E?` | `Yes` → 11；`No` → 10 |
| 10 | 判斷 | `IndCode = 0x10?` | `Yes` → 14；`No` → 11 |
| 11 | 流程 | `Return the Results with a value = IndCode` | → 15 |
| 12 | 流程 | `Return the Results with a value of $FF or IndCode (see note to the left)` | → 15 |
| 13 | 流程 | `Retry Flag ++` | → 4 |
| 14 | 流程 | `Return the Results with a value = IndCode` | → 16 |
| 15 | 終點 | `END ROUTINE` | — |
| 16 | 流程 | `Proceed to MPFA Select Process` | — |

**NOTE（逐字，五行）**

```text
NOTE
-3 retries with:  600 ms Timeout, Transaction ID = 0x02, Option = 0x02 (Return $FF)
-3 retries with:  IndCode = 0x03 (Return IndCode)
-3 retries with:  Indcode = 0x0D (Return IndCode)
-3 retries with:  Indcode = 0x0F (Return IndCode)
-3 retries with multiple combinations of the above (Return $FF)
```

---

## 二　`MPFA Select Process` —— 標題 `MPFA SELECT PROCESS`，`Version 1.2 – Edited by Jim Witek`

分頁唯一文字格：`Note: This applies to HU equipped with Sirius XM X 65/40 chipset only`

| # | 形狀 | 文字（逐字） | 出邊 |
|--:|---|---|---|
| 1 | 起點（實心圓） | — | → 2 |
| 2 | 標註 | `Set Retry Flag = 0` | → 3 |
| 3 | 流程 | `Determine package index # to be selected based on vehicle sales codes` | → 4（邊標 `PkgIndex`） |
| 4 | 流程（雙側框） | `TX PkgCmd message with TransactionID = 0x01, Option = 0x01, & PkgIndex = value determined above` | → 5 |
| 5 | 判斷 | `PkgInd received within 600 ms with TransactionID = 0x01 & Option = 0x01?` | `Yes` → 7；`No` → 6 |
| 6 | 判斷 | `Retry Flag < 3?` | `Yes` → 13（`Retry Flag ++`）→ 回 4；`No` → 12 |
| 7 | 判斷 | `IndCode = 0x03?` | `Yes` → 6；`No` → 8 |
| 8 | 判斷 | `IndCode = 0x0D or 0x0F?` | `Yes` → 6；`No` → 9 |
| 9 | 判斷 | `IndCode = 0x0C or 0x0E?` | `Yes` → 14；`No` → 10 |
| 10 | 判斷 | `IndCode = 0x00?` | `Yes` → 11；`No` → 17 |
| 11 | 流程（雙側框） | `Store the OpCode : PkgInd , TransactionID , IndCode, RadioID , Option , ArrayHash , , PkgMAC, BLanteUPC, BLpostUPC, BLdispUPC, OLanteUPC, OLpostUPC, & OLdispUPC values for the CA Pellet creation` | → 15 |
| 12 | 流程 | `Return the Results with a value of $FF or IndCode (see note to the left)` | → 16 |
| 13 | 流程 | `Retry Flag ++` | → 4 |
| 14 | 流程 | `Return the Results with a value = IndCode` | → 16 |
| 15 | 流程 | `Return the Results with a value = IndCode` | → 18 |
| 16 | 終點 | `END ROUTINE` | — |
| 17 | 流程 | `Return the Results with a value = IndCode` | → 16 |
| 18 | 流程 | `MPFA Process Complete – Proceed to CA Pellet Creation (Process Standard Section 3.3)` | — |

**NOTE（逐字，五行）**

```text
NOTE
-3 retries with:  600 ms Timeout, Transaction ID = 0x02, Option = 0x02 (Return $FF)
-3 retries with:  IndCode = 0x03 (Return IndCode)
-3 retries with:  Indcode = 0x0D (Return IndCode)
-3 retries with:  Indcode = 0x0F (Return IndCode)
-3 retries with multiple combinations of the above (Return $FF)
```

> **原文件內部不一致（`[A-DIAG60]`）**：本圖之 NOTE 首行書 `Transaction ID = 0x02, Option = 0x02`，
> 而同圖節點 4／5 為 `0x01`／`0x01` —— NOTE 顯係自 Validate 分頁逐字複製而未改。
> **本包不改寫**（§0：只轉錄）；retry 之結局語意兩圖相同，不影響 TC。已登 FB-DIAG-t。

---

## 三　兩圖差異表

| 項 | Validate | Select |
|---|---|---|
| `TransactionID` / `Option` | `0x02` / `0x02` | `0x01` / `0x01` |
| 節點 3 動詞 | `to be validated` | `to be selected` |
| `IndCode = 0x0C or 0x0E?` 之 `Yes` | → `Return … = IndCode` → `END ROUTINE` | → `Return … = IndCode` → `END ROUTINE`（同） |
| **`IndCode = 0x10?` 分支** | **有** —— `Yes` → `Return … = IndCode` → `Proceed to MPFA Select Process` | **無** |
| **`IndCode = 0x00?` 分支** | **無** | **有** —— `Yes` → `Store the OpCode : …` → `Return … = IndCode` → `MPFA Process Complete – Proceed to CA Pellet Creation` |
| 終端流程 | `Proceed to MPFA Select Process` | `MPFA Process Complete – Proceed to CA Pellet Creation (Process Standard Section 3.3)` |
| NOTE 五行 | 逐字相同 | 逐字相同（含 `0x02` 之誤，見上） |

**與 CFTS004 之一致性複核（下放包 §5 條件 2）**

| CFTS004 | 流程圖 | 判 |
|---|---|---|
| `-4940465`／`-4940454`：`three identical instances of Indication Codes $03, $0D, or $0F` → 該碼 | NOTE 第 2～4 行：`3 retries with: IndCode = 0x03／0x0D／0x0F (Return IndCode)` | **一致**（次數 3、碼值集合同） |
| `-4940466`／`-4940455`：`differing Indication Codes or as a result of timeout or for another reason` → `$FF` | NOTE 第 1 行（timeout → `$FF`）＋第 5 行（`multiple combinations` → `$FF`） | **一致** |
| `-4940464`：`code $10 is invalid for the package select routine` | Select 圖**無** `0x10` 分支；Validate 圖有 | **一致**（`$10` 只在 Validate 出現） |

**無矛盾，升級條件 2 不命中。**

---

## 四　其餘十分頁對本 feature 之適用性（T3）

| 分頁 | 對 389 列之引用 | 判 |
|---|---|---|
| `History` | 版次紀錄 | 非要件 |
| `SEEK Cancel_Stop Transitions` | 0 | Tuner seek 之 HMI 行為；037 `$5008` 只述 seek **status** 之讀寫，未引本表 |
| `TA-PTY31 station list cancel e ` | 0 | RDS TA/PTY 行為，非診斷 DID |
| `PI Seek Ordering` | 0 | 同上 |
| `Default ROW Market Presets` | 0 | 預設電台，037 無對應 DID |
| `Preset Defaults- R1` | 0 | 同上 |
| `Preset Defaults- VP3&4` | 0 | 同上（且非 R1 機種） |
| ` Predefined Presets -X65 chip  ` | 0 | 同上 |
| `Travel Link- Weather Icons` | 0 | Travel Link 圖示，037 無對應 DID |
| `Sheet1` | 0 | 空白 |

**只有兩張 MPFA 流程圖被本 feature 引用；其餘十分頁不產 TC。**
判準：`CFTS004-4940461`／`-4940450` 明引之標的為「`MPFA Select Process`／`MPFA Validate Process` flowchart」，
未引本檔其他分頁；037 之 389 列亦無任何列指向上述十分頁之主題。
