# 上繳包 33 —— batch 4 之重做（限定逐條重導）、TSV 增 `requirement_title`

- 日期：2026-08-25
- 下放包：[handoff/33_batch4_rework.md](../handoff/33_batch4_rework.md)
- **batch 4 之第二輪**（R-PMH120 之上限）
- **零寫回工作簿**

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH122～126 **5/5 逐字相符**，命中數各 1 |
| 2 限定逐條重導 | **十四筆 → 三筆**（**非下放包所列之五筆** —— §2.2 具名其差異） |
| 3 `input_test_data` | 四批 **37 條全為 `NA`**（**下放包謂 43 條、謂 batch 3 已是 `NA`，二者皆與實測不同**） |
| 4 狀態詞 | `-002`／`-028` → **`ACCEPTED`**；**`-023` 我未改**（其不同類，§4） |
| 5 TSV 增欄 | 48 列全帶 `requirement_title`；**⚠ 停止條件 8 觸發 —— 五處不符** |
| 6 must-hit 母體 | 來源改為 glob；**⚠ 停止條件 9 字面觸發（規模未變），目的未觸發** |
| 7 lint | **四批皆 32/32**；檢查項數維持 **32** |
| 停止條件 7 | **未觸發**（14 條全 1:1 且步數 ≥ 2） |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中數 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH122 | 追溯欄不得記載未驗證之句子 | 482 | `55366ba34f74179b` | `55366ba34f74179b` | 1 | ✅ |
| R-PMH123 | `A-PMH27` 採 `ACCEPTED` | 395 | `ee77d0a36d1230ed` | `ee77d0a36d1230ed` | 1 | ✅ |
| R-PMH124 | 一般化須及於期望值與母體 | 379 | `880a2d7e17eeae55` | `880a2d7e17eeae55` | 1 | ✅ |
| R-PMH125 | TSV 增 `requirement_title` | 582 | `618b40eca70718e6` | `618b40eca70718e6` | 1 | ✅ |
| R-PMH126 | 限定須逐條導出 | 473 | `007460230dc2e4eb` | `007460230dc2e4eb` | 1 | ✅ |

---

## 2. 步驟 2 —— 限定之逐條重導（R-PMH126）

### 2.1 §2.1 之指摘成立 —— **我把同一段貼了十四次**

十四條之 `reasoning` 含一字不差之「與**本條之逾時斷言**同謂詞取相反值」，
而九條之 ER 中無任何逾時。**該句於該九條為不成立之陳述**（R-PMH43）。

**結構上已改掉了產生它的方式**：限定不再寫死於各條之 `proc`／`er`，
改為**旗標 `lim=(ER 之指名, 其理由)`**，由 `main()` 依旗標插入步驟與 ER
並**產生編號**。**無旗標者不可能得到限定** —— 樣板在結構上已不可貼。

### 2.2 ⚠ 我的逐條導出結果為**三筆**，與下放包所列之五筆不同

R-PMH126 令「逐條具名該條之哪一個 ER 斷言與素材取相反值」。**逐條導出如下**：

| 素材 | 逐字 |
|---|---|
| `SU9.)` | `Pressing "Screen Off" or "Power Off" hard key **will not do anything when pressed during animation**.` |
| `SU9.1)` | `Pressing Power Off or Screen Off hard keys **during the splash screen(s) or disclaimer** will reset the timeout **and the radio shall display the screen the next time the screen turns on**.` |

| tc | 其斷言 | 素材是否取相反值 | 判 |
|---|---|---|---|
| `-024` | ER3 splash 逾時 1.5 秒 | `SU9.1)` 前半重設逾時 → **是** | **保留** |
| `-026` | ER3 splash 逾時 1.5 秒 | 同上 → **是** | **保留** |
| `-027` | ER3 splash／免責**不再顯示** | `SU9.1)` **後半**令其 `display the screen the next time the screen turns on` → **是** | **保留** |
| `-028`／`-029` | 動畫時長 3 秒／10 秒 | `SU9.)` 逐字為**按鍵於動畫期間不做任何事** → **否** | **移除** |
| `-032` | 動畫不再播放（計次） | 同上 → **否** | **移除** |
| 其餘九條 | 無逾時亦無再顯示之斷言 | → **否** | **移除** |

**與下放包 §2.1 之差異二處，皆須裁**：

1. **`-027` 下放包列為「無逾時斷言」而我保留** ——
   其依據**不是逾時，是 `SU9.1)` 之後半句**（再顯示）。
   **本批唯一以後半句為依據者，已於其 reasoning 具名。**
2. **`-028`／`-029`／`-032` 下放包列為「有逾時／時長斷言」而我移除** ——
   其斷言確為時長／計次，**惟 `SU9.)` 於動畫期間之逐字為「不做任何事」**，
   **二者不取相反值**。依 R-PMH126 末句「該條若無與素材取相反值之斷言，
   其限定即為 §8.5 之不必要窄化，須移除」。

> **停止條件 7 所預設之「九條」因而為十一條。**
> **實測：14 條全部 procedure : ER 為 1:1，且步數皆 ≥ 2 → 停止條件 7 未觸發。**
> **若下放包之五筆為裁定而非工作稿，一句話反轉。**

### 2.3 `-035` 之矛盾已消失

其限定經 §2.2 判為移除，**「不要按這顆鍵」而後「按這顆鍵」不再並存**。
**下放包 §2.2 之預期（依 §2.1 移除後矛盾自然消失）成立。**

### 2.4 修正後之十四條全文

#### `NR1L-DisclaimerScreen-024` — Splash screen is presented after the startup animation

- **leaf**：`SWE1-HMI-PM-001-01`　**Test Set**：`Splash Screen`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：**有**（press the Power Off or Screen Off hard key）
- **軸**：路徑：點火開啟下之正常序列（對 -025 之點火維持關閉）

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The driver door is open and the ignition is on
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and record the animation start
3. Read the display and record the splash screen
4. Check that the splash screen is presented after the animation
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The startup animation is presented when the driver door is closed
3. The splash screen is presented after the animation
4. Each splash screen times out after 1.5 seconds
```

#### `NR1L-DisclaimerScreen-025` — Screen is black when the ignition remains off after the animation

- **leaf**：`SWE1-HMI-PM-001-01`　**Test Set**：`Splash Screen`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **事件層限定**：無
- **軸**：等價類：點火於動畫後維持關閉（對 -026 之動畫期間開啟）

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

- **leaf**：`SWE1-HMI-PM-001-02`　**Test Set**：`Splash Screen`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **事件層限定**：**有**（press the Power Off or Screen Off hard key）
- **軸**：等價類：點火於動畫期間開啟（對 -025 之維持關閉）

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

- **leaf**：`SWE1-HMI-PM-011`　**Test Set**：`Splash Screen`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：**有**（press the Power Off or Screen Off hard key）
- **軸**：計次單位：CAN BUS cycle（對 -032 之 ignition cycle）

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

- **leaf**：`SWE1-HMI-PM-006-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：無
- **軸**：動畫別：啟動動畫之時序（對 -029 之關機動畫）

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

- **leaf**：`SWE1-HMI-PM-006-02`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：無
- **軸**：動畫別：關機動畫之時序（對 -028 之啟動動畫）

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

- **leaf**：`SWE1-HMI-PM-006-03`　**Test Set**：`Startup Animation`　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1
- **事件層限定**：無
- **軸**：謂詞：關機動畫之觸發組合（對 -028／-029 之時序）

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

- **leaf**：`SWE1-HMI-PM-007`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **事件層限定**：無
- **軸**：等價類：門被移除／不存在（其對立類無專條，見 reasoning）

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

- **leaf**：`SWE1-HMI-PM-008-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：無
- **軸**：路徑：同週期內重複觸發（對 -033 之點火轉 ACC/RUN/START）

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

- **leaf**：`SWE1-HMI-PM-008-02`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **事件層限定**：無
- **軸**：等價類：門開著時點火開啟（對 -032 之同週期重複門關閉）

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

- **leaf**：`SWE1-HMI-PM-009-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：無
- **軸**：路徑：最後狀態為 Radio OFF（對 -035 之按電源鍵開機）

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

- **leaf**：`SWE1-HMI-PM-009-02`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **事件層限定**：無
- **軸**：等價類：按電源鍵開機（對 -034 之門關閉）

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

- **leaf**：`SWE1-HMI-PM-010`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：無
- **軸**：觸發：開機時之跨螢幕同步（對 -037 之中斷）

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

- **leaf**：`SWE1-HMI-PM-010`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **事件層限定**：無
- **軸**：觸發：動畫被中斷（對 -036 之開機同步）

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

## 3. 步驟 3 —— `input_test_data` 四批核對

| 批 | 條數 | 值 |
|---|---|---|
| batch01 | 8 | `NA` |
| batch02 | 7 | `NA` |
| batch03 | 8 | **原 `N/A` → 已改 `NA`** |
| batch04 | 14 | **原 `N/A` → 已改 `NA`** |
| **合計** | **37** | **全為 `NA`** |

⚠ **下放包 §2.3 二處與實測不同**：
(a) 謂「batch 1／2／3 皆為 `NA`」—— **batch 3 實為 `N/A`**，故**須改者為兩批而非一批**；
(b) 步驟 3 謂「`NA` 應為 43 條全數」—— **實為 37 條**（8＋7＋8＋14）。

**已一併更正並於 `gen_batch03.py` 之註解具名。**

---

## 4. 步驟 4 —— 停手三筆之狀態詞

| 筆 | 狀態詞 | 依據 |
|---|---|---|
| `-002`（A-PMH27） | **`ACCEPTED`** | R-PMH123 |
| `-028`（A-PMH13） | **原 `RESOLVED（處置已定）` → 改 `ACCEPTED`** | R-PMH123 之「同理適用」 |
| **`-023`** | **`STOPPED-PENDING-DR`（我未改為 `ACCEPTED`）** | 見下 |

### 4.1 ⚠ 我未把 `-023` 改為 `ACCEPTED`

**R-PMH123 令三者一致，而我判 `-023` 不同類**：

- `-002`／`-028` 為 **out of scope** —— **不寫入交付工作簿**，其缺口永久存在；
- **`-023` 仍在交付範圍內** —— 其為 `Power Transitions` 組 6 leaf 之一，
  **只是暫不產出 TC，待 `DR-PMH5` `ANSWERED`**。

**該差別正是 R-PMH119(b) 所分者**（逐字：「**2 leaf 停手**（`-023` 依 R-PMH111、`-002` 依 R-PMH117）」
—— 其以不同條文分別處置，非同一處置）。

**若標 `ACCEPTED`，讀者會以為 `-023` 已被裁定不寫入** —— 而它沒有。
**一句話可反轉。**

---

## 5. 步驟 5 —— TSV 增 `requirement_title` ＋ **⚠ 停止條件 8 觸發**

`data/layer3_sections.tsv` 增一欄，**48 列全帶值、空值 0**，
其值逐字取自 037 `Analysis Report` 之 `Requirement  Title` 欄。

**逐條核對四批 37 條**：

| tc | leaf | `requirement_title`（037 之權威） | tc_title | 判定 |
|---|---|---|---|---|
| `-001` | `SWE1-HMI-PM-001-03` | Disclaimer and Loading Screen Display | Loading indicator replaced by Accept button when the system becomes ready | 相符 |
| `-002` | `SWE1-HMI-PM-001-04` | Accept Button Display upon System Readiness | Accept press goes directly to the last mode screen | 相符 |
| `-003` | `SWE1-HMI-PM-001-04` | Accept Button Display upon System Readiness | Disclaimer screen times out without user input on a non-Maserati application | 相符 |
| `-004` | `SWE1-HMI-PM-001-05` | Maserati Disclaimer Timeout Exception | Maserati disclaimer screen provides no timeout | 相符 |
| `-005` | `SWE1-HMI-PM-003` | Maserati Comfort Controls on Disclaimer Screen | Maserati disclaimer screen exposes the comfort controls | 相符 |
| `-006` | `SWE1-HMI-PM-004` | Lower Comfort Screen Exception for Maserati | Comfort controls suppressed on Maserati disclaimer when the lower comfort screen is fitted | 相符 |
| `-007` | `SWE1-HMI-PM-005` | Pop-up Suppression during Disclaimer Screen | Pop-ups withheld until the disclaimer screen is removed while its audio still plays | 相符 |
| `-008` | `SWE1-HMI-PM-022-02` | Disclaimer Screen Display on Power On | Power button to On displays the disclaimer screen | 相符 |
| `-009` | `SWE1-HMI-PM-012` | Start-up and Goodbye Sound Synchronization | Start-up sounds start on driver door close and sync with the animation | 相符 |
| `-010` | `SWE1-HMI-PM-012` | Start-up and Goodbye Sound Synchronization | Goodbye sounds sync on start with the shut-down animation | 相符 |
| `-011` | `SWE1-HMI-PM-013` | Start-up/Goodbye Sound Settings Options | The sound setting offers Always, Once a Day and Never options | 相符 |
| `-012` | `SWE1-HMI-PM-014` | Sound Setting: Always Play | Always plays the sounds every time the startup animation is played | 相符 |
| `-013` | `SWE1-HMI-PM-015` | Sound Setting: Play Once a Day | Once a Day plays the sounds only once per day | 相符 |
| `-014` | `SWE1-HMI-PM-016` | Sound Setting: Never Play | Never plays no start-up or goodbye sound in any situation | 相符 |
| `-015` | `SWE1-HMI-PM-017` | Sound Volume Matching with Entertainment | Sound volume level matches the current entertainment sounds volume | 相符 |
| `-016` | `SWE1-HMI-PM-018-01` | Head Unit Awake Time for Ignition Off Pop-ups | Head unit stays awake at ignition off to display the pending pop-up | 相符 |
| `-017` | `SWE1-HMI-PM-018-01` | Head Unit Awake Time for Ignition Off Pop-ups | FOTA pop-up interaction extends the stay awake time up to ten minutes | **不符** |
| `-018` | `SWE1-HMI-PM-018-02` | Awake Time Extension on FOTA Pop-up Interaction | Accepting the FOTA pop-up starts the update and dismisses the later pop-ups | **不符** |
| `-019` | `SWE1-HMI-PM-018-03` | Pop-up Priority 1: FOTA Update Available | Scheduling an update time displays the later pop-ups | 相符 |
| `-020` | `SWE1-HMI-PM-018-03` | Pop-up Priority 1: FOTA Update Available | Dismissing the update displays the later pop-ups | 相符 |
| `-021` | `SWE1-HMI-PM-018-04` | Pop-up Priority 2: FOTA Wi-Fi Configuration | Charge Now is displayed when the Wi-Fi configuration is complete | 相符 |
| `-022` | `SWE1-HMI-PM-018-04` | Pop-up Priority 2: FOTA Wi-Fi Configuration | Charge Now is displayed after the Wi-Fi configuration pop-up is dismissed | 相符 |
| `-023` | `SWE1-HMI-PM-018-05` | Pop-up Priority 3: XEV Key Off Pop-ups | Dismissing the XEV key off pop-ups shuts the radio down | 相符 |
| `-024` | `SWE1-HMI-PM-001-01` | Startup Animation on Driver Door Close | Splash screen is presented after the startup animation | **部分不符** |
| `-025` | `SWE1-HMI-PM-001-01` | Startup Animation on Driver Door Close | Screen is black when the ignition remains off after the animation | **不符** |
| `-026` | `SWE1-HMI-PM-001-02` | Splash Screen Interruption upon Ignition On | Splash screens are presented when the ignition is turned on during the animation | 相符 |
| `-027` | `SWE1-HMI-PM-011` | Single Splash/Disclaimer per CAN BUS Cycle | Splash and disclaimer screens are shown once per CAN BUS cycle | 相符 |
| `-028` | `SWE1-HMI-PM-006-01` | Start-up Animation Duration and Trigger | Start-up animation starts on driver door close and concludes by three seconds | 相符 |
| `-029` | `SWE1-HMI-PM-006-02` | Shut-down Animation Duration | Shut-down animation begins playing and concludes within ten seconds | 相符 |
| `-030` | `SWE1-HMI-PM-006-03` | Shut-down Animation Trigger Conditions | Shut-down animation begins only on key off combined with radio UI shut down | 相符 |
| `-031` | `SWE1-HMI-PM-007` | Start-up Animation Skip on Door Removal | No start-up animation is shown when the doors are removed | 相符 |
| `-032` | `SWE1-HMI-PM-008-01` | Single Animation per CAN BUS Wake Up | Animation is played only once while the ignition cycle has not changed | **不符** |
| `-033` | `SWE1-HMI-PM-008-02` | Animation Skip on Open Door Ignition | Animation is skipped when the ignition is turned on with the door open | 相符 |
| `-034` | `SWE1-HMI-PM-009-01` | Screen Behavior on Door Close (Radio OFF) | Animation and splash play with the screen black when the last state is Radio OFF | 相符 |
| `-035` | `SWE1-HMI-PM-009-02` | Animation Skip on Power Button Press | No start-up animation is shown when the power button is pressed on | 相符 |
| `-036` | `SWE1-HMI-PM-010` | Multi-Screen Animation Synchronization | Start-up animation syncs across all capable screens | 相符 |
| `-037` | `SWE1-HMI-PM-010` | Multi-Screen Animation Synchronization | Animations on all screens stop when the animation is interrupted | 相符 |

### 5.1 五處不符 —— **停止條件 8 觸發，我未自行改**

| tc | leaf 之 `requirement_title` | 我寫的 TC | 問題 |
|---|---|---|---|
| **`-017`** | `-018-01` = `Head Unit Awake Time for Ignition Off Pop-ups` | FOTA 互動延長喚醒 | **其應在 `-018-02`**（`Awake Time Extension on FOTA Pop-up Interaction`） |
| **`-018`** | `-018-02` = `Awake Time Extension on FOTA Pop-up Interaction` | 接受 FOTA popup → 開始更新 | **其應在 `-018-03`**（`Pop-up Priority 1: FOTA Update Available`） |
| **`-024`** | `-001-01` = `Startup Animation on Driver Door Close` | splash 於動畫後呈現 | **leaf 之標的為動畫，本條之標的為 splash**（其 ER1 涵蓋動畫，惟主標的偏移） |
| **`-025`** | `-001-01` = `Startup Animation on Driver Door Close` | 點火維持關閉 → 螢幕黑 | **與該 title 無交集** |
| **`-032`** | `-008-01` = `Single Animation per CAN BUS Wake Up` | 動畫於同一 **ignition cycle** 內只播一次 | **037 取 `CAN BUS Wake Up` 為單位，我取 `ignition cycle`** —— 我在其 reasoning 中明言「不斷言二者等價」，**而 037 已經替我選了** |

**我未自行改**，其理由二項：

1. **`-017`／`-018` 之更正是 leaf 之重新指派**，其動到 batch 3
   —— 而 **batch 3 已於 31 包覆核通過**。改之即重開一個已結之批。
2. **`-024`／`-025` 之更正有兩條路而其選擇非我可決**：
   改 TC 之射程以就 title（則 SU1 之 splash 呈現與黑螢幕二句**無 leaf 可歸**），
   或維持 TC 而承認 037 之 title 未涵蓋該二句（則為 037 之缺口）。
   **前者會製造新缺口，後者是對 RD 提出異議 —— 二者皆須裁。**

> **`-032` 我傾向改為 `CAN BUS wake up`** —— 037 為需求單位之權威（canon §8.2），
> 其已作出選擇，我之「不斷言等價」在該選擇面前失去理由。**惟仍待裁。**

### 5.2 一項附帶所得

**本欄一加上去，五處問題立刻現形，而其中二處（`-017`／`-018`）在 batch 3 已覆核通過之後。**
**R-PMH125 之增欄本身就是一次有效的檢查** —— 而**它不是一個檢查程式**，
**沒有任何 must-hit 會攔它**，其效力全繫於有人去逐條讀。

---

## 6. 步驟 6 —— must-hit 母體之一般化（R-PMH124）＋ **⚠ 停止條件 9 字面觸發**

| | 原（32 包） | 現 |
|---|---|---|
| 母體之來源 | 寫死之列舉 `("batch01","batch02","batch03","batch04")` | **glob `generated/batch*.json`** |
| 今日之規模 | 4 批 | **4 批** |

**停止條件 9 逐字：「步驟 6 之母體規模未變（依 R-PMH124 即為未竟）」→ 字面觸發。**

**而其目的未觸發**，理由：

- **32 包已把列舉補為四批**（其為當時之「未竟」之修補），
  故本輪之一般化所改者為**母體之來源**，非其今日之內容；
- **規模不變是因為列舉在今日恰好是完整的** ——
  **其差別在第五批出現時才可觀測**：glob 會自動納入，列舉不會。

**兩面並陳，處置待裁。**

> **另一項數字須分辨**：本輪之 must-hit 項數由 **33 → 22**
> （7＋12＋3），**其減少來自 §2 之限定由 14 筆減為 3 筆，與本步之一般化無關。**

實跑：

```
--- batch01：1 條／7 項 ---
--- batch02：6 條／12 項 ---
--- batch03：0 條／0 項 ---（其限定在 pre_conditions，明白印出，不冒充通過）
--- batch04：3 條／3 項 ---
刪去 22/22 皆 FAIL: True；重複 FAIL: True；一步三項 FAIL: True
```

---

## 7. lint 全跑 ＋ 檢查項數 32

```
batch01 → 32/32 PASS    batch02 → 32/32 PASS
batch03 → 32/32 PASS    batch04 → 32/32 PASS
--limit-must-hit → 22/22    --final-step-must-hit → 5/5 FAIL、範圍向 PASS
```

**新增檢查程式 0、新增檢查項 0** —— apparatus 維持凍結（§四已判 `input_test_data` 不解凍）。

---

## 8. 檢查總表（程式產生，R-PMH92）

**未註冊 must-hit 而標「未實測」者 = 4**（不變）。`verdict_form` **0 failure**。

---

## 9. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手；R-PMH111 之條件式 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（5 問，擬增第六問）** | 否 |

---

## 10. 本包是否仍有該驗而未驗者 —— **有**

1. **`requirement_title` 一加上去就抓到五處，而 batch 1／2／3 之其餘 23 條我只做了「讀起來相符」之判斷。**
   **那是我一個人讀一遍的結果，與 32 包我判「十四條沒問題」是同一種動作** ——
   而那一次錯了三項。**這一欄值得再由你讀一次，不是由我。**
2. **`-032` 之單位問題可能不只一處** —— 037 之 title 在多處指定了單位與範圍
   （`per CAN BUS Wake Up`／`per CAN BUS Cycle`／`Ignition Off`），
   **我只逐條比對了「射程」，未逐條比對「單位」**。
3. **限定之逐條導出我只對 `SU9.)`／`SU9.1)` 做了** ——
   batch 1 之七項、batch 2 之十二項**是在 R-PMH126 之前寫的，其是否亦為樣板，本包未查**。
   **R-PMH126 是一條通則，而我只把它施於本批。**
4. **A-PMH28（流程圖之五類行為）仍全數無 TC 覆蓋** ——
   下放包 §九提案併入 `DR-PMH8` 第六問，**本包未執行**（其未在作業步驟內）。
5. **`-024`／`-025` 之處置若採「承認 037 之 title 未涵蓋該二句」，
   則 `SU1.)` 之 splash 呈現與黑螢幕二句成為 RD 之缺口** ——
   **那是對上游 RD 的異議，本 feature 至今未曾提出過此類異議**，其形態未有前例。

---

## 11. 建議之 commit（**未執行**）

```
feat(power_moding): package 33 — batch 4 rework (limits derived per TC), requirement_title column, NA alignment
```

pathspec（**17 路徑** —— **含 32 包**，其覆核不通過而異動仍在工作區）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/data/layer3_sections.tsv
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/32_batch4.md
features/power_moding/docs/handoff/33_batch4_rework.md
features/power_moding/docs/upstream/32_batch4.md
features/power_moding/docs/upstream/33_batch4_rework.md
features/power_moding/generated/batch03.json
features/power_moding/generated/batch04.json
features/power_moding/scripts/check_table.py
features/power_moding/scripts/gen_batch03.py
features/power_moding/scripts/gen_batch04.py
features/power_moding/scripts/lint_batch.py
features/power_moding/scripts/spec_assertion_scan.py
features/power_moding/scripts/verdict_form.py
```

### 11.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| apparatus | **維持凍結** —— 新增程式 0、新增檢查項 0；一處**一般化**（must-hit 母體之來源） |
| **停止條件 8** | **觸發** —— 五處射程不符，**我未自行改**，兩條路皆須裁 |
| **停止條件 9** | **字面觸發**（規模未變），目的未觸發，兩面並陳 |
| 與下放包不同之處 | **三處**：限定筆數 3 vs 5（§2.2）；`-023` 狀態詞（§4.1）；`NA` 之批數與條數（§3） |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT` |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
