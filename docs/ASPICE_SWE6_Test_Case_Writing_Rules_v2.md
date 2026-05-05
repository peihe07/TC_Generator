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

### 1.1.1 Test Item 命名指引

Test Item 用來識別「這個 TC 在驗證需求中的哪個行為 / 哪個情境」。本指引提供命名建議，**不強制單一格式**——選擇能讓審查者一眼看懂測試重點的寫法即可。

#### 可接受的命名形式

| 形式 | 適用情境 | 範例 |
|---|---|---|
| **A. 規格原句** | 直接引用 SWRA / Requirement 條文，保留 traceability | `The radio HU shall allow a user to see system information` |
| **B. 規格原句 + 情境括號** | 同需求下有多個 sibling TC，需區分情境 | `The radio HU shall allow a user to see system information`<br>`(Cold boot)` |
| **C. Topic Header + 條列項目** | 規格條文以多行列舉子項目（顯示資訊、支援格式等） | `BT Devices`<br>`The display shall show the following information:`<br>`BT Friendly Name` |
| **D. Trigger → Outcome（簡潔型）** | 因果關係單純、可一句話表達 | `Select CarPlay icon → CarPlay interface displayed` |

#### 撰寫原則（不論採用哪種形式皆適用）

- **保留 traceability 優先**：直接引用規格原句不需改寫
- **多行排版**：規格原句與情境括號之間空一行
- **情境括號用 sibling 區分**：當同需求下產生多個 TC，每個 TC 需以 `(...)` 標示其獨特情境
- **禁止 hedge 詞**：`should` / `may` / `within reasonable time` / `properly` / `successfully`

#### Sibling 區分規則（必要時）

同一個規格條文若衍生多個 TC，每個 Test Item 必須在情境括號中標明區分點，避免兩個 sibling 看起來完全一樣。判別法：把兩個 Test Item 並排，能不能立刻看出差異？不能 → FAIL。

範例：
```
The radio HU shall allow a user to see system information
(Cold boot)
```
```
The radio HU shall allow a user to see system information
(Power Cycle)
```
```
The radio HU shall allow a user to see system information
(Low memory)
```

#### 撰寫檢核

- 是否能識別出對應的 Requirement / SWRA 條文？
- 同需求下其他 TC 與本 TC 的差異是否在 Test Item 上即可區分？
- 是否刪除了所有 hedge 詞？

---

### 1.1.2 Requirement ↔ SWRA 衝突處理

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

### 1.6 Test Set — 測試集分組

Test Set 是 Test Item 的上層分組欄位，用於將同一子功能的 TC 聚集在一起，方便測試管理與審查。

#### 命名規則

- **形式**：名詞或名詞片語，1–3 個英文字
- **對應對象**：SWRA / Req 的子功能模組（e.g. `Bluetooth`, `ECU Certificate`, `System Information`），**不是**測試技術類別
- **內聚原則**：同 Test Set 內所有 TC 應共享 setup pattern 與 UI 進入路徑
- **拼寫一致性**：全專案統一拼寫（case-sensitive），禁止尾隨空白，禁止同義異寫

#### 禁止寫法

- 動詞短句：`Verify XXX`
- 完整句子
- `(...)` 括號標籤（情境標籤屬於 Test Item，不屬於 Test Set）
- 縮寫變體混用

#### 範例對照

| ✅ 正確 | ❌ 錯誤 |
|---|---|
| `Bluetooth` | `BT (Bluetooth)` — 縮寫變體 |
| `System Information` | `Test System Info` — 動詞 + 縮寫 |
| `ECU Certificate` | `ECU Cert.` — 縮寫 |
| `Showroom Demo Mode` | `Showroom_demo_mode` — 命名風格不一致 |

> **同義異寫警示**：`Screenshot` 與 `Screen Shot`、`System log` 與 `System Logs ` 不可共存於同一專案。決定一種寫法後全專案統一。

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

### 2.2 Connect / Insert 的判別準則

`Connect` / `Insert` 類動作（USB、藍牙裝置、SD 卡等）要放 Pre-Condition 還是 Procedure，依下列判別法決定：

#### 判別法：移除測試會失敗嗎？

把該裝置「移除」後，TC 是否仍能執行？
- **不能執行** → 屬於環境前提，可放 Pre-Condition
- **能執行，但測試的就是「插入動作本身」** → 必須放 Procedure

#### 範例對照

| 情境 | 歸屬 | 寫法 |
|---|---|---|
| 測試 USB 內檔案的處理（移除 USB 則無法測） | Pre-Condition | `1. A USB drive containing valid Demo Video files is connected.` |
| 測試「插入 USB 時是否顯示通知」（插入動作本身就是被驗證的觸發） | Procedure | `Step 3: Insert USB drive into HU port.` |
| 測試 PBAP 同步功能（裝置必須先 paired） | Pre-Condition | `1. A PBAP-supported device is paired.` |
| 測試「首次 pairing 流程」 | Procedure | `Step 2: Initiate Bluetooth pairing on the HU.` |

---

## 3. Input Test Data — 輸入測試資料

### 3.1 欄位分工原則

測試資料分配三層，**互斥不重複**：

| 層級 | 資料類型 | 寫入欄位 | 範例 |
|---|---|---|---|
| 1 | **環境型資料**（檔案、裝置、外部訊號源） | Pre-Condition | `1. A USB drive containing valid .mp4 video files is connected.` |
| 2 | **互動型資料**（按鍵、選項、UI 值） | Procedure step 文字內 | `Press [Screen Off] button.` |
| 3 | **獨立資料集**（CAN 訊號值、邊界數值、批次測試數據） | Input Test Data 欄位 | `CAN: VinLockStatus = 0x01` |

### 3.2 何時填 NA

- 若資料已落入第 1 層（PC）或第 2 層（Procedure），本欄位填 `NA`
- **禁止重複描述**——同一份資料不可同時出現在 PC、Procedure、Input 三處
- UI 操作型 TC 多數本欄位為 `NA`，這是合理的，**不視為 self-check 失敗**

### 3.3 範例

| 情境 | Input Test Data 欄位內容 |
|---|---|
| UI 操作型 TC（資料埋在 Procedure step） | `NA` |
| Boundary 測試（多個邊界值） | `File size: 200MB / 201MB` |
| CAN 訊號注入測試 | `CAN: VinLockStatus = 0x01` |
| 批次格式測試 | `Test files: video_5MB.mp4, video_300MB.mp4` |

---

## 4. Test Procedure (Steps) — 測試步驟

### 4.1 原則 A：每個 Step 必須有明確目的

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

### 4.2 原則 B：Final Step 必須觸發驗證目標

最後一個 Step 必須直接觸發本 TC 的測試重點。如果最後一步只是導航或開啟畫面，而未觸發需要驗證的行為，則測試重點不明確。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| `Select "Showroom Demo Video" on App Drawer page.` | `Select "Showroom Demo Video" and start playback of the uploaded .mp4 video.` |
| → 僅開啟頁面，未觸發播放行為 | → 明確觸發「播放已上傳影片」 |
| → 測試者不知道要驗證什麼 | → 測試者立刻知道要驗證的是影片播放 |

---

### 4.3 Step 其他規則

- Step 必須是可執行動作（user operation / test tool operation / system trigger）
- Step **不可包含 Verify / Confirm**（驗證目的）— 驗證描述應出現在 Expected Result
- 重複操作必須定義明確次數或停止條件

---

### 4.4 比較情境必須先建立基準狀態 (Baseline)

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

### 4.5 禁用模糊動詞，改用明確檢查動詞

Step 的主要動詞決定了測試者是否能清楚知道「這一步要做什麼、要看什麼」。模糊動詞（如 `observe`、`verify`）會讓驗證目標不明確，測試者必須自行判斷，違反 SWRA 的可重現與確定性原則。

#### 4.5.1 禁用動詞清單（hard rule）

以下動詞**不可作為 Step 的主要動詞**，因為它們隱含「用眼睛看、自己判斷」的意味，導致驗證目標模糊：

| 禁用動詞 | 問題 |
|---|---|
| `observe` | 沒有具體目標，測試者不知看什麼 |
| `observe whether` | 「是否」把判斷責任丟給測試者 |
| `see if` | 同上，未提供明確判斷標準 |
| `check whether` | 應使用 `check that` 明確描述標準 |
| `confirm whether` | 應使用 `confirm that` 明確描述標準 |
| `verify` | 在 SWE.6 語境中過度廣泛；請改用明確動詞 |

**關於 `verify` 的例外說明：**
`verify` 可以用於描述「目的」，例如 `... to verify that the phone is connected.`，但**不可作為 Step 的主要動作動詞**。因為 `verify` 本身沒有指定具體的檢查手段（看 UI？讀 log？比對數值？），在執行時會產生歧義。

#### 4.5.2 推薦動詞清單（Preferred Verbs）

每個推薦動詞後面都必須接一個**具體、可觀察的目標**（UI 元件、log 訊息、signal 數值、計數、狀態）：

| 推薦動詞 | 用途 | 範例 |
|---|---|---|
| `Check` / `Check that` | 確認 UI 狀態或系統狀態符合預期 | `Check that the CarPlay home screen is displayed on the HU.` |
| `Confirm` / `Confirm that` | 確認特定條件成立或事件發生 | `Confirm the BT icon appears in the status bar within 3 s.` |
| `Read` | 讀取並取得具體數值 | `Read the contact count on the HU.` |
| `Record` | 記錄數值以供後續比對 | `Record the initial phonebook entry count.` |
| `Compare` | 比對兩個具體數值 | `Compare the current count with the recorded baseline.` |

#### 4.5.3 錯誤與修正對照

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| `Observe the screen.` | `Check that the Home screen is displayed on the HU.` |
| `Observe whether CarPlay launches.` | `Check that the CarPlay interface is displayed on the HU.` |
| `Check whether the BT icon is displayed.` | `Check that the BT icon is displayed in the status bar.` |
| `Verify the phonebook count.` | `Read the phonebook count on the HU and record the value.` |
| `Verify the call is connected.` | `Confirm that the call is connected by checking the call status on the HU.` |

#### 4.5.4 與 §4.3 原則整合

§4.3 原本規定「Step 不可包含 Verify / Confirm，驗證描述應出現在 Expected Result」。在實務上這有兩種情況：

1. **最終驗證動作：** 由 Final Step 承擔，其描述形式為「執行動作 + check that 可觀察結果」（例：`Select the CarPlay icon in the Menu Bar and check that the CarPlay interface is displayed on the HU.`）。實際的通過/失敗判斷仍寫在對應的 Expected Result。
2. **中間設定確認：** 若需要在流程中建立 baseline（例：§4.4 的 `Check the HU phonebook contains exactly 5,000 entries.`），使用推薦動詞 `Check that` 是允許的，因為它本身就是一個具體、可執行的讀取並比對動作。

原則不變：**Step 是可執行的動作；驗證標準寫在 Expected Result**。但 Step 中的「check that / confirm that」是為了讓 Final Step 與 baseline 確認具備明確的操作意圖，並非把 ER 的內容複製到 Step。

---

### 4.6 Standard Setup Snippets — 標準步驟常數

專案級重複出現的標準步驟應定義為**全專案常數**，所有 TC 統一引用；大小寫、連字號、空格不容許變體。

#### 範例常數表（專案應自行維護）

| 常數名稱 | 標準字串 |
|---|---|
| `ENTER_DEALER_MODE` | `Press and Hold the top right and bottom left corners of the screen for 5 seconds to enter Dealer Mode.` |
| `ENTER_ENG_MODE` | `Press and Hold the top left and bottom right corners of the screen for 5 seconds to enter Eng Mode.` |
| `SCREEN_OFF` | `Press H/K [Screen Off] button to turn off the HU screen.` |
| `OPEN_APP_DRAWER` | `Press [Apps] on Menu Bar to open App Drawer.` |

#### 工具側強制機制

- prompt builder / linter 應 enforce 統一字串
- export 前自動修正大小寫 / 連字號 / 空格變體
- 新增常數時須同步更新本規則文件與工具常數表，不容許 ad-hoc 寫法擴散

---

### 4.7 Tooling / CLI 步驟格式

當步驟需要執行 shell / adb / CAN tool 等外部指令，採「**動作描述 + 實際指令**」雙行格式：

#### 格式規則

- **動作描述行**：用業務語言說明意圖，維持步驟編號
- **指令行**：以 `$` 開頭，**不加編號**，緊接於說明之下
- **對應 ER 行**：只描述觀察到的結果，不重複指令字串

#### 範例

```
Procedure:
3. Mount a tmpfs of 1 GB to occupy actual RAM.
   $ mount -t tmpfs -o size=1024M tmpfs /data/local/tmp/ramtest

4. Fill tmpfs with zero-filled blocks to consume memory.
   $ dd if=/dev/zero of=/data/local/tmp/ramtest/blob bs=10M count=100

ER:
3. tmpfs is mounted at /data/local/tmp/ramtest.
4. Available memory has decreased.
```

#### 設計意義

- 業務描述讓非工程師審查者能理解意圖
- 指令讓執行者可直接複製執行

---

### 4.8 步驟長度與意圖層級

步驟分三類管理，**不是一刀切字數限制**。判別「該步驟是否該包含 `to ...` 意圖子句」是核心。

#### A. 一般執行步驟（setup / transition）

- **目標長度**：≤ 12 字
- 動作 + 目標即可，不加意圖子句
- ✓ `Press [Screen Off] button to turn off the HU screen.`（UI 多用途，加 to 合理）
- ✓ `Insert USB device.`
- ✗ `Press the Screen Off button on the head unit so that we can later enter Eng Mode by pressing the corners.`（解釋背景）

#### B. Final Step（§4.2 verification owner）

- **必須含意圖**：`check that ...` / `to verify ...` / `... to check ...`
- **長度容許上限**：≤ 18 字（因為要包含 ACTION + check target + 期待對象）
- ✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU.`
- ✓ `Open "BT Friendly Name and Mac Address for each connected device" menu item to check Bluetooth information.`

#### C. 意圖必要的 setup 步驟（§4.1 三條件例外）

當步驟符合下列三條件之一，可加 `to ...` 子句，長度可放寬至 18 字：

1. UI 多用途（同一按鈕在不同情境下做不同事）
2. 設置非顯性 precondition（執行該動作的目的不直觀）
3. 目標不透明（手勢、深層選單、原始 AT 指令）

範例：
- ✓ `Press and Hold the top right and bottom left corners of the screen for 5 seconds to enter Dealer Mode.`（UI 不透明，必要意圖）
- ✓ `Mount tmpfs of 1 GB to occupy actual RAM.`（非顯性 precondition）

#### 判別法（寫完後自問）

> 「拿掉這個 `to ...` 子句，下一個步驟還能無歧義執行嗎？」

- 能 → 拿掉（屬 A 類）
- 不能 → 保留（屬 B 或 C）

#### 通則

- 不重複前一步已建立的狀態（`HU screen is OFF` 不需在每步重申）
- 不解釋設計理由 / 背景知識（那屬 reasoning 欄位，不屬步驟）
- 不寫條件分支（`if X then Y` → 拆成兩個 TC，見 §1.4）

---

## 5. Expected Result — 預期結果

### 5.1 必須是可觀察的結果

Expected Result 必須能透過以下方式驗證：

- UI display（介面顯示）
- system state change（系統狀態變化）
- measurable behavior（可量測行為）
- external observable response（外部可觀察回應）

不可使用模糊描述。

---

### 5.2 必須完整覆蓋驗證目標

**Mistake #6：** Expected Result 僅確認上傳成功，未驗證播放是否正常，這樣不算完整覆蓋 Test Item 的驗證目標。

| ❌ 錯誤 | ✅ 正確 |
|---|---|
| Showroom Demo Video from USB has been uploaded on Showroom Demo Video page. | The uploaded .mp4 video is displayed and playback starts successfully. |
| → 僅確認上傳成功，未驗證播放 | → 同時驗證上傳結果與播放功能 |

---

### 5.3 Step N ↔ Expected Result N 一對一

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

### 5.4 不可重述需求原文

Expected Result 必須描述 observable outcome，不可簡單複製貼上需求規格文字。必須是具體可觀察的描述，例如 UI 上顯示什麼、數字是多少、狀態變成什麼。

---

### 5.5 多階段 ER 編排

當 Procedure 含「**環境建立階段**」與「**主驗證階段**」（典型如 Fault Injection / Boundary 測試），ER 採以下編排：

#### 編排規則

- 兩階段間以**空行**分隔
- 最終驗證若需列舉多項 sub-items，用 `a./b./c.` 子層 + `-` bullet
- 階段內仍維持與 Procedure step 的 1:1 對應（§5.3 主規則不變）

#### 完整範例

```
Procedure (Fault Injection — Low Memory):
1. Access adb shell.
2. Check current RAM usage.
3. Mount tmpfs of 1 GB.
4. Fill tmpfs to consume RAM.
5. Re-check available memory.
6. Press [Screen Off] button.
7. Enter Dealer Mode.
8. Select System Information.

Expected Result:
1. adb shell is accessed.
2. RAM usage is visible.
3. tmpfs is mounted at /data/local/tmp/ramtest.
4. tmpfs is populated.
5. Available memory has decreased.

6. HU screen is OFF.
7. Dealer Mode page is displayed.
8. System Information includes:
   a. Radio Part Information
      - Hardware part number
      - Software version number
   b. SDAR Information
      - SDAR hardware version
      - SDAR firmware version
```

#### 設計意義

空行分隔讓審查者一眼看出「環境準備」與「主測試」的界線；子層 bullet 列舉細項時不需強行用編號，可讀性高於一行塞滿。

---

### 5.6 行末標點：四欄位末尾不加句點

**Pre-Condition / Input Test Data / Test Procedure / Expected Result** 四欄輸出時，**每一行末尾不加句點**（`.` 與 `。` 都不加）。行內的句點保留（多句連寫時的內部標點不受影響）。

#### 適用範圍

- 編號項（`1.` / `2.` / `a.` 等）的內容文字末尾
- 多階段 ER 中每一行（含子層 bullet）

#### 範例

| ✗ 末尾加句點 | ✓ 末尾不加句點 |
|---|---|
| `1. BT is enabled.` | `1. BT is enabled` |
| `1. Press [Screen Off] button. Wait 5 seconds.` | `1. Press [Screen Off] button. Wait 5 seconds` |
| `2. CarPlay home screen is displayed on the HU.` | `2. CarPlay home screen is displayed on the HU` |

#### 設計意義

四個欄位以條列為主，每行語意已由換行界定，末尾句點在 Excel 表格中視覺上是噪訊；統一不加，與既有 reviewer 範本格式一致。

> 註：本文件 §5.5、§6 之既有範例尚保留舊格式（行末有句點），僅供結構說明用，**正式輸出請以本節規則為準**。Tooling（writer + LLM normalizer）會在輸出時自動清掉行末句點。

---

## 6. 完整範例：Reviewer 修正後的 Test Case

### 6.1 AddressBook — Add Contact After Deletion to Return to 5,000

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

### 6.2 Caller ID — 同步前後顯示變化

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

> Reviewer 思路:「電話簿沒同步前顯示號碼，同步後顯示名字，也是一種優先度確認方式」

### 6.3 DealerMode — Upload Supported Video File Type (.mp4)

> 此範例同時展示：Step Purpose（4.1）、Final Step 驗證目標（4.2）、個別格式驗證（1.4）、Standard Setup Snippets（4.6）

```
Test Set: Showroom Demo Mode

Test Item:
  Dealer Mode shall only allow video file types to be uploaded.
  Reference CFTS018 for the allowed video file types.
  (Upload supported video file type: .mp4)

Pre-Condition:
  1. Dev / Pre-Prod build only.
  2. A USB drive containing a valid .mp4 video file is connected.

Input Test Data:
  NA

Test Procedure:
  1. Press H/K [Screen Off] button to turn off the HU screen.   ← SCREEN_OFF
  2. Press and Hold the top right and bottom left corners
     of the screen for 5 seconds to enter Dealer Mode.          ← ENTER_DEALER_MODE
  3. Select "Showroom Demo Mode information".
  4. Select "File Browser".
  5. Select "Upload Showroom Demo Video from USB".
  6. Select the .mp4 video file and confirm upload.
  7. Tap "X" to exit Dealer Mode.
  8. Press [Apps] on Menu Bar to open App Drawer.               ← OPEN_APP_DRAWER
  9. Select "Showroom Demo Video" and start playback
     of the uploaded .mp4 video.                                ← Final Step 觸發驗證

Expected Result:
  1. The HU screen is turned off.
  2. Dealer Mode is entered successfully.
  3. Showroom Demo Mode information page is displayed.
  4. File Browser page is displayed.
  5. The upload option for Showroom Demo Video is available and selectable.
  6. The selected .mp4 video file is accepted for upload.
  7. Dealer Mode is exited and the previous screen is displayed.
  8. App Drawer page is displayed.
  9. The uploaded .mp4 video is displayed and playback starts.
```

> 注意：每種支援格式（.avi, .mpg, .wmv, .3gp, .mkv）各需一個獨立 TC，僅 Test Item 情境標示和 Step 5/6/9 的檔案格式不同。

### 6.4 DealerMode — Low Memory Fault Injection（多階段 ER 範例）

> 此範例展示：Tooling/CLI 步驟格式（4.7）、多階段 ER 編排（5.5）

```
Test Set: System Information

Test Item:
  The radio HU shall allow a user to see system information
  (Low memory)

Pre-Condition:
  1. ADB is connected.

Input Test Data:
  NA

Test Procedure:
  1. Access adb shell to enter the device shell.
     $ adb shell

  2. Check current RAM memory usage.
     $ cat /proc/meminfo | grep -E "MemTotal|MemAvailable|Cached"

  3. Mount a tmpfs of 1 GB to occupy actual RAM.
     $ mount -t tmpfs -o size=1024M tmpfs /data/local/tmp/ramtest

  4. Fill tmpfs with zero-filled blocks to consume memory.
     $ dd if=/dev/zero of=/data/local/tmp/ramtest/blob bs=10M count=100

  5. Re-check available memory to confirm RAM is reduced.
     $ cat /proc/meminfo | grep -E "MemAvailable|Cached"

  6. Press H/K [Screen Off] button to turn off the HU screen.
  7. Press and Hold the top right and bottom left corners
     of the screen for 5 seconds to enter Dealer Mode.
  8. Select "System Information" and check that all displayed
     information is shown correctly under low memory conditions.

Expected Result:
  1. adb shell is accessed.
  2. RAM memory usage is visible.
  3. tmpfs is mounted at /data/local/tmp/ramtest.
  4. tmpfs is populated; data is written successfully.
  5. Available memory has decreased.

  6. HU screen is OFF.
  7. Dealer Mode page is displayed.
  8. System Information includes:
     a. Radio Part Information
        - Hardware part number
        - Software version number
        - Serial number
        - Android version
     b. SDAR Information
        - SDAR hardware version
        - SDAR firmware version
```

---

## 7. 自檢清單：18 項必檢錯誤

| # | 錯誤類型 | ✔ |
|---|---|---|
| 1 | Pre-Condition 包含操作或驗證目標 | ☐ |
| 2 | Pre-Condition 包含系統預設狀態或不必要資訊 | ☐ |
| 3 | 一個 TC 驗證多個獨立情境 | ☐ |
| 4 | Final Step 未觸發驗證行為 | ☐ |
| 5 | Test Steps 缺乏明確目的 | ☐ |
| 6 | Expected Result 模糊或不可觀察 | ☐ |
| 7 | Expected Result 未完整覆蓋驗證目標 | ☐ |
| 8 | Test Item 未明確識別需求 / 情境 | ☐ |
| 9 | TC 與 Requirement / SWRA 意圖不符 | ☐ |
| 10 | 多種支援項目未個別驗證 (False Pass 風險) | ☐ |
| 11 | 同一 Req 下多個 TC 未區分各自 scenario | ☐ |
| 12 | 涉及比較的測試未先建立 Baseline | ☐ |
| 13 | Test Item 包含 hedge 詞（should / properly / successfully 等） | ☐ |
| 14 | Step 使用禁用模糊動詞（observe / verify 等） | ☐ |
| 15 | Test Set 命名違規（動詞 / 縮寫變體 / 同義異寫）§1.6 | ☐ |
| 16 | Input Test Data 與 PC / Procedure 重複描述 §3.1 | ☐ |
| 17 | 標準 setup 步驟未引用全專案常數，出現變體 §4.6 | ☐ |
| 18 | 多階段 TC 之 ER 未採空行分隔編排 §5.5 | ☐ |
| 19 | PC / Input Test Data / Procedure / ER 行末出現句點 §5.6 | ☐ |
