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
| **DR-PMH1** | CFTS009 所定之 Off Road+ power moding 行為 | **`CLOSED`**（R-PMH72；**歷程中從未 `SENT`**） | 1（`SWE1-HMI-PM-028`） | `Off Road Plus` 批之 1 條為 `PENDING` 佔位；**含 PENDING 之工作簿不得出貨**（§8.4.3） | **A-PMH13** | **High（交付前阻斷）** |
| **DR-PMH2** | **Power Moding State Matrix**（獨立 Excel 文件） | **`CLOSED`**（R-PMH73；**歷程中從未 `SENT`**）⚠ 見 §DR-PMH2 之落地複驗與 A-PMH18 | ch 9 之 5 leaf（引 `9.1`）＋ 全 feature 之 power moding 行為 | 規格逐字稱「behavior **shall not be developed without following** the Power Moding State Matrix」——**該文件不在四份素材內** | **A-PMH14** | **High** |
| **DR-PMH3** | `SU9.)` 與 `SU9.1)` 是否應存在於 037 | **`CLOSED`**（R-PMH74；**歷程中從未 `SENT`**） | **0（現無 leaf）** | PDF p8 有該二需求而 SYS1／037 全無 → **不在 48 leaf 內**；其題材落在 `Disclaimer Screen` 且影響逾時語意 | **A-PMH14** | **High** |
| **DR-PMH5** | **PDF p9 之能力矩陣**之來源文件 | **`DRAFT`**（R-PMH83 已授權發出，**待 Pei 告知實際發出日期與對象**） | ch 9 之 5 leaf（引 `9.1`） | **ch 9 不得開批** —— 已提供之 `DCR21421` State Matrix 為**另一主題之矩陣**，不含 p9 之內容（A-PMH18） | **A-PMH18** | **High（阻斷 ch 9 開批）** |

---

## DR-PMH1（開立 2026-08-24，依 **R-PMH47(c)**）

**型別**：規格轉介之涵蓋缺口（行為定義在他規格，而該規格之交付物亦未涵蓋）。

**成對之 anomaly**：**A-PMH13**（RESOLVED —— 處置已定，本 DR 為其 (c) 項）。

**狀態**：`CLOSED-BY-RULING`（2026-08-24，**R-PMH72** —— Pei「DR-PMH1 拿掉」；未答覆而結案）

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
**成對之 anomaly**：**A-PMH14**。**狀態**：`RESOLVED（素材已到）`（2026-08-24，**R-PMH73**）
**⚠ 惟其內容與 PDF p9 不對應 —— 見文末「DR-PMH2 之落地複驗」**

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
**成對之 anomaly**：**A-PMH14**。**狀態**：`CLOSED-BY-RULING`（2026-08-24，**R-PMH74** —— Pei「037 沒有納入就不放」）

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

**狀態欄自 21 包起用 R-PMH82 之四級**：`DRAFT`／`SENT`／`ANSWERED`／`CLOSED`。
**未記載發出日期與對象者，一律為 `DRAFT`，不得稱「已發」。**

| DR | 主旨 | 狀態 | 發出日期 | 發出對象 | 管道 | 結案依據 | 阻斷 |
|---|---|---|---|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | **`CLOSED`** | **（從未發出）** | — | — | R-PMH72 | 解除 |
| **DR-PMH2** | Power Moding State Matrix Excel | **`CLOSED`** | **（從未發出）** | — | — | R-PMH73 | ⚠ 其素材與 p9 不對應（A-PMH18）→ 另開 `DR-PMH5` |
| **DR-PMH3** | `SU9.)`／`SU9.1)` 是否應在 037 | **`CLOSED`** | **（從未發出）** | — | — | R-PMH74 | 解除 |
| **DR-PMH4** | outline 9.1 之 PDF 破句何者為權威 | **`CLOSED`** | **（從未發出）** | — | — | R-PMH75 | 解除 |
| **DR-PMH5** | **PDF p9 之能力矩陣**之來源文件 | **`DRAFT`** | **（待填）** | （待填） | （待填） | — | **ch 9 開批** |
| **DR-PMH6** | RVC 情境下 HVAC popup 之規格依據 | **`DRAFT`** | **（待填）** | （待填） | （待填） | — | **否**（R-PMH80 已以限縮＋揭露解除） |

**合計未結 2 筆（`DR-PMH5`／`DR-PMH6`），二者皆為 `DRAFT`。**

**R-PMH82 之回溯記明**：`DR-PMH1`～`4` 自 2026-08-24 開立起，
經執行層於**六個往返連續重申**而其狀態欄始終為 `OPEN` ——
**該欄無法分辨「登記了」與「發出了」**，致「尚未發出」這件事
沒有任何欄位承載它。四者最終由 Pei 之裁定結清，**歷程中從未 `SENT`**。

**`DR-PMH5`／`DR-PMH6` 已由 Pei 於 2026-08-25 授權發出（R-PMH83）**，
其可寄出全文見 `docs/handoff/21a_dr_dispatch.md` §三，
並轉錄於本檔 §五、§六。**執行層不得代為發出**；
Pei 告知實際日期與對象後，狀態方改 `SENT` ——
**不得以下放包之日期充當發出日期。**


---

## 四、Pei 之裁定逐字（2026-08-24）

```
DR-PMH1 拿掉
DR-PMH2 /Users/peihe/Work_Projects/TC_Generator/features/power_moding/inputs/Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421 (August 3 2022).xlsx
DR-PMH3 037沒有納入就不放
DR-PMH4 以刪掉之後的為主
```

**DR-PMH1 之「拿掉」採 19a §1.1 之解讀（乙）** —— 該列不放進工作簿，
非「該 DR 不發」。**若原意為（甲），一句話即可反轉**（其差別：（甲）該列仍寫入
並以 `PENDING` 佔位、交付前仍阻斷）。**執行層據此執行，並在此具名該解讀。**

---

## DR-PMH4（開立並同輪結案，2026-08-24）

**型別**：來源本身損壞（R-PMH69）——**兩個來源皆不可逕信**。

**問題**：outline `9.1` 之 PDF 原句含 `aofnd`（非英文字）、
`the radio should shut Off the popup should close`（兩主謂相連無連接詞）、
`within 60 seconds the timeout defined in pop-up list`（兩時間條件並列無連接詞）
—— 形態為一次未完成之編輯，舊文字與新文字疊寫。
SYS1 之版本恰好刪去該兩段舊文字並將 `aofnd` 改回 `if`。

**裁定（R-PMH75）**：「以刪掉之後的為主」→ **SYS1 為權威**，R-PMH50 於 9.1 反轉。

**承擔之風險已具名**：`the radio should shut Off`（逾時後收音機關機）
**不會有任何一條 TC 驗到**。

---

## DR-PMH2 之落地複驗（19 包步驟 8）—— **⚠ 素材已到，惟其內容與 p9 不對應**

`shasum -c` **6/6 OK**（第六筆素材已入 `MANIFEST.sha256`）。

| 項 | 值 |
|---|---|
| 檔名 | `Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421 (August 3 2022).xlsx` |
| SHA256 | 見 `inputs/MANIFEST.sha256` |
| 分頁 | `Title`／`State Matrix`／`SR24 Change Log` |
| `State Matrix` 之非空列 | 43 列、362 個非空格 |
| Title 之版本 | `SR24 2A (post). CR21421`／`August 3rd 2022` |
| Change Log 之末筆 | `SR24 2A DCR21421`／**2021-10-20** |

### **矩陣之軸與 PDF p9 之軸不對應 —— 逐字探針全 0**

| PDF p9 之標籤 | 於 State Matrix |
|---|---|
| `HEADUNIT POWER` | **0** |
| `ICS Hard Controls` | **0** |
| `HVAC Knobs` | **0** |
| `Climate GUI` | **0** |
| `ENGINE ON`／`ENGINE OFF` | **0** |
| `Power Button only is functional` | **0** |
| `Fully functional` | **0** |
| `Power Accessory Delay`／`accessory delay` | **0** |
| `FOTA`／`Charge Now`／`stay awake` | **0** |

**該 Excel 之軸為**：`Key-on`／`Key-off`／`Key On Gear≠Reverse` 三個區塊
× `Turn Off @ door opening Enabled/Disabled` × `HU on/off`
× `Call Active/Not Active` × `Door Open/Closed`；列為事件
（`ON/OFF button Pressed`／`Door opened`／`Incoming Call`／`Call Ended` …）。

**PDF p9 之矩陣為**：`HEADUNIT POWER OFF`／`ON` ×
`ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit`，
列為 `KEY ON ENGINE ON`／`KEY OFF (ACC)`／`KEY OFF (No ACC)`。

**二者為兩個不同的矩陣。**

### 依 R-PMH73 之明文「不一致者不得自行取捨，停並上呈」—— **停手上呈**

**未執行之事（具名）**：

1. **A-PMH14 之新漏 2 未改為 `RESOLVED（來源已補）`** ——
   該狀態之前提為「內容在另一份素材裡」，而實測**不在**。
   逕改會使 `ANOMALIES.md` 出現一句不實陳述（R-PMH43／R-PMH63）。
   **其狀態改為 `PENDING（來源已到，惟內容不對應）`。**
2. **新漏 3（p10 之 `POWER MODING STATE MATRIX:` 段）之狀態已改為
   `RESOLVED（來源已補）`** —— 該段之內容即「矩陣存在於一份獨立 Excel」，
   **該 Excel 確已到齊**，其前提成立。二者不同，故分別處置。

**版本落差之具名（R-PMH73 明文要求）**：
Excel 為 `DCR21421`／2022-08-03，PDF 為 `DCR22412`／2023-01-24 —— **Excel 較早**。
且其 Change Log 之末筆為 **2021-10-20**，**未及 2022-08-03**，
亦即該檔之變更紀錄與其自稱之日期亦不一致。

**待 Pei**：p9 之矩陣是否另有一份文件？或 p9 之矩陣即為 PDF 自身之摘要而
Excel 為另一主題（開機／關機事件轉移）之矩陣、二者本不對應？
**不自行取捨。**

---

## DR-PMH5（開立 2026-08-24，依 **R-PMH76**）

**型別**：規範性文件之缺件 —— 規格所引之矩陣**存在**，惟所提供者為另一份。

**成對之 anomaly**：**A-PMH18**。**狀態**：`OPEN`。**阻斷 ch 9 開批。**

### 問題全文

PDF p9 之 `Power Moding` 節含一張**靜態能力矩陣**，其後緊接一句
`Please refer to Power Moding State Matrix for further specifications.`
該矩陣於 SYS1 匯出中**整表缺失**（A-PMH14 新漏 2），
**且該句本身於 SYS1 全 52 則命中 0**。

2026-08-24 所提供之
`Power Moding HMI State Matrix R1 SR24 Post 2A DCR21421 (August 3 2022).xlsx`
**不含該矩陣之內容** —— 已做**逐字**與**語意**兩層對照，二者皆不涵蓋：

| | **PDF p9 之矩陣** | **所提供之 Excel** |
|---|---|---|
| 型別 | **靜態能力表** | **事件驅動之狀態轉移表** |
| 列軸 | 電源狀態：`KEY ON ENGINE ON`／`KEY OFF (ACC)`／`KEY OFF (No ACC)` | **事件**：`ON/OFF button Pressed`／`Door opened`／`Incoming Call`／`Gear changes to Reverse`／`Screen Off Button Pressed` … |
| 欄軸 | 受控對象：`ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`／`Headunit`，各分 `HEADUNIT POWER OFF`／`ON` | **情境條件**：`Turn Off @ door opening Enabled/Disabled` × `HU on`／`HU off`／`Power Button OFF` × `Call Active/Not Active` × `Door Open/Closed`（另一區塊為 `Screen Off × Mute × Gear`） |
| 格內容 | **是否可用**（`Fully functional`／`Not Visibile due to power off`） | **轉移後之結果**（`Event ignored`／`Radio Wakes Up and mutes` …） |
| 區塊 | 單一表 | **三塊**：`Key-on`（列 1–16）／`Key-off`（19–33）／`Key On, Gear ≠/= Reverse`（37–48） |

**逐字探針十三個全 0 命中**：`HEADUNIT POWER`／`ICS Hard Controls`／`HVAC Knobs`／
`Climate GUI`／`ENGINE ON`／`ENGINE OFF`／`Power Button only is functional`／
`Fully functional`／`Power Accessory Delay`／`accessory delay`／`FOTA`／
`Charge Now`／`stay awake`。

**語意層亦不涵蓋**：Excel 之 `HU on`／`HU off`／`Power Button OFF` 是**情境條件**，
不是 p9 之「受控對象在該電源狀態下是否可用」；
Excel 全簿無任何一格描述 `ICS Hard Controls`／`HVAC Knobs`／`Climate GUI`
三者之可用性。

### 所需

**PDF p9 那張能力矩陣之可讀來源**：其原始檔，或該矩陣所在頁之高解析輸出。

### 其影響

`9.1` 之 5 個 leaf（`SWE1-HMI-PM-018-01` ～ `-05`，`Power Transitions` 組）
其判讀背景不完整。**R-PMH75 已定 `9.1` 之 `source_clause` 取自 SYS1，
惟 SYS1 之 `9.1` 只有 `PM1)` 之散文，不含該矩陣。**

### 版本落差（一併回報）

| 文件 | DCR | 日期 |
|---|---|---|
| 所提供之 Excel | `DCR21421` | **2022-08-03**（Title 分頁自載） |
| 規格 PDF | `DCR22412` | 2023-01-24 |

**Excel 較早**，且其 `SR24 Change Log` 之末筆為 **2021-10-20**，未及其自稱日期。

---

## DR-PMH6（開立 2026-08-25，依 **R-PMH80(b)**）

**型別**：規範性素材有載而規格未載，且與規格之全稱句字面牴觸。

**成對之 anomaly**：`10.3` 之牴觸（20 包 §4.2 查出，R-PMH80 處置）。
**狀態**：`DRAFT`（R-PMH83 已授權發出，待 Pei 告知實際日期與對象）。
**不阻斷** —— `Power Off Behavior` 組已由 R-PMH80 以「限縮 ＋ 揭露」解除。

### 問題摘要

| | 逐字 |
|---|---|
| 規格 `PITA6`（outline 10.3） | `HVAC pop-ups shall be temporarily displayed during Power Button Off state.`（**全稱句，無例外**） |
| 矩陣 `r48c10`（`Key On, Gear = Reverse` × `Power Button State = OFF`） | `Popup not displayed over RVC` |

**執行層曾提「以 `PITA4` 建立之倒車影像優先原則調和」，該調和不採**（R-PMH80）：
`PITA4` 之逐字為 `Screen Off and HU Power button **selections** shall be ignored
while backup cam is being shown.` —— **其對象為使用者之按鍵輸入，非 popup 之顯示**。

### 處置（R-PMH80，不待答覆即生效）

(a) `10.3` 之 TC 於 Pre-Condition 加「倒車影像未顯示（`Gear != Reverse`）」，
    依 R-PMH55 之形態限縮，來源於 `reasoning` 具名；
(b) RVC 情境之行為**只在矩陣有、規格未載**，依 R-PMH55(b) 不撰 TC，
    **登記為覆蓋缺口**。

---

## 五、`DR-PMH5` 之可寄出全文（R-PMH83 授權，**執行層不得代為發出**）

```text
Subject: Power Moding HMI — request for the source of the capability matrix on page 9

Hello,

We are preparing the SWE.6 test cases for Power Moding HMI
(FM-WI-FSM-037-A03-N1L-SWE1-PowerModing-HMI-V0.1, based on
"Power Moding HMI Logic and Flow R1 SR24 2A DCR22412 (January 24 2023)").

Page 10 of the logic and flow document states, verbatim:

    POWER MODING STATE MATRIX: Power Moding behavior shall not be developed
    without following the Power Moding State Matrix, which is in a separate
    Excel document. If this document is not available, please request a copy
    from the author of this logic and flow document.

We have received a file named "Power Moding HMI State Matrix R1 SR24 Post 2A
DCR21421 (August 3 2022).xlsx". However, it does not appear to correspond to
the matrix printed on page 9 of the logic and flow document. The two differ in
structure:

  Page 9 matrix
    Rows    : KEY ON ENGINE ON / KEY OFF (ACC) / KEY OFF (No ACC)
    Columns : ICS Hard Controls / HVAC Knobs / Climate GUI / Headunit,
              each split by HEADUNIT POWER OFF and HEADUNIT POWER ON
    Cells   : whether the item is available in that power state

  Excel "State Matrix" sheet
    Blocks  : Key-on / Key-off / Key On, Gear <> Reverse
    Rows    : events (ON/OFF button Pressed, Door opened, Incoming Call,
              Plug in Projection, VR button long press, Call Ended,
              SRT or Off Road+ Hard Button press, Screen Off Button Pressed,
              Mute Button Pressed, HVAC Hard Control Adjustment, ...)
    Columns : context conditions (Turn Off @ door opening Enabled/Disabled,
              HU on / HU off / Power Button OFF, Call Active/Not Active,
              Door Open/Closed)
    Cells   : the resulting state after the event

We searched the Excel file for the terms used on page 9. The following strings
return zero matches across all 362 non-empty cells:

    HEADUNIT POWER, ICS Hard Controls, HVAC Knobs, Climate GUI,
    ENGINE ON, ENGINE OFF, Power Button only is functional,
    Fully functional, Power Accessory Delay, accessory delay,
    FOTA, Charge Now, stay awake

No cell in the Excel file describes the availability of ICS Hard Controls,
HVAC Knobs or Climate GUI in a given power state.

We also note that the page 9 matrix is absent from the SYS1 structured export
of this document, so it is not available to us in any machine-readable form.

Could you please clarify one of the following:

  (1) Is there a separate document that contains the page 9 capability matrix,
      and if so may we have a copy; or

  (2) Is the page 9 matrix itself the authoritative source for that content,
      with the DCR21421 Excel covering a different subject (event-driven power
      state transitions)?

Until this is clarified we have suspended test case authoring for section 9
(Power Moding), which covers 5 requirements (SWE1-HMI-PM-018-01 through -05).

One further observation, offered for your information only: the change log in
the DCR21421 Excel ends at 2021-10-20, which is earlier than the August 3 2022
date given on its own title sheet.

Thank you,
```

---

## 六、`DR-PMH6` 之可寄出全文（R-PMH83 授權，**執行層不得代為發出**）

```text
Subject: Power Moding HMI — PITA6 and the state matrix appear to conflict for the reverse camera case

Hello,

While preparing the SWE.6 test cases for Power Moding HMI we found what appears
to be a conflict between the logic and flow document and the Power Moding State
Matrix. We would rather ask than choose one of them.

The logic and flow document, section "Additional Power Moding Behavior Notes",
states verbatim:

    PITA6: HVAC pop-ups shall be temporarily displayed during Power Button Off
    state.

This is written without exception.

The Power Moding State Matrix ("State Matrix" sheet, block "Key On, Gear =
Reverse", row "HVAC Hard Control Adjustment", column "Power Button State = OFF")
states verbatim:

    Popup not displayed over RVC

For the case where the vehicle is in reverse and the reverse camera is being
shown, these two cannot both hold: PITA6 says the HVAC pop-up is displayed
during Power Button Off state, and the matrix says it is not displayed over the
reverse camera view.

We considered reading PITA6 as a general rule with the reverse camera as an
exception, on the basis of PITA4. However PITA4 reads, verbatim:

    PITA4: Screen Off and HU Power button selections shall be ignored while
    backup cam is being shown.

PITA4 concerns user key inputs being ignored, not the display of pop-ups, so we
do not think it establishes an exception for PITA6. We have therefore not made
that assumption.

Two questions:

  (1) Should PITA6 be read as conditional, i.e. excluding the case where the
      reverse camera is being shown? If so, could the wording be updated
      accordingly?

  (2) The behaviour "Popup not displayed over RVC" appears only in the state
      matrix and not in the logic and flow document, and consequently has no
      corresponding requirement in the SWE.1 analysis report. Should it be
      added as a requirement? At present no test case will cover it, because we
      do not author test cases for behaviour that has no requirement of its own.

In the meantime we are writing the PITA6 test case with a pre-condition that
the reverse camera is not being shown, and recording the reverse camera case as
a coverage gap.

Thank you,
```
