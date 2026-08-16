# 30 — Comfort HMI / R-C38 落實、前後排鏡射表、候選判定範圍收斂

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 41
- 結果：R-C38 已貼入並機械化，`044-02` 產 `[BLOCKED-NON-HMI]` row（`-081`），
  **403 leaf 之阻塞數由 3 降為 2**。`ch2_ch7_mirror_map.tsv` 建成 26 列、
  雙向全列。231 對逐對判完，**新發現 3 對 sibling（tri-mode 軸）**。
  四類 241 對之 verdict 已改措辭。`-023`／`-076` 之 7 條 TC 逐條複查完畢。
  lint **41/41 PASS，81 條**。**未寫回。**

---

## 0. 下放包七項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | R-C38 貼入 `RULINGS.md`；profile §5 增第三類 marker 與三者對照表 | ✅ §1 |
| 2 | `044-02` 產 BLOCKED row、白名單增列、登 RD-1 | ✅ §1.2／§1.3 |
| 3 | 建 `data/ch2_ch7_mirror_map.tsv`，雙向、含 `partial` 分界欄 | ✅ §2 |
| 4 | 依 §3 收斂候選判定範圍，回報三類各若干對 | ✅ §3 —— **但收斂之結果為零**，見 §3.1 |
| 5 | 四類 verdict 改 `not-broken-by-3-samples (class)` | ✅ §4 |
| 6 | 複查 `-023`／`-076` 之圖片依賴；其餘 18 leaf 入生成時清單 | ✅ §5 —— **18 leaf 之清單本輪無法重建**，見 §5.3 |
| 7 | 全批重跑 lint 與 §9 自評；不寫回 | ✅ §7／§8 |

---

## 1. R-C38 —— 已貼入、已機械化、已產列

### 1.1 條文與 profile

R-C38 原文貼入 `RULINGS.md`（置於 R-C37 之後、執行層回報段之前，
與其他條文同層）。profile §5 改為四段：

| 段 | 內容 |
|---|---|
| §5.1 | `[BLOCKED-SPEC]`（R-C24），原文不動 |
| **§5.2** | **`[BLOCKED-NON-HMI]`（R-C38）** —— 欄位表、五項使用條件、RD-1 之連帶義務 |
| **§5.3** | **三類 marker 對照表 ＋ 判別次序** |
| §5.4 | R-C16 之不產列者（原 §5.2），另補與 §5.2 之界線 |

§5.3 之判別次序寫成一條可執行之問句串，而非三欄並列：

> 先問「條文有無委派字面」—— 有 → `[BLOCKED-SPEC]`；無 → 再問
> 「本 feature 內有無可觀察端」—— 無 → `[BLOCKED-NON-HMI]`；有 → 正常生成。
> **037 未產出該 leaf 者不進入本次序**，屬 §5.4。

三欄對照表回答「它們差在哪」，次序回答「我現在該用哪個」。上繳 29 §1.5 之
三欄表已證 `044-02` 非 `[BLOCKED-SPEC]`，卻仍推薦了不合的 R-C16 ——
**差異表不足以導出選擇**，故補次序。

### 1.2 `044-02` 之 BLOCKED row —— `NR1L-ComfortHMI-081`

```
tc_id                    NR1L-ComfortHMI-081
req_id                   SWE1-HVAC-044-02
test_procedure           （空）
expected_result          （空）
specification_reference  …_10.1; …_2.14
remarks                  [BLOCKED-NON-HMI] Not an HMI-observable property —
                         the requirement states a reduction in climate control
                         system power consumption, which no Comfort HMI screen,
                         pop-up or status indicator displays, and which no
                         other document is stated to own
```

**tc_id 釘死為 `-081` 而非由計數器取得。** 044 是本批第一個 parent，
若讓 `-02` 由計數器取號，`-067`…`-080` 全部後移一號 ——
**會移動的識別碼不是識別碼**（R-C7）。generator 因此加了一條：TC 物件自帶
`tc_id` 時不動計數器。

**五項使用條件之實測（R-C30，搜尋範圍具名）**：

| 項 | 實測 |
|---|---|
| 一、無委派字面 | 10.1 全句一句，無 `see`／`as per`／`refer to`／具名文件（上繳 29 §1.3） |
| 二、037 產出該 leaf | 是 —— `SWE1-HVAC-044-02`，有 TITLE／DESC／VC／VM |
| 三、全 feature 無可觀察端 | `data/section_fulltext.tsv` 全 **129 節**、pattern `power\|consumption\|energy\|batter`（不分大小寫）→ **命中 5 節** |
| 四、替代觀察量已由他 leaf 涵蓋 | 具名 **10.6**（`-075`／`-076`）與 **10.9.1**（`-080`） |
| 五、白名單增列 | 41 §1.2 裁定准；已入 `lint_tcs.py` 之 `MARKER_WHITELIST` |

**第三項之五個命中值得逐一交代**（陰性側不留白，R-C37）：

| 節 | 命中字 | 是不是可觀察端？ |
|---|---|---|
| 2.7 / 7.5 / 16.7 | `power` | **否** —— `climate power button`（電源鍵），與耗電量無關 |
| 10.1 | `power`, `consumption` | 本節自身 |
| **10.9.1** | `batter`, `consumption` | **文字上是，實質不是** —— pop-up 文字「Press again for lower battery consumption」是**一個字串之顯示**，其驗證屬 10.9.1 自身之 leaf（`-080` 已涵蓋），不是耗電量之量測 |

第四項之意義即在此：全 spec 內唯一與「耗電」有關的可觀察物，是一句
**提示文字**，而它已經有主。取用它就是兩個 leaf 共用一組可觀察量（§4.5）。

### 1.3 RD-1 —— `DATA_REQUESTS.md` #24

已登：`044-02` 之 Verification Method 標 `Manual UI Testing`，而其
Expected Result 為 `Reduces climate control system power consumption`
—— **無任何 UI 可觀察量**。Medium，不阻塞（BLOCKED row 已產，leaf 未遺失）。
待確認：改標驗證方法，抑或改寫 Expected Result 為一個 HMI 可觀察量。

### 1.4 lint 之三處改動

1. `BLOCKED_MARKERS` 由一元組變二元組；`blocked-row-empty`、豁免清單一併涵蓋
2. `MARKER_WHITELIST` 增 `[BLOCKED-NON-HMI]: {NR1L-ComfortHMI-081}`
3. **`blocked-remarks` 之首行檢查改為依 marker 分岔，且兩者互斥**：
   - `[BLOCKED-SPEC]` → 首 60 字元內須有 `Owner:`（R-C27，原規則）
   - `[BLOCKED-NON-HMI]` → 首 60 字元內須有 `Not an HMI-observable property`，
     且**全欄不得出現 `Owner:`**

第 3 項刻意不寫成「兩者擇一即可」。**沒有擁有者是本類之判準**（R-C38），
一個寬鬆的「有 owner 或有片語都算過」，會讓一個明明有委派對象的 leaf
躲在 `[BLOCKED-NON-HMI]` 底下 —— 那正是 marker 用來區分的兩件事被合併回去。

每次 lint 之具名回報行現輸出三行：受豁免之列（三 marker 合併）、
`[BLOCKED-SPEC]` 白名單、`[BLOCKED-NON-HMI]` 白名單。

---

## 2. `data/ch2_ch7_mirror_map.tsv` —— 26 列，雙向全列

欄位 `ch7_outline`｜`ch2_outline`｜`對應強度`｜`依據`｜`涵蓋與未涵蓋之行為分界`，
比照 `ch16_mirror_map.tsv`。

**覆蓋 assertion（R-C37，建表不得只取有對應者）**：ch2 全 **22** 節、
ch7 全 **11** 節，逐一出現於表中，缺一即建表腳本失敗。

| 強度 | 列數 |
|---|---|
| `mirrored` | 3 |
| `partial` | 9（**全部填了分界欄**） |
| `no-counterpart` | 14（ch7 側 2、ch2 側 12） |

### 2.1 事實訂正 —— ch7 是 **11** 節，不是 12

下放包 41 §2 記為「ch2 全 22 節與 ch7 全 12 節」。實測
`data/section_fulltext.tsv`：ch7 為 `7.1`／`7.1.1`／`7.2`…`7.10`，**共 11 節**。
ch2 之 22 正確。表以 11 建，assertion 依 11。

### 2.2 三對 `mirrored`

| ch7 | ch2 | 依據 |
|---|---|---|
| 7.2 | 2.3 | CR2 與 C2 首二句逐字相同；差異為值域與連動對象（C2 四模式＋front defrost＋AC＋MTC 但書；CR2 三模式，另加 `Fan breaks Auto for Airflow mode`）|
| 7.7 | 2.11 | CR7 與 C12 首句、`Sync synchronizes driver and passenger temperatures to the driver temperature` 一句逐字相同 |
| 7.8 | 2.12 | `ON state for the {three\|four} airflow modes is shown by highlighting the button and increasing button size` 除模式數外逐字相同 |

### 2.3 `partial` 九列所暴露之事

建表本身查出了幾件抽樣看不到的事：

1. **`7.1` 之通則在 ch2 只剩一句。** CR1 說「後排畫面上硬鍵一律控前排」，
   而 ch2 內唯一同義句是 C13.1 末句，**只講 MODE 一鍵**。
   CR1 具名的 fan knob 與 driver/passenger temperature 兩鍵，
   **ch2 全 22 節沒有對應句** —— 同一行為在前排側從未被陳述。
2. **`7.4` 一節綑綁了 ch2 的兩節**（C5 ＋ C5.1），形態與 ch16 之 `16.4`
   綑綁五者相同，故拆成兩列 `partial`。其中 CR4 載有 `500 ms` 明值而
   C5.1 無值 —— 即 `DATA_REQUESTS` #21，**方向與當初相反**：
   當初記為「後排有值可參考」，表上看清楚的是「**前排缺值**」。
3. **`7.6` 之未涵蓋是雙向的。** C11 有 defrost 例外、status bar 破折號、
   回復上次等級；CR6 有 rear lock／front climate 兩鍵保留、前排關閉時
   後排不可用。兩側各有對方沒有的行為，故分界欄兩側都寫。
4. **`7.9` 全句只有一句**（`AC has on/ off state.`），C3 之四項連動
   （Auto／Defrost／Recirc 自動開 AC、AC breaks Auto）在 ch7 全章不存在。
   **後排 A/C 與 AUTO 之關係未定義。**

### 2.4 兩處易混淆，已寫入表內

- **`2.9` 之 `Rear Defrost` 不是本章之 rear climate** —— 它是後窗除霜器。
  ch7 全 11 節對 `defrost` **零命中**。表中 `2.9` 記為 `no-counterpart`
  並於依據欄標明，免得日後有人把 `Rear *` 前綴當成對應線索。
- **`7.10` 之 4 Zone** 於 ch2 無對應：C5／C5.1 之「雙側」指前排駕駛／乘客。

---

## 3. 候選判定之範圍收斂 —— **三類之第三類是空的，且是結構性的**

### 3.1 回報三類各若干對

依 41 §3 之判定時點規則，對 `class-invalidated` 之 **231 對**分類：

| 規則 | 條件 | 對數 |
|---|---|---|
| 一 | 兩節皆已生成 → 現在逐對判 | **24** |
| 二 | 一節已生成、一節未生成 → 現在逐對判，入 `pending_sibling` 待回填 | **207** |
| 三 | 兩節皆未生成 → `deferred` | **0** |

**收斂之結果為零 —— 231 對全部落在「現在就要判」。** 而這不是巧合。

`sibling_candidates.py` 之候選是在**某個 Test Set 完成之日**產生的，
它拿該組之節去對全部 129 節。**故任一候選對至少有一節是已生成的。**
全表 689 列驗證此點：`both` 55、`one` 632、`neither` **2** ——
而那 2 列是上一輪抽樣時**人工加入**的 `2.3 ↔ 7.2`、`2.12 ↔ 7.8`，
不是產生器產的，且皆已判為 `sibling`。

> **41 §3 之規則三，在現行產生器下永遠取不到值。**
> 它治的是「兩節皆未生成之對」，而那種對根本進不了這張表。

這不是說規則三沒有意義 —— 它描述的工作量其實**存在**，只是不在這張表裡：
真正「兩節皆未生成」的對，是那些**還沒被任何一輪候選產生器掃到**的組合
（15 組中尚有 10 組未生成）。它們現在既非 `deferred` 也非任何 verdict，
而是**不存在於表中**。要讓規則三有對象，得改產生器：
在每組完成時，除了「本組 × 全部」之外，也把「未生成組 × 未生成組」入表並標
`deferred`。**此為改動，未做，待裁。**

### 3.2 231 對之逐對判定結果

| verdict | 對數 |
|---|---|
| `not-sibling`（逐對）| **228** |
| **`sibling`（本輪新發現）** | **3** |

每對之 `reason` 皆重寫，具名條文標籤與其句子，並標明落在規則一或規則二。

**新發現之三對，全部同一軸**：

| 對 | 依據 |
|---|---|
| `2.12 ↔ 3.1` | C13「There are 4 Airflow Mode … Only one airflow mode can be selected at a time」與 C19「there are 3 airflow mode buttons … individually toggle ON / OFF which provides 7 possible distribution modes」**對同一車輛互斥** —— 故非兩個需求，是同一需求（本車之氣流模式集合與選取方式）之兩個配置值 |
| `2.12.1 ↔ 3.1` | C13.0 開頭即寫 `In some **non-tri mode** equipment types` —— **條文自己以 tri-mode 為對照定義自身** |
| `2.12.2 ↔ 3.1` | C13.1 之 `Face > Face/Feet > Feet > Feet plus Windshield` 循環與 C19 之七組合循環，同為「MODE 硬鍵之推進與順序」 |

差異軸為 profile §3.2 **第三軸「tri-mode 有無」**。三對之 `3.1` 已生成、
ch2 側未生成，屬規則二，`duplicate_of` 待 `Airflow and Defrost` 生成時
由 `pending-sibling` gate 要求回填（已列於本輪 lint 之具名回報行，11 對）。

### 3.3 連帶發現 —— 第三軸實為**三值**，不是二值

`2.12`（4 模式）／`2.12.1`（5 狀態，非 tri-mode）／`3.1`（tri-mode 7 組合）
是同一問題的三個答案。profile §3.2 第三軸現記為「tri-mode 有無」，
**是一個二值軸的名字**。

這正是 35 §4 所治之形態：否定式 PC（「本車非 tri-mode」）之涵蓋隨軸值而變，
而軸多了一個值時，既有的否定式不會自己變紅。`axis-value-count` gate 現在
盯的是 `axis-values` 區塊之值數 —— **若該軸改為三值，gate 會要求複核全部
negation users（現 65 條）**。

**未改，待裁**：軸之更名與值數變更屬 profile 變更，不自取。

### 3.4 逐對判定之七類依據（228 對）

| 依據類 | 對數 | 一句話 |
|---|---|---|
| ch10 之外加狀態（ch2↔ch10）| **61** | **ch10 自身以委派字面回指 ch2**（`see standard ICE AUTO logics`／`as in standard AUTO mode`／`compared to the standard ICE AUTO pop up`）—— 委派不是重述 |
| ch16 鏡射（含 ch10↔ch16、ch2↔ch16、ch3↔ch16）| **52** | 兩套介面不會同時出現於同一車輛 |
| popup／widget 呈現 vs 內容（ch14／15／17／9）| **40** | 同一個 popup 的兩個面向 |
| ch7 之對造在 ch2 而非對方（ch7↔ch10／ch2／ch3）| **26** | 由新建之鏡射表判定 |
| 座椅 `Auto Comfort Settings` 同形異義 | **25** | `Auto` 於座椅語境非 HVAC 模式 |
| ch3 vs ch2／ch10 之不同功能 | **16** | 唯一交會已登 #22 |
| 同章不同 Test Set（ch2↔ch2）| **8** | 共有語彙出現於各自之連動子句 |

**最像 sibling 的幾對，逐對讀了全文並單獨寫理由**（R-C37 之陰性側）：
`10.8 ↔ 2.3`（Menu Bar icon vs main category control 之 AUTO 呈現）、
`10.9 ↔ 15.1`（popup 內容 vs popup 之觸發選用）、
`3.1 ↔ 7.8`（**兩個 3 意義不同**：可個別切換之按鈕數 vs 互斥狀態數）、
`11.5 ↔ 12.6`（HVS6 同文異委派對象 —— 屬 #11 之 ch11／ch12 合併問題）。

---

## 4. 四類之 verdict 措辭 —— 241 列已改

`not-sibling (class)` → **`not-broken-by-3-samples (class)`**，241 列全數。
每列之 `reason` 前置一段，載明：原措辭為過度陳述、三對之力度足以破類不足以
證類（R-C37）、該對尚未逐對判定、其所屬節生成之日轉為逐對判定。

`data/pending_sibling.tsv` 現況（689 列）：

| verdict | 列數 |
|---|---|
| `sibling` | **11**（8 ＋ 本輪 3）|
| `not-sibling`（逐對）| **437**（209 ＋ 228）|
| `not-broken-by-3-samples (class)` | **241** |
| `class-invalidated` | **0**（已清空）|
| `deferred` | **0**（§3.1）|

**一項結構問題，本輪未改，呈報**：`lint_tcs.py` 之 `pending-sibling` gate
**只盯 `verdict == "sibling"` 的列**。這意味著：

> 一對被判為 `not-sibling` 之後，其對造節生成之日**不會有任何機制要求複看**。

§3 規則二說「其結果寫入 `pending_sibling.tsv`，由 gate 於對造節生成時要求
回填」—— 回填之對象是 `duplicate_of`，而 `duplicate_of` 只有 `sibling` 才有。
所以規則二對 `not-sibling` 之結果**沒有回訪機制**。而 §4 又說「類級判定不因
曾通過而免除，其所屬節生成之日轉為逐對判定」——
**逐對判定之結果若為 `not-sibling`，同樣沒有回訪機制。**

本輪之 228 對逐對判定，其中 207 對之對造節尚未生成。**它們現在的狀態，
和上一輪那 241 對類級判定的狀態，在機制上是一樣的：一個沒有第二次機會的
判斷。** 差別只在粒度與理由長度。

可能之解（未做，待裁）：gate 改盯「對造節未生成之全部列」而非僅
`sibling`，於對造節生成之日以具名回報行列出「本節之候選對曾判 X，理由 Y，
請複看」。成本是回報行變長；收益是 §4 之「不因曾通過而免除」有機制承載，
而不只是一句寫在 reason 欄裡的話。

---

## 5. A-CF23 —— `-023`／`-076` 之七條 TC 逐條複查

問句：**該 TC 所驗之行為，是否有任何部分依賴圖片所載之內容？**

### 5.1 `SWE1-HVAC-076`（13.2，1 張圖）—— 三條皆**否**

`-001`／`-003` 所驗者為分頁切換至 `Seats tab`（該名稱由 LS1 文字具名）；
`-002` 所驗者為 popup 之出現與 5 秒無互動後消失（皆為 LS1 明載之事件）。
**三條之 ER 不驗任何視覺呈現。** 該 leaf 之 `reasoning` 原已寫「popup 樣式與
Seats tab 內容本節未定義，寫入即造值」，本輪把它接成一個具名的答。

### 5.2 `SWE1-HVAC-023`（3.1 Tri-Mode，6 張圖）—— 三條皆**部分為是**

| TC | 不依賴圖的部分 | **依賴圖的部分** |
|---|---|---|
| `-015` | 個別 toggle 之邏輯（C19 明載）| ON 態之呈現 |
| `-016` | 七組合之循環順序（C19 逐項列出）| 「active」之判讀方式 |
| `-017` | UP/RIGHT 前進、DOWN/LEFT 後退（C19 明載）| 同上 |

**具體缺口**：C19 全句**未定義三個 airflow mode 按鈕之 ON 態如何呈現**。
C13（`2.12`）之「highlighting the button and increasing button size」屬
**四模式配置**，於 tri-mode 車不適用（此點與 §3.2 之新 sibling 同源：
兩者是同一需求的不同配置值，故 C13 的呈現規則不能借給 C19）。

故三條之 ER 雖以「toggled ON」／「active」陳述，**其判讀依據不在條文內**。
已記入 A-CF23 之影響清單並寫入各 TC 之 `reasoning`。**TC 內容一字未動。**

### 5.3 形態，以及其餘 18 個 leaf

**同一 leaf 之三條 TC，行為邏輯不依賴圖，而狀態之判讀方式依賴圖。**
問句若寫成「這條依不依賴圖」，會得到一個是非；寫成「**哪一部分**依賴圖」，
才會得到一個分界。已把這句寫進 `RUNBOOK.md` 之生成時必答項。

**其餘 18 個帶圖 leaf 之具名清單，本輪未能重建（R-C30）**：
`inputs/` 於本 session 不可達 ——
`find . -maxdepth 3 -name "*037-A03*"` 於 repo root **零命中**，
037 workbook 無法重新量測。29 §5 所載之部分名單為 `-055`（5）、
`-001`／`-044`／`-045`／`-083`（各 3）。

故 41 §5 之「其餘 18 leaf 入生成時清單」**落實為規則而非清單**：
`RUNBOOK.md` 新增一節，載明必答項、兩種答案之義務、以及「空白不算答」。
形態比照 `interface-axis-answered`：**正確性不可機械檢查，「有沒有問過」
可以。** 具名清單待 037 可達時補建。

---

## 6. 本輪浮現、未處置之 coverage hole 候選（§8.4.2，具名不吸收）

判 231 對時讀全文所見。**皆未開 DR，未動任何 TC**，列此待裁：

| # | 缺口 | 兩側之實測 |
|---|---|---|
| a | **AUTO ECO 是否及於後排氣候** | ch10 全 9 節未提及 `rear`；ch7 之 CR2 為 C2 之後排重述，不含 ECO |
| b | **widget 顯示中時 AUTO ECO 之回饋** | 14.19「-Auto Pop-up: do not show (feedback is already on widget)」與 10.9「comfort pop ups … shall reflect the AUTO ECO and AUTO states」—— 前者使後者於該情境無對象；14.19 未述 AUTO ECO，ch10 未述 widget |
| c | **tri-mode 車上 AUTO 與七組合之互斥關係** | C2 寫 `mutually exclusive with the four airflow modes`，而 tri-mode 車沒有「四模式」；C19 全句不提 AUTO |
| d | **後排 A/C 與 AUTO 之關係** | CR9 全句僅 `AC has on/ off state.`；C3 之四項連動 ch7 全章不存在（§2.3 第 4 點）|
| e | **前排 long press 門檻無值** | 已為 #21，**方向訂正**：表上看清楚的是前排缺值，不是後排有值可參考 |

c 與 §3.2 之新 sibling 是同一件事的兩面：既然 `2.12 ↔ 3.1` 是同一需求的
兩個配置值，那麼 C2 對「四模式」所宣告的互斥，在 tri-mode 側就有一個
對應物該被寫出來 —— 而它沒有。

---

## 7. lint 與 §9 自評

```
41 / 41 gates PASS; 0 finding(s) across 81 TCs
```

TC 由 80 增為 **81**（新增之 BLOCKED row）；leaf 由 75 增為 **76**。

**§9 十七項之變動**：本輪唯一新增之 TC 為 BLOCKED row，其餘 TC 之
內容（PC／procedure／ER）**一字未動**，變動僅及三個 `reasoning`。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | Pre-Condition 為 spec trigger（§4.4／§8.5）| 變 | `-081` 之 PC 兩行：第十五軸（10.1 明文 `used on EV Vehicles only`，spec-verbatim）＋ 第十三軸排除（2.14，spec-derived）。**BLOCKED row 之 PC 照常填** —— 空的是 procedure 與 ER，不是資格條件 |
| 5 / 6 / 10 | 步驟與 ER | 變 | `-081` 之 procedure／ER **為空**，依 R-C24 之豁免（`proc-min-steps`／`proc-er-1to1`），豁免以具名回報行輸出 |
| 12 | 溯源、§8.2.1、§8.4.2 | 變 | `-081` 溯 `SWE1-HVAC-044-02`；`-015`～`-017` 之 reasoning 依 §8.4.2 具名 A-CF23 之缺口而不擴張 ER |
| 16 | `specification_reference` | 變 | `-081` 填 `10.1`（自身）＋ `2.14`（第十三軸排除之出處，R-C29）|
| 其餘 12 項 | — | 不變 | 無 TC 內容變動 |

**未寫回**（下放包 41 §7.7）。`write_back.py` 未執行，工作簿未動。

---

## 8. 「本包是否仍有該驗而未驗者」（R-C30）

1. **`not-sibling` 之判定沒有回訪機制**（§4 末）。本輪 228 對中 207 對之
   對造節未生成，其狀態與上一輪那 241 對在機制上相同。**這是本包最大的
   未完項**，且它不是工作量問題，是機制問題。
2. **41 §3 之規則三取不到值**（§3.1）。真正「兩節皆未生成」的對不在表中，
   要讓規則三有對象需改產生器 —— **未改**。
3. **第三軸可能是三值而非二值**（§3.3）。若成立，65 條 negation users 須複核。
   **未改 profile，未複核。**
4. **`ch2_ch7_mirror_map.tsv` 之 `mirrored` 三列，其判定依據仍是「開頭一樣」。**
   `RUNBOOK.md` 之「節級看開頭，TC 級看那一句」對 ch16 已成教訓；
   本表之三列尚未經 TC 級複核（`Rear Climate` 未生成）。
   **R-C36-1 之形態應同樣適用於本表，但本輪未立條文，亦未自取。**
5. **18 個帶圖 leaf 之清單未重建**（§5.3），037 不可達。
6. **§6 之五項 coverage hole 候選未開 DR。** 具名於此，未吸收進任何 TC，
   亦未自行登記 —— 開不開 DR 屬裁量。
7. **231 對之逐對判定，其中 24 對（規則一，兩節皆已生成）我讀了雙方全文；
   另 207 對（規則二）之未生成側，我讀的是 `section_fulltext.tsv` 之條文，
   不是該節將來的 TC。** 兩者粒度不同，如實記之。

---

## 9. 建議 commit message（git 未執行）

```
feat(comfort): R-C38 third BLOCKED marker; ch2<->ch7 mirror map

- paste R-C38 into RULINGS.md and add profile §5.2/§5.3: [BLOCKED-NON-HMI]
  for a leaf that delegates to nobody and observes nothing. §5.3 carries a
  decision ORDER, not just a difference table — 29 §1.5 proved 044-02 was
  not [BLOCKED-SPEC] and still picked the wrong alternative
- emit 044-02 as that row (NR1L-ComfortHMI-081, tc_id pinned so -067..-080
  do not renumber); whitelist it; register DATA_REQUESTS #24 for the
  Manual UI Testing / no-UI-quantity mismatch
- lint: two markers, and their Remarks checks are opposites — a
  [BLOCKED-NON-HMI] that names an Owner is a [BLOCKED-SPEC] in disguise
- build data/ch2_ch7_mirror_map.tsv: 26 rows, ch2's 22 and ch7's 11 sections
  both listed in full (the handoff said 12; measured 11)
- judge all 231 class-invalidated pairs individually. Three are siblings —
  2.12 / 2.12.1 / 2.12.2 <-> 3.1, all on the tri-mode axis; C13.0 defines
  itself as "In some non-tri mode equipment types"
- reword the four surviving classes to not-broken-by-3-samples (class)
- review the 7 TCs whose 037 leaf carries images: -076's three do not depend
  on them, -023's three do, in one specific part — C19 never defines how a
  tri-mode button's ON state is shown
- lint 41/41 PASS across 81 TCs; no write-back
```

---

## 10. 待分析層

1. **§4 末** —— `not-sibling` 之回訪機制：gate 改盯「對造節未生成之全部列」？
2. **§3.1** —— 規則三取不到值：改產生器使「未生成 × 未生成」入表標 `deferred`？
3. **§3.3** —— 第三軸改為三值（連帶 65 條 negation users 之複核）？
4. **§5.3** —— 18 個帶圖 leaf 之清單，待 037 可達；在此之前規則已就位。
5. **§6** —— 五項 coverage hole 候選，開不開 DR。
6. **§8 第 4 點** —— `ch2_ch7_mirror_map.tsv` 之 `mirrored` 是否比照 R-C36-1
   下放至 TC 層。
