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

### 未結 DR 清單（每包上繳須附，R-PMH47(c)）

| DR | 狀態 | 阻斷交付 |
|---|---|---|
| **DR-PMH1** | **OPEN** | **是** |

合計未結 **1** 筆。
