# DATA REQUESTS — Vehicle Category (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/vehicle_category/inputs/`; each landing closes or advances the linked
DR。**DR 由 Pei 發出（Tier 3）；本檔僅登記，執行層不發送。**

來源：下放包 01 §六（`docs/handoff/01_intake_recon.md`）。序號於 01 包編定。
下放包 02 §四之裁定已併入：A-VC2 附於 DR-VC2，不單獨發。

| DR | 狀態 | 標的 | 阻斷範圍 |
|---|---|---|---|
| DR-VC1 | **未結** | 037 作者 | 僅 `SWE1-HMI-VC-021` |
| DR-VC2 | **未結** | 037 作者 | 不阻斷生成；交付前須有答覆 |
| DR-VC3 | **未結** | 037 作者 | 不阻斷本次交付；表 B 措辭取決於此 |
| DR-VC4 | **未結** | 規格作者 | 條件性 —— 待 DR-VC3 回覆 |
| DR-VC5 | **未結** | 037 作者 | 不阻斷（R-VC3 已裁全取）|
| DR-VC6 | **未結** | 規格作者 | 條件性 —— 待 DR-VC3 回覆 |
| DR-VC7 | **未結** | 037 作者 | 不阻斷（R-VC11 已裁其僅作邊界）|
| DR-VC8 | **未結** | 037 作者 | 僅 `SWE1-HMI-VC-033-01` |
| DR-VC9 | **未結** | 規格／037 作者 | `VC-013-04`／`VC-007-01`／`VC-025-01` 三筆 |
| **DR-VC10** | **未結** | 規格作者／HMI 彈窗清單維護者 | **二問**：(一) 四筆之 ER 文字；(二) `061` 之進入路徑 |

**十筆全為未結。**

**發送批次（下放包 03 §四、04 §四、09 §二）—— 同批 A，現為五項**：
DR-VC2、DR-VC7、**DR-VC8**、A-VC2 之封面一問、A-VC10 之
Title／Description 語意一問 —— 五者同為對 037 作者之查詢，
**同批發送，一次往返**。
DR-VC6 待 DR-VC3 回覆後另批。DR-VC1／DR-VC3／DR-VC5 之批次未指定。
**DR-VC10（下放包 24 T128 新立）獨立發送**（下放包 25 §2.5 裁定）——
其對象為規格作者與彈窗清單維護者，與同批 A 之 037 作者不同，**不併同批 A**。
其範圍為二問（見該節）。

---

## DR-VC1 —— Privacy Lock 彈窗之實際 PU 編號

- **標的**：037 作者
- **狀態**：未結
- **內容**：規格 §3.6（CO13）之 Privacy Lock 彈窗 id 於**規格原文即為字面
  `PUXXXX`**，非實 id；037 `SWE1-HMI-VC-021` 原樣沿用。請提供實際 PU 編號。
- **阻斷範圍**：僅 `SWE1-HMI-VC-021`。缺件期間該 TC 之對應欄填
  `PENDING: DR-VC1 Privacy Lock popup ID`（IN §8.4.3），不得留空、不得填 NA。

## DR-VC2 —— `SYS-HMI-RA-VC-###` 之來源系統與對應關係

- **標的**：037 作者
- **狀態**：未結
- **內容**：`Source Requirement ID` 欄之 `SYS-HMI-RA-VC-###`（61 個相異值）
  在 SYS1 export 全簿命中 0。請說明該 id 之來源系統，及其對 SYS1
  `NRL-######` 之對應關係。
- **阻斷範圍**：不阻斷生成（R-VC5(c)）。**交付前須有答覆**以完成雙向追溯。
- **實測佐證**：T4／T12 重測確認 `SYS-HMI-RA` 於 SYS1 三分頁
  （`Basic Report` / `Polarion` / `_polarion`）全儲存格出現次數為 **0**。
- **附帶一問（A-VC2，下放包 02 §四裁定）**：037 封面 `Reviewer：` 為空、
  `Date：` 為 `2020/09/05`，與修訂履歷（2025-12-26 ~ 2026-04-27）矛盾。
  請確認封面欄位是否為表單樣板殘留。**不單獨發 DR** —— 封面欄位不阻斷任何
  Phase，單獨往返一輪之成本高於其資訊價值。

## DR-VC3 —— 18 節有內容而 037 零涵蓋

- **標的**：037 作者
- **狀態**：未結
- **內容**：規格 §8.1–8.5、§9.1–9.2、§10.1–10.2、§11.9–11.9.3、§14.2、§15、
  §16.1、§16.2.1、§16.2.2 共 **18 節**有實質需求內容而 037 無對應需求。
  請確認係「刻意排除」或「分析遺漏」；若為前者，請提供排除依據與承接單位。
- **阻斷範圍**：不阻斷本次交付（R-VC3）。惟表 B 之措辭取決於此答覆。
- **關聯**：A-VC3 併入本 DR，不單獨發。
- **措辭依據（R-VC7）**：18 節之內容摘要**已於 T17 以 repo 內權威素材逐節
  重驗**（結果見上繳包 02 §7）。下放包 01 §4.2(b) 之原摘要係讀 Project 附件
  之衍生 PDF 所寫，**不得引為本 DR 之措辭依據，亦不得寫入表 B**；
  發出時一律採 T17 重驗後之內容。
- **T17 之實質發現（發出前須知）**：18 節中 **§15 與 §10.1／10.2 之關鍵內容
  在 repo 之權威素材中不可得** —— 其為圖檔，SYS1 `Description` 僅存
  `(image: imageNN.png)` 佔位。故本 DR 對該三節之提問應改為
  「該節內容僅存於圖，SYS1 匯出未帶文字」，而非引述任何摘要文字。

## DR-VC4 —— VF507 / VF352 兩份未附文件

- **標的**：規格作者
- **狀態**：未結
- **內容**：規格 §8.4 之 Cabrio 前提條件引 **VF507**、§14 之 EPB 逾時引
  **VF352**，二文件未附。
- **阻斷範圍**：**條件性** —— DR-VC3 回覆為「應補」時始為必要素材。
  DR-VC3 回覆前不催。

## DR-VC5 —— FROP 跨域 17 列之承接單位

- **標的**：037 作者
- **狀態**：未結
- **內容**：`FROP` 欄之 `Power Management`（16 列）與 `Audio Management`
  （1 列）共 17 列：其 TC 應由本 feature 產出，或由 FROP 所指之 feature 承接？
- **阻斷範圍**：不阻斷（R-VC3 已裁全取）。答覆到後若需縮限，以 `[OVERRIDE]`
  處理，不得回頭默默扣列。
- **本輪實測佐證**：T5 已測 —— 該 17 列與 `features/power/`、
  `features/power_moding/` 之既有 req_id 與 spec_reference **重疊 0 筆**。

## DR-VC6 —— §15 與 §10.1／10.2 之圖內內容

- **標的**：規格作者
- **狀態**：未結
- **⚠ 問法已改（下放包 28 §一 R-VC27 末段，T148）**。原問「該三節之內容
  僅存於圖，請提供文字版本」——**其前提於 §10.1／§10.2 不成立**（A-VC20）。

- **內容（三問）**：

  **(一) §15 之三圖內容** —— 其 SYS1 `Description` 逐字為
  `Electronic Park Brake Service Mode Pop-up / (image: image20.png) /
  (image: image21.png) / (image: image22.png)`，
  即**標題句以外之內容確實只在三張圖裡**。請提供其文字版本
  （EPB 彈窗表：PU0132 / 0133 / 0134 / 0136 / 0139 / 0141 / 0143 /
  0144 / 0145 / 0202 / 0275 之訊息與逾時）。

  **(二) §10.1／§10.2 之圖內容** —— 該二節之**文字部分已有，不需索取**。
  其 SYS1 `Description` 逐字含
  `Refer to the HMI Settings list for settings location.`、
  `All four Aux switches (Aux 1 Aux 2, Aux 3, and Aux 4) can be used
  simultaneously`、`Graphics are visual aids only. Please see PDO release
  for official graphics`。**僅索取 image9–12 四張圖之內容**
  （Aux Switch 之 Type / Power Source / Last State 組合表及其可用條件）。

  **(三) `All four Aux switches … simultaneously` 一句之地位** ——
  該句是否**即為該二節之完整需求**，抑或**圖中另有其他規則**？
  此問決定該二節於表 B 之「覆蓋落差」是整節或僅圖內部分。
- **阻斷範圍**：**條件性** —— 該二節皆在 037 未涵蓋之 17 節內，
  依 R-VC3 本次不產出 TC。**僅當 DR-VC3 回覆為「應補」時始為必要素材**；
  DR-VC3 回覆前不催。
- **實測佐證（T17）**：SYS1 `Description` 於 §15 僅存標題 +
  `(image: image20–22.png)`；§10.1／10.2 僅存「Refer to the HMI Settings
  list」「All four Aux switches … simultaneously」與 image9–12 佔位。
  repo PDF 之文字層於對應頁（p15–18、p25–27）僅存投影片標題與頁碼。

- **⚠ 本欄自 T17 起即為正確，而 R-VC12 二(a) 與表 B 同期寫成「未帶文字」**
  （下放包 28 §一／A-VC20）。**同一 repo 內，正解與錯解並存了 24 個包** ——
  本欄逐字記著那二句，而錯的那一份被引用。
  **不是沒人讀過那三格；是讀了、記對了，然後沒有任何機制去比對二者。**
  記於此，因為它改變了 A-VC20 之教訓：光是「重測」不夠，
  **既有台帳之互相牴觸也要有人看見**。
- **不得引述**：下放包 01 §4.2(b) 對該三節之摘要文字已由 R-VC12 二作廢，
  本 DR 不引用之。

## DR-VC7 —— 037 Priority 欄之賦值判準

- **標的**：037 作者
- **狀態**：未結
- **內容**：欄 18 `Priority` 於 117 個 leaf **按規格章節整批賦值**
  （High 28 / Medium 88 / Low 1，每章內部無例外，證據見 A-VC9），
  且該欄為九個分析欄中**唯一無 Description-Action 配對**者。
  請說明其賦值判準，及 Medium 一格（88 筆）內是否有更細之區辨。
- **阻斷範圍**：不阻斷 —— R-VC11 已裁定其僅作**邊界**使用，非映射來源。
  回覆到後 R-VC11(b) 之邊界重審。
- **批次**：同批 A —— 與 DR-VC2、A-VC2 之封面一問、A-VC10 之一問同發。

- **附帶一問（A-VC10，下放包 04 §四）**：037 於部分 leaf 上，
  `Requirement Title` 所載之條件多於 `Requirement Description`。
  最鮮明之一例：`SWE1-HMI-VC-035-03` 與 `SWE1-HMI-VC-036-02` 之
  Description **逐字相同**（`Selecting cancel will take the user back to
  the previous screen.`），而 Title 分別載明
  `without changing any settings` 與 `without clearing any data`。
  執行層實測：117 個 leaf 之 Description 相異值為 **116**，
  **唯一之重複組即此二筆** —— 即該欄單獨無法區辨此二需求，Title 可以。
  請說明二欄之分工：Description 是否為規格原文之逐字轉錄，
  Title 是否為需求化改寫並得補入規格他處或圖中之條件？
  **不單獨發 DR**（同 A-VC2 之處理）。

## DR-VC8 —— `VC-033-01` 之鎖定門檻與計時起點

- **標的**：037 作者
- **狀態**：未結
- **內容**：`SWE1-HMI-VC-033-01`（§7.1）之鎖定門檻，二欄相差一次：

  | 欄 | 原文 | 觸發於 |
  |---|---|---|
  | `Requirement Title` | `After three sequential wrong PINs` | **第 3 次** |
  | `Requirement Description` | `more than three times in sequence` | **第 4 次** |

  請確認實際門檻，並說明 **30 分鐘之計時起點**（末次錯誤輸入時／
  彈窗顯示時）與**其間之 HMI 呈現**（按鈕灰化／顯示倒數／無提示）。
- **阻斷範圍**：**僅 `SWE1-HMI-VC-033-01`**。缺件期間該 TC 之門檻欄填
  `PENDING: DR-VC8 Glove Box lockout threshold`（IN §8.4.3），
  不得留空、不得填 NA、**不得自行取 3 或 4**（A-VC14(a)）。
- **批次**：同批 A（第五項）。
- **附帶查詢之界線**：計時起點與 HMI 呈現為**已存在需求之未明處**，
  故一併問；**不擴大至規格未涵蓋之範圍**。
- **實測佐證（T52）**：全 117 leaf 之同型掃描中，本筆為**唯一之真陽性**
  （其餘 9 筆候選為假陽性）。掃描方法與其偽陰性見上繳包 10 §3。

## DR-VC9 —— PDO Graphics 素材，及純交叉引用型 leaf 之地位

- **標的**：規格作者（素材）＋ 037 作者（leaf 地位）
- **狀態**：未結
- **內容分二問**：

  **(一) 素材**：`PDO Graphics` 於規格 §2.6.2／§2.6.3 被引為版面之權威來源
  （`refer to PDO Graphics`／`Refer to PDO graphics.`），
  但該件**不在本 feature 之素材清單**（`feature.yaml` 之 `reference:` 六項
  已窮舉，見 R-VC10）。請提供該件，或說明其取得方式。

  **(二) leaf 地位**：037 之下列三 leaf，其 `Description` **僅為交叉引用或
  表格題名**，無自身可測內容（T79 之全表掃描，117 leaf 母體）：

  | leaf | § | `Description` 逐字 | 形態 |
  |---|---|---|---|
  | `SWE1-HMI-VC-013-04` | 2.6.3 | `Refer to PDO graphics.` | 純交叉引用 |
  | `SWE1-HMI-VC-007-01` | 2.4 | `Vehicle Tab Labels and Order.` | 表格題名（SYS1 為 `VC2.2.) Vehicle Tab Labels and Order`）|
  | `SWE1-HMI-VC-025-01` | 3.9 | `C1.) Controls Button Table.` | 表格題名 |

  三者皆有 priority（P3／P2／P2），皆在 117 leaf 母體內。
  請確認**其是否應登記為需求 leaf** —— 若為表格題名之誤登，
  其下之對照列（`007-02`~`-05`／`025-02`~`-05`）已各自成 leaf。

  **(三) `VC-014` 之 `(See table above)`（下放包 20 §2.2）**：
  §3.1 之 Description 逐字為
  `CO2.) Possible items to be placed in the Controls tab include, but are not
  limited to (See table above): …`。

  **執行層已實測 SYS1**（R-VC7 之權威複本）：
  - SYS1 **§3 僅為章標題**（逐字 `Controls`），**其下無任何表**；
  - 章 3 之唯一表在 **§3.9**（`C1.) Controls Button Table`，二欄 28 列），
    **位於 §3.1 之後方**；
  - 章 2 之 §2.4 雖有表，但其為 Vehicle Tab Labels and Order（頁籤名與位置），
    **與 Controls 項目無關**。

  即 **`above` 於規格自身即不成立**。請確認該引用之標的為何。

  > 本問之措辭刻意載明實測 —— 上游需要知道的是「**查過了、沒有**」，
  > 而非「我們沒找到」（下放包 20 §2.2）。

- **阻斷範圍**：
  - **(二) 阻斷三筆 b 段**：`VC-007-01`／`VC-013-04`（第 1 批）、
    `VC-025-01`（第 3 批）—— 三筆皆**保留不生成**，其地位待確認。
  - **(一)(三) 不阻斷生成**：`VC-011`／`VC-012-03`（第 1 批）與
    `VC-014`（第 3 批）帶 `PENDING` 生成，其字串分別為
    `PENDING: DR-VC9 Dashboard content table`／
    `PENDING: DR-VC9 PDO graphics`／
    `PENDING: DR-VC9 Controls table reference`。
- **不得自行剔除該三 leaf** —— 117 母體為 R-VC3 所裁，剔除屬 Tier 2
  （下放包 14 §2.1 之明文）。
- **批次（下放包 15 §3.1 已裁）—— 維持單一編號，雙標的分送**：

  | 分問 | 標的 | 發送批次 |
  |---|---|---|
  | **(一)** 索取 PDO Graphics | **規格作者** | **獨立發，不等 DR-VC3** |
  | **(二)** 三筆純交叉引用 leaf 之地位 | **037 作者** | **併同批 A**（成六項）|

  (一) 不併入 DR-VC4／DR-VC6 之理由：該二筆為**條件性**（待 DR-VC3 回覆為
  「應補」始為必要素材），而 PDO Graphics 是**第 1 批 b 段之硬阻斷**。
  條件性索件與硬阻斷索件混批，會使前者拖慢後者。

  **編號不拆**：DR 之編號是追蹤單位，一件事拆二號會使本檔之未結數失真。
  分送屬**發送安排**，非編號問題。

---

## DR-VC10 —— 章 13 之二問：`PU0091` 之字 ＋ `061` 之進入路徑

> **範圍於下放包 25 §2.1 擴為二問**（沿 DR-VC9 之雙標的先例，一封信兩問）——
> 二者對象同為規格作者，且皆源於章 13 之同一組需求。
> **不併同批 A**（同批 A 之對象為 037 作者，非規格作者）。

---

### （一）`PU0091` 之權威彈窗字串（原文，下放包 24 T128(c)）

**由來**：A-VC18。同一彈窗，規格側作 `Feature not available while vehicle
is in motion`，`Pop Up List HMI R1 (26PI)` 與 `HMI Settings List R1 SR25
Post R1L-R` **二份獨立來源**一致作 `Function not available while vehicle is
in motion.`（且有句末句點）。

**已實測，非「我們沒找到」**：`Pop Up List` `Main` 分頁全 1344 列已搜
`PU0091`，**唯一命中第 93 列**，其 `String/Popup Message` 欄逐字為
`Function not available while vehicle is in motion.`。

### 問

1. `PU0091` 之**權威字串**為 `Feature` 或 `Function`？句末是否含句點？
2. 若彈窗清單為準，SYS1 §13.4.1／§13.4.2 之引文是否應更正？
   （若是，037 之 `062-01`／`063-01` `Description` 隨之）
3. `PU0091` 之 `Description` 欄作 `Driver Lockout: Function / Some functions
   are lock while vehicle is in motion` —— 該彈窗是否為**通用**之行進中攔阻
   彈窗（非本 feature 專屬）？若是，其字串之變更歸誰。

### 阻斷範圍

第 5 批 `062-01`／`062-02`／`063-01`／`063-02` 四筆之 ER 文字。
**不阻斷該四筆之生成** —— 依 IN §8.4.3 帶 `PENDING` 佔位。

狀態：**未結**。

---

### （二）`061` 之 Software Updates 於 Key Off 之進入路徑（下放包 25 §2.1）

**由來**：A-VC19。章 13 為三個「他路徑仍可用」之需求給出路徑，**獨缺其一**：
`059-*` 有 §13.2 之 `through the Phone screens`、
`060-*` 有 §13.3 之 `through the Media`、
**`061` 只斷言「Key Off／ACC 可用」，未載經何路徑**。

**為何不能以通稱表述帶過**（下放包 25 §2.1 之裁定）：
`034-02` 所缺者為**測試資料**（通稱後 Procedure 仍可執行）；
本項所缺者為**進入路徑** ——
「經一條於 Key Off 仍可用之路徑進入」**不是可執行的步驟**。

**已實測，非「我們沒找到」**：
- SYS1 全表搜 `Software Update|FOTA|Wi-Fi` —— **僅命中 §13.4／§13.4.1／§13.4.2**，
  三節皆未載路徑。
- `HMI Settings List` `Settings` 分頁：`Software Updates` 為**第 27 類**
  （第 650 列），即在被 §13.1 擋住的 Settings 頁籤後方；
  其第 651 列作 `See Software Updates Logic and Flow for logic`
  —— **委派至我方未持有之文件**。

### 問

1. 使用者於 Key Off／ACC 下，**經何路徑**到達 Software Updates？
   （Phone 有 Phone screens、Audio 有 Media —— Software Updates 之對應者為何）
2. 若該路徑載於 `Software Updates Logic and Flow`，**請提供該件**；
   或告知 §13.4 是否應比照 §13.2／§13.3 補寫路徑。

### 阻斷範圍

`061` 之 Procedure。**不阻斷生成** —— 依 IN §8.4.3 帶
`PENDING: DR-VC10 Software Updates entry path in Key Off`。

**⚠ 本項之揭露強度**：「SYS1 未載其路徑」為**否定性判斷**，
其強度限於已搜之樣式與 `HMI Settings List` 之 `Settings` 分頁。
**若路徑載於未持有之 `Software Updates Logic and Flow`，本判斷不成立。**
