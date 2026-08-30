# 報告 12 — 87 個「軸層適用、變體不合、範圍隨變體層」之物件於 SYS2 之收錄面

**下放包 12 作業 B。A-ICS74／R-ICS40(f) 之量測。**
**只量不裁。本報告不作任何「應否納入」之判斷，不調和不符，不代擬條文。**

> # ⚠ E15 觸發
>
> **87 個中有 86 個在 SYS2 中有對應列**（門檻不設數字，非零即觸發）。
> 其中 **45 列為非 `Out of Scope`**（`Information` 44、**`Functional Requirement` 1**）。
> **範圍擴張屬 Pei 之決定，本報告停在此，不作任何納入與否之判斷。**
> 詳見 §5。

---

## §0 掃描條件

### 0-1 SYS2 素材之自驗

| 項 | 實測值 |
|---|---|
| 檔 | `features/ics_management/inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` |
| 讀法 | `openpyxl`，`data_only=True`、`read_only=True` |
| 分頁（全部） | `Basic Report`、`Polarion`、`_polarion` |
| **所取分頁** | **`Basic Report`**（`Polarion` 88×2 為工具設定表、`_polarion` 372×6 為欄位對映表，皆不含需求列） |
| **表頭列** | **第 1 列** |
| 資料範圍 | 第 2～334 列 |
| **資料列數** | **333**（與報告 10 §4-4 之 333 相符） |
| 欄數 | 81 |

**所取欄（逐一書出欄名，全文以欄名引用，不以 `c{n}`）：**

| 欄名（逐字） | 用途 |
|---|---|
| `ID` | SYS2 需求項 ID（`NRL-…`） |
| `Description` | 需求本文 |
| `SYS2 來源需求項目ID  Source Requirement items` | **ObjectID 比對欄**（欄名內為**雙空格**，逐字照抄） |
| `SYS2 分類 Category` | Category |
| `SYS2 子分類 Sub Category Function Name` | 子分類 |
| `SYS2 SW/HW/System (如果是HW+SW，就選System) ( software, hardware, or system (both software and hardware).)` | SW/HW/System |
| `SYS2 MD Feedback` | 人工範圍決定之留痕 |
| `SYS2 文件識別碼 Document ID` | 文件識別碼 |

### 0-2 ObjectID 之比對方式

`SYS2 來源需求項目ID  Source Requirement items` 之儲存格內容轉字串後，
以 `re.findall(r"\d{7}")` 取出**所有** 7 位數字，與 CFTS020 之 ObjectID 作
**區分大小寫之精確字串比對**。不作前綴比對、不作模糊比對。
一列得含多個來源 ID；一個 ObjectID 亦得對到多列（本次實測皆為 1:1）。

實測：333 列中**帶來源 ID 者 302 列**，相異來源 ID **302**；**來源欄空白者 31 列**。

### 0-3 87 個之取得方式

以 `importlib` **唯讀載入** `features/ics_management/scripts/cfts020_probe.py`
（該檔一字未改，見 §0-4 之自證），呼叫 `parse()`（判準 R-ICS2 v2(b)）：

| 集合 | 定義（三層分列，不合併旗標） | 實數 |
|---|---|---|
| 138 | `verdict=="適用"` ∧ `variant_fits_dut is True` | **138** |
| **29** | `verdict=="適用"` ∧ `variant_fits_dut is False` ∧ `scope!="隨變體層"` | **29** |
| **87** | `verdict=="適用"` ∧ `variant_fits_dut is False` ∧ `scope=="隨變體層"` | **87** |

三數與 upstream-11 §4-3 之 138／29／87 **完全相符**，集合本身無疑義。
惟其**分佈**與 upstream-11 §4-3 之敘述不符 —— 見 §2 與 §6。

### 0-4 未改檔之自證（不執行 git，依禁區令）

```
$ shasum features/ics_management/scripts/cfts020_probe.py
0927a3969faff09f5e1c0028f98f3eaf33406043  scripts/cfts020_probe.py
$ ls -l features/ics_management/scripts/cfts020_probe.py
-rw-r--r--  11259  Aug 29 21:13   ← mtime 為 b11 之時刻，本包未動
$ ls -l features/ics_management/scripts/sys2_87_probe_12.py
-rw-r--r--  10017  Aug 30 12:37   ← 本包新建
```

本作業寫入之檔**僅二**：
`features/ics_management/docs/reports/12_87_objects_sys2.md`（本檔）、
`features/ics_management/scripts/sys2_87_probe_12.py`（新腳本）。

### 0-5 重現指令

```
python3 features/ics_management/scripts/sys2_87_probe_12.py            # 摘要（§2／§3）
python3 features/ics_management/scripts/sys2_87_probe_12.py --table    # §1 逐一表
python3 features/ics_management/scripts/sys2_87_probe_12.py --reverse  # §4 反向查核
```

---

## §1 87 個逐一之 SYS2 對應判

**87 個中：SYS2 有對應列 86，無對應列 1。**
無對應者唯一：`4819365`（§1.5.1，`Artifact Type = Description`，章節引言性文字）。

`Functional Requirement` 唯一：`4819353`（§1.4.3.2）→ `NRL-52850`，
子分類 `ICS / DCSD (CFTS020)`、`SW/HW/System = System`、
`SYS2 MD Feedback` 逐字 `[01-Dec] Noted and  updated the SW and HW scope`。
其 `Description` 與 CFTS020 本文逐字同：
`If the$DCSD_DISP_STAT$ signal is received with an implausible value (values 5 or 6) , the HU shall continue to behave using the last plausible value received. …`
（此列即報告 10 §4-4 已逐字舉證之 `NRL-52850`；當時未知其來源物件屬本 87 之內。）

逐一表（依 ObjectID 升序）：

| # | ObjectID | 頂層節 | 節號 | SYS2 對應 | SYS2 ID | Category | 子分類 | SW/HW/System |
|---|---|---|---|---|---|---|---|---|
| 1 | `4819144` | §1.4 | §1.4.1 | **有** | NRL-402350 | Out of Scope | None | Out of Scope |
| 2 | `4819146` | §1.4 | §1.4.1 | **有** | NRL-402351 | Information | None | Information |
| 3 | `4819150` | §1.4 | §1.4.1.1.1 | **有** | NRL-402352 | Out of Scope | None | Out of Scope |
| 4 | `4819151` | §1.4 | §1.4.1.1.1 | **有** | NRL-402353 | Out of Scope | None | Out of Scope |
| 5 | `4819152` | §1.4 | §1.4.1.1.1 | **有** | NRL-402354 | Out of Scope | None | Out of Scope |
| 6 | `4819153` | §1.4 | §1.4.1.1.1 | **有** | NRL-402355 | Out of Scope | None | Out of Scope |
| 7 | `4819154` | §1.4 | §1.4.1.1.1 | **有** | NRL-402356 | Out of Scope | None | Out of Scope |
| 8 | `4819157` | §1.4 | §1.4.1.1.2 | **有** | NRL-402357 | Information | None | Information |
| 9 | `4819158` | §1.4 | §1.4.1.1.2 | **有** | NRL-402358 | Out of Scope | None | Out of Scope |
| 10 | `4819159` | §1.4 | §1.4.1.1.2 | **有** | NRL-402359 | Out of Scope | None | Out of Scope |
| 11 | `4819160` | §1.4 | §1.4.1.1.2 | **有** | NRL-402360 | Out of Scope | None | Out of Scope |
| 12 | `4819161` | §1.4 | §1.4.1.1.2 | **有** | NRL-402361 | Information | None | Information |
| 13 | `4819185` | §1.4 | §1.4.1.1.6 | **有** | NRL-402362 | Out of Scope | None | Out of Scope |
| 14 | `4819186` | §1.4 | §1.4.1.1.6 | **有** | NRL-402363 | Out of Scope | None | Out of Scope |
| 15 | `4819187` | §1.4 | §1.4.1.1.6 | **有** | NRL-402364 | Out of Scope | None | Out of Scope |
| 16 | `4819188` | §1.4 | §1.4.1.1.6 | **有** | NRL-402365 | Information | None | Information |
| 17 | `4819189` | §1.4 | §1.4.1.1.6 | **有** | NRL-402366 | Out of Scope | None | Out of Scope |
| 18 | `4819192` | §1.4 | §1.4.1.1.7 | **有** | NRL-402367 | Information | None | Information |
| 19 | `4819193` | §1.4 | §1.4.1.1.7 | **有** | NRL-402368 | Out of Scope | None | Out of Scope |
| 20 | `4819194` | §1.4 | §1.4.1.1.7 | **有** | NRL-402369 | Out of Scope | None | Out of Scope |
| 21 | `4819195` | §1.4 | §1.4.1.1.7 | **有** | NRL-402370 | Out of Scope | None | Out of Scope |
| 22 | `4819196` | §1.4 | §1.4.1.1.7 | **有** | NRL-402371 | Information | None | Information |
| 23 | `4819213` | §1.4 | §1.4.1.1.10 | **有** | NRL-402372 | Information | None | Information |
| 24 | `4819214` | §1.4 | §1.4.1.1.10 | **有** | NRL-402373 | Information | None | Information |
| 25 | `4819215` | §1.4 | §1.4.1.1.10 | **有** | NRL-402374 | Information | None | Information |
| 26 | `4819216` | §1.4 | §1.4.1.1.10 | **有** | NRL-402375 | Information | None | Information |
| 27 | `4819217` | §1.4 | §1.4.1.1.10 | **有** | NRL-402376 | Information | None | Information |
| 28 | `4819220` | §1.4 | §1.4.1.1.11 | **有** | NRL-402377 | Information | None | Information |
| 29 | `4819221` | §1.4 | §1.4.1.1.11 | **有** | NRL-402378 | Information | None | Information |
| 30 | `4819222` | §1.4 | §1.4.1.1.11 | **有** | NRL-402379 | Information | None | Information |
| 31 | `4819223` | §1.4 | §1.4.1.1.11 | **有** | NRL-402380 | Out of Scope | None | Out of Scope |
| 32 | `4819224` | §1.4 | §1.4.1.1.11 | **有** | NRL-402381 | Information | None | Information |
| 33 | `4819227` | §1.4 | §1.4.1.1.12 | **有** | NRL-402382 | Information | None | Information |
| 34 | `4819228` | §1.4 | §1.4.1.1.12 | **有** | NRL-402383 | Out of Scope | None | Out of Scope |
| 35 | `4819229` | §1.4 | §1.4.1.1.12 | **有** | NRL-402384 | Information | None | Information |
| 36 | `4819230` | §1.4 | §1.4.1.1.12 | **有** | NRL-402385 | Out of Scope | None | Out of Scope |
| 37 | `4819231` | §1.4 | §1.4.1.1.12 | **有** | NRL-402386 | Information | None | Information |
| 38 | `4819233` | §1.4 | §1.4.1.1.12 | **有** | NRL-402387 | Information | None | Information |
| 39 | `4819234` | §1.4 | §1.4.1.1.12 | **有** | NRL-402388 | Information | None | Information |
| 40 | `4819235` | §1.4 | §1.4.1.1.12 | **有** | NRL-402389 | Information | None | Information |
| 41 | `4819238` | §1.4 | §1.4.1.2.1 | **有** | NRL-402390 | Out of Scope | None | Out of Scope |
| 42 | `4819239` | §1.4 | §1.4.1.2.1 | **有** | NRL-402391 | Out of Scope | None | Out of Scope |
| 43 | `4819240` | §1.4 | §1.4.1.2.1 | **有** | NRL-402392 | Out of Scope | None | Out of Scope |
| 44 | `4819241` | §1.4 | §1.4.1.2.1 | **有** | NRL-402393 | Out of Scope | None | Out of Scope |
| 45 | `4819242` | §1.4 | §1.4.1.2.1 | **有** | NRL-402394 | Out of Scope | None | Out of Scope |
| 46 | `4819245` | §1.4 | §1.4.1.2.2 | **有** | NRL-402395 | Information | None | Information |
| 47 | `4819246` | §1.4 | §1.4.1.2.2 | **有** | NRL-402396 | Out of Scope | None | Out of Scope |
| 48 | `4819247` | §1.4 | §1.4.1.2.2 | **有** | NRL-402397 | Out of Scope | None | Out of Scope |
| 49 | `4819248` | §1.4 | §1.4.1.2.2 | **有** | NRL-402398 | Out of Scope | None | Out of Scope |
| 50 | `4819249` | §1.4 | §1.4.1.2.2 | **有** | NRL-402399 | Information | None | Information |
| 51 | `4819270` | §1.4 | §1.4.1.2.6 | **有** | NRL-402400 | Information | None | Information |
| 52 | `4819271` | §1.4 | §1.4.1.2.6 | **有** | NRL-402401 | Out of Scope | None | Out of Scope |
| 53 | `4819272` | §1.4 | §1.4.1.2.6 | **有** | NRL-402402 | Out of Scope | None | Out of Scope |
| 54 | `4819273` | §1.4 | §1.4.1.2.6 | **有** | NRL-402403 | Out of Scope | None | Out of Scope |
| 55 | `4819274` | §1.4 | §1.4.1.2.6 | **有** | NRL-402404 | Information | None | Information |
| 56 | `4819294` | §1.4 | §1.4.1.2.9 | **有** | NRL-402405 | Information | None | Information |
| 57 | `4819297` | §1.4 | §1.4.1.3.1 | **有** | NRL-402406 | Out of Scope | None | Out of Scope |
| 58 | `4819298` | §1.4 | §1.4.1.3.1 | **有** | NRL-402407 | Out of Scope | None | Out of Scope |
| 59 | `4819299` | §1.4 | §1.4.1.3.1 | **有** | NRL-402408 | Out of Scope | None | Out of Scope |
| 60 | `4819300` | §1.4 | §1.4.1.3.1 | **有** | NRL-402409 | Information | None | Information |
| 61 | `4819301` | §1.4 | §1.4.1.3.1 | **有** | NRL-402410 | Out of Scope | None | Out of Scope |
| 62 | `4819304` | §1.4 | §1.4.1.3.2 | **有** | NRL-402411 | Information | None | Information |
| 63 | `4819305` | §1.4 | §1.4.1.3.2 | **有** | NRL-402412 | Information | None | Information |
| 64 | `4819306` | §1.4 | §1.4.1.3.2 | **有** | NRL-402413 | Information | None | Information |
| 65 | `4819307` | §1.4 | §1.4.1.3.2 | **有** | NRL-402414 | Information | None | Information |
| 66 | `4819308` | §1.4 | §1.4.1.3.2 | **有** | NRL-402415 | Information | None | Information |
| 67 | `4819311` | §1.4 | §1.4.1.3.3 | **有** | NRL-402416 | Information | None | Information |
| 68 | `4819312` | §1.4 | §1.4.1.3.3 | **有** | NRL-402417 | Information | None | Information |
| 69 | `4819313` | §1.4 | §1.4.1.3.3 | **有** | NRL-402418 | Information | None | Information |
| 70 | `4819314` | §1.4 | §1.4.1.3.3 | **有** | NRL-402419 | Information | None | Information |
| 71 | `4819315` | §1.4 | §1.4.1.3.3 | **有** | NRL-402420 | Information | None | Information |
| 72 | `4819331` | §1.4 | §1.4.1.3.5 | **有** | NRL-402421 | Information | None | Information |
| 73 | `4819334` | §1.4 | §1.4.1.4.1 | **有** | NRL-402422 | Information | None | Information |
| 74 | `4819335` | §1.4 | §1.4.1.4.1 | **有** | NRL-402423 | Information | None | Information |
| 75 | `4819336` | §1.4 | §1.4.1.4.1 | **有** | NRL-402424 | Information | None | Information |
| 76 | `4819337` | §1.4 | §1.4.1.4.1 | **有** | NRL-402425 | Information | None | Information |
| 77 | `4819338` | §1.4 | §1.4.1.4.1 | **有** | NRL-402426 | Information | None | Information |
| 78 | `4819341` | §1.4 | §1.4.2 | **有** | NRL-402427 | Out of Scope | None | Out of Scope |
| 79 | `4819344` | §1.4 | §1.4.2.1 | **有** | NRL-402428 | Information | None | Information |
| 80 | `4819347` | §1.4 | §1.4.3.1 | **有** | NRL-402429 | Out of Scope | None | Out of Scope |
| 81 | `4819348` | §1.4 | §1.4.3.1 | **有** | NRL-402430 | Out of Scope | None | Out of Scope |
| 82 | `4819349` | §1.4 | §1.4.3.1 | **有** | NRL-402431 | Out of Scope | None | Out of Scope |
| 83 | `4819350` | §1.4 | §1.4.3.1 | **有** | NRL-402432 | Out of Scope | None | Out of Scope |
| 84 | `4819351` | §1.4 | §1.4.3.1 | **有** | NRL-402433 | Out of Scope | None | Out of Scope |
| 85 | `4819353` | §1.4 | §1.4.3.2 | **有** | NRL-52850 | Functional Requirement | ICS / DCSD (CFTS020) | System |
| 86 | `4819355` | §1.4 | §1.4.3.3 | **有** | NRL-402434 | Out of Scope | None | Out of Scope |
| 87 | `4819365` | §1.5 | §1.5.1 | **無** | — | — | — | — |

---

## §2 依頂層節分組之實數

| 頂層節 | 節標題（逐字） | `variant_of()` 歸類 | 87 之物件數 | SYS2 有對應 | 對到 FR 列之物件 |
|---|---|---|---|---|---|
| §1.4 | `Diagnosis and Recovery Common Between Architectures - ICS, HU, DCSD, FPDM, CCDMF and CCDMR` | **未分類** | **86** | **86** | **1** |
| §1.5 | `Functional Requirements - PNet - ICS and Associated HU` | Associated | **1** | 0 | 0 |
| **合計** | | | **87** | **86** | **1** |

87 個之 SYS2 對應列（86 列）之 `Category` 分佈：

| Category | 列數 |
|---|---|
| `Information` | **44** |
| `Out of Scope` | **41** |
| **`Functional Requirement`** | **1** |

> ### 與 upstream-11 §4-3 之敘述不符（列記，不調和）
>
> upstream-11 §4-3 稱這 87 個「分佈於 §1.5／1.6／1.7／1.14／1.16／1.17 等
> **Associated 分支**」。**實測不然**：
> **86／87 落在 §1.4**，而 §1.4 之標題為
> `… Common Between Architectures …` —— `variant_of()` 判為**未分類**，
> **既非 Associated 亦非 Disassociated**。落在真正 Associated 分支者**只有 1 個**
> （`4819365`，§1.5.1，且 SYS2 無對應列）。
>
> 成因（實測）：`87 = 適用 ∧ variant_fits_dut is False`，
> 而 `variant_fits_dut` 之定義為 `variant == "Disassociated"` ——
> **「未分類」亦落入 `False`**。故 87 之組成為
> **未分類 86 ＋ Associated 1**，非「Associated 分支 87」。
>
> 全域佐證（實測）：軸層適用者 **254** 之 `variant` 分佈為
> `Disassociated 138`／`未分類 86`／`Associated 30`；
> 而 `Associated 30 = §1.18 之 29 ＋ §1.5 之 1`。
> 即 **§1.6／1.7／1.14／1.16／1.17 之 Associated 物件無一軸層適用**。
>
> **本報告不推定此敘述不符之意涵，不調和，建議登新異常（`A-ICS?`）。**

---

## §3 與 §1.18 之 29 個的欄位形態對照（本作業之核心）

同一組欄位、同一掃法之並列：

| 欄位形態 | **87 個**（範圍隨變體層） | **29 個**（§1.18，R-ICS39 裁定算數） | 138 個（變體合 DUT，對照組） |
|---|---|---|---|
| 物件數 | 87 | 29 | 138 |
| SYS2 有對應列之物件數 | **86** | **28** | 135 |
| 無對應者 | 1（`4819365`，Description 型） | 1（`4821675`，Description 型） | 3 |
| 對應之 SYS2 列數 | 86 | 28 | 135 |
| `Category` = `Functional Requirement` | **1** | **8** | 47（另 `Functional requirement` 1） |
| `Category` = `Information` | 44 | 6 | 21 |
| `Category` = `Out of Scope` | 41 | 14 | 61（另 `Out of scope` 4） |
| `Category` = `Heading` | 0 | 0 | 1 |
| 子分類 `ICS / DCSD (CFTS020)` | **1** | **8** | 41（另 `Camera(CAM)` 6、`Display (including HAL)` 5） |
| 子分類空白（`None`） | 85 | 20 | 83 |
| `SW/HW/System` = `System` | 1 | 7 | 37 |
| `SW/HW/System` = `HW` | 0 | 1 | 4 |
| `SW/HW/System` = `SW` | 0 | 0 | 7 |
| `SYS2 MD Feedback` 非空之列 | **7** | **9** | 53 |
| 其中 FR 列帶 MD Feedback | 1／1 | 8／8 | — |
| `Document ID` | 逐列流水（`SR26_20260310-15xx`／`-16xx`） | 逐列流水（`SR26_20260310-17xx`） | 逐列流水＋`SR26_20250813-1632` × 27 |

### 3-1 核心答案：**有可辨差異，且差異落在關鍵欄。**

**下放包所設之判準為「若二者在 SYS2 中之欄位形態無可辨差異，
則『SYS2 收錄』這個理由對二者一體適用」。實測：該前件不成立。**

可辨差異逐一：

**(1) `Category` 之分佈形態不同 —— 最關鍵之一差。**
- 29 個：**8／28 為 `Functional Requirement`**（28.6%），
  且此 8 個即 `4821701`／`4821702`／`4821703`／`4821704`／`4821705`／`4821706`／
  `4821709`／`4821710` —— 報告 10 §7-4 所列、R-ICS39 所依之同一組。
- 87 個：**1／86 為 `Functional Requirement`**（1.2%），其餘 85 列為
  `Information` 44 ＋ `Out of Scope` 41。

**(2) 子分類 `ICS / DCSD (CFTS020)` 之標註**（報告 10 §4-4 指此欄為在案需求之標記）：
29 個側 **8 列有**（與其 8 個 FR 列完全重合）；87 個側 **1 列有**（與其 1 個 FR 列重合）。
即：**二側皆非零，但量級為 8 : 1。**

**(3) `SYS2 MD Feedback` 之內容形態不同 —— 逐字對照。**

29 個側之 FR 列（8／8 皆有 MD Feedback），逐字（節錄）：
```
NRL-402555 src=4821701  FR  04/13:HW supplier have accpted the requirement. 04/07: Analysis based on latest spec release from STLA 26PI1.6 (New Requ…
NRL-402558 src=4821704  FR  04/16: HW supplier have accepted the requirement. 04/13: Requesting the HW supplier to review the system requirement. …
NRL-402564 src=4821710  FR  04/13: HW supplier have accepted the requirement 04/07: Analysis based on latest spec release from STLA 26PI1.6 (New Req…
```
→ **形態為「HW supplier 已接受此需求」之逐條驗收留痕，8 條一致。**

87 個側之 7 列 MD Feedback，逐字（節錄）：
```
NRL-402375 src=4819216  Information  04/24: RAR solution accepted; Marking the statement as information RAR Link: …
NRL-402381 src=4819224  Information  04/24: RAR solution accepted; Marking the statement as information RAR Link: …
NRL-402415 src=4819308  Information  04/24: RAR solution accepted; Marking the statement as information RAR Link: …
NRL-402420 src=4819315  Information  （同上）
NRL-402426 src=4819338  Information  （同上）
NRL-402428 src=4819344  Information  （同上）
NRL-52850  src=4819353  Functional Requirement  [01-Dec] Noted and  updated the SW and HW scope
```
→ **6／7 之形態為「降級為 Information」之留痕，與 29 個側之「接受為需求」方向相反**；
唯一之 FR 列（`NRL-52850`）之留痕為 `Noted and  updated the SW and HW scope`，
形態上與 29 個側之 `HW supplier have accepted` 亦不同字。

**(4) 無可辨差異之欄位（列記，以求對稱）：**
- 二側皆為**逐列流水之 `Document ID`**（87 側 `-15xx`／`-16xx`，29 側 `-17xx`），
  差異僅為列序，**不具區辨力**。
- 二側之「有無對應列」比例幾乎相同（86／87 vs 28／29），
  且**二側之唯一落空者皆為 `Artifact Type = Description` 之章節引言型物件**
  （87 側 `4819365`、29 側 `4821675`）—— **此欄形態完全同型**。
- 二側之 `ID` 命名空間同為 `NRL-…`，同一分頁、同一表頭。

### 3-2 本節之限度（不裁）

- 上列 (1)(2)(3) 為**欄位形態之差異之實測**。
  **本報告不判斷該差異是否足以使 R-ICS39 之理由不及於 87 個** —— 該判斷屬範圍決定（Tier 3），為 Pei 之權。
- 同時列記反向之事實：**87 個側之 FR 與子分類標註皆非零**（各 1）。
  即「87 個全數為 SYS2 所不收」**與實測不符**。
- 報告 10 §7-4 之附註曾指出「SYS2 之**收錄哪些列**本身是同一套適用性過濾之下游，
  不具區辨力；具區辨力的是**每列之 `Category`**」。
  本次實測與該附註**方向一致**：二側皆幾近全數有列（86／87、28／29），
  差異落在 `Category`。**列記此一致，不以其為結論。**

---

## §4 反向查核：87 是否為完整集合

### 4-1 掃法

以 SYS2 之 333 列為起點反向映射（不以 87 為起點），
每列之來源 ID 逐一歸入下列互斥桶：

| 桶 | SYS2 列數 | `Category` 分佈 |
|---|---|---|
| ① 來源在 **87** 之內 | **86** | `Information` 44、`Out of Scope` 41、`Functional Requirement` 1 |
| ② 來源在 **29**（§1.18）之內 | **28** | `Out of Scope` 14、`Functional Requirement` 8、`Information` 6 |
| ③ 來源在 **138**（變體合 DUT）之內 | **135** | `Out of Scope` 61、`Functional Requirement` 47、`Information` 21、`Out of scope` 4、`Functional requirement` 1、`Heading` 1 |
| ④ 來源在 CFTS020 內但**軸層判不適用** | **11** | `Information` 10、`Heading` 1；**`Functional Requirement` 0** |
| ⑤ 來源 ID **不在** CFTS020 之 2180 物件內 | **42** | `Heading` 41、`Information` 1；**`Functional Requirement` 0** |
| ⑥ 來源欄**空白**（無 7 位 ID） | **31** | **`Functional Requirement` 23**、`Information` 3、`Out of scope` 3、`Heading` 2 |
| 合計 | **333** | |

（④ 之細分：`variant=未分類` 7 列（§1.1 ×1、§1.2 ×6）、`Disassociated` 3 列（§1.9）、
**`Associated` 1 列（§1.18，`Category=Information`）**。
⑤＋⑥ ＝ 73，與報告 10 §7-4 之「無法對映 CFTS020 者 73」相符。）

### 4-2 對本題之直接答

**問：SYS2 中是否另有本 DUT 的在案需求，其來源落在 CFTS020 的 Associated 分支
而不在這 87 個之內？**

**答：有 —— 且全部落在 §1.18，即 R-ICS39 已裁之 29 個所在之節；
除 §1.18 外，Associated 分支在 SYS2 中一列都沒有。**

實測（以 `variant_of()` 之 `Associated` 為準，即 §1.5／1.6／1.7／1.14／1.16／1.17／1.18）：

| 項 | 實數 |
|---|---|
| CFTS020 中 `variant == Associated` 之物件總數 | **262** |
| 其中 SYS2 有對應列者 | **29** |
| 該 29 個之頂層節分佈 | **§1.18 × 29**（§1.5／1.6／1.7／1.14／1.16／1.17 合計 **0**） |
| 該 29 中軸層適用者（＝ R-ICS39 之 28 有列 ＋ 1 無列） | 28 |
| 該 29 中軸層**不適用**但 SYS2 有列者 | **1**（`Category = Information`，非在案 FR） |

### 4-3 「87 是否為完整集合」之判讀範圍

- **就「軸層適用 ∧ 變體不合 DUT ∧ 範圍隨變體層」此一定義而言，87 是完整集合** ——
  以 probe 全 2180 物件逐一過濾，無遺漏（138＋29＋87 ＝ **254** ＝ 軸層適用總數；
  另以頂層節核算：§1.8 92＋§1.4 86＋§1.15 29＋§1.18 29＋§1.9 17＋§1.5 1 ＝ 254）。
- **但該定義所涵蓋者，與「Associated 分支」不是同一件事**（§2）。
  若本題之真意為「Associated 分支之 SYS2 收錄面」，
  則其完整集合為 **§1.18 之 29 個 ＋ §1.5 之 1 個**，
  而 §1.18 之 29 個 R-ICS39 已裁，§1.5 之 1 個 SYS2 無列。
  **此二讀法之落差為實測結果，本報告不擇一，一併呈報。**
- 桶⑥之 **23 列在案 `Functional Requirement` 之來源欄空白**，
  逐字檢視其 `Description` 皆為 DCSD 觸控／顯示之 HW 介面規格
  （`Display Specification for 8.4`、`DCSD is the Slave (Device). SOC I2C address: 0x12 …`、
  `During multi touch drag, All 5 touch points are sent on every message` 等），
  子分類 **16 列**為 `ICS / DCSD (CFTS020)`、**7 列**空白。
  **其無 CFTS020 來源 ID，故不落入本題之「Associated 分支」範圍。列記，不推定。**

---

## §5 E15 判定

# ⚠ E15 觸發

**判定依據（下放包 12 §停下回報條件）**：
「若量得 87 個中**有任何一個為 SYS2 所收**（門檻不設數字，只要非零），停下回報。」

「為 SYS2 所收」之三種可能讀法，**實測皆非零**：

| 讀法 | 87 個側之實數 | 非零？ |
|---|---|---|
| (i) SYS2 中**有對應列**即算收 | **86**／87 | **是** |
| (ii) 有對應列且 `Category` **非 `Out of Scope`** 即算收 | **45**（`Information` 44 ＋ `Functional Requirement` 1） | **是** |
| (iii) 有對應列且 `Category` == `Functional Requirement`（最嚴，即 R-ICS39 所依之同一形態） | **1**（`4819353` → `NRL-52850`） | **是** |

**故 E15 於三讀法下皆觸發。**
下放包未指明採何讀法，本報告**不擇一**（E9 之精神：不自行擇一），三數並呈。

**停下回報。範圍擴張屬 Pei 之決定，本報告不作任何「應否納入」之判斷、
不動任何 TC、不動任何錨、不擬條文。**

E9（條文互斥）：**未觸發** —— 本次未遇條文互斥。

---

## §6 未預料之事（呈報，不調和、不代擬條文）

1. **（最重）upstream-11 §4-3 對 87 個之分佈敘述與實測不符。**
   該處稱 87 個「分佈於 §1.5／1.6／1.7／1.14／1.16／1.17 等 Associated 分支」；
   實測為 **§1.4 × 86 ＋ §1.5 × 1**，而 §1.4 之標題為
   `Diagnosis and Recovery **Common Between Architectures** …`，
   `variant_of()` 判為**未分類**。
   成因為 `variant_fits_dut` 之定義（`== "Disassociated"`）使「未分類」與
   「Associated」**同落 `False`**，二者在 87 之計數中被合併。
   A-ICS74 之敘述亦承此（「分佈於 §1.5／1.6／1.7／1.14／1.16／1.17 等 Associated 分支」）。
   **本項使本作業之題目本身需重新界定**：
   「這 87 個 SYS2 是否也收」與「Associated 分支 SYS2 是否也收」**不是同一問**。
   建議登新異常（`A-ICS?`）。**本報告二讀法俱量，見 §4-3。**

2. **§1.4 為「架構共通」節，其 86 個軸層適用物件從未被任一裁決碰過。**
   R-ICS39 之爭點（Associated vs Disassociated）對「Common Between Architectures」
   之物件**在概念上不適用** —— 共通節本就不隨變體分支。
   而現行 probe 之 `scope` 欄對其判為「隨變體層」，
   即**把一個無變體歸屬之節，掛在變體層之下**。
   **本報告不判斷此為缺陷或為設計，只列記其為實測事實。**

3. **§1.6／1.7／1.14／1.16／1.17 之 Associated 物件無一軸層適用**（實測，§2）。
   即真正之「Associated 分支軸層適用物件」只有 §1.18（29）與 §1.5（1）二處。
   §1.5 之該一物件（`4819365`）之 `Artifact Type` 為 `Description`（章節引言），
   且 SYS2 無對應列。

4. **二側之唯一「SYS2 無對應列」者皆為 `Artifact Type = Description` 型**
   （87 側 `4819365`、29 側 `4821675`）。即 SYS2 之收錄對
   「章節引言型物件」有一致之排除行為。列記，不推定其意涵。

5. **SYS2 有 23 列在案 `Functional Requirement` 之來源欄完全空白**（§4-3），
   內容為 DCSD 觸控／顯示 HW 介面規格。這批需求**無 CFTS020 追溯來源**，
   本 feature 之任何以 CFTS020 為起點之掃描皆掃不到它們。
   下放包未預料此類。建議登為資料請求或異常（`A-ICS?`／`DR-ICS?`）。

6. **`Category` 欄有大小寫不一致之值**（`Out of Scope` / `Out of scope`、
   `Functional Requirement` / `Functional requirement`），
   出現於 138 對照組（各 4 列／1 列）。87 與 29 二側**無**此變體。
   本報告之計數對此**未作正規化合併**（逐字計）；
   若日後以 `Category` 作機檢判準，須先定正規化規則。列記。

7. 本報告所量之 `NRL-52850`（`4819353`）**在報告 10 §4-4 已逐字舉證過**，
   當時作為「DCSD 相關之在案 FR」之一例；
   本次方測出**其來源物件 `4819353` 正落在這 87 個之內**。
   即：**87 個之 SYS2 收錄，在報告 10 時已有一個實例在案，只是當時未以此角度歸類。**
   列記，不推定其對 R-ICS39 之影響。
