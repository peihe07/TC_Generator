# 下放包 43 —— 五項裁定、`028`／`029` 改以彈窗表徵、ROV 分包定案

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`42_rov_a.md`；對應上繳：`docs/upstream/38_rov_a_v2.md`
- **條文凍結中：本包不新增、不修訂任何條文**（43 條／留存 26 不變）

---

## 一、上繳包 37 審查判定

### 1.1 §2.2 —— **「P 看不見它，F 把它當成未填的佔位」**

本輪最重要之一句。同一個字串 `$FOTA_Status$ = [Installing FOTA Update]`：

- **F** 之 `RE_F` 把任何 `[Word…]` 判為未填佔位 → **誤報**
- **P** 之二式皆要求訊號名含一個點（`$<MSG>.<Sig>$`），而本記法無點
  → **P 根本沒把它認成訊號，`P=0` 是沉默不是核可**

> **無任何檢查在確認它是一個合法之訊號寫法。**

**二者須一併處置** —— 只修 F 會把「誤報」變成「沉默」，
而沉默正是 PLAYBOOK (30) 所指之最難察覺者。§二 #1。

### 1.2 §1.2 —— `PUXXX1`／`PUXXX3` 與 A-SU3 之別，**分得對**

> **A-SU3**：一個**已存在**之彈窗被寫錯編號 → 可推定其正解。
> **本項**：一個**尚未被指派編號**之彈窗 → **沒有正解可推。**

**採認，且此區分應保留於台帳** —— 二者形態相同（清單查無）而處置相反，
日後若只記「查無」，會有人比照 A-SU3 去推一個不存在的編號。

### 1.3 §7 —— **「訊號值與彈窗是同一件事的兩種寫法」**

執行層之改寫方向正確且其來源可查：
`PU0303` 之 Description 逐字為 `Shown after a successful update.`、
`PU0416` 為 `Displayed when the software update is complete.` ——
**二者即 `$FOTA_Status$ = [Successful FOTA Update]` 之外部表徵，
且其出處為彈窗清單，不是推想。**

**且其指出 `028` 比 `029` 嚴重、而題目沒問到它** —— 分析層之自評題設得太窄，
執行層答了更廣的那一題。**採認。**

### 1.4 §3.2 —— ROV-A 之選樣把最難觸發之二列前置

> **餘 16 列之實際難度低於 ROV-A 所呈現者。**

**確認為分析層之選樣效果，非本組之性質。** 記明以免日後讀 ROV-A 之
50% 第四型比率而誤估全組。

### 1.5 §5 —— `DELIVERY_CHECKLIST.md` 自增五項，**全部追認**

其檔首之區分正確：**BACKLOG 多數不需動作，本檔未答即不得交付**；
且 **D-2 之外，其餘七項皆不需上游即可完成** —— 此句對期程判讀很有用。

`D-6`（037 之標點／拼寫／彎引號逐字保留須列明）與
`D-8`（`005` 之規格自身抵觸須隨交付揭露）尤其該在。

---

## 二、五項裁定

### #1 `F=2` —— **取 (甲)，且 P 一併處置**

| 項 | 裁 |
|---|---|
| **F** | 加例外：**緊接於 `$<name>$ =` 之後之方括號不判為佔位**。**例外做成 profile-scoped**（比照 `I-cross` 掛 `PROFILE_CHECKS`），未指定 `--profile` 時行為不變 |
| **P** | **profile 版增一式**，認得無點之 `$<Name>$ = [值]` 形態，使其**被檢查而非被忽略**。其判準：`$` 包覆之名、`=`、方括號包覆之值，三者齊備即通過；缺一即報 |
| **回測** | 既有八本之報告基線**須逐項不變**（未帶 `--profile`）；帶 `--profile sw_update` 之既有四簿（pilot06／batch01／batch02a／batch03）之各項亦須不變 |

**不改 TC** —— 「依來源逐字」不讓步。

### #2 `PUXXX1`／`PUXXX3` —— **不推定，以功能描述指稱**

`104`／`105`／`106` 之 TC：**ER 以彈窗之功能描述指稱**
（如 `the schedule update pop-up`／`the conditions not met pop-up`），
**不引任何編號**。`REASONING.md` 記明其編號於**二側皆為佔位**。

**不開 DR**（不阻斷交付），**改列 `DELIVERY_CHECKLIST.md` D-9**：
> 三列之彈窗編號待上游指派；一經指派，其 ER 須補編號。

### #3 `028`／`029` 之 `$FOTA_Status$` —— **改以彈窗表徵**（§三）

### #4 `IX_END` 片語表 —— **改為語形抽取，不寫死片語**

裁：`until` 之後之子句**整段正規化為訖點標籤**（不再比對固定片語表）。
**回測**：既有四簿之 `I-cross` 各項須不變；`rov_a` 之 `029` 應由半窗轉為完整窗。
**實作自訂，須揭露其正規化規則。**

### #5 ROV 分包 —— **定案四批**

| 批 | 037 列 | 數 | 依據 |
|---|---|---:|---|
| **ROV-B** | `097`／`099`／`100`／`101`／`102`／`103` | 6 | 強制更新彈窗之互動流程，同一畫面族 |
| **ROV-C** | `089`／`098`／`107`／`108`／`109` | 5 | 其餘可直接觸發者 |
| **ROV-D** | `088`／`095` | 2 | 須一次真實更新成功；彈窗已在案 |
| **ROV-E** | `104`／`105`／`106` | 3 | 待 #2 之處置落地 |

**下放包 44 為 ROV-B 之草案。**

---

## 三、`028`／`029` 之改寫（整列全文）

### 3.1 `newR1L-SU-028` ← `SWE1-FOTA-090`

**test_item**
```
The ROV FOTA HMI shall display the cached “What’s New” information to the user. The ROV Update Service shall retain the cached data until the next transition to Body ON mode.
(What's New shown at the next Body ON after a successful update)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package whose deployment package contains What's New details is staged on the OTA Server for this head unit
3. The vehicle is in Body ON mode
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an ROV update and wait until the head unit displays the update success pop-up PU0303
2. Set the vehicle to Body OFF mode
3. Set the vehicle to Body ON mode
4. Check that the head unit displays the What's New details of the deployed package
```
**expected_result**
```
1. The head unit displays the update success pop-up PU0303
2. The vehicle is in Body OFF mode and the head unit screen is off
3. The vehicle is in Body ON mode and the head unit completes start-up
4. The head unit displays the What's New details of the deployed package
```
**specification_reference**
```
CFTS057-4907909
```
**design_method**：`狀態轉換 (State Transition Testing)`｜**priority**：`P2`

> **`REASONING.md` 須記二事**：
> (i) `PU0303` 於本 TC **僅作為「更新已成功」之可觀測時點指標**，
> **本 TC 不驗該彈窗** —— 其驗證屬 `SWE1-FOTA-088`（IN §8.2.1）。
> (ii) 取彈窗而不取 `$FOTA_Status$` 之依據：後者為 CarPropertyManager 之
> 車輛屬性，台架不可觀測（R-SU25(b)）；前者之對應關係載於彈窗清單
> （`PU0303` Description：`Shown after a successful update.`），**非推想**。

### 3.2 `newR1L-SU-029` ← `SWE1-FOTA-092`

**test_item**
```
If FOTA_Status indicates Installing FOTA Update( $FOTA_Status$ = [Installing FOTA Update]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the installation progress screens corresponding to the active update session.
(Installation screens shown while the update is installing)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package is staged on the OTA Server for this head unit
3. The vehicle is in Body ON mode
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an ROV update and accept it on the head unit
2. Record the head unit screen content as continuous video capture until the installation ends
3. Check that the recorded screen content shows the installation progress screens for the active update session
```
**expected_result**
```
1. The ROV update is accepted and the installation starts
2. The head unit screen content until the installation ends is recorded as continuous video capture
3. The recorded screen content shows the installation progress screens for the active update session
```
**specification_reference**
```
CFTS057-4907898
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **改寫之內容**：proc 3 刪去 `while $FOTA_Status$ = [Installing FOTA Update]`
> 之限定子句 —— 其為不可觀測之限定，且**刪後 ER 3 仍可判**
> （錄影中有無安裝進度畫面）。`test_item` 之上半**保留該訊號寫法**
> （其為 037 原文，R-S4 逐字），**故 F／P 之處置仍須落地**（§二 #1）。

---

## 四、任務（T56）

| # | 任務 |
|---|---|
| T56a | **F 與 P 之 profile 版處置**（§二 #1）：F 加例外、P 增一式，**二者皆 profile-scoped**。回測：未帶 profile 之八本逐項不變；帶 profile 之既有四簿逐項不變 |
| T56b | **`IX_END` 改語形抽取**（§二 #4）：回測既有四簿之 `I-cross` 不變、`029` 轉為完整窗 |
| T56c | **`028`／`029` 之改寫產出**（§三整列全文）：`030`／`031` 不動。跑 lint，**預期 20 項全 0 ＋ U=6 ＋ `I-cross` 實報** |
| T56d | **`REASONING.md` 補記**：`028` 之二事（§3.1）；`104`–`106` 之彈窗編號佔位（§二 #2，先記，TC 未起草） |
| T56e | **`DELIVERY_CHECKLIST.md` D-9**（§二 #2） |
| T56f | **ROV-B 六列之材料索引**：`097`／`099`／`100`／`101`／`102`／`103` 於 `25a` 之行號區間。**不重傾印**。**併報**：該六列之 Description 中出現之全部 `$…$` 屬性名與其值（如 `$FOTA_Install$ = [Accepted]`），供分析層判其可觀測性 |
| T56g | **git** |

**不在本輪**：ROV-B 之 TC（下放包 44）、ROV-C／D／E、`Interruption Handling` 其餘 12 列、寫回。

---

## 五、上繳包要求（`docs/upstream/38_rov_a_v2.md`）

1. T56a／T56b 之回測結果 —— **本輪核心**（既有基線須逐項不變）
2. T56c 之 lint 全輸出
3. T56f 之材料索引與屬性名清單
4. T56d／T56e／T56g 之結果
5. 未結 DR 清單（5 筆）
6. 獨立自評（入 BACKLOG）—— 特別回答：**`099`／`100` 之 ER 若依 037 原文
   斷言 `$FOTA_Install$` 之值變化，其與 `028` 之 `$FOTA_Status$` 同為
   CarPropertyManager 屬性而不可觀測。而該二列之外部表徵
   （安裝是否開始）**恰為彼此之反面** —— 若二者皆以「安裝是否開始」為判定對象，
   是否落入 R-SU41 之「區分不在判定對象內」，抑或其反面關係本身即為合法之區分**
