# 34 — Comfort HMI / A-CF26 跨 feature、預裁與通案、`14.12` 查證、批次 8

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 46／47／48／49
- 結果：七項全數落實。**A-CF26 已登（跨 feature，High），未動 privacy 任何檔案。**
  `14.12` 三條件**第二項不成立，未增軸**。
  批次 8 產 **10 條**（`-115`…`-124`），**停下 11 leaf，涉三條未登記之軸**。
  lint **42/42 PASS，124 條**。第三次寫回已產出（ENTRY 005），
  **3 項 FAIL 與 ENTRY 004 同源，不可交付、不送 Excel 確認。**

---

## 0. 下放包七項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 登 A-CF26（跨 feature，High），列 DR 具名對象；不改 privacy | ✅ §1 —— DR #36；`features/privacy/` 零讀寫 |
| 2 | ENTRY 004 增記狀態；產出標「範本容量待擴充」| ✅ §2 —— 另建 `output/STATUS.md` |
| 3 | DR #32 記入預裁（含升 High 之觸發條件）| ✅ §3 |
| 4 | profile §3.2 增「入口未定義」清單；DR #34 改類首項並併入 `-114` | ✅ §4 |
| 5 | 查 `14.12` 三條件，齊備方增軸 | ✅ §5 —— **第二項不成立，未增軸**，登 DR #37 |
| 6 | 執行批次 8 | ✅ §6 —— 產 10、**停 11**，見 §6.2 |
| 7 | 寫回照常但不送 Excel 確認 | ✅ §7 —— ENTRY 005 |
| — | 上繳 34 | 本件 |

---

## 1. A-CF26 —— 跨 feature，已登，未動 privacy

### 1.1 實測

對象：通用空白範本 `SWQT_20260121`（`cd876c202c71e74b…`）之資料工作表，
及自其產出之 prepared 檔（`b68117a2…`）—— 兩者於此性質上相同。

| 項 | 涵蓋 | 缺口 |
|---|---|---|
| B 欄編號公式 | row 10–59 | row 60 起無列號 |
| R 欄 x14 下拉（design_method）| `R10` ＋ `R11:R59` | row 60 起無下拉 |
| **P 欄 DV（priority）** | **`P10:Q11`** | **row 12 起無下拉** |
| `T–Z` DV | `T10:Z11` | row 12 起無下拉 |
| `AF` DV | `AF10:AF11` | row 12 起無下拉 |

### 1.2 性質：內容正確而約束缺失 —— 這一句是本項之全部要點

**已寫入之值不是錯的。** priority 由 generator 產出並經 lint 之 `priority`
gate 逐格檢查（`P0`–`P3`）；design_method 經 `design-method` gate 對
`下拉選單!A1:A9` 逐字元比對。缺的是**下拉約束**，其作用在保護**後續之
人工編輯** —— 評閱者或測試員於 Excel 內改 P 欄時，row 12 之後無任何阻擋。

> **故本項不是「已交付之內容有誤」，是「已交付之防呆缺一段」。**
> 兩者之緊急度與處置皆不同，寫明以免被讀成前者。

### 1.3 跨 feature 之處置

依 **R-C21** 登於 Comfort 之 `ANOMALIES.md`（**A-CF26**）與
`DATA_REQUESTS.md`（**#36，High**），具名對象為 **privacy** 及其他以
`SWQT_20260121` 為母本之 feature：privacy 以同一份範本交付 11 條
（row 10–20），其 **row 12–20 共 9 列**之 P 欄同樣無下拉約束，且該檔已交付。

**本輪未讀寫 `features/privacy/` 之任何檔案**（`git status` 對該路徑零命中）。
是否回溯由 Pei 決定。

### 1.4 為何當初沒被發現 —— 值得記

ENTRY 002 之 pilot 寫 14 列（row 10–23），其 assertion 九項**完全沒有檢查
DV 涵蓋**；而 profile §0.1 之 Excel 四項確認問的是「R 欄下拉可用且為九項」，
**R10 恰在範圍內**。於是人與程式兩端都通過了。

> **一個檢查沒問的問題，不會因為別的檢查通過而變成已答。**

---

## 2. ENTRY 004 之狀態與產出標記

`DELIVERY.sha256` 之 ENTRY 004 狀態欄增記
`not confirmed — pending template extension (DR #35)`，並載明 46 §1 之裁定
（由 Pei 於 Excel 擴充而非 `xlsx_surgical.py` 延伸）與 A-CF26／#36 之連結。

**產出檔之位元組一律不動** —— 改檔即改 hash，台帳就指不到它了。
故「標記」寫在旁邊：新增 `output/STATUS.md`，逐檔列 ENTRY、列範圍、狀態，
並解釋「範本容量待擴充」是什麼意思、解除條件為何。該檔不參與
`shasum -c`，台帳權威仍為 `DELIVERY.sha256`。

---

## 3. DR #32 之預裁

47 §1 之預裁已逐項寫入 DR #32：條件三仍不成立時比照 `2.1` 之
`-01`／`-02`（DR #17／#20）—— 不產列、不指派 tc_id、**不入 coverage 分母**、
**不創造第五類 marker**，並記其理由：

> 四類 marker 之共同前提是「我們知道這件事該由誰負責」；`[COVERED-BY]`
> 之前提更是內容有主。此處連該由誰負責都未定，**尚未到分類的階段** ——
> 再造一個標籤只會把「條文沒說」偽裝成一種已知類別。

**升 High 之觸發條件**亦已寫明：`Heated Vented Seats` 或 `Climate Popups`
任一組生成完畢，且其 TC 之 ER 未定義 configuration→icon 之對照。

---

## 4. 「入口未定義」通案

profile §3.2 增第二份生成時檢查清單，四項作業規則照 48 §1 貼入，
並記其**不立 R-Cnn 之理由**（§8.4.1 與 R-C30 之組合適用；條文已 39 條，
每多一條即多一份被引錯或被遺忘的機會）。

另補一句本項與介面型軸檢查之分工，因為兩者容易混：

> 軸問「這條在**哪種車**上跑不起來」，本項問「這條的**第一步**做不做得到」。

`DATA_REQUESTS` #34 改為該類之**單一項**，逐例列節次與詞：

| 例 | 節 | 詞 | 實測 |
|---|---|---|---|
| (a) | `16.16` | `controls screen` | pattern `controls screen` 全 129 節**僅 1 命中，即該節自身** |
| (b) | `16.17` | `Voice Recognition session` | pattern `Voice Recognition\|voice command` 命中 `2.16`／`16.17`／`2.6.1`／`16.6.1` **四節，無一節定義如何啟動** |

影響 5 條 TC（`-094`～`-097`、`-114`）之可執行性。**TC 內容一律不動。**

---

## 5. `14.12` 三條件 —— **第二項不成立，未增軸**

| 條件 | 結果 | 依據 |
|---|---|---|
| 一、兩值逐字出現，具名節次與句 | ✅ | `14.12` HVACP12：「If the hard controls are **knobs that turn** then the HVAC popups should be **radial** popups.」「If the hard controls are **UP/DOWN toggles** then the HVAC popups should be **vertical** popups…」 |
| **二、互斥且窮盡，或條文明示其為並列情形** | **❌** | 見下 |
| 三、無任何值由推論補齊 | ✅ | 兩值皆條文原文 |

### 5.1 非互斥 —— 條文明示同一台車可同時具不同型態之硬控

| 節 | 句 |
|---|---|
| `7.1` | 「**fan knob** will always control the fan speed **and driver/passenger temperature controls** will always control the front driver/pass temperature」 |
| `2.14` | 「3 knob HVAC controls」／「one zone MTC with **push button TEMPERATURE** and hard controls」 |
| `3.1` | 「If the MODE button is **a multi-directional toggle** or a hard control that allows 2 controls (**UP/DOWN or RIGHT/LEFT**)」 |

故「the type of hard controls」是**逐控制**之性質（風扇一種、溫度另一種、
MODE 又一種），**而配置軸每車取一值**。這與第三軸之發現同形：
**一個被當成並列項的東西，其實是另一個層級上的區分。**

### 5.2 非窮盡 —— 五種型態，只給了兩種的 popup 樣式

全 129 節實測所得之硬控輸入型態：

| 型態 | 節 |
|---|---|
| `knobs that turn` | 14.12 |
| `UP/DOWN toggles` | 14.12 |
| `multi-directional toggle`／`RIGHT/LEFT` | 3.1 |
| `push button TEMPERATURE` | 2.14 |
| `4-way rocker`（舊款）| 13.5 |

`14.12` **只對其中兩種給出 popup 樣式**。第二項之「或條文明示其為並列情形」
分支亦不成立：那兩句是**同一控制之兩種情形**之並列，不是**車輛配置**之並列，
且不涵蓋其餘三種。

### 5.3 結論與其代價

**不增第十六軸**，登 **DR #37（High）**。

49 §1 要求「須於 `Climate Popups`（42 leaves）生成前有結論」——
本輪之結論是「**這個問題不是增一個軸能解的**」。屆時 `14.12` 之 leaf
依 profile §3.2「未判類別之軸不得使用」須停下，除非 DR #37 先得答案。
**建議於該組生成前解答，以免大批回溯補 PC**（前例 34 §4.1 之 2.2 八條）。

---

## 6. 批次 8 —— `Home Screen Widget`

### 6.1 節次與 leaf 數，自 framework.md 導出

| outline | leaves |
|---|---|
| `17.1` | 3 |
| `17.2` | 8 |
| `17.3` | 3 |
| `17.4` | 2 |
| `17.5` | 2 |
| `18.1` | 3 |
| **合計** | **21** |

037 獨立實測：124(3)＋125(8)＋126(3)＋127(2)＋128(2)＋129(3) = **21**。
**兩者相符**（48 §2 之改法生效後首批，本輪無不相容可報）。

### 6.2 產 10、停 11 —— 三條未登記之軸

profile §3.2 明文「**未判類別之軸不得使用**」。停下之 11 leaf 分屬三軸，
每軸皆已代跑 49 §1 之三條件，使增軸與否只剩一個裁定動作：

| 軸 | leaf | 三條件 | 結論 |
|---|---|---|---|
| **(A) 螢幕尺寸／widget 尺寸** | `125-08`、`126-02`、`127-01`、`127-02`、`129-01`～`-03`（**7**）| **不齊** | 不增軸；即 **DR #6** 之同一問題 |
| **(B) Comfort Features 有無** | `126-01`、`126-03`（**2**）| **全齊** | **建議增為第十六軸** |
| **(C) dual airflow modes 有無** | `128-01`、`128-02`（**2**）| **第一項不齊** | 不增軸 |

**(A)**：`17.2` 之 `12" Portrait 50% widget`、`17.3` 之 `50% widget`、
`17.4` 之 `8.4/10.1/12 landscaped screens` 與 `25% widget`。值域無窮盡之依據，
且**本次交付出哪幾種螢幕配置**正是 DR #6 未解之問。

**`18.1` 另有一層，值得單獨記**：其全句與 `17.1` **逐字相同**，
唯一區辨者是**章標題**（`10.25" Home screen - Comfort Widget`
vs `Home screen - Comfort Widget`）—— **章標題不是條文**。
故螢幕尺寸之 PC **連出處都沒有**，R-C28 第一問在軸的問題之前就先失敗了。
而不補該 PC 逕行生成，會產出與 `17.1` **完全相同**的一組 TC（§4.5／§4.6）。

**(B) Comfort Features 有無 —— 三條件全齊，代查結果如下**：
一、兩值皆逐字出現於 `17.3`：「all Comfort features **available to the
vehicle** (i.e. Heated/Vented seats, Heated steering wheel)」與
「If the vehicle is **not equipped with Comfort Features** this widget page
will not be shown」；二、有／無為邏輯上之互斥且窮盡（同軸 10 之形態）；
三、無推論。**增軸屬 profile 變更，不自取** —— 回報待裁。

**(C) dual airflow modes**：正向值於 `2.3.1`／`14.14`／`17.5` **三節**逐字出現，
**其反面於全 129 節無任何字面**（pattern `single airflow|without dual
airflow|not equipped with dual` **零命中**），故第二個值須由推論補齊 ——
**第一項不成立**。

### 6.3 本批使 DR #6 之影響範圍擴大

DR #6 原記「3 節（19.1–19.3）」。本批實測顯示同一個未解問題
**另外影響 7 個 leaf**（(A) 之全部）。已於上繳具名；DR #6 之影響欄
待分析層裁定是否一併更新。

### 6.4 R-C17 —— 逐 leaf 判，非逐批判，結果為零剔除

Comfort 擁有「Comfort widget 自身之內容與行為」。判定測試為
**該規則定義於何處**，非誰引用之。實測六節全文：
**無一句陳述首頁管理行為**（新增／刪除／重排頁面、widget 拖放、
Shortcuts 編輯、品牌頁預設配置），每個 leaf 皆是 widget **包含什麼**或
**顯示什麼**。故本批**未因 R-C17 剔除任何 leaf**，此為實測結論而非未檢查。

**`17.1` 之括號另議**：「(Refer to the Comfort – Front Comfort/Climate and
Comfort – Heated/Vented Seats HMI sections for complete logic.)」
—— 委派對象為**本 spec 之節**，依 profile §5.3 之次序指向 `[COVERED-BY]`，
惟 **R-C39 條件四不成立**：扣除委派後仍有獨立餘留（「widget 有兩個畫面，
其一為 Comfort、其二為 Seats」本身可驗）。故**不標 marker、正常生成**，
且該三條**只驗兩個畫面之存在與名稱，不驗其內容**（內容即被委派者，§8.2.1）。

### 6.5 一處 PC 之來源類別訂正

`PC_WIDGET` 初稿寫成 `[spec-verbatim] The Comfort widget is shown on the
home screen (17.1)`。**17.1 從未說 widget 在首頁上** —— 它說 widget
*有* 兩個畫面。R-C28 第一問對「條文明文對應」失敗。

改為 `[test-setup] The Comfort widget is shown on the home screen`：
它是測試員安排之起始狀態，而「它如何被放到首頁」依 **R-C17** 屬 Home Screen
之領域。**一個看起來有出處的 PC，其出處可以是假的** —— 括號裡的節次
不會自己檢查它支不支持那句話。

### 6.6 23 列 provisional 重新確認 —— 全部涉 `17.2`

批次 8 使 `17.1`／`17.2` 落地，23 列到期（14 `not-sibling`／6 `deferred`／
3 類級），**全部逐對判完，verdict 全為 `not-sibling`**。其分界即本批之
§8.2.1 界線：

> **`17.2` 驗「該元素在 widget 上存在且可操作」，
> `2.3`／`2.6`／`2.7`／`2.11`／`2.13` 等驗「該功能在 climate 主畫面上之行為」。**
> 兩者之可觀察量分屬兩個介面。

`-116`～`-124` 之 ER 一律停在「widget 顯示該元素」與「按下後該元素改變狀態」，
**刻意不驗其行為規則**，故與對造之 ER 無共用可觀察量。

ch10 側另記：`10.8` 明指 AUTO ECO 之可觀察端為 **`the Comfort main Menu Bar
icon`**，而 `17.2` 之 `auto button` 在**首頁 widget** 上，兩者為不同元件；
其交界已登 **DR #26**（widget 顯示中時 AUTO ECO 之回饋於何處）——
**交界不是 sibling，兩者分列**。

---

## 7. 第三次寫回 —— ENTRY 005，3 項 FAIL 與 ENTRY 004 同源

前置 gate 6 項全 PASS（TC 數實測 124、tc_id 001–124 連續無缺號）。
splice row 10–133，124 列。assertion **10 PASS、3 FAIL**：

| FAIL | 範本涵蓋 | 後果 |
|---|---|---|
| B 欄公式 | row 10–59 | 74 列無列號 |
| R 欄下拉 | `R10` ＋ `R11:R59` | 74 列無下拉 |
| P 欄 DV | `P10:Q11` | **122 列**無下拉 |

**A-CF19 之呈現側實測**：N 欄最長 **599 字元**（`-119`）；欄寬 15.5；
`wrapText=True`；列高 14.0 → 可見約 1 行 ≈ 15 字元，**即最長者之 2%**。
內容完整而僅首行可見。（ENTRY 004 時為 430 字元／3%；隨批次成長而惡化。）

依 46 §3：**不送 Pei 之 Excel 四項確認**，`DELIVERY.sha256` 增
**ENTRY 005**，狀態記「範本容量待擴充 —— 不可交付」。

### 7.1 一次性 gate 於本次首度誤擋，已修

`--write` 第一次被自己的 gate 擋下：「台帳尚無 ENTRY 005」判為 present。
成因是該判斷做**台帳全文之子字串搜尋**，而 ENTRY 004 之狀態欄提及
「擴充後另立 **ENTRY 005**」—— 那個**提及**被讀成 ENTRY 本身。

改為比對 **ENTRY 標頭行**。

> 台帳談論自己未來的條目是正常的；一個分不出「引用」與「紀錄」的 gate 不是。

**這是本輪第二次由 gate 自己擋下自己的問題**（第一次是 §6.2 之
`axis-value-count` 覆蓋檢查攔下 `126-03` 之未受保護否定式 PC）。

### 7.2 ENTRY 005 之編號

46 §1.2 為範本擴充預留了 ENTRY 005。**該擴充屬 Pei 之 Tier 3 作業，尚未發生**，
故該號仍空，本次寫回取之。若擴充先落地，此常數移位 —— 而一次性 gate
就是使該衝突「出聲」而非「無聲」的東西。

---

## 8. lint 與 §9 自評

```
42 / 42 gates PASS; 0 finding(s) across 124 TCs
```

TC 114 → **124**；leaf 109 → **119**；已生成節 37 → **39**。
`pending_sibling.tsv` 1668 列（`vocab` 1588／`via-hierarchy` 80），
`provisional` `false` **146**／`true` 1522，重建冪等。

**§9 十七項**：本輪新增 10 條（批次 8）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 1 | Test Set | 變 | `Home Screen Widget`，自 framework.md 第 15 組 |
| 2 | tc_title | 變 | 10 條皆 2–14 字、無 modal |
| 3 | Pre-Condition | 變 | `[test-setup]` widget 在首頁（§6.5 之訂正）＋ 軸 13（2.14）＋ EMEA（16.2）＋ 軸 9（6.3）；`-116`／`-119` 另含軸 4（2.13）與軸 2（2.11）|
| 4 | Input Test Data | 變 | 全數 `NA` |
| 5–8 | 步驟 | 變 | 每條 2 步；末步持驗證；無禁用動詞 |
| 9 | Baseline | 變 | `-115`／`-119` 需前後對照，首步建立基線 |
| 10 | Procedure ↔ ER 1:1 | 變 | 10 條全數 1:1，ER 無 modal |
| 11 | FP／FF | 變 | 本批無否定式 ER（`126-03` 之「不顯示」已停下）|
| 12 | 溯源、§8.2.1、§8.4 | 變 | 10 leaf 各溯其 037 req_id；**§8.2.1 之界線見 §6.6**；11 leaf 依 §8.4.2 停下不吸收 |
| 13 | Design Method | 變 | 9 條功能測試、`-115`（預設畫面之回復）狀態轉換 |
| 14／15 | §11 格式 | 變 | 無行尾句點；UI 標籤用 `"…"` |
| 16 | `specification_reference` | 變 | 各條含自身節次 ＋ 17.1（PC 出處）＋ 2.14 ＋ 16.2 ＋ 6.3，適用者另加 2.13／2.11（R-C29）|
| 17 | §8.6／§8.7 | 變 | 六元素之名稱皆 CW1 原文；**`12" Portrait`／`50%`／`25%` 一律未取**（其 leaf 已停）|

---

## 9. 「本包是否仍有該驗而未驗者」（R-C30）

1. **批次 8 之 10 條未經 §7 之 FP／FF 人工複核**，只經 lint。
2. **`17.1` 之三條把「兩個畫面」拆成三個 leaf 各一 TC，而 `-115`（有兩個畫面）
   與 `-116`／`-117`（其一為 Comfort、其二為 Seats）之可觀察量高度重疊** ——
   037 之分解如此（`-01` 畫面數、`-02` 「1. Comfort」、`-03` 「2. Seats」），
   依 R-C33 單位歸 037 未合併。**§4.5 之風險已知而未消除。**
3. **`-115` 之「Move through the Comfort widget screens」未定義切換手勢** ——
   與 §4 之「入口未定義」同型，**未併入 DR #34**，因其為*操作方式*而非*入口*。
   兩者是否同類，待裁。
4. **停下之 11 leaf 佔本組 21 leaf 之 52%。** `Home Screen Widget` 之 coverage
   為 10/21，且其中 7 leaf 卡在 DR #6（未解逾 10 個下放包）。
5. **DR #37 未解前 `Climate Popups`（42 leaf）不宜開工** —— 該組為第三大，
   `14.12` 之 leaf 屆時必停。
6. **A-CF26 之 privacy 側僅依 46 §2 所述登記，執行層未實測 privacy 之交付件** ——
   本輪未讀 `features/privacy/` 任何檔案（那是刻意的），
   故「row 12–20 無下拉」一句**係轉述分析層之陳述，非執行層實測**。
7. **`output/STATUS.md` 不參與任何機械檢查** —— 它若與 `DELIVERY.sha256`
   分歧，沒有東西會出聲。**這是新增的一處無保護記述**，記之。

---

## 10. 建議 commit message（git 未執行）

```
feat(comfort): batch 8 Home Screen Widget; A-CF26, 14.12 axis check

- A-CF26 (cross-feature, High): the blank template's P-column validation
  covers P10:Q11 only, so every feature built on SWQT_20260121 loses the
  priority dropdown from row 12. privacy shipped 11 rows; its rows 12-20
  are affected. Registered per R-C21 with privacy named — no file under
  features/privacy/ was read or written
- the point of A-CF26 is that the CONTENT is right and the GUARD is
  missing: priority values pass lint's own gate; what is absent is the
  dropdown protecting later hand edits
- ENTRY 004 gains `not confirmed — pending template extension`; product
  status goes in output/STATUS.md rather than into the files, because
  editing a product changes the hash the ledger points at
- DR #32 records 47 §1's pre-ruling and its High trigger; profile §3.2
  gains the "entry undefined" generation-time checklist and DR #34 becomes
  that class's single item, absorbing -114
- 14.12 fails condition TWO and is NOT registered as axis 16: the spec has
  one vehicle carrying a fan knob AND push-button temperature AND a
  multi-directional MODE control, so "the type of hard controls" is per
  control, not per vehicle; and five forms are attested while 14.12 gives a
  popup style for two. DR #37
- batch 8: 10 TCs, -115..-124, and 11 leaves stopped on three unregistered
  axes. Each was run through the three conditions anyway so registering one
  costs a ruling, not an investigation: screen/widget size fails (it is
  DR #6), Comfort-Features-present PASSES all three, dual-airflow-modes
  fails condition one — its negation appears nowhere in 129 sections
- 18.1 is verbatim identical to 17.1; only the CHAPTER TITLE differs, and a
  chapter title is not a clause, so the screen-size PC has no source at all
- fixed a PC that looked sourced and was not: 17.1 never says the widget is
  on the home screen. Now [test-setup], per R-C17
- third write-back, ENTRY 005, 124 rows: same three FAILs as ENTRY 004,
  not delivered, not sent for Excel confirmation. The one-shot ledger gate
  blocked itself on ENTRY 004's *mention* of "ENTRY 005" — now matches the
  entry header, not any substring
- lint 42/42 PASS across 124 TCs
```

---

## 11. 待分析層

1. **(B) Comfort Features 有無** —— 三條件全齊，是否登為第十六軸並判其類別
   （介面型／功能型）。齊備即可解封 `126-01`／`126-03`。
2. **DR #6** —— 螢幕／widget 尺寸；其影響範圍是否自 3 節更新為
   「3 節 ＋ 本批 7 leaf」。**未解前 `Home Screen Widget` 停在 10/21。**
3. **DR #37** —— `14.12` 之其餘硬控型態；**建議先於 `Climate Popups` 開工**。
4. **§9.3** —— 「操作方式未定義」（`-115` 之畫面切換手勢）是否併入
   「入口未定義」通案。
5. **§9.2** —— `17.1` 三條之 §4.5 重疊風險是否接受。
6. **§9.6** —— A-CF26 之 privacy 側是否需執行層實測（現為轉述）。
7. **批次 9 之授權**；建議避開 `Climate Popups` 直至 DR #37 有解。
