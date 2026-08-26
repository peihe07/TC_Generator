# 上繳包 23 —— Vehicle Category：CONT 第三處置類 ＋ 第 4 批 16 筆（T121–T125）

- 日期：2026-08-26
- 對應下放：`docs/handoff/23_batch4_tc.md`
  （SHA256 `11b1f9ad46ce9c99a66f7a630e3d8faeb6c3620b9b6db4cab1df4ec945620bca`，141 行）
- **結論：T121–T125 全數完成。第 4 批 16 筆，收斂 20 項全過；五批回歸全綠。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T121 | 第三處置類入 profile；表增二欄；`038-03`／`038-04` 登記 | ✅ **惟 `cont_deferred.tsv` 未依字面清空，見 §1.2** |
| T122 | R-3 之 token 工作定義入 profile | ✅ profile §10 |
| T123 | 第三檢查點 ＋ self-test 前置 | ✅ 斷言增為 **8** 個；反向實測（真實標的）亦過 |
| T124 | 第 4 批 16 筆 | ✅ `generated/batch4_settings_behavior.json` |
| T125 | 收斂 ＋ 五批回歸 | ✅ **20 checked / 0 failed** ×5 |

**三件請你先看**：
1. **`cont_deferred.tsv` 之「清空」若照字面執行，會使 `058-02`／`064-02`
   變成未處置候選而讓第一層 FAIL** —— 我只移除本批之 `038-03`。見 §1.2。
2. **第 7b 之取材分布不是取材決定之紀錄** —— 預期 `SYS1` 3 筆，
   實得 1 筆，因 `038-03`／`038-04` 之 SYS1 句與 037 `Description` **逐字相同**，
   而 7b 依序命中即止。**這不是錯，是該欄位量不到的東西**。見 §4.2。
3. **`split_flag` 沿既有四批之慣例填 `False`** —— 但第 4 批之 `038-05`
   確為拆分。此欄現在四批裡沒有承載任何資訊，請裁。見 §6。

---

## 1. T121 —— 第三處置類

### 1.1 profile §9 為**首次落檔**，非搬移

下放包 23 T121 稱「§2.2 逐字入 profile **該節**」。**該節不存在** ——
收錄判準自下放包 20 §2.1 明文起，一直只在該下放包裡：
profile 無、`RULINGS.md` 無、腳本之揭露段亦無。

故 profile 新增 **§9**，含：
- **§9.1** 二類（下放包 20 §2.1 逐字，`in` 比對通過）
- **§9.2** 第三處置類（下放包 23 §2.2 逐字，`in` 比對通過）
- **§9.3** 登記欄位表 ＋ **`resolution_key` 之逐字要求**
- **§9.4** 三層分工 ＋ **第三層之已知盲區**

**§9.3 之一項自裁請覆核**：下放包舉例為 `resolution_key=popup`，
**我登記 `pop-up`**（SYS1 §11.5 之原文記法）。理由記於 §9.3 ——
若判準容許 `pop-up` 與 `popup` 互通，該欄之保護即退回語意判斷，
而**能被語意判斷放過的東西，正是這個檢查原本要攔的東西**。
故不做去連字號、不做同義展開，一律 `pop-up`。

**§9.4 之盲區揭露**：第三層只驗 `resolution_key` 出現於所指欄位，
**不驗該欄位所述之狀態是否真為先行詞**。
「PC 裡有 `pop-up` 這個詞」不等於「PC 建立的正是該彈窗」——
後者仍為人工。記明以免誤以為層次 2 已全機器化。

### 1.2 ⚠ `cont_deferred.tsv` 未依字面清空

下放包 T121 曰「`cont_deferred.tsv` **清空**（本批列冊二筆皆已判定）」。

**該檔現有三筆**：`038-03`（第 4 批）、`058-02`／`064-02`（**第 5 批**）。
「本批列冊二筆」指 `038-02`（已於上繳包 22 移轉）與 `038-03`——
**與「清空」不是同一件事**。

**照字面清空之後果實測可推**：`058-02`／`064-02` 之 `reference` 特徵
仍會命中第一層，而其既不在 CONT、不在排除清單、也不再在列冊 →
**列為未處置 → 第一層 FAIL**。三態之「已看見、待判定」正是為它們而設。

**處置**：只移除 `038-03`，保留第 5 批之二筆。**表列如下**：

```
leaf                    batch  狀態
SWE1-HMI-VC-038-03      4      → 移入 CONT（本包）
SWE1-HMI-VC-058-02      5      列冊（保留）
SWE1-HMI-VC-064-02      5      列冊（保留）
```

### 1.3 登記

`cont_table.tsv` 增 `resolution`／`resolution_key` 二欄（既有 6 條留空）：

| leaf | kind | 節 | 句 | resolution | key |
|---|---|---|---|---|---|
| `038-03` | reference | 11.5 | **3** | `PC` | `pop-up` |
| `038-04` | reference | 11.5 | **4** | `Step` | `pop-up` |

---

## 2. T122 —— token 工作定義（profile §10）

以**空白切分計詞**為本 feature 之工作定義，canon 若日後定義則以 canon 為準、
全表重算。

**其實益**：上繳包 22 §8 把 54／42／21 標為**近似值**，
故「`1-3` 逾 50」當時嚴格說只是傾向。定義落檔後**三者為正式值**，
該判定隨之為正式判定 —— §2.2 之層次 2 得以成立。

**未機器化（已記於 profile §10）**：現無腳本於登記時計 token 並比對 50。
CONT 現有 8 條之取材範圍**皆由人工計數**。
記明以免誤以為 R-3 於本 feature 已受檢查。

---

## 3. T123 —— 第三檢查點

### 3.1 置於 `cont_guard.py` 之 `layer3`，非 `verify_batch.py` 之新項

下放包曰「併入第 17 項或獨立編號，執行層定並回報」。**定為前者**，理由三：

1. **CONT 之判準與其檢查應同處** —— 一、二層已在該檔，第三層分家則
   「改判準要改幾個檔」變成要記得的事。
2. **self-test 前置已是該檔之程式結構**（§7.1.1），沿用即可，
   `verify_batch.py` 另建一套等於有二套。
3. 第 17 項本就收 `cont_guard` 之離開碼 —— **第三層自動成為每批之常駐檢查**，
   不需再改 `verify_batch.py` 一個字。

代價：`cont_guard.py` 自此需讀 `generated/*.json`。已加 `load_generated()`。

### 3.2 三態，非二態

第三層之輸出為 `已驗`／`待生成`／`不符`。
**`待生成` 獨立成一態**（沿 20a §2.1 之三態原則）——
登記了但該 leaf 尚未生成者，與「驗過了」**不得看起來一樣**。
本包執行過程中此態確實出現過：登記後、生成前，
第三層顯示 `已驗 0；待生成 2` —— 那正是當時的真實狀態。

### 3.3 self-test 增為 8 個斷言

```
cont_guard —— self-test 前置（PLAYBOOK §7.1.1）
  self-test 1  第一層(b) 已知標的 019-02 應為候選  PASS  命中=['reference']
  self-test 2  第一層(a) 反向 017 不應為候選        PASS  命中=無
  self-test 3  第二層(b) 第 1 批四筆登記應全過      PASS  母體=4 不符=[]
  self-test 4  第二層(a) 反向 012-03→§2.5 應 FAIL   PASS
  self-test 5  第二層(a) 反向 013-02→§2.6.3 s1 應 FAIL PASS
  self-test 6  第三層(b) 已知標的 PC 含 key 應過        PASS
  self-test 7  第三層(a) 反向 key 不在 PC 應 FAIL       PASS
  self-test 8  第三層(a) 反向 key 只在 PC 而聲稱 Step 應 FAIL PASS
  → 八個斷言全過，開始跑正式母體
```

**斷言 6／7 為夾具（fixture）而非真實 `038-03`**，與下放包 §3.3 所述不同，
理由記明：真實標的須待 T124 生成後才存在，而 self-test 之意義在於
**跑正式母體之前**就把檢查器驗過。夾具以 **TC 之真實欄位形狀**構成
（`pre_conditions`／`test_procedure` 之欄位名），
故「第三層查錯欄位」這一類錯誤夾具測得出來。

**斷言 8 是我加的第三個**，下放包未要求：
`resolution_key` 只在 PC 而聲稱 `Step` → 應 FAIL。
**它測的是「有沒有查對欄位」，不是「有沒有找到字」** ——
若第三層寫成「整份 TC 的 JSON 裡有沒有這個詞」，斷言 6／7 全過而 8 不過，
**而那個寫法會把層次 2 所要區分的二種承載方式抹平**。

### 3.4 下放包所要求之反向實測（真實標的）亦執行

生成後，將 `038-03` 之 `resolution_key` 暫改為 PC 所無之 `thermostat`：

```
第三層 —— 已驗 1 條 [('SWE1-HMI-VC-038-04', 'Step', 'pop-up')]；
          不符 1 條 [('SWE1-HMI-VC-038-03', 'PC', 'thermostat', 'pre_conditions 未含該 key')]
**FAIL** —— 結構聲稱不符 1
```

已還原，還原後 `已驗 2 條`。

---

## 4. T124／T125 —— 第 4 批 16 筆

`generated/batch4_settings_behavior.json`。`leaf_scope` 15、`held_leaves` **空**、
`split_delta: 1`、**PENDING 0** —— **首個全潔批，亦為首個 a 段即全批之批次**。

### 4.1 收斂 20 項全過

```
verify_batch — batch4_settings_behavior.json（收斂條件；下放包 10 §四 ＋ 13 §4.4）
  #  條件                                                             判
------------------------------------------------------------------------------------------------
  1  16 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                           PASS
     TC 數 16；缺 key 無
  2  IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）                        PASS
     本腳本不代替逐項判讀，見上繳包 10 §4.2
 11  pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled） PASS
     default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）              PASS
     命中 0 處 無
  3  test_item 括號下半 16 筆兩兩不同（機械）                                    PASS
     缺括號 無；重複 無；相異 16
 3b  test_item 括號下半無中文（R-S4）                                        PASS
     含中文 無
  4  specification_reference 16 筆與 recon_leaf_to_section.tsv 逐字相符   PASS
     不符 0 筆 
  5  priority 16 筆與 priority_final.tsv 逐字相符                         PASS
     不符 0 筆 
  6  Test Set 16 筆一致，Test Group 皆為 `Vehicle Category`               PASS
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
 15  母體 = leaf_scope + split_delta = 15 + 1 = 16（R-VC22(b)／IN §8.2.2） PASS
     tcs=16；leaf_scope=15；宣告 split_delta=1；實際拆分增量=1（{'SWE1-HMI-VC-038-05': 2}）；held=0（b 段不計入母體）
 16  續行型 leaf 之 test_item 上半與 SYS1 完整句逐字相符（R-VC7）                   PASS
     適用 3 筆；不符 0 筆 無
 17  CONT 表二層防護（候選無未處置 ∧ 內容驗證全過；含 self-test）                        PASS
     PASS —— 未處置候選 0；內容不符 0；結構聲稱不符 0；離開碼 0
------------------------------------------------------------------------------------------------
20 checked / 0 failed
```

### 4.2 ⚠ 第 7b 之取材分布：預期 SYS1 3、實得 1

```
取材來源分布 {'Description': 12, 'Title': 2, 'SYS1': 1}
```

上繳包 22 §5.3 預期 `SYS1` 3 筆（CONT 之 `038-02`／`038-03`／`038-04`）。
**實得 1 筆。差額不是錯，是 7b 量不到**：

| leaf | SYS1 句 vs 037 `Description` | 7b 之歸屬 |
|---|---|---|
| `038-02` | **不同**（取 s1＋s2，Description 只有 s2）| `SYS1` |
| `038-03` | **逐字相同** | `Description`（先命中即止）|
| `038-04` | **逐字相同** | `Description`（同上）|

第 7b 之判準是「上半對得上**某一個**來源」，其分布為**首次命中之歸屬**，
**不是取材決定之紀錄**。二者在來源字串相異時恰好一致，相同時就分不開。

**取材決定之真正承載者是第 16 項** —— 它依 CONT 表逐字比對 SYS1 之指定句，
本批**適用 3 筆、不符 0**。三筆之 SYS1 身分在那裡受檢，不在 7b。

### 4.3 R-VC25 例外路徑之首次動用（`035-03`／`036-02`）

二筆之三件逐筆記於其 `reasoning`：

| | `035-03` | `036-02` |
|---|---|---|
| (a) 理由 | 二筆 Description **逐字相同**（`Selecting cancel will take the user back to the previous screen.`），P0 之依據 `without changing any settings` **只在 Title** | 同左，其依據為 `without clearing any data` |
| (b) R-VC24 判別 | 謂語 `returns the user…` 為本 leaf 行為；`restore-defaults prompt` 為**情境脈絡** | 同左；`clear-personal-data prompt` 為**情境脈絡** |
| (c) 非行為主張 | 由 (b) 滿足 | 由 (b) 滿足 |

**二筆之區分**：Description 相同、Title 僅以提示之別區分，
故括號下半即以該別區分（`restore-defaults` / `clear-personal-data`）。
**ER 皆含 baseline（§5.6）**：第 2 步記錄現值 → Cancel → 第 4 步回讀比對。
「未變」無變前之值即不可判。

### 4.4 本批特有拘束之落實

| 筆 | 落實 |
|---|---|
| `034-02` | 進入路徑改經 **Phone screens → Phone settings**（SYS1 §13.2 明文於 Key Off 可用），**未經 Settings 頁籤**；`reasoning` 載 §11.1 與 §13.1 之路徑解與「規格自身無衝突、不發 DR」|
| `034-02` 測試資料 | **`HMI Settings List` 已實測搜尋**：`key-off`／`ignition`／`ACC`／`Timed Mode` 命中 21 列、`grey`／`gray` 命中 15 列 —— **其所載之灰化成因為頭燈關閉、Display Mode 為 Auto、sync 選項、Steering only、車輛行進中，無一為 key-off**；該表無「key-off 可用性」欄位。故**不具名**，以規格語言之通稱表述（§8.4.1）|
| `036-01` | `reasoning` 載 R-VC14(b) 分歧揭露：失效為「該清而未清」，資料仍在，**非 data-loss** → P1；隱私外洩風險依 R-VC11(c) 記於 reasoning，**不入 priority** |
| `037-01`／`-02` | 一靜一動：`-01` 之括號下半 `The rule itself`、`-02` 之 `The transition`；`-02` 之 ER 含 baseline（第 2 步記錄全模式狀態 → 開一 → 第 4 步比對）|
| `038-03`／`-04` | 依 §9.2 第三處置類；**登記先行、生成後由第三層證明**（`已驗 2 條`）|
| `038-05` | 拆 2，同 req_id，括號下半以分支區分；s6 之「持續至完成」置於**未完成支**（完成支無灰化可觀察）|
| `039` | 上半之彎雙引號與 `X/Close` 斜線逐字保留；**ER 限於 HU 彈窗之出現與其文字**，叢集（Driver screen）中文顯示委派記於 reasoning（§8.4.2）|
| 記法 | `035-02`／`036-01`／`038-01` 三筆二欄不對稱 —— **一律取 `Description`**，各筆 reasoning 載其取自哪欄 |

### 4.5 五批回歸

```
pilot_glovebox                   20 checked / 0 failed
batch1_category_structure        20 checked / 0 failed
batch2_settings_list             20 checked / 0 failed
batch3_controls                  20 checked / 0 failed
batch4_settings_behavior         20 checked / 0 failed
```

---

## 5. ⚠ `038-03` 不拆之人工判讀（請覆核）

本筆之來源含**二個離開條件**：系統完成、使用者按 X。
§8.3 壓測下我判為**同一規則之二個邊界**（規則本身是「彈窗不自行消失」），
非二個獨立觸發，故依授權之 16 筆不拆。

**惟 IN §402 之拆分判準是「不同觸發」** —— 而「等待系統完成」與
「按 X」在操作上確為二個不同動作。**此判讀為人工，我把它記在 TC 之
`reasoning` 裡而非埋掉**。若上游認為應拆，本筆為第一候選（16 → 17）。

---

## 6. `split_flag` 之慣例請裁

第 4 批之 `038-05` 拆 2，而 `split_flag` 填 `False`——
**沿既有四批之慣例**（第 2 批之 `046-05`／`048-02` 亦為拆分而填 `False`）。

實測：**現有 82 筆 TC 之 `split_flag` 全為 `False`，`split_reason` 全為空**，
**含四筆確為拆分者**。即此二欄現在不承載任何資訊。

未自行改為 `True` 之理由：改則第 4 批與前三批不一致，
而回溯改前三批屬既交付者之改動（R-TM13）。**請裁其一**：
(甲) 維持全 `False`，並明文該二欄於本 feature 不使用；
(乙) 自第 4 批起填 `True` ＋ 理由，並回溯前三批之四筆。

---

## 7. 進度

**117 leaf 中 96 筆已收斂，TC 累計 98 筆。** b 段保留 3 筆。

| 剩餘 | leaf | 阻斷 |
|---|---|---|
| 第 5 批 `Ignition Availability` | 16 | **無**（下放包 23 §七：DR-VC5 未答亦可生成）|
| 第 6 批 `Brake Service` | 2 | **DR-VC3**（邊界）|
| 第 7 批 `Cabrio Widget` | 1 | **DR-VC3**（同上）|
| b 段 | 3 | **DR-VC9(二)** |

**九筆 DR 至今全未結。**

---

## 8. 待你裁

1. **`resolution_key` 登記為 `pop-up` 而非下放包所舉之 `popup`**（§1.1）
2. **`cont_deferred.tsv` 未依字面清空**（§1.2）—— 若你要的就是字面清空，請說，我改回並附第一層 FAIL 之實測
3. **`038-03` 不拆之人工判讀**（§5）
4. **`split_flag` 之慣例**（§6）—— 甲／乙
5. 第 5 批之生成授權；同批 A（六項）、DR-VC3、DR-VC9(一) 之發送（Tier 3）

---

## 9. 量測條件揭露（R-G8）

### `034-02` 之測試資料查證

搜尋範圍限 `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` 之
`Settings` 分頁全 1015 列，樣式為 `key[- ]?off|ignition|ACC|Timed Mode` 與
`grey|gray`。**其結論為否定性判斷**（「該表未載 key-off 可用性」），
其強度限於該分頁；`Brand-Specific Names` 分頁未逐列讀
（其內容為品牌別名對照，與可用性無關）。**未讀 `Pop Up List HMI R1 (26PI).xlsx`** ——
該檔為彈窗清單，不含設定之可用性。

### 第三層之驗證強度

第三層驗 `resolution_key` **逐字出現於所指欄位**。
**不驗語意** —— 見 profile §9.4 之盲區揭露。
故「`038-03` 之 PC 建立的正是 s1 所述之那個彈窗」**仍為人工判斷**，
本包之機器證據只到「PC 裡有 `pop-up` 這個詞」。

### token 計數

依 profile §10 之工作定義（空白切分），**已自近似值升為正式值**。
惟該定義本身**未機器化** —— CONT 現有 8 條之範圍皆人工計數。

---

## 10. 檔案清單

| 檔 | 動作 |
|---|---|
| `docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md` | 增 §9（四小節）、§10 |
| `features/vehicle_category/data/cont_table.tsv` | 增二欄；增 `038-03`／`038-04` |
| `features/vehicle_category/data/cont_deferred.tsv` | 移除 `038-03`（保留第 5 批二筆）|
| `features/vehicle_category/scripts/cont_guard.py` | 增 `layer3`／`load_generated`／夾具；斷言 5 → 8 |
| `features/vehicle_category/scripts/gen_batch4.py` | 新增 |
| `features/vehicle_category/generated/batch4_settings_behavior.json` | 新增（16 筆）|

---

## 附錄 A —— 第 4 批 16 筆全文

### A.1 `VC-034-01` — Settings absent from the vehicle are not listed

| 欄 | 值 |
|---|---|
| `tc_title` | Settings absent from the vehicle are not listed |
| `priority` | **P2** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.1` |
| `functional_safety` | NA |
| `distinguishing_axis` | 不適用者之處置：隱藏（對 -02 之灰化） |

**`test_item`**

```
Settings not contained within a specific vehicle will not be displayed in that vehicles Settings list.

(Applicability -- a setting the vehicle does not contain is absent from its list)
```

**`pre_conditions`**

```
1. The vehicle under test is a configuration that does not contain the setting named in the test data
```

**`input_test_data`**：A setting that the vehicle under test does not contain, named from the HMI Settings List

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Record every item in the Settings list and compare it against the setting named in the test data
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The setting named in the test data is not present anywhere in the Settings list
```

**`reasoning`**：**驗證目標**：不屬於該車之設定不出現於其 Settings 清單。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）。**為什麼這樣切**：§11.1 之二規則由 037 拆為 -01／-02 二 leaf，本筆只驗「隱藏」，灰化屬 -02（§8.2.1）。**範圍**：不驗該設定於其他車型是否出現 —— 那是他車之組態，非本需求所斷言（§8.4.2）。

### A.2 `VC-034-02` — Key Off greys out unavailable settings

| 欄 | 值 |
|---|---|
| `tc_title` | Key Off greys out unavailable settings |
| `priority` | **P2** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.1` |
| `functional_safety` | NA |
| `distinguishing_axis` | 不適用者之處置：灰化（對 -01 之隱藏） |

**`test_item`**

```
If a setting is available to the vehicle but not when key-off, they will appear grey when the system is in key-off.

(Key Off -- an unavailable setting greys out instead of disappearing)
```

**`pre_conditions`**

```
1. The vehicle under test contains a setting that the system does not offer while in Key Off
```

**`input_test_data`**：A setting that is available to the vehicle but not in key-off

**`test_procedure`**

```
1. Place the vehicle in Key Off
2. Open the Phone settings through the Phone screens
3. Record how the setting named in the test data is rendered in that list
```

**`expected_result`**

```
1. The system is in Key Off
2. The Phone settings are reachable through the Phone screens while the system is in Key Off
3. The setting named in the test data is present in the list and is rendered grey
```

**`reasoning`**：**驗證目標**：車輛有、但 key-off 下不可用之設定，於 key-off 呈灰而非消失。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 進入路徑之拘束（上繳包 22 §2.3）**：SYS1 §13.1 於 Key Off／Timed Mode／ACC 擋住 **Settings 頁籤**，故本筆**不得以該頁籤進入**，否則於待測狀態下不可執行。改經 §13.2 明文於 Key Off 可用之 Phone screens 進入 Phone settings。§11.1 與 §13.1 **非衝突** ——一管入口、一管入口之後的呈現，§13.5 之 `tab or a Settings category` 為旁證，故不發 DR。**⚠ 測試資料未具名（§8.4.1）**：`HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026)` 之 `Settings` 分頁已實測搜尋 `key-off`／`key off`／`ignition`／`ACC`／`Timed Mode`（命中 21 列）與 `grey`／`gray`（命中 15 列）—— **其所載之灰化成因為頭燈關閉、Display Mode 為 Auto、sync 選項、Steering only、車輛行進中，無一為 key-off**；該清單無「key-off 可用性」之欄位。故不自行指定某一設定，以規格語言之通稱表述之。

### A.3 `VC-035-01` — Restore defaults resets the settings

| 欄 | 值 |
|---|---|
| `tc_title` | Restore defaults resets the settings |
| `priority` | **P1** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.2` |
| `functional_safety` | NA |
| `distinguishing_axis` | 回復預設之三段：值之生效（對 -02 之確認彈窗、-03 之取消） |

**`test_item`**

```
Selecting yes to restoring defaults will reset their settings to default.

(Restore defaults confirmed -- the settings actually return to their default values)
```

**`pre_conditions`**

```
1. At least one setting holds a value other than its default
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Record the current value of the setting that holds a non-default value
3. Open the restore defaults prompt and press "Yes"
4. Record the value of that setting again
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The setting reads its non-default value
3. The restore defaults action is accepted
4. The setting reads its default value
```

**`reasoning`**：**驗證目標**：於回復預設之提示選 Yes，設定確實回到預設值。**取材（R-VC25）**：上半取自 037 `Description`。**為什麼含前後二次記錄**：「回到預設」為值之變化，無變化前之值即無從判其已變（§5.6 之 baseline）。

### A.4 `VC-035-02` — Confirmation pop-up after a reset to default

| 欄 | 值 |
|---|---|
| `tc_title` | Confirmation pop-up after a reset to default |
| `priority` | **P2** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.2` |
| `functional_safety` | NA |
| `distinguishing_axis` | 回復預設之三段：確認彈窗（對 -01 之值生效、-03 之取消） |

**`test_item`**

```
Once settings are restored a pop-up will be shown stating ‘Settings reset to default’.

(Confirmation pop-up -- its appearance and its wording after the reset)
```

**`pre_conditions`**

```
1. At least one setting holds a value other than its default
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Open the restore defaults prompt and press "Yes"
3. Record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The restore defaults action is accepted
3. A pop-up is displayed and its text reads "Settings reset to default"
```

**`reasoning`**：**驗證目標**：回復完成後顯示 `Settings reset to default` 之彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：本 leaf 之 Description 用彎單引號 `‘…’`、Title 用直單引號 `'…'`。**取 Description 一欄，不混用**；上半之彎單引號依 R-VC23 逐字保留，ER 之彈窗文字為作者散文，依 R-VC23(b) 用直雙引號。

### A.5 `VC-035-03` — Cancel leaves the settings unchanged

| 欄 | 值 |
|---|---|
| `tc_title` | Cancel leaves the settings unchanged |
| `priority` | **P0** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.2` |
| `functional_safety` | NA |
| `distinguishing_axis` | 回復預設之三段：取消（對 -01 之值生效、-02 之確認彈窗） |

**`test_item`**

```
Selecting 'Cancel' on the restore-defaults prompt returns the user to the previous screen without changing any settings

(Restore-defaults prompt cancelled -- baseline recorded before the cancel and re-read after)
```

**`pre_conditions`**

```
1. The settings named in the test data hold known values other than their defaults
```

**`input_test_data`**：Three settings that currently hold non-default values, read before and after the cancel. The count of three is a test-design parameter and is not stated by the source

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Record the current value of each setting named in the test data
3. Open the restore defaults prompt and press "Cancel"
4. Record the value of each setting named in the test data again
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The recorded values form the baseline for step 4
3. The previous screen is displayed
4. Each recorded value is identical to the baseline recorded in step 2
```

**`reasoning`**：**驗證目標**：於回復預設之提示選 Cancel，返回前一畫面且設定未變。**⚠ 取材為 R-VC25 之例外路徑（Title），三件逐筆記**：(a) **理由** —— 本筆與 `036-02` 之 Description **逐字相同**（`Selecting cancel will take the user back to the previous screen.`），而其 P0 之依據 `without changing any settings` **只在 Title**；Description 未載該條件，取之則本 TC 之驗證標的落空（A-VC10 第一面）。(b) **R-VC24 判別結果** —— Title 之謂語為 `returns the user…`，為本 leaf 之行為；`restore-defaults prompt` 用以定位是哪一個提示，屬**情境脈絡**。(c) **非行為主張** —— 由 (b) 滿足。**ER 之 baseline（§5.6）**：「未變」無變前之值即不可判，故第 2 步記錄、第 4 步回讀。**測試資料之三筆為測試設計參數**，非來源所載（§8.4.1）。

### A.6 `VC-036-01` — Clear personal data confirmed

| 欄 | 值 |
|---|---|
| `tc_title` | Clear personal data confirmed |
| `priority` | **P1** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.3` |
| `functional_safety` | NA |
| `distinguishing_axis` | 清除個人資料之二支：執行（對 -02 之取消） |

**`test_item`**

```
Selecting yes to clearing personal data will clear their personal data, a pop-up will be shown stating ‘Personal data cleared’ with an ‘X’ button in the top right corner.

(Clear personal data confirmed -- the data is cleared and the pop-up carries its X button)
```

**`pre_conditions`**

```
1. Personal data is stored in the vehicle under test
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Record the personal data that is stored
3. Open the clear personal data prompt and press "Yes"
4. Record the pop-up that is displayed, its text and the controls it carries
5. Record the personal data that is stored again
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The stored personal data is present
3. The clear personal data action is accepted
4. A pop-up is displayed, its text reads "Personal data cleared" and it carries an "X" button in the top right corner
5. The personal data recorded in step 2 is no longer stored
```

**`reasoning`**：**驗證目標**：選 Yes 清除個人資料，並顯示帶右上 X 之確認彈窗。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：Description 用彎單引號、Title 用直單引號 —— 取 Description 一欄。**⚠ R-VC14(b) 之分歧揭露**：037 給 Medium，本地初判 P0（資料遺失風險），**改判 P1** —— 本筆之失效為「該清而未清」，資料仍在，**非 data-loss**；其風險為隱私外洩，依 R-VC11(c) 記於本欄而**不入 priority**。取消支（-02）之失效才是靜默清除，故其為 P0。**為什麼一 TC 不拆**：清除與彈窗為同一觸發（按 Yes）之二個後果，IN §398 明文不拆，列為二條 ER。

### A.7 `VC-036-02` — Cancel leaves the personal data intact

| 欄 | 值 |
|---|---|
| `tc_title` | Cancel leaves the personal data intact |
| `priority` | **P0** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.3` |
| `functional_safety` | NA |
| `distinguishing_axis` | 清除個人資料之二支：取消（對 -01 之執行） |

**`test_item`**

```
Selecting 'Cancel' on the clear-personal-data prompt returns the user to the previous screen without clearing any data

(Clear-personal-data prompt cancelled -- stored data re-read against the baseline)
```

**`pre_conditions`**

```
1. Personal data is stored in the vehicle under test
```

**`input_test_data`**：The stored personal data that is read before and after the cancel

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Record the personal data that is stored
3. Open the clear personal data prompt and press "Cancel"
4. Record the personal data that is stored again
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The recorded personal data forms the baseline for step 4
3. The previous screen is displayed
4. The stored personal data is identical to the baseline recorded in step 2
```

**`reasoning`**：**驗證目標**：於清除個人資料之提示選 Cancel，返回前一畫面且資料未被清除。**⚠ 取材為 R-VC25 之例外路徑（Title），三件逐筆記**：(a) **理由** —— 本筆與 `035-03` 之 Description 逐字相同，而其 P0 之依據 `without clearing any data` **只在 Title**（A-VC10 第一面）。(b) **R-VC24 判別結果** —— Title 之謂語為 `returns the user…`，為本 leaf 之行為；`clear-personal-data prompt` 為**情境脈絡**。(c) **非行為主張** —— 由 (b) 滿足。**與 `035-03` 之區分**：二筆之 Title 僅以提示之別區分（restore-defaults／clear-personal-data），括號下半即以此區分。**ER 之 baseline（§5.6）**：「未被清除」須有清除前之內容可比。

### A.8 `VC-037-01` — Only one suspension mode is on

| 欄 | 值 |
|---|---|
| `tc_title` | Only one suspension mode is on |
| `priority` | **P1** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.4` |
| `functional_safety` | NA |
| `distinguishing_axis` | 互斥之靜態面：任一時刻之狀態（對 -02 之切換動作） |

**`test_item`**

```
Under suspension, the user can only have one of the suspension modes on at a time.

(The rule itself -- at most one suspension mode reads on at any moment)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with Suspension settings that offer more than one suspension mode
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Open the Suspension settings and record the state of every suspension mode
3. Press each suspension mode in turn and record the state of every suspension mode after each press
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. Exactly one suspension mode reads on
3. Exactly one suspension mode reads on after each press
```

**`reasoning`**：**驗證目標**：懸吊模式於任一時刻至多一者為開。**取材（R-VC25）**：上半取自 037 `Description`。**一靜一動之區分（下放包 20 §3.4／上繳包 22 §5.2）**：本筆驗**規則**（同時僅一），`-02` 驗**行為**（開一關餘）；括號下半以此區分。本筆之第 3 步逐一按過每個模式，其驗的是每次之後不變式仍成立，非某一次之轉換結果。

### A.9 `VC-037-02` — Activating a mode turns the others off

| 欄 | 值 |
|---|---|
| `tc_title` | Activating a mode turns the others off |
| `priority` | **P1** |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `specification_reference` | `…_11.4` |
| `functional_safety` | NA |
| `distinguishing_axis` | 互斥之動態面：開一關餘之轉換（對 -01 之不變式） |

**`test_item`**

```
If the user selects to turn one on, the rest will be turned to off.

(The transition -- turning one on drives the others off)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with Suspension settings that offer more than one suspension mode
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Open the Suspension settings and record the state of every suspension mode
3. Press a suspension mode that currently reads off
4. Record the state of every suspension mode again
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The recorded states form the baseline for step 4
3. The pressed suspension mode is accepted
4. The pressed suspension mode reads on and every suspension mode that read on in the baseline now reads off
```

**`reasoning`**：**驗證目標**：開啟一個懸吊模式時，其餘自動關閉。**取材（R-VC25）**：上半取自 037 `Description`。**ER 之 baseline（§5.6，下放包 23 §3.2）**：「其餘被關掉」須先知道原本哪些是開的 —— 無 baseline 則「餘者為 off」與「餘者本來就 off」不可分。**一靜一動之區分**：本筆為行為，`-01` 為規則。

### A.10 `VC-038-01` — Progress pop-up on a language change

| 欄 | 值 |
|---|---|
| `tc_title` | Progress pop-up on a language change |
| `priority` | **P2** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.5` |
| `functional_safety` | NA |
| `distinguishing_axis` | 語言變更五段：彈窗之出現（對 -02 之語言、-03 之持續、-04 之返回、-05 之清單呈現） |

**`test_item`**

```
If the user selects to change languages, a pop-up will appear stating ‘Language updated, voice command change in process…’.

(Language change triggered -- the progress pop-up appears with its stated text)
```

**`pre_conditions`**

```
1. The vehicle under test offers more than one language in the language settings
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Open the language settings and select a language other than the current one
3. Record the pop-up that is displayed and its text
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The language selection is accepted
3. A pop-up is displayed and its text reads "Language updated, voice command change in process…"
```

**`reasoning`**：**驗證目標**：選擇變更語言時出現進度彈窗，其文字為所載者。**取材（R-VC25）**：上半取自 037 `Description`。**⚠ 二欄記法不對稱（A-VC10 第三面）**：Description 用彎單引號、Title 用直單引號 —— 取 Description 一欄。ER 之彈窗文字含來源之刪節號 `…`，逐字保留（R-VC23(c)）；其引號為作者散文之直雙引號（R-VC23(b)）。

### A.11 `VC-038-02` — Pop-up appears in the new language

| 欄 | 值 |
|---|---|
| `tc_title` | Pop-up appears in the new language |
| `priority` | **P3** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.5` |
| `functional_safety` | NA |
| `distinguishing_axis` | 語言變更五段：彈窗之呈現語言（對 -01 之出現） |

**`test_item`**

```
STN6.) If the user selects to change languages, a pop-up will appear stating ‘Language updated, voice command change in process…’ . It will be presented in the newly selected language (not always English).

(Pop-up language -- rendered in the newly selected language, not English)
```

**`pre_conditions`**

```
1. The current language of the vehicle under test is English
```

**`input_test_data`**：A target language other than English that the vehicle offers

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Open the language settings and select the target language named in the test data
3. Record the language in which the pop-up text is rendered
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The language selection is accepted
3. The pop-up text is rendered in the target language named in the test data and not in English
```

**`reasoning`**：**驗證目標**：進度彈窗以新選之語言呈現，非固定英文。**⚠ 取材為 CONT 之指涉型（R-VC25 優先序第 2）**：037 `Description` 之 `It` 其先行詞（pop-up）在 s1，取單句則指涉無解。**登記 SYS1 §11.5 範圍 `1-2`，33 token，未逾 R-3 之 50**（profile §9.2 層次 1 之預設處置對本筆成立，故不採第三處置類）。上半即 s1＋s2 之逐字，收斂第 16 項逐字比對。

### A.12 `VC-038-03` — Pop-up stays until completion or X

| 欄 | 值 |
|---|---|
| `tc_title` | Pop-up stays until completion or X |
| `priority` | **P2** |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `specification_reference` | `…_11.5` |
| `functional_safety` | NA |
| `distinguishing_axis` | 語言變更五段：彈窗之持續與離開條件（對 -01 之出現、-04 之返回） |

**`test_item`**

```
This pop-up will stay on the screen until either the system completes changing the voice commands or the user presses X.

(Persistence -- the pop-up leaves only on completion or on X)
```

**`pre_conditions`**

```
1. The language-change pop-up is displayed and the system has not completed changing the voice commands
```

**`input_test_data`**：NA

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

**`reasoning`**：**驗證目標**：彈窗持續顯示，直到系統完成或使用者按 X。**⚠ 取材為第三處置類 `resolved-by-structure`（profile §9.2 層次 2，下放包 23 §2.2）**：`This pop-up` 之先行詞在 SYS1 §11.5 s1，而連續 `1-3` 為 **54 token，逾 R-3 之 50**（profile §10 之工作定義）；非連續 `1,3` 為 42 但破壞 verbatim 之連續性，使第 7b 項與第二層之子串判準對本筆失效。**採單句 s3 ＋ 指涉由 TC 結構承載** —— 其先行詞「語言變更彈窗已顯示」**本即本 TC 驗證持續性之前提**，不解指涉也必須建立它。CONT 登記 `resolution=PC`／`resolution_key=pop-up`，**第三檢查點驗其 pre_conditions 確含該詞**。**⚠ 不拆之判讀（人工，記明）**：本筆含二個離開條件（系統完成、使用者按 X）。§8.3 壓測下二者為同一規則「彈窗不自行消失」之二個邊界，而非二個獨立觸發，故依授權不拆；惟此為人工判讀，若上游認為應拆，本筆為第一候選。

### A.13 `VC-038-04` — Return to the language settings screen

| 欄 | 值 |
|---|---|
| `tc_title` | Return to the language settings screen |
| `priority` | **P3** |
| `design_method` | 狀態轉換 (State Transition Testing) |
| `specification_reference` | `…_11.5` |
| `functional_safety` | NA |
| `distinguishing_axis` | 語言變更五段：彈窗關閉後之落點（對 -03 之持續） |

**`test_item`**

```
The user is then taken back to the language settings screen.

(Return target -- the screen the user lands on once the pop-up is gone)
```

**`pre_conditions`**

```
1. A language change has been selected from the language settings screen
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Press the X button on the language-change pop-up
2. Record the screen that is displayed
```

**`expected_result`**

```
1. The X press is accepted
2. The language settings screen is displayed
```

**`reasoning`**：**驗證目標**：彈窗結束後使用者返回語言設定畫面。**⚠ 第一層偽陰性之第二實例（上繳包 22 §6）**：037 之 `The user is **then** taken back…` 以 `then` 承接前句，但首字大寫、非代名詞起首 —— 二特徵皆不命中，候選偵測看不到，由勘查之 SYS1 對照發現。**取材為第三處置類**：`then` 所承接之「按 X 或系統完成」**即本 TC 之必然步驟**，故取單句 s4，CONT 登記 `resolution=Step`／`resolution_key=pop-up`，**第三檢查點驗其 test_procedure 確含該詞**。

### A.14 `VC-038-05` — Language screen normal once updating completes

| 欄 | 值 |
|---|---|
| `tc_title` | Language screen normal once updating completes |
| `priority` | **P3** |
| `design_method` | 決策表 (Decision Table Testing) |
| `specification_reference` | `…_11.5` |
| `functional_safety` | NA |
| `distinguishing_axis` | 更新完成與否：完成支（對未完成支之勾選＋灰化） |

**`test_item`**

```
If the voice commands are complete the screen will be shown as normal, if not complete the current language is shown checked while the rest will be greyed out. They will remain greyed out until the system has completed updating the voice commands.

(Voice commands complete -- the language settings screen renders as normal)
```

**`pre_conditions`**

```
1. A language change has been made and the system has completed changing the voice commands
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the language settings screen
2. Record how every language option is rendered
```

**`expected_result`**

```
1. The language settings screen is displayed
2. Every language option is rendered as normal and none of them is grey
```

**`reasoning`**：**驗證目標**：語音命令更新完成後，語言設定畫面呈現如常。**取材（R-VC25）**：上半取自 037 `Description`（含 s5＋s6 二句）。**⚠ 拆 2 之理由（IN §8.2.2／§5.2，上繳包 22 §5.1）**：s5 自身即二個 if 分支（完成 → 如常；未完成 → 現用語言勾選、其餘灰化），二者為**二個獨立失效**，單一 TC 之判準不明；且 IN §5.2 禁一 TC 內寫條件分支。二筆同 req_id，括號下半以分支區分（IN §8.2.2：sub-id 數 ≠ TC 數）。

### A.15 `VC-038-05` — Other languages grey while updating runs

| 欄 | 值 |
|---|---|
| `tc_title` | Other languages grey while updating runs |
| `priority` | **P3** |
| `design_method` | 決策表 (Decision Table Testing) |
| `specification_reference` | `…_11.5` |
| `functional_safety` | NA |
| `distinguishing_axis` | 更新完成與否：未完成支（對完成支之如常呈現） |

**`test_item`**

```
If the voice commands are complete the screen will be shown as normal, if not complete the current language is shown checked while the rest will be greyed out. They will remain greyed out until the system has completed updating the voice commands.

(Voice commands not complete -- current language checked, the rest greyed until completion)
```

**`pre_conditions`**

```
1. A language change has been made and the system has not completed changing the voice commands
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the language settings screen
2. Record how every language option is rendered
3. Wait until the system has completed changing the voice commands and record how every language option is rendered again
```

**`expected_result`**

```
1. The language settings screen is displayed
2. The current language is rendered checked and every other language option is rendered grey
3. The other language options are no longer grey
```

**`reasoning`**：**驗證目標**：更新未完成時，現用語言勾選、其餘灰化，且灰化持續至完成。**取材（R-VC25）**：上半同完成支，取自 037 `Description`。**為什麼第 3 步在本支而不在完成支**：s6 之「持續至完成」是對**未完成**狀態之時間性斷言，其終點才是完成；把它放到完成支則無灰化可觀察。**與完成支之區分**：括號下半載其分支條件。

### A.16 `VC-039` — Chinese language change pop-up

| 欄 | 值 |
|---|---|
| `tc_title` | Chinese language change pop-up |
| `priority` | **P3** |
| `design_method` | 功能測試 (Functional based ; no specific technique) |
| `specification_reference` | `…_11.6` |
| `functional_safety` | NA |
| `distinguishing_axis` | 語言之特定值：中文（對 -038 各筆之語言無關流程） |

**`test_item`**

```
STN15.) If user changes language to Chinese, display pop-up, “Language updates in progress...Driver screen only will display language in Chinese.” with X/Close button.

(Chinese selected -- the head unit pop-up and its X/Close button)
```

**`pre_conditions`**

```
1. The vehicle under test offers Chinese in the language settings
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Settings" tab
2. Open the language settings and select Chinese
3. Record the pop-up that is displayed, its text and the controls it carries
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Settings" tab active
2. The Chinese language selection is accepted
3. A pop-up is displayed, its text reads "Language updates in progress...Driver screen only will display language in Chinese." and it carries an X/Close button
```

**`reasoning`**：**驗證目標**：語言改為中文時顯示所載之彈窗，帶 X/Close 按鍵。**取材（R-VC25）**：上半取自 037 `Description`。**記法（R-VC23）**：上半之彎雙引號 `“…”` 與 `X/Close` 之斜線逐字保留；ER 之彈窗文字為作者散文，依 R-VC23(b) 用直雙引號，其內容含來源之三點刪節 `...` 逐字。**⚠ 範圍（§8.4.2）**：來源之 `Driver screen only will display language in Chinese` 為彈窗**文字之內容**，其所述之叢集（Driver screen）中文顯示屬**叢集側之行為**，非本 HMI 需求所斷言 —— 本筆之 ER 限於 HU 彈窗之出現與其文字，叢集顯示委派記於本欄，不入 ER。

---

> 以上 16 筆。收斂 20 項全過，五批回歸全綠。
> 未寫回工作簿、未進行任何 git 操作。
