# 上繳包 14 —— Vehicle Category：第 1 批勘查 ＋ 全表交叉引用掃描（T78–T82）

- 日期：2026-08-26
- 對應下放：`docs/handoff/14_batch1_survey.md`
  （SHA256 `6d6f0f38f3426614c52e8eca940c5821d5e2caa42747e717f8487945c1a6b500`，207 行）
- **結論：勘查完成，未生成任何 TC**（下放包 §三末句：勘查後停）。
- R-VC21 已抄入 `RULINGS.md`（byte-level diff：1,873 B／34 行／`da11e39581d20a3f`）。
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T78 | 第 1 批勘查（a–f）| ✅ 五個風險點**四確認、一推翻**；另**新得一項下放包未點到者** |
| T79 | 純交叉引用全表掃描 | ✅ **確認 3 筆**（含一筆在第 3 批）；掃描器初版漏抓一筆，已修 |
| T80 | DR-VC9 | ✅ 未結 DR 更新為**九筆** |
| T81 | A-VC17 | ✅ |
| T82 | 包 13 之 T73–T77 | ✅ 上一輪已完成（上繳包 13）|

**兩件請你先看**：
1. **SYS1 §2.6.2 有三句，037 之三 leaf 只覆蓋第 1、3 句 —— 第 2 句無 leaf。**
   下放包未點到。見 §2.6。
2. **T79 新得 `VC-025-01`**（`C1.) Controls Button Table.`）——
   與 `VC-007-01` 同型，但**在第 3 批 `Controls`**，不在第 1 批。
   即本問題不限於第 1 批。

---

## 1. T78(a) —— 24 leaf 逐字全文

已逐筆取出（`Title`／`Description`），全文見 §附。
priority 分布：**P1 1 ／ P2 7 ／ P3 16**（117 leaf 母體之 `Category Structure` 24 筆）。

---

## 2. T78(b) —— 五個風險點之覆核

### 2.1 §2.1 `VC-013-04` —— **確認**

```
Description: Refer to PDO graphics.        ← 全部內容即此一句
```

SYS1 §2.6.3 之末句逐字同此，為**獨立一句**，非某句之片段。
引用後殘餘為**空**。**確認為純交叉引用。**

其 `Title`（`The portrait Dashboard layout shall follow the PDO graphics
reference for sizing, ordering, and overflow behavior`）雖列出
sizing／ordering／overflow 三項，**但三項皆委由 PDO Graphics 決定** ——
Title 讀來像需求，實則仍是指路。處置依下放包 §2.1：不剔除、DR-VC9、
帶 `PENDING`、A-VC17。

### 2.2 §2.2 句子片段 —— **確認，且 SYS1 給出完整句**

SYS1 §2.6.2 第 3 句與 §2.6.3 第 2 句為 037 拆點所在：

| 完整句（SYS1 逐字）| 037 之拆法 |
|---|---|
| `If there are two or more features, display them in the two half banners (topmost feature in the left, followed by the right), continuing with additional features below the banners (refer to PDO Graphics).` | `012-02` = 前半；`012-03` = `continuing with…`（小寫續行）|
| `For four or more features, display the first two features as single banners, the next two features as half banners in the same row, and follow with remaining features as tiles below the half banners.` | `013-02` = 前半（037 於此處補了句號）；`013-03` = `follow with…`（小寫續行）|

處置依下放包 §2.2：續行型 leaf 之 `test_item` 上半**取完整句**，
括號下半載明本 leaf 之驗證範圍，`reasoning` 載明取整句之理由。

> 一處值得記：**037 之 `013-02` 在句中補了句號並刪去 `and`**，
> 使其看似完整句。若只讀 037 不比對 SYS1，`013-03` 之續行性質
> 會被讀成「另一條獨立需求」。**T78(d) 之 SYS1 對照在此不是佐證，是必要條件。**

### 2.3 §2.3 `VC-007` 表格 —— **三項全部確認，且可靠切分**

**(a) `VC-007-01` 為表頭** —— **確認**。SYS1 §2.4 逐字為
`VC2.2.) Vehicle Tab Labels and Order`，其下即四欄表，
**第一列為欄名** `Note | Specialty Feature | Tab Name | Order`。
037 之 `Vehicle Tab Labels and Order.` 即該題名。併入 DR-VC9。

**(b) 逐列可靠切分** —— **確認可靠**。自 SYS1 切出 **11 資料列 + 1 欄名列，
每列恰 4 欄**，`|` 數量一致：

```
Note      | Specialty Feature                    | Tab Name         | Order
VC2.2.2   | PHEV / MEV / HEV                     | E. Hybrid        | Fourth
VC2.2.3   | Performance Pages Race Options…      | Dashboard        | Seventh
VC2.2.4   | Trip                                 | Trip             | Fourth
VC2.2.5   | Camera App                           | Cameras          | Second
VC2.2.6   | Vehicle Info                         | My Car           | First
VC2.2.7   | BEV                                  | Electric Vehicle | Fifth
VC2.2.8   | ARM Performance Pages                | Performance      | Sixth
VC2.2.9   | Maserati Drive Modes                 | Drive Modes      | Seventh
VC2.2.10  | Fuel Cell                            | Electric         | Fifth
VC2.2.11  | Active Driving Assist Pages          | Autonomy         | Third
```

> ⚠ `VC2.2.3` 之 Specialty Feature 欄在 SYS1 即為
> `Performance Pages Race OptionsDrive Modes DXROff Road Pages…` ——
> **多個功能名之間無分隔符，且有黏連**（`OptionsDrive`／`DXROff`）。
> 該欄無法可靠切成個別功能名。生成時之處置：
> **逐字引用整格，不自行拆分**（§8.4.1）。

**(c) 權威來源** —— **SYS1 即權威**。規格 PDF 之 §2.4 在影像頁，
文字層無此表（同 T17 之發現）。故取材以 SYS1 §2.4 為準，
037 之扁平化格僅為索引。`spec_reference` 仍逐字取 037 之
`HMI Source ID`（R-VC4 不變）。

### 2.4 §2.4 `VC-011` 之 `the table` —— **確認不明，無法自上下文確定**

SYS1 §2.6.1 逐字與 037 相同（`VC4.1) Within the Dashboard tab, display the
applicable content in order of the table.`），**未具名**。

自上下文查：章 2 之唯一表為 §2.4 之 Vehicle Tab Labels and Order
（其 `Order` 欄確為位置）。**但 §2.6 談的是 Dashboard 頁籤內之 apps，
§2.4 談的是 Vehicle Category 之頁籤** —— 二者層級不同。
`HMI Settings List`（已在手）亦查無 Dashboard 內容之排序表。

**不自行認定**（§8.4.1）。併入 DR-VC9 詢問。

### 2.5 §2.5 `VC-008` 外部引用 —— **確認**

`(see Camera HMI Logic and Flow)` 為外部規格引用。
本 TC 之範圍僅及於「Cameras 出現為頁籤」，
**不測 Camera App 自身行為**（§8.4.2），`reasoning` 須載明委派。

`VC-008`／`VC-009` **各自成 TC，不合併** —— 依 R-VC18 之一 leaf 一 TC 先例，
037 已拆則不得合併。同意下放包之判斷。

### 2.6 ⚠ **新得 —— SYS1 §2.6.2 有三句，037 只覆蓋兩句**

SYS1 §2.6.2 逐句切分：

| # | 句 | 037 之 leaf |
|---|---|---|
| 1 | `If there is only one feature, display it in the single banner.` | `012-01` |
| 2 | **`If there are two features, display them in the two half banners (topmost feature in the left, followed by the right).`** | **無** |
| 3 | `If there are two or more features, display them in the two half banners (…), continuing with additional features below the banners (refer to PDO Graphics).` | `012-02` ＋ `012-03` |

**第 2 句無對應 leaf。**

判讀：第 3 句之 `two or more` **在語意上涵蓋**第 2 句之 `two`，
且二者所述之呈現方式逐字相同 —— 即**規格本身有一組冗餘（近乎重複）之句對**，
037 取了較寬的那一句而略去較窄的。

**這不是覆蓋洞，但也不是無事** —— 其性質為
「037 在一個已涵蓋之節內，對規格之冗餘句對作了未揭露之取捨」。
依 IN §8.4.2 末段（真覆蓋洞須浮現、不得默默吸收）之精神**回報**，
但**不主張其為缺陷** —— 取寬句是合理的，缺的只是揭露。

**未立 A**（其非異常，是上游冗餘），**未擅改任何 leaf**。
建議併入 DR-VC9 或同批 A 一併問「第 2 句是否為冗餘、可否確認以第 3 句為準」。
**待你定。**

---

## 3. T78(c) —— 素材可用性（24 leaf）

| 素材需求 | leaf | 在手 |
|---|---|---|
| 僅 037／SYS1 文字層 | 15 筆 | ✅ |
| SYS1 §2.4 四欄表 | `007-01`~`-05`（5 筆）| ✅（SYS1，§2.3(b) 已驗可切分）|
| Camera HMI Logic and Flow | `008` | **不需取得** —— 僅為 §8.4.2 之委派對象 |
| PDO Graphics | `012-03`、`013-04` | ❌ **不在手 → DR-VC9** |
| `the table`（指涉未明）| `011` | ❌ **未明 → DR-VC9** |

**24 筆中 21 筆素材齊備，3 筆需 DR-VC9。**

---

## 4. T78(d) —— SYS1 對照

見 §2.2／§2.3／§2.6 之逐項。**結論：SYS1 對本批為必要而非佐證** ——
三處只有 SYS1 有完整形態：

1. §2.4 之四欄表（037 扁平化、規格 PDF 在影像頁）
2. §2.6.2／§2.6.3 之完整句（037 拆點在句中）
3. §2.6.2 之第 2 句（037 無 leaf）

---

## 5. T78(e) —— 版面方向之 Pre-Condition 形態

`012-*`（landscape）與 `013-*`（portrait）需以顯示器方向為前提。

**判定：屬 §4.4 允許之 hardware / peripheral 類。**

依據：§4.4 之允許例含 `hardware / peripheral (A PBAP-supported device is
available.)`。顯示器之方向為**該車輛之硬體配置**，非測試步驟可切換者 ——
其自檢（requires *do / check / confirm*？）為**否**：
測試者不會「把螢幕轉成直向」，而是換一台配直向螢幕的車。

建議形態：

```
1. The vehicle is equipped with a landscape display
1. The vehicle is equipped with a portrait display
```

> ⚠ 但**尚未登入 profile §5 之常數表**。依包 13 §三之教訓
> （「pilot 是建表的最好時機」），此二片語於第 1 批生成時
> **應同時登入常數表**，否則第 2 批之 `Settings List` 若也需方向前提，
> 又會各自書寫。**本輪未登入** —— 常數之措辭一經登記即凍結（profile §5.2(c)），
> 宜與生成同輪定案，不宜勘查階段先押。

---

## 6. T78(f) —— TC 數預估

**24 leaf → 預估 24 TC（一 leaf 一 TC）**，依 R-VC18 之先例。

逐筆研判可能需拆分者：**無**。理由：本批之 24 筆各自為單一呈現規則，
無 §8.3 之 boundary 軸（`012-*`／`013-*` 之「一個／兩個／四個以上」
已由 037 拆成獨立 leaf，非同一 leaf 內之邊界）。

**需帶 `PENDING` 者 3 筆**：

| leaf | PENDING 字串 |
|---|---|
| `VC-007-01` | `PENDING: DR-VC9 PDO graphics`（其為表頭，地位待確認）|
| `VC-011` | `PENDING: DR-VC9 PDO graphics`（`the table` 指涉未明）|
| `VC-012-03` | `PENDING: DR-VC9 PDO graphics` |
| `VC-013-04` | `PENDING: DR-VC9 PDO graphics` |

—— 實為 **4 筆**（含 `VC-011`，其阻斷源為指涉未明而非素材未到，
但同屬 DR-VC9 之標的）。

> 下放包 §2.1 只點名 `VC-013-04` 帶 PENDING。**本勘查得 4 筆。**
> 若 DR-VC9 之 (二) 確認 `007-01` 為表頭誤登，該筆之處置將由
> 「帶 PENDING 生成」改為「剔除」（Tier 2）—— 二者差別甚大，
> 故建議**第 1 批之生成待 DR-VC9 回覆**，或先生成 20 筆、留 4 筆待答。
> **待你定。**

---

## 7. T79 —— 純交叉引用全表掃描

腳本：`scripts/t79_crossref_scan.py`。母體 **117 leaf**。

```
A 段 — Description 命中引用詞: 6 leaf
B 段 — 候選（引用後殘餘不足／表頭形態）: 4 leaf
```

### 7.1 C 段人工判讀 —— 確認 3、推翻 1

| leaf | § | 批 | `Description` | 判 |
|---|---|---|---|---|
| `VC-007-01` | 2.4 | **1** | `Vehicle Tab Labels and Order.` | **確認**（表格題名）|
| `VC-013-04` | 2.6.3 | **1** | `Refer to PDO graphics.` | **確認**（殘餘為空）|
| **`VC-025-01`** | 3.9 | **3** | `C1.) Controls Button Table.` | **確認 —— 分析層未點名，本掃描新得** |
| `VC-012-03` | 2.6.2 | 1 | `continuing with additional features below the banners (refer to PDO Graphics)` | **推翻** —— 殘餘有可測內容；其問題是句子片段（§2.2），非純交叉引用 |

**三筆之共同形態**：`Title` 皆被 037 改寫為
「Adopt X as the authoritative source」或「shall follow X」之句式 ——
**讀來像需求，實則仍是指路**，可測內容在其下之對照列或在未到手之素材。

> A-VC10（Title 資訊量大於 Description）在此顯出另一面：
> **Title 之改寫可以把一個題名寫成看似可測之需求。只讀 Title 會漏掉這三筆。**

### 7.2 ⚠ 掃描器初版漏抓 `VC-007-01`

初版之「表頭形態」以「VERB 未命中」為條件，而
`Vehicle Tab Labels and Order.` 之 **`Order` 是名詞卻命中了動詞表** ——
**漏掉了分析層 §2.3(a) 已點名的其中一筆。**

改以**題名形態**判定（去 `Cn.)` 條號前綴後，字母 token 多數為 Title-Case
且無小寫功能詞連接成句）後始命中。
另移除裸 `per` —— 其命中 `one radio button per line` 之「每」而非「依據」，
造成 `VC-042-02` 之假陽性。

**與 T52 同型：掃描器初版漏抓它被造出來要抓的那一筆。**
這是第七件檢查器錯誤，且是**第二次同型**。

---

## 8. T80／T81 —— DR-VC9 與 A-VC17

**DR-VC9**（未結 DR 由八筆增為**九筆**）分二問：
(一) 索取 PDO Graphics；(二) 三筆純交叉引用 leaf 之地位。

批次歸屬**待你定** —— 下放包 §五建議併入同批 A 使其成為六項，
但本 DR 之 (一) 為對**規格作者**之索件，與同批 A 之對象（037 作者）不同。
**已於 DR 檔內記明此點，未自行決定。**

**A-VC17** 已立，含 T79 之全表結果、三筆之共同形態、
以及掃描器初版漏抓之記錄。狀態 PENDING（待 DR-VC9）。

---

## 9. 待你裁

1. **第 1 批之生成時機** —— 4 筆帶 PENDING；其中 `VC-007-01` 之處置
   （帶 PENDING 生成 vs 剔除）取決於 DR-VC9 (二)。
   建議待答，或先生成 20 筆。
2. **§2.6 之第 2 句** —— 是否併入 DR-VC9／同批 A 詢問。
3. **DR-VC9 之批次歸屬**（對象跨規格作者與 037 作者）。
4. **顯示器方向之二片語**是否於第 1 批生成時登入 profile §5 常數表。

---

## 10. 量測條件揭露（R-G8）

### T78(d) 之 SYS1 對照

- 取 SYS1 `Basic Report` 之 `Description` 欄，`_x000D_` 已還原。
- **偽陰性**：SYS1 為結構化匯出，FO §3 之 Mode A 盲點（匯出可能靜默漏句）
  本法看不見。§2.6 之「三句 vs 兩 leaf」是**以 SYS1 為準**所得 ——
  若 SYS1 自身漏句，實際句數可能更多。
- §2.4 之表以 `|` 結尾與否切列。**偽陽性**：若某欄之內容自身含 `|`，
  切分會錯。本次 11 列每列恰 4 欄且欄名列一致，故未實現。

### T79 之掃描

- 三段判準之 A 段為詞表（`refer to`／`see`／`as per`／`as defined in`／
  `according to`／`as described in`／`for complete logic`）。
  **偽陰性**：以其他措辭指路者（`the values are given in …`、
  `subject to the PDO release`）不在詞表內。
- B 段之「殘餘不足」以 token 數 < 6 且無動詞為準。
  **偽陰性**：殘餘長但仍不可測者（如純名詞列舉）不會被列為候選。
- **C 段為人工判讀，無機械證據** —— 三筆之「確認」與一筆之「推翻」
  皆為我讀 `Title` 與 `Description` 後之判斷。
  `VC-012-03` 之推翻尤其：其殘餘 `continuing with additional features
  below the banners` 是否「可測」，取決於「below the banners」在無
  PDO Graphics 時能否驗證 —— **我判為可測（相對位置可觀察），
  但那是判斷不是量測。**

### T78(f) 之 TC 數預估

- 「無需拆分」為人工研判，非機械。其依據為「本批 24 筆各自為單一呈現規則」。
  **若生成時發現某筆實含二個觸發**，該預估即失準 —— 預估非承諾。
