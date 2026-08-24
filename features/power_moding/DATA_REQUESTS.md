# DATA REQUESTS — Power Moding (FW036)

Files and answers Pei can supply that unblock or upgrade generation. Drop into
`features/power_moding/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it.

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

**本 feature 之前綴為 `DR-PMH`**（R-PMH3(b)），不與 `DR-PW` 共用序號。

| # | 主旨 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| **DR-PMH1** | CFTS009 所定之 Off Road+ power moding 行為 | **OPEN** | 1（`SWE1-HMI-PM-028`） | `Off Road Plus` 批之 1 條為 `PENDING` 佔位；**含 PENDING 之工作簿不得出貨**（§8.4.3） | **A-PMH13** | **High（交付前阻斷）** |
| **DR-PMH2** | **Power Moding State Matrix**（獨立 Excel 文件） | **OPEN** | ch 9 之 5 leaf（引 `9.1`）＋ 全 feature 之 power moding 行為 | 規格逐字稱「behavior **shall not be developed without following** the Power Moding State Matrix」——**該文件不在四份素材內** | **A-PMH14** | **High** |
| **DR-PMH3** | `SU9.)` 與 `SU9.1)` 是否應存在於 037 | **OPEN** | **0（現無 leaf）** | PDF p8 有該二需求而 SYS1／037 全無 → **不在 48 leaf 內**；其題材落在 `Disclaimer Screen` 且影響逾時語意 | **A-PMH14** | **High** |

---

## DR-PMH1（開立 2026-08-24，依 **R-PMH47(c)**）

**型別**：規格轉介之涵蓋缺口（行為定義在他規格，而該規格之交付物亦未涵蓋）。

**成對之 anomaly**：**A-PMH13**（RESOLVED —— 處置已定，本 DR 為其 (c) 項）。

**狀態**：`OPEN`

### 問題全文

> `SWE1-HMI-PM-028`（037 `Requirement Title` 為 `CFTS009 Behavior Reference`，
> 對應 SYS1 `Outline Number` **12.2**）之內文逐字為：
>
> ```
> OFF2.) Please refer to CFTS009 for complete behavior.
> ```
>
> 該需求**本身不含任何可驗證之行為**，其行為定義於 **CFTS009**。
>
> 執行層已就此做過兩輪擴查（唯讀，未修改任何他 feature 之檔案）：
>
> | 輪次 | 範圍 | 結果 |
> |---|---|---|
> | 06 包 | `features/power` 之已交付件（284 資料列，其 `spec_reference` 前綴僅 `CFTS009`／`CFTS010`） | **零命中** |
> | 07／08／09 包 | 母體 **15 個有內容交付件**、**3,023 資料列**、**11 個欄位**（含 `Remarks`／`Test Case Design Methods`／`Test Case Reference ID`／`Test Set`）、**166 個相異 Test Set 全數人工核對** | **零命中** |
>
> 即：**CFTS009 所定之 Off Road+ power moding 行為，在本專案已交付之任何
> 工作簿中皆無對應 TC。兩邊都沒有 —— 這是全案缺口，不是分工。**
>
> **請上游釋明**：
>
> 1. 該 leaf 之行為應由 **CFTS009 之 SWE 需求**涵蓋（則本報告之該列為純轉介，
>    本 feature 依 §8.4.2 判其 out of scope 並揭露，另請上游確認 CFTS009
>    側之對應 SWE 需求 id 以供追溯）；
> 2. 抑或 **本報告（037-A03 Power Moding HMI）應自行載明其行為**
>    （則請補充其可驗證之敘述，本 feature 據以撰寫 TC）。
>
> 二者擇一即可，惟**在答覆前該列只能以 `PENDING: DR-PMH1` 佔位**，
> 而**含 PENDING 之工作簿不得出貨**（§8.4.3）。

### 影響

- **Leaves served**：1（`SWE1-HMI-PM-028`）
- **Batch impact**：`Off Road Plus` 批（3 leaf）之其中 1 條為佔位列；
  其餘 2 條（`-027` 12.1「不喚醒」、`-029` 12.3「靜音」）**本身含可驗證行為**，
  不受影響。
- **交付影響**：**阻斷** —— 交付前須本 DR 結案，或由 Pei 裁定降轉。

---

## DR-PMH2（開立 2026-08-24，依 **A-PMH14** 新漏 3）

**型別**：素材缺件 —— 規格所指之外部文件不在本 feature 之素材內。
**成對之 anomaly**：**A-PMH14**。**狀態**：`OPEN`

### 問題全文

> `Power Moding HMI Logic and Flow R1 SR24 2A` 之 PDF p10 逐字載：
>
> ```
> POWER MODING STATE MATRIX: Power Moding behavior shall not be developed without
> following the Power Moding State Matrix, which is in a separate Excel document.
> If this document is not available, please request a copy from the author of this
> logic and flow document.
> ```
>
> **這是一條規範性陳述**（`shall not be developed without following …`），
> 而該 Excel **不在本 feature 之四份素材內**（036／037／SYS1 匯出／PDF）。
>
> 該註記於 **SYS1 匯出之全 52 則描述中亦不存在**（四組探針皆 0 命中）——
> 即：**若只讀 SYS1，連「有這份文件」都不會知道。**
>
> **請提供該 Excel**，或釋明其於本次交付範圍內是否為必要。

### 影響
- ch 9 之 **5 個 leaf** 引 `9.1`（Power Moding 之 PM1)–PM4)），其判讀背景
  即該狀態矩陣；p9 之矩陣表格於 SYS1 亦全缺（A-PMH14 新漏 2）。
- **不阻斷 batch 1**（`Disclaimer Screen` 不引 ch 9）；
  **阻斷 `Power Transitions` 批之 ch 9 部分**。

---

## DR-PMH3（開立 2026-08-24，依 **A-PMH14** 新漏 1）

**型別**：leaf 母體缺口 —— 規格有需求而 037 無對應列。
**成對之 anomaly**：**A-PMH14**。**狀態**：`OPEN`

### 問題全文

> PDF p8 於 `SU8.)` 之後尚有二條需求：
>
> ```
> SU9.) Pressing "Screen Off" or "Power Off" hard key will not do anything when
>       pressed during animation.
> SU9.1) Pressing Power Off or Screen Off hard keys during the splash screen(s) or
>        disclaimer will reset the timeout and the radio shall display the screen
>        the next time the screen turns on. (DCR20015)
> ```
>
> **SYS1 匯出之 `7.9` 止於 `SU8.)`，且 7.9 為 7.x 之最末則**；
> `SU9.1`／`SU9)`／`reset the timeout`／`hard keys during the splash`
> 四組探針於 SYS1 全 52 則**皆 0 命中**。
>
> 037 之 leaf 以 `HMI Source ID` 指向 outline 編號 —— **SYS1 既無該二 outline，
> 037 即無對應之 Functional Requirement 列**，故該二需求
> **不在 R-PMH1 所定之 48 leaf 之內**。
>
> **請釋明**：037 是否應含 `SU9.)` 與 `SU9.1)` 之對應需求？
> 若應含而未含，本 feature 之 leaf 母體 **48** 即為低估。

### 影響
- **題材落在 `Disclaimer Screen` 內**（按 Power Off／Screen Off 於 splash
  或 disclaimer 期間之行為）。
- **`SU9.1` 直接影響逾時語意** —— batch 1 之 `-003`（逾時路徑）與
  `-004`（Maserati 無逾時）已依 PDF 於 pre-condition／procedure 加
  「不按任何硬鍵」之限定；**該限定只能自 PDF 取得**。
- **不阻斷 batch 1 已寫之 8 條**，但**該 Test Set 之覆蓋完整性待答**。

---

### 未結 DR 清單（每包上繳須附，R-PMH47(c)）

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | **OPEN** | **交付**（§8.4.3） |
| **DR-PMH2** | Power Moding State Matrix Excel | **OPEN** | `Power Transitions` 批之 ch 9 部分 |
| **DR-PMH3** | `SU9.)`／`SU9.1)` 是否應在 037 | **OPEN** | `Disclaimer Screen` 之覆蓋完整性 |

合計未結 **3** 筆。
