# 上繳包 24 —— Vehicle Category：`038-03` 補拆 ＋ 第 5 批勘查（T126–T128）

- 日期：2026-08-26
- 對應下放：`docs/handoff/24_batch5_survey.md`
  （SHA256 `052ede70f1bd5ed6441431443b284e50ad4aed1678a9465b64a577e6175cfb75`，120 行）
- **結論：T126／T127 完成，第 4 批 16 → 17 筆，收斂 20 項全過、五批回歸全綠。
  T128 勘查完成，未生成任何 TC。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T126 | `038-03` 拆 2 | ✅ 17 筆，`split_delta: 2`；第三層 `已驗 3 條`（拆後二筆各驗）|
| T127 | `split_flag` 明文 | ✅ profile §11 |
| T128 | 第 5 批勘查 a–g | ✅ **二個新異常：A-VC18／A-VC19；新立 DR-VC10** |

**三件請你先看**：
1. **`PU0091` 之彈窗文字，規格作 `Feature`、彈窗清單與設定清單作 `Function`**
   —— 二份獨立來源對規格一份，且影響二筆 **P0** 之 ER。**A-VC18／DR-VC10**。見 §3.3。
2. **`058`／`064` 各對應一個實體彈窗，且其 `Exit Conditions` 恰好佐證了規格的話**
   —— `PU0237` 為 `<X>/<OK>`、`PU0319` 為 **`N/A`（不可關閉）**。
   這不是異常，是**規格與彈窗清單對得上的一次**。見 §3.4。
3. **拆分判準：本輪提出「互相消耗」為既有判準之外的第三個充分條件** ——
   它正是 `038-03` 覆蓋洞的成因，且能一致解釋前四批之既有處置。見 §4.2。

---

## 1. T126 —— `038-03` 拆 2

### 1.1 你的推翻我接受，且理由比我的判準好

我在上繳包 23 §5 判「同一規則之二個邊界」而不拆。
**你的問法是對的：「這個失效，現有哪一筆會 FAIL？」——「完成時彈窗不消失」，沒有。**

我的判準停在**規則層面**（規則是「不自行消失」，二個離開條件是它的邊界），
你的判準走到**覆蓋層面**（Procedure 只走了 X，完成那條路沒有任何步驟踩過去）。
規則層面成立不蘊含覆蓋層面成立 —— **這是我沒走完的一步**。

### 1.2 落實

| 筆 | 括號下半 | Procedure 之離開路徑 |
|---|---|---|
| `038-03`(1) | `Persistence -- the user-action exit, the pop-up leaves on X` | 按 X |
| `038-03`(2) | `Persistence -- the system-completion exit, the pop-up leaves with no user action` | 等待系統完成，**明文不按任何鍵** |

第 2 步之 `without pressing any control on the pop-up` 是必要的 ——
否則離開可能由使用者動作促成，**二筆就在驗同一件事**。

新筆之 CONT 承襲 `resolution=PC`／`resolution_key=pop-up`。
第三層對同一 leaf 之**每一筆 TC** 各驗一次，故 `已驗` 由 2 升為 3：

```
已驗 3 條 [('SWE1-HMI-VC-038-03', 'PC', 'pop-up'), ('SWE1-HMI-VC-038-03', 'PC', 'pop-up'), ('SWE1-HMI-VC-038-04', 'Step', 'pop-up')]；待生成 1 條 [('SWE1-HMI-VC-064-02', 'PC', 'pop-up')]；不符 0 條 無
```

`split_delta` 1 → **2**；第 15 項驗宣告值與自 `tcs` 實際數得之增量相符：

```
tcs=17；leaf_scope=15；宣告 split_delta=2；實際拆分增量=2（{'SWE1-HMI-VC-038-03': 2, 'SWE1-HMI-VC-038-05': 2}）；held=0（b 段不計入母體）
```

### 1.3 連帶實益（你在 §1.3 指出者）已落入 reasoning

`038-05` 未完成支第 3 步等到完成後驗「選項不再灰」——
補拆後「完成 → 彈窗消失」成為該步之明確前置，
該步若 FAIL 不再混淆（灰化未解 vs 彈窗未關）。已逐字記於新筆之 `reasoning`。

---

## 2. T127 —— profile §11

`split_flag` 恆 `False`、`split_reason` 恆空，明文入 profile。
**現況實測**：全 **99** 筆 TC 皆如此，其中 **8 筆為拆分之產物**
（`046-05`／`048-02`／`038-03`／`038-05` 四個 leaf 各 2，`split_delta` 合計 4）。

**已記明其未機器化** —— 無檢查項驗「恆 `False`」；
其違反不會被攔，只會使該欄成為第二個拆分來源。

---

## 3. T128 —— 第 5 批勘查

### 3.1 (a)(b) 基本盤

16 leaf，**priority P0 2 ／ P1 10 ／ P2 4**。
**037 之 `Priority` 欄 16 筆全為 `High`** —— 本地判準之分化全由 R-VC11 產生。

| 節 | leaf | 標的 |
|---|---|---|
| 13.1 | `057` | Settings 頁籤於 Key Off／Timed Mode／ACC 不可用 |
| 13.1.1 | `058-01`／`-02`／`-03` | 嘗試進入時之彈窗、其不逾時、其關閉後之落點 |
| 13.2 | `059-01`／`-02` | Phone settings 之路徑與其 Key Off／ACC 可用 |
| 13.3 | `060-01`／`-02` | Audio settings 之路徑與其 Key Off／ACC 可用 |
| 13.4 | `061` | Software Updates 於 Key Off／ACC 可用 |
| 13.4.1 | `062-01`／`-02` | 行進中按 Wi-Fi 下載設定之攔阻彈窗、其離開 |
| 13.4.2 | `063-01`／`-02` | FOTA 流程中起步之攔阻彈窗、其離開 |
| 13.5 | `064-01`／`-02`／`-03` | 開啟中途轉 Key Off 之彈窗、其不可關閉、其自動解除 |

**FROP 實測**：`057`–`061`／`064-*` 為 `Power Management`（12 筆），
**`062-*`／`063-*` 為 `Vehicle Settings`（4 筆）** ——
下放包 §3.1 稱「FROP = Power Management **全批**」，
**實測不符：本組非單一 FROP。**（R-VC16(e) 之一對一主張須以成員比對為據，
本處即以成員比對更正。不阻斷生成，記於此以免表 A 之填寫沿用該敘述。）

**狀態定義**：`057`（tab 不可用）與 `059-02`／`060-02`／`061`（他路徑可用）
**並存不悖** —— 沿上繳包 22 §2 之路徑解，生成時不視為例外。

### 3.2 ⚠ (b) `061` 之進入路徑未載 —— **A-VC19**

章 13 為三個「他路徑仍可用」之需求給出路徑，**獨缺其一**：

| leaf | 路徑 |
|---|---|
| `059-*` | ✅ §13.2 `through the Phone screens` |
| `060-*` | ✅ §13.3 `through the Media` |
| **`061`** | ❌ **只斷言可用，未載經何路徑** |

且 `Software Updates` **實測為 Settings 清單之第 27 類**
（`HMI Settings List` 第 650 列），即它本來就在被 §13.1 擋住的頁籤後方。
SYS1 全表搜 `Software Update|FOTA|Wi-Fi` **僅命中 §13.4／13.4.1／13.4.2**，
三節皆無路徑；設定清單該列作 `See Software Updates Logic and Flow for logic`
—— **委派至本 feature 未持有之文件**。

`061` 為 P1，其 TC 需要一條可走的路。**處置提案：沿 `034-02` 之既有裁定**
（查得則具名、查無則以規格語言之通稱表述），**不新立 DR**。
若你認為此處應發 DR，A-VC19 即其素材。

### 3.3 ⚠ (c) `PU0091` 之文字二源相左 —— **A-VC18／DR-VC10**

| 來源 | 逐字 |
|---|---|
| SYS1 §13.4.1／§13.4.2 ＋ 037 `062-01`／`063-01` | `“**Feature** not available while vehicle is in motion”` |
| `Pop Up List HMI R1 (26PI)` `Main` 第 93 列 `String/Popup Message` | `**Function** not available while vehicle is in motion**.**` |
| `HMI Settings List` 第 150 列 | `"**Function** not available while vehicle is in motion"` |

**二份獨立來源作 `Function`，規格側作 `Feature`；且句末句點有無亦異。**

**為什麼不能擇一**：`String/Popup Message` 欄**就是彈窗的字**，不是對它的描述；
而 `062-01`／`063-01` 皆為 **P0**（行進中攔阻，safety 型），
其 ER 之標的正是「該彈窗出現且文字為何」。取 `Feature` 則與實機可能不符，
取 `Function` 則與其 `specification_reference` 所指之原句不符。**§8.4.1 禁自行認定。**

**處置**：四筆（`062-01`／`-02`／`063-01`／`-02`）之 ER 帶
`PENDING: DR-VC10 PU0091 popup string`。**第 5 批因此非全潔批。**

### 3.4 (c) `058`／`064` 之彈窗實體查得 —— **非異常，是對得上的一次**

| leaf 群 | PU | `Timeout` | `Exit Conditions` | 文字 |
|---|---|---|---|---|
| `058-01`~`-03` | **PU0237** | `N/A` | `<X>` `<OK>` | `Turn vehicle to Run or Key On to access menu.` |
| `064-01`~`-03` | **PU0319** | `N/A` | **`N/A`** | 同上（逐字相同）|

`PU0237` 之 `Description` 作「若在 ACC／Timed Mode／Key off：不可用之類別
於其列項被選取時顯示彈窗」；`PU0319` 之作「在 RUN 之後轉 Key Off 或 ACC…
**彈窗顯示且無法被關閉**」。

**三項佐證**：
1. `058` 與 `064` **確為二個不同彈窗**（文字相同、行為不同）—— 規格把它們寫在二節是對的。
2. `PU0319` 之 `Exit Conditions` = **`N/A`**，逐欄佐證 `064-02` 之
   `cannot be closed by the user`。
3. 二者 `Timeout` 皆 `N/A`，佐證 `058-02`／`064-02` 之「不逾時」。

**惟 PU 編號未載於 SYS1／037**（不同於 `PU0091` 之明載）——
故**只入 `reasoning` 作追溯佐證，不入 ER**（沿 DR-VC1 對 `VC-021` 之 `PUXXXX` 分寸）。

### 3.5 (d) CONT 判定 —— 列冊二筆已判，**另發現四筆第一層偽陰性**

**已登記（列冊 → CONT）**：

| leaf | 節 | 句 | 層次 | resolution |
|---|---|---|---|---|
| `058-02` | 13.1.1 | **`1-2`** | **層次 1** —— s1+s2 = **43 token，未逾 50** | 空 |
| `064-02` | 13.5 | **`2`** | **層次 2** —— s1+s2 = **54 token，逾 50** | `PC` / `pop-up` |

**層次不得跳層**（profile §9.2）—— `058-02` 之整段未逾限，故**不採第三處置類**，
即使它與 `064-02` 看起來是同一種句子。二筆之差別只在 s1 之長度（37 vs 42 token）。

`cont_deferred.tsv` 至此**清空**（只剩表頭）。第二層 10 條全過。

**另四筆為第一層看不到之指涉**（由勘查 (d) 之 SYS1 對照發現）：

| leaf | 逐字 | 為何第一層看不到 |
|---|---|---|
| `058-03` | `Closing the pop-up with ‘X’ or ‘OK’ returns…` | `the pop-up` 為定冠詞回指，非代名詞起首 |
| `062-02` | `If they press ‘OK’ or ‘X’ they will be returned…` | `they` 非句首（句首為 `If`）|
| `063-02` | 同上句型 | 同上 |
| `064-03` | `If vehicle is turned to Run or Key On while pop-up is on screen…` | `pop-up` 無冠詞，非代名詞 |

**我未自行登記** —— T128(d) 只授權判定列冊之二筆。四筆之判定請裁。
**我的看法**：四筆之指涉皆可由 TC 結構承載（其先行詞為該 TC 必然建立之彈窗），
且四筆之 037 `Description` 與 SYS1 對應句**逐字相同**，
**登記與否不改上半之字**，只改「這個聲稱有沒有被檢查」。**傾向登記。**

> **第一層之偽陰性至此累計 6 個實例**（`013-02`／`038-04` ＋ 本輪四筆）。
> 其形態穩定：**定冠詞回指、非句首代名詞、無冠詞名詞**。
> 現行二特徵（小寫起首／句首代名詞）**結構上抓不到這三型**。
> 是否擴充第一層，請裁 —— 擴充會提高偽陽性，而**現行之補網是勘查 (d) 之人工對照**，
> 六次都是它抓到的。

### 3.6 (e) 記法

| | 筆數 |
|---|---|
| Title 直單 `'…'` ／ Description 彎單 `‘…’` 或彎雙 `“…”` | **7 筆不對稱** |
| 無引號 | 9 筆 |

不對稱者：`058-01`／`058-03`／`062-01`／`062-02`／`063-01`／`063-02`／`064-01`。
**同 A-VC10 第三面，取材時二欄不得混用。**
`064-01` 之 Title 另含斜線 `Key Off/Timed Mode/ACC`（Description 作 `, ... or`）。

**Title 越界（R-VC24）掃描**：候選 **1 筆** ——
`062-02` 之 Title 含 `Software Downloads Over Wi-Fi`（屬 `062-01`）。
**判為情境脈絡，非行為主張**：Title 之謂語為 `return them to the Settings list`
（本 leaf 之行為），該詞用以定位「哪一個 in-motion 彈窗」。**非越界。**

### 3.7 (f) 拆分壓測 —— 依 §1.3 之覆蓋洞問法

**逐筆施「這個失效，哪一筆會 FAIL？」**，得三筆確有覆蓋洞：

| leaf | 覆蓋洞 | 判 |
|---|---|---|
| `058-03` | 只走 X 則「按 OK 落點錯」無人抓；**按 X 已使彈窗消失，不重建情境走不了 OK** | **拆 2** |
| `062-02` | 同型（OK／X）| **拆 2** |
| `063-02` | 同型（OK／X）| **拆 2** |
| `064-01` | tab 與 category 為二個**範圍**；且 `064-02` 已載該彈窗不可關閉，二者間須整輪點火循環 | **拆 2（傾向，請裁）** |

**其餘 12 筆不拆**，其列舉項可於同一流程內以各自之步驟／ER 涵蓋。

### 3.8 ⚠ 拆分判準：本輪提出之第三個充分條件

前四批之既有判準為「**不同觸發／不同輸入／不同範圍**」（IN §402）。
`038-03` 之覆蓋洞顯示還有一個：

```
**互相消耗** —— 列舉之替代項，走了其一即使另一之情境不復存在
（須重建才能走），則單一 TC 之 Procedure 結構上只能走一條，
另一條必然無步驟可踩。**此時不拆即必有覆蓋洞。**

為「拆」之充分條件之一，與既有之三者並存，不取代之。
```

**它一致解釋前四批之既有處置**（本輪回頭驗證，非事後修飾）：

| 既有筆 | 列舉項 | 是否互相消耗 | 既有處置 | 判準是否吻合 |
|---|---|---|---|---|
| `045` | 不逾時 ＋ 選取後不關閉 | 否（同一畫面可連續觀察）| **不拆**，二條 ER | ✅ |
| `049` | < 500 ms ／ > 500 ms | 否（可連續按二次）| **不拆**，二條 ER | ✅ |
| `048-02` | 正面規則 ／ 例外清單 | 否 —— 但**範圍不同** | **拆 2** | ✅（既有判準）|
| `046-05` | 游標移動 ／ 按下選取 | 否 —— 但**行為不同** | **拆 2** | ✅（既有判準）|
| **`038-03`** | 按 X ／ 系統完成 | **是** —— 彈窗被消耗 | 原不拆 → **拆 2** | ✅（本判準）|

**四筆既有處置無一需要改動** —— 新判準只增加一個「拆」的理由，不推翻既有者。

### 3.9 (g) 預估

| | 甲（不拆）| **乙（本輪提案）** |
|---|---|---|
| leaf | 16 | 16 |
| TC | 16 | **19 或 20** |
| `split_delta` | 0 | **3 或 4** |

- **19**：`058-03`／`062-02`／`063-02` 三筆拆（互相消耗，判準明確）
- **20**：另加 `064-01`（tab／category 之範圍拆，**請裁**）

**a 段 16、b 段 0。**
**PENDING 4 筆**（`062-01`／`062-02`／`063-01`／`063-02`，皆為 DR-VC10）
—— **本批非全潔批**。

---

## 4. 收斂與回歸

### 4.1 第 4 批 17 筆

```
verify_batch — batch4_settings_behavior.json（收斂條件；下放包 10 §四 ＋ 13 §4.4）
  #  條件                                                             判
------------------------------------------------------------------------------------------------
  1  17 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                           PASS
     TC 數 17；缺 key 無
  2  IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）                        PASS
     本腳本不代替逐項判讀，見上繳包 10 §4.2
 11  pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled） PASS
     default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）              PASS
     命中 0 處 無
  3  test_item 括號下半 17 筆兩兩不同（機械）                                    PASS
     缺括號 無；重複 無；相異 17
 3b  test_item 括號下半無中文（R-S4）                                        PASS
     含中文 無
  4  specification_reference 17 筆與 recon_leaf_to_section.tsv 逐字相符   PASS
     不符 0 筆 
  5  priority 17 筆與 priority_final.tsv 逐字相符                         PASS
     不符 0 筆 
  6  Test Set 17 筆一致，Test Group 皆為 `Vehicle Category`               PASS
     test_set=['Settings Behavior']；test_group=['Vehicle Category']
  7  尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）                                 PASS
     尾句號 0；單引號 0；方括號角括號 0；空白 0
 7b  test_item 上半為來源之逐字子串（R-VC23(c)；整段，不倚樣式表）                       PASS
     取材來源分布 {'Description': 12, 'Title': 2, 'SYS1': 1}；未對上來源 0 筆 無
  8  PENDING 之分布與其字串（pilot 專屬；他批以第 8b 項驗）                           PASS
     033-01 之 PENDING 數 None；字串相符 False；他筆帶 PENDING 無
  9  `028-02`／`033-01` 之括號下半明載其流程（pilot 專屬）                         PASS
     未載者 無
 10  `VC-021` 之委派（pilot 專屬；本批不適用）                                   PASS
     N/A
  A  Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 步驟無 observe/verify 起首 PASS
     步數不足 無；1:1 不符 無；ER 含 modal 無；禁用起首動詞 無
 13  該批 Test Set 全筆一致且與 framework.md §2 逐字相符                        PASS
     批內 test_set=['Settings Behavior']；framework §2 之 8 組=8 個；相符=True
 14  常數之變體擴散（正規化後相等而原字不同 → FAIL；§5.3）                               PASS
     profile 常數（展開後）3 條；變體 0 處 無
 15  母體 = leaf_scope + split_delta = 15 + 2 = 17（R-VC22(b)／IN §8.2.2） PASS
     tcs=17；leaf_scope=15；宣告 split_delta=2；實際拆分增量=2（{'SWE1-HMI-VC-038-03': 2, 'SWE1-HMI-VC-038-05': 2}）；held=0（b 段不計入母體）
 16  續行型 leaf 之 test_item 上半與 SYS1 完整句逐字相符（R-VC7）                   PASS
     適用 3 筆；不符 0 筆 無
 17  CONT 表二層防護（候選無未處置 ∧ 內容驗證全過；含 self-test）                        PASS
     PASS —— 未處置候選 0；內容不符 0；結構聲稱不符 0；離開碼 0
------------------------------------------------------------------------------------------------
20 checked / 0 failed
```

### 4.2 五批回歸

```
pilot_glovebox                   20 checked / 0 failed
batch1_category_structure        20 checked / 0 failed
batch2_settings_list             20 checked / 0 failed
batch3_controls                  20 checked / 0 failed
batch4_settings_behavior         20 checked / 0 failed
```

**TC 累計 99 筆**（第 4 批 16 → 17）。

---

## 5. 待你裁

1. **DR-VC10 之發送**（A-VC18，`PU0091` 之字）—— 其對象為規格作者與彈窗清單
   維護者，**與同批 A 之 037 作者不同，不宜併入同批 A**
2. **A-VC19（`061` 路徑未載）之處置** —— 提案為通稱表述、不新立 DR
3. **四筆第一層偽陰性之 CONT 登記**（`058-03`／`062-02`／`063-02`／`064-03`）
   ，及**是否擴充第一層之特徵**（§3.5）
4. **`064-01` 是否拆 2**（§3.7）
5. **§3.8 之拆分判準是否採為正式條文**
6. 第 5 批之生成授權（19 或 20 筆）
7. 同批 A（六項）、DR-VC3、DR-VC9(一)（Tier 3）

---

## 6. 進度

**117 leaf 中 96 筆已收斂，TC 累計 99 筆。**

| 剩餘 | leaf | 阻斷 |
|---|---|---|
| 第 5 批 `Ignition Availability` | 16 | 無（DR-VC10 以 `PENDING` 內嵌，不阻斷）|
| 第 6 批 `Brake Service` | 2 | **DR-VC3** |
| 第 7 批 `Cabrio Widget` | 1 | **DR-VC3** |
| b 段 | 3 | **DR-VC9(二)** |

**十筆 DR 全未結。**

---

## 7. 量測條件揭露（R-G8）

### `PU0091`／`PU0237`／`PU0319` 之查得

`Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁**全 1344 列**，
以 `PU0091` 精確比對（唯一命中第 93 列）、
以 `Turn vehicle to Run|Key On to access` 樣式搜（命中 2 列）。
**`Templates`／`Drop Down Fields` 二分頁未逐列讀** ——
前者為版型、後者為下拉欄位，皆不含彈窗字串。

### `061` 路徑之否定性判斷

「SYS1 未載其路徑」為**否定性判斷**，其強度限於已搜之樣式
（`Software Update|FOTA|Wi-Fi`，命中 3 節）與 `HMI Settings List` 之
`Settings` 分頁。**若路徑載於本 feature 未持有之
`Software Updates Logic and Flow`，本判斷不成立** —— 該文件即第 651 列所委派者。

### FROP 之更正

以 037 第 8 欄逐列讀 16 筆得，非抽樣。**與下放包 §3.1 之敘述不符者為實測值。**

### 拆分判準之回頭驗證（§3.8）

四筆既有 TC 之比對**為本輪回頭施行**，非該四筆生成當時之判準。
其結論是「新判準不與既有處置衝突」，**不是「當時就是依它判的」**。

---

## 附錄 A —— `038-03` 拆後二筆全文

### A.1 `VC-038-03`(1) — Pop-up stays until the user presses X

| 欄 | 值 |
|---|---|
| `priority` | P2 ｜ `design_method` | 狀態轉換 (State Transition Testing) |
| `distinguishing_axis` | 離開條件：使用者動作（對完成路徑之時間性離開） |

**`test_item`**

```
This pop-up will stay on the screen until either the system completes changing the voice commands or the user presses X.

(Persistence -- the user-action exit, the pop-up leaves on X)
```

**`pre_conditions`**：`1. The language-change pop-up is displayed and the system has not completed changing the voice commands`

**`test_procedure`**

```
1. Record the screen while the system is still changing the voice commands
2. Press the X button on the pop-up
3. Record the screen again
```

**`expected_result`**

```
1. The pop-up is still displayed
2. The X press is accepted
3. The pop-up is no longer displayed
```

**`reasoning`**：**驗證目標**：彈窗持續顯示，直到使用者按 X 才離開。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2，下放包 23 §2.2）**：`This pop-up` 之先行詞在 SYS1 §11.5 s1，而連續 `1-3` 為 **54 token，逾 R-3 之 50**（profile §10 之工作定義）；非連續 `1,3` 為 42 但破壞 verbatim 之連續性，使第 7b 項與第二層之子串判準對本筆失效。**採單句 s3 ＋ 指涉由 TC 結構承載** —— 其先行詞「語言變更彈窗已顯示」**本即本 TC 驗證持續性之前提**，不解指涉也必須建立它。CONT 登記 `resolution=PC`／`resolution_key=pop-up`，**第三檢查點驗其 pre_conditions 確含該詞**。**⚠ 拆 2（下放包 24 §1.3 之裁定，推翻上繳包 23 §5 之不拆判讀）**：上繳包 23 我判二個離開條件為同一規則之二個邊界而不拆，**分析層以覆蓋洞推翻** —— 不拆之實質後果是「系統完成時彈窗不消失」這個失效**現有 16 筆無一會 FAIL**（本筆之 Procedure 只走 X 路徑；`038-05` 未完成支第 3 步記錄的是語言清單非彈窗）。**判準不是「二觸發」之形式論，是「這個失效哪一筆會 FAIL」。**本筆改為 X 路徑，完成路徑另立一筆。

### A.2 `VC-038-03`(2) — Pop-up leaves when updating completes

| 欄 | 值 |
|---|---|
| `priority` | P2 ｜ `design_method` | 狀態轉換 (State Transition Testing) |
| `distinguishing_axis` | 離開條件：系統完成（對 X 路徑之使用者動作離開） |

**`test_item`**

```
This pop-up will stay on the screen until either the system completes changing the voice commands or the user presses X.

(Persistence -- the system-completion exit, the pop-up leaves with no user action)
```

**`pre_conditions`**：`1. The language-change pop-up is displayed and the system has not completed changing the voice commands`

**`test_procedure`**

```
1. Record the screen while the system is still changing the voice commands
2. Wait until the system has completed changing the voice commands, without pressing any control on the pop-up
3. Record the screen again
```

**`expected_result`**

```
1. The pop-up is still displayed
2. The voice command change runs to completion
3. The pop-up is no longer displayed
```

**`reasoning`**：**驗證目標**：系統完成語音命令變更時，彈窗自行離開，不需使用者動作。**⚠ 本筆為下放包 24 §1.3 所補之覆蓋洞**：第 4 批原 16 筆中，「完成時彈窗不消失」這個失效**無一筆會 FAIL**。**取材同 X 路徑筆**：第三處置類，單句 s3，CONT 登記 `resolution=PC`／`resolution_key=pop-up`。**連帶之實益（下放包 24 §1.3）**：`038-05` 未完成支第 3 步等到完成後驗「選項不再灰」—— 若彈窗該消失而未消失，它可能正擋著清單，該步之 FAIL 原因會混淆（灰化未解 vs 彈窗未關）。本筆使「完成 → 彈窗消失」成為該步之明確前置。**第 2 步之 `without pressing any control`**：離開須由系統完成所致，不得由使用者動作促成 —— 否則本筆與 X 路徑筆驗的是同一件事。

---

> 勘查完成，未生成第 5 批任何 TC。未寫回工作簿、未進行任何 git 操作。
