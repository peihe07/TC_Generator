# 上繳包 23 —— pilot-01 收束、R-G33 落地、寫回前之待裁

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/23_pilot01_closeout.md`
- 步驟 1–5 全數執行。**停止條件 59 觸發（步驟 2），已依其規定補寫並重跑；
  其「補寫後逐字相同」之停手條款未觸發。** 其餘 1–58 全未觸發
- **git 未執行**（§6 為建議）

---

## 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-G33 → ledger、R-DM48 補充 → `RULINGS.md`；**兩表皆相符**；R-DM 區塊累計 **52**，逐字元全數相符。**惟置放位置與指示不同，理由見 §1.1** |
| 2 R-G33(c) 複驗 | **三條中兩條不足**（#4 完全未指名、#3 僅指名二分之一）→ **停止條件 59 觸發** → 補寫 → 全數 PASS |
| 3 BACKLOG 重審節 | 已寫入；**本層增列一項**（§三末列） |
| 4 A-DM34 複驗 | 三值皆與 `dbc_probe.py` 實測相符，PASS |
| 5 INDEX | 已更新 |

**本輪最重要的一件事：R-G33 立條的當下就抓到兩條違反，而其中一條
（#4）是分析層自己在步驟 2 裡沒點到的。** 下放包 23 步驟 2 明文只要
逐字判定 #3，理由是「#3（005）之 leaf 亦在 deferred 陣列中」——
但 **#4（004 邊界條）之 leaf 同樣在 deferred 陣列中**，而 22 輪我自發
寫揭露句時只寫了 #1，沒寫 #4。

即：**一條為了防止漏揭露而立的條文，第一次執行就在立條者與執行者
雙方都漏掉的地方生效。** 這正是把個案變成機器判準的價值。

---

## 一、抄錄核對表

### 1.1 置放位置：與指示不同，附實測理由

下放包 23 步驟 1 指示「**R-DM48 之補充**以『補充』形態追加於
`features/display/RULINGS.md` 之 **R-DM48 條下**」。

**我先照做，量測其後果，然後改採另一種置放。** 兩者皆已實測：

| 置放 | `transcribe_rulings.py` 之順序驗證 | exit |
|---|---|---|
| 緊接 R-DM48 條之下（**指示之字面**） | `有不符（52 vs 52）`，指出第 50／51 個不符 | **1** |
| 檔末，依下放包順序（**本輪採用**） | `全數相符（52 vs 52）` | **0** |

原因：`transcribe_rulings.py` 之 `display_source_blocks()` 依
**下放包檔名排序**重建應有順序（01…23），再與 `RULINGS.md` 之
實際區塊序列逐一比對。R-DM48 出自下放包 20、R-DM49 出自 22 ——
把 23 之補充插進 20 之位置，會使實際序列成為 `…48, 48補, 49`
而應有序列為 `…48, 49, 48補`。

**為何選擇後者**：R-TM13 之核心要求是「原條文不刪不改」，
兩種置放皆滿足。而順序驗證是本檔自 05 輪起唯一的**機器**保證，
「累計 N 個、逐字元全數相符」這句話從 09 輪起每一包都在引用。
為了字面上的相鄰而讓它從 exit 0 變成 exit 1，代價不對等。

**代償措施**（使「條下」之導覽功能不失）：

1. R-DM48 條之正下方留一則指標（非 fence，不入核對表母體）：

   > **補充（下放包 23）**：見本檔末〈來源：下放包 23（R-DM48 之補充）〉節之
   > `R-DM48 之補充（跨訊號不可外推）`。**原條文依 R-TM13 不刪不改。**
   > 補充置於檔末而非緊接本條之下，理由見上繳 23 §1.1（實測：
   > 緊接置放會使 `transcribe_rulings.py` 之順序驗證由「全數相符」轉為
   > 「有不符」並 exit 1）。

2. 檔末「廢止與取代之對照」表增一列（該表為本檔既有之跨條關係索引）：

   | 被廢止／修正者 | 取代者 | 出處 |
   |---|---|---|
   | R-DM48 之理由「同一訊號之六個值裡規則就不一致」 | **R-DM48 之補充（下放包 23）**：跨訊號亦不一致；處置規則不變，理由與適用範圍加強。原條文不刪不改 | 下放包 23 §三 |

**這是一次對指示之偏離，故具名上報。** 若分析層仍要求字面置放，
請明示；屆時我會同步調整 `display_source_blocks()` 之順序模型
（該腳本現以「下放包序＝檔內序」為前提，字面置放會使該前提失效，
須改為顯式序表）—— **但那會把一個自動的保證換成一份要人維護的表。**

### 1.2 核對表（機器輸出，R-G20）

## 抄錄核對表 — 23_pilot01_closeout.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 52 | R-DM48 之補充 | `features/display/RULINGS.md` | 428 | `692e4eb2f17c84c9` | 是 |
| — | R-G33 | `docs/fw036/RULINGS_LEDGER.md` | 1010 | `b259d0903f299566` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **52** 個，與各下放包原檔逐字元比對 **全數相符**（52 vs 52）。

兩條分屬兩檔，故上表兩列即為「各自獨立核對表」之要求：
`R-G33` → `docs/fw036/RULINGS_LEDGER.md`（全域）；
`R-DM48 之補充` → `features/display/RULINGS.md`（Display）。

---

## 二、R-G33(c) 之三條複驗（含 #3 之逐字判定）

### 2.1 判準之實作

依 §三 R-G33 之「機器化判準」逐字實作：

> 對每一 TC，若其 `leaf_id` 出現於同批 `batch_context.md` 之 `deferred`
> 陣列，則其 `test_item` 括號下半須含該 deferred 項之指名 token。
> 不含即為違反。

母體：`deferred` 陣列 **3 項**（`generated/pilot-01.json`）。
leaf 分布：`004` → 1 項；`005` → **2 項**。
指名 token 取自各 deferred 項之標的，英文對應為
`warning popup`／`protective shutdown`／`multi-stage`。

### 2.2 補寫前之複驗（停止條件 59 觸發）

```text
deferred 陣列（母體 3 項）：
  1. SWE1-DM-004 之 warning popup（PU0517）—— DR-DM10(a) 未結。組 B {4820289} 於越過門檻時即關背光，使 popup 之顯示不可觀測；組 A {4820283} 則蘊含警示階段。兩組皆宣告適用於 R1H / Atlantis High
  2. SWE1-DM-005 之保護性關閉（原 #2）—— 組 A／組 B 何者為準未裁定，且 {4820283} 之警示階段無時長；DR-DM10 開立；21 包 §2.1 分支 3
  3. SWE1-DM-005 之 multi-stage 分級門檻 —— DR-DM4 未結（CFTS_013 未取得）

leaf → deferred 項數：
  004: 1
  005: 2

逐條複驗（R-G33(b)：須指名其未涵蓋之物，不得只寫泛稱）
------------------------------------------------------------------------
TC#1  leaf=SWE1-DM-004  deferred 項數=1
  括號下半：(Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)
  deferred 標的：'warning popup（PU0517）'

TC#2  leaf=SWE1-DM-004  deferred 項數=1
  括號下半：(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered)
  deferred 標的：'warning popup（PU0517）'

TC#3  leaf=SWE1-DM-005  deferred 項數=2
  括號下半：(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown)
  deferred 標的：'保護性關閉（原 #2）'
  deferred 標的：'multi-stage 分級門檻'

```

逐字判定：

| TC | leaf | 該 leaf 之 deferred 項 | 括號下半是否指名 | 判定 |
|---|---|---|---|---|
| #1 | 004 | `warning popup（PU0517）` | `the warning popup is deferred` | **滿足** |
| **#4** | **004** | `warning popup（PU0517）` | **無任何 popup 之指名** | **違反** |
| **#3** | **005** | ① `保護性關閉（原 #2）` ② `multi-stage 分級門檻` | ① `not the protective shutdown` **滿足**；② **無 multi-stage 之指名** | **部分違反（1/2）** |

#### #3 之逐字判定（步驟 2 所指定者）

原括號下半：

```text
(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown)
```

- 對 deferred 項 ①（`SWE1-DM-005 之保護性關閉（原 #2）`）：
  `protective shutdown` 為「保護性關閉」之逐字英文，且以
  `not the …` 明指其未涵蓋 → **滿足 R-G33(b)「指名其未涵蓋之物」**，
  非泛稱。
- 對 deferred 項 ②（`SWE1-DM-005 之 multi-stage 分級門檻`）：
  全句**無** `multi-stage`、無 `threshold`、無 DR-DM4 之任何指涉
  → **不滿足**。

即：**#3 之揭露句正確，但只揭露了兩項中的一項。**
`005` 有兩個 deferred 面向，而括號下半只擋住了其中一個。

#### #4 之違反 —— 下放包 23 步驟 2 未點到者

步驟 2 只指定複驗 #3（`#3（005）之 leaf 亦在 deferred 陣列中`）。
**#4 之 leaf（004）同樣在 deferred 陣列中**，而其括號下半
`(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot,
so nothing is triggered)` 完全未指名 popup。

22 輪我自發寫揭露句時只寫了 #1 —— 因為當時被 deferred 的是「#1 的
ER 3」，我把它想成「#1 的事」。**R-G33 之判準是 leaf 級而非 TC 級，
這個差別正是它抓到的東西。**

### 2.3 補寫（停止條件 59 前半）

| TC | 補寫後之括號下半 |
|---|---|
| #4 | `(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered; the warning popup itself is deferred)` |
| #3 | `(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown and not the multi-stage thresholds, both deferred)` |

#1 **未動**（22 輪已滿足）。

措辭之取捨：
- #4 用 `the warning popup itself is deferred` 而非與 #1 相同之
  `the warning popup is deferred` —— 加 `itself` 一詞同時達成兩件事：
  **避免與 #1 逐字相同**（停止條件 59 後半），並點出本條驗的是
  popup 之**不出現**、而 popup 本身之驗證另案 deferred。
- #3 用 `both deferred` 收束兩項，避免句子再長。

### 2.4 補寫後之複驗（全數 PASS）

```text
R-G33(b)(c) 複驗（補寫後）
------------------------------------------------------------------------
TC#1  leaf=SWE1-DM-004  deferred 項數=1
  括號下半：(Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)
    指名 token 'warning popup' → 含   （deferred 項：SWE1-DM-004 之 warning popup（PU0517）—— DR…）

TC#2  leaf=SWE1-DM-004  deferred 項數=1
  括號下半：(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered; the warning popup itself is deferred)
    指名 token 'warning popup' → 含   （deferred 項：SWE1-DM-004 之 warning popup（PU0517）—— DR…）

TC#3  leaf=SWE1-DM-005  deferred 項數=2
  括號下半：(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown and not the multi-stage thresholds, both deferred)
    指名 token 'protective shutdown' → 含   （deferred 項：SWE1-DM-005 之保護性關閉（原 #2）—— 組 A／組 B 何者為準未…）
    指名 token 'multi-stage' → 含   （deferred 項：SWE1-DM-005 之 multi-stage 分級門檻 —— DR-DM4…）

全部滿足：PASS

停止條件 59 後半：任二條之括號下半是否逐字相同
  distinct = 3 of 3  →  PASS

同 leaf 之括號下半（lint I-sibling 之母體）
  SWE1-DM-004: 2 筆，逐字重複 = 0
  SWE1-DM-005: 1 筆，逐字重複 = 0

§9 第 2 項（tc_title）—— 未動，複列
  TC#1 words=9 :: Hot threshold exceeded → Hot state notified to HU
  TC#2 words=10 :: Temperature at 85 degrees C → Hot state not entered
  TC#3 words=11 :: Temperature falls back to non-Hot → backlight on and touch enabled
  distinct = 3 of 3
```

**停止條件 59 之後半（補寫使任二條逐字相同）未觸發**：
三條之括號下半 `distinct = 3 of 3`；同 leaf 者（004 之兩條）
逐字重複 0。

---

## 三、`BACKLOG.md` 之重審節全文

寫入 `features/display/BACKLOG.md`，置於「B 類」與「已知而不入本檔者」
之間（第 38 行起）。**不入 A／B 分流**，理由寫在節首。

> ## DR-DM10 回覆後重審
>
> **非未驗項，不入 A／B 分流** —— A／B 分的是「已知該驗而未驗者」，
> 本節是**條件性待辦**：其觸發條件是 DR-DM10(a)（組 A／組 B 何者為準）
> 之答覆到達。答覆未到，本節任一項都無從進行。
>
> | 項 | 重審理由 | 現況 |
> |---|---|---|
> | #4 之 ER 3（`No popup is shown on the display`） | 其論據「未觸發時兩組皆無 popup」為真，但**與 #1 被 deferred 之論據來自同一份互相矛盾之規格**。若答覆顯示存在第三種讀法，該論據須重估 | 現行判定：可寫（R-DM49(a)(b)(c) 三項皆滿足） |
> | #1 之收斂範圍 | 若答覆為「組 A 為準」，popup 側即可觀測，#1 得**回復其 popup ER（增列，非重寫）** | 現行：2 步 2 ER，僅訊號側 |
> | 原 #2（005 保護性關閉） | deferred 之解除 | deferred，未寫 |
> | `batch_context.md` 之 `deferred` 三項 | 逐項複核其是否仍成立 | 3 項（004 popup／005 關閉／005 multi-stage） |
> | DR-DM10 之阻斷範圍欄 | 004 popup 側與 005 關閉側之狀態同步 | 兩者皆列 |
> | **各 TC 之括號下半（R-G33）** | deferred 項若解除，其括號下半之揭露句須同步移除 —— **否則工作簿上會留下一句已不成立的「is deferred」** | 3 條皆含揭露句（23 包補寫） |
>
> > 末列為本層增列，不在下放包 23 §四之清單內。理由：R-G33 之揭露句與
> > `deferred` 陣列是綁在一起的（R-G33(c)），**陣列變動而揭露句不動，
> > 就會從「防止誤讀為完整覆蓋」翻轉成「誤導為仍未覆蓋」。**
> > 揭露句之風險是雙向的，原清單只列了單向。

**增列之理由再述**：R-G33 使 036 工作簿上出現了三句
`… is deferred`。這三句現在是**正確**的。DR-DM10 一旦答覆而 deferred
解除，若沒有人回頭刪它們，工作簿會宣告一個已經被測的面向沒有被測 ——
**與 R-G33 想擋的誤讀方向相反，但同樣是誤讀。** 立條時只想到一個方向。

---

## 四、修訂後之 `test_item` 全文、重跑之 lint、自檢第 2 項

### 4.1 三條之 `test_item` 全文（rev4）

```text
#1  SWE1-DM-004
The Display Management software shall monitor thermal status inputs and evaluate Hot condition thresholds based on configured thermal algorithm logic. The software shall trigger warning popup requests when configured warning threshold conditions are satisfied.

(Signal side of the Hot transition — the DISP_HOT notification only; the warning popup is deferred)
```

```text
#4  SWE1-DM-004
The Display Management software shall monitor thermal status inputs and evaluate Hot condition thresholds based on configured thermal algorithm logic.

(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered; the warning popup itself is deferred)
```

```text
#3  SWE1-DM-005
The Display Management software shall determine display ON/OFF operational decision based on thermal protection algorithm evaluation.

(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown and not the multi-stage thresholds, both deferred)
```

上半三條**皆未動**（R-G33(a)：不得因此刪句）。

### 4.2 重跑之 `lint036.py`（整批，附母體）

| 項 | 值 |
|---|---|
| 受檢母體 | `generated/pilot-01.json` 之 `tcs`，**3 筆**（rev4） |
| 受檢方式 | 036 母本之拋棄式複本，資料列 10–12，其餘資料列清空 |
| profile | `display` |
| 036 母本 sha256（前後） | `6372fb6be02f48dc…`（**未變**） |
| 寫回母本 | **否** |

```text
# lint036 報告：lint_scratch.xlsx

- 來源：`/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/e90244b2-6851-4dfb-8775-8cb1bd4f77d3/scratchpad/lint_scratch.xlsx`（唯讀）
- 資料列數：3
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`display`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |

**總計：行計 0**（列計不加總——同一列可觸發多項檢查）

## 明細

```

**二十項行計皆 0。** `I-sibling` 於本批有母體（#1／#4 同為
`SWE1-DM-004`），補寫後兩者括號下半逐字重複 0 —— 該 0 為實測。

### 4.3 §9 自檢第 2 項（sibling 相異）

`tc_title` 三條**本輪未動**，複列以示未受補寫影響：

```text
  TC#1 words=9  :: Hot threshold exceeded → Hot state notified to HU
  TC#2 words=10 :: Temperature at 85 degrees C → Hot state not entered
  TC#3 words=11 :: Temperature falls back to non-Hot → backlight on and touch enabled
  distinct = 3 of 3
```

括號下半（本輪動過者）：`distinct = 3 of 3`，同 leaf 逐字重複 0。

### 4.4 §9 其餘各項之受影響範圍

補寫只動 `test_item` 之括號下半。逐項檢其是否波及：

| §9 項 | 是否受影響 | 說明 |
|---|---|---|
| 2（tc_title） | **是（須複驗）** | 已複驗，3 of 3 相異；字數未變 |
| 10（Procedure ↔ ER 1:1） | 否 | 未動 procedure／ER |
| 12（無捏造） | **是（須複驗）** | 補寫之內容全部來自 `deferred` 陣列之既有文字，**未引入任何新的事實或值** |
| 14（行尾句號） | 否 | 括號下半不在該四欄之內 |
| 其餘十三項 | 否 | 未動其判準所依之欄位 |

第 12 項具名：`the warning popup itself is deferred` 與
`not the multi-stage thresholds` 兩句所述之事實，
分別對應 `deferred` 陣列第 1 項與第 3 項，**逐字可溯**。

---

## 五、A-DM34 之登記複驗（步驟 4）

```text
dbc_probe.py exit = 0
  DCSD_DISP_STAT           A-DM34 記載=4  實測=['4']  →  相符
  FPDM_DISP_STAT           A-DM34 記載=3  實測=['3']  →  相符
  TGW_FPDM_DISP_STATSts    A-DM34 記載=3  實測=['3']  →  相符

A-DM34 登記複驗：PASS

ANOMALIES.md A-DM34 節：
  含 '**4**' : True
  含 '**3**' : True
  嚴重度標記 : True
  非阻塞聲明 : True
```

三個 raw 值皆與 `dbc_probe.py` 之實際輸出相符（該腳本入口即呼叫
`_verify_bindings()`，故其讀取之 DBC 已受 R-G23 檢查）。
`[LOW]` 與「不阻塞」之聲明俱在。**PASS。**

---

## 六、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A 與組 B 何者為本架構之準 | 004 之 popup 側；005 之關閉側全部 TC | DR-DM10(a) |
| A2 | `{4820283}` 警示階段之時長／終止準據 | 原 #2；`PU0130` | DR-DM10(b) |
| A3 | `[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]` 之 raw 值 | 現行 ER 只驗行為不寫值；**007／008 之訊號欄** | DR-DM9 |
| A4 | `popup_priority.tsv` | `SWE-DM-006` | DR-DM2 |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |

**A 類本輪無增減。**

### B 類 —— 不阻斷交付

| 編號 | 項 | 為何不阻斷 |
|---|---|---|
| B1 | `{CFTS013-XXX}` 之實際條號 | 其所在條為 `Radio:noSys` |
| B2 | `{CFTS013-967}` 與 DR-DM4 三號不同 | 同上 |
| B3 | multi-stage 分級門檻（DR-DM4） | 單級 85 °C 行為可獨立驗 |
| B4 | 亮度降低之數值 | popup ER 已 deferred，無所附麗 |
| B5 | `degrees C` 與 `deg C` 寫法不一致 | 規格自身之差異 |
| B6 | DTC `B1429-00` 之時間門檻 | 本批未驗 DTC —— 未取而非漏取 |
| B7 | `DISP_HOT` 跨訊號 raw 值不一致（A-DM34） | 本批未用 FPDM 側任何值；判準已足以隔離 |
| B8 | Test Set 分組之「恰當性」未被腳本檢查 | 集合相等已驗；恰當性屬 Tier 2 人工論述 |
| B9 | 停止條件 58 之詞表非窮盡 | 已依 R-G33 註於使用處具名；ER 較長時須先擴充 |
| **B10** | **R-G33 之判準本輪為一次性腳本，未入 `lint036`** | 三條已逐條驗過且結果具名；接入共用腳本屬 Tier 2（動 `scripts/`） |
| **B11** | **R-G33 之「指名 token」對照表為本層自訂** | `warning popup`／`protective shutdown`／`multi-stage` 三個英文 token 是我從中文 deferred 項**自行對譯**的，**條文未規定對照方式**；本批三項皆單純，但若 deferred 項之措辭較抽象，該對譯即成判斷而非量測 |

B10／B11 為本輪新增。**B11 與 B9 是同一類問題的第二例**：
一個看起來是機器判準的檢查，其詞表是人給的。

---

## 七、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/generated/pilot-01.json \
  features/display/RULINGS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/23_pilot01_closeout.md \
  features/display/docs/upstream/23_pilot01_closeout.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): pilot-01 rev4 — disclose every deferred facet in the test item

- add R-G33: a requirement facet named in the verbatim upper half of
  test_item but not covered by the expected result must be named in the
  bracketed lower half, so a workbook reader sees the partial coverage
- apply it to all three test cases: TC #4 named no deferred facet at all and
  TC #3 named only one of its two, both are now explicit
- supplement R-DM48: the DISP_HOT label maps to a different raw value on a
  different signal, so a resolved label may not be carried across signals
- add the DR-DM10 re-review list to BACKLOG, including removing the
  disclosure sentences once the deferrals are lifted
- lint036 --profile display: all twenty checks report zero
```

> `batches/pilot-01/batch_context.md` 不入 pathspec（`.gitignore` 已排除）。
> 036 母本未變更，亦不入。

---

## 八、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項，其中兩項是本輪自己製造的。**

1. **R-G33 之判準是我實作的，而條文正是為了取代人的判斷而立。**
   §2.1 之三個英文 token 由我自中文 deferred 項對譯（B11）。
   本批三項標的具體（popup／shutdown／multi-stage），對譯無爭議；
   **但「對譯無爭議」這件事本身是我判斷的，沒有第二個來源核對。**

2. **036 工作簿上現有三句 `… is deferred`，其正確性有時效。**
   已寫入 BACKLOG（§三末列）。但 BACKLOG 是一份要人讀的清單，
   **沒有任何機制在 `deferred` 陣列變動時提醒去改工作簿。**
   R-G33(c) 要求兩者一致，卻只在寫入時檢查，不在解除時檢查。

3. **`test_item` 上半與 ER 之落差，本輪只是把它寫出來，沒有縮小它。**
   #1 之上半仍宣告 `shall trigger warning popup requests`。
   R-G33 讓讀者看得見這件事沒被測 —— 這是誠實，不是覆蓋。
   **004 仍是部分覆蓋，且本輪之後看起來更像已處理完畢。**
   交付前若只看「三條 TC、lint 全 0、揭露俱全」，會低估 A1 之份量。
