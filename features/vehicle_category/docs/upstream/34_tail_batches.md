# 上繳包 34 —— Vehicle Category：b 段 3 筆 ＋ 第 6／7 批（T173–T177）

- 日期：2026-08-27
- 對應下放：`docs/handoff/34_tail_batches.md`
  （SHA256 `670740358c6269c7c80382fb42eb202fa19dacf989bfdf1b5342b254f58960de`，144 行）
- **⚠ 本包同時補做下放包 33（T169–T172）—— 該包從未執行，見 §0。**
- **結論：b 段 3 筆全生成；第 6／7 批 2 筆生成、**`065-02` 留置**（停止條件 (b) 命中）。**
- 未寫回、未進行任何 git 操作。

---

## 0. ⚠ 下放包 33 從未執行 —— 本包補做

接到下放包 34 時發現：`docs/handoff/33_resume_plan.md` **已落檔但無對應上繳包**，
且 `docs/RESUME_PLAN.md` **不存在** —— 而下放包 34 引用其 §4.1、
T177 要求「更新」它，R-VC30 要求「接 **R-VC29** 之後」而 R-VC29 未抄錄。

**我未見過該包**（本 session 之訊息序列自 32 直接跳到 34）。
**已補做 T169–T172**，結果見 §1。

> **NN 檢查抓得到「號碼碰撞」，抓不到「號碼跳過」。**
> 本次是後者 —— 33 落檔而未被執行，34 之 NN 檢查看到 `33_` 存在即通過。
> **建議**：NN 檢查併驗「前一號之上繳包是否存在」。

---

## 1. 補做下放包 33（T169–T172）

| # | 任務 | 結果 |
|---|---|---|
| T169 | `docs/RESUME_PLAN.md` 建檔 | ✅ 逐字採 §四 |
| T170 | R-VC29 抄錄 | ✅ byte-level `diff -q` 相同（`8a0db8cde659c9ec`）|
| T171 | §7.6 之承載者加註 ＋ §7 首之更正 | ✅ |
| T172 | OWNER 已知殘餘之措辭 | ✅ 改依 33 §二（不另輪修，若再被使用則屆時一併修）|

**T171 之更正值得記**：上繳包 32 §1 我寫「五條紀律皆無承載者」——
**§7.6 有**（`ledger_xref`，經 R-VC29 指定）。
我寫那句時**沒去查有沒有現成工具能承載它們** ——
**與 §7.4 所禁者同型**（看到「這是紀律」這個表徵，就下「無承載者」之判斷）。
已於 PLAYBOOK §7 首逐字記明。

---

## 2. T173／T174 —— R-VC30 與 b 段 3 筆

**R-VC30** 逐字抄入（`diff -q` 相同，`d8afae9c2b2ce96b`）。

三筆依 R-VC22(d) **併回原批**，既有各筆逐字不動（`scripts/gen_bsegment.py`
讀既有批檔、插入、寫回）：

| 批 | 前 | 後 | `held_leaves` |
|---|---|---|---|
| 第 1 批 | 22 筆 | **24 筆** | `[]`（原 2 筆）|
| 第 3 批 | 16 筆 | **17 筆** | `[]`（原 1 筆）|

二批**全項重跑，22 checked / 0 failed**。

### 2.1 分析層之預想被實測證實 —— 真殼只有一筆

下放包 §一末段：「(a) 之成本原估 3 筆殼，實測 `007-01`／`025-01` 之表**都在手**」。
**逐項覆核成立**：

| leaf | 表 | 實測 |
|---|---|---|
| `007-01` | SYS1 §2.4 `Vehicle Tab Labels and Order` | **VC2.2.2–VC2.2.11 共 10 列**（無 VC2.2.1）|
| `025-01` | SYS1 §3.9 `Controls Button Table` | **28 列**，`Rear Sunshade` … `Ambient Lighting` |
| `013-04` | PDO graphics | **不在素材** → 殼，帶 `PENDING: DR-VC9 PDO graphics` |

**二筆之全集比對可執行。**

### 2.2 層次分工之落實（IN §8.2.1）

`007-01`／`025-01` 之 reasoning 各載一句可檢驗之分工說明：

> **逐列全對而少一列，逐列層不會 FAIL，本筆會。**

即全集層驗**完整性與排他性**，`-02`~`-05` 驗**各列之內容**。

### 2.3 profile §8 之人工複核請你做

三筆上半皆為**短來源之完整句**（29／22／27 字元），
依 profile §8 **須人工複核** —— 全文見 §5。

---

## 3. ⚠ T175 —— `065-02` 命中停止條件 (b)，留置

### 3.1 實測

SYS1 §14.1 之句子切分（全案同一式 `(?<=\.)\s+(?=[A-Z])`）：

```
s1: 'EPB1.) Service mode option will be greyed out if the vehicle is in motion.'
s2: 'If the user presses on the greyed out line they will receive a pop-up
     stating ‘Feature not available while vehicle is in motion’
     (image: image18.png)'          ← **圖佔位黏在句尾**
```

`(image: image18.png)` 之前**無 `. ` 可切**，故它跟著 s2 走。

### 3.2 三處置類**皆不合**

`065-02` 之 037 `Description` 為 `If the user presses on **the greyed out line**…`
—— **定冠詞回指**，其先行詞（灰化之 Service mode 列）在 `065-01`。
第一層特徵**不命中**（profile §9.4.1 之第三型，已登記之偽陰性）。

| 層次 | 標的 | 判 |
|---|---|---|
| 1（整段 s1-2）| 39 token，**未逾 R-3 之 50** —— 條件成立 | ❌ **標的夾帶 `(image: image18.png)`** |
| 2（單句 s2，resolved-by-structure）| 先行詞為本 TC 結構必然建立之狀態 —— 條件成立 | ❌ **s2 本身即夾帶該佔位** |
| 排除（判為非此類）| —— | ❌ 其確為指涉型 |

**二個層次之標的都會把圖佔位寫進 `test_item` 上半。**

### 3.3 我沒有自行處置

可能之解有數個（剝除佔位後再取／改切分式／視為排除／另立第四處置類），
**每一個都是對 profile §9.2 之擴充** —— 依 §3.2 之停止條件
「停並回報，**不生成**」，`065-02` 留置為 b 段，未生成。

**其連帶**：該筆之彈窗文字為 `Feature not available while vehicle is in motion`
—— **即 A-VC18 所爭之 `PU0091` 字串**。生成時須帶
`PENDING: DR-VC10 PU0091 popup string`。**現未生成，故 PENDING 未計入。**

### 3.4 其餘二筆之五項停止條件

| 條件 | `065-01` | `066` |
|---|---|---|
| (a) 拆分候選（R-VC26）| 未命中 —— 單一規則，無列舉項 | 未命中 |
| (b) 新 CONT 形態 | 未命中 —— 完整可讀句，無指涉 | 未命中 —— 同左 |
| (c) 已知 DR 外之 PENDING | 未命中 | 未命中 |
| (d) 記法驗證異常 | 未命中 | **註**：Description 含 `(image: image23.png)`，**上半取首句**，不入佔位；第 7b 項通過 |
| (e) Title 越界（R-VC24）| 越界候選 **0**（`EPB Service` 為 Title 獨有之改寫用語）| 越界候選 **0**（`Vehicle Category` 同）|

### 3.5 `066` 之委派兩態已預寫

依 §3.3 之要求，其 reasoning 逐字載：

> **若 DR-VC3 回覆「應補」，章 8／9 另立 `Cabrio Rooftop` 組（R-VC16(c)），
> 本委派之標的即改指該組** —— 二態預先寫明，回覆後只需確認，不需改寫本欄。

---

## 4. T176／T177

### 4.1 八批回歸

```
pilot_glovebox                     22 checked / 0 failed
batch1_category_structure          22 checked / 0 failed
batch2_settings_list               22 checked / 0 failed
batch3_controls                    22 checked / 0 failed
batch4_settings_behavior           22 checked / 0 failed
batch5_ignition_availability       22 checked / 0 failed
batch6_brake_service               22 checked / 0 failed
batch7_cabrio_widget               22 checked / 0 failed
```

### 4.2 進度實測

```
TC 合計 125；已生成 leaf 116／117；PENDING 13 處
117 母體之未生成者：['SWE1-HMI-VC-065-02']
```

**下放包預估 126 筆** —— 實得 **125**，差額即留置之 `065-02`。

### 4.3 REV-15 ／ `RESUME_PLAN` 更新

- **REV-15** 已記：置末之理由書寫過寬。
  併記其**與 REV-13 同族而方向相反**（REV-13 範圍太小、本次太大），
  以及本輪之實益（`066` 之委派兩態預寫，理由精確之後處置也具體了）。
- **`RESUME_PLAN.md`** 加 §4.4 執行進度加註（原文不改）：
  b 段與第 6／7 批自待辦移除，**新增 `065-02` 之 CONT 處置為待辦第 1 項**
  （非 DR 阻斷），§4.2 出貨序第 1 項之母體由 12 處改為 **13 處**。

---

## 5. 五筆 TC 全文

> **b 段三筆之上半請依 profile §8 人工複核**（短來源，29／22／27 字元）。

### `VC-007-01`（第 1 批） — Vehicle Tab set matches the mapping table as a whole

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_2.4` |

**`test_item`**（上半為 profile §8 之完整句取材，**請人工複核**）

```
Vehicle Tab Labels and Order.

(Whole-set layer -- the tab set as a whole against the mapping table, no table row missing and no tab outside it)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Specialty features listed in the mapping table
```

**`input_test_data`**：The Vehicle Tab Labels and Order table of SYS1 section 2.4, whose rows are VC2.2.2 to VC2.2.11

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Controls" tab
2. Record every Specialty tab that is present, with its name and its left-to-right position
3. Compare the recorded set against the rows of the mapping table named in the test data
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Controls" tab active
2. The recorded set is the baseline for the comparison in step 3
3. Every table row whose Specialty feature the vehicle is equipped with has a tab present, and no tab is present that the table does not name
```

**`distinguishing_axis`**：表之層次：全集（對 -02～-05 之逐列）

**`reasoning`**：**驗證目標**：Vehicle Tab 之**全集**與 SYS1 §2.4 之對照表相符 ——表內該有的都在、表外不該有的都不在。**⚠ 本筆為 b 段，依 R-VC30（Pei 2026-08-27 裁定 (a)）生成** ——裁為需求 leaf，維持於 117 母體。**DR-VC9(二) 之查證維持發送**；若上游回覆與本裁定相反（確認為表頭誤登），依 `docs/RESUME_PLAN.md` §4.1 由 Pei 再裁。**⚠ 與 sibling 之層次分工（IN §8.2.1）**：本筆為**全集層**（完整性與排他性）；`-02`~`-05` 為**逐列層**（各列之名稱與位置）。**二者為不同驗證點，不重複** ——逐列全對而少一列，逐列層不會 FAIL，本筆會。**取材（profile §8 短來源）**：037 `Description` 為 `Vehicle Tab Labels and Order.`，**29 字元** —— 該長度下子串判準幾近無保護，故上半取其**完整句**，且依 profile §8 須人工複核。**測試資料之表為實測**：SYS1 §2.4 之 `VC2.2.x` 列實測為 **VC2.2.2–VC2.2.11 共 10 列**（無 VC2.2.1）。

### `VC-013-04`（第 1 批） — Portrait Dashboard layout follows the PDO graphics

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P3** | 功能測試 (Functional based ; no specific technique) | `…_2.6.3` |

**`test_item`**（上半為 profile §8 之完整句取材，**請人工複核**）

```
Refer to PDO graphics.

(Portrait Dashboard -- the layout as a whole against the PDO graphics reference)
```

**`pre_conditions`**

```
1. The vehicle is equipped with a portrait display
2. The Dashboard tab holds features to display
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Controls" tab
2. Select the Dashboard tab and record the layout as displayed
3. Compare the recorded layout against PENDING: DR-VC9 PDO graphics
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Controls" tab active
2. The Dashboard layout is displayed on the portrait display
3. The recorded layout matches the PDO graphics reference
```

**`distinguishing_axis`**：直向 Dashboard：版面整體對 PDO（對 -01～-03 之具體規則）

**`reasoning`**：**驗證目標**：直向 Dashboard 之版面與 PDO graphics 相符。**⚠ 本筆為 R-VC30 所裁之殼 TC** —— PDO graphics **不在素材**（DR-VC9(一) 未結），故 Procedure 之比對標的以 `PENDING: DR-VC9 PDO graphics` 佔位（IN §8.4.3）。**其為三筆 b 段中唯一之殼** —— `007-01`／`025-01` 之表皆在 SYS1。**⚠ 與 sibling 之分工（IN §8.2.1）**：`013-01`~`-03` 驗**已載於規格之具體版面規則**（三則以下各一橫幅／四則以上之拆分／其餘以磚塊置於下方）；本筆驗**版面整體與 PDO 之相符**，即規格文字未載而委由圖說者。二者不重複。**Pre-Condition 之方向**：`DISPLAY_PORTRAIT`（profile §6 常數，逐字重用）—— 本 leaf 明載 `For portrait displays`。**取材（profile §8 短來源）**：037 `Description` 為 `Refer to PDO graphics.`，**22 字元**，上半取其完整句，須人工複核。

### `VC-025-01`（第 3 批） — Controls button set matches the button table as a whole

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P2** | 功能測試 (Functional based ; no specific technique) | `…_3.9` |

**`test_item`**（上半為 profile §8 之完整句取材，**請人工複核**）

```
C1.) Controls Button Table.

(Whole-set layer -- the Controls button set as a whole against the button table, no table row missing and no button outside it)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Controls features listed in the button table
```

**`input_test_data`**：The Controls Button Table of SYS1 section 3.9, whose rows are the 28 buttons from Rear Sunshade to Ambient Lighting

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Controls" tab
2. Record every button that is present in the Controls tab
3. Compare the recorded set against the rows of the button table named in the test data
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Controls" tab active
2. The recorded set is the baseline for the comparison in step 3
3. Every table row whose Controls feature the vehicle is equipped with has a button present, and no button is present that the table does not name
```

**`distinguishing_axis`**：表之層次：全集（對 -02～-05 之逐列狀態語意）

**`reasoning`**：**驗證目標**：Controls 按鈕之**全集**與 SYS1 §3.9 之 `Controls Button Table` 相符。**⚠ 本筆為 b 段，依 R-VC30 生成**（同 `007-01`，DR-VC9(二) 之查證維持發送）。**⚠ 與 sibling 之層次分工（IN §8.2.1）**：本筆為**全集層**（成員之完整性與排他性）；`-02`~`-05` 為**逐列層**（各按鈕之**狀態語意**，如 `Activates Feature`／`Off, On (if unavailable – greyed out)`）。**二者為不同驗證點** —— 每個按鈕之狀態都對而少一個按鈕，逐列層不會 FAIL，本筆會。**取材（profile §8 短來源）**：037 `Description` 為 `C1.) Controls Button Table.`，**27 字元**，上半取其完整句，須人工複核。**測試資料之表為實測**：SYS1 §3.9 之按鈕列實測為 **28 列**，自 `Rear Sunshade` 至 `Ambient Lighting`。**⚠ 範圍（§8.4.2）**：本筆不驗各按鈕之狀態語意（屬 `-02`~`-05`），亦不驗表外項目於他處之行為。

### `VC-065-01`（第 6 批） — Service mode greys out while the vehicle moves

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P0** | 功能測試 (Functional based ; no specific technique) | `…_14.1` |

**`test_item`**（上半為 profile §8 之完整句取材，**請人工複核**）

```
Service mode option will be greyed out if the vehicle is in motion.

(In-motion lockout -- the Service mode option is rendered grey)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the EPB Service mode option
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Open the Vehicle Category screen and select the "Controls" tab
2. Open the Brake Service screen while the vehicle is stationary and record how the Service mode option is rendered
3. Set the vehicle in motion and record how the Service mode option is rendered
```

**`expected_result`**

```
1. The Vehicle Category screen is displayed with the "Controls" tab active
2. The Service mode option is rendered as normal while stationary
3. The Service mode option is rendered grey while the vehicle is in motion
```

**`distinguishing_axis`**：行進中之呈現：灰化（對 -02 之按下後果，留置）

**`reasoning`**：**驗證目標**：車輛行進中，EPB Service mode 選項呈灰。**取材（R-VC25）**：上半取自 037 `Description`（優先序第 1）——`Service mode option will be greyed out if the vehicle is in motion.`，**非 CONT**（其為完整可讀句，無指涉）。**ER 之 baseline（§5.6）**：「行進中呈灰」須有靜止時之呈現可比 ——否則「一直都是灰的」與「因行進而變灰」不可分。**P0 之依據**：行進中之攔阻屬 safety 型（同 `062-01`／`063-01`）。**與 `065-02` 之分工（IN §8.2.1）**：本筆驗**呈現**（灰化），`-02` 驗**按下之後果**（彈窗）—— 二個不同驗證點。**未涵蓋**：§14.2 之彈窗優先序（037 未涵蓋，表 B 第 14 列）。

### `VC-066`（第 7 批） — Cabrio widget carries its title

| `priority` | `design_method` | `spec_ref` |
|---|---|---|
| **P3** | 功能測試 (Functional based ; no specific technique) | `…_16.2` |

**`test_item`**（上半為 profile §8 之完整句取材，**請人工複核**）

```
W0.) Widget title for this feature is Cabrio.

(Widget title -- the literal string shown as this feature's widget title)
```

**`pre_conditions`**

```
1. The vehicle under test is equipped with the Cabrio feature
2. The widget for this feature is placed where widgets are displayed
```

**`input_test_data`**：NA

**`test_procedure`**

```
1. Display the screen that holds this feature's widget
2. Record the title text shown on that widget
```

**`expected_result`**

```
1. The widget for this feature is displayed
2. The widget title reads "Cabrio"
```

**`distinguishing_axis`**：widget 之標題文字（本組唯一 leaf）

**`reasoning`**：**驗證目標**：該 widget 之標題文字為 `Cabrio`。**取材（R-VC25）**：上半取自 037 `Description` 之**首句**`W0.) Widget title for this feature is Cabrio.` ——其後之 `(image: image23.png)` 為圖佔位，**不入上半**（上半仍為 Description 之逐字子串，第 7b 項通過）。**非 CONT** —— 該句完整可讀，無指涉。**⚠ 委派之兩態（下放包 34 §3.3）**：widget 所開啟之 Cabrio 功能（車頂開闔、擋風板）屬**章 8／9**，037 未涵蓋，見表 B 第 1–7 列。**若 DR-VC3 回覆「應補」，章 8／9 另立 `Cabrio Rooftop` 組（R-VC16(c)），本委派之標的即改指該組** ——二態預先寫明，回覆後只需確認，不需改寫本欄。**範圍（§8.4.2）**：本筆只驗標題文字，不驗 widget 之開啟行為、不驗其所開啟之功能。


---

## 5.1 ⚠ 側檔重生時抓到一個同源比對之盲區

重生側檔得 **123 筆**，而全簿 **125 筆** —— `BATCH_ORDER` 漏了第 6／7 批。
**而 `--verify` 照樣 PASS**：其母體亦自 `BATCH_ORDER` 推導，
**二者同源，比不出漏批**。

這正是上繳包 28 §7 所自陳者之實例：

> 側檔之鍵與內容自六批 JSON 推導，故「側檔與 JSON 相符」對本輪必然成立。

**已補一個不同源之判準**：`--verify` 另驗 `BATCH_ORDER` 是否涵蓋
`generated/` 之全部批檔。雙向實測：

```
(a) 反向：暫自 BATCH_ORDER 移除第 7 批 → **FAIL**
    ["側檔多出之鍵 ['SWE1-HMI-VC-066#1']",
     "BATCH_ORDER 未涵蓋之批檔 ['batch7_cabrio_widget']"]
(b) 正向：還原後 → PASS（125 筆）
```

**注意反向之第一則**：移除批次後「側檔**多出**該鍵」—— 因側檔未重生。
若當時順手重生，該則會消失而只剩第二則 —— **新判準是唯一抓得到的那一個。**

---

## 6. 量測條件揭露（R-G8）

- **b 段三筆併回原批**：既有各筆**逐字未動**（腳本只 insert，不改既有元素）。
  `pending_scope` 自實際內容重新推導，故第 1 批由 2 處增為 3 處（＋`013-04`）。
- **`007-01`／`025-01` 之表列數為實測**（`VC2.2.x` 之正則命中、
  §3.9 之 `|` 分隔列計數），**非引用任何既有敘述**。
- **`065-02` 之停止判定**依 SYS1 之**現行切分式**。
  若切分式改（如把 `(image:` 前也視為斷點），本判定可能不成立 ——
  **但改切分式本身即為對全案共用之正規化之改動**，不在本輪範圍。
- **八批回歸為本輪實測**；`ledger_xref` 未重跑（本包未修訂任何條文之款）。
- **下放包 33 之補做**：其 T169–T172 於本包執行，
  **其上繳包（33）不另出** —— 結果併入本包 §1。若你要獨立的 33 上繳包，說一聲。

---

## 7. 待你裁

1. **`065-02` 之 CONT 處置**（§3）—— 四個可能之解皆為 profile §9.2 之擴充
2. **b 段三筆上半之人工複核**（profile §8，§5 全文）
3. **NN 檢查併驗「前一號之上繳包是否存在」**（§0）
4. **Excel 人工驗收**（Pei）—— 寫回前最後一道，仍未回報
5. Tier 3：十筆 DR 之回覆、`QS Suggestion` 狀態查詢

---

## 8. 進度

**117 leaf 中 116 筆已生成**（`065-02` 留置），**TC 累計 125 筆**，
八批回歸 **22 checked / 0 failed** ×8。

表 A 完成、表 B 草稿（四處待 DR-VC3）、**`reasoning` 側檔已重生（125 筆）**、
TC ID 已裁（R-VC28）、丙″ 六項全過、交付前清單五項建檔、續作計畫建檔。

**13 處 PENDING。十筆 DR 未結。**
