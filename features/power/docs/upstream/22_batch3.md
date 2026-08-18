# 上繳包 22 —— 節奏重整、第二批發現與第三批啟動

> 對應下放包：`features/power/docs/handoff/22_batch3.md`
> 執行層：Claude（TC_Generator）
> **§J 自檢已先驗**：§A fenced block = **8**、§J 列數 = **8**、§H 步驟 9 = 「**八條**」——
> **三處一致，未停。**
> 本包**未執行任何 git 操作**（R-P149 已知悉，見 §八(丙)）；
> **未對任何 workbook 呼叫 `save()`**；**未觸碰客戶樹與 `inputs/`**；
> **未合併或刪除三對成對錨點所生之 TC**；**未以「規格指向另一節」作為略過分支之依據**；
> **未為使 ER 有依據而造值**；**第三批之 leaf 範圍未逾 Power State 前 32**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

---

## 〇、編號查核與一項台帳缺口（§H 步驟 2，R-P147）

**先查後開，實查結果**：
**A-PW 最大 111、R-P 最大 147、DR-PW 最大 8、閘門最大 G106。**
本包新號自 **A-PW112 / R-P153 / DR-PW10 / G109** 起。

> **台帳缺口 —— `R-P148` ~ `R-P152` 未落檔。**
> `docs/handoff/21_need_rework.md` **存在**而 `docs/upstream/21_need_rework.md` **不存在**
> —— 即 **21 包未執行**。22 包 §前言載其「五條裁決維持有效」，
> 惟其條文未經抄錄，`RULINGS.md` 自 `R-P147` 直接跳至 `R-P153`。
>
> **執行層未代為抄錄** —— 抄錄其條文會使未執行之 §H 看似已做。
> 已於 `RULINGS.md` 第二十二輪之首記明此缺口，使其不致靜默。
> **`DR-PW9` 亦保留予該包（R-P148），本包未佔用**，故本包自 `DR-PW10` 起
> —— 與下放包所寫之編號恰好一致，惟係查後所得，非逕用（§K 第 3 項之要求）。
>
> **其中 R-P149 / R-P150 為對執行層之直接拘束，本包已遵行** —— 見 §八(丙)。

---

## 一、B1 —— R-P153 之落實

`037` / `039` / `042` 之 `remarks` 現載
「`DR-PW10 (Medium) 待範圍確認：來源錨點 Model Year 2017 / State Under Review`」，
通過 G50 之 §11 規則（`remarks` 自 R-P131 起已入 `LONG_FIELDS`）。
**三條 TC 未合併、未刪除。DR-PW10（Medium）已開。**

---

## 二、B2 —— R-P154 之承接查證（**最重要**）

### 2.1 訂正

`SWE-PM-057` 之 `reasoning` 原以 **R-P42** 為略過 `4941706`「LTM High present」分支之依據。
**該依據誤用** —— `4941706` **在**本 leaf 之 `source_anchor` 清單內，為被引用之錨點；
R-P42 管「未被引用者不測」，不管「被引用者之某分支得不測」。
正當依據為 **§8.2.1**，而 §8.2.1 要求列出承擔之 sibling Req ID。已改寫。

### 2.2 查詢方法與涵蓋範圍

| 項目 | 值 |
|---|---|
| 母體 | `layer3_full.tsv` 之**全 114 leaf / 238 錨點**（`SWE-PM-089` 依 R-P1 無錨點，故 114 而非 115）|
| 方法 | 取每一錨點之 CFTS 本文原文（`anchor_bodies()`，R-P17 文字層），以 `LTM\s*High` 搜尋 |
| 命中 | **8 個錨點**，逐一對其所屬 leaf 與章節判別 |

### 2.3 結論 —— **找到承接者，非 coverage hole**

`4941706` 所指之「Auto_SwitchOn_Setting.Req management section」
即 CFTS009 **§1.6.3.1.2**，錨點 **`4941710`**，屬 **`SWE-PM-062`**，
由 **`NR1L-PowerManagement-025` / `026` / `027`** 承擔。

**行為對應之依據**：`4941702` 逐字載
「For LTM/ETM, the user can set **one** parameter, by means of `Auto_SwitchOn_Setting.Req`」
—— 即 LTM High 存在時 `SwitchOff_Timeout_Setting.Req` 不可選，
`Timeout1` 改由 `Auto_SwitchOn_Setting.Req` 決定（`4941710` 之三值各附其 `Timeout1` 條件）。

已補列於 `SWE-PM-057` 之 `reasoning`（A-PW113）。

---

## 三、B3 —— R-P155 之分支查證

`025` / `026` / `027` 之 pre_condition 皆為「An LTM High Radio is present」，
**確僅測 LTM High 存在側**。

**不存在側不補測，理由為規格未定義**：
`4941710` 之三個括號條件（`If LTM High is present: "Timeout1" = / <> "00 minutes"`）
**僅就存在側給出 `Timeout1` 之結果，對不存在側之 `Timeout1` 關係一字未載**。
依 §8.4.1 不得造值，**登記為「規格未定義，不補測」**，已記入 `SWE-PM-062` 之 `reasoning`。

另記互補關係：不存在側之 `SwitchOff_Timeout_Setting.Req` 選擇由 `SWE-PM-057`
（`018` / `019` / `020`，pre_condition 為「An LTM High Radio is absent」）承擔。

---

## 四、B4 —— 全批 43 條之 ER 檢查與 G109 評估

### 4.1 R-P156 —— 斷言通話狀態變化者

以「ER 行同時含 `call` 與狀態動詞」機械篩出 **12 行**，逐行查 `source_clause` 依據：

| TC | 判定 | 處置 |
|---|---|---|
| `037` ER1 `The call is released at MaxCallTimeout expiration` | **無依據** | 改為 `MaxCallTimeout reaches its expiration while Phone_Call.Info is still "Active"` |
| `036` / `031` ER1 `The call is released and its audio is removed …` | **無依據**（原文僅載訊號轉為 `Not_Active`）| 改為該訊號之回讀 |
| `028` ER1 `… and its audio is routed through the TLM` | connected 有依據、**音訊路由無依據** | 刪去音訊路由 |
| `032` / `034` 同上 | 同上 | 改為 `is managed by the TLM` |
| `012` / `013` `routed to the head set and is not dropped` | **有依據**（`transfer the call … to the head set`）| 不改 |
| `040` / `043` `The active call is not dropped by the ignition change` | **有依據** | 不改 |

**六條修正、六條保留、未造任何值。**

### 4.2 R-P157 —— 依據落於本 leaf 範圍外者

- **`038` / `039`** 依 **(i)** 刪除 —— ER1 之「MaxCallTimeout does not start」
  出自 `4941718`（屬 `SWE-PM-064`），現為 `No call is active when Timeout1 expires`。
- **`023` / `024`** 依 **(ii)** 記入 `reasoning_note` —— 其 ER1 述 HMI 呈現，
  而 `4941703` 未載呈現方式；已明示**僅描述觀察事實，不為 pass/fail 判準**，
  本條之判準為 ER2。

### 4.3 G109 可行性評估 —— **不可行**

本條所提之機械判準為「ER 之具名標的若不出現於本 leaf 之 `source_clause`，即為候選」——
**該判準即現行之 G82，而 G82 對全批實測為 0**。

以 `038` 為例：`MaxCallTimeout` **確實出現**於其 `source_clause`（`4941726` 載之），
故 G82 不會標記；**真正越界者不是標的，而是該標的之規則**
（「僅於通話仍 Active 時啟動」）—— 該規則落在 `4941718`。

> **「標的在範圍內而其規則在範圍外」無法以 token 層比對辨識**，
> 須理解該 ER 之斷言依據哪一條規則。**故 G109 不實作，理由如上。**

---

## 五、B5 —— 第三批：**範圍未能如 R-P158 所定，兩項排除**

R-P158 令第三批為 Power State 前 32 leaf（`SWE-PM-001`–`032`）。
**實產 22 leaf / 61 條**（臨時 tc_id `044`–`104`）。兩項排除皆有明確依據：

### 5.1 排除一 —— `SWE-PM-001`–`009`（9 leaf），**DR-PW6 停**

該九 leaf 即 **DR-PW6 之影響面**：31 處懸空 `WrapperResource` 參照中，
**落在被引用錨點下之 2 處皆位於 CFTS009 §1.6.2.1**（錨點 `4941354` / `4941355`），
觸及 `SWE-PM-001`–`009`。其阻斷欄逐字為
「§1.6.2.1 之 9 個 leaf 其 TC 之 `specification_reference` 無可引之規格文字」。

本包實測確認：**該九 leaf 之錨點集合全部包含章節 1.6.2.1**。

> 於此撰寫 TC 將產出 **R-P121 所指之「可撰寫而不可執行」類 —— 較缺一條 TC 危險**。
> 另 `SWE-PM-003` 尚受 **DR-PW5（High，live）** 影響（Stolen Vehicle Mode 之涵蓋歸屬未定）。

**須提請注意**：R-P124(d) 當初擇 `Timeout Settings` 為第二批，
其理由之一正是「不觸及 DR-PW5 與 DR-PW6」。
**第三批之範圍直接撞上此二 DR，而下放包未提及**（A-PW118）。

### 5.2 排除二 —— `SWE-PM-010`（1 leaf），**G103 當場攔下**

> **這是 R-P144 / G103 立條以來之首次真實命中。**

`SWE-PM-010` 之 037 `Source Requirement ID` 經 SYS2 解析得 **8 個** item id，
而 `layer3_full.tsv` 僅載 **7 個** —— 缺 **`4941984`**。

實查 `4941984`：**於 CFTS009 / CFTS010 之文字層皆無內文段落、亦無所屬章節**
（鄰近之 `4941983` / `4941985` 皆存在）。
`build_layer3` 因其無法解析至章節而**靜默丟棄**。

| 閘 | 對 `SWE-PM-010` 之結果 |
|---|---|
| G94（`source_clause` 對 `source_anchor`）| **全綠** |
| G99（`source_anchor` 對 layer3）| **全綠** |
| **G103（layer3 對 037 獨立重算）** | **FAIL —— 缺 `4941984`** |

依 **R-P144(b)** 停並上繳：該 leaf 已自第三批排除，**已開 DR-PW11（High）**（A-PW117）。

### 5.3 第三批之概況（G111）

| 項目 | 實測 |
|---|---|
| leaf | **22**（`SWE-PM-011`–`032`）|
| TC | **61**（臨時 tc_id `044`–`104`）|
| `specification_reference` | **61 / 61 指向 CFTS009** |
| G94 / G99 / G103 | **22 / 22 皆相等**（全批 33 leaf 亦全數相等）|
| lint | `exit=0`；阻斷類 **PASS**；TC 總數 **104** |

### 5.4 分層取樣（R-P158：每 leaf 至少一條 ＋ 全部 P0）

**57 / 61 全文**。未取樣者 **4 條**：`054`、`065`、`066`、`091` —— 皆為 P1
（`SWE-PM-015` 之 Rear Camera 變體二條、`SWE-PM-026` 之前狀態 Standby 分支、
`SWE-PM-011` 之其一），其結構與同 leaf 已取樣者相同，僅前提或分支不同。
**依 R-P159，此 4 條不經分析層目視 —— 其代價已由該條明載。**

### leaf `SWE-PM-011`（本 leaf 共 6 條）

**`source_anchor`**：`4941375,4941376,4941383,4941384,4941385,4941386,4941387,4941388`　**章節**：1.6.2.1.2

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
While the HU is in IDLE mode, the HU shall transition to Full-Operation mode if the VR button is pressed. Refer to CFTS042 for VR button press definition.
The VR button press defined in CFTS009-2326 refers to both short and long presses of the VR button
If CarPlay VR was activated by the button press defined in CFTS009-2326, then the HU shall complete the Siri interaction as defined in the Apple Accessory Interface Specification
Once the CarPlay VR interaction defined in CFTS009-2329 is completed, the HU shall have different behaviors depending on the command that was issued:
If the CarPlay Device requests audio control and video control, then the HU shall remain in FULL OPERATION mode with the entertainment audio unmuted and the screen on.
If the Carplay device requests audio control and does not request video control, then the HU shall remain in FULL OPERATION mode with the audio unmuted and the Screen OFF function activated.  See CFTS020 for Screen Off definition
If the Carplay device does not request audio control and does request video control, then the HU shall remain in FULL OPERATION mode with the audio muted and the Screen On.  See CFTS020 for Screen On definition
If the CarPlay Device does not request audio control or video control, then the HU shall return to IDLE mode.
```

**`reasoning`**

> 驗證目標：IDLE 下 VR 按鍵之轉換，及 CarPlay VR 互動完成後依請求類型之四種後續行為。為什麼這樣切：四種請求組合（audio＋video / 僅 audio / 僅 video / 皆無）為四個互斥分支，依 §8.2.2 各拆一條；VR 按鍵之轉換另成一條。刻意略過：`4941376` 所述之短按與長按等價、`4941383` 所引之 Apple Accessory Interface Specification 與 CFTS042 / CFTS020 皆為外部文件，依 §8.4.2 不測本 spec 未擁有者。

#### NR1L-PowerManagement-044 — SWE-PM-011（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-044`

**req_id**：`SWE-PM-011`

**split_index**：`1`

**tc_title**：`VR button press in IDLE mode transitions the HU to Full-Operation`

**test_set**：`Power State`

**test_item**：`VR button press in IDLE mode transitions the HU to Full-Operation`

**pre_conditions**

```
1. The HU is in IDLE mode
2. A VR button is available on the bench
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Press the VR button with a short press and release it
2. Read the HU mode to check the transition to Full-Operation
```

**expected_result**

```
1. The HU accepts the VR button press
2. The HU is in Full-Operation mode
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 IDLE → Full-Operation 之 VR 觸發（短按）`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-045 — SWE-PM-011（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-045`

**req_id**：`SWE-PM-011`

**split_index**：`2`

**tc_title**：`CarPlay requesting audio and video keeps audio unmuted and screen on`

**test_set**：`Power State`

**test_item**：`CarPlay requesting audio and video keeps audio unmuted and screen on`

**pre_conditions**

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```

**input_test_data**

```
CarPlay request: audio control and video control
```

**test_procedure**

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode, the entertainment audio and the screen to check the resulting behavior
```

**expected_result**

```
1. The HU accepts the request without leaving FULL OPERATION mode
2. The entertainment audio is unmuted and the screen is on
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 audio ＋ video 皆請求之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-046 — SWE-PM-011（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-046`

**req_id**：`SWE-PM-011`

**split_index**：`3`

**tc_title**：`CarPlay requesting audio only activates the Screen OFF function`

**test_set**：`Power State`

**test_item**：`CarPlay requesting audio only activates the Screen OFF function`

**pre_conditions**

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```

**input_test_data**

```
CarPlay request: audio control only
```

**test_procedure**

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode, the audio and the screen to check the resulting behavior
```

**expected_result**

```
1. The HU accepts the request without leaving FULL OPERATION mode
2. The audio is unmuted and the Screen OFF function is activated
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗僅請求 audio 之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-047 — SWE-PM-011（split_index 4，P0）

**tc_id**：`NR1L-PowerManagement-047`

**req_id**：`SWE-PM-011`

**split_index**：`4`

**tc_title**：`CarPlay requesting video only mutes the audio and keeps the screen on`

**test_set**：`Power State`

**test_item**：`CarPlay requesting video only mutes the audio and keeps the screen on`

**pre_conditions**

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```

**input_test_data**

```
CarPlay request: video control only
```

**test_procedure**

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode, the audio and the screen to check the resulting behavior
```

**expected_result**

```
1. The HU accepts the request without leaving FULL OPERATION mode
2. The audio is muted and the Screen On function is activated
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗僅請求 video 之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-048 — SWE-PM-011（split_index 5，P0）

**tc_id**：`NR1L-PowerManagement-048`

**req_id**：`SWE-PM-011`

**split_index**：`5`

**tc_title**：`CarPlay requesting neither audio nor video returns the HU to IDLE`

**test_set**：`Power State`

**test_item**：`CarPlay requesting neither audio nor video returns the HU to IDLE`

**pre_conditions**

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```

**input_test_data**

```
CarPlay request: neither audio control nor video control
```

**test_procedure**

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode to check the return to IDLE mode
```

**expected_result**

```
1. The HU accepts the request and leaves FULL OPERATION mode
2. The HU is in IDLE mode
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗二者皆不請求之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-049 — SWE-PM-011（split_index 6，P0）

**tc_id**：`NR1L-PowerManagement-049`

**req_id**：`SWE-PM-011`

**split_index**：`6`

**tc_title**：`VR button long press in IDLE mode transitions the HU to Full-Operation`

**test_set**：`Power State`

**test_item**：`VR button long press in IDLE mode transitions the HU to Full-Operation`

**pre_conditions**

```
1. The HU is in IDLE mode
2. A VR button is available on the bench
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Press the VR button with a long press and release it
2. Read the HU mode to check the transition to Full-Operation
```

**expected_result**

```
1. The HU accepts the VR button long press
2. The HU is in Full-Operation mode
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗長按之觸發（`051` 驗短按）——`4941376` 載二者皆為該定義所指`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### leaf `SWE-PM-012`（本 leaf 共 2 條）

**`source_anchor`**：`4941449,4941450`　**章節**：1.6.2.1.13

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
After a battery reconnection and also when TLM has to exit INIT state (as soon as the voltage is limited within certain thresholds), TLM is able to work properly again and it has to restore the last user settings and the last variables values: VPLastStatus, SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored to their values before the battery disconnection / battery reset
Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Info to "Sleep" first and starting from Sleep state.
```

**`reasoning`**

> 驗證目標：電池回接／離開 INIT 後之使用者設定還原與起始狀態。為什麼這樣切：還原（`4941449`）與起始狀態（`4941450`）為兩個獨立部分失效 —— 設定還原而起始狀態錯誤仍屬失敗，反之亦然。

#### NR1L-PowerManagement-050 — SWE-PM-012（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-050`

**req_id**：`SWE-PM-012`

**split_index**：`1`

**tc_title**：`User settings are restored after a battery reconnection`

**test_set**：`Power State`

**test_item**：`User settings are restored after a battery reconnection`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req hold known values
3. The battery is disconnected
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Reconnect the battery and let the voltage settle within its thresholds
2. Read the three stored variables to check that their previous values returned
```

**expected_result**

```
1. The TLM leaves INIT state once the voltage is within its thresholds
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req read their values before the battery disconnection
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.13`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗電池回接後之使用者設定還原`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-051 — SWE-PM-012（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-051`

**req_id**：`SWE-PM-012`

**split_index**：`2`

**tc_title**：`TLM starts from Sleep state after leaving INIT`

**test_set**：`Power State`

**test_item**：`TLM starts from Sleep state after leaving INIT`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The battery has just been reconnected
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let the TLM exit INIT state
2. Read TLM_Status.Info and the state machine to check the starting state
```

**expected_result**

```
1. The TLM leaves INIT state without an error being reported
2. TLM_Status.Info reads "Sleep" and the TLM starts from Sleep state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.13`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗離開 INIT 後之起始狀態`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-013`（本 leaf 共 3 條）

**`source_anchor`**：`4941391,4941392,4941393,4941394`　**章節**：1.6.2.1.3

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Start, Ignition Start, Ignition Cranking, Ignition On Engine On, Ignition Off Ignition Pre-Off
In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". This mode shall exist for AMP, ICS, and DTV when STATUS_BH_BCM2.RemStActvSts is equal to "Remote Start Active" is recieved and TLM sends $Telematic_Power$ = "Partial_Operation"
This status is related to TLM OFF. AMP/ICS/DTV shall be OFF. Audio for ANC, ACN, and chimes (if equipped) shall be active in this state)
All TLM, AMP, ICS, and DTV functionalities run in background and are ready but not HMI interaction is enabled within this status, except for the interaction that permit a change status.
```

**`reasoning`**

> 驗證目標：Partial Operation 之進入條件、各模組電源與音訊、以及 HMI 互動之限制。為什麼這樣切：三者為獨立可觀察面，依 §8.2.2 各拆一條。刻意略過：`4941391` 為 Ignition Working Conditions 之列舉，非行為陳述。

#### NR1L-PowerManagement-052 — SWE-PM-013（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-052`

**req_id**：`SWE-PM-013`

**split_index**：`1`

**tc_title**：`Remote Start Active reports Partial_Operation`

**test_set**：`Power State`

**test_item**：`Remote Start Active reports Partial_Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition On
```

**input_test_data**

```
STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read $Telematic_Power$ to check the reported mode
```

**expected_result**

```
1. The TLM accepts the signal without a bus error
2. $Telematic_Power$ reads "Partial_Operation"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Remote Start Active 之模式回報`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-053 — SWE-PM-013（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-053`

**req_id**：`SWE-PM-013`

**split_index**：`2`

**tc_title**：`AMP, ICS and DTV are off while chime audio stays active`

**test_set**：`Power State`

**test_item**：`AMP, ICS and DTV are off while chime audio stays active`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in Partial Operation with AMP, ICS and DTV equipped
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let the TLM settle in Partial Operation
2. Read the AMP, ICS and DTV power states and the audio paths to check the active set
```

**expected_result**

```
1. The TLM stays in Partial Operation without further transition
2. AMP, ICS and DTV are OFF while audio for ANC, ACN and chimes is active
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Partial Operation 之各模組電源與音訊`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-014`（本 leaf 共 8 條）

**`source_anchor`**：`4941504,4941505,4941506,4941507,4941508,4941510,4941511,4941512`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM2.RemStActvSts has a transition  from "Remote Start Active" to "Remote Start Not Active"THEN IF LTM_OperationalModeSts.Info is equal to "Ignition Pre Off" OR to "Ignition Off", TLM has to set RemStartFail = "True" THEN IF Phone_Call.Info == "Not Active", TLM has to set RemStartFail ="False" AND TLM_Status.Info and $Telematic_Power$ to "Standby" value and it passes to TLM Standby state.IF Phone_Call.Info == "Active" TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.In this case, TLM has to stay in this state until Phone_Call.Info becomes equal to "Not_Active", OR at maximum until MaxCallTimeout expiration. See par. “Phone call management in Timed state” .ELSE IF LTM_OperationalModeSts.Info is not equal to "Ignition Pre Off" OR to "Ignition Off"  THEN TLM has to set RemStartFail = "False" AND TLM has to stay in the original state (Full Operation).IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal LTM_OperationalModeSts.Info has a transition to "Ignition Pre Off" OR to "Ignition Off" valueAND STATUS_BH_BCM2.RemStActvSts is equal to "Remote Start Not Active"AND RemStartFail == "False"THENaccording to a time setting selectable in the TLM menu it is possible to have two different behaviours
Behaviour 1: "SwitchOff_Timeout_Setting.Req == Timeout1 == 00 MIN" or ( If Auto_SwitchOn_Setting.Req =="Active", when  Timeout1 == 00 MIN" for LTM High Radio):
If Phone_Call.Info == Not_Active, at LTM_OperationalModeSts.Info transition TLM sets TLM_Status.Info and $Telematic_Power$ to "Standby" value and then it goes to TLM Standby state.
If Phone_Call.Info == Active, at LTM_OperationalModeSts.Info transition TLM sets TLM_Status.Info and $Telematic_Power$ to "Timed" value and then it goes to TLM Timed state.
In this case, TLM has to stay in this state until Phone_Call.Info becomes equal to "Not_Active", OR at maximum until MaxCallTimeout expiration. See par. “Phone call management in Timed state” .
Behaviour 2: "SwitchOff_Timeout_Setting.Req == Timeout1 <> 00 MIN" or ( If Auto_SwitchOn_Setting.Req =="Not_Active ", when  Timeout1 <> 00 MIN" for LTM High Radio):
IF Brand_Configuration _2 == "Jeep" AND STATUS_BH_BCM1.DriverDoorSts == "Open" AND PhoneCall.Info == "Not_Active" at LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Telematic_Power$ to "Standby" value and then it passes to TLM Standby state.
ELSE at LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $Telematic_Power$ to "Timed" value and then it passes to TLM Timed state, mantaining the current active source.
```

**`reasoning`**

> 驗證目標：Remote Start 結束之 RemStartFail 處理，及 Behaviour 1 / 2 於 LTM_OperationalModeSts.Info 轉換時之去向。為什麼這樣切：Behaviour 1 / 2 為兩個互斥前提（Timeout1 == / <> 00 MIN），其下各有通話中與無通話之分支，依 §8.2.2 逐一拆分；RemStartFail 之設定與清除為兩個時點，另拆二條。刻意略過：`4941508` 所引之「Phone call management in Timed state」章節屬 `SWE-PM-038` / `065`，依 §8.2.1 由其承擔。

#### NR1L-PowerManagement-055 — SWE-PM-014（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-055`

**req_id**：`SWE-PM-014`

**split_index**：`1`

**tc_title**：`Remote Start ends at ignition off: RemStartFail is set true`

**test_set**：`Power State`

**test_item**：`Remote Start ends at ignition off: RemStartFail is set true`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. LTM_OperationalModeSts.Info is at "Ignition Off"
```

**input_test_data**

```
STATUS_BH_BCM2.RemStActvSts: "Remote Start Active" to "Remote Start Not Active"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read RemStartFail to check that it follows the transition
```

**expected_result**

```
1. The TLM accepts the transition without a bus error
2. RemStartFail reads "True"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Remote Start 結束於點火關閉時之 RemStartFail 設定`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-056 — SWE-PM-014（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-056`

**req_id**：`SWE-PM-014`

**split_index**：`2`

**tc_title**：`RemStartFail is cleared when the call is not active`

**test_set**：`Power State`

**test_item**：`RemStartFail is cleared when the call is not active`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. RemStartFail reads "True"
3. Phone_Call.Info reads "Not Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let the TLM evaluate the call state after the RemStartFail transition
2. Read RemStartFail and TLM_Status.Info to check the resulting values
```

**expected_result**

```
1. The TLM evaluates Phone_Call.Info without a further transition being needed
2. RemStartFail reads "False"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗通話未啟用時之 RemStartFail 清除`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-057 — SWE-PM-014（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-057`

**req_id**：`SWE-PM-014`

**split_index**：`3`

**tc_title**：`Behaviour 1 with no active call passes the TLM to Standby`

**test_set**：`Power State`

**test_item**：`Behaviour 1 with no active call passes the TLM to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Not_Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**expected_result**

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM goes to TLM Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Behaviour 1 之無通話分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-058 — SWE-PM-014（split_index 4，P0）

**tc_id**：`NR1L-PowerManagement-058`

**req_id**：`SWE-PM-014`

**split_index**：`4`

**tc_title**：`Behaviour 1 with an active call passes the TLM to Timed`

**test_set**：`Power State`

**test_item**：`Behaviour 1 with an active call passes the TLM to Timed`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```

**expected_result**

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM stays there until Phone_Call.Info becomes "Not_Active"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Behaviour 1 之通話中分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-059 — SWE-PM-014（split_index 5，P0）

**tc_id**：`NR1L-PowerManagement-059`

**req_id**：`SWE-PM-014`

**split_index**：`5`

**tc_title**：`Behaviour 2 on a Jeep with the driver door open passes to Standby`

**test_set**：`Power State`

**test_item**：`Behaviour 2 on a Jeep with the driver door open passes to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read a value other than "00 MIN"
3. Brand_Configuration _2 reads "Jeep"
4. PhoneCall.Info reads "Not_Active"
```

**input_test_data**

```
STATUS_BH_BCM1.DriverDoorSts = "Open"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data and let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**expected_result**

```
1. The TLM registers both the door signal and the mode transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Behaviour 2 之 Jeep ＋ 駕駛門開啟分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-060 — SWE-PM-014（split_index 6，P0）

**tc_id**：`NR1L-PowerManagement-060`

**req_id**：`SWE-PM-014`

**split_index**：`6`

**tc_title**：`Behaviour 2 otherwise passes to Timed keeping the active source`

**test_set**：`Power State`

**test_item**：`Behaviour 2 otherwise passes to Timed keeping the active source`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read a value other than "00 MIN"
3. Brand_Configuration _2 reads a value other than "Jeep"
4. A tuner source is currently active
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info, $Telematic_Power$ and the active source to check the transition to Timed
```

**expected_result**

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the current active source is maintained
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Behaviour 2 之 ELSE 分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-061 — SWE-PM-014（split_index 7，P0）

**tc_id**：`NR1L-PowerManagement-061`

**req_id**：`SWE-PM-014`

**split_index**：`7`

**tc_title**：`Behaviour 1 reached through Auto_SwitchOn_Setting.Req on LTM High`

**test_set**：`Power State`

**test_item**：`Behaviour 1 reached through Auto_SwitchOn_Setting.Req on LTM High`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 MIN"
4. Phone_Call.Info reads "Not_Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**expected_result**

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM goes to TLM Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Behaviour 1 之 LTM High 形態（`063` 驗 SwitchOff_Timeout_Setting.Req 形態）`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

#### NR1L-PowerManagement-062 — SWE-PM-014（split_index 8，P0）

**tc_id**：`NR1L-PowerManagement-062`

**req_id**：`SWE-PM-014`

**split_index**：`8`

**tc_title**：`Behaviour 2 reached through Auto_SwitchOn_Setting.Req on LTM High`

**test_set**：`Power State`

**test_item**：`Behaviour 2 reached through Auto_SwitchOn_Setting.Req on LTM High`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Not_Active " and Timeout1 reads a value other than "00 MIN"
4. Brand_Configuration _2 reads a value other than "Jeep"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```

**expected_result**

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the current active source is maintained
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Behaviour 2 之 LTM High 形態（`066` 驗 SwitchOff_Timeout_Setting.Req 形態）`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### leaf `SWE-PM-015`（本 leaf 共 4 條）

**`source_anchor`**：`4941540,4941541,4941542,4941543`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHEN IF Phone_Call.Info == Not_Active TLM has to set VPLastStatus to “OFF” value and to set TLM_Status.Info and $Telematic_Power$ to "Idle" value and then it passes to TLM Idle state.
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” valueTHEN IF Phone_Call.Info == Not_Active TLM has to set VPLastStatus to “OFF” value and to set TLM_Status.Info and $Telematic_Power$ to "Idle" value and then it passes to TLM Idle state.
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHEN IF Phone_Call.Info == Not_Active AND Rear Camera is not Active (provided that proxi parameter Rear_View_Camera == "Present") TLM has to set VPLastStatus to “OFF” value and to set TLM_Status.Info and $Telematic_Power$ to "Idle" value and then it passes to TLM Idle state.
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” valueTHEN IF Phone_Call.Info == Not_Active AND Rear Camera is not active (provided that proxi parameter Rear_View_Camera == "Present") TLM has to set VPLastStatus to “OFF” value and to set TLM_Status.Info and $Telematic_Power$ to "Idle" value and then it passes to TLM Idle state.
```

**`reasoning`**

> 驗證目標：Full-Operation 下二個關機鍵之按下所致之 Idle 轉換，及其於 Rear_View_Camera 存在時之條件。為什麼這樣切：`Front_Panel_OnOff.Req` 與 `CLIMATIC_PANEL.Radio_Btn0` 為**不同觸發**（§5.7），各拆一條；`4941542` / `4941543` 另加 Rear Camera 條件，為不同前提，再各拆一條。

#### NR1L-PowerManagement-063 — SWE-PM-015（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-063`

**req_id**：`SWE-PM-015`

**split_index**：`1`

**tc_title**：`Front_Panel_OnOff.Req press with no active call passes the TLM to Idle`

**test_set**：`Power State`

**test_item**：`Front_Panel_OnOff.Req press with no active call passes the TLM to Idle`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Phone_Call.Info reads "Not_Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
```

**expected_result**

```
1. The TLM registers the press transition
2. VPLastStatus reads "OFF", TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req 之按下 → Idle`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-064 — SWE-PM-015（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-064`

**req_id**：`SWE-PM-015`

**split_index**：`2`

**tc_title**：`CLIMATIC_PANEL.Radio_Btn0 press with no active call passes the TLM to Idle`

**test_set**：`Power State`

**test_item**：`CLIMATIC_PANEL.Radio_Btn0 press with no active call passes the TLM to Idle`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Phone_Call.Info reads "Not_Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
```

**expected_result**

```
1. The TLM registers the press transition
2. VPLastStatus reads "OFF", TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 之按下 → Idle`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-016`（本 leaf 共 1 條）

**`source_anchor`**：`4941544`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI parameter Rear_View_Camera == "Present" AND Rear Camera becomes activeTHEN TLM has to stay in Full-Operation state and to manage rear view camera images on its screen, until Rear_Camera_Enable.Info passes to “False” again.
```

**`reasoning`**

> 驗證目標：Full-Operation 下後視攝影機啟動時之停留與影像管理。為什麼這樣切：本錨點為單一行為，不拆。

#### NR1L-PowerManagement-067 — SWE-PM-016（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-067`

**req_id**：`SWE-PM-016`

**split_index**：`1`

**tc_title**：`Rear camera activation keeps the TLM in Full-Operation`

**test_set**：`Power State`

**test_item**：`Rear camera activation keeps the TLM in Full-Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Rear_View_Camera reads "Present"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Make the Rear Camera become active
2. Read the TLM screen and Rear_Camera_Enable.Info to check that images are managed
```

**expected_result**

```
1. The TLM stays in Full-Operation state on the camera activation
2. The rear view camera images are managed on the TLM screen until Rear_Camera_Enable.Info passes to "False"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗後視攝影機啟動時之停留與影像管理`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-017`（本 leaf 共 1 條）

**`source_anchor`**：`4941545`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI parameter Rear_View_Camera == "Present" AND Rear Camera becomes inactive,THENTLM has to manage the last active source, that depends also on Audio_Data_Exchange.Info value and on Phone_Call.Info values, that could have changed their value while showing rvc images, and on priorities of the sources.
```

**`reasoning`**

> 驗證目標：後視攝影機關閉後之音源回復。為什麼這樣切：單一行為。刻意略過：`4941545` 所述之「priorities of the sources」未於本錨點定義其優先序，依 §8.4.1 不造值，ER 僅述其依 Audio_Data_Exchange.Info 與 Phone_Call.Info 決定。

#### NR1L-PowerManagement-068 — SWE-PM-017（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-068`

**req_id**：`SWE-PM-017`

**split_index**：`1`

**tc_title**：`Rear camera deactivation restores the last active source`

**test_set**：`Power State`

**test_item**：`Rear camera deactivation restores the last active source`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Rear_View_Camera reads "Present" and the Rear Camera is active
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Make the Rear Camera become inactive
2. Read the active source to check that the last active source is managed
```

**expected_result**

```
1. The TLM leaves the rear view camera images on the deactivation
2. The last active source is managed according to Audio_Data_Exchange.Info and Phone_Call.Info values
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗後視攝影機關閉後之音源回復`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-018`（本 leaf 共 1 條）

**`source_anchor`**：`4941548`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal LTM_OperationalModeSts has a transition to "Ignition Pre Off" OR to "Ignition Off" valueTHENTLM has to set TLM_Status.Info and $Telematic_Power$ to "Standby" value and then it passes to TLM Standby state.
```

**`reasoning`**

> 驗證目標：Idle 下點火轉為 Pre Off / Off 之 Standby 轉換。單一行為，不拆。

#### NR1L-PowerManagement-069 — SWE-PM-018（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-069`

**req_id**：`SWE-PM-018`

**split_index**：`1`

**tc_title**：`Ignition off in Idle passes the TLM to Standby`

**test_set**：`Power State`

**test_item**：`Ignition off in Idle passes the TLM to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
```

**input_test_data**

```
LTM_OperationalModeSts: "Ignition Off"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Idle ＋ 點火關閉 → Standby`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-019`（本 leaf 共 4 條）

**`source_anchor`**：`4941552,4941553,4941554,4941555,4941556,4941557`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHEN
IF PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info == True THEN TLM ignores this transition ELSE
TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has to set VPLastStatus to “ON” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and then it passes to TLM Full-Operation state.
IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” valueTHEN
IF PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info == True THEN TLM ignores this transition ELSE
TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has to set VPLastStatus to “ON” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and then it passes to TLM Full-Operation state.
```

**`reasoning`**

> 驗證目標：Idle 下二個開機鍵之按下，於後視攝影機啟用時被忽略、否則顯示 Splash Screen 並轉 Full-Operation。為什麼這樣切：二鍵為不同觸發（§5.7），其下 IF / ELSE 為兩個互斥分支，共四條。刻意略過：`4941554` 所引之「Splash Screen logo visualization」章節屬他 leaf，依 §8.2.1 本條僅驗其顯示與時長。

#### NR1L-PowerManagement-070 — SWE-PM-019（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-070`

**req_id**：`SWE-PM-019`

**split_index**：`1`

**tc_title**：`Front_Panel_OnOff.Req press is ignored while the rear camera is enabled`

**test_set**：`Power State`

**test_item**：`Front_Panel_OnOff.Req press is ignored while the rear camera is enabled`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read TLM_Status.Info and the screen to check that the transition is ignored
```

**expected_result**

```
1. The TLM receives the press transition
2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req 於後視攝影機啟用時被忽略`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-071 — SWE-PM-019（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-071`

**req_id**：`SWE-PM-019`

**split_index**：`2`

**tc_title**：`Front_Panel_OnOff.Req press otherwise shows the Splash Screen and enters Full-Operation`

**test_set**：`Power State`

**test_item**：`Front_Panel_OnOff.Req press otherwise shows the Splash Screen and enters Full-Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_Camera_Enable.Info reads "False"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read the screen, VPLastStatus and TLM_Status.Info to check the transition
```

**expected_result**

```
1. A Splash Screen is shown for Response_Wait_Time
2. VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req 之 ELSE 分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-072 — SWE-PM-019（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-072`

**req_id**：`SWE-PM-019`

**split_index**：`3`

**tc_title**：`CLIMATIC_PANEL.Radio_Btn0 press is ignored while the rear camera is enabled`

**test_set**：`Power State`

**test_item**：`CLIMATIC_PANEL.Radio_Btn0 press is ignored while the rear camera is enabled`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read TLM_Status.Info and the screen to check that the transition is ignored
```

**expected_result**

```
1. The TLM receives the press transition
2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 於後視攝影機啟用時被忽略`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-073 — SWE-PM-019（split_index 4，P0）

**tc_id**：`NR1L-PowerManagement-073`

**req_id**：`SWE-PM-019`

**split_index**：`4`

**tc_title**：`CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the Splash Screen and enters Full-Operation`

**test_set**：`Power State`

**test_item**：`CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the Splash Screen and enters Full-Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_Camera_Enable.Info reads "False"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read the screen, VPLastStatus and TLM_Status.Info to check the transition
```

**expected_result**

```
1. A Splash Screen is shown for Response_Wait_Time
2. VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 之 ELSE 分支`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-020`（本 leaf 共 3 條）

**`source_anchor`**：`4941558,4941559`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Phone_Call.Info has a transition from “Not_Active” value to “Active” valueTHENTLM has to set VPLastStatus  to “ON” value and TLM_Status.Info and $Telematic_Power$ to "Full-Operation" value and then it passes to TLM Full-Operation state.This condition does not apply to Calls made through Apple CarPlay on R1H in SR21.
Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in Phone Main Screen, TLM shall set TLM_Status.Info and $Telematic_Power$ to "Idle" again and then it passes to TLM Idle state.IF Phone_Call.Info turns back to "Not_Active" when another Screen is active on TLM_Display.GUI (due to user actions during the call), TLM shall stay in Full-Operation state.        Refer to TLM HMI document for further details about the screens visualization.
```

**`reasoning`**

> 驗證目標：Idle 下通話進入之 Full-Operation 轉換，及通話結束時依當前畫面之兩種去向。為什麼這樣切：進入與結束為兩個時點；結束後之去向依 TLM_Display.GUI 是否為 Phone Main Screen 分為兩個互斥分支，依 §8.2.2 拆為三條。刻意略過：`4941558` 明載「does not apply to Calls made through Apple CarPlay on R1H in SR21」，已置於 pre_condition。

#### NR1L-PowerManagement-074 — SWE-PM-020（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-074`

**req_id**：`SWE-PM-020`

**split_index**：`1`

**tc_title**：`Incoming call in Idle passes the TLM to Full-Operation`

**test_set**：`Power State`

**test_item**：`Incoming call in Idle passes the TLM to Full-Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. The call is not made through Apple CarPlay
```

**input_test_data**

```
Phone_Call.Info: "Not_Active" to "Active"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Idle ＋ 通話進入 → Full-Operation`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-075 — SWE-PM-020（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-075`

**req_id**：`SWE-PM-020`

**split_index**：`2`

**tc_title**：`Call ending on the Phone Main Screen returns the TLM to Idle`

**test_set**：`Power State`

**test_item**：`Call ending on the Phone Main Screen returns the TLM to Idle`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info reads "Full-Operation" entered through a call
3. TLM_Display.GUI is in Phone Main Screen
```

**input_test_data**

```
Phone_Call.Info: "Active" to "Not_Active"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the return to Idle
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗通話結束於 Phone Main Screen 之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-076 — SWE-PM-020（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-076`

**req_id**：`SWE-PM-020`

**split_index**：`3`

**tc_title**：`Call ending on another screen keeps the TLM in Full-Operation`

**test_set**：`Power State`

**test_item**：`Call ending on another screen keeps the TLM in Full-Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info reads "Full-Operation" entered through a call
3. TLM_Display.GUI is on a screen other than Phone Main Screen
```

**input_test_data**

```
Phone_Call.Info: "Active" to "Not_Active"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info to check that Full-Operation state is kept
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info still reads "Full-Operation" and the TLM stays in Full-Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗通話結束於其他畫面之分支`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-021`（本 leaf 共 1 條）

**`source_anchor`**：`4941560`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Idle" AND PROXI parameter Rear_View_Camera == "Present" AND Rear_Camera_Enable.Info passes from "False" to "True"THENTLM stays in Idle state but allows its screen only to show the rear view camera video on its screen.Refer to VF551 for details about video availability requirements on TLM screen state.
```

**`reasoning`**

> 驗證目標：Idle 下後視攝影機啟用時之停留與畫面限制。單一行為。刻意略過：`4941560` 所引之 VF551 為外部文件，依 §8.4.2 不測。

#### NR1L-PowerManagement-077 — SWE-PM-021（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-077`

**req_id**：`SWE-PM-021`

**split_index**：`1`

**tc_title**：`Rear camera enable in Idle keeps Idle with video only`

**test_set**：`Power State`

**test_item**：`Rear camera enable in Idle keeps Idle with video only`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present"
```

**input_test_data**

```
Rear_Camera_Enable.Info: "False" to "True"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and the screen content to check what the screen shows
```

**expected_result**

```
1. The TLM registers the transition without leaving Idle state
2. The screen shows the rear view camera video and nothing else
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Idle 下後視攝影機啟用之停留與畫面限制`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-022`（本 leaf 共 1 條）

**`source_anchor`**：`4941562`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation” || “Idle”AND signal PowerModeSts_Telematic passes from “Standard_Power” to “Logistic_Mode_On”, then TLM has to set TLM_Status.Info to "Logistic Idle" and $Telematic_Power$ to “Logistic_On” and then it passes to Logistic Idle state.
```

**`reasoning`**

> 驗證目標：物流模式進入時之狀態與訊號設定。單一行為。

#### NR1L-PowerManagement-078 — SWE-PM-022（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-078`

**req_id**：`SWE-PM-022`

**split_index**：`1`

**tc_title**：`Logistic mode on passes the TLM to Logistic Idle`

**test_set**：`Power State`

**test_item**：`Logistic mode on passes the TLM to Logistic Idle`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
```

**input_test_data**

```
PowerModeSts_Telematic: "Standard_Power" to "Logistic_Mode_On"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info reads "Logistic Idle", $Telematic_Power$ reads "Logistic_On" and the TLM passes to Logistic Idle state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗物流模式進入`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-023`（本 leaf 共 1 條）

**`source_anchor`**：`4941565`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal LTM_OperationalModeSts.Info has a transition from "Ignition Off" to another valueTHENTLM has to set VPLastStatus  to “On” value and to set TLM_Status.Info and $Telematic_Power$ to “Full-Operation” value and then it passes to TLM Full-Operation state.
```

**`reasoning`**

> 驗證目標：Timed 下離開 Ignition Off 之 Full-Operation 轉換。單一行為。

#### NR1L-PowerManagement-079 — SWE-PM-023（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-079`

**req_id**：`SWE-PM-023`

**split_index**：`1`

**tc_title**：`Leaving Ignition Off in Timed passes the TLM to Full-Operation`

**test_set**：`Power State`

**test_item**：`Leaving Ignition Off in Timed passes the TLM to Full-Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
```

**input_test_data**

```
LTM_OperationalModeSts.Info: from "Ignition Off" to another value
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. VPLastStatus reads "On", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Timed ＋ 離開 Ignition Off → Full-Operation`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-024`（本 leaf 共 1 條）

**`source_anchor`**：`4941566`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND STATUS_BH_BCM2.RemStActvSts == "Remote Start Not Active"AND signal LTM_OperationalModeSts.Info has a transition from "Ignition Off" to another valueTHENTLM has to set VPLastStatus  to “On” value and  RemStartFail to "False"AND TLM has to set TLM_Status.Info and $Telematic_Power$ to “Full-Operation” value and then it passes to TLM Full-Operation state.
```

**`reasoning`**

> 驗證目標：Timed 下 Remote Start Not Active 時離開 Ignition Off 之轉換與 RemStartFail 清除。單一行為。與 `SWE-PM-023` 之區別在於本條多一個 `STATUS_BH_BCM2.RemStActvSts` 前提與 `RemStartFail` 之設定。

#### NR1L-PowerManagement-080 — SWE-PM-024（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-080`

**req_id**：`SWE-PM-024`

**split_index**：`1`

**tc_title**：`Remote Start not active on leaving Ignition Off clears RemStartFail`

**test_set**：`Power State`

**test_item**：`Remote Start not active on leaving Ignition Off clears RemStartFail`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. STATUS_BH_BCM2.RemStActvSts reads "Remote Start Not Active"
```

**input_test_data**

```
LTM_OperationalModeSts.Info: from "Ignition Off" to another value
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read VPLastStatus, RemStartFail and TLM_Status.Info to check the resulting values
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. VPLastStatus reads "On", RemStartFail reads "False" and the TLM passes to TLM Full-Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Remote Start Not Active 下之 RemStartFail 清除`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-025`（本 leaf 共 8 條）

**`source_anchor`**：`4941569,4941570,4941571,4941572,4941573,4941574`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHENIF Phone_Call.Info == ActiveTHEN TLM shall show a popup to the user, asking whether to transfer the call in order to turn off TLM or not (refer to TLM HMI Specification)
In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.IF user does not accept, TLM shall stay in Timed state.
IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state, in order to respond quickly to user requests, without requiring the activation of the network (if it was already not active).
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” valueTHENIF Phone_Call.Info == ActiveTHEN TLM shall show a popup to the user, asking whether to transfer the call in order to turn off TLM or not (refer to TLM HMI Specification)
In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.IF user does not accept, TLM shall stay in Timed state.
IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state, in order to respond quickly to user requests, without requiring the activation of the network (if it was already not active).
```

**`reasoning`**

> 驗證目標：Timed 下二個關機鍵之按下，於通話中顯示轉接 popup 並依使用者回應分歧、於無通話時直接轉 Standby。為什麼這樣切：二鍵為不同觸發（§5.7）；其下「通話中→popup」「接受」「拒絕」「無通話」為四個獨立可觀察結果，依 §8.2.2 各拆一條，共八條。刻意略過：`4941569` 所引之 TLM HMI Specification 為外部文件（§8.4.2）。

#### NR1L-PowerManagement-081 — SWE-PM-025（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-081`

**req_id**：`SWE-PM-025`

**split_index**：`1`

**tc_title**：`Front_Panel_OnOff.Req press in Timed with an active call shows a popup`

**test_set**：`Power State`

**test_item**：`Front_Panel_OnOff.Req press in Timed with an active call shows a popup`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read the screen to check that the transfer popup is shown
```

**expected_result**

```
1. The TLM registers the press transition
2. A popup asking whether to transfer the call is shown to the user
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req ＋ 通話中之 popup`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-082 — SWE-PM-025（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-082`

**req_id**：`SWE-PM-025`

**split_index**：`2`

**tc_title**：`Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby`

**test_set**：`Power State`

**test_item**：`Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Accept the popup as the user
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**expected_result**

```
1. The TLM accepts the user answer
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req popup 之接受分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-083 — SWE-PM-025（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-083`

**req_id**：`SWE-PM-025`

**split_index**：`3`

**tc_title**：`Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed`

**test_set**：`Power State`

**test_item**：`Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Decline the popup as the user
2. Read TLM_Status.Info to check that Timed state is kept
```

**expected_result**

```
1. The TLM accepts the user answer
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req popup 之拒絕分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-084 — SWE-PM-025（split_index 4，P0）

**tc_id**：`NR1L-PowerManagement-084`

**req_id**：`SWE-PM-025`

**split_index**：`4`

**tc_title**：`Front_Panel_OnOff.Req press in Timed with no active call passes to Standby`

**test_set**：`Power State`

**test_item**：`Front_Panel_OnOff.Req press in Timed with no active call passes to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Not_Active"
4. A tuner source is currently active
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read the active functionality and TLM_Status.Info to check the transition to Standby
```

**expected_result**

```
1. The active functionality stops and no source stays active
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Front_Panel_OnOff.Req ＋ 無通話之直接轉換`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-085 — SWE-PM-025（split_index 5，P0）

**tc_id**：`NR1L-PowerManagement-085`

**req_id**：`SWE-PM-025`

**split_index**：`5`

**tc_title**：`CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active call shows a popup`

**test_set**：`Power State`

**test_item**：`CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active call shows a popup`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read the screen to check that the transfer popup is shown
```

**expected_result**

```
1. The TLM registers the press transition
2. A popup asking whether to transfer the call is shown to the user
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 通話中之 popup`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-086 — SWE-PM-025（split_index 6，P0）

**tc_id**：`NR1L-PowerManagement-086`

**req_id**：`SWE-PM-025`

**split_index**：`6`

**tc_title**：`Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby`

**test_set**：`Power State`

**test_item**：`Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Accept the popup as the user
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```

**expected_result**

```
1. The TLM accepts the user answer
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之接受分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-087 — SWE-PM-025（split_index 7，P0）

**tc_id**：`NR1L-PowerManagement-087`

**req_id**：`SWE-PM-025`

**split_index**：`7`

**tc_title**：`Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed`

**test_set**：`Power State`

**test_item**：`Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Decline the popup as the user
2. Read TLM_Status.Info to check that Timed state is kept
```

**expected_result**

```
1. The TLM accepts the user answer
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之拒絕分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-088 — SWE-PM-025（split_index 8，P0）

**tc_id**：`NR1L-PowerManagement-088`

**req_id**：`SWE-PM-025`

**split_index**：`8`

**tc_title**：`CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active call passes to Standby`

**test_set**：`Power State`

**test_item**：`CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active call passes to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Not_Active"
4. A tuner source is currently active
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read the active functionality and TLM_Status.Info to check the transition to Standby
```

**expected_result**

```
1. The active functionality stops and no source stays active
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 無通話之直接轉換`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-026`（本 leaf 共 3 條）

**`source_anchor`**：`4941575,4941576,4941577`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND proxi parameter Brand_Configuration_2 == "Jeep" AND
AND SWITCH_OFF_DOOR is equal to “enable”
AND (STATUS_BH_BCM1.DriverDoorSts passes to "Open" OR STATUS_BH_BCM1.PsngrDoorSts passes to "Open")
STATUS_BH_BCM1.DriverDoorSts passes to "Open"THEN
IF previous internal state TLM_Status.Info == "Full-Operation" AND PhoneCall.Info == "Not_Active"THEN TLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state
IF PhoneCall.Info == "Active"OR IF previous internal state TLM_Status.Info == StandbyTHEN TLM shall stay in Timed state.
```

**`reasoning`**

> 驗證目標：Jeep 且 SWITCH_OFF_DOOR 啟用時車門開啟之三種去向。為什麼這樣切：依前狀態與通話狀態分為三個互斥分支（前狀態 Full-Operation 且無通話 → Standby；通話中 → 留 Timed；前狀態 Standby → 留 Timed），依 §8.2.2 各拆一條。

#### NR1L-PowerManagement-089 — SWE-PM-026（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-089`

**req_id**：`SWE-PM-026`

**split_index**：`1`

**tc_title**：`Door open on a Jeep from Full-Operation passes the TLM to Standby`

**test_set**：`Power State`

**test_item**：`Door open on a Jeep from Full-Operation passes the TLM to Standby`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. The previous internal state was "Full-Operation" and PhoneCall.Info reads "Not_Active"
```

**input_test_data**

```
STATUS_BH_BCM1.DriverDoorSts = "Open"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read the active functionality and TLM_Status.Info to check the transition to Standby
```

**expected_result**

```
1. The active functionality stops and no source stays active
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Jeep 車門開啟 ＋ 前狀態 Full-Operation 之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-090 — SWE-PM-026（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-090`

**req_id**：`SWE-PM-026`

**split_index**：`2`

**tc_title**：`Door open with an active call keeps the TLM in Timed`

**test_set**：`Power State`

**test_item**：`Door open with an active call keeps the TLM in Timed`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. PhoneCall.Info reads "Active"
```

**input_test_data**

```
STATUS_BH_BCM1.PsngrDoorSts = "Open"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info to check that Timed state is kept
```

**expected_result**

```
1. The TLM registers the door signal without a bus error
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗通話中之門開啟分支`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-027`（本 leaf 共 2 條）

**`source_anchor`**：`4941579,4941642`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Activation.Req back to "False" value, showing proper HMI Antitheft screens if needed, for a maximum time equal to Timeout1.
IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Activation.Req back to "False" value and to stay in the original state (Partial Operation),  showing proper HMI Antitheft screens, if needed (see VF210).
```

**`reasoning`**

> 驗證目標：防盜失敗後之請求復歸與畫面時限，及其於 Partial Operation 下之停留。為什麼這樣切：`4941579` 與 `4941642` 為二個錨點，前者載最長 Timeout1 之畫面時限、後者載停留於原狀態（Partial Operation），二者之可觀察結果不同，各拆一條。

#### NR1L-PowerManagement-092 — SWE-PM-027（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-092`

**req_id**：`SWE-PM-027`

**split_index**：`1`

**tc_title**：`Antitheft failure clears the activation request within Timeout1`

**test_set**：`Power State`

**test_item**：`Antitheft failure clears the activation request within Timeout1`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**input_test_data**

```
Antitheft_Result.Info = "Not_Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req and the screen to check the reset and the screen time
```

**expected_result**

```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False" and the Antitheft screens are shown for a time not longer than Timeout1
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗防盜失敗後之請求復歸與畫面時限`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-093 — SWE-PM-027（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-093`

**req_id**：`SWE-PM-027`

**split_index**：`2`

**tc_title**：`Antitheft failure in Partial Operation keeps the original state`

**test_set**：`Power State`

**test_item**：`Antitheft failure in Partial Operation keeps the original state`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in Partial Operation
3. Antitheft_Activation.Req reads "True"
```

**input_test_data**

```
Antitheft_Result.Info = "Not_Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req and the TLM state to check that the state is kept
```

**expected_result**

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original state Partial Operation and the Antitheft screens are shown
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗防盜失敗於 Partial Operation 之停留`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-028`（本 leaf 共 4 條）

**`source_anchor`**：`4941580,4941581,4941582`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ", when  Timeout1 == 00 MIN" for LTM High Radio): THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

**`reasoning`**

> 驗證目標：防盜成功後之請求復歸、Timeout1 之暫時取值與其復歸、以及狀態轉換。為什麼這樣切：三者為獨立部分失效，依 §8.2.2 各拆一條。

#### NR1L-PowerManagement-094 — SWE-PM-028（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-094`

**req_id**：`SWE-PM-028`

**split_index**：`1`

**tc_title**：`Antitheft success clears the activation request`

**test_set**：`Power State`

**test_item**：`Antitheft success clears the activation request`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req to check that it is set back
```

**expected_result**

```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗防盜成功後之請求復歸`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-095 — SWE-PM-028（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-095`

**req_id**：`SWE-PM-028`

**split_index**：`2`

**tc_title**：`Antitheft success with a zero timeout takes Timeout1 from PROXI`

**test_set**：`Power State`

**test_item**：`Antitheft success with a zero timeout takes Timeout1 from PROXI`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. Switch_Off_Time reads 20 minutes
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**expected_result**

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Timeout1 之暫時取值與其復歸`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-096 — SWE-PM-028（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-096`

**req_id**：`SWE-PM-028`

**split_index**：`3`

**tc_title**：`Antitheft success passes the TLM to Timed state`

**test_set**：`Power State`

**test_item**：`Antitheft success passes the TLM to Timed state`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```

**expected_result**

```
1. The TLM accepts the signal without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM passes to TLM Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗防盜成功後之狀態轉換`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-097 — SWE-PM-028（split_index 4，P0）

**tc_id**：`NR1L-PowerManagement-097`

**req_id**：`SWE-PM-028`

**split_index**：`4`

**tc_title**：`Antitheft success on LTM High takes Timeout1 from PROXI`

**test_set**：`Power State`

**test_item**：`Antitheft success on LTM High takes Timeout1 from PROXI`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"
4. Switch_Off_Time reads 20 minutes
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**expected_result**

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 LTM High 形態之 Timeout1 取值（`100` 之對應條驗 SwitchOff_Timeout_Setting.Req 形態）`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### leaf `SWE-PM-029`（本 leaf 共 4 條）

**`source_anchor`**：`4941586,4941587,4941588,4941589`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activation.Req back to "False" value and following logic must be guaranteed:
IF SwitchOff_Timeout_Setting.Req == 00 min  THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (for example 20 minutes if Switch_Off_Time == 20 minutes), only for this case,  restoring it to "00 minutes" at next Ignition On event.
IF SwitchOff_Timeout_Setting.Req == 00 min  THEN TLM has to set Timeout1 to the value specified by $PwrAccDelayAct$ (for example 10  minutes if $PwrAccDelayAct$ == 10 minutes), only for this case,  restoring it to "00 minutes" at next Ignition  On event.
AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to TLM Timed state.
```

**`reasoning`**

> 驗證目標：同 `SWE-PM-028` 之防盜成功邏輯，惟本 leaf 之 Timeout1 取值另有 `$PwrAccDelayAct$` 一支。為什麼這樣切：`4941587`（取自 `Switch_Off_Time`）與 `4941588`（取自 `$PwrAccDelayAct$`）為二個不同來源，各拆一條；請求復歸與狀態轉換另各一條。

#### NR1L-PowerManagement-098 — SWE-PM-029（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-098`

**req_id**：`SWE-PM-029`

**split_index**：`1`

**tc_title**：`Antitheft success clears the activation request on this variant`

**test_set**：`Power State`

**test_item**：`Antitheft success clears the activation request on this variant`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req to check that it is set back
```

**expected_result**

```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗本變體之請求復歸`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-099 — SWE-PM-029（split_index 2，P0）

**tc_id**：`NR1L-PowerManagement-099`

**req_id**：`SWE-PM-029`

**split_index**：`2`

**tc_title**：`Timeout1 follows Switch_Off_Time when the setting is zero`

**test_set**：`Power State`

**test_item**：`Timeout1 follows Switch_Off_Time when the setting is zero`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. Switch_Off_Time reads 20 minutes
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**expected_result**

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Timeout1 取自 Switch_Off_Time 之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-100 — SWE-PM-029（split_index 3，P0）

**tc_id**：`NR1L-PowerManagement-100`

**req_id**：`SWE-PM-029`

**split_index**：`3`

**tc_title**：`Timeout1 follows PwrAccDelayAct when the setting is zero`

**test_set**：`Power State`

**test_item**：`Timeout1 follows PwrAccDelayAct when the setting is zero`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. $PwrAccDelayAct$ reads 10 minutes
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```

**expected_result**

```
1. Timeout1 reads 10 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Timeout1 取自 $PwrAccDelayAct$ 之分支`

**functional_safety**：`NA`

**remarks**：``

#### NR1L-PowerManagement-101 — SWE-PM-029（split_index 4，P0）

**tc_id**：`NR1L-PowerManagement-101`

**req_id**：`SWE-PM-029`

**split_index**：`4`

**tc_title**：`Antitheft success on this variant passes the TLM to Timed`

**test_set**：`Power State`

**test_item**：`Antitheft success on this variant passes the TLM to Timed`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**input_test_data**

```
Antitheft_Result.Info = "Successfully"
```

**test_procedure**

```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```

**expected_result**

```
1. The TLM accepts the signal without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM passes to TLM Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗本變體之狀態轉換`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-030`（本 leaf 共 1 條）

**`source_anchor`**：`4941600`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF Auto_SwitchOn_Setting.Req == Active OR IF Auto_SwitchOn_Setting.Req == Recall_Last AND VPLastStatus == OnTHEN TLM has to show a proper Splash Screen, depending on par. "Splash Screen logo visualization" logics, for Response_Wait_Time.
```

**`reasoning`**

> 驗證目標：Auto_SwitchOn_Setting.Req 條件成立時之 Splash Screen 顯示與時長。單一行為。刻意略過：所引之「Splash Screen logo visualization」章節屬他 leaf（§8.2.1）。

#### NR1L-PowerManagement-102 — SWE-PM-030（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-102`

**req_id**：`SWE-PM-030`

**split_index**：`1`

**tc_title**：`Splash Screen is shown for the configured wait time`

**test_set**：`Power State`

**test_item**：`Splash Screen is shown for the configured wait time`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Bring the TLM through the switch on sequence
2. Read the screen and its duration to check the Splash Screen presentation
```

**expected_result**

```
1. A proper Splash Screen is shown on the TLM screen
2. The Splash Screen stays for Response_Wait_Time
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Auto_SwitchOn_Setting.Req 為 Active 時之 Splash Screen`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-031`（本 leaf 共 1 條）

**`source_anchor`**：`4941615`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF Rear_View_Camera PROXI parameter == "Present", according to the value of Rear_Camera_Enable.Info, TLM shall show or not rear view camera images regardless of TLM_Status.Info and $Telematic_Power$ value.
```

**`reasoning`**

> 驗證目標：後視影像之顯示與 TLM_Status.Info 無關。單一行為，以「訊號 False 與 True 兩段」於同一條內對照，因其為同一行為之兩個取值而非兩個行為。

#### NR1L-PowerManagement-103 — SWE-PM-031（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-103`

**req_id**：`SWE-PM-031`

**split_index**：`1`

**tc_title**：`Rear view camera images follow the enable signal in any state`

**test_set**：`Power State`

**test_item**：`Rear view camera images follow the enable signal in any state`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. Rear_View_Camera reads "Present"
3. The TLM is in Standby state
```

**input_test_data**

```
Rear_Camera_Enable.Info: "False" then "True"
```

**test_procedure**

```
1. Send the two values listed in Input Test Data in turn
2. Read the screen against TLM_Status.Info to check that images follow the signal only
```

**expected_result**

```
1. No rear view camera images are shown while the signal reads "False"
2. The rear view camera images are shown while the signal reads "True" regardless of TLM_Status.Info
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗後視影像之顯示與狀態無關`

**functional_safety**：`NA`

**remarks**：``

### leaf `SWE-PM-032`（本 leaf 共 1 條）

**`source_anchor`**：`4941630`　**章節**：1.6.2.1.15

**`source_clause`**（G94 逐字相符、G99 / G103 皆相等）

```
IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND STATUS_BH_BCM2.RemStActvSts has a transition from “Remote Start Not Active” value to “Remote Start Active” valueTHENTLM has to set TLM_Status.Info and $Telematic_Power$ to "Partial Operation" value and it passes to TLM Partial Operation state.
```

**`reasoning`**

> 驗證目標：Standby 或 Sleep 下 Remote Start 啟動之 Partial Operation 轉換。單一行為。

#### NR1L-PowerManagement-104 — SWE-PM-032（split_index 1，P0）

**tc_id**：`NR1L-PowerManagement-104`

**req_id**：`SWE-PM-032`

**split_index**：`1`

**tc_title**：`Remote Start from Standby passes the TLM to Partial Operation`

**test_set**：`Power State`

**test_item**：`Remote Start from Standby passes the TLM to Partial Operation`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
```

**input_test_data**

```
STATUS_BH_BCM2.RemStActvSts: "Remote Start Not Active" to "Remote Start Active"
```

**test_procedure**

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition
```

**expected_result**

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Partial Operation" and the TLM passes to TLM Partial Operation state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Standby ＋ Remote Start → Partial Operation`

**functional_safety**：`NA`

**remarks**：``

---

## 六、第三批之反向涵蓋（G112）

## 現況（batch_003_power_state_a.json，61 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-011 —— 行為項 10，已覆蓋 6，無對應 **4**

TC：044, 045, 046, 047, 048, 049

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | While the HU is in IDLE mode, the HU shall transition to Full-Operation mode i | 044 | 0.88 | 已覆蓋 | `press` |
| 2 | Refer to CFTS042 for VR button press definition | 044 | 0.50 | 已覆蓋 | `cfts042`、`definition`、`refer` |
| 3 | The VR button press defined in CFTS009-2326 refers to both short and long pres | 044 | 0.44 | **無對應** | `cfts009-2326`、`defin`、`long`、`press`、`refer` |
| 4 | If CarPlay VR was activated by the button press defined in CFTS009-2326, then  | 046 | 0.30 | **無對應** | `accessory`、`apple`、`button`、`cfts009-2326`、`cfts009-2329`、`command`、`complete`、`defin`、`depend`、`different`、`interface`、`issu`、`once`、`pres`、`siri`、`specification` |
| 5 | If the CarPlay Device requests audio control and video control, then the HU sh | 045 | 0.93 | 已覆蓋 | `remain` |
| 6 | If the Carplay device requests audio control and does not request video contro | 046 | 0.82 | 已覆蓋 | `doe`、`remain`、`video` |
| 7 | See CFTS020 for Screen Off definition | 046 | 0.40 | **無對應** | `cfts020`、`definition`、`see` |
| 8 | If the Carplay device does not request audio control and does request video co | 047 | 0.86 | 已覆蓋 | `doe`、`remain` |
| 9 | See CFTS020 for Screen On definition | 045 | 0.25 | **無對應** | `cfts020`、`definition`、`see` |
| 10 | If the CarPlay Device does not request audio control or video control, then th | 048 | 0.91 | 已覆蓋 | `doe` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`2326`、`2329`

**R-P127 殘差詞分桶**（合計 38）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **4** | `long`(#3)、`button`(#4)、`pres`(#4)、`video`(#6) |
| 候選（須人工判 措詞差異 / 真缺口） | **34** | `press`(#1)、`cfts042`(#2)、`definition`(#2)、`refer`(#2)、`cfts009-2326`(#3)、`defin`(#3)、`press`(#3)、`refer`(#3)、`accessory`(#4)、`apple`(#4)、`cfts009-2326`(#4)、`cfts009-2329`(#4) |

### SWE-PM-012 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：050, 051

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | After a battery reconnection and also when TLM has to exit INIT state (as soon | 050 | 0.57 | 已覆蓋 | `able`、`accord`、`also`、`behave`、`certain`、`exit`、`last`、`limit`、`par`、`properly`、`requirement`、`reset`、`restore`、`soon`、`work` |
| 2 | "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Inf | 051 | 0.50 | 已覆蓋 | `first`、`sett`、`signal`、`telematic_power$` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`Telematic_Power`

**R-P127 殘差詞分桶**（合計 19）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `exit`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `able`(#1)、`accord`(#1)、`also`(#1)、`behave`(#1)、`certain`(#1)、`last`(#1)、`limit`(#1)、`par`(#1)、`properly`(#1)、`requirement`(#1)、`reset`(#1)、`restore`(#1) |

### SWE-PM-013 —— 行為項 4，已覆蓋 3，無對應 **1**

TC：052, 053, 054

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Star | 052 | 0.56 | 已覆蓋 | `crank`、`engine`、`follow`、`off`、`pre-off`、`pre_start`、`thi` |
| 2 | This mode shall exist for AMP, ICS, and DTV when STATUS_BH_BCM2.RemStActvSts i | 052 | 0.47 | 已覆蓋 | `amp`、`dtv`、`equal`、`exist`、`ics`、`off`、`reciev`、`relat`、`statu`、`thi` |
| 3 | AMP/ICS/DTV shall be OFF | 053 | 1.00 | 已覆蓋 | （無） |
| 4 | Audio for ANC, ACN, and chimes (if equipped) shall be active in this state) Al | 053 | 0.40 | **無對應** | `background`、`but`、`change`、`enabl`、`except`、`functionaliti`、`hmi`、`interaction`、`permit`、`ready`、`run`、`state`、`statu`、`thi`、`within` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`Pre_Start`、`TLM OFF`

**R-P127 殘差詞分桶**（合計 32）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **14** | `off`(#1)、`amp`(#2)、`dtv`(#2)、`ics`(#2)、`off`(#2)、`statu`(#2)、`background`(#4)、`change`(#4)、`except`(#4)、`functionaliti`(#4)、`hmi`(#4)、`interaction`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `crank`(#1)、`engine`(#1)、`follow`(#1)、`pre-off`(#1)、`pre_start`(#1)、`thi`(#1)、`equal`(#2)、`exist`(#2)、`reciev`(#2)、`relat`(#2)、`thi`(#2)、`but`(#4) |

### SWE-PM-014 —— 行為項 14，已覆蓋 9，無對應 **5**

TC：055, 056, 057, 058, 059, 060, 061, 062

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM | 055 | 0.52 | 已覆蓋 | `case`、`equal`、`false`、`pass`、`phone_call.info`、`pre`、`standby`、`state`、`state.if`、`state.in`、`stay`、`thi`、`tim`、`value` |
| 2 | until Phone_Call.Info becomes equal to "Not_Active", OR at maximum | 058 | 0.60 | 已覆蓋 | `equal`、`maximum` |
| 3 | until MaxCallTimeout expiration | — | 0.00 | **無對應** | `expiration`、`maxcalltimeout` |
| 4 | “Phone call management in Timed state” .ELSE IF LTM_OperationalModeSts.Info is | 055 | 0.34 | **無對應** | `behaviour`、`call`、`different`、`else`、`equal`、`false`、`full`、`management`、`menu`、`min`、`operation`、`original`、`phone`、`possible`、`pre`、`selectable`、`sett`、`signal`、`state`、`stay`、`switchoff_timeout_setting.req`、`thenaccord`、`tim`、`time`、`timeout1`、`two`、`valueand` |
| 5 | If Auto_SwitchOn_Setting.Req =="Active", when Timeout1 == 00 MIN" for LTM High | 061 | 1.00 | 已覆蓋 | （無） |
| 6 | If Phone_Call.Info == Not_Active, at LTM_OperationalModeSts.Info transition TL | 057 | 0.83 | 已覆蓋 | `set`、`value` |
| 7 | If Phone_Call.Info == Active, at LTM_OperationalModeSts.Info transition TLM se | 057 | 0.75 | 已覆蓋 | `set`、`tim`、`value` |
| 8 | In this case, TLM has to stay in this state | 056 | 0.40 | **無對應** | `case`、`stay`、`thi` |
| 9 | until Phone_Call.Info becomes equal to "Not_Active", OR at maximum | 058 | 0.60 | 已覆蓋 | `equal`、`maximum` |
| 10 | until MaxCallTimeout expiration | — | 0.00 | **無對應** | `expiration`、`maxcalltimeout` |
| 11 | “Phone call management in Timed state” | 056 | 0.40 | **無對應** | `management`、`phone`、`tim` |
| 12 | Behaviour 2: "SwitchOff_Timeout_Setting.Req == Timeout1 <> 00 MIN" or ( | 057 | 1.00 | 已覆蓋 | （無） |
| 13 | If Auto_SwitchOn_Setting.Req =="Not_Active ", when Timeout1 <> 00 MIN" for LTM | 059 | 0.77 | 已覆蓋 | `auto_switchon_setting.req`、`high`、`ltm`、`radio`、`set` |
| 14 | ELSE at LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $ | 060 | 0.73 | 已覆蓋 | `else`、`mantain`、`set`、`state` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`ELSE`、`ELSE IF`、`IF`、`OR`、`THEN IF`、`THEN TLM`、`state.IF`、`state.In`

**R-P127 殘差詞分桶**（合計 69）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **32** | `false`(#1)、`pass`(#1)、`phone_call.info`(#1)、`standby`(#1)、`state`(#1)、`stay`(#1)、`tim`(#1)、`value`(#1)、`behaviour`(#4)、`call`(#4)、`false`(#4)、`min`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **37** | `case`(#1)、`equal`(#1)、`pre`(#1)、`state.if`(#1)、`state.in`(#1)、`thi`(#1)、`equal`(#2)、`maximum`(#2)、`expiration`(#3)、`maxcalltimeout`(#3)、`different`(#4)、`else`(#4) |

### SWE-PM-015 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：063, 064, 065, 066

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_P | 063 | 0.79 | 已覆蓋 | `set`、`signal`、`value`、`valuethen` |
| 2 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATI | 064 | 0.79 | 已覆蓋 | `set`、`signal`、`value`、`valuethen` |
| 3 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_P | 065 | 0.74 | 已覆蓋 | `parameter`、`provid`、`proxi`、`set`、`signal`、`value`、`valuethen` |
| 4 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATI | 066 | 0.74 | 已覆蓋 | `parameter`、`provid`、`proxi`、`set`、`signal`、`value`、`valuethen` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 22）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **22** | `set`(#1)、`signal`(#1)、`value`(#1)、`valuethen`(#1)、`set`(#2)、`signal`(#2)、`value`(#2)、`valuethen`(#2)、`parameter`(#3)、`provid`(#3)、`proxi`(#3)、`set`(#3) |

### SWE-PM-016 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：067

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI paramete | 067 | 0.72 | 已覆蓋 | `activethen`、`becom`、`manage`、`parameter`、`proxi` |
| 2 | until Rear_Camera_Enable.Info passes to “False” again | 067 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND PROXI`、`IF`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `activethen`(#1)、`becom`(#1)、`manage`(#1)、`parameter`(#1)、`proxi`(#1) |

### SWE-PM-017 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：068

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI paramete | 068 | 0.50 | 已覆蓋 | `also`、`becom`、`chang`、`could`、`depend`、`manage`、`parameter`、`prioriti`、`proxi`、`rvc`、`show`、`sourc`、`their`、`thentlm`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND PROXI`、`IF`、`THENTLM`

**R-P127 殘差詞分桶**（合計 15）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **15** | `also`(#1)、`becom`(#1)、`chang`(#1)、`could`(#1)、`depend`(#1)、`manage`(#1)、`parameter`(#1)、`prioriti`(#1)、`proxi`(#1)、`rvc`(#1)、`show`(#1)、`sourc`(#1) |

### SWE-PM-018 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：069

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal LTM_OperationalMo | 069 | 0.69 | 已覆蓋 | `pre`、`set`、`signal`、`value`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `pre`(#1)、`set`(#1)、`signal`(#1)、`value`(#1)、`valuethentlm`(#1) |

### SWE-PM-019 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：070, 071, 072, 073

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Front_Panel_OnOff | 070 | 0.58 | 已覆蓋 | `depend`、`else`、`par`、`parameter`、`proper`、`proxi`、`show`、`signal`、`thi`、`value`、`valuethen` |
| 2 | "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has  | 071 | 0.67 | 已覆蓋 | `logic`、`logo`、`set`、`value`、`visualization` |
| 3 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal CLIMATIC_PANEL.Ra | 072 | 0.58 | 已覆蓋 | `depend`、`else`、`par`、`parameter`、`proper`、`proxi`、`show`、`signal`、`thi`、`value`、`valuethen` |
| 4 | "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has  | 071 | 0.67 | 已覆蓋 | `logic`、`logo`、`set`、`value`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`ELSE
TLM`、`IF`、`IF PROXI`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 32）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `show`(#1)、`show`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **30** | `depend`(#1)、`else`(#1)、`par`(#1)、`parameter`(#1)、`proper`(#1)、`proxi`(#1)、`signal`(#1)、`thi`(#1)、`value`(#1)、`valuethen`(#1)、`logic`(#2)、`logo`(#2) |

### SWE-PM-020 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：074, 075, 076

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Phone_Call.Info h | 074 | 0.61 | 已覆蓋 | `apply`、`condition`、`doe`、`r1h`、`set`、`signal`、`sr21`、`state.thi`、`value`、`valuethentlm` |
| 2 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in | 075 | 0.60 | 已覆蓋 | `action`、`another`、`back`、`due`、`dur`、`set`、`state.if`、`stay`、`turn`、`user` |
| 3 | Refer to TLM HMI document for further details about the screens visualization | 075 | 0.22 | **無對應** | `about`、`detail`、`document`、`further`、`hmi`、`refer`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`TLM HMI`、`state.IF`、`state.This`

**R-P127 殘差詞分桶**（合計 27）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `another`(#2)、`stay`(#2) |
| 候選（須人工判 措詞差異 / 真缺口） | **25** | `apply`(#1)、`condition`(#1)、`doe`(#1)、`r1h`(#1)、`set`(#1)、`signal`(#1)、`sr21`(#1)、`state.thi`(#1)、`value`(#1)、`valuethentlm`(#1)、`action`(#2)、`back`(#2) |

### SWE-PM-021 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：077

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle" AND PROXI parameter Rear_Vi | 077 | 0.57 | 已覆蓋 | `about`、`allow`、`availability`、`but`、`detail`、`parameter`、`pass`、`proxi`、`requirement`、`screen.refer`、`stay`、`thentlm`、`vf551` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND PROXI`、`IF`、`THENTLM`、`screen.Refer`

**R-P127 殘差詞分桶**（合計 13）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **13** | `about`(#1)、`allow`(#1)、`availability`(#1)、`but`(#1)、`detail`(#1)、`parameter`(#1)、`pass`(#1)、`proxi`(#1)、`requirement`(#1)、`screen.refer`(#1)、`stay`(#1)、`thentlm`(#1) |

### SWE-PM-022 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：078

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation” || “Idle”AND sign | 078 | 0.86 | 已覆蓋 | `set`、`signal` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `set`(#1)、`signal`(#1) |

### SWE-PM-023 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：079

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal LTM_OperationalM | 079 | 0.82 | 已覆蓋 | `set`、`signal`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `set`(#1)、`signal`(#1)、`valuethentlm`(#1) |

### SWE-PM-024 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：080

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND STATUS_BH_BCM2.RemStAct | 080 | 0.87 | 已覆蓋 | `set`、`signal`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`IF`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `set`(#1)、`signal`(#1)、`valuethentlm`(#1) |

### SWE-PM-025 —— 行為項 4，已覆蓋 2，無對應 **2**

TC：081, 082, 083, 084, 085, 086, 087, 088

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND Front_Panel_OnOff.Req h | 081 | 0.46 | 已覆蓋 | `accept`、`activethen`、`case`、`doe`、`hmi`、`off`、`order`、`pass`、`refer`、`set`、`specification`、`standby`、`state`、`state.if`、`stay`、`thi`、`turn`、`value`、`valuethenif` |
| 2 | IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Medi | 084 | 0.37 | **無對應** | `activation`、`already`、`audio`、`etc`、`media`、`network`、`not_activetlm`、`order`、`quickly`、`request`、`requir`、`respond`、`set`、`stream`、`user`、`value`、`without` |
| 3 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND CLIMATIC_PANEL.Radio_Bt | 085 | 0.46 | 已覆蓋 | `accept`、`activethen`、`case`、`doe`、`hmi`、`off`、`order`、`pass`、`refer`、`set`、`specification`、`standby`、`state`、`state.if`、`stay`、`thi`、`turn`、`value`、`valuethenif` |
| 4 | IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Medi | 084 | 0.37 | **無對應** | `activation`、`already`、`audio`、`etc`、`media`、`network`、`not_activetlm`、`order`、`quickly`、`request`、`requir`、`respond`、`set`、`stream`、`user`、`value`、`without` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`Not_ActiveTLM`、`TLM HMI`、`state.IF`

**R-P127 殘差詞分桶**（合計 72）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **12** | `accept`(#1)、`pass`(#1)、`standby`(#1)、`state`(#1)、`stay`(#1)、`user`(#2)、`accept`(#3)、`pass`(#3)、`standby`(#3)、`state`(#3)、`stay`(#3)、`user`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **60** | `activethen`(#1)、`case`(#1)、`doe`(#1)、`hmi`(#1)、`off`(#1)、`order`(#1)、`refer`(#1)、`set`(#1)、`specification`(#1)、`state.if`(#1)、`thi`(#1)、`turn`(#1) |

### SWE-PM-026 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：089, 090, 091

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND proxi parameter Brand_C | 089 | 0.65 | 已覆蓋 | `audio`、`equal`、`etc`、`media`、`parameter`、`proxi`、`set`、`standbythen`、`status_bh_bcm1.psngrdoorst`、`stream`、`tuner`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND
AND`、`IF`、`OR`、`OR IF`、`THEN
IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 12）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `status_bh_bcm1.psngrdoorst`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **11** | `audio`(#1)、`equal`(#1)、`etc`(#1)、`media`(#1)、`parameter`(#1)、`proxi`(#1)、`set`(#1)、`standbythen`(#1)、`stream`(#1)、`tuner`(#1)、`value`(#1) |

### SWE-PM-027 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：092, 093

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 092 | 0.50 | 已覆蓋 | `back`、`equal`、`hmi`、`maximum`、`need`、`proper`、`set`、`show`、`value` |
| 2 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 093 | 0.57 | 已覆蓋 | `back`、`hmi`、`need`、`proper`、`see`、`set`、`show`、`value`、`vf210` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 18）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `back`(#1)、`equal`(#1)、`hmi`(#1)、`maximum`(#1)、`need`(#1)、`proper`(#1)、`set`(#1)、`show`(#1)、`value`(#1)、`back`(#2)、`hmi`(#2)、`need`(#2) |

### SWE-PM-028 —— 行為項 3，已覆蓋 3，無對應 **0**

TC：094, 095, 096, 097

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activ | 094 | 0.54 | 已覆蓋 | `follow`、`guarante`、`logic`、`min`、`switchoff_timeout_setting.req`、`value` |
| 2 | If Auto_SwitchOn_Setting.Req =="Active ", when Timeout1 == 00 MIN" for LTM Hig | 097 | 0.56 | 已覆蓋 | `case`、`example`、`only`、`parameter`、`restor`、`set`、`specifi`、`thentlm`、`thi`、`value` |
| 3 | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and  | 096 | 0.75 | 已覆蓋 | `set`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND TLM`、`IF`、`THEN TLM`、`THENTLM`

**R-P127 殘差詞分桶**（合計 18）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **4** | `min`(#1)、`switchoff_timeout_setting.req`(#1)、`set`(#2)、`set`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **14** | `follow`(#1)、`guarante`(#1)、`logic`(#1)、`value`(#1)、`case`(#2)、`example`(#2)、`only`(#2)、`parameter`(#2)、`restor`(#2)、`specifi`(#2)、`thentlm`(#2)、`thi`(#2) |

### SWE-PM-029 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：098, 099, 100, 101

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activ | 099 | 0.39 | **無對應** | `antitheft_activation.req`、`back`、`case`、`example`、`false`、`guarante`、`logic`、`only`、`parameter`、`proxi`、`restor`、`set`、`specifi`、`thentlm`、`thi`、`tlm`、`value` |
| 2 | IF SwitchOff_Timeout_Setting.Req == 00 min THEN TLM has to set Timeout1 to the | 100 | 0.47 | 已覆蓋 | `case`、`example`、`only`、`restor`、`set`、`specifi`、`thi`、`tlm`、`value` |
| 3 | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and  | 101 | 0.75 | 已覆蓋 | `set`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND TLM`、`IF`、`PROXI`、`THEN TLM`、`THENTLM`

**R-P127 殘差詞分桶**（合計 28）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **10** | `antitheft_activation.req`(#1)、`back`(#1)、`false`(#1)、`set`(#1)、`thi`(#1)、`tlm`(#1)、`set`(#2)、`thi`(#2)、`tlm`(#2)、`set`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `case`(#1)、`example`(#1)、`guarante`(#1)、`logic`(#1)、`only`(#1)、`parameter`(#1)、`proxi`(#1)、`restor`(#1)、`specifi`(#1)、`thentlm`(#1)、`value`(#1)、`case`(#2) |

### SWE-PM-030 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：102

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Auto_SwitchOn_Setting.Req == Active OR IF Auto_SwitchOn_Setting.Req == Reca | 102 | 0.50 | 已覆蓋 | `depend`、`onthen`、`par`、`recall_last`、`show`、`vplaststatu` |
| 2 | "Splash Screen logo visualization" logics, for Response_Wait_Time | 102 | 0.50 | 已覆蓋 | `logic`、`logo`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR IF`、`Recall_Last`

**R-P127 殘差詞分桶**（合計 9）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **9** | `depend`(#1)、`onthen`(#1)、`par`(#1)、`recall_last`(#1)、`show`(#1)、`vplaststatu`(#1)、`logic`(#2)、`logo`(#2)、`visualization`(#2) |

### SWE-PM-031 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：103

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Rear_View_Camera PROXI parameter == "Present", according to the value of Re | 103 | 0.62 | 已覆蓋 | `accord`、`parameter`、`proxi`、`show`、`telematic_power$`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`PROXI`、`Telematic_Power`

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `accord`(#1)、`parameter`(#1)、`proxi`(#1)、`show`(#1)、`telematic_power$`(#1)、`value`(#1) |

### SWE-PM-032 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：104

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND STATUS_BH_ | 104 | 0.77 | 已覆蓋 | `set`、`sleep`、`value`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR`

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `set`(#1)、`sleep`(#1)、`value`(#1)、`valuethentlm`(#1) |

**合計**：行為項 **66**，已覆蓋 **52**，無對應 **14**。

### 6.1 無對應項之裁決（R-P118(d)，沉默不算裁決）

| leaf | 項 | 裁決 | 依據 |
|---|---|---|---|
| `011` #3 | `The VR button press … refers to both short and long presses` | **已由他條涵蓋** | 該項為**定義性陳述**；其可測面（短按、長按）由 `044` 與新補之長按條承擔 |
| `011` #4 / #7 / #9 | Apple Accessory Interface Specification / CFTS020 之引用 | **範圍外** | 外部文件，依 §8.4.2 不測本 spec 未擁有者 |
| `013` #4 | `Audio for ANC, ACN, and chimes … shall be active` | **已由他條涵蓋** | 該 leaf 之 AMP/ICS/DTV 條之 ER 逐字含之 |
| `014` #3 / #10 | `until MaxCallTimeout expiration` | **已由他 leaf 涵蓋** | `4941508` 明指「Phone call management in Timed state」節，屬 `SWE-PM-038` / `065`（§8.2.1）|
| `014` #4 / #11 | 同上之節引用 | **已由他 leaf 涵蓋** | 同上 |
| `014` #8 | `In this case, TLM has to stay in this state` | **已由他條涵蓋** | 該 leaf 之 Behaviour 1 通話中條 |
| `020` #3 | `Refer to TLM HMI document …` | **範圍外** | 外部文件（§8.4.2）|
| `025` #2 / #4 | `IF Phone_Call.Info == Not_Active TLM has to stop its active functionality …` | **已由他條涵蓋** | 該 leaf 之「無通話 → Standby」二條，overlap 低係措詞差異 |
| `029` #1 | `IF Antitheft_Result.Info == "Successfully" THEN …` | **已由他條涵蓋** | 該 leaf 之請求復歸條 |

### 6.2 R-P128 盲測 —— **抓出 4 項事前未知之缺口**

第三批之 61 條係逐 leaf 依錨點原文直接撰寫，**撰寫時未跑反向涵蓋**。

| # | 缺口 | 原文 | 透鏡 1 之判定 |
|---|---|---|---|
| 1 | `SWE-PM-011` VR **長按**未測 | `refers to both short and long presses` | 無對應（0.44）|
| 2 | `SWE-PM-014` Behaviour 1 之 **LTM High 形態**未測 | `or ( If Auto_SwitchOn_Setting.Req =="Active", when Timeout1 == 00 MIN" for LTM High Radio)` | 無對應（0.43）|
| 3 | `SWE-PM-014` Behaviour 2 之 LTM High 形態未測 | 同上之對應句 | 同上 |
| 4 | `SWE-PM-028` 之 LTM High 形態未測 | `or ( If Auto_SwitchOn_Setting.Req =="Active ", when Timeout1 == 00 MIN" for LTM High Radio)` | 無對應（0.35）|

> **四者皆為「原文以 OR 並列而 TC 只取其一」** ——
> 與 A-PW94（`Ignition Pre Off`）、A-PW87（`greater` 負分支）、
> R-P117(c)（`BODY OFF-TIMED`）**同型之第四至七例**（A-PW119）。
> **該形態已重複七次，而至今無任何閘門可攔。**

已依 R-P118(d) 裁為真缺口並補四條（TC 57 → **61**）。

### 6.3 R-P127 分桶與信噪比

| 桶 | 計數 |
|---|---|
| `已由他條涵蓋`（機械可判）| **82** |
| `候選（須人工判）` | **370** |
| **殘差詞合計** | **452** |

> **信噪比 ＝ 真缺口 4 / 452 ≒ 0.9%**（第二批為 1 / 145 ≒ 0.7%）。

---

## 七、§D 全表自驗

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G109** | ER 斷言依據落於範圍外 | 可行則實作，不可行則明列理由 | **不可行** —— 該判準即 G82（實測 0）；越界者為**規則**而非標的，token 層無法辨識 | **已評估（不實作）** | —— |
| **G110** | R-P154 之承接查證 | 找到承接 leaf 或判為 coverage hole | **找到** —— `SWE-PM-062`（`025`–`027`）；母體 114 leaf / 238 錨點 | **PASS** | 真實 |
| **G111** | 第三批產出 | 32 leaf；`spec_reference` 全部 CFTS009 | **22 leaf**（DR-PW6 停 9、G103 停 1）；61 條；**61 / 61 CFTS009** | **PASS（範圍縮減，已附依據）** | 真實 |
| **G112** | 第三批反向涵蓋 | 行為項／已覆蓋／無對應；三桶；事前未知缺口數 | 行為項 **66**、已覆蓋 **52**、無對應 **14**（皆已裁決）；殘差 **452**；**事前未知缺口 4**；信噪比 **0.9%** | **PASS** | **真實（盲測）** |
| **G70** | lint 全閘 | 全 PASS；leaf 11 → 43；TC 43 → N | `exit=0`；阻斷類 PASS；**leaf 33**（11 → 33，非 43）；**TC 104** | **PASS（leaf 數因排除而異）** | 真實 |
| G94 / G99 / G103 | 沿用 | 期望值不變 | **33 / 33、33 / 33、33 / 33 皆相等** | **PASS** | 合成＋真實 |
| G1–G106 | 沿用 | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合 |

---

## 八、執行層對「本包是否仍有該驗而未驗者」之獨立判斷

分析層於 §K 自判三項（R-P159 為取捨、T13/T16 形態可能更多、21 包並行），
執行層無異議，**本節不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 五項**

1. **第三批之範圍撞上 DR-PW5 / DR-PW6，而下放包未提及。**
   R-P124(d) 當初擇 `Timeout Settings` 之理由之一即「不觸及此二 DR」。
   **DR-PW6 不解，`SWE-PM-001`–`009` 永遠無法產出** ——
   它不只是第三批的問題，是 114 leaf 中 9 個的問題。

2. **`4941984` 之發現說明 layer3 之「靜默丟棄」是一種普遍機制，而本包只驗了 33 個 leaf。**
   G103 之比對範圍是**已產出 TC 之 leaf**。
   **其餘 81 個 leaf 是否也有被靜默丟棄的錨點，本包沒有測。**
   那是一次全量掃描就能得到的數字，我沒有做 —— 因為它超出下放包所要求之範圍。

3. **「原文以 OR 並列而 TC 只取其一」已重複七次。**
   每一次都是靠反向涵蓋的透鏡 1 或 3 事後抓到。
   **這個形態有明確的語法特徵（`or` / `OR` 連接之並列條件），
   看起來是可機械化的** —— 但立閘屬分析層，我不自行為之，僅提請評估。

4. **第三批 61 條全出自我一人，且 R-P159 生效後只有 57 條會被讀到。**
   前二批的三輪缺陷都是分析層讀 TC 全文時發現的。
   本批之取樣率高（93%），但**未取樣的 4 條與 T15 同型之錯誤將無人可及**。

5. **`SWE-PM-014` 之八個錨點我拆成八條，`SWE-PM-025` 之六個錨點拆成八條。**
   這些拆法沒有第二人看過，與 18 §七(甲)2 所指之 `SWE-PM-038` 同型。
   特別是 `SWE-PM-025`：`4941569`–`4941571` 與 `4941572`–`4941574`
   **兩組文字幾乎逐字相同，只差觸發訊號**（`Front_Panel_OnOff.Req` vs
   `CLIMATIC_PANEL.Radio_Btn0`）。我依 §5.7 視為不同觸發而各拆四條，
   **若它們其實是同一行為之兩個入口，本 leaf 就多了四條。**

**（乙）已驗而應標明其強度不足者 —— 一項**

6. **反向涵蓋之「無對應 14 項」我全裁為已涵蓋或範圍外，無一裁為真缺口。**
   四項真缺口是從**殘差詞**（透鏡 3）來的，不是從「無對應」來的。
   即：**透鏡 1 的 14 項無對應，命中率為 0。**
   這與第二批相同（第二批 2 項無對應也全裁為已涵蓋）。
   **透鏡 1 至此連續兩批零命中，其存續價值應予檢討。**

**（丙）R-P149 / R-P150 之遵行（21 包未執行，惟其條文拘束執行層）**

7. **R-P149**（自造損壞不得以 git 修復）—— **本包全程未執行任何 git 操作**。
   20 包之 `git checkout` 我當時判為「修復自身損壞」，
   該條指出**揭露正確而動作仍越線**，我接受。
8. **R-P150**（切片編輯後須立即以語法或載入層檢查驗證）——
   本包對 `lint_tcs.py` 未作切片編輯；對 `batch_002` / `batch_003` 之修改
   **皆以 JSON 載入 → 改鍵 → 寫回**，非字串切片，且每次改動後立即重跑 lint。

---

## 九、DATA_REQUESTS

**新增 DR-PW10（Medium）**（R-P153）與 **DR-PW11（High）**（A-PW117 / R-P144）。
`DR-PW9` **保留予下放包 21，本包未佔用**。

現存 live：DR-PW1（High）、DR-PW5（High）、DR-PW8（High）、**DR-PW11（High）**、
DR-PW3（Medium）、DR-PW6（Medium）、**DR-PW10（Medium）**、DR-PW7（Low）；
DR-PW2、DR-PW4 維持撤回。

---

## 十、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/generated/batch_003_power_state_a.json` | **第三批 22 leaf / 61 條（新增）** |
| `features/power/data/reverse_coverage_003-power-state-a.md` | 第三批反向涵蓋（新增）|
| `features/power/generated/batch_002_timeout_settings.json` | R-P153 標記、R-P154 / R-P155 之 `reasoning`、R-P156 / R-P157 之 ER 修正（改）|
| `features/power/DATA_REQUESTS.md` | DR-PW10、DR-PW11（改）|
| `features/power/RULINGS.md` | R-P153 ~ R-P160 ＋ 台帳缺口記（改）|
| `features/power/ANOMALIES.md` | A-PW112 ~ A-PW119（改）|
| `features/power/docs/upstream/22_batch3.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 22 輪索引（改）|
