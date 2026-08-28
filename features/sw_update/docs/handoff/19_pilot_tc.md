# 下放包 19 —— 四項確認、R-SU20 v2／R-SU23／R-SU24、pilot TC 起草（4 列）

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`18_pilot_material.md`；對應上繳：`docs/upstream/18_pilot_review.md`
- 裁定狀態：R-SU20 v2、R-SU23（分位門檻之判準向）、R-SU24（TC ID）—— 分析層即裁
- **本 feature 之首批 TC 草案（4 列 → 5 TC），並開出首筆 DR**

---

## 一、上繳包 17 審查判定

**收。§7.2 之自陳是本輪最重要的一節。**

### 1.1 §7.2 —— 種子回測「5/5」實為循環，執行層自陳

> 上一輪之種子是 7 個**實際觀測到的**孤島；本輪之 5 個是
> **依改組推算出來的預期值**，不是獨立觀測。
> 於是「5/5 通過」實際上是「程式算出的結果等於我用同一套規則手算的結果」
> —— **它驗的是我沒算錯，不是偵測器沒壞。**

且指出真正有鑑別力者為「種子外之新發現 0 個」，並自行加了改組前後對照表
把「解除 2／新產生 0」分開列，才把 T31a 之問題答完整。

**教訓（入 PLAYBOOK）：種子必須是獨立觀測；由待驗規則推算出之預期值
不得充當種子** —— 與 §7(10)（A 型實例不能充當 B 型種子）同族，
但更隱蔽：本例之種子與被驗者出自**同一套規則**。

### 1.2 §5.2 —— 邊界脆弱之第三次，且證明它不是巧合

`176` 之首選分與機制 3 門檻為**同一個浮點數**。成因結構性：
門檻定義為 `tops[int(n * 20 / 100)]`，**取自母體之實測值**，
故該位次之列必然等於門檻。

> 前兩次（`292` 差 0.001、`260` 差 0.00000）被當成「巧合／脆弱」處理；
> **本次顯示它根本不是巧合 —— 只要門檻取自實測值，就永遠有一列坐在界上。**

**此為對前兩輪處置之更正性發現**，§三 R-SU23 據此立條。

### 1.3 §7.1 之限度說明 —— 採認，且其自我約束正確

三個量（段數／孤島數／單列段數）**必然同向**，
「三個量同向」不構成三重證據，只是同一件事說了三遍。
真正獨立之證據只有下放包 18 §二對 `359` 之記名依據（讀 Description 得到的）。

且提出**單向指標**之概念：段數變好不足以證明對，變壞足以要求交代。**採認。**

### 1.4 §5.1 pilot 組成之誤 —— **分析層之誤，確認**

`Silent Update` 為 **HMI 2（`177`、`183`）／Service 7**，
下放包 18 §4.1 誤載為 HMI 1／Service 8。
執行層並指出該誤之方向有利（`177` 為限制型、`183` 為顯示型，
二者 UI 形態不同，對 pilot 更有價值）。**選定依據不變，數字更正。**

---

## 二、四項確認

| # | 事項 | 裁定 |
|---|---|---|
| 1 | 機制 3 門檻之 `<` vs `≤` | **改 `≤`**（攔下界上之列），見 §三 R-SU23 |
| 2 | pilot 組成 HMI 1/8 → 2/7 | **准**，分析層之誤 |
| 3 | R-SU20(a)「連續」之 strict vs loose | **採 strict**，並明載其盲區，見 §三 R-SU20 v2 |
| 4 | TC ID 命名 | 見 §三 R-SU24 |

---

## 三、裁決條文（抄入 RULINGS.md，逐字）

```
R-SU20 v2（Layer 2 正確性之最低檢查 —— 孤島列之評估範圍）

v1(b)(c)(d)(e)(f) 維持。(a) 細化。

(a) v2 —— **孤島列僅就「群內部列」評估**：某列之前鄰與後鄰**皆存在
    且皆與其不同組**者為孤島。群首、群尾、單列群**不評估**。

    採 strict 而不採 loose（缺鄰視為不同）之理由：loose 得 13 列，
    其中 8 列為**Test Set 之正常邊界**，非證據 —— 每個單列群與每個
    群首／群尾只要與鄰居不同即成孤島，該檢查將被邊界淹沒而失去鑑別力。

    **已知盲區（須隨檢查陳述）**：本檢查**不覆蓋群邊界之錯分**。
    位於 Heading 群首尾之列若被錯置，孤島檢查不會報警。
    此為採 strict 之代價，非疏漏。
```

```
R-SU23（以母體實測分位為門檻者之判準向）

實測（上繳包 17 §5.2）：機制 3 之門檻定義為 `tops[int(n*20/100)]`，
**取自母體之實測值**，故該位次之列之分數**必然等於門檻**，
其是否被攔完全取決於判準寫成 `<` 或 `≤`。

此結構亦說明前二例（`292` 分 0.257 vs 第 15 百分位 0.256；
`260` 分差 0.00810 vs 第 10 百分位 0.00810）**並非巧合，
而是同一結構之相鄰表現**。

裁定：
(a) 凡以母體實測分位為門檻之偵測器，其判準一律取**包含界值之向**
    —— 即「攔下」側含等號（`score ≤ threshold` 為攔下）。
    理由：攔下之代價為多送一列人裁，漏攔之代價為一個缺口未被發現，
    二者不對稱。
(b) 現行機制 3 之判準由 `<` 改為 `≤`。據此 `SWE1-FOTA-176`
    **改為被攔下**（其實害為零 —— 該列非缺口列，GT 正解皆在前 5）。
(c) 凡陳述此類門檻之效果時，**須同時載明「界上恆有一列」**，
    不得將其表現為巧合或個案。
```

```
R-SU24（TC ID 之命名）

格式：`{project}-SU-{NNN}` —— 比照 vehicle_category 之 R-VC28。

`{project}` 之值**取自 036 母本之專案名稱儲存格實測**（T32a），
**不得沿用他 feature 之值**。實測前暫記為 `{project}`，
不得以 `newR1L` 等推定值產出任何 TC ID。

`{NNN}` 為零填 3 位、於同一 `{project}-SU` 群內單調遞增（IN §10.3）；
指派由產生器為之，LLM 不自行編號。

一列產生多個 TC 時（IN §8.2.2），各 TC 之 ID 獨立遞增，
`Requirement or Design ID` 欄同列該 037 列 id。
```

---

## 四、pilot TC 草案（4 列 → 5 TC）

**本節為分析層起草，供執行層與 Pei 審。未經審定不得寫回。**

選 4 列之理由：`175`（Service 型基準）、`176`（GT 列，示範階段二錨定與拆分）、
`177`（HMI 限制型，示範首選錯而正解在 #2）、`183`（HMI 顯示型，示範範圍紀律）。

---

### TC-1 ← `SWE1-FOTA-175`

**test_item**
```
When the update type is identified as Silent Update, the WiFi Update Service shall automatically execute the update in background mode.
(Silent update runs in background with no HMI interaction)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package classified as Silent Update is available on the OTA Server
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Read the update metadata received by the WiFi Update Service and record the update type
3. Record the head unit screen content throughout the update execution
4. Check that the update completes in background and no SW Update HMI prompt or progress notification is displayed
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The recorded update type is Silent Update
3. The head unit screen content throughout the update execution is recorded
4. The update completes in background mode; no SW Update HMI screen, prompt, or progress notification appears on the head unit
```

**specification_reference**
```
CFTS057-4907475
```

**design_method**：`功能測試 (Functional based ; no specific technique)`
**priority**：`P1`

**階段二錨定之依據**：`4907475`（章 4.7.3.2，首選 0.278）述
「silent updates run automatically without any progress notifications or end user interaction」，
與本列之二個結果面（自動背景執行、不觸發 HMI）**逐面對應**。
`4907476`（候選 #3）為其近同義句，不重複列（一事一錨）。
⚠ 本列首句「validate update metadata … determine whether the update type is Silent」
於前 5 候選中**無對應之需求物件**；其判定行為疑為 4.7.3 之
update type 組態所隱含。**不臆補錨**，記於 reasoning。

---

### TC-2 ← `SWE1-FOTA-176`（facet A）

**test_item**
```
During a Silent Update session, the WiFi Update Service shall not trigger the SW Update HMI for update progress notifications.
(No progress notification during a silent session)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package classified as Silent Update is available on the OTA Server
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Read the update type received by the WiFi Update Service and record it
3. Record the head unit screen content from download start to installation end
4. Check that no update progress notification is displayed on the head unit during the session
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The recorded update type is Silent Update
3. The head unit screen content from download start to installation end is recorded
4. No update progress notification is displayed on the head unit at any point of the silent session
```

**specification_reference**
```
CFTS057-4907476
```

**design_method**：`功能測試 (Functional based ; no specific technique)`
**priority**：`P1`

---

### TC-3 ← `SWE1-FOTA-176`（facet B）

拆分依據（IN §8.2.2）：本列含二個**獨立之部分失效** ——
(A) 靜默期間出現進度通知；(B) 安全所需之通知未被允許。
二者各自失效皆會使單一 TC 判 fail，判決不可辨，故拆。二 TC 同 trace `SWE1-FOTA-176`。

**test_item**
```
During a Silent Update session, the WiFi Update Service shall allow user notification only when required to satisfy safety-related requirements.
(Safety-required notification is permitted during a silent session)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package classified as Silent Update is available on the OTA Server
3. PENDING: DR-SU1 靜默期間之安全相關通知條件清單
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Read the update type received by the WiFi Update Service and record it
3. PENDING: DR-SU1 觸發一項安全相關條件之步驟
4. Check that the safety-related notification is displayed on the head unit during the silent session
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The recorded update type is Silent Update
3. PENDING: DR-SU1 安全相關條件之成立狀態
4. The safety-related notification is displayed on the head unit while the silent session continues
```

**specification_reference**
```
CFTS057-4907477
```

**design_method**：`功能測試 (Functional based ; no specific technique)`
**priority**：`P1`

> **DR-SU1（本 feature 首筆）**：`4907477` 與 037 `SWE1-FOTA-176` 皆僅稱
> 「necessary for safety requirements」，**未列舉何者為安全相關條件**。
> 無此清單則無可執行之觸發步驟。依 IN §8.4.3 掛 `PENDING`，
> **不得自行舉例**（如 eCall、碰撞偵測）—— 舉例即造值。

---

### TC-4 ← `SWE1-FOTA-177`

**test_item**
```
If the SW Update HMI is available, the assigned update service shall not present the user with options to opt out of or defer the update.
(No opt-out or defer option offered when HMI is available)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. The SW Update HMI is available on the head unit
3. An update package classified as Silent Update is available on the OTA Server
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Read the update type received by the update service and record it
3. Record every SW Update screen displayed on the head unit during the session
4. Check that no screen offers an opt-out control or a defer control to the user
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The recorded update type is Silent Update
3. Every SW Update screen displayed during the session is recorded
4. None of the recorded screens offers an opt-out control or a defer control
```

**specification_reference**
```
CFTS057-4907478
```

**design_method**：`負向測試 (Negative / Invalid)`
**priority**：`P2`

**階段二錨定之依據**：路徑 A **首選為 `4907662`（章 4.11）** ——
其述為「HMI SHOULD provide the user with opt in options: Install or schedule later」，
是**相反之規定**（一般更新之 opt-in），非本列所述。
正解為候選 **#2 `4907478`**（章 4.7.3.2）：
「If an HMI is available, the user SHALL NOT be presented with a choice of
opting out or deferring the update」—— 與本列**逐句對應**。
**此為 R-SU14 v5「不取首選為錨」之實例**：首選之章正確與否不論，
其內容與本列**語意相反**，若取首選即成錯錨。

---

### TC-5 ← `SWE1-FOTA-183`

**test_item**
```
When the update completes, the OTA client will display a success notification and what's new details.
(Completion notification with What's New shown after a silent update)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package classified as Silent Update is available on the OTA Server
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. Wait for the silent update deployment to complete
3. Read the deployment status reported to the update service and record it
4. Check that the head unit displays the update success notification together with the What's New details
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. The silent update deployment completes
3. The recorded deployment status is success
4. The head unit displays the update success notification and the What's New details of the deployed package
```

**specification_reference**
```
CFTS057-4907485
```

**design_method**：`功能測試 (Functional based ; no specific technique)`
**priority**：`P2`

**範圍紀律之記錄（IN §8.4.2）**：候選 #3／#4／#5（`4907634`／`4907908`／`4907889`）
皆載 `PU0410` 之彈窗編號，但其所屬章為 `4.10.5.1`／`9.3`／`9.1`
（ROV 與 Post-Installation 之情境），**非本列所在之 4.7.3.2**。
本列之正解 `4907485` **未指定任何彈窗編號**。
故 TC 不引 `PU0410` —— 引之即為自外部章節挪用規則。

---

### 4.1 本批之共通事項（供審）

- `input_test_data` 全為 `NA` —— 依 R-1 v2（SWC 0708 實測 285/286 為 `NA`），
  資料已內聯於 Pre-Condition 與 Procedure
- 各 TC 之 Final Step 皆為唯一驗證步驟（IN §5.5）
- `test_item` 皆為兩段式，下半括號**兩兩不同**（R-S4 sibling 區分）
- 各欄各行**無尾句號**（IN §11）
- UI 標籤未出現方括號；本批無 H/K 按鍵與具名彈窗
- `SWE1-FOTA-179`–`182`、`184` 之 TC 待本批審定後續作

---

## 五、任務（T32）

| # | 任務 |
|---|---|
| T32a | **母本專案名稱之實測**（R-SU24）：實測 036 母本封面／表頭之專案名稱儲存格（含其位址與原值），回報實值。**不得推定** |
| T32b | **pilot TC 之 lint**：對 §四 之 5 個 TC 跑現有 lint（含檢查 P 之 profile 行為、尾句號、引號、欄位鍵完整性）。**PENDING 之列預期會觸發缺件檢查 —— 如實回報，不得為使其通過而改寫** |
| T32c | **DR 台帳**：`DATA_REQUESTS.md` 新增 **DR-SU1**（依 §四 TC-3 之措辭），狀態 `OPEN`。本 feature 之 DR 由 0 筆變 1 筆，後續每包附未結清單 |
| T32d | **機制 3 判準改 `≤`**（R-SU23(b)）：修改實作並重跑，回報改判準後全母體攔下之列數（原 62）與其差集（新增被攔之列 id） |
| T32e | **孤島檢查之 strict 宣告**（R-SU20 v2(a)）：於 `islands.py` 與 `framework.md` 明載採 strict 及其**已知盲區**（群邊界之錯分不被覆蓋） |
| T32f | **T-抄**：R-SU20 v2、R-SU23、R-SU24 逐字 append；索引表同步（24 條現行、R-SU20→v2；留存 14 條）。PLAYBOOK 追加：「種子必須是獨立觀測 —— 由待驗規則推算出之預期值不得充當種子」（出處：上繳包 17 §7.2） |

**不在本輪**：其餘 5 列之 TC、寫回、git。

---

## 六、上繳包要求（`docs/upstream/18_pilot_review.md`）

1. T32f 核對結果 + 索引表
2. T32b 之 lint 全輸出 —— **本輪核心**
3. T32a 之實測值（決定 TC ID 是否可產出）
4. T32c／T32d／T32e 之結果
5. 未結 DR 清單（應為 1 筆）
6. 獨立自評 —— 特別回答：**§四之 5 個 TC，有無哪一個之 Procedure 步驟
   在實機上不可執行**（例如「Read the update metadata received by the WiFi
   Update Service」是否有可操作之讀取途徑；若無，該步驟即為紙上可寫、
   台架不可跑）
