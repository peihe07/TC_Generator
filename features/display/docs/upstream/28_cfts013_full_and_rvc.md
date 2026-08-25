# 上繳包 28 —— CFTS_013 全文驗明、矩陣判讀、rvc-01（007／008 六條）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/28_cfts013_full_and_rvc.md`
- **停止條件 71 觸發**（A2 之三條皆以條號錨定查無）→ **A3 停手**；
  A1／A4／A5 完成，任務 B／C 續行並完成
- 停止條件 60／72／73 皆未觸發；1–70 亦全未觸發
- **git 未執行**（§五為建議）

---

## 摘要

| 任務 | 結果 |
|---|---|
| A1 | `cfts013_doc` 入綁定，**`entries: 13`／13 of 13 match** |
| A2 | **629／633／952 三者皆查無** —— 該檔之條號**全為 7 位**（117 個相異）。停止條件 71 觸發 |
| A3 | **停手**（依 71） |
| A4 | `{CFTS013-XXX}` **0 項／0 次**；`CFTS013-967` **0 項／0 次** |
| A5 | 兩句樣板殘句於全文 **0 命中** → A-DM37 之分類不變 |
| B | **矩陣為類別制，含 0 個 PU 編號**；但**可機器化**：明序清單 ＋ N×N 表 ＋ 清單欄 5 之類別碼（94.9% 覆蓋） |
| C | `rvc-01` **六條**；lint 20 項行計 0；`check_disclosure` 雙向 0；綁定 13/13 |

**新登記**：A-DM38（release 不同期）、A-DM39（兩套編號體系）、
**DR-DM11**（倒車檔訊號，HIGH）。

---

## 一、任務 A

### 1.1 A1 —— 台帳與綁定

| 項 | 值 |
|---|---|
| 檔 | `R1LR_Atl-H_26PI2.5 Jun Release-Activation and Configuration_CFTS_013_Radio Error Management_20260608-1149.docx` |
| bytes | **520,083**（與分析層 `get_file_info` 之數相同） |
| mtime | 2026-08-25 23:04:30 |
| sha256 | `00d47c9e3bf6e4528d247921c5a82bf76f53d542bf7350ef23c127b9276c892f` |
| `reference:` 鍵 | **`cfts013_doc`**，與 `cfts013_sysra` 分列 |

```text
entries: 13
| cfts013_doc | `R1LR_Atl-H_26PI2.5 Jun Release-Activation and Configuration_CFTS_013_Radio Error Management_20260608-1149.docx` | `00d47c9e3bf6e452…` | `00d47c9e3bf6e452…` | MATCH |
| cfts013_sysra | `SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx` | `1036b2af9f655441…` | `1036b2af9f655441…` | MATCH |
**13 of 13 match.**
```

**`entries: 13`／13 of 13 match**（R-G26：綠燈連同母體）。
`entries` 由 12 增為 13 —— 若 YAML 縮排有誤，它會停在 12 而輸出仍是
「12 of 12 match」（A-DM30 之防線）。

**A-DM38（MEDIUM，新）—— release 不同期**：CFTS_013 為
`26PI2.5 Jun Release`（2026-06-08），CFTS_020 為 `26PI1.5 Mar Release`
（2026-03-10）。**CFTS_013 晚三個月且屬下一個 PI 家族。**
是否構成版本錯配屬 Tier 2，本層不逕判。
**本批不受影響** —— `rvc-01` 之值域來源為 CFTS_020 ＋ DBC，
未引 CFTS_013 之任一值（停止條件 73 實測 0）。

### 1.2 A2 —— 629／633／952 之條號錨定（**停止條件 71 觸發**）

```text
# 母體：block 走訪（段落 327 ＋ 表格 1）共 347 項；口徑『項計』

## 全檔之條號集合
  條文本體（`NNN: [Artifact Type…`）：85 個相異
  標題式（`{NNN}`）：44 個相異
  聯集 = 117 個；位數分布 = {7: 117}
  範圍 = 4819633 … 5423093
  最小十個：['4819633', '4819851', '4820282', '4821300', '4821301', '4821302', '4821303', '4821587', '4821589', '4821590']

## 目標三條之判定（R-DM52：條號錨定，非全檔子字串）
  629: **查無**（條號錨定）   ｜ 對照：`CFTS013-629` 子字串 0 項；裸 `629` 子字串 0 項／出現 0 次
  633: **查無**（條號錨定）   ｜ 對照：`CFTS013-633` 子字串 0 項；裸 `633` 子字串 1 項／出現 1 次
  952: **查無**（條號錨定）   ｜ 對照：`CFTS013-952` 子字串 0 項；裸 `952` 子字串 0 項／出現 0 次

## `CFTS013-` 之任何三位數引用（全檔）
  ['1009', '1015']
```

**三者皆查無。** 且 `629`／`952` 連裸子字串都是 0 次 ——
不是「藏在某處沒被錨到」，是**根本不在這份文件裡**。

**A-DM39（HIGH，新）—— 這不是「有沒有這一條」，是兩套編號**：
本檔之條號 **117 個相異，位數分布 100% 為 7 位**（`4819633`…`5423093`）。
一項佐證：其集合**含 `4820282`** —— 那正是 CFTS_020 `1.11.2.2` 之
`{4820282}`。**兩份文件共用同一個 7 位編號空間**（Polarion 全域 id）。

而 DR-DM4 所求之 `629`／`633`／`952` 為**另一套 3 位編號**。
求 3 位條號可能永遠查無 —— **DR-DM4 之標的須重擬**（本層建議，不逕改）。

**結構線索（供裁定，A3 已停手故未讀其內容）**：本檔有四個 DCSD 專節 ——

```text
1.5   DCSD Display Hot Error Behavior {4943077}
1.5.1 Activating the DCSD Display Hot Algorithm {4943080}
1.5.2 Standard HU and DCSD DIsplay Hot', Screen Priority and HMI Event processing {4943082}
1.5.3 Multi-stage HU and DCSD Display Hot', Screen Priority and HMI Event processing {4943095}
```

**`1.5.1` 之標題逐字即 DR-DM4 所求之「DCSD Display Hot 演算法」。**
只回報標題（結構），未抽取其內容 —— 那是 A3。

> 我判斷 A3 之停手在此有點可惜：東西看起來就在 `1.5.1`。
> **但停止條件 71 之文字是「停任務 A 後半（A3）」，沒有例外條款**，
> 而 24 包那次錯誤（以未查證之前提下指令）的教訓正是不自行開例外。
> **一句「續行 A3」即可解封，本層可於單輪內補上。**

### 1.3 A4／A5

```text
## A4 —— 佔位符與 967 之複核（口徑並列，R-G16）
  '{CFTS013-XXX}'    項計 =   0   出現次數計 =   0
  'CFTS013-XXX'      項計 =   0   出現次數計 =   0
  'XXX'              項計 =   0   出現次數計 =   0
  'CFTS013-967'      項計 =   0   出現次數計 =   0
  '967'              項計 =   0   出現次數計 =   0

  註：CFTS_020 內 `{CFTS013-XXX}` 出現 5 次（上繳 21 §A-DM33）。
      本檔為 CFTS_013 **本身**，故其內不應有指向自己的 `CFTS013-` 佔位符。

## A5 —— A-DM37 三句殘渣之全文對照
  SYSRA -1192  逐字 'The TBM shall do this or that'
        於 CFTS_013 全文：0 項命中  →  **不見於本文**
  SYSRA -1197  逐字 'The HU shall dipslay xxxxxxxx'
        於 CFTS_013 全文：0 項命中  →  **不見於本文**
  SYSRA -1194  逐字 '0'
        於 CFTS_013 全文：154 項命中  →  **見於本文**
  片語探針 'do this or that'   : 0 項
  片語探針 'dipslay'           : 0 項
  片語探針 'TBM shall'         : 0 項

## 結構（供分析層裁定 DR-DM4 之範圍；A3 已依停止條件 71 停手）
  （以上取自本文標題，非目次；目次項含 tab 已排除）

  本文標題共 16 個；與 DCSD 相關者：
    1.5 DCSD Display Hot Error Behavior {4943077}
    1.5.1 Activating the DCSD Display Hot Algorithm {4943080}
    1.5.2 Standard HU and DCSD DIsplay Hot', Screen Priority and HMI Event processing {4943082}
    1.5.3 Multi-stage HU and DCSD Display Hot', Screen Priority and HMI Event processing {4943095}
```

**A4**：本檔內 `{CFTS013-XXX}` **0 項／0 次**、`CFTS013-967` **0 項／0 次**
（口徑並列，R-G16）。即 CFTS_020 內那 5 次佔位符
**在 CFTS_013 本身找不到對應** —— 佔位符是 CFTS_020 側之未填欄，
不是 CFTS_013 側之缺頁。

**A5**：A-DM37 之兩句樣板殘句（`The TBM shall do this or that`、
`The HU shall dipslay xxxxxxxx`）於全文 **0 項命中**；
片語探針 `do this or that`／`dipslay`／`TBM shall` 亦皆 0。
→ **該三句為 SYSRA 撰寫殘渣，未升為規格本文殘渣，A-DM37 之分類不變。**
（`-1194` 之 `0` 命中 154 項為單字元比對之必然，不作數 —— 具名以免被當成證據。）

---

## 二、任務 B —— 2021 Priority Matrix 之判讀

### 2.1 B1：其**是**可機器化，但不是我原先設想的形狀

```text
# B1 —— 結構判讀
  pages = 10
  文字層字元數 = 9383（pymupdf get_text；口徑：字元計）

  ## page 1：非空行 7；前 18 行逐字
    | SR24 1° Pop-up Matrix
    | General Rules and Specifications
    | Version
    | May 3, 2021
    | HMI Team
    | Ronald Tapplin
    | Ron.tapplin@fcagroup.com
```

**它不是一張「popup id × 優先級」表，是一份「類別規則書」。**
10 頁、文字層 9,383 字元。抽樣三格：

**抽樣一（page 4）—— 明序清單，逐字**：

```text
Pop-up Categories (Priorities)
Window Pop-up priorities (higher to lower):
RVC
Cat. X
Cat. SL
Anti-Theft  (Keypad and Anti-Theft pop-ups)
Cat. 1
Display off (black curtain, which is not a pop-up but a window layer)
Cat. 2  and Cat. VR
Cat. 3
```

**抽樣二（page 10 `New Matrix Table`）—— N×N 之文字結果格**：

```text
1T
1P
N/A
Cat. SL is stacked under RVC
Cat. 1T is stacked under RVC
Overlap without waiting
```

**抽樣三（page 9）—— Cat SL 之定義**：

```text
Category SL (SOS and Legal) [2018 03 12]
– This category is maximum priority and it contains pop-ups related
  to SOS Call, Assist Call, other emergency or possible safety related
  features and information that need to be given to user due to LEGAL reasons.
```

> **一項內部不一致須具名**：page 4 之明序清單把 `Cat. SL` 排在
> `Cat. X` **之下**，而 page 9 逐字稱 SL `is maximum priority`，
> page 10 又稱 `Cat. SL is stacked under RVC`。
> 三處對 SL 之位置說法不同。**本層不裁定，記明。**

### 2.2 B2：矩陣內 **0 個 PU 編號** —— 交集為 0，但那不是壞消息

```text
# B2 —— popup id 集合
  矩陣 PDF 之 PU 編號：0 個相異
  26PI Pop Up List 之 PU 編號：1332 個相異
  交集 = 0   僅矩陣有 = 0   僅清單有 = 1332
  PU0517: 矩陣內 **無** ／ 清單內 有
  PU0130: 矩陣內 **無** ／ 清單內 有

```

`PU0517`／`PU0130` **皆不在矩陣內** —— 因為**矩陣裡沒有任何 PU 編號**。
交集 0、僅清單有 1332，這三個數字合起來說的是同一件事：
**兩份文件以不同的鍵在講話。**

**接合點在類別碼。** `Pop Up List HMI R1 (26PI).xlsx` 之 `Main` 分頁
**欄 5**（無表頭）即類別欄：

```text
## 欄 5 之表頭與覆蓋率
   欄 5 表頭 = 'None'
   PU 列數 = 1341；欄 5 非空 = 1337；值落在矩陣詞彙 = 88
   覆蓋率（矩陣詞彙／PU 列）= 88/1341 = 6.6%
   欄 5 非空但不在矩陣詞彙者之值分布（前 8）：
     '2': 1110
     '3': 73
     '---': 52
     'RVC-X': 5
     '2 SL': 4
     'Custom': 2
     'RVC\n2': 1
     '1': 1
   PU0517 欄 5 = '1T'
   PU0130 欄 5 = '1T'

## 修正後之覆蓋（前一段之 TOK 漏了裸 `1`／`2`／`3` —— 它們正是 Cat.1／2／3）
   PU 列數 = 1341
   欄 5 之值為**單一**矩陣類別者 = 1272  →  94.9%
   其餘 69 列之值分布：
     '---': 52
     'RVC-X': 5
     '': 4
     '2 SL': 4
     'Custom': 2
     'RVC\n2': 1
     '-': 1
```

**1272／1341 = 94.9% 之 popup 帶單一矩陣類別碼。**
`PU0517` 與 `PU0130` 皆為 **`1T`**（page 7 逐字：
`1T (Temperature). Overheating related pop-ups (screen, system, speaker...)`）。

即 **DR-DM2 之仲裁順序在原理上可機器化**：
matrix 之明序清單（page 4）＋ N×N 表（page 10）× 清單欄 5 之類別碼
= 每一 popup 之仲裁位置。

未覆蓋之 69 列：`---` 52、`RVC-X` 5、空 4、`2 SL` 4、`Custom` 2、
`RVC\n2` 1、`-` 1 —— 其中 `RVC-X`／`2 SL`／`RVC\n2` 為**複合值**，
須另定解析規則；`Custom`／`---` 為無類別。

### 2.3 B3：版本時差之證據 —— 問法須改

下放包 B3 問「矩陣內 id 有而 26PI 清單無者幾個、反向幾個」，
其預設是兩邊以 id 相接。**實測顯示該預設不成立**（矩陣 0 個 id），
故該對數字無法作為時差證據。

**可測之時差證據改為類別詞彙之漂移**：矩陣之六個類別 token
（`1T` 10／`1P` 9／`SL` 12／`RVC` 16／`VR` 19／`X` 20 次）
與清單欄 5 之值域**完全對得上**（`1T`／`1P`／`VR`／`X`／`RVC`／`SL`
＋裸 `1`／`2`／`3`）。

即：**2021 之矩陣與 26PI 之清單，其類別詞彙未漂移。**
矩陣以 id 無關之方式定義優先序，故 popup 之新增／刪除**不使其失效**；
會使其失效的是類別詞彙之改動，而該項實測為 0。

**這是「2021 版仍可用」之證據基礎** —— 但仍有一項未測：
**類別之語意**是否漂移（同一個 `1T` 在 2021 與 2026 是否指同一件事），
逐字比對做不到這件事。

### 2.4 B4：**未產出 `popup_priority.tsv`**

依 B4 之指定。本輪只判讀。

---

## 三、任務 C —— `rvc-01`

### 3.1 六條之十欄全文

#### #1 — `SWE1-DM-007`

| 欄 | 值 |
|---|---|
| `tc_title` | RVC requested from screen on → camera state reported |
| `specification_reference` | CFTS020-4819642 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `priority` | P1 |
| `functional_safety` | NA |
| `split_flag` | False |

```text
[test_item]
The Display Management software shall transition display state to Rear View Camera (RVC) mode when reverse gear signal is detected under static vehicle condition.The software shall restore previous display state after RVC release event.

(Entry from the steady on state — the reverse gear trigger and the HU-side signal value are deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen ON state
2. The Rear View Camera is not being displayed

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Request the Rear View Camera screen on the HU
3. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 3 (RR_CMRA)

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 1 (ON) is received
2. The HU transitions to the Rear View Camera screen
3. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 3 (RR_CMRA) is received

```

#### #2 — `SWE1-DM-007`

| 欄 | 值 |
|---|---|
| `tc_title` | RVC released with normal display → screen on state restored |
| `specification_reference` | CFTS020-4819645 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `priority` | P1 |
| `functional_safety` | NA |
| `split_flag` | False |

```text
[test_item]
The Display Management software shall transition display state to Rear View Camera (RVC) mode when reverse gear signal is detected under static vehicle condition.The software shall restore previous display state after RVC release event.

(Restore path of the steady on state — the reverse gear trigger and the HU-side signal value are deferred)

[pre_conditions]
1. The Rear View Camera is being displayed
2. The requested display intensity is a non-zero value

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Release the Rear View Camera screen on the HU
3. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 1 (ON)
4. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 3 (RR_CMRA) is received
2. The HU leaves the Rear View Camera screen
3. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 1 (ON) is received
4. The DCSD Display returns to the DCSD Screen ON state

```

#### #3 — `SWE1-DM-007`

| 欄 | 值 |
|---|---|
| `tc_title` | RVC not requested → camera state not reported |
| `specification_reference` | CFTS020-4819642 |
| `design_method` | 邊界值分析 (Boundary Value Analysis, BVA) |
| `priority` | P1 |
| `functional_safety` | NA |
| `split_flag` | True |

```text
[test_item]
The Display Management software shall transition display state to Rear View Camera (RVC) mode when reverse gear signal is detected under static vehicle condition.The software shall restore previous display state after RVC release event.

(Negative of the entry trigger — the reverse gear trigger and the HU-side signal value are deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen ON state
2. The Rear View Camera is not requested for the whole of this test

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ again after one minute and record its value

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ is not 3 (RR_CMRA)
2. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ is not 3 (RR_CMRA)

```

`split_reason`（逐字）：

> §9 第 11 項之 negative：`{4819642}` 之觸發為「HU 轉入高優先之 RVC 畫面」，本條驗其未成立時 `[RR_CMRA]` 不出現。R-DM49(c)：其證據強度與正向條不同 —— `{4819642}` 只載觸發成立時之行為，未載未成立時不發生；依 R-DM49(a)(b) 判其可寫：所否定之行為其正向出處逐字存在，且該否定未引入任何新的值


#### #4 — `SWE1-DM-008`

| 欄 | 值 |
|---|---|
| `tc_title` | RVC requested from screen off → display returns and reports camera |
| `specification_reference` | CFTS020-4819668 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `priority` | P1 |
| `functional_safety` | NA |
| `split_flag` | False |

```text
[test_item]
The Display Management software shall support dynamic transition between operational HMI screen and Rear View Camera (RVC) display during runtime conditions.The software shall ensure seamless display arbitration during active application execution and dynamic vehicle state transition.

(Arbitration from the off state — the splash abort and the HU-side signal value are deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen OFF state
2. The Rear View Camera is not being displayed

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Request the Rear View Camera screen on the HU
3. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 3 (RR_CMRA)
4. Read the backlight state of the DCSD Display and record it

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 0 (OFF) is received
2. The HU transitions to the Rear View Camera screen
3. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 3 (RR_CMRA) is received
4. The DCSD Display returns to the DCSD Screen ON state

```

#### #5 — `SWE1-DM-008`

| 欄 | 值 |
|---|---|
| `tc_title` | RVC released with zero intensity → screen off state restored |
| `specification_reference` | CFTS020-4819671 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `priority` | P1 |
| `functional_safety` | NA |
| `split_flag` | True |

```text
[test_item]
The Display Management software shall support dynamic transition between operational HMI screen and Rear View Camera (RVC) display during runtime conditions.The software shall ensure seamless display arbitration during active application execution and dynamic vehicle state transition.

(Restore path that ends in the off state — the splash abort and the HU-side signal value are deferred)

[pre_conditions]
1. The Rear View Camera is being displayed
2. The DCSD Display was in the DCSD Screen OFF state before the camera was requested

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Release the Rear View Camera screen on the HU and set the requested display intensity to zero
3. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 0 (OFF)
4. Read the backlight state of the DCSD Display and record it

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 3 (RR_CMRA) is received
2. The HU leaves the Rear View Camera screen
3. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 0 (OFF) is received
4. The DCSD Display returns to the DCSD Screen OFF state

```

`split_reason`（逐字）：

> §8.3 之狀態軸：`{4819645}`（HU 送 `[DISP_NORMAL]` 且 intensity 非零 → `[ON]`）與 `{4819671}`（HU 送 `[DISP_OFF]` 且 `[0% Intensity]` → `[OFF]`）為同一釋放動作之兩個目的態，其失效可獨立發生，故分列


#### #6 — `SWE1-DM-008`

| 欄 | 值 |
|---|---|
| `tc_title` | RVC requested during touch to turn on → camera state reported |
| `specification_reference` | CFTS020-4820265 / CFTS020-4819652 |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `priority` | P1 |
| `functional_safety` | NA |
| `split_flag` | False |

```text
[test_item]
The Display Management software shall support dynamic transition between operational HMI screen and Rear View Camera (RVC) display during runtime conditions.The software shall ensure seamless display arbitration during active application execution and dynamic vehicle state transition.

(Arbitration while a transient screen is up — the splash abort and the HU-side signal value are deferred)

[pre_conditions]
1. The DCSD Display is showing the TOUCH SCREEN TO TURN ON screen
2. The requested display intensity is a non-zero value

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Request the Rear View Camera screen on the HU
3. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 3 (RR_CMRA)

[expected_result]
1. The DCSD Display shows the TOUCH SCREEN TO TURN ON screen
2. The HU transitions to the Rear View Camera screen
3. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 3 (RR_CMRA) is received

```

### 3.2 `reasoning` 全文

```text
**007／008 之切分（本層之判斷，037 之 Static／Dynamic 無逐字對應）**：037 以 `Static`（007）／`Dynamic`（008）區分兩條，而 CFTS_020 全文 `static` **0 命中**、`dynamic` **1 命中**；SYS2 之 12 列 RVC 錨**同時錨到兩個 leaf 且錨據完全相同**（`RVC → 'Rear View Camera' @description`），**無任何區分依據**（上繳 27 前之勘查）。本層以 CFTS_020 之條文結構切分並揭露其為判斷：**007 取「前態為 DCSD Screen ON、釋放後還原回 ON」之路徑**（`{4819642}`／`{4819645}`，對應 037 之 `restore previous display state`）；**008 取「前態非 ON 或處於過渡畫面、釋放後目的態不同」之路徑**（`{4819668}` 自 OFF 進入、`{4819671}` 釋放回 OFF、`{4820265}` TOUCH SCREEN TO TURN ON 期間），對應 037 之 `dynamic vehicle state transition` 與 `seamless display arbitration`。**此切分不是規格明載，是本層依條文之前態／目的態所作之分類。**

**逐條之拼法判定（R-DM48／A-DM35 條款層級）**：本批所引之六條，其 DCSD 側逐字皆為**短拼法** ——`{4819642}`／`{4819668}`／`{4820265}`／`{4819652}` 用 `$DCSD_DISP_STAT$ = [RR_CMRA]`；`{4819645}` 用 `= [ON]`；`{4819671}` 用 `= [OFF]`。三者皆逐字解得 DBC `DIS_CENTERSTACK.DCSD_DISP_STAT` 之 `VAL_`（`3 "RR_CMRA"`／`1 "ON"`／`0 "OFF"`，`dbc_probe.py` 實測，選定判準為 `MESSAGE.Signal` 兩半皆相等），**故本批得寫 raw**。對照：`{4819632}`／`{4820250}` 用長拼法之 `[values as defined in section …]`，本批未引。**HU 側 `$TGW_DISP_STAT$` 之值一律不寫 raw**（DR-DM9(b) 未結）—— 步驟以行為描述「Request／Release the Rear View Camera screen on the HU」，ER 只驗 DCSD 側。

**架構適用性**：CFTS_020 之 RVC × `$DCSD_DISP_STAT$` 條文共 98 條，其屬性行同時含 `R1H` 與 `Atlantis High` 者 **24 條**。本批所引六條皆在其內。未取者具名：`{4819633}`／`{4819643}`／`{4819653}`／`{4819655}`／`{4819669}` 為 `PowerNet`；`{4819672}`／`{4819673}` 為 `PowerNet` 之 Stealth Mode；`{4820507}` 為 `CUSW`。

**sibling 軸（§8.3）**：007 三條之軸為 進入／還原／負向；008 三條之軸為 前態 OFF 之進入／目的態 OFF 之還原／過渡畫面期間之進入。一 TC 一驗證目標（§5.7）；單一觸發之多重後果併一條多行 ER（如 #4 之「轉回 ON 態」與「送 `[RR_CMRA]`」為同一觸發之兩個後果）。

**baseline（§5.6）**：六條之 step 1／ER 1 皆為前態之讀取 —— RVC 為狀態轉換，不記前態則無從判斷是否真的轉換過。

**Priority（§10.2）**：六條皆 **P1**。RVC 涉倒車視野，本層曾考慮 P0；惟 **R-DM46 已實測 SYS3 之 `ASIL Level` 31/31 為 `QM`、`SG ID`／`FSR ID` 全空**，無功能安全分級之依據，故不以安全性升為 P0，改以 major user-facing functionality 判 P1。`functional_safety` 六條皆 `NA`，同一依據。

**Design Method（§12）**：於步驟定稿後指派。五條為狀態轉換；#3（負向）為邊界值分析 ——其標的是觸發條件之未成立這一點本身。

**R-DM51(a) 之遵守**：本批未引 CFTS013 之任一門檻（50／51／55／56／60）；`{CFTS013-937}` 之優先序為 **HU 側**事實，本批之 RVC 優先行為一律以 CFTS_020 之DCSD 側條文為據，兩側未混引（28 包 §3.2.5）。

**未涵蓋之面向（R-G33，已於各條括號下半指名）**：007 之 `reverse gear` 觸發（DR-DM11，新開）與 HU 側訊號值（DR-DM9）；008 之 splash 中止（DR-DM1）與 HU 側訊號值。**037 之 007 逐字要求以倒車檔訊號為觸發，而本批六條之觸發一律為「RVC 被請求」** ——此為已知覆蓋缺口，交付時不得以「007 有 TC」表述其倒車檔面向已驗。
```

### 3.3 `deferred` 陣列（R-DM53 四鍵）

```json
[
  {
    "leaf_id": "SWE1-DM-007",
    "token": "reverse gear",
    "blocking_dr": "DR-DM11",
    "reason": "037 之 007 逐字為 `when reverse gear signal is detected under static vehicle condition`，而 CFTS_020 之 RVC 諸條一律以抽象之 `if the Rear View Camera is to be displayed` 為觸發，**受裁素材內查無倒車檔訊號**。2021 Priority Matrix p8 有 `Gear in R`，惟其為 HU 側 HMI 文件，依 28 包 §3.2.5 不得混引。DR-DM11 開立"
  },
  {
    "leaf_id": "SWE1-DM-007",
    "token": "HU-side signal value",
    "blocking_dr": "DR-DM9",
    "reason": "`$TGW_DISP_STAT$ = [DISP_REAR_CAMERA]`／`[DISP_NORMAL]` 之 raw 值未逐字解得 `TGW_DISP_STATSts` 之 `VAL_`（DR-DM9(b)）。步驟以行為描述請求／釋放 RVC，ER 只驗 DCSD 側之訊號值"
  },
  {
    "leaf_id": "SWE1-DM-008",
    "token": "HU-side signal value",
    "blocking_dr": "DR-DM9",
    "reason": "同 007；本 leaf 之三條亦不寫 HU 側訊號值"
  },
  {
    "leaf_id": "SWE1-DM-008",
    "token": "splash abort",
    "blocking_dr": "DR-DM1",
    "reason": "`{4819635}`（Splash/Disclaimer 期間請求 RVC → 中止 splash）之時段定義轉指 `{CFTS009-722}`，DR-DM1 未結，該時段無從建立前置條件"
  }
]
```

### 3.4 三項機器檢查

**(1) `lint036.py --profile display`**（母體 6 筆，拋棄式複本，
母本 sha 前後皆 `6372fb6be02f48dc…`）：

```text
# lint036 報告：lint_rvc.xlsx

- 來源：`/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/e90244b2-6851-4dfb-8775-8cb1bd4f77d3/scratchpad/lint_rvc.xlsx`（唯讀）
- 資料列數：6
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`display`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |

**總計：行計 0**（列計不加總——同一列可觸發多項檢查）

## 明細

```

**二十項行計皆 0。** `I-sibling` 於本批**有母體**（兩個 leaf 各 3 筆），
0 為實測 —— 六條之括號下半逐字相異（§3.4(3)）。

**(2) `check_disclosure.py`**（雙向）：

```text
# R-G33(c) 雙向檢查（R-G33(d)(2)；乙案 R-DM54）
batch: generated/rvc-01.json
tcs: 6   deferred entries: 4   （未解除 4 / 已解除 0）

| TC | leaf | token | 項之狀態 | 方向 | 判定 |
|---|---|---|---|---|---|
| #1 | SWE1-DM-007 | `reverse gear` | 未解除 | MISSING | 含 |
| #1 | SWE1-DM-007 | `HU-side signal value` | 未解除 | MISSING | 含 |
| #2 | SWE1-DM-007 | `reverse gear` | 未解除 | MISSING | 含 |
| #2 | SWE1-DM-007 | `HU-side signal value` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-007 | `reverse gear` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-007 | `HU-side signal value` | 未解除 | MISSING | 含 |
| #4 | SWE1-DM-008 | `HU-side signal value` | 未解除 | MISSING | 含 |
| #4 | SWE1-DM-008 | `splash abort` | 未解除 | MISSING | 含 |
| #5 | SWE1-DM-008 | `HU-side signal value` | 未解除 | MISSING | 含 |
| #5 | SWE1-DM-008 | `splash abort` | 未解除 | MISSING | 含 |
| #6 | SWE1-DM-008 | `HU-side signal value` | 未解除 | MISSING | 含 |
| #6 | SWE1-DM-008 | `splash abort` | 未解除 | MISSING | 含 |

MISSING = 0   STALE = 0
```

**MISSING 0／STALE 0**，12 個 (TC × token) 組合逐一列出。

**(3) canon 側之機器檢查**：

```text
population: generated/rvc-01.json, tcs = 6

--- tc_title（canon 4.3：2–14 字）與相異 ---
  #1 words=9 :: RVC requested from screen on → camera state reported
  #2 words=10 :: RVC released with normal display → screen on state restored
  #3 words=8 :: RVC not requested → camera state not reported
  #4 words=11 :: RVC requested from screen off → display returns and reports camera
  #5 words=10 :: RVC released with zero intensity → screen off state restored
  #6 words=11 :: RVC requested during touch to turn on → camera state reported
  distinct = 6 of 6

--- I-sibling：同 leaf 之括號下半逐字比對 ---
  SWE1-DM-007: 3 筆，逐字重複 = 0
    #1 (Entry from the steady on state — the reverse gear trigger and the HU-side signal value are deferred)
    #2 (Restore path of the steady on state — the reverse gear trigger and the HU-side signal value are deferred)
    #3 (Negative of the entry trigger — the reverse gear trigger and the HU-side signal value are deferred)
  SWE1-DM-008: 3 筆，逐字重複 = 0
    #4 (Arbitration from the off state — the splash abort and the HU-side signal value are deferred)
    #5 (Restore path that ends in the off state — the splash abort and the HU-side signal value are deferred)
    #6 (Arbitration while a transient screen is up — the splash abort and the HU-side signal value are deferred)

--- test_item 上半 tokens（lint L 閾值 50）---
  #1 tokens=34
  #2 tokens=34
  #3 tokens=34
  #4 tokens=36
  #5 tokens=36
  #6 tokens=36

--- Procedure ↔ ER 1:1 ---
  #1 proc=3 er=3 match=True
  #2 proc=4 er=4 match=True
  #3 proc=2 er=2 match=True
  #4 proc=4 er=4 match=True
  #5 proc=4 er=4 match=True
  #6 proc=3 er=3 match=True

--- 停止條件 54（ER 中未解析之值標籤）／55（PC 中之動作動詞）---
  54 hits = 0   55 hits = 0

--- 停止條件 60（CFTS013 之門檻出現於 DCSD 標的）---
  hits = 0

--- 停止條件 73（引 CFTS_013 全文之值）---
  specification_reference 含 CFTS013 者 = 0

--- 四欄之行尾句號／方括號（canon 11）---
  行尾句號 = 0   方括號 = 0

--- 訊號寫法（R-1 v3；lint P 檢查之對象）---
  #1 signals=['$DIS_CENTERSTACK.DCSD_DISP_STAT$']  raw=[('1', 'ON'), ('3', 'RR_CMRA')]
  #2 signals=['$DIS_CENTERSTACK.DCSD_DISP_STAT$']  raw=[('1', 'ON'), ('3', 'RR_CMRA')]
  #3 signals=['$DIS_CENTERSTACK.DCSD_DISP_STAT$']  raw=[]
  #4 signals=['$DIS_CENTERSTACK.DCSD_DISP_STAT$']  raw=[('0', 'OFF'), ('3', 'RR_CMRA')]
  #5 signals=['$DIS_CENTERSTACK.DCSD_DISP_STAT$']  raw=[('0', 'OFF'), ('3', 'RR_CMRA')]
  #6 signals=['$DIS_CENTERSTACK.DCSD_DISP_STAT$']  raw=[('3', 'RR_CMRA')]
```

### 3.5 停止條件 72 之判定（追溯斷裂）

**未觸發，但其判準在本批不適用，須具名。**

72 之文字為「leaf 引之章節在 SYS2 無對應列」。實測：
**037 之 007／008 兩條需求文皆不引任何章節**（R-DM27 已實測八條之
外部引用 0/8），故該判準無標的。

而 SYS2 側之實況是另一回事：**12 列 RVC 全部同時錨到 007 與 008，
錨據完全相同**（`RVC → 'Rear View Camera' @description`）。
**不是斷裂，是不可區分。** 兩者之風險不同 ——
斷裂會使追溯欄寫不出來，不可區分則會讓人**以為**追溯成立。

此即 §3.6 之切分須揭露為判斷之原因。

### 3.6 007／008 之切分 —— **本層之判斷**

| 查法 | 實測 |
|---|---|
| CFTS_020 全文 `static` | **0 命中** |
| CFTS_020 全文 `dynamic` | **1 命中** |
| SYS2 之 12 列 RVC | 同時錨到兩個 leaf，錨據相同 |

**受裁素材內無任何 Static／Dynamic 之區分依據。** 本層之切分：

| leaf | 取用之路徑 | 條文 | 037 之對應語 |
|---|---|---|---|
| **007** | 前態 `DCSD Screen ON`、釋放後還原回 ON | `{4819642}`／`{4819645}` | `restore previous display state` |
| **008** | 前態非 ON 或過渡畫面、釋放後目的態不同 | `{4819668}`／`{4819671}`／`{4820265}` | `dynamic vehicle state transition`／`seamless display arbitration` |

**這是分類，不是引述。** 若上游另有定義，本批須重審。

### 3.7 架構適用性

CFTS_020 之 RVC × `$DCSD_DISP_STAT$` 條文共 **98 條**，
屬性行同時含 `R1H` 與 `Atlantis High` 者 **24 條**。本批六條皆在其內。

未取者具名：`{4819633}`／`{4819643}`／`{4819653}`／`{4819655}`／
`{4819669}` 為 `PowerNet`；`{4819672}`／`{4819673}` 為 `PowerNet` 之
Stealth Mode；`{4820507}` 為 `CUSW`。

### 3.8 已知覆蓋缺口 —— **DR-DM11（新，HIGH）**

**037 之 007 逐字要求 `when reverse gear signal is detected under static
vehicle condition`，而 CFTS_020 之 24 條適用條文一律寫
`if the Rear View Camera is to be displayed`** —— 全文查無倒車檔訊號。

故本批六條之觸發一律為「RVC 被請求」。**交付時不得以「007 有 TC」
表述其倒車檔面向已驗。**

2021 Priority Matrix page 8 有逐字之
`Triggering conditions can be: 1) Gear in R 2) HU soft button press` ——
**看得到而不能用**：其為 HU 側 HMI 文件，依 28 包 §3.2.5 與 R-DM51
之分寸不得混引。**這是本輪最想抄而沒抄的一句。**

---

## 四、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A／組 B 何者為準 | 004 popup 側；005 關閉側 | DR-DM10(a) |
| A2 | DCSD 側 warning → off 之分段變數與第二門檻 | 原 pilot #2；`PU0130` | DR-DM10(b) |
| A3 | 長拼法標籤與 HU 側 `$TGW_DISP_STAT$` 之值 | `{4820287}`；`rvc-01` 六條之 HU 側 | DR-DM9 |
| A4 | `popup_priority.tsv`（仲裁順序表） | `SWE-DM-006` | DR-DM2（**本輪判讀：原理上可機器化**） |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |
| **A9** | **倒車檔訊號與 `static vehicle condition` 之判準** | **007 之觸發面向** | **DR-DM11（新，HIGH）** |
| **A10** | **DR-DM4 之標的須重擬（3 位 vs 7 位編號）** | DR-DM4 之答覆本身 | **A-DM39** |

A9／A10 為本輪新增。**A4 之可行性本輪大幅提升**（判讀完成，待裁降級）。

### B 類 —— 不阻斷交付

| 編號 | 項 | 狀態 |
|---|---|---|
| B1–B10、B12–B16 | 見上繳 25／26／27 | 不變 |
| **B17** | **矩陣對 `Cat. SL` 之位置三處說法不同**（p4 在 X 之下／p9 稱 maximum／p10 稱 stacked under RVC） | 本批未用矩陣；`SWE-DM-006` 動工時須先裁 |
| **B18** | **矩陣類別之語意漂移未測** | 逐字比對只能證明詞彙未變，不能證明 `1T` 在 2021 與 2026 指同一件事 |
| **B19** | **清單欄 5 之 69 列複合／無類別值** | `RVC-X` 5、`2 SL` 4、`RVC\n2` 1 須另定解析規則；`---` 52、`Custom` 2 為無類別 |
| **B20** | **CFTS_013 `1.5.1` 之內容未讀** | A3 依停止條件 71 停手；一句「續行 A3」即可解封 |

B17–B20 為本輪新增。

---

## 五、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/feature.yaml \
  features/display/generated/rvc-01.json \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/28_cfts013_full_and_rvc.md \
  features/display/docs/upstream/28_cfts013_full_and_rvc.md
```

```text
feat(display): add the RVC batch, and find that CFTS_013 uses other clause numbers

- add rvc-01: six test cases over SWE1-DM-007 and SWE1-DM-008, all six
  writing the DCSD signal value because every clause they cite uses the
  short spelling that resolves against the DBC
- split 007 from 008 by entry and exit state, since neither the spec nor the
  SYS2 rows distinguish static from dynamic, and record that as a judgement
- open DR-DM11: the leaf asks for a reverse gear trigger and the spec only
  ever says the camera is to be displayed
- bind the CFTS_013 workbook, taking the reference set to thirteen
- record A-DM39: that document numbers its clauses with seven digits and
  shares the numbering space with CFTS_020, so the three-digit clauses
  DR-DM4 asks for are a different scheme, not missing content
- record A-DM38: CFTS_013 is a release family later than CFTS_020
- read the 2021 priority matrix: it carries no popup ids at all, it ranks
  categories, and the pop-up list carries a category on 1272 of 1341 rows
- lint036 --profile display: all twenty checks report zero
```

> `batches/rvc-01/batch_context.md` 不入 pathspec（`.gitignore` 已排除）。
> `generated/pilot-01.json` 未變更，不入。036 母本未變更，亦不入。

---

## 六、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **007／008 之切分是我做的分類，而它決定了六條 TC 的歸屬。**
   §3.6 已揭露，但揭露不等於正確。**最壞情況是上游的 Static／Dynamic
   指的是別的軸**（例如車速為零 vs 行進中），那六條的 leaf 欄全錯 ——
   TC 內容仍成立，追溯欄全錯。**這是本批風險最集中的一處。**

2. **CFTS_013 `1.5.1` 就在那裡，而我沒讀。**
   停止條件 71 說停 A3，我停了。**但我知道 DR-DM4 想要的東西很可能
   在那一節裡**，而 DR-DM4 已經開了三輪。B20 記了此事 ——
   這是「守規則」與「把事做完」之間我選了前者，且我認為選對了，
   **但代價是真的**。

3. **矩陣之 `Cat. SL` 三處說法不同，我只記不裁（B17）。**
   那是對的（Tier 2）。**但 `SWE-DM-006` 之全部價值就是仲裁順序**，
   而其權威文件內部就不一致 —— **DR-DM2 即使答覆了，這個不一致仍在。**
   我判斷這件事應該現在就讓上游知道，不要等到 006 動工。
