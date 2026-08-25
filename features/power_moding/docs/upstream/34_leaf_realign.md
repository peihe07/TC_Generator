# 上繳包 34 —— 射程改以 DESC 比對、`-017`／`-018` 改掛、`-024` 撤除（含 34a）

- 日期：2026-08-25
- 下放包：[handoff/34_leaf_realign.md](../handoff/34_leaf_realign.md) ＋ [34a_flowchart_and_cutoff.md](../handoff/34a_flowchart_and_cutoff.md)
- **零寫回工作簿**

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 ＋ 三處撤回附註 | **6/6 逐字相符**；三條正文 SHA256 **前後同值**（實測） |
| 2 TSV 增 `requirement_description` | 48 列全帶值、空值 0 |
| **3 DESC 射程重驗（36 條）** | **⚠ 停止條件 7 觸發 —— 四處不符，未自行改** |
| 4 `-017`／`-018` 改掛 | 完成；batch 3 lint **32/32** |
| 5 `-024` 撤除 | batch 4 **14 → 13 條**；tc_id **不重編**（`-024` 位次空出） |
| **6 單位比對（36 條）** | **⚠ 停止條件 8 觸發 —— 三處不符** |
| 7 batch 1／2 之樣板查核 | **batch 2 之六條為樣板而其陳述皆為真**；batch 1 之 `-007` 非樣板 |
| 8 `PENDING-ON-DR` 補三筆 | **10 → 13 筆** |
| 9 `DR-PMH8` 增 Q6／Q7 | **7 問 ＋ 首段更正句**，SHA256 `34c711b9dae0af53`，維持 `DRAFT` |
| 停止條件 9 | **未觸發** —— `Splash Screen` 組 leaf 計數 = **3** |

---

## 1. 條文抄錄 ＋ 三處撤回

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH127 | 射程取 DESC；R-PMH125 比對欄撤回 | 722 | `3cf3aa7cc03bd8ed` | `3cf3aa7cc03bd8ed` | 1 | ✅ |
| R-PMH128 | `-017`／`-018` 改掛 | 737 | `065bb0558d84ce47` | `065bb0558d84ce47` | 1 | ✅ |
| R-PMH129 | `-024` 撤除 | 704 | `07f8217a1426bb68` | `07f8217a1426bb68` | 1 | ✅ |
| R-PMH130 | `-023` 狀態詞維持 | 392 | `d13fb40f03759651` | `d13fb40f03759651` | 1 | ✅ |
| R-PMH131 | A-PMH28 定案 | 697 | `eac5e46245f19887` | `eac5e46245f19887` | 1 | ✅ |
| R-PMH132 | R-PMH121 核可生效 | 530 | `75d2fabf5d246937` | `75d2fabf5d246937` | 1 | ✅ |

**三處撤回之附註皆置於 fenced block 之外，正文未改一字**（R-PMH44）：

| 被撤回一部者 | 撤回前 SHA256 | 撤回後 SHA256 | 不變 |
|---|---|---|---|
| R-PMH125（比對欄） | `618b40eca70718e6` | `618b40eca70718e6` | ✅ |
| R-PMH121（核可生效） | `04cdd9167e63da4b` | `04cdd9167e63da4b` | ✅ |
| R-PMH123（`-023` 部分） | `ee77d0a36d1230ed` | `ee77d0a36d1230ed` | ✅ |

**32 包 §4.2(a) 之撤回**記於 `gen_batch04.py` 之 `-024` 定義處（其為指示而非條文，無 SHA 可證）。

---

## 2. 步驟 2 —— TSV 增 `requirement_description`

`data/layer3_sections.tsv` 現有九欄，**48 列全帶 `requirement_title` 與
`requirement_description`，空值 0**。

---

## 3. ⚠ 步驟 3 —— DESC 射程重驗（36 條）：**停止條件 7 觸發，四處**

| tc | leaf | `Requirement Description`（037 之權威，節錄） | 判定 |
|---|---|---|---|
| `-001` | `SWE1-HMI-PM-001-03` | During the Disclaimer screen (content per CFTS009/legal), if the system is not ready, it displays "Loading…". When the system is r | 相符 |
| `-002` | `SWE1-HMI-PM-001-04` | The system allows the user to either press Accept to go directly to last mode screen, or wait for timeout (which automatically equ | 相符 |
| `-003` | `SWE1-HMI-PM-001-04` | The system allows the user to either press Accept to go directly to last mode screen, or wait for timeout (which automatically equ | 相符 |
| `-004` | `SWE1-HMI-PM-001-05` | Exception: For Maserati applications, the system provides no timeout (per CFTS009); the user must manually press Accept. | 相符 |
| `-005` | `SWE1-HMI-PM-003` | SU2.) For Maserati vehicles, while on the disclaimer screen the user will have access to their comfort controls. No timeout is pro | 相符 |
| `-006` | `SWE1-HMI-PM-004` | SU2.1) Do not display comfort controls on Maserati disclaimer screen when vehicle is equipped with lower comfort screen. | 相符 |
| `-007` | `SWE1-HMI-PM-005` | SU3.) No pop-ups will appear until the disclaimer screen has been removed. If an item like a traffic announcement is received like | 相符 |
| `-008` | `SWE1-HMI-PM-022-02` | When the user presses the power button to change to On state, the system shall display the disclaimer screen (see SU6.) unless cer | **不符（例外未處理）** |
| `-009` | `SWE1-HMI-PM-012` | SSND 1) If start-up sounds are supported, it will start upon driver door close and sync with the start-up animation. If goodbye so | 相符 |
| `-010` | `SWE1-HMI-PM-012` | SSND 1) If start-up sounds are supported, it will start upon driver door close and sync with the start-up animation. If goodbye so | 相符 |
| `-011` | `SWE1-HMI-PM-013` | SSND 2) Start-up and goodbye sounds shall have a setting with Always/Once a Day/Never options. | 相符 |
| `-012` | `SWE1-HMI-PM-014` | SSND 2.1) If the setting is Always, start-up and goodbye sounds should be played everytime the startup animation is played. | 相符 |
| `-013` | `SWE1-HMI-PM-015` | SSND 2.2) If the setting is Once a Day, start-up and goodbye sounds should be played only once per day (i.e other valid triggers w | 相符 |
| `-014` | `SWE1-HMI-PM-016` | SSND 2.3) If the setting is Never, start-up and goodbye sounds should not be played on any situation. | 相符 |
| `-015` | `SWE1-HMI-PM-017` | SSND 3) Sound volume level shall match current entertainment sounds volume. [DCR19385]_x000D_ _x000D_ | 相符 |
| `-016` | `SWE1-HMI-PM-018-01` | If there are popups to show at IGN OFF and the user has set Power Accessory Delay to 0 seconds, the system shall stay awake for up | **不符（射程不足）** |
| `-017` | `SWE1-HMI-PM-018-02` | If the user interacts with the FOTA popup, the system shall stay awake until the user has not interacted with the popup for 60 sec | 相符 |
| `-018` | `SWE1-HMI-PM-018-03` | For Priority 1 (FOTA update available): If the user accepts the FOTA popup, the system shall start the update and dismiss FOTA via | 相符 |
| `-019` | `SWE1-HMI-PM-018-03` | For Priority 1 (FOTA update available): If the user accepts the FOTA popup, the system shall start the update and dismiss FOTA via | 相符 |
| `-020` | `SWE1-HMI-PM-018-03` | For Priority 1 (FOTA update available): If the user accepts the FOTA popup, the system shall start the update and dismiss FOTA via | 相符 |
| `-021` | `SWE1-HMI-PM-018-04` | For Priority 2 (FOTA via Wi-Fi configuration): If the user chooses to configure Wi-Fi, the system shall display Charge Now (if app | 相符 |
| `-022` | `SWE1-HMI-PM-018-04` | For Priority 2 (FOTA via Wi-Fi configuration): If the user chooses to configure Wi-Fi, the system shall display Charge Now (if app | 相符 |
| `-023` | `SWE1-HMI-PM-018-05` | For Priority 3 (XEV key off popups: Charge Now/Summary, Preconditioning): If the user dismisses any XEV key off popup, the system  | 相符 |
| `-025` | `SWE1-HMI-PM-001-01` | When driver door is closed, the system plays a 3-second startup animation. If ignition remains OFF after animation, the system tur | **不符（DESC 首句無本 leaf 之 TC）** |
| `-026` | `SWE1-HMI-PM-001-02` | If ignition is turned ON during the startup animation, the system interrupts the animation and plays splash screens (1.5 sec each) | **不符（射程不足）** |
| `-027` | `SWE1-HMI-PM-011` | SU8.) Show the splash screen and disclaimer screen once per CAN BUS cycle | 相符 |
| `-028` | `SWE1-HMI-PM-006-01` | If start-up animation is supported, the system shall start it upon driver door close and conclude it within 3 seconds. | 相符 |
| `-029` | `SWE1-HMI-PM-006-02` | If shut-down animation is supported, the system shall begin playing it and conclude it within 10 seconds. | 相符 |
| `-030` | `SWE1-HMI-PM-006-03` | The system shall begin shut-down animation only when both KEY OFF and radio UI shut down are present (not necessarily simultaneous | 相符 |
| `-031` | `SWE1-HMI-PM-007` | DS4.1) If doors are removed/not present and ignition is turned to ACC, RUN, or START, do not show Start Up Animation and jump dire | 相符 |
| `-032` | `SWE1-HMI-PM-008-01` | If the ignition cycle has not changed, the system shall play the animation only once per CAN BUS wake-up upon closing the driver d | 相符 |
| `-033` | `SWE1-HMI-PM-008-02` | If the vehicle ignition is turned to ACC, RUN, or START ON while the driver door is open, the system shall skip the animation scre | 相符 |
| `-034` | `SWE1-HMI-PM-009-01` | If the last state is Radio OFF, the system shall play startup animation and show applicable splash screens when the driver door is | 相符 |
| `-035` | `SWE1-HMI-PM-009-02` | When the Power Button is pressed On, the system shall not show the Start Up Animation. | 相符 |
| `-036` | `SWE1-HMI-PM-010` | SU7.) Start up animation should sync on start up with all capable screen’s start up animation. Animations on all screens should st | 相符 |
| `-037` | `SWE1-HMI-PM-010` | SU7.) Start up animation should sync on start up with all capable screen’s start up animation. Animations on all screens should st | 相符 |

### 3.1 四處不符，逐處具名

| # | tc | DESC 之要求 | 我之 TC | 差 |
|---|---|---|---|---|
| **1** | **`-016`** | `… stay awake for up to 2.5 minutes …` **＋** `If the user does not interact with the popup within **the 60-second timeout defined in the pop-up list**, the system shall **close the popup**. If no other popups remain, the system shall **shut off the radio**.` | 只斷言「維持喚醒 ≤ 2.5 分鐘」 | **三項未斷言**：60 秒逾時、popup 關閉、radio 關機 |
| **2** | **`-026`** | `… the system **interrupts the animation** and plays splash screens (1.5 sec each), **then proceeds to Disclaimer**.` | 只斷言 splash 呈現與 1.5 秒逾時 | **二項未斷言**：動畫被中斷、其後進入免責畫面 |
| **3** | **`-008`** | `… shall display the disclaimer screen **unless certain phone call scenarios have occurred**.` | 無任何排除通話情境之前提 | **其例外未處理** |
| 4 | `-025` | DESC **首句**為 `When driver door is closed, the system plays a 3-second startup animation.` | 只斷言第二句（黑螢幕） | **首句由 `-028` 承載，而 `-028` 掛 `-006-01`** —— 037 自身重複，非我之錯，惟本 leaf 之首句無本 leaf 之 TC |

**我未自行改**（下放包步驟 3 逐字：「發現任一不符即停並上呈 —— 不自行改掛」）。

### 3.2 ⚠ 第 1 項推翻了 A-PMH25 —— **我當初「不造值」的前提不成立**

30 包我判 9.1 之權威文本於逾時處為破句（`within 60 the timeout defined in pop-up list`），
**故 `-016` 不斷言任何逾時秒數**（A-PMH25）。

**037 之 DESC 於同處為完整句**：`within the 60-second timeout defined in the pop-up list,
the system shall close the popup. If no other popups remain, the system shall shut off the radio.`

**60 秒之值在 037 內，其後二句亦完整。**
**「無法確定」只在 SYS1 側成立，而 037 為需求單位之權威**（canon §8.2）。

→ **A-PMH25 改 `RESOLVED`**（原文依 R-PMH44 保留，其更正另立一節）。

> **這一項是本包最實質的所得**：**我在 30 包看的是 SYS1，而該欄一直在 037 裡。**
> R-PMH127 所令之增欄，**不只修正了比對之判準，還修正了一個「不造值」之判斷**。

### 3.3 第 3 項（`-008`）之性質不同

`-008` 屬 **batch 1**，**其於 12 包經覆核、於此後未再動**。
其 DESC 之 `unless certain phone call scenarios have occurred` **本身即未定義**
（`certain` 未指明何者）—— **改與不改皆須先知道那是哪些情境**。
**其形態同 A-PMH22（記法未定義），惟本包不開新 DR**（下放包未令），**具名待裁**。

---

## 4. 步驟 4 —— `-017`／`-018` 之改掛

| tc | 原 leaf | 現 leaf | 037 DESC 之依據 |
|---|---|---|---|
| `-017` | `-018-01` | **`-018-02`** | `If the user interacts with the FOTA popup … 60 seconds. The maximum … 10 minutes.` |
| `-018` | `-018-02` | **`-018-03`** | `For Priority 1 (FOTA update available): If the user accepts the FOTA popup …` |

其 `reasoning` 與 `distinguishing_axis` 一併更新（原「同 leaf 之第二條、profile §4」之
拆分依據**隨之撤回** —— `-017` 與 `-016` 已非同 leaf）。

**batch 3 之 leaf 指派現為**：`-016`→`-018-01`／`-017`→`-018-02`／
`-018`／`-019`／`-020`→`-018-03`／`-021`／`-022`→`-018-04`／`-023`→`-018-05`。
**leaf_scope 仍為 5，lint 32/32。**

---

## 5. 步驟 5 —— `-024` 之撤除

- 其定義**保留於 `gen_batch04.py`**，以 `dropped=True` 排除於輸出（R-PMH44 原文不刪）；
- **tc_id 不重編** —— 輸出自 `-025` 起，`-024` 之位次空出；
- `limits` 由三筆減為 **二筆**（`-026`／`-027`）；
- **`Splash Screen` 組 leaf 計數 = 3**（`-001-01`／`-001-02`／`-011`）→ **停止條件 9 未觸發**。

**覆蓋缺口登記為 A-PMH29**，併入 `DR-PMH8` Q6，並入 `PENDING-ON-DR` 第 11 筆。

### 5.1 修正後之 batch 4（13 條）

#### `NR1L-DisclaimerScreen-025` — Screen is black when the ignition remains off after the animation

- **leaf**：`SWE1-HMI-PM-001-01`　**Test Set**：`Splash Screen`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**限定**：無

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The driver door is open and the ignition is off
```

**test_procedure**

```
1. Close the driver door and let the animation finish
2. Check that the screen is black after the animation
```

**expected_result**

```
1. The startup animation finishes with the ignition still off
2. The screen is black
```

#### `NR1L-DisclaimerScreen-026` — Splash screens are presented when the ignition is turned on during the animation

- **leaf**：`SWE1-HMI-PM-001-02`　**Test Set**：`Splash Screen`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**限定**：**有**

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The driver door is open and the ignition is off
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and turn the ignition on during the animation
3. Read the display and record each splash screen and its duration
4. Check that the splash screens are presented with a 1.5 second timeout
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The ignition is turned on while the animation is playing
3. The splash screens are presented
4. Each splash screen times out after 1.5 seconds
```

#### `NR1L-DisclaimerScreen-027` — Splash and disclaimer screens are shown once per CAN BUS cycle

- **leaf**：`SWE1-HMI-PM-011`　**Test Set**：`Splash Screen`　**dm**：狀態轉換 (State Transition Testing)　**限定**：**有**

**pre_conditions**

```
1. Splash screen and disclaimer screen are supported on this vehicle
2. The CAN BUS has just woken up and neither screen has been shown yet
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and record the screens shown
3. Reopen and close the driver door in the same CAN BUS cycle
4. Check that neither screen is shown a second time
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The splash screen and the disclaimer screen are shown once
3. The second door closure occurs within the same CAN BUS cycle
4. Neither the splash screen nor the disclaimer screen is shown again
```

#### `NR1L-DisclaimerScreen-028` — Start-up animation starts on driver door close and concludes by three seconds

- **leaf**：`SWE1-HMI-PM-006-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**限定**：無

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The driver door is open
```

**test_procedure**

```
1. Close the driver door and record the animation start time
2. Record the animation end time
3. Check that the animation concluded within three seconds
```

**expected_result**

```
1. The start-up animation starts when the driver door is closed
2. The animation end time is recorded
3. The animation concludes by three seconds
```

#### `NR1L-DisclaimerScreen-029` — Shut-down animation begins playing and concludes within ten seconds

- **leaf**：`SWE1-HMI-PM-006-02`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**限定**：無

**pre_conditions**

```
1. Shut-down animation is supported on this vehicle
2. The head unit is on
```

**test_procedure**

```
1. Trigger the shut-down animation and record its start time
2. Record the animation end time
3. Check that the animation concluded within ten seconds
```

**expected_result**

```
1. The shut-down animation begins playing
2. The animation end time is recorded
3. The animation concludes within ten seconds
```

#### `NR1L-DisclaimerScreen-030` — Shut-down animation begins only on key off combined with radio UI shut down

- **leaf**：`SWE1-HMI-PM-006-03`　**Test Set**：`Startup Animation`　**dm**：功能測試 (Functional based ; no specific technique)　**限定**：無

**pre_conditions**

```
1. Shut-down animation is supported on this vehicle
2. The ignition is on and the radio UI is running
```

**test_procedure**

```
1. Turn the key off without shutting the radio UI down
2. Shut the radio UI down and read the display
3. Check that the animation began only after both had occurred
```

**expected_result**

```
1. The shut-down animation does not begin on key off alone
2. The shut-down animation begins after the radio UI shuts down
3. The animation began only once both conditions had occurred
```

#### `NR1L-DisclaimerScreen-031` — No start-up animation is shown when the doors are removed

- **leaf**：`SWE1-HMI-PM-007`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**限定**：無

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The doors are removed or not present
```

**test_procedure**

```
1. Turn the ignition to ACC, RUN or START and read the display
2. Check that the display went directly to the splash screen
```

**expected_result**

```
1. No start-up animation is shown
2. The display goes directly to the splash screen
```

#### `NR1L-DisclaimerScreen-032` — Animation is played only once while the ignition cycle has not changed

- **leaf**：`SWE1-HMI-PM-008-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**限定**：無

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The animation has already been played once in this ignition cycle
```

**test_procedure**

```
1. Reopen and close the driver door in the same ignition cycle
2. Check that the animation is not played a second time
```

**expected_result**

```
1. The driver door is closed again within the same ignition cycle
2. The animation is not played a second time
```

#### `NR1L-DisclaimerScreen-033` — Animation is skipped when the ignition is turned on with the door open

- **leaf**：`SWE1-HMI-PM-008-02`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**限定**：無

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The driver door is open
```

**test_procedure**

```
1. Turn the ignition to ACC, RUN or START with the door open
2. Check that the display starts from the applicable splash screen
```

**expected_result**

```
1. The animation screen is skipped
2. The display starts from the applicable splash screen
```

#### `NR1L-DisclaimerScreen-034` — Animation and splash play with the screen black when the last state is Radio OFF

- **leaf**：`SWE1-HMI-PM-009-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**限定**：無

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The last state of the radio is OFF and the driver door is open
```

**test_procedure**

```
1. Close the driver door and record the animation and splash screens
2. Check that the screen remains black afterwards
```

**expected_result**

```
1. The startup animation plays and the applicable splash screens are shown
2. The screen remains black
```

#### `NR1L-DisclaimerScreen-035` — No start-up animation is shown when the power button is pressed on

- **leaf**：`SWE1-HMI-PM-009-02`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**限定**：無

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The head unit is off
```

**test_procedure**

```
1. Press the power button to turn the head unit on
2. Check that no start-up animation is shown
```

**expected_result**

```
1. The head unit turns on
2. No start-up animation is shown
```

#### `NR1L-DisclaimerScreen-036` — Start-up animation syncs across all capable screens

- **leaf**：`SWE1-HMI-PM-010`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**限定**：無

**pre_conditions**

```
1. Start-up animation is supported on more than one screen in this vehicle
2. The driver door is open
```

**test_procedure**

```
1. Close the driver door and record each screen's animation start
2. Check that the animations started in sync with each other
```

**expected_result**

```
1. The start-up animation starts on every capable screen
2. The animations on all capable screens are in sync on start up
```

#### `NR1L-DisclaimerScreen-037` — Animations on all screens stop when the animation is interrupted

- **leaf**：`SWE1-HMI-PM-010`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**限定**：無

**pre_conditions**

```
1. Start-up animation is supported on more than one screen in this vehicle
2. The start-up animation is playing on every capable screen
```

**test_procedure**

```
1. Interrupt the animation with an ignition button press
2. Check that the animations stopped on all screens
```

**expected_result**

```
1. The animation is interrupted by the ignition button press
2. The animations on all screens stop
```


---

## 6. ⚠ 步驟 6 —— 單位比對：**停止條件 8 觸發，三處**

| tc | leaf | DESC 之單位 | TC 之單位 | 缺 |
|---|---|---|---|---|
| **`-016`** | `-018-01` | `0 秒`／`2.5 分`／**`60 秒`** | `0 秒`／`2.5 分` | **`60 秒`** |
| **`-025`** | `-001-01` | **`3 秒`** | —— | **`3 秒`**（其由 `-028` 承載，惟該條掛他 leaf） |
| **`-032`** | `-008-01` | `ignition cycle`／**`CAN BUS wake-up`** | `ignition cycle` | **`CAN BUS wake-up`** |

**其餘 33 條相符。**

> ⚠ **一項自查**：本比對之第一版用了寬鬆之前綴比對，**`-016` 之 `60 秒` 被誤判為相符**
> （`'0 seconds'` 之首詞 `0` 命中 `'60-second'`）。**改為正規化後之精確集合差方測出。**
> **寬鬆比對會把「缺一個單位」讀成「相符」——其為偽陰，於此具名。**

### 6.1 `-032` 之單位 —— 34 包 §2.2 判為偽陽，**而單位比對仍判其缺**

下放包 §2.2 以「DESC 兩個單位皆在，037 未替任何人選」判 `-032` 之 title 指摘不成立。
**該判斷就 `射程` 而言成立**（本包 §3 之 DESC 比對亦判其相符）。

**惟就 `單位` 而言其仍缺** —— DESC 逐字為
`play the animation only once **per CAN BUS wake-up** upon closing the driver door`，
**其計次單位為 CAN BUS wake-up，而 `ignition cycle` 是其條件**。
我之 TC 以 `ignition cycle` 為計次單位而**未驗 CAN BUS wake-up**。

**二者不衝突**：射程相符（同一句），單位不符（計次之基準取錯）。**具名待裁。**

---

## 7. 步驟 7 —— batch 1／2 之限定是否亦為樣板（**只查不改**）

| 批 | 條數 | 結果 |
|---|---|---|
| batch 1（`-007`） | 1 | **非樣板** —— 其 reasoning 逐字載「**ER1～ER5 之逐斷言掃描已完成**」並逐一具名其結果（ER1／ER2 為限定之複述、ER3 規格側 2 行矩陣側 0 格、ER5 …） |
| **batch 2**（`-009`／`-010`／`-012`～`-015`） | 6 | **是樣板** —— 六條含一字不差之「本條之 ER 斷言『聲音有／無播放』」，**未具名哪一個 ER** |

### 7.1 **惟其與 batch 4 之樣板性質不同，此點須分辨**

**batch 4 之樣板其陳述於九條為假**（該九條無逾時斷言）。
**batch 2 之樣板其陳述於六條皆為真** —— 逐條實查：

| tc | 其確有之聲音斷言 |
|---|---|
| `-009` | `The start-up sound starts when the driver door is closed` |
| `-010` | `The goodbye sound starts at the start of the animation` |
| `-012` | `The sound was played on both occasions` |
| `-013` | `The sound was played once and not on the second occasion` |
| `-014` | `No start-up sound is played …`（負向） |
| `-015` | `The start-up sound is played and its volume level is recorded` |

**故其違反者為 R-PMH126 之形式要求（須具名該一個 ER），非其實質**
（R-PMH43 之「陳述須有證據」於此六條成立）。

**本輪只查與具名，未改**（下放包步驟 7 明令）。

---

## 8. 步驟 8 —— `PENDING-ON-DR` 補三筆（10 → 13）

| # | 判定 | 所繫 |
|---|---|---|
| 11 | `-024` 之撤除（A-PMH29） | `DR-PMH8` Q6 |
| 12 | A-PMH28 之五類流程圖行為 | `DR-PMH8` Q7 |
| 13 | `-023` 之停手 | `DR-PMH5` (1)(2) |

第 (3) 欄逐值列出。**第 13 筆特別記明**：依 R-PMH130，其於「已知未決清單」中之
出現理由為**「待答」而非「已接受」**。

**R-PMH132(b) 生效後，本簿之各筆全數為交付揭露事項** —— 其第 (3) 欄即該清單之內容。

---

## 9. 步驟 9 —— `DR-PMH8` 之最終形態

**7 問 ＋ 首段更正句**，SHA256 **`34c711b9dae0af53`**，**狀態 `DRAFT`、`SENT` 欄留空**。

**Q6／Q7 分立而不合為一節**（下放包令執行層擇一並載理由）——
其型別雖同（皆為「規格有而 037 無」），**惟成因不同**：
Q6 為 **SYS1 匯出漏句**（A-PMH03），Q7 為 **其載體為流程圖**（A-PMH04／A-PMH28）。
**上游若只答其一，分立可看出另一問未答**（同 Q4／Q5 分立之理由）。

---

## 10. 檢查總表 ＋ lint

```
batch01 32/32   batch02 32/32   batch03 32/32   batch04 32/32
--limit-must-hit → 刪去 21/21 皆 FAIL（7 + 12 + 2）
--final-step-must-hit → 通過
```

**新增檢查程式 0、新增檢查項 0**；apparatus 維持凍結。
`verdict_form` **0 failure**；**未註冊 must-hit 而標「未實測」者 = 4**（不變）。

---

## 11. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（7 問）** | 否 —— **其載 R-PMH112 之更正，未發出期間該不符持續存在** |

---

## 12. 本包是否仍有該驗而未驗者 —— **有**

1. **DESC 一比就查出四處，而其中 `-008` 屬 batch 1。**
   **batch 1 於 12 包覆核通過，此後十九輪未再以任何新判準重驗過。**
   **本包只逐條比對了 DESC 與單位兩項** —— batch 1／2 是否還有其他形態之問題，未查。
2. **A-PMH25 之翻案顯示一件更一般的事**：**我有多少「不造值」之判斷，其前提是「SYS1 側沒有」？**
   本包只翻了這一件。**037 之 DESC 是二包前才進到台帳的，在此之前所有基於「素材不足」
   之判斷都沒有對照過它。**
3. **`-016`／`-026` 之射程不足，其修正會改變 batch 3／4 之內容** ——
   而 batch 3 已覆核通過、batch 4 已用滿 R-PMH120 之二輪。**其輪數如何計，未定。**
4. **單位比對之第一版寬鬆比對曾把 `-016` 讀成相符** —— 我改為精確比對才測出。
   **若我沒有改，本包會報「單位全數相符」。**
5. **`-025` 之「DESC 首句無本 leaf 之 TC」我判為第 4 處而非前三處之同級** ——
   其成因是 **037 自身於 `-001-01` 與 `-006-01` 重複了同一行為**。
   **我未判其為 037 之缺陷，只記其現象** —— 該判斷未經裁定。
6. **A-PMH28 之五類行為經 R-PMH131 定案不寫 TC，而其中 `toggle them one after another`
   仍落在 `-026`／`-033`／`-034` 之標的內** —— 其「不斷言輪替順序」自此為裁定而非暫置，
   **惟該三條之 reasoning 尚未改為引 R-PMH131**（本包未令，未改）。

---

## 13. 建議之 commit（**未執行**）

```
feat(power_moding): package 34 — scope verified against 037 DESC, -017/-018 rehooked, -024 withdrawn
```

pathspec（**11 路徑**）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/data/layer3_sections.tsv
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/34_leaf_realign.md
features/power_moding/docs/handoff/34a_flowchart_and_cutoff.md
features/power_moding/docs/upstream/34_leaf_realign.md
features/power_moding/generated/batch03.json
features/power_moding/generated/batch04.json
features/power_moding/scripts/gen_batch03.py
features/power_moding/scripts/gen_batch04.py
```

### 13.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| **停止條件 7** | **觸發** —— DESC 射程四處不符，**未自行改** |
| **停止條件 8** | **觸發** —— 單位三處不符，**未自行改** |
| 停止條件 9 | 未觸發（`Splash Screen` = 3 leaf） |
| apparatus | **維持凍結** —— 新增程式 0、新增檢查項 0 |
| 計數之變更 | **`n_leaf` 未變（46）** —— `-024` 之撤除減的是 TC，非 leaf（`-001-01` 仍有 `-025`） |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT`（7 問） |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
