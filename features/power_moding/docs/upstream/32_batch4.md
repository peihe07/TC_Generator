# 上繳包 32 —— batch 4（兩個 Test Set，12 leaf → 14 條）、章 7 全枚舉、A-PMH04 之重驗

- 日期：2026-08-25
- 下放包：[handoff/32_batch4.md](../handoff/32_batch4.md)
- **零寫回工作簿**；`workbook_state = BLANK` 未變

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH119～121 **3/3 逐字相符**；**R-PMH121 標「待 Pei 核可」，未生效** |
| 2 `-002` 之落實 | **已於上一輪執行，本輪為複驗** —— 六項逐項實測相符（見 §2） |
| 3 章 7 規格側全枚舉 | **28/28，未判定 0**；`splash_anim` 全文 **38 行**，**牴觸 0** |
| 4 A-PMH04 之重驗 | **停止條件 8 未觸發**；**惟查出 A-PMH28**（流程圖載有散文所無之行為） |
| 5 batch 4 之產出 | **14 條 TC 自 12 leaf，2 個 Test Set**，lint **32/32** |
| 6 lint 全跑 | **四批皆 32/32**；**檢查項數維持 32** |
| **停止條件 7** | **⚠ 觸發** —— 字面觸發、目的未觸發，兩面並陳（§5.2） |
| 停止條件 8／9 | **未觸發** |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中數 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH119 | R-PMH117 核可生效 | 546 | `91d4d92a801d8bc3` | `91d4d92a801d8bc3` | 1 | ✅ |
| R-PMH120 | 收尾計畫 ＋ 覆核循環上限二輪 | 520 | `7e0e469a04b1b50a` | `7e0e469a04b1b50a` | 1 | ✅ |
| R-PMH121 | DR 未覆之交付截止規則（**待核可**） | 481 | `04cdd9167e63da4b` | `04cdd9167e63da4b` | 1 | ✅ |

---

## 2. 步驟 2 —— **複驗而非重做**

R-PMH119 之連帶**已於 31 包之後、Pei 逐字「核可」之當輪執行完畢**。
本輪逐項實測：

| 連帶 | 實測 |
|---|---|
| `N_LEAF` | **46** |
| 台帳未 excluded 之 leaf | **46**（48 列 − `-002` − `-028`） |
| `EXCLUDED` 標記 | `-002` → `EXCLUDED-BY-R-PMH117`；`-028` → `EXCLUDED-BY-R-PMH72` |
| `Power Transitions` 組 | **6**；八組合計 **46** |
| G1–G5 | `8/46 = 0.1739`／`min = 2`／零命中／`9/46 = 0.1957`／逸出 0 —— **全 PASS** |
| `--self-test`／`--check-doc-sync` | **exit 0／exit 0** |

**本條之抄錄為其追認，非其觸發** —— 已於 `RULINGS.md` 之核對表下方具名。

### 2.1 ⚠ A-PMH27 之狀態詞與下放包不同

步驟 2 逐字令改為 `RESOLVED（Pei 核可 2026-08-25）`。**我用 `ACCEPTED（Pei 核可 2026-08-25，經裁定不寫入）`。**

**理由**：本 anomaly 之**事實未消失** —— `SU1.1)` 之行為仍定義於 CFTS009，
本 feature 仍不持有該文件，該行為仍**不會有任何一條 TC 驗到**。
裁定所改變者是**我方之處置**，不是**該缺口本身**。

**前例**：R-PMH74 對 A-PMH14 新漏 1 之處置逐字為
「**不撤銷** —— 其狀態改為 `ACCEPTED（經裁定不補）`」—— 同一形態。

**且 R-PMH121(c) 取後者方能成立**：交付揭露清單須列停手三筆「其停手依據與所需之上游輸入」——
**若其狀態為 `RESOLVED`，該筆即無理由出現在一份「已知未決清單」上。**

**一句話可反轉。** 差別：`RESOLVED` 讀作「此事已了」，`ACCEPTED` 讀作「此事仍在，而我方已決定承擔」。

---

## 3. 步驟 3 —— 章 7 之規格側全枚舉

| 項 | 數 |
|---|---|
| 章 7 之敘述行區間 | **L282–L309** |
| 其非空行（母體） | **28** |
| `splash_anim` 關鍵詞命中（章 7 內） | 17 |
| **未命中而逐行判定** | **11** |
| **未判定** | **0** |

**`splash_anim` 斷言之全文掃描**（母體為 PDF 全文之關鍵詞命中）：
**38 行，記法分布 {'未對照': 20, '印證': 22, '待定義': 19}（含章 7 補判之 23 行）**，**未具名 0**、**牴觸 0**。

**矩陣側**：174 格全枚舉，**入選 0**（全簿無 `animation`／`splash` 之任一詞），
174 格全記 `未對照`；分類錯誤稽核 **0** 格。

---

## 4. 步驟 4 —— A-PMH04 之重驗

### 4.1 停止條件 8 —— **未觸發**

A-PMH04 之六則圖片佔位 outline 為 `2.1`／`3.1`／`4.1`／`5.1`／`6.1`／`12.4`，
**無一落在 7.5～7.8**；batch 4 之 **12 leaf 全部在 p8 且皆有散文來源**
（`SU1.)`／`SU4.)`／`DS4.1)`／`SU5.)`／`SU6.)`／`SU7.)`／`SU8.)`）。

**故「有 leaf 之內容只在 p3–p7 之流程圖而無其他來源」不成立。**

### 4.2 ⚠ 惟本輪首次讀該六張圖之**文字層**，查出 **A-PMH28**

下放包 §4.2(c) 逐字指出「14 包曾測得『48 leaf 無一落在 p3–p7』，
**惟該量測之單位為 leaf 之頁次，非其內容之來源**」。**依此重驗，所得如下**：

| 逐字（流程圖文字層） | 散文之對應 |
|---|---|
| `If vehicle supports more than 1 Splash screen, toggle them one after another with a 1.5 timeout each` | **`toggle them one after another` 於散文 0 命中** |
| `If vehicle supports only one Splash screen` | 該一對多分支散文未分述 |
| `Ignition ON or Ign. OFF > 3 sec.` ／ `Ignition ON ≤ 3 sec.` | **該 3 秒分支散文無** |
| `ON OR Recall Last and Last = ON`／`OFF OR ... Last = OFF` | `Recall Last` 之判準散文無 |
| `If disclaimer screen is skipped see CFTS009 for Instant ON` | 指向 CFTS009（未持有） |

**其記法為 `待定義` 而非 `牴觸`** —— 其與散文**不取相反值，而是散文所無**；
且**流程圖是否為規範性來源未經裁定**（A-PMH04 提案 (a) 至今未裁）。

**其效力**：batch 4 **不斷言** splash 之輪替順序、張數判準與 3 秒分支（§8.4.1），
**該等行為因而無任何 TC 覆蓋**。

> **⚠ 本項與 A-PMH18／`DR-PMH5` 為同一形態** —— 一份看起來有規範性之素材
> 其地位未定，而其內容落在我方射程內。
> **其差別在於：p9 之來源不明，而本項之來源就在同一份 PDF 內。**

---

## 5. 步驟 5 —— batch 4 之產出

### 5.1 範圍與拆分

| Test Set | leaf | TC |
|---|---|---|
| `Splash Screen` | 3（`-001-01`／`-001-02`／`-011`） | **4** |
| `Startup Animation` | 9 | **10** |

**兩處拆分**（皆依 profile §4 與 canon §8.2.2）：
`-001-01` 拆 2（點火維持關閉 → 黑螢幕 ／ 正常序列 → splash，**其預期結果相反**）；
`-010` 拆 2（開機同步 ／ 中斷停止，**兩個獨立觸發**）。

### 5.2 ⚠ **停止條件 7 —— 字面觸發，目的未觸發**

下放包停止條件 7 逐字：「`-001-01`／`-001-02` 之 `source_clause` **未含 `SU1.)` 之漏句子句**」。

**實測**：

| tc | leaf | 含 `after the animation (3 sec) a splash screen is presented timeout (1.5 each).` |
|---|---|---|
| `-024` | `-001-01` | **是** |
| `-025` | `-001-01` | 否 |
| `-026` | `-001-02` | 否 |

**字面：觸發**（三條中二條不含）。

**而我進一步量測了「哪些句子真的漏」**（SYS1 outline 7.1 之 `Description` 全文）：

| 子句 | SYS1 命中 |
|---|---|
| `after the animation (3 sec) a splash screen is presented timeout (1.5 each).` | **0** ← A-PMH03 |
| `If ignition remains off after animation, screen is black.` | **1** |
| `If ignition is turned on during animation, splash screen(s) are presented (1.5 sec timeout each).` | **1** |

**只有一句真的漏，而它已由 `-024` 承載。** `-025`／`-026` 之來源句在 SYS1 中俱在。

**目的：未觸發。**

**我未以目的覆蓋字面**（R-PMH77(c)）——
**我沒有把該子句補進 `-025`／`-026` 之 `source_clause`**：
那會使追溯欄記載一個該條並未驗證之句子，**是把檢查做綠而不是把事做對**。
**兩面並陳，處置待裁。**

### 5.3 事件層限定（R-PMH55(c)）—— 十四條各一項

`SU9.1)` 逐字載「於 splash 或免責畫面期間按 Power Off／Screen Off 硬鍵**會重設逾時**」，
與本批之逾時斷言**同謂詞取相反值**且條件互斥未證（R-PMH84）。

**其為測試員之動作 → 置於 procedure**（canon §4.5）——
**對照 R-PMH113 之「無通話進行中」為狀態 → 置於 pre_condition。**
**限定之位置由其型別決定**（R-PMH113 之同一原則）。

> ⚠ **`-035`（按電源鍵開機）之限定與其動作看似衝突** —— 步驟 1 禁的是
> **Power Off／Screen Off 硬鍵**，步驟 2 按的是**電源鍵之 On**；`SU9.1)` 之標的為前者。
> **該區別已於其 reasoning 具名。**

### 5.4 `DS4.1)` 之前綴（下放包 §4.2(b)）

`-031` 之 `test_item` 上半照原文抄 **`DS4.1)`**，**未代以 `SU4.1)`**（canon §4.3.1）。
其為 A-PMH11 所登記之疑似原文筆誤，依 R-PMH26 只登記不開 DR。

### 5.5 十四條之全文

#### `NR1L-DisclaimerScreen-024` — Splash screen is presented after the startup animation

- **leaf**：`SWE1-HMI-PM-001-01`　**Test Set**：`Splash Screen`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **軸**：路徑：點火開啟下之正常序列（對 -025 之點火維持關閉）
- **`source_clause`**（`spec_pdf p8`）：`SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), after the animation (3 sec) a splash screen is presented timeout (1.5 each).`

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
- **軸**：等價類：點火於動畫後維持關閉（對 -026 之動畫期間開啟）
- **`source_clause`**（`spec_pdf p8`）：`If ignition remains off after animation, screen is black.`

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The driver door is open and the ignition is off
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and let the animation finish
3. Check that the screen is black after the animation
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The startup animation finishes with the ignition still off
3. The screen is black
```

#### `NR1L-DisclaimerScreen-026` — Splash screens are presented when the ignition is turned on during the animation

- **leaf**：`SWE1-HMI-PM-001-02`　**Test Set**：`Splash Screen`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **軸**：等價類：點火於動畫期間開啟（對 -025 之維持關閉）
- **`source_clause`**（`spec_pdf p8`）：`If ignition is turned on during animation, splash screen(s) are presented (1.5 sec timeout each).`

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
- **軸**：計次單位：CAN BUS cycle（對 -032 之 ignition cycle）
- **`source_clause`**（`spec_pdf p8`）：`SU8.) Show the splash screen and disclaimer screen once per CAN BUS cycle`

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
- **軸**：動畫別：啟動動畫之時序（對 -029 之關機動畫）
- **`source_clause`**（`spec_pdf p8`）：`SU4.) If start-up animation is supported, it shall start upon driver door close, and conclude by 3 seconds.`

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The driver door is open
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and record the animation start time
3. Record the animation end time
4. Check that the animation concluded within three seconds
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The start-up animation starts when the driver door is closed
3. The animation end time is recorded
4. The animation concludes by three seconds
```

#### `NR1L-DisclaimerScreen-029` — Shut-down animation begins playing and concludes within ten seconds

- **leaf**：`SWE1-HMI-PM-006-02`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **軸**：動畫別：關機動畫之時序（對 -028 之啟動動畫）
- **`source_clause`**（`spec_pdf p8`）：`If shut-down animation is supported, it shall begin playing and conclude within 10s.`

**pre_conditions**

```
1. Shut-down animation is supported on this vehicle
2. The head unit is on
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Trigger the shut-down animation and record its start time
3. Record the animation end time
4. Check that the animation concluded within ten seconds
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The shut-down animation begins playing
3. The animation end time is recorded
4. The animation concludes within ten seconds
```

#### `NR1L-DisclaimerScreen-030` — Shut-down animation begins only on key off combined with radio UI shut down

- **leaf**：`SWE1-HMI-PM-006-03`　**Test Set**：`Startup Animation`　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1
- **軸**：謂詞：關機動畫之觸發組合（對 -028／-029 之時序）
- **`source_clause`**（`spec_pdf p8`）：`Begin shut down animation only when you have the combination of a KEY OFF and radio UI shut down.`

**pre_conditions**

```
1. Shut-down animation is supported on this vehicle
2. The ignition is on and the radio UI is running
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Turn the key off without shutting the radio UI down
3. Shut the radio UI down and read the display
4. Check that the animation began only after both had occurred
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The shut-down animation does not begin on key off alone
3. The shut-down animation begins after the radio UI shuts down
4. The animation began only once both conditions had occurred
```

#### `NR1L-DisclaimerScreen-031` — No start-up animation is shown when the doors are removed

- **leaf**：`SWE1-HMI-PM-007`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **軸**：等價類：門被移除／不存在（其對立類無專條，見 reasoning）
- **`source_clause`**（`spec_pdf p8`）：`DS4.1) If doors are removed/not present and ignition is turned to ACC, RUN, or START, do not show Start Up Animation and jump directly to Splash screen.`

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The doors are removed or not present
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Turn the ignition to ACC, RUN or START and read the display
3. Check that the display went directly to the splash screen
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. No start-up animation is shown
3. The display goes directly to the splash screen
```

#### `NR1L-DisclaimerScreen-032` — Animation is played only once while the ignition cycle has not changed

- **leaf**：`SWE1-HMI-PM-008-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **軸**：路徑：同週期內重複觸發（對 -033 之點火轉 ACC/RUN/START）
- **`source_clause`**（`spec_pdf p8`）：`SU5.) If ignition cycle has not changed the animation should only be played once.`

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The animation has already been played once in this ignition cycle
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Reopen and close the driver door in the same ignition cycle
3. Check that the animation is not played a second time
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The driver door is closed again within the same ignition cycle
3. The animation is not played a second time
```

#### `NR1L-DisclaimerScreen-033` — Animation is skipped when the ignition is turned on with the door open

- **leaf**：`SWE1-HMI-PM-008-02`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **軸**：等價類：門開著時點火開啟（對 -032 之同週期重複門關閉）
- **`source_clause`**（`spec_pdf p8`）：`-- If vehicle ignition is turned to ACC, RUN or START ON with the door open, the animation screen shall be skipped and start from applicable splash screen.`

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The driver door is open
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Turn the ignition to ACC, RUN or START with the door open
3. Check that the display starts from the applicable splash screen
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The animation screen is skipped
3. The display starts from the applicable splash screen
```

#### `NR1L-DisclaimerScreen-034` — Animation and splash play with the screen black when the last state is Radio OFF

- **leaf**：`SWE1-HMI-PM-009-01`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **軸**：路徑：最後狀態為 Radio OFF（對 -035 之按電源鍵開機）
- **`source_clause`**（`spec_pdf p8`）：`SU6.) If last state is Radio OFF, play startup animation and show applicable splash screens when driver door closed then screen remains black.`

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The last state of the radio is OFF and the driver door is open
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and record the animation and splash screens
3. Check that the screen remains black afterwards
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The startup animation plays and the applicable splash screens are shown
3. The screen remains black
```

#### `NR1L-DisclaimerScreen-035` — No start-up animation is shown when the power button is pressed on

- **leaf**：`SWE1-HMI-PM-009-02`　**Test Set**：`Startup Animation`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **軸**：等價類：按電源鍵開機（對 -034 之門關閉）
- **`source_clause`**（`spec_pdf p8`）：`When Power Button is pressed On do not show Start Up Animation.`

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The head unit is off
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Press the power button to turn the head unit on
3. Check that no start-up animation is shown
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The head unit turns on
3. No start-up animation is shown
```

#### `NR1L-DisclaimerScreen-036` — Start-up animation syncs across all capable screens

- **leaf**：`SWE1-HMI-PM-010`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **軸**：觸發：開機時之跨螢幕同步（對 -037 之中斷）
- **`source_clause`**（`spec_pdf p8`）：`SU7.) Start up animation should sync on start up with all capable screen's start up animation.`

**pre_conditions**

```
1. Start-up animation is supported on more than one screen in this vehicle
2. The driver door is open
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and record each screen's animation start
3. Check that the animations started in sync with each other
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The start-up animation starts on every capable screen
3. The animations on all capable screens are in sync on start up
```

#### `NR1L-DisclaimerScreen-037` — Animations on all screens stop when the animation is interrupted

- **leaf**：`SWE1-HMI-PM-010`　**Test Set**：`Startup Animation`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1
- **軸**：觸發：動畫被中斷（對 -036 之開機同步）
- **`source_clause`**（`spec_pdf p8`）：`Animations on all screens should stop (refer to logic for specific behavior) during any interruptions of animation (timeout, ignition button press).`

**pre_conditions**

```
1. Start-up animation is supported on more than one screen in this vehicle
2. The start-up animation is playing on every capable screen
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Interrupt the animation with an ignition button press
3. Check that the animations stopped on all screens
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The animation is interrupted by the ignition button press
3. The animations on all screens stop
```


---

## 6. lint 全跑 ＋ 檢查項數 32 之證明

```
batch01 → 32/32 PASS    batch02 → 32/32 PASS
batch03 → 32/32 PASS    batch04 → 32/32 PASS
--limit-must-hit → 刪去 33/33 皆 FAIL（batch01 7 ＋ batch02 12 ＋ batch04 14；batch03 之 limits 為空）
--final-step-must-hit → must-hit 5/5 FAIL；範圍向 PASS；`Compare` 邊界二例
```

### 6.1 ⚠ 一項自查：must-hit 之母體原本漏了 batch 4

**上繳草稿一度寫成「33/33」而實測為 `19/19`** —— `--limit-must-hit` 之迴圈
寫死為 `("batch01", "batch02")`，**batch 3／4 之限定從未進過該錨點**。
**我在報出之前自己量了一次才發現。**

**已依 R-PMH107 補入**（既有檢查對新資料之適用，為義務，非新增檢查項）：
迴圈改為四批；**`batch03` 之 `limits` 為空**（其限定在 `pre_conditions`，
不受 R-PMH99(c) 之字串檢查所管），**該空值明白印出，不冒充通過**。

**現值：刪去 33/33 皆 FAIL（7 ＋ 12 ＋ 14），重複 FAIL，一步三項 FAIL。**

> **此即 28 §5.2 一般化之未竟處**：當時把 `test_set` 與 leaf 覆蓋改為讀宣告，
> **而 must-hit 之批次清單仍是寫死的** —— 一般化只做了一半，兩包之後才被發現。

### 6.2 一項一般化（R-PMH107，下放包 §4.4(c) 已預告）

| | 原 | 現 |
|---|---|---|
| 判準 | 各 TC 之 `test_set` == `d["test_set"]`（**該批一個值**） | 各 TC 之 `test_set` ∈ `d["test_sets"]`（**該批之宣告，得為多值**） |
| 對 batch 4 | **必 FAIL**（兩值） | 通過 |
| 檢查之種類 | 各 TC 之 test_set 須合於該批之宣告 | **不變** |

**`chk(...)` 呼叫數未變 —— 檢查項數維持 32。停止條件 9 未觸發。**

### 6.3 ⚠ 三處跨軸指涉被迫改寫，其代價須具名

R-PMH53 之檢查以**兩條之 `distinguishing_axis` 是否共用詞**為判準。
故**跨軸之指涉必被判為不相容**（如「動畫之 3 秒屬另一條之標的」——
其軸為「動畫別」而本條之軸為「路徑」）。

本批之三處跨軸指涉因而**以描述指名而不用 `tc_id`**（如「本批啟動動畫時序條」）。
**其代價**：該三處失去機器可追之指標。

**另一處為 `-031`**：其 axis 原寫「對 `-028` 之正常門關閉」而 `-028` 之軸為「動畫別」，
不共用詞。**改寫後其 axis 逐字載「其對立類無專條」** ——
**該不對稱是真的**：本批各動畫條皆以門正常關閉為**前提**而不驗其為一個等價類。

---

## 7. 檢查總表（程式產生，R-PMH92）

新納入二列：`lint_batch.py generated/batch04.json`、
`spec_assertion_scan.py --assertion splash_anim`（**既有檢查對新資料之適用，R-PMH107**）。

`verdict_form.py`：母體 **1646** 項（本輪納入 `IGNOFF`／`SPLASH` 二表），**0 failure**。
**未註冊 must-hit 而標「未實測」者 = 4**（不變）。
**apparatus 維持凍結** —— 本包新增檢查程式 **0**、新增檢查項 **0**。

---

## 8. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手；R-PMH111 之條件式續行 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（5 問）** | 否 —— **其載有 R-PMH112 之更正，未發出期間該不符持續存在** |

---

## 9. 本包是否仍有該驗而未驗者 —— **有**

1. **十四條又是我寫的，又沒有人讀過。** 四批之中三批在 lint 全綠後被判產出面須改
   （12／29／31 包）。**R-PMH120 給每批二輪，而 batch 4 是本 feature 至今單批最大的一批
   （14 條、兩個 Test Set、12 leaf）** —— **二輪是否夠，我沒有把握，這句話現在就先講。**
2. **A-PMH28 之五類流程圖行為全部無 TC 覆蓋**，而其中 `toggle them one after another`
   **直接落在 `-024`／`-026` 之標的內**。其未被斷言之理由是「流程圖之規範性未裁」——
   **而那個未裁已經從 01 包放到現在（A-PMH04 之提案 (a)）。**
3. **`-006-01`／`-02`／`-03` 之三分（啟動時序／關機時序／關機觸發組合）是我的讀法。**
   三 leaf 共用 outline 7.5 且 `section_title` 完全相同，**037 依何而分，台帳沒有記**。
   若其原意之分法不同，三條之對應即錯位。
4. **`-030` 之反向順序未驗** —— `SU4.)` 以 `even not simulteneously` 涵蓋兩種順序而只舉一例，
   本條取其例；**先關 radio UI 後 key off 之順序未驗**。
5. **`-037` 之 `timeout` 中斷未驗** —— 權威文本舉二例（`timeout, ignition button press`），本條取後者。
6. **章 7 之全枚舉只做了 28 行之散文區** —— **p3–p7 之流程圖行雖已入 `splash_anim` 之判定表，
   但那是關鍵詞命中之子集**；流程圖之非命中行（如 `System Loading`／`Black Screen`／`5 secs`）
   **未逐行判定**。**其母體我沒有量。**
7. **`-025`／`-026` 之 `source_clause` 不含漏句子句一事已具名待裁**（§5.2）。

---

## 10. 建議之 commit（**未執行**）

```
feat(power_moding): package 32 — batch 4 (14 TCs, 2 test sets), ch7 spec-side enumeration, A-PMH28
```

pathspec（**12 路徑**）：

```
features/power_moding/ANOMALIES.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/32_batch4.md
features/power_moding/docs/upstream/32_batch4.md
features/power_moding/generated/batch04.json
features/power_moding/scripts/check_table.py
features/power_moding/scripts/gen_batch04.py
features/power_moding/scripts/lint_batch.py
features/power_moding/scripts/spec_assertion_scan.py
features/power_moding/scripts/verdict_form.py
```

### 10.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| apparatus | **維持凍結** —— 新增程式 0、新增檢查項 0；**二處一般化**（`test_set` 讀法；must-hit 之批次母體） |
| 計數之變更 | **無** —— `N_LEAF` 於上一輪已改為 46，本輪只複驗 |
| **停止條件 7** | **字面觸發**，未以目的覆蓋之，處置待裁 |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT` |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
