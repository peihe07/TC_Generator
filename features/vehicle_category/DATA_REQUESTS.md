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

**九筆全為未結。**

**發送批次（下放包 03 §四、04 §四、09 §二）—— 同批 A，現為五項**：
DR-VC2、DR-VC7、**DR-VC8**、A-VC2 之封面一問、A-VC10 之
Title／Description 語意一問 —— 五者同為對 037 作者之查詢，
**同批發送，一次往返**。
DR-VC6 待 DR-VC3 回覆後另批。DR-VC1／DR-VC3／DR-VC5 之批次未指定。

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
- **內容**：規格 §15（EPB 彈窗表：PU0132 / 0133 / 0134 / 0136 / 0139 /
  0141 / 0143 / 0144 / 0145 / 0202 / 0275 之訊息與逾時）與
  §10.1／10.2（Aux Switch 之 Type / Power Source / Last State 組合表
  及 Last State 之可用條件）之內容**僅存於投影片圖中**，
  SYS1 Polarion 匯出未帶文字（`(image: imageNN.png)` 佔位）。
  若該二節需納入測試範圍，請提供其文字版本或可讀之來源。
- **阻斷範圍**：**條件性** —— 該二節皆在 037 未涵蓋之 17 節內，
  依 R-VC3 本次不產出 TC。**僅當 DR-VC3 回覆為「應補」時始為必要素材**；
  DR-VC3 回覆前不催。
- **實測佐證（T17）**：SYS1 `Description` 於 §15 僅存標題 +
  `(image: image20–22.png)`；§10.1／10.2 僅存「Refer to the HMI Settings
  list」「All four Aux switches … simultaneously」與 image9–12 佔位。
  repo PDF 之文字層於對應頁（p15–18、p25–27）僅存投影片標題與頁碼。
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
