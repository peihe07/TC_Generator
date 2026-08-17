# 67 — Comfort HMI / 外部參照之全面盤點（形態式）、22 問複核、版本落差、BASELINE

- 產出層：執行層｜2026-08-17｜對象：分析層
- 覆核對象：`docs/handoff/87_reference_sweep.md`
- **未生成 TC、未改 RD-1、未寫回、未動交付夾。**

---

## 1. 全面盤點 —— 形態式 pattern，**17 句，涉 17 節**

### 1.1 pattern（形態，非清單）與其命中

| 形態 | 正規式 | 命中 |
|---|---|---|
| 指示動詞 | `refer(s\|ring)? to`／`as per`／`according to`／`per the` | 4 |
| `see` | `\bsee\b` | 8 |
| 被動處所 | `(defined\|specified\|described\|listed\|documented\|found) in` | 0 |
| 如所示於 | `as (displayed\|shown\|defined\|described) in` | 2 |
| 遵循 | `follow(s\|ing)? (the\|requirements)` | 3 |
| 具名文件形態 | `[A-Z]…{1,5} (Logic and Flow\|List\|Table\|Document(ation)?\|Notes\|Specification\|Guide)` | 4 |
| 具名代號 | `CFTS\d+`／`VF\d+`／`PDO` | 2 |
| 參數表形態 | `PROXI`／`$…$` | 0 |

（一句可命中多個形態，故各列之和大於 17。）

### 1.2 形態式與清單式之差 —— 這一項值得單獨記

上一輪之 pattern **混入了具體文件名**（`HMI Settings List`／`HMI Notes`／
`Pop Up List`／`Market Config`／`Read Me`）。本輪改為純形態後重掃並比對：

- **`PROXI`／`$…$` 與「被動處所」兩個形態，於 129 節命中 0** ——
  即本 spec **從不以參數名指涉配置**（那是 CFTS043 之寫法），
  亦不用 `defined in` 之句式。**兩個 0 都是資訊**：它們界定了這份文件的說話方式
- **清單式找到的每一件，形態式也找到了** —— 但那是運氣好，不是方法對：
  清單式只能找到**我已經想得到的文件**；`2.1` 之 Massage Seats 文件
  上一輪之所以被找到，是因為它含 `Logic and Flow` 而我恰好把該詞放進了清單

### 1.3 三類逐項

#### 類 (1) —— 已在 `inputs/` 或 `spec-index/`：**3 句／3 文件，全部「已用」**

| 節 | 句 | 物 | 已用／未用 |
|---|---|---|---|
| `9.1` | `On some vehicles (**See CFTS043** for details), there are additional Rear Climate controls and shortcuts` | `inputs/SYS1_CFTS043-…Tree view_R1L-R scope.xlsx` ＋ `inputs/R1LR_Atl-H_25PI3.5_…CFTS_043….doc` | **已用** —— `039` 之七條以之為 PC；`-430`～`-433` 引其 `$Rear_HVAC_cfg$` |
| `11.5` | `**Refer to HMI Settings List** for the details on the Auto Comfort Settings options…` | `inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | **已用**（`-382`）—— **惟所引者為客戶目錄之 SR24 版，見 §3.1** |
| `14.1` | `HVAC pop-ups should **follow the pop-up list**` | `inputs/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx` | **已用**（`-434`）—— 引用字串仍指客戶目錄路徑，見 §3.3 |

#### 類 (1) 之「已有而未用」—— **3 件**

| 件 | 129 節有無句子指涉 | 未用之理由 |
|---|---|---|
| `inputs/SR24 R1 Market Configuration Table v1.6.xlsx` | **無** —— 129 節無一句提及。指涉它的是 **CFTS043**（`*Refer to Market Configuration Table to determine LATAM related countries`）| 已掃其 8 個工作表：資料頁 HVAC 類關鍵詞 **0 命中**。**它是國別表，不是配置表** —— 其用途在「哪些國家算 LATAM」，而該題之上游條文（5 模組）標為 R1L-R 範圍外 |
| `inputs/R1LR_Atl-H_25PI3.5_…CFTS_043….doc` | 間接（`9.1` 指 CFTS043）| 同一份需求之兩種形式；**引用取 SYS1 tree view**，因其有 `Scope` 欄可判 R1L-R 範圍，`.doc` 無之。`.doc` 已全文讀過（1.74 MB 文字），供閱讀不供引用 |
| `inputs/SYS2_CFTS043 … 技術安全需求分析報告 … V01.xlsx` | **無** | **判為不得引**，見 §3.2 |

**分析層 §1 所指之一例已確認**：CFTS043 自 Phase 0 即在 `inputs/`，
而「哪種車配哪一組氣流模式」直到 Pei 追問方以它查過。
**查後未解，但「查過而未解」與「未查」是兩件事** —— 現有可稽之陰性：
5 模組之條文四列 `Scope = None`、`Radio = R1M, R1H`。

#### 類 (2) —— 在客戶目錄而不在我方：**4 句／4 文件**

| 節 | 物 | 客戶目錄之路徑 |
|---|---|---|
| `2.1` | `separate **HMI Logic and Flow documentation for Massage Seats**` | `1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/HMI/Massage Seats HMI Logic and Flow R1 SR24 Post 2A CR20339 (January 24 2022).pdf` |
| `2.13` | `**VF HVAC document**` | 候選 `1_Customer_Requirement/VF/VF_Split document/DT28_split/Climate_Controls_2_Zone_VF727_V3_R3.docx`（**身分未定**）|
| `13.4` | `**HMI Core Logic and Flow, requirement N0**` | `…/26PI2.5/HMI/Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf`（**無文字層**）＋ `10_Reviewing/00_TestCase/Media/Media/REF/SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023).xlsx`（169 列，`N0` 0 命中）|
| `13.5` | `**CFTS044**` | `…/26PI1.5/SubSystem/Activation and Configuration/R1LR_Atl-H_26PI1.5 Mar Release-Activation and Configuration_CFTS_044_Vehicle Controls_20260310-1524.doc` |

#### 類 (3) —— 遍尋不著：**3 句／3 對象**

| 節 | 物 | 搜尋範圍（R-C30）|
|---|---|---|
| `2.5` | `the table`（recirc icon）| **未指名任何節次或文件** —— 129 節逐節通讀無該對照；PDO 兩件（Theme Config 全掃、Graphics Release 文字層）皆 0 命中 |
| `16.5` | `the Climate Main page table` | 同上；其較 `2.5` 具體而仍無對照 |
| `12.6` | `HMI Notes` | `/Users/peihe/Work/02_Project_R1LR/` **全樹 `find -iname "*HMI*Notes*"`** ＋ 系統層 `mdfind` ＋ `Work_Projects/` 四個 repo，**0 命中**。近似者 `HMI Read Me R1 SR24 Post 1A` 經內容查證**不是**（`Auto Comfort` 0 命中）|

#### 非外部（指向本 spec 自身）：**7 句**

`7.1.1`（視覺動詞之 `see`，**假陽性**）、`9.2`（`«HVAC Popups» chapter`）、
`10.5`（`standard ICE AUTO logics` —— `ICE` 為 ch16 之條款前綴）、
`16.2`（`see ICE11.`）、`16.16`（`see Climate section`）、
`17.1`（`Refer to the Comfort – … HMI sections`）、
`15.1`（`follow the chart below` —— **見 §1.4**）。

### 1.4 盤點中冒出之第四種情形 —— **物在本 spec 內，而我方讀不到**

`15.1`：

> HVACP11.1) …then the HVAC pop ups displayed will **follow the chart below**.
> The graphics provided are examples…

**該圖表在 spec 之 PDF 裡，而不在我方所讀之 SYS1 export 裡** ——
`section_fulltext.tsv` 之 129 節圖片標記 **0 個**（A-CF23 已載：037 側有 52 個
圖片標記，export 側 0 個，即圖根本沒有進到文字裡）。

**它不屬三類中任何一類**：不是「已在手上」（讀不到）、
不是「客戶目錄有而我方無」（我方有那份 PDF）、也不是「遍尋不著」（它就在那）。

**其影響須具名**：`15.1` 之四條 TC（`105-01`／`105-02` 及其「離開」側）
之 ER **不可能取自該圖表**，因為我方從未見過它。
四條之 ER 取自條文之文字部分（進入／離開時 pop up 出現），**未宣稱圖表之內容**
—— 這一點事後看是對的，但它當時**不是一個被作出的判斷，只是我們看不到而已**。

同型另有 `12.7`（`images should be shown in full…`）—— 其為呈現要求而非對照表，
不構成缺口。

**建議**：此類（指向本 spec 內之圖）列為 A-CF23 之影響清單一項，
於下一輪逐節掃「below／above ＋ chart／table／image」並逐條判其是否被 TC 依賴。

---

## 2. RD-1 二十二問之逐題複核

判準：其「不可寫」之依據，是**條文真的沒給**，還是**我方未查已在手上之物**。

| 問 | 判定 | 依據 |
|---|---|---|
| 1 tab 組（2）| **依據成立而不完整** | 見 §2.1 |
| 2 氣流模式（9）| **依據成立且不變** | CFTS043 已查（Pei 追問後）：5 模組四列 `Scope=None`／`Radio=R1M,R1H`；四模組正面陳述 0 命中；MCT 為國別表 |
| 3 icon（3）| **依據成立，範圍已收窄** | 具名擁有者 PDO release（出自 HMI Read Me 明文）；我方之 PDO 兩件經掃皆無 icon 對照 |
| 4 額外後排控制（1）| **依據成立且不變（今有可稽之陰性）** | CFTS043 tree view 掃 `additional rear`／`Rear Climate softkey`／`shortcut` → **17 列全部 `Scope = None`** |
| 5 VF727（2）| **依據成立且不變** | 文件在客戶目錄，**身分未定**；其內容為訊號介面，未見 HMI 側 on/off 邏輯 |
| 6 ch18 對 ch17（3）| **依據成立且不變** | 逐字相同，無可寫入 PC 之分辨 |
| **7 AUTO 何時不可用（1）** | **依據不成立（部分）** | 見 §2.2 |
| 8 HMI Notes（1）| **依據成立且不變** | 類 (3)，搜尋範圍見 §1.3 |
| 9 設定保持（0）| **依據成立，已拆二** | 畫面狀態之保持有擁有者（Last Mode Table）；設定值仍無 |

**依據會改變者：第 7 問（不成立，部分）與第 1 問（成立而不完整）。**

### 2.1 第 1 問 —— 依據成立，惟「查過所有能查的」不成立

`2.1` 除 tab 集合外另有一句：

> **Refer to separate HMI Logic and Flow documentation for Massage Seats logic.**

而 tab 集合為 `Front, Seats (WS or R1 Low) or Seat & Wheel (Maserati),
**Massage**, Rear` —— **四個 tab 之一有一份具名之外部文件，且它就在客戶目錄裡**
（路徑見 §1.3）。

**本輪未讀該文件** —— 依 §5「不因找到文件而順勢生成」，
且其引用須先經 R-C45 認可。故：

- 「129 節無 tab 之配置對照」**仍成立**
- 「我方已查盡」**不成立**

**建議**：下一輪讀該文件，判其是否給出「哪種配置有 Massage tab」。
**即使給出，也只解 tab 集合之一項，不解順序**（`001-02`）。

### 2.2 第 7 問 —— **本層原先之依據寫得太滿**

RD-1 現行措辭：「**no section in the document says when AUTO is unavailable**」。

**實測：兩節說了一個條件。**

> `2.3`（C2.）與 `16.3`（ICE2.）皆有 **`(AUTO is not shown in MTC configurations)`**

且 MTC 早已是 profile §3.2 之**第一軸**，其兩值於本語料中各有 TC 在用
（`003-09`／`107-09` 取 MTC 值）。

**但這不使該問可撤**：`10.4` 之字面為 `off **and available**`，
而 `not shown` 與 `not available` **是否同一件事，條文沒說**。
把兩者當成同一件事，即以我方判讀補條文之未言（§8.4.1）。

**故其處置為改寫而非撤除**（**本輪未改 RD-1**）。建議措辭方向：
> 條文於 `2.3`／`16.3` 述及 MTC 配置下 AUTO 不顯示；
> 此是否即 `10.4` 所稱之 `not available`？若是，該條之反向側即可以第一軸之
> MTC 值設定；若否，請說明 AUTO 何時「不可用」。

**這一題之錯不在別人的文件裡** —— 那句話在我們自己每天讀的 spec 裡，
且我方在別處引用它作為第一軸之出處。
**「沒有任何一節說」是一句全稱否定，而我方從未以那句話去搜過。**

---

## 3. 版本落差與可引性

### 3.1 `HMI Settings List` —— 兩版之 30／31 節**逐格相同**

| | `inputs/` 之 SR25 R1L-R (Feb 13 2026) | profile §1.1 ／ `-382` 所依之 SR24 Post 2A (June 15 2023) |
|---|---|---|
| `Settings` 列數 | 1,015 | 1,015 |
| 30／31 節之列 | r104–r110 | r107–r113 |
| **逐格比對（各 7 列）** | **完全相同**：`30 Auto-On Driver`／`30.1 Heated Seat｜Heated_Seat`／`30.2 Heated Steering Wheel｜Heated_Steering_Wheel`／`30.3 Vented Seat｜Vented Seat`／`31 Auto-On Passenger`／`31.1 Heated Seat`／`31.2 Vented Seat` | 同左 |

列號差三，因 SR25 版少一個 `SR24 Change Log` 工作表所致之上移；**內容不差**。

**處置之三個選項，及本層之建議**：

| 選項 | 作法 | 代價 |
|---|---|---|
| (a) 分析層 §3.1 之建議 | **改放 SR24 版入 `inputs/`**，與 profile §1.1 及 `-382` 之依據一致 | 素材補入屬 Pei；`inputs/` 將有兩個版本或需替換 |
| (b) **本層建議** | **採 `inputs/` 之 SR25 版**：其內容經上表實測未變，更新 profile §1.1、`external_docs.py` 之 `EXT_SETTINGS`，並於 `-382` 之 `reasoning` 記其換版 | **牽動語料** → 須重跑 lint 並寫回（本輪不做）|
| (c) 維持現狀 | 引客戶目錄之 SR24 副本 | **該副本不受 `BASELINE.sha256` 保護** —— 同一份事實，手邊有一份受保護的副本卻不引它 |

**建議 (b)**，理由是 R-C45 一之「釘版」要釘的是**可被複驗的那一份**；
而 (b) 之前提（內容未變）**本輪已先量測後宣稱**，不是推定。

### 3.2 `SYS2_CFTS043 技術安全需求分析報告` —— **不得引為事實出處**

| 項 | 判斷 |
|---|---|
| 其為何物 | **我方自己的 SYS.2 工作產品**（Polarion 匯出，`Basic Report` 408 列） |
| 含所需事實否 | 含 —— 例如 `IF $Clima_Zone$ == [2 Zones] AND $Rear_HVAC_cfg$ == [Absent]` |
| **判定** | **不得引**。R-C45 之「外部文件」指**需求方之文件**；本件為**衍生物**，其內容轉述 CFTS043。以衍生物代替來源，等於把另一個流程之產出當成需求；且**其正確性是別人的交付物，不是我方可據以宣稱者** |
| 得作何用 | **唯讀之對照與導覽**（同 R-C18 對 `layer3_map` 之處置：可看，不可據以判讀）|
| 附帶所得 | `SYS-RA-HVAC-007`：`In the case of conflict between this document and the HMI requirements, **the HMI requirements shall have precedence**` —— 與本 pipeline 之立場相同：行為之驗證對象是 HMI spec |

**建議入 profile §1.1 之「未認可」表**並記上述理由（本輪未改 profile，待裁）。

### 3.3 `Pop Up List` 之路徑

`inputs/` 之副本與 profile §1.1 所記者**同為 SR24 Post 2A (Dec 15, 2023)**，
惟引用字串仍指客戶目錄。建議與 §3.1 一併處置：**引用已入 `inputs/` 者，
路徑改指 `inputs/`** —— 受 `BASELINE.sha256` 保護之副本才是可複驗的那一份。

---

## 4. `BASELINE.sha256`（R-C20）

**`inputs/` 八檔逐檔 SHA256**：

| 檔 | SHA256 |
|---|---|
| `FM-WI-FSM-036-A01 … _SWQT_20260121.xlsx` | `cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d` |
| `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx` | `a8186089a28c…`（原列未變）|
| **`HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx`** | **新列** |
| **`Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx`** | **新列** |
| `R1LR_Atl-H_25PI3.5_…CFTS_043….doc` | `6373bd860fc8…`（原列未變）|
| `SR24 R1 Market Configuration Table v1.6.xlsx` | `ae4cf0b929b0…`（原列未變）|
| `SYS1_CFTS043-…Tree view_R1L-R scope.xlsx` | `cbe747aa139f…`（原列未變）|
| **`SYS2_CFTS043 … 技術安全需求分析報告 … V01.xlsx`** | **新列** |

（完整 64 位數見 `BASELINE.sha256`；此處列首 12 碼以便對照。）

**`spec-index/` 之 SR24 三檔仍在**（export xlsx／JSON／PDF），未因增檔而移出。

| | 前 | **後** |
|---|---|---|
| 列數 | 8 | **11** |
| `shasum -a 256 -c` | — | **11 OK，0 FAILED** |

**「還沒用到」不是不保護它的理由** —— `SYS2` 報告即為此例：
**列入 BASELINE 與可否引用是兩件事**，前者管它會不會消失，後者管它能不能當依據。
執行層曾自陳「一個沒有 `shasum -c` 掛在上面的 hash，是紀錄而不是檢查」，
本項即其解除：三份外部文件自此進入 `shasum -c` 之保護範圍。

### 4.1 順帶修掉之同型缺陷

`write_back.py` 之前置 gate 原寫 `n_ok == 8`（BASELINE 之檔數）。
`inputs/` 自 5 增為 8 之後該式立即失效 —— **與 `len(withheld) >= 20`、
`len(LEAF_UNIVERSE) == 403` 同型**（R-C43）。

改為 `FAILED == 0 且 OK > 0`：**gate 要證的是「每一列都驗過且都對」，
那句話裡本來就不該有一個數字。** 現行實測 `OK=11, FAILED=0`。

---

## 5. 本輪之改動、未改動與現況

**已改**：`BASELINE.sha256`（11 列）、`write_back.py` 之 BASELINE gate。

**未改（依 §5 之不做清單）**：未生成 TC（**含 `2.1` 之 Massage Seats 文件
—— 找到它與它回答了問題是兩件事，本輪連讀都未讀**）、未改 RD-1、
未寫回、未動交付夾、未改 profile §1.1 與 `external_docs.py`。

**現況**：lint **54 / 54 PASS，0 finding across 434 TCs**；
台帳 gate 驗過 68／已知不存在 1／有問題 0；反向驗證 7 支全 PASS。

---

## 6. 待裁定

1. §3.1 之三選項（本層建議 (b)，牽動語料須重跑並寫回）
2. §3.2 之 SYS2 報告判定，及其入「未認可」表
3. §3.3 之引用路徑改指 `inputs/`
4. §2.1 之 Massage Seats HMI L&F 是否讀、是否認可
5. §2.2 之 RD-1 第 7 問改寫措辭
6. §1.4 之第四種情形（指向本 spec 內之圖）是否列為 A-CF23 之影響清單
