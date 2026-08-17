# 66 — Comfort HMI / 外部參照之全面盤點、22 問複核、版本一致性、BASELINE 更新

- 產出層：執行層｜2026-08-17｜對象：分析層
- 對應：`docs/handoff/87_reference_sweep.md`（撰寫中）
- **未生成 TC、未改 RD-1、未寫回。**

---

## 1. 外部參照之全面盤點（Phase 0 就該做而未做）

### 1.1 掃描之涵蓋範圍（R-C30）

| 項 | 內容 |
|---|---|
| 對象 | `data/section_fulltext.tsv` **全 129 節之 `full_text`**（不截斷）|
| 切句 | 以 `[.;]` 後接大寫或 `(`／`«` 切句 |
| pattern | `refer to`／`see`／`as per`／`according to`／`defined in`／`follow(s) the｜requirements`／`specified｜described｜listed｜documented｜found in`／`as displayed｜shown in`／`the table(s)`／`document`／`chapter`／`section`／`list`／`CFTS\d+`／`VF\d*\s?HVAC`／`HMI Settings List`／`HMI Notes`／`Pop Up List`／`Logic and Flow`／`PDO`／`Market Config`／`Read Me`／`PROXI` |
| 命中 | **21 句，涉 21 節** |
| **已知漏報** | 以**代名詞或泛稱**指涉他物者不被命中（例：「the applicable table」若寫成「it」）。本輪未做語意判讀，**此為未被證明不存在**（R-C13）|

**第一次以 pattern 掃過** —— 此前之「129 節通讀後未見」是通讀，
其涵蓋範圍無法事後重算（上繳 60 §1 已自陳）。

### 1.2 三類之計數

| 類 | 數 |
|---|---|
| **(1) 已在 `inputs/` 或 `spec-index/`** | **4 句／3 個文件** |
| **(2) 存在於客戶目錄而不在我方** | **4 句／4 個文件** |
| **(3) 遍尋不著（真缺口）** | **3 句／3 個對象** |
| （非外部 —— 指向本 spec 自身之節或章）| **10 句** |

### 1.3 第 (1) 類 —— 逐項含「已用／未用」

| 節 | 句 | 文件 | 狀態 |
|---|---|---|---|
| `9.1` | `On some vehicles (See CFTS043 for details), there are additional Rear Climate controls and shortcuts` | CFTS043（tree view ＋ `.doc` 皆在 `inputs/`）| **已用** —— `039` 之後續七條以之為 PC；`-430`～`-433` 引其 `$Rear_HVAC_cfg$` |
| `11.5` | `Refer to HMI Settings List for the details on the Auto Comfort Settings options…` | HMI Settings List（**SR25 版今在 `inputs/`**）| **已用**（`-382`）—— **惟所引者為客戶目錄之 SR24 版，見 §3** |
| `14.1` | `HVAC pop-ups should follow the pop-up list` | Pop Up List（**今在 `inputs/`**）| **已用**（`-434`）—— 引用路徑仍指客戶目錄，見 §3.3 |

**「已有而未用」者：`inputs/` 之三件**

| 件 | 是否被 129 節之句子指涉 | 用況 |
|---|---|---|
| `SR24 R1 Market Configuration Table v1.6.xlsx` | **否** —— 129 節無一句提及；其被指涉者為 **CFTS043**（`*Refer to Market Configuration Table to determine LATAM related countries`）| **未用**。已掃其 8 個工作表，資料頁 HVAC 類關鍵詞 0 命中（上繳 60 §3）—— **它是國別表，不是配置表** |
| `R1LR_Atl-H_25PI3.5_Cabin_CFTS_043 … .doc` | 間接（`9.1` 指 CFTS043）| **未用** —— 本輪之引用取 SYS1 tree view（有 `Scope` 欄可判 R1L-R 範圍），`.doc` 僅供閱讀 |
| `SYS2_CFTS043 … 技術安全需求分析報告 … V01.xlsx` | **否** | **未用，且判為不得引** —— 見 §3.2 |

### 1.4 第 (2) 類 —— 在客戶目錄而不在我方

| 節 | 對象 | 現況 |
|---|---|---|
| `2.1` | `separate HMI Logic and Flow documentation for Massage Seats` | **`Massage Seats HMI Logic and Flow R1 SR24 Post 2A CR20339 (January 24 2022).pdf` 在客戶目錄**。**本輪未讀** —— 見 §2.1，它可能觸及 RD-1 第 1 問 |
| `2.13` | `VF HVAC document` | `Climate_Controls_2_Zone_VF727` 為候選，**身分未定**（RD-1 第 5 問）|
| `13.4` | `HMI Core Logic and Flow, requirement N0` | 文件在；`N0` 未查得（SYS1 export 僅 169 列、PDF 無文字層）|
| `13.5` | `CFTS044` | 文件在；`rocker`／`4-way` 0 命中 |

### 1.5 第 (3) 類 —— 真缺口

| 節 | 對象 | 依據 |
|---|---|---|
| `2.5` | `the table`（recirc icon）| 未指名任何節次或文件；129 節無該對照 |
| `16.5` | `the Climate Main page table` | 比 `2.5` 具體而仍未給對照 |
| `12.6` | `HMI Notes` | 客戶目錄全樹 ＋ `mdfind` 0 命中 |

---

## 2. RD-1 之 22 問複核 —— **兩題之依據會變**

逐題問「其不可寫，是條文真的沒給，還是我方未查已在手上的東西」：

| 問 | 依據是否改變 | 說明 |
|---|---|---|
| 1 tab 組（2）| **可能改變** | 見 §2.1 |
| 2 氣流模式（9）| 不變 | CFTS043 之四列 `Scope = None`；四模組正面陳述 0 命中 |
| 3 icon（3）| 不變 | PDO 釋出件仍未取得 |
| 4 額外後排控制（1）| 不變（**今有可稽之陰性**）| CFTS043 tree view 掃 `additional rear`／`Rear Climate softkey`／`shortcut` 命中 **17 列，全部 `Scope = None`** —— 無一在 R1L-R 範圍內 |
| 5 VF727（2）| 不變 | 身分未定 |
| 6 ch18 對 ch17（3）| 不變 | 逐字相同，無分辨 |
| **7 AUTO 何時不可用（1）** | **會改變** | 見 §2.2 |
| 8 HMI Notes（1）| 不變 | 第 (3) 類 |
| 9 設定保持（0）| 不變 | Last Mode Table 只管畫面 |

### 2.1 第 1 問 —— `2.1` 有一句被漏掉了

`2.1` 除 tab 集合外另有一句：

> Refer to **separate HMI Logic and Flow documentation for Massage Seats** logic.

而 tab 集合正是 `Front, Seats (WS or R1 Low) or Seat & Wheel (Maserati),
**Massage**, Rear` —— **其中一個 tab 之邏輯有一份具名之外部文件，
而該文件就在客戶目錄裡**（`Massage Seats HMI Logic and Flow R1 SR24 Post 2A
CR20339 (January 24 2022).pdf`）。

**本輪未讀該文件**（時間與範圍所限，且其引用需先經 R-C45 認可）。
故本層之判定是：**第 1 問之「129 節無此對照」仍成立，
但「我們查過了所有能查的」不成立** —— 至少有一份具名文件未讀。

**建議**：下一輪先讀該文件，判其是否給出「哪種配置有 Massage tab」，
再決定第 1 問是否縮為一條（僅 tab 順序）。

### 2.2 第 7 問 —— **本層原先之依據過強**

RD-1 現行措辭為「**no section in the document says when AUTO is unavailable**」。

**實測：129 節之中有兩節說了一個條件**——

> `2.3`（C2.）／`16.3`（ICE2.）：**(AUTO is not shown in MTC configurations)**

而 MTC **已是 profile §3.2 之第一軸**，其兩值皆有 TC 在用。

**但這不使該問可撤**，因為 `10.4` 之字面是 `off **and available**`，
而 `not shown` 與 `not available` **是不是同一件事，條文沒說**。
把兩者當成同一件事，即以我方之判讀補條文之未言（§8.4.1）。

**故其處置為改寫而非撤除**：把問題從「有沒有任何條件」
改為「`MTC configurations` 中 AUTO 不顯示 —— 這是否即 `10.4` 所稱之
`not available`？若是，該條之反向側即可用第一軸之 MTC 值設定」。

**這一題之依據是我方寫錯的**：說「沒有任何一節說」，
而有兩節說了，且那句話我們自己在別處引用了很多次（第一軸之出處即它）。
**它不在別人的文件裡，它在我們每天讀的那份 spec 裡。**

---

## 3. 版本一致性與 SYS2 報告之可引性

### 3.1 HMI Settings List：SR24 與 SR25 之 30／31 節 **逐格相同**

| | `inputs/` 之 SR25 R1L-R (Feb 13 2026) | profile §1.1 所記之 SR24 Post 2A (June 15 2023) |
|---|---|---|
| `Settings` 工作表列數 | 1,015 | 1,015 |
| **30／31 節（各 7 列）** | r104–110 | r107–113 |
| **逐格比對** | **完全相同** —— `30 Auto-On Driver`／`30.1 Heated Seat｜Heated_Seat`／`30.2 Heated Steering Wheel｜Heated_Steering_Wheel`／`30.3 Vented Seat｜Vented Seat`／`31 Auto-On Passenger`／`31.1 Heated Seat`／`31.2 Vented Seat` | 同左 |

（列號差三，因 SR25 版少了 `SR24 Change Log` 工作表所致之上移；內容不差。）

**依 R-C45 第二項之處置建議**：該條所引之事實（選項之名稱）
**經實測為版本無關** —— 這正是 R-C45 二所要求者，且本輪是**先量測再宣稱**。

建議：

1. **profile §1.1 之該列改記 `inputs/` 之 SR25 版為引用對象**，
   並加一欄記「SR24 版之 30／31 節經逐格比對相同（2026-08-17）」
2. `external_docs.py` 之 `EXT_SETTINGS` 字串隨之改版本名
3. 上列二者**牽動 `-382` 之 `specification_reference` 與 lint 之
   `EXTERNAL_REFS`，屬語料變動，須重跑 lint 並寫回** ——
   **本輪不改**（指示為不寫回），列此待裁

**若分析層裁定不改**，亦須有一句理由入 profile：
現況是「引一份不在 `inputs/`、不受 `BASELINE.sha256` 保護的副本」，
而同一份事實有一份受保護的副本就在手邊。

### 3.2 `SYS2_CFTS043 技術安全需求分析報告` —— **判為不得引為事實出處**

| 項 | 判斷 |
|---|---|
| 其為何物 | **我方自己的 SYS.2 工作產品**（Polarion 匯出，408 列），內容為對 CFTS043 之需求分析 |
| 其含所需事實嗎 | 含 —— 例如 `IF $Clima_Zone$ == [2 Zones] AND $Rear_HVAC_cfg$ == [Absent]` |
| **判定** | **不得引**。R-C45 之「外部文件」指**需求方之文件**；本件是**衍生物**，其內容轉述 CFTS043。以衍生物代替其來源，等於把另一個流程之產出當成需求 —— 且**其正確性是別人的交付物，不是我方可據以宣稱者** |
| 得作何用 | **唯讀之對照與導覽**（同 R-C18 對 `layer3_map` 之處置：可看，不可據以判讀）|
| 一項附帶所得 | 其 `SYS-RA-HVAC-007` 寫 `In the case of conflict between this document and the HMI requirements, **the HMI requirements shall have precedence**` —— **與本 pipeline 之立場一致**：行為之驗證對象是 HMI spec |

**故 profile §1.1 之「未認可」表增列本件並記其理由。**（本輪已列，見 §5。）

### 3.3 另一項版本落差 —— Pop Up List

`inputs/` 之副本與 profile §1.1 所記之客戶目錄副本**同為 SR24 Post 2A
(Dec 15, 2023)**，惟**引用字串仍指客戶目錄之路徑**。
建議與 §3.1 一併處置：**引用已入 `inputs/` 者，路徑改指 `inputs/`** ——
受 `BASELINE.sha256` 保護之副本才是可被複驗的那一份。

---

## 4. `BASELINE.sha256` 之更新（R-C20）

| | 前 | **後** |
|---|---|---|
| `inputs/` | 5 檔 | **8 檔** |
| `spec-index/` | 3 件 | 3 件 |
| 合計 | 8 | **11** |
| 實測 | — | **`shasum -a 256 -c`：11 OK，0 FAILED** |

**涵蓋以來源為準，不以「是否已用」為準**：一份放進素材夾而未列入雜湊者，
其消失與被替換皆不出聲。**「還沒用到」不是不保護它的理由。**
（`SYS2 SYSRA 報告`即為此例：**列入 BASELINE 與可否引用是兩件事** ——
前者管它會不會消失，後者管它能不能當依據。）

### 4.1 順帶修掉一個同型缺陷

`write_back.py` 之前置 gate 寫 `n_ok == 8`（BASELINE 之檔數）。
`inputs/` 自 5 增為 8 之後該式立即失效 —— **與 `len(withheld) >= 20`、
`len(LEAF_UNIVERSE) == 403` 同型**（R-C43）。

改為 `FAILED == 0 且 OK > 0`：**gate 要證的是「每一列都驗過且都對」，
那句話裡本來就不該有一個數字。**

---

## 5. 本輪之改動與未改動

**已改**：`BASELINE.sha256`（11 列）、`write_back.py` 之 BASELINE gate。

**未改**（依指示）：未生成 TC、未改 RD-1、未寫回；
profile §1.1 之引用對象與 `external_docs.py` 之字串**維持現狀**，
其改動建議見 §3.1／§3.3 待裁。

**現況**：lint **54 / 54 PASS，0 finding across 434 TCs**；
台帳 gate 驗過 68／已知不存在 1／問題 0；反向驗證 7 支全 PASS。

---

## 6. 待裁定

1. §3.1／§3.3 之引用對象是否改指 `inputs/`（牽動語料，須重跑並寫回）
2. §2.1 之 Massage Seats HMI L&F 是否讀、是否認可
3. §2.2 之 RD-1 第 7 問改寫措辭（**本層未改 RD-1**）
4. §3.2 之 SYS2 SYSRA 報告判定是否成立
