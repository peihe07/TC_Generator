# 下放包 41 —— 六項裁定、`022`／`025` 之 test_item 更正、`021` 改判、DR-SU5

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`40_batch3_update_hmi.md`；對應上繳：`docs/upstream/36_batch3_v2.md`
- **條文凍結中：本包不新增、不修訂任何條文**（43 條／留存 26 不變）
- 裁定範圍：**TC 內容錯誤之更正**（凍結第 1 條之例外）

---

## 一、上繳包 35 審查判定

**收。§2.1 抓到四份 `test_item` 之拼接，其中二份是 TC 內容錯誤。**

### 1.1 §2.1 —— **`134` 之拼接是造句不是摘句**

> `After completion of the download,` 自 s2 接到 s3 上 ——
> 原文中該子句修飾「SWMC 提供細節給 HMI」，接過去後修飾「HMI 顯示給使用者」，
> **主詞換了。**

**確認為 TC 內容錯誤。** R-S4 允許**摘句**（取與測試目的直接相關之句），
**不允許把 A 句之子句接到 B 句上** —— 後者產生一個原文沒有的句子。

**與 `002` 之 `at any point of the session` 同族**：
前者加字、本者移接，**二者皆使 `test_item` 之上半不再是原文**。

### 1.2 §2.1 —— **`132` 之驗證點不在其 `test_item` 內**

TC-22 之 ER 第 4 行驗 s3（提供接受指引），而其上半取 s2＋s4。
**讀 TC 的人看不到那句被驗的需求。** 確認為 TC 內容錯誤。

### 1.3 §7 —— TC-21 之還原步驟，**三點理由全部成立，第三點最硬**

> **還原之後 HU 是否回到「與更新前等價」之狀態，無任何需求可據以確認。
> 而 TC-21 之判決依賴二次執行之可比性 ——
> 第二次執行之起點若不可確認，二次之差異就不可歸因於更新類型。**

且第 2 點之推理正確且冷靜：**`Rollback Protection` 是一個 Test Set，
其名即防止回退 —— 一個以防回退為需求之系統，其台架上是否可回退，
恰恰不能假設。**

**(丁) 三解之取捨採 (丙)**，其理由逐字採認：

> (乙解) 會使一個真實存在之驗證單元消失於二個較窄之 TC 之間 ——
> **不是本列沒有點，是把點拆掉以求可執行。**

### 1.4 §3.1 `005` —— 規格自身抵觸，併入 DR-SU1，**追認**

`4907485`（第 3 步：完成時顯示成功通知）與 `4907477`
（靜默期間不得通知，除非安全所需）**在同一章、同一情境內抵觸**。
**改寫解決不了，併入 DR-SU1 之問 (ii) 正確。**

### 1.5 §2.2 二項逕行 —— **追認，且其自陳之 B-2 值得留意**

彎引號與句點前空格之還原**皆為逐字還原不是改寫**，四條件逐項成立。

> **現狀是「已逐字保留而未記其為何保留」，日後有人會以為是我方打錯。**

**正確。** 交付時之審閱者不會讀 BACKLOG —— 其記法待解凍後處理，
本輪先於各該 TC 之 `reasoning` 記一句「標點依 037 原文逐字保留」。
**此為 `reasoning` 之內容，不動 TC 欄位，屬逕行範圍。**

### 1.6 §5 —— `BACKLOG.md` 之檔首規定正確

> **本檔不是待辦清單** —— 阻斷交付者一律進 DR 或待裁表，不進本檔，
> 否則真正的待辦會被稀釋。

且執行層**自己遵守了它**（§7 之 TC-21 阻斷交付，故不入 BACKLOG 而入待裁表）。

---

## 二、六項裁定

| # | 事項 | 裁 |
|---:|---|---|
| 1 | 四份 `test_item` 拼接 | **`132`／`134` 為 TC 內容錯誤，改（§三）**；`131` 之 s1＋s5 為合法摘句（二句皆與測試目的直接相關），惟須於 `reasoning` 宣告未涵蓋之 facet；`136` 相鄰，不動 |
| 2 | `131` 之 s4 無 TC | **與 TC-21 同族，一併掛 DR-SU5**（見 §四）—— 「跨類型之一致性」與「由伺服器決定類型」皆需二次執行 |
| 3 | `005` 失格併入 DR-SU1 | **追認** |
| 4 | TC-21 之還原步驟 | **採 (丙解)**：改判掛 `PENDING`，開 **DR-SU5**（§三、§四） |
| 5 | `I-cross` 預期值記法 | **准**：其後各包之預期一律記為「**20 項全 0 ＋ `I-cross=n`**」，並附該批之窗形態說明 |
| 6 | 上繳號 `34` 跳號 | **明記跳號，不補** —— 其成因（T52 併入 T53）已載於本包檔頭與上繳包 35 檔首，可追溯 |

---

## 三、三份 TC 之更正（**整列全文，不給差分**）

### 3.1 `newR1L-SU-022` ← `SWE1-FOTA-132`

**test_item**
```
If the customer has not accepted the required terms and conditions, the SWMC shall provide SW Update HMI guidance describing how the customer can complete the acceptance process. The SWMC shall block update download initiation until terms and conditions acceptance is confirmed.
(Download blocked and guidance shown when terms and conditions are not accepted)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package whose Download Descriptor requires terms and conditions acceptance is staged on the OTA Server for this head unit
3. The customer preference record for this vehicle shows the terms and conditions as not accepted
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Read the software version shown on the head unit and record it as Version_after
4. Check that the SW Update screen shows guidance on how to accept the terms and conditions and that Version_after equals Version_initial
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. Version_after is recorded
4. The SW Update screen shows guidance on how to accept the terms and conditions; Version_after equals Version_initial
```
**specification_reference**
```
CFTS057-4907657
```
**design_method**：`負向測試 (Negative / Invalid)`｜**priority**：`P1`

> **更正之內容**：上半由 s2＋s4 改為 **s3＋s4（相鄰二句）** ——
> s3 即 ER 第 4 行前半之驗證點，s4 即其後半。**上半與判定對象自此逐句對應。**
> s2（查詢客戶接受狀態）為其前置行為，已由 pre_conditions 第 3 行承載。

---

### 3.2 `newR1L-SU-025` ← `SWE1-FOTA-134`

**test_item**
```
The SW Update HMI shall display the deployment package details to the user . The SW Update HMI shall provide opt-in options including “Install” and “Schedule Later”.
(Install and Schedule Later offered after download completes)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package configured as a non-silent update is staged on the OTA Server for this head unit
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Accept the update on the opt-in screen and wait until the download completes
3. Check that the head unit shows the deployment package details together with an "Install" option and a "Schedule Later" option
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The download completes and the post-download screen is displayed on the head unit
3. The post-download screen shows the deployment package details, an "Install" option and a "Schedule Later" option
```
**specification_reference**
```
CFTS057-4907662
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **更正之內容**：刪除自 s2 移接之時間子句 `After completion of the download,`，
> 上半改為 **s3＋s4（相鄰二句）**，二句皆以 SW Update HMI 為主詞，
> **與判定對象同主詞**。下載完成之時點由 procedure 第 2 步承載。
> **`to the user .` 之句點前空格、`“Install”` 之彎引號，皆依 037 原文逐字保留**
> （`reasoning` 記一句）。

---

### 3.3 `newR1L-SU-021` ← `SWE1-FOTA-131` —— **改判掛 `PENDING`**

**test_item**
```
The WiFi Update Service shall retrieve update type configuration from the OTA server for each update campaign using SWMC. The WiFi Update Service shall control the applicable update flow according to the server-defined update type configuration.
(Update flow follows the update type configured on the server)
```
**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update campaign configured on the OTA Server with update type Regular is available for this head unit
3. PENDING: DR-SU5 bench procedure for running the same head unit against two update campaigns of different update types from a comparable starting state
```
**input_test_data**
```
NA
```
**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Record the SW Update screens shown on the head unit as continuous video capture until the update finishes
3. PENDING: DR-SU5 step to return the head unit to a comparable starting state and set the campaign to update type Silent
4. Trigger an update availability check to the OTA Server
5. Check that the recorded screen content of the first run contains the opt-in screen and that no opt-in screen is shown in the second run
```
**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The SW Update screens shown until the update finishes are recorded as continuous video capture
3. PENDING: DR-SU5 observable state showing the head unit is back at a comparable starting state and the campaign type is Silent
4. The update availability check completes and an update is reported as available
5. The recorded screen content of the first run contains the opt-in screen; the second run shows no opt-in screen
```
**specification_reference**
```
CFTS057-4907453
CFTS057-4907656
```
**design_method**：`狀態轉換 (State Transition Testing)`｜**priority**：`P1`

> **改判之依據**：原第 3 步之「還原至更新前之軟體版本」**在台架上不可行且不可確認**
> （上繳包 35 §7）。其措辭改為「回到**可比之起始狀態**」——
> **不預設其手段為降版**，使 DR 之請求不被一個未經驗證之作法所侷限。
> **`PENDING` 3 行**（pre 3／proc 3／ER 3）。

---

## 四、DR-SU5 之開立

| 欄 | 值 |
|---|---|
| 事項 | 更新類型切換之台架程序與二次執行之可比性 |
| 對象 | `SWE1-FOTA-131`（`newR1L-SU-021`；**併其 s4「跨更新類型之一致互動流程」，本輪無 TC**） |
| 理由 | 本列之驗證單元為「伺服器所設之類型決定所適用之流程」，**一個 campaign 只有一個類型，故本質上需二次執行**。而 (i) 素材全無「還原／降版」之需求或程序；(ii) `Rollback Protection` 為本 feature 之一個 Test Set，其需求即**防止**回退；(iii) 縱可回退，**「與更新前等價」無需求可據以確認**，而二次之差異須可歸因於類型方有意義 |
| **請求 1** | 同一 HU 對二個不同類型之 campaign 依序執行時，**如何使二次之起始狀態可比**（乾淨刷機？二台 HU？其他程序？） |
| **請求 2** | `SWE1-FOTA-131` 之 s4 要求「跨更新類型之一致使用者互動流程」。**「一致」之判準為何** —— 何者須相同、何者得因類型而異 |
| Urgency | Medium —— 阻斷 1 個 TC 與 1 個未起草之 facet；不阻斷其餘九列 |

**DR 總數由 4 增為 5。**

---

## 五、本批之修正後預期

| 項 | 值 |
|---|---|
| batch 3 TC 數 | **10**（`018`–`027`） |
| `PENDING` | **3**（`021`） |
| 預期 lint | **20 項全 0 ＋ `U=3` ＋ `I-cross=9`** |
| **可交付** | **9 列**（`018`–`020`、`022`–`027`） |

**全案可交付候選：batch 3 之 9 ＋ batch 1 之 `004`／`006`／`007` = 12 列。**

---

## 六、任務（T54）

| # | 任務 |
|---|---|
| T54a | **三份 TC 之更正產出**（§三，整列全文照抄）：`021`／`022`／`025`。其餘七列不動。跑 lint，**預期 20 項全 0 ＋ U=3 ＋ I-cross=9** |
| T54b | **`reasoning` 之補記**（§1.5）：`025` 記「標點依 037 原文逐字保留」；`131` 之 `021` 記「s4（一致之互動流程）本批未涵蓋，見 DR-SU5 請求 2」 |
| T54c | **DR-SU5 開立**：`DATA_REQUESTS.md` 新增（§四之表）；DR 文本增其節。**發送者為 Pei** |
| T54d | **`ROV Installation` 20 列之難類盤點**（下批前置，R-SU31(b)）：其 105 列數、126 內部列數、GT 涵蓋列數、含 `PU` 彈窗編號之列數。**只出數，材料已備於 `25a` 不重傾印** |
| T54e | **git** |

**不在本輪**：`ROV Installation` 之 TC（下放包 42）、`Interruption Handling` 其餘 12 列、寫回。

---

## 七、上繳包要求（`docs/upstream/36_batch3_v2.md`）

1. T54a 之 lint 全輸出
2. T54c／T54d 之結果
3. 未結 DR 清單（**5 筆**）
4. 可交付候選之列數確認（**12 列**）
5. 獨立自評（入 BACKLOG）—— 特別回答：**`022` 之上半改為 s3＋s4 後，
   s2（查詢客戶接受狀態）之行為由 pre_conditions 第 3 行承載 ——
   而 pre_conditions 載的是「客戶偏好記錄顯示未接受」這個**狀態**，
   不是「SWMC 去查詢」這個**行為**。該行為是否因此完全無 TC 涵蓋**
