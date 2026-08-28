# 下放包 20 —— R-SU25（可觀測面）、pilot TC v2（5 TC 全改）、DR-SU1 英文化

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`19_pilot_tc.md`；對應上繳：`docs/upstream/19_observability.md`
- 裁定狀態：R-SU25 —— 分析層即裁
- **本包全面改寫 pilot 之 5 個 TC；成因為分析層之草案缺陷，非執行層之產出誤差**

---

## 一、上繳包 18 審查判定

**收。§7.1 找到的是本 feature 之結構性問題，而它在 lint 全綠之處被找到。**

### 1.1 §7.1 —— 5 個 TC 全部有不可執行之步驟，成因同一

> 「Read the update type received by the WiFi Update Service」這類步驟
> **讀的是內部服務狀態，而本 feature 無任何已綁定之觀測通道**（無 DBC、無 LID）。

**此為分析層之草案缺陷，且是最該被抓的一種** ——
TC 在紙上完全合規（21 項 lint 中 18 項全 0），
**而它在台架上跑不起來**。§三 R-SU25 立條，§四全面改寫。

### 1.2 §3.1 K／T 三行 —— **分析層之誤，確認**

下放包 19 §四 TC-3 之三個 `PENDING` 說明以中文書寫，違 **R-14**。
執行層依 T32b「不得為使其通過而改寫」**原樣寫入未改一字**，
並明言「改寫屬起草，由分析層為之，執行層不代擬定稿」——
**處置正確**。§四 TC-3 已英文化。

### 1.3 §3.2 之限度記明 —— 採認

> lint 之 21 項全綠不等於 TC 對。lint 查得到「ER 有情態詞」，
> 查不到「ER 驗錯了東西」。

**本輪即為其實證**：18 項全 0，而 5 個 TC 全部不可執行。

### 1.4 §5.1 歷史腳本保留 `<` 之取捨 —— 採認

`detector_backtest.py`／`stratified_gt.py` 保留舊判準、以更正表銜接，
理由為「已交付之二包正是分析層據以裁定之依據，改之則不可重現」。
**「歷史可重現」與「現行判準唯一」並存之作法正確**，
且 `mech3.py::caught()` 為唯一權威實作，來源明確。

### 1.5 §2.1 專案名稱 —— 採認，並記其方法意義

036 `D2` = `newR1L`、037 `D3` = `NR1L`，**二者不同**；R-SU24 令取 036，故取 `newR1L`。
執行層指出：實測結果恰與他 feature 相同，**但若當初推定，將無從分辨是對是錯**。
**此即「不推定而實測」之價值 —— 其價值不在結果不同，在於結果可信。**

---

## 二、pilot 之判定

**pilot 批 v1 不採用。** 5 個 TC 全部改寫（§四）。

`newR1L-SU-001`–`005` 之 ID 保留（同列同 ID，不重新編號）；
`sandbox/pilot01` 之產出視為 v1 受檢物，**不作交付**，v2 另出 `pilot02`。

---

## 三、R-SU25（新條，抄入 RULINGS.md，逐字）

```
R-SU25（可觀測面 —— 步驟目標與 ER 判定對象之限制）

實測（上繳包 18 §7.1）：pilot v1 之 5 個 TC 皆含
「Read the update type received by the WiFi Update Service」類步驟 ——
其讀取對象為**內部服務間之訊息或狀態**，而本 feature
**無任何已綁定之觀測通道**（`feature.yaml` 未綁 DBC、無 LID、
無診斷服務、無已裁定之 log tag）。

該類步驟在 lint 之 21 項中**全數合格**，卻在台架上不可執行。

裁定：

(a) Procedure 步驟之操作目標與 ER 之判定對象，一律限於
    **測試者可觀測之面**：HMI 顯示內容、實體按鍵之回應、
    CAN 訊號、檔案系統或 adb 可讀之狀態、可自 UI 讀取之版本或設定值。

(b) **內部服務間之訊息與狀態不得作為步驟目標或 ER 判定對象**
    （如 SWMC 傳給 WiFiUpdateService 之 metadata、服務內部之判定結果），
    除非該 feature 已有**經裁定之觀測通道**。觀測通道之裁定須載明
    其取得方式（指令、log tag、訊號名）與其來源文件。

(c) 需求之主體若全為內部服務，其 TC 之驗證面取**該行為之外部可觀測後果**
    （如：更新確實被套用 → 版本號改變；HMI 未被觸發 → 畫面無該提示）。
    後果亦無可觀測者，掛 `PENDING` 並登 DR，**不得寫成內部讀取步驟充數**。

(d) 需求所述之內部輸入若實為**測試之設定**（如更新類型為 Silent），
    依 IN §4.5 移至 **Pre-Condition**，**不得寫成讀取步驟** ——
    測試者是設定它，不是讀它。

(e) 本條之判別問句：**「這一步，台架上的人要看哪裡？」**
    答不出具體之看處者，該步驟不合格。
```

---

## 四、pilot TC v2（5 TC，全部改寫）

改寫之三個作法（對應 R-SU25(c)(d)）：
1. 「讀取更新類型」為**測試設定** → 移入 Pre-Condition
2. 「背景執行／部署完成」之驗證面 → 改取**版本號之前後變化**（§5.6 baseline）
3. 「不觸發 HMI」之驗證面 → 改取**畫面內容之記錄與比對**（本即可觀測）

---

### TC-1 ← `SWE1-FOTA-175`（`newR1L-SU-001`）

**test_item**
```
When the update type is identified as Silent Update, the WiFi Update Service shall automatically execute the update in background mode.
(Silent update runs in background with no HMI interaction)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Record the head unit screen content continuously until the update finishes
4. Read the software version shown on the head unit and record it as Version_after
5. Check that Version_after differs from Version_initial and that no SW Update prompt or progress notification appears in the recorded screen content
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit screen content until the update finishes is recorded
4. Version_after is recorded
5. Version_after differs from Version_initial; the recorded screen content contains no SW Update prompt and no progress notification
```

**specification_reference**
```
CFTS057-4907475
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

---

### TC-2 ← `SWE1-FOTA-176` facet A（`newR1L-SU-002`）

**test_item**
```
During a Silent Update session, the WiFi Update Service shall not trigger the SW Update HMI for update progress notifications.
(No progress notification during a silent session)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Record the head unit screen content continuously until the software version changes
4. Check that no update progress notification appears anywhere in the recorded screen content
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit screen content until the software version changes is recorded
4. The recorded screen content contains no update progress notification at any point of the session
```

**specification_reference**
```
CFTS057-4907476
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

---

### TC-3 ← `SWE1-FOTA-176` facet B（`newR1L-SU-003`）

拆分依據同下放包 19（IN §8.2.2；二個獨立部分失效）。
**三個 `PENDING` 說明已依 R-14 改為英文。**

**test_item**
```
During a Silent Update session, the WiFi Update Service shall allow user notification only when required to satisfy safety-related requirements.
(Safety-required notification is permitted during a silent session)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
3. PENDING: DR-SU1 list of safety-related notification conditions applicable during a silent session
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Record the head unit screen content continuously from the start of the session
3. PENDING: DR-SU1 step to bring one safety-related condition into effect
4. Check that the safety-related notification is displayed on the head unit while the session continues
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The head unit screen content from the start of the session is recorded
3. PENDING: DR-SU1 observable state showing the safety-related condition is in effect
4. The safety-related notification is displayed on the head unit and the session continues
```

**specification_reference**
```
CFTS057-4907477
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

---

### TC-4 ← `SWE1-FOTA-177`（`newR1L-SU-004`）

**test_item**
```
If the SW Update HMI is available, the assigned update service shall not present the user with options to opt out of or defer the update.
(No opt-out or defer option offered when HMI is available)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
3. The SW Update HMI is available on the head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Record every SW Update screen shown on the head unit until the update finishes
3. Check that none of the recorded screens offers an opt-out control or a defer control
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. Every SW Update screen shown until the update finishes is recorded
3. None of the recorded screens offers an opt-out control or a defer control
```

**specification_reference**
```
CFTS057-4907478
```
**design_method**：`負向測試 (Negative / Invalid)`｜**priority**：`P2`

> 錨定依據不變（下放包 19 §四 TC-4）：首選 `4907662` 之內容與本列**語意相反**，
> 正解為候選 #2 `4907478`。

---

### TC-5 ← `SWE1-FOTA-183`（`newR1L-SU-005`）

**test_item**
```
When the update completes, the OTA client will display a success notification and what's new details.
(Completion notification with What's New shown after a silent update)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Read the software version shown on the head unit until it differs from Version_initial
4. Check that the head unit displays the update success notification together with the What's New details
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The software version shown on the head unit differs from Version_initial
4. The head unit displays the update success notification and the What's New details of the deployed package
```

**specification_reference**
```
CFTS057-4907485
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

> 範圍紀律不變（下放包 19 §四 TC-5）：不引 `PU0410`。

---

## 五、任務（T33）

| # | 任務 |
|---|---|
| T33a | **pilot v2 之產出與 lint**：於 `sandbox/pilot02/` 產出 5 列（TC ID 沿用 `newR1L-SU-001`–`005`），跑 lint。**預期 K=0／T=0**（PENDING 說明已英文化）、**U=3**（計數用，仍應為 3）。任一與預期不符即如實回報 |
| T33b | **內部服務主體之普查**（R-SU25 之規模測定）：全 311 列，以語形判其 `Requirement Description` 之**主體**是否全為內部服務（主詞為 `SWMC`／`WiFiUpdateService`／`USB Update Service`／`Update Engine`／`SW Updater Manager` 等，且句中無 HMI／畫面／按鍵／CAN 訊號／版本／檔案之外部面）。輸出：該類列之 id 清單與計數、其在 21 個 Test Set 之分佈。**regex 與判準逐一揭露**；**執行層只分類語形，不裁定該列是否真無可觀測後果** |
| T33c | **觀測通道之盤查**：查本 feature 之素材中有無可作觀測通道者 —— 至少查 (i) 037 全欄有無 `adb`／`log`／`logcat`／`dumpsys`／診斷服務之字樣；(ii) CFTS_57 之 487 物件全文同樣掃描；(iii) SYSAD 之介面節有無可觀測之對外介面。**查得與否皆如實回報**，查無不得代以推定 |
| T33d | **DR-SU1 之更新**：其 `Batch impact` 欄改為指向 v2 之三行英文佔位；狀態維持 `OPEN` |
| T33e | **T-抄**：R-SU25 逐字 append；索引表同步（25 條現行）。PLAYBOOK 追加：「lint 全綠不等於 TC 對 —— 機械層查得到形，查不到『驗錯了東西』與『台架上跑不起來』」（出處：上繳包 18 §3.2、§7.1） |

**不在本輪**：其餘 4 列之 TC、寫回、git。

---

## 六、上繳包要求（`docs/upstream/19_observability.md`）

1. T33e 核對結果 + 索引表
2. T33a 之 lint 全輸出
3. **T33b 之普查結果與 T33c 之通道盤查 —— 本輪核心**
   （二者合起來決定：本 feature 有多少列在現況下根本寫不出可執行之 TC）
4. T33d
5. 未結 DR 清單
6. 獨立自評 —— 特別回答：**T33b 之語形判準會把哪一類「其實有可觀測後果」之列
   誤判為內部列**（即偽陽性之方向），以及**哪一類真正的內部列會被漏掉**
