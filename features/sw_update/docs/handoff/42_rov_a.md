# 下放包 42 —— 四項裁定、難度三軸、`ROV Installation` 首四列（ROV-A）

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`41_batch3_v2.md`；對應上繳：`docs/upstream/37_rov_a.md`
- **條文凍結中：本包不新增、不修訂任何條文**（43 條／留存 26 不變）

---

## 一、上繳包 36 審查判定

### 1.1 §T54d —— **難度不只二軸，是三軸**，且 ROV 這批證明了它

執行層之發現正確且重要：

> `batch 2a` 是錨極確定而可觀測性極差；`ROV Installation` 是可觀測性極佳
> 而錨完全沒有地面真值支持。**只報 105 列數，這批會看起來是最簡單的（0%）
> —— 而它是第一個 GT 完全掛零的批次。**

**分析層讀完材料後再加一軸**：本組之觸發面**繫於 `$FOTA_Status$` 之各值**
（`[Installing FOTA Update]`／`[FOTA Failure Complete]`／
`[FOTA FailureRollback Successful]`），而**其中失敗類之值須以一次真實之更新失敗
方能產生** —— 其為 **R-SU39 之第四型（觸發手段不可得）**。

**故難度為三軸，且三軸可獨立變動**：

| 軸 | batch 2a | batch 3 | **ROV-A** |
|---|---|---|---|
| 可觀測性（105 列） | 差（67%） | 佳（0%） | **佳（0%）** |
| 錨定確定性（GT） | 極佳（6/6） | 無（0） | **無（0）** |
| 觸發可行性 | 差（2/6 第四型） | 佳 | **半（見 §三）** |

**B-7 之建議採認並擴為三軸**，其記法待解凍後條文化；
**本包起之批次選定一律三軸各自報數，不合併**。

### 1.2 §2-1 `025` 之引號不一致 —— **不是錯誤，是規則要求的**

`test_item` 用彎引號（037 逐字，R-4）、`test_procedure`／`expected_result`
用直引號（IN §11：作者自己之散文一律 `"..."`）—— **二者依據不同條文，
其不一致為正確結果。**

**惟測試者之困惑是真的**：同一 TC 內同一 UI 標籤二種寫法。
**處置：不改 TC**，於 `REASONING.md` 該列記一句
「上半引號依 037 原文逐字保留，步驟與 ER 之引號依 IN §11」。

**執行層照抄未擅改，正確。**

### 1.3 §2-2 `REASONING.md` —— **准 (乙)**，惟須列入交付前檢查

其診斷正確：**歷來所有「記於 reasoning」之內容至今只在腳本註解與台帳裡，
不隨 TC 走，而交付時審閱者拿到的是工作簿不是這個 repo。**

**裁定**：`REASONING.md` 為內部台帳，**交付前須裁定其是否併入 `AH Remarks`**
—— 列入交付前檢查清單（T55d）。**現在不決定，但不能忘記。**

其整理過程之收穫一併記：
> 逐 TC 收攏後才看得出「這一列為什麼長這樣」是一個連貫的故事。

### 1.4 §自評 `132` 之 s2 —— **採 (丙) 間接涵蓋，理由成立**

其與 `313` 之別說得準：**`313` 是餘量為空（沒有自己的點）；
s2 是有自己的點但不可觀測，且其失效必然表現在 s3 或 s4 上**
（不查詢就無從得知是否已接受，後果必落在指引或阻擋）。
**故「間接涵蓋」在本例有實質根據，不是託辭。**

且其自陳之要點正確：
> 更正前 s2 在 `test_item` 裡，**看起來被涵蓋了而實際上沒有** —— 那比現在更糟。
> 現在它的未涵蓋是顯式的。

**B-8 之一般性觀察成立**：追溯矩陣看 trace 與 `test_item`，
不會發現 ER 沒動到那一句 —— **「寫進去」與「驗到了」在追溯面上長得一樣。**

### 1.5 §T54a —— 新記法首次適用即相符

`20 項全 0 ＋ U=3 ＋ I-cross=9`，且三份更正之上半皆實測逐字見於 037。

---

## 二、四項裁定

| # | 事項 | 裁 |
|---:|---|---|
| 1 | `025` 引號不一致 | **不改 TC**；`REASONING.md` 記其依據（§1.2） |
| 2 | `REASONING.md` 落點 | **准 (乙)**；**交付前須裁其是否併入 `AH`**，入交付前檢查清單 |
| 3 | 難度軸 | **三軸各自報數，不合併**（§1.1） |
| 4 | `132` s2 | **採 (丙) 間接涵蓋**；其推理記入 `REASONING.md` 該列 |

---

## 三、ROV-A 四列（`090`／`092`／`093`／`094`）

**選定依據（三軸）**：105 列 0／GT 0／觸發 —— `090`、`092` 可行；
`093`、`094` 須一次真實之更新失敗，**第四型**。

**`088`／`095` 不在本批** —— 二者引用 `PU0303`／`PU0416`，
依 A-SU3 之前例（PDF 之 `PU971` 於彈窗清單查無）**須先查表**（T55a）。

**共通**：`input_test_data` 全為 `NA`；
訊號記法**依來源逐字**（`$FOTA_Status$ = [值]`）——
本 feature 未綁 DBC，依 R-1 v3(d) 保留來源名稱，不改寫。

---

### TC-28 `newR1L-SU-028` ← `SWE1-FOTA-090`

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
1. Trigger an ROV update and wait until $FOTA_Status$ = [Successful FOTA Update]
2. Set the vehicle to Body OFF mode
3. Set the vehicle to Body ON mode
4. Check that the head unit displays the What's New details of the deployed package
```
**expected_result**
```
1. $FOTA_Status$ = [Successful FOTA Update] is reported
2. The vehicle is in Body OFF mode and the head unit screen is off
3. The vehicle is in Body ON mode and the head unit completes start-up
4. The head unit displays the What's New details of the deployed package
```
**specification_reference**
```
CFTS057-4907909
```
**design_method**：`狀態轉換 (State Transition Testing)`｜**priority**：`P2`

---

### TC-29 `newR1L-SU-029` ← `SWE1-FOTA-092`

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
3. Check that the recorded screen content shows the installation progress screens while $FOTA_Status$ = [Installing FOTA Update]
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

---

### TC-30 `newR1L-SU-030` ← `SWE1-FOTA-093` —— **第四型，掛 `PENDING`**

**test_item**
```
If FOTA_Status indicates FOTA FailureRollback Successful($FOTA_Status$ = [FOTA FailureRollback Successful]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Reverted” pop-up after successful rollback.
(Reverted pop-up shown after a rollback completes)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package is staged on the OTA Server for this head unit
3. The vehicle is in Body ON mode
4. PENDING: DR-SU2 means of making an ROV update fail and roll back on the test bench
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an ROV update and accept it on the head unit
2. PENDING: DR-SU2 step to make the update fail so that the rollback completes successfully
3. Check that the head unit displays the "Reverted" pop-up
```
**expected_result**
```
1. The ROV update is accepted and the installation starts
2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA FailureRollback Successful]
3. The head unit displays the "Reverted" pop-up
```
**specification_reference**
```
CFTS057-4907901
```
**design_method**：`基礎故障注入 (Fault Injection Lite)`｜**priority**：`P1`

---

### TC-31 `newR1L-SU-031` ← `SWE1-FOTA-094` —— **第四型，掛 `PENDING`**

**test_item**
```
If FOTA_Status indicates FOTA Failure Complete($FOTA_Status$ = [FOTA Failure Complete]), the ROV Update Service shall notify the ROV FOTA HMI. The ROV FOTA HMI shall display the “Walk Home Scenario” pop-up.
(Walk Home Scenario pop-up shown after an update failure completes)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package is staged on the OTA Server for this head unit
3. The vehicle is in Body ON mode
4. PENDING: DR-SU2 means of making an ROV update fail without a successful rollback on the test bench
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an ROV update and accept it on the head unit
2. PENDING: DR-SU2 step to make the update fail so that the failure completes without rollback
3. Check that the head unit displays the "Walk Home Scenario" pop-up
```
**expected_result**
```
1. The ROV update is accepted and the installation starts
2. PENDING: DR-SU2 observable state showing $FOTA_Status$ = [FOTA Failure Complete]
3. The head unit displays the "Walk Home Scenario" pop-up
```
**specification_reference**
```
CFTS057-4907902
```
**design_method**：`基礎故障注入 (Fault Injection Lite)`｜**priority**：`P1`

> **TC-30 vs TC-31 之區分**（R-SU41(b)）：其判定對象分別為
> `"Reverted"` 與 `"Walk Home Scenario"` 二個不同之彈窗，
> 且其觸發側狀態（回退成功 vs 失敗未回退）於 ER 第 2 行分別載明。
> **遮住其餘內容，二者之 Final Step 仍可看出驗的是不同的事。**
>
> **`093`／`094` 之第四型與 batch 2a 之 `315`／`318` 同族** ——
> 其觀測面（彈窗）明確，缺者為**使更新失敗之手段**。
> DR-SU2(d) 之第四型段由 2 列增為 **4 列**。

---

## 四、本批之預期

| 項 | 值 |
|---|---|
| TC 數 | **4**（`028`–`031`） |
| `PENDING` | **6**（`030` 3 ＋ `031` 3） |
| 預期 lint | **20 項全 0 ＋ U=6 ＋ I-cross=n**（`028` 無 `until`、`029` 有，故半窗數須實報） |
| 可交付 | **2 列**（`028`／`029`） |

**全案可交付候選：12 ＋ 2 = 14 列。**

---

## 五、任務（T55）

| # | 任務 |
|---|---|
| T55a | **`PU` 編號之查表**（A-SU3 之前例）：`PU0303`／`PU0416`／`PU0410`／`PUxxx1`／`PUXXX3` 五者於彈窗清單（T5 已查之 51 個）中是否在案。**在案者列其名稱；查無者明載** —— 決定 `088`／`095` 及後續各列可否逕引 |
| T55b | **ROV-A 產出與 lint**：`sandbox/rov_a/` 產出 `newR1L-SU-028`–`031`。**預期 20 項全 0 ＋ U=6**，`I-cross` 實報 |
| T55c | **DR-SU2(d) 第四型段增列**：`093`／`094`（4 列）。DR 文本同步 —— 其請求為**使更新失敗之手段**，與 `315`／`318` 之請求並列 |
| T55d | **交付前檢查清單建檔**（`DELIVERY_CHECKLIST.md`）：首三項為 (i) `REASONING.md` 是否併入 `AH`；(ii) `PENDING` 全數結案或經 Pei 降轉 `NA`；(iii) `C` 欄留空之理由須隨交付說明。**只建檔列項，不執行** |
| T55e | **`ROV Installation` 餘 16 列之三軸盤點**：逐列列出其觸發面（可由測試者直接造成／須真實更新成功／須真實更新失敗／須特定車型或訊號值），供分包 |
| T55f | **git** |

**不在本輪**：`088`／`095`（待 T55a）、ROV 餘 16 列、`Interruption Handling` 其餘 12 列、寫回。

---

## 六、上繳包要求（`docs/upstream/37_rov_a.md`）

1. T55a 之查表結果 —— **本輪核心**（決定後續各列可否引 `PU` 編號）
2. T55b 之 lint 全輸出
3. T55e 之三軸盤點
4. T55c／T55d／T55f 之結果
5. 未結 DR 清單（5 筆）
6. 獨立自評（入 BACKLOG）—— 特別回答：**TC-29 之 procedure 第 3 步寫
   `while $FOTA_Status$ = [Installing FOTA Update]` ——
   而 `$FOTA_Status$` 是 CarPropertyManager 之車輛屬性，測試者看不到它。
   該子句是否為一個不可觀測之限定條件，若是，應如何改寫方不失其情境**
