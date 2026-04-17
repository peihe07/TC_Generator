# ASPICE SWE.6 Test Case 撰寫規則
---

Test Case 必須符合 ASPICE SWE.6 核心要求：

- **Deterministic** 確定性 — 結果不可有模糊空間
- **Reproducible** 可重現 — 任何人執行結果相同
- **Auditable** 可稽核 — 可作為識證證據
- **Traceable** 可追溯 — 每個 TC 對應到需求
- **Free from False Pass** — 無假通過風險

---

## 1. Test Item — 測試項目設計

### 1.1 必須對齊需求意圖

Test Item 定義「這條 Test Case 要驗證什麼」。每個 Test Item 必須對應一個 Requirement behavior 或一個 Requirement scenario，不可自行發揮或偏離需求。

#### ❌ Mistake #7 — 測項設計與需求/SWRA 皆無關

**Requirement：**
> Camera Mode: The HU shall have the option to enable or disable the engineering configuration. If disabled, the HU shall revert to default parameters.

**錯誤的 Test Procedure：**
```
1. Launch EngMode.
2. Select Camera Mode.
3. Change any settings on the Camera Mode screen.
4. Launch RVC.
```
> 問題：測項僅測試 Camera Mode 畫面操作與 RVC 啟動，與需求意圖 (enable/disable → revert to default) 毫無關係。

#### ✅ 正確的 Test Procedure：
```
1. Launch EngMode.
2. Set Engineering Configuration to Enable.
3. Change at least one camera-related parameter.
4. Check the changed parameter is applied.
5. Re-launch EngMode and Set Engineering Configuration to Disable.
6. Check the parameter reverts to default on the HU.
```
> → 完整驗證 enable → change → disable → revert to default 流程。

---

#### ❌ Mistake #7(2) — 未驗證需求關鍵行為

**Requirement：**
> The HU shall create the 'All Call Logs' list by analyzing the time stamps of the Outgoing, Incoming and Missed Call log entries.

**錯誤的 Test Procedure：**
```
1. Initiate call log download via Bluetooth pairing, wait for synchronization.
2. Observe the order of entries in the All Call Logs list.
```
> 問題：未驗證 Outgoing/Incoming/Missed 三種類型是否正確合併顯示，也缺乏可驗證 timestamp 排序正確性的測試步驟設計。

---

### 1.1.1 Requirement ↔ SWRA 衝突處理

當 SWRA 與 Requirement Description 內容矛盾時：
1. **Requirement takes precedence.**（以需求為主）
2. **Align with RD for clarification.**（進一步與 RD 釐清）

Test Case 設計必須以 Requirement 為準，不可依據與需求矛盾的 SWRA 設計驗證邏輯。

---

### 1.2 同一需求下的多個 TC 必須標示情境

Design Rule #1：同一 Requirement 下的多個 Test Case，每個 Test Item 必須明確標示其 test scenario 或 validation focus。否則無法區分各 TC 測什麼。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| `<MaxCount-AddressBookEntries> \| 5000 \| records` | `(Initial Sync = 5,000)` |
| （未標示各 TC 情境，無法區分） | `(Initial Sync > 5,000)` |
| | `(Add New Contact After HU Reaches 5,000)` |
| | `(Delete Contact After HU Reaches 5,000)` |
| | `(Add Contact After Deletion to Return to 5,000)` |
| | `(Add Duplicate Contact Below Capacity)` |

---

### 1.3 需求關鍵字分析 (Focus on Keywords)

設計 TC 前必須先分析 Requirement 中的關鍵字，確保每個關鍵概念皆有對應的驗證。

**Reviewer 實例（藍字修改）— Outgoing Call Log 關鍵字拆解：**

| 關鍵字 | 意義 | 對應 Test Scenario |
|---|---|---|
| maximum | 上限值 | TC1: Initial Sync = 60 |
| per BT device | 每個裝置獨立計算 | TC5: Per BT Device – Independent Limit |
| stop downloading | 達到上限後停止 | TC3: Stop Download（需 Log capture 確認） |
| first set ... in whatever order received | 保留最先接收的順序 | TC4: Received Order Preserved |
| （補充） | 小於上限的基本情境 | TC6: Initial Sync < 60 |

---

### 1.4 每個支援項目必須個別驗證

**Mistake #4：** 當需求明確列出多個支援項目（格式、類型、裝置等），將多種格式混合在同一 TC 驗證會產生 False Pass 風險。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| Pre-Condition: USB device is connected (Prepare the Video format contain .mp4, .avi, .mpg, .wmv, .3gp, .mkv) | 每種格式各自一個 TC： |
| → 無法確定單一格式的相容性問題 | `(Upload supported video file type: .mp4)` |
| | `(Upload supported video file type: .avi)` |
| | `(Upload supported video file type: .mpg)` |
| | `(Upload supported video file type: .wmv)` |
| | `(Upload supported video file type: .3gp)` |
| | `(Upload supported video file type: .mkv)` |

---

### 1.5 思考深度：Reviewer 的延伸情境思考

**Reviewer 實例（藍字註記）— Caller ID 情境拆解：**

> 需求要顯示 Caller ID，但要懂得思考以下情境：
> - Unknown number → 顯示電話號碼
> - Contact exists → 顯示聯絡人名稱
> - Name vs Number priority → 優先顯示什麼？
> - Unknown / Private / Withheld number → 如何顯示？
> - 電話簿沒同步前顯示號碼、同步後顯示名字 → 也是一種優先度確認方式

---

## 2. Pre-Condition — 先前條件

### 2.1 定義與判斷原則

Pre-condition 是測試開始前必須存在的「**狀態 (State)**」或「**環境 (Environment)**」，而不是測試者在執行期間要做的「**動作 (Action)**」。只包含最小必要狀態。

#### ✅ 合法的 Pre-Condition 類型

| 類型 | 判斷基準 | 範例 |
|---|---|---|
| 外部環境 | DUT 本身無法控制，需由測試設備/環境提供 | `GPS signal is available.` |
| 硬體與週邊 | 需要特定實體裝置、配件或傳輸協定支援 | `A PBAP-supported device is available.` |
| 功能初始狀態 | 為了測試 B 功能，必須先讓 A 功能處於開啟狀態 | `Bluetooth is enabled.` |
| 系統版本與模式 | 需要特定版本/模式才能執行測試 | `Dev / Pre-Prod build only.` |

#### ❌ 不可放入 Pre-Condition 的內容

| 排除類型 | 說明 | 錯誤範例 |
|---|---|---|
| 系統基本狀態 | 理所當然的系統預設，不需列出 | `The HU is powered on.` |
| 待驗證功能 | 屬於要驗證的功能，不該當作已成立的前提 | `Dealer Mode is accessible.` |
| 操作動作 | 插入裝置等動作應放在 Step | `USB or SD Card is inserted and ready.` |
| Step 控制的狀態 | 由測試步驟建立或控制的狀態 | `The device is not connected to the HU.` |
| 不必要的重複資訊 | 系統預設狀態的重複描述 | `HU is powered on and Bluetooth is enabled.` |

#### Reviewer 實例：最小狀態原則

| ❌ 原始寫法（過多不必要資訊） | ✅ 修正後（僅保留必要狀態） |
|---|---|
| 1. A PBAP-supported device is available. | 1. A PBAP-supported device is available. |
| 2. The device has 5,000 phonebook entries registered. | |
| 3. HU is powered on and Bluetooth is enabled. ← 系統預設 | |
| 4. The device is not connected to the HU. ← Step 控制 | |

---

## 3. Test Procedure (Steps) — 測試步驟

### 3.1 原則 A：每個 Step 必須有明確目的

每一步都要讓測試者在操作時心中有明確的預期結果。

判斷標準：讀完這一步後，測試者是否能立刻回答「這一步是為了什麼？」

#### ❌ Mistake #5 — Step 缺乏明確目的

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| `Press H/K [Screen off] button.` | `Press H/K [Screen Off] button to turn off the screen.` |
| → 目的不明：關螢幕？還是別的？ | → 目的明確 |
| `Press and Hold the top right and bottom left corners of the screen for five seconds.` | `Press and hold the top-right and bottom-left corners of the screen for 5 seconds to enter Dealer Mode.` |
| → 目的不明：進入什麼模式？ | → 目的明確 |
| `Tap "X"` | `Tap "X" to exit Dealer Mode.` |
| → 目的不明：關閉什麼？退出哪裡？ | → 目的明確 |

**Reviewer 實例 — Microphone Softkey 目的釐清（紅字）：**

> 「你沒有單純測試按 softkey 去控制 mute/unmute」
> 「按 microphone 邏輯上應該是 mute/unmute，但你寫的像按了去觸發 VR」
> 「VRS 不應該需要按什麼去觸發，就像 Siri enable 後需要再按什麼去觸發嗎？」
>
> → 每個 Step 的目的必須明確，避免測試者對操作意圖產生混淆。

---

### 3.2 原則 B：Final Step 必須觸發驗證目標

最後一個 Step 必須直接觸發本 TC 的測試重點。如果最後一步只是導航或開啟畫面，而未觸發需要驗證的行為，則測試重點不明確。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| `Select "Showroom Demo Video" on App Drawer page.` | `Select "Showroom Demo Video" and start playback of the uploaded .mp4 video.` |
| → 僅開啟頁面，未觸發播放行為 | → 明確觸發「播放已上傳影片」 |
| → 測試者不知道要驗證什麼 | → 測試者立刻知道要驗證的是影片播放 |

---

### 3.3 Step 其他規則

- Step 必須是可執行動作（user operation / test tool operation / system trigger）
- Step **不可包含 Verify / Confirm** — 驗證描述應出現在 Expected Result
- 重複操作必須定義明確次數或停止條件

---

### 3.4 比較情境必須先建立基準狀態 (Baseline)

**Mistake #2：** 當驗證目標涉及「變化前後的比較」時，必須在操作前先建立基準狀態。缺少基準確認，無法證明「remains at 5,000」。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| 1. Add one new contact on the device. | 1. Pair the PBAP-supported device with the HU. |
| 2. Re-trigger phonebook synchronization. | 2. **Check the HU phonebook contains exactly 5,000 entries.** ← 建立基準 |
| 3. Open the Phonebook screen on the HU. | 3. Add one new contact on the device. |
| → 未先確認 HU 已有 5,000 筆 | 4. Trigger phonebook synchronization/update. |
| → 無法證明「remains at 5,000」 | 5. Wait until synchronization is completed. |
| | 6. Open the Phonebook screen on the HU. |
| | 7. Search for the newly added contact. |
| | → 動作前確認 + 動作後確認 = 有對比 |

**Reviewer 原始檔案內嵌註記：**
> 「寫更新情境要有動作前確認 + 動作後確認 才有對比」

---

## 4. Expected Result — 預期結果

### 4.1 必須是可觀察的結果

Expected Result 必須能透過以下方式驗證：

- UI display（介面顯示）
- system state change（系統狀態變化）
- measurable behavior（可量測行為）
- external observable response（外部可觀察回應）

不可使用模糊描述。

---

### 4.2 必須完整覆蓋驗證目標

**Mistake #6：** Expected Result 僅確認上傳成功，未驗證播放是否正常，這樣不算完整覆蓋 Test Item 的驗證目標。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| Showroom Demo Video from USB has been uploaded on Showroom Demo Video page. | The uploaded .mp4 video is displayed and playback starts successfully. |
| → 僅確認上傳成功，未驗證播放 | → 同時驗證上傳結果與播放功能 |

---

### 4.3 Step N ↔ Expected Result N 一對一

每個 Step 對應一個 Expected Result，順序必須一致。不可一個 Step 對應多個 ER，也不可多個 Step 對應同一 ER。

**Reviewer 實例 — All Call Logs Interleaved Types（紅字修正）：**

```
Step 1: Pair the PBAP-supported device with the HU.
ER 1:   The device is successfully paired and connected.

Step 2: Trigger call log synchronization.
ER 2:   Call log synchronization is triggered successfully.

Step 3: Wait until synchronization is completed.
ER 3:   Call log synchronization completes successfully.

Step 4: Open the All Call Logs screen on the HU.
ER 4:   The All Call Logs screen opens successfully.

Step 5: Check the top 6 entries order in the All Call Logs list.
ER 5:   Missed(T6)→Outgoing(T5)→Incoming(T4)→Missed(T3)→Incoming(T2)→Outgoing(T1)
        → 依 timestamp 排序，與 call type 無關
```

---

### 4.4 不可重述需求原文

Expected Result 必須描述 observable outcome，不可簡單複製貼上需求規格文字。必須是具體可觀察的描述，例如 UI 上顯示什麼、數字是多少、狀態變成什麼。

---

## 5. 完整範例：Reviewer 修正後的 Test Case

### 5.1 AddressBook — Add Contact After Deletion to Return to 5,000

```
Test Item:
  <MaxCount-AddressBookEntries> | 5000 | records
  (Add Contact After Deletion to Return to 5,000)

Pre-Condition:
  1. A PBAP-supported device is available.
  2. HU phonebook entry count is 4,999 after a deletion update.

Test Procedure:
  1. Pair the PBAP-supported device with the HU via Bluetooth.
  2. Check the HU phonebook contains exactly 4,999 entries.    ← Baseline
  3. Add Contact_ReAdd on the device.
  4. Trigger phonebook synchronization/update.
  5. Wait until phonebook synchronization/update is completed.
  6. Open the Phonebook screen on the HU.
  7. Search for Contact_ReAdd.                                 ← Final Step 觸發驗證

Expected Result:
  1. The device is successfully paired and connected to the HU.
  2. HU phonebook displays exactly 4,999 entries.
  3. Contact_ReAdd is successfully created on the device.
  4. Phonebook synchronization/update starts successfully.
  5. Phonebook synchronization/update completes successfully.
  6. The HU phonebook entry count becomes exactly 5,000.
  7. Contact_ReAdd is found in the HU phonebook.
```

### 5.2 Caller ID — 同步前後顯示變化

```
Test Item:
  Caller ID display priority
  (Name vs Number after phonebook sync)

Test Procedure:
  1. Pair a mobile phone with the HU.
  2. Ensure the phone number exists in the phonebook with a contact name.
  3. Receive an incoming call before phonebook synchronization is completed.
  4. Check the Caller ID displayed on the Radio screen after synchronization.

Expected Result:
  1. The phone is paired successfully.
  2. The phone number exists in the phonebook.
  3. The incoming call is received.
  4. The display updates from phone number to contact name after synchronization.
```

> Reviewer 思路：「電話簿沒同步前顯示號碼，同步後顯示名字，也是一種優先度確認方式」

### 5.3 DealerMode — Upload Supported Video File Type (.mp4)

> 此範例同時展示：Step Purpose（3.1）、Final Step 驗證目標（3.2）、個別格式驗證（1.4）

```
Test Item:
  Dealer Mode shall only allow video file types to be uploaded.
  Reference CFTS018 for the allowed video file types.
  (Upload supported video file type: .mp4)

Pre-Condition:
  1. Dev / Pre-Prod build only.

Test Procedure:
  1. Press H/K [Screen Off] button to turn off the screen.
  2. Press and hold the top-right and bottom-left corners of the screen
     for 5 seconds to enter Dealer Mode.
  3. Select "Showroom Demo Mode information".
  4. Select "File Browser".
  5. Insert a USB storage device containing a .mp4 video file.
  6. Select "Upload Showroom Demo Video from USB".
  7. Select the .mp4 video file and confirm upload.
  8. Tap "X" to exit Dealer Mode.
  9. Open App Drawer.
  10. Select "Showroom Demo Video" and start playback
      of the uploaded .mp4 video.                        ← Final Step 觸發驗證

Expected Result:
  1. The screen is turned off.
  2. Dealer Mode is entered successfully.
  3. Showroom Demo Mode information page is displayed.
  4. File Browser page is displayed.
  5. The USB storage device is detected by the system.
  6. The upload option for Showroom Demo Video is available and selectable.
  7. The selected .mp4 video file is accepted for upload.
  8. Dealer Mode is exited and the previous screen is displayed.
  9. App Drawer page is displayed.
  10. The uploaded .mp4 video is displayed and playback starts successfully.
```

> 注意：每種支援格式（.avi, .mpg, .wmv, .3gp, .mkv）各需一個獨立 TC，僅 Test Item 情境標示和 Step 5/7/10 的檔案格式不同。

---

## 6. 自檢清單：12 項必檢錯誤

| # | 錯誤類型 | ✔ |
|---|---|---|
| 1 | Pre-Condition 包含操作或驗證目標 | ☐ |
| 2 | Pre-Condition 包含系統預設狀態或不必要資訊 | ☐ |
| 3 | 一個 TC 驗證多個獨立情境 | ☐ |
| 4 | Final Step 未觸發驗證行為 | ☐ |
| 5 | Test Steps 缺乏明確目的 | ☐ |
| 6 | Expected Result 模糊或不可觀察 | ☐ |
| 7 | Expected Result 未完整覆蓋驗證目標 | ☐ |
| 8 | Test Item 未明確定義驗證目標 | ☐ |
| 9 | TC 與 Requirement / SWRA 意圖不符 | ☐ |
| 10 | 多種支援項目未個別驗證 (False Pass 風險) | ☐ |
| 11 | 同一 Req 下多個 TC 未區分各自 scenario | ☐ |
| 12 | 涉及比較的測試未先建立 Baseline | ☐ |
