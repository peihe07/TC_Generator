# 上繳包 35 —— DESC 完整涵蓋之一次性總結，追溯維度封閉

- 日期：2026-08-25
- 下放包：[handoff/35_desc_closing_pass.md](../handoff/35_desc_closing_pass.md)
- **零寫回工作簿**

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH133～135 **3/3 逐字相符** |
| **2 DESC 逐斷言涵蓋表** | **42 斷言／30 leaf；未涵蓋（本 leaf）= 2**；已知四處全數出現於表中 → **停止條件 7 未觸發** |
| **3 回溯重判** | 母體 **25** 項「素材不足」陳述；**翻案 2**（A-PMH25 已翻 ＋ **新查出 `-003`**） |
| 4 七處修正 | 三處改內容、二處只登記、六條補具名、三條補引 R-PMH131 |
| 5 全批重跑 | **四批皆 32/32**，全套錨點通過 |
| 6 `DR-PMH8` | **8 問 ＋ 首段更正句**，SHA256 `41926e3de87df5c4`，`DRAFT` |
| 7 `PENDING-ON-DR` | **13 → 14 筆** |
| 停止條件 8 | **未觸發** —— 翻案之二項皆已具名 |
| 停止條件 9 | **未觸發** —— 修正後 1:1 全數維持 |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH133 | DESC 為斷言完整性之權威 | 633 | `8b9afef57405b1d3` | `8b9afef57405b1d3` | 1 | ✅ |
| R-PMH134 | 追溯維度封閉為三項 | 511 | `1a49271c17a82617` | `1a49271c17a82617` | 1 | ✅ |
| R-PMH135 | 新判準之修正不計輪數 | 335 | `77838e4e34085bff` | `77838e4e34085bff` | 1 | ✅ |

---

## 2. 步驟 2 —— DESC 逐斷言涵蓋表（本包核心）

**切分**：以 `(?<=[.;])\s+(?=[A-Z(])` 產生機器候選，再人讀複核（R-PMH101）。
**30 個有 TC 之 leaf → 42 個斷言。**

| leaf | # | DESC 斷言 | 涵蓋之 TC／ER | 註 |
|---|---|---|---|---|
| `SWE1-HMI-PM-001-01` | A1 | When driver door is closed, the system plays a 3-second startup animation. | **未涵蓋（本 leaf）** | 其行為由 `-028` 驗到而該條掛 `-006-01` —— **A-PMH30** |
| `SWE1-HMI-PM-001-01` | A2 | If ignition remains OFF after animation, the system turns the screen black. | `-025` ER2 |  |
| `SWE1-HMI-PM-001-02` | A1 | If ignition is turned ON during the startup animation, the system interrupts the animation and plays splash sc | `-026` ER2／ER3／ER4／ER5 | **本包補 ER2（動畫被中斷）與 ER4（其後進入免責）** |
| `SWE1-HMI-PM-001-03` | A1 | During the Disclaimer screen (content per CFTS009/legal), if the system is not ready, it displays "Loading…". | `-001` ER1 |  |
| `SWE1-HMI-PM-001-03` | A2 | When the system is ready, it removes "Loading…" and shows the Accept button. | `-001` ER3 |  |
| `SWE1-HMI-PM-001-04` | A1 | The system allows the user to either press Accept to go directly to last mode screen, or wait for timeout (whi | `-002` ＋ `-003`（聯集） | ⚠ **DESC 之 `which automatically equals Accept` 未被斷言** —— 35 包步驟 3 之翻案，**待裁** |
| `SWE1-HMI-PM-001-05` | A1 | Exception: For Maserati applications, the system provides no timeout (per CFTS009); the user must manually pre | `-004` ER2／ER3 |  |
| `SWE1-HMI-PM-003` | A1 | SU2.) For Maserati vehicles, while on the disclaimer screen the user will have access to their comfort control | `-005` ER1／ER2 |  |
| `SWE1-HMI-PM-003` | A2 | No timeout is provided for Maserati applications, see CFTS009. | **未涵蓋（本 leaf）** | 其行為由 `-004` 驗到而該條掛 `-001-05` —— **A-PMH30 之第二例** |
| `SWE1-HMI-PM-004` | A1 | SU2.1) Do not display comfort controls on Maserati disclaimer screen when vehicle is equipped with lower comfo | `-006` ER2 |  |
| `SWE1-HMI-PM-005` | A1 | SU3.) No pop-ups will appear until the disclaimer screen has been removed. | `-007` ER4 |  |
| `SWE1-HMI-PM-005` | A2 | If an item like a traffic announcement is received like on this screen the user will begin hearing the announc | `-007` ER3／ER4 |  |
| `SWE1-HMI-PM-006-01` | A1 | If start-up animation is supported, the system shall start it upon driver door close and conclude it within 3  | `-028` ER1／ER3 |  |
| `SWE1-HMI-PM-006-02` | A1 | If shut-down animation is supported, the system shall begin playing it and conclude it within 10 seconds. | `-029` ER1／ER3 |  |
| `SWE1-HMI-PM-006-03` | A1 | The system shall begin shut-down animation only when both KEY OFF and radio UI shut down are present (not nece | `-030` ER1／ER2／ER3 |  |
| `SWE1-HMI-PM-007` | A1 | DS4.1) If doors are removed/not present and ignition is turned to ACC, RUN, or START, do not show Start Up Ani | `-031` ER1／ER2 |  |
| `SWE1-HMI-PM-008-01` | A1 | If the ignition cycle has not changed, the system shall play the animation only once per CAN BUS wake-up upon  | `-032` ER1／ER2 | **本包將計次基準由 `ignition cycle` 改為 `CAN BUS wake-up`** |
| `SWE1-HMI-PM-008-02` | A1 | If the vehicle ignition is turned to ACC, RUN, or START ON while the driver door is open, the system shall ski | `-033` ER1／ER2 |  |
| `SWE1-HMI-PM-009-01` | A1 | If the last state is Radio OFF, the system shall play startup animation and show applicable splash screens whe | `-034` ER1／ER2 |  |
| `SWE1-HMI-PM-009-02` | A1 | When the Power Button is pressed On, the system shall not show the Start Up Animation. | `-035` ER2 |  |
| `SWE1-HMI-PM-010` | A1 | SU7.) Start up animation should sync on start up with all capable screen’s start up animation. | `-036` ER2／ER3 |  |
| `SWE1-HMI-PM-010` | A2 | Animations on all screens should stop (refer to logic for specific behavior) during any interruptions of anima | `-037` ER1／ER2 |  |
| `SWE1-HMI-PM-011` | A1 | SU8.) Show the splash screen and disclaimer screen once per CAN BUS cycle | `-027` ER2／ER4 |  |
| `SWE1-HMI-PM-012` | A1 | SSND 1) If start-up sounds are supported, it will start upon driver door close and sync with the start-up anim | `-009` ER3／ER5 |  |
| `SWE1-HMI-PM-012` | A2 | If goodbye sounds are supported, it shall sync on start with the shut-down animation. | `-010` ER4／ER5 |  |
| `SWE1-HMI-PM-012` | A3 | Sounds will sync amongst all supported vehicle displays. | `-009` ER4（**只涵蓋啟動音側**） | **告別音側未涵蓋 —— A-PMH23** |
| `SWE1-HMI-PM-013` | A1 | SSND 2) Start-up and goodbye sounds shall have a setting with Always/Once a Day/Never options. | `-011` ER2 |  |
| `SWE1-HMI-PM-014` | A1 | SSND 2.1) If the setting is Always, start-up and goodbye sounds should be played everytime the startup animati | `-012` ER3／ER4 |  |
| `SWE1-HMI-PM-015` | A1 | SSND 2.2) If the setting is Once a Day, start-up and goodbye sounds should be played only once per day (i.e ot | `-013` ER3／ER4 |  |
| `SWE1-HMI-PM-016` | A1 | SSND 2.3) If the setting is Never, start-up and goodbye sounds should not be played on any situation. | `-014` ER3／ER4／ER5 |  |
| `SWE1-HMI-PM-017` | A1 | SSND 3) Sound volume level shall match current entertainment sounds volume. [DCR19385]_x000D_ _x000D_ | `-015` ER4／ER5 |  |
| `SWE1-HMI-PM-018-01` | A1 | If there are popups to show at IGN OFF and the user has set Power Accessory Delay to 0 seconds, the system sha | `-016` ER1／ER2／ER6 |  |
| `SWE1-HMI-PM-018-01` | A2 | If the user does not interact with the popup within the 60-second timeout defined in the pop-up list, the syst | `-016` ER4 | **本包新補** —— 原為 `未涵蓋`（A-PMH25 之翻案） |
| `SWE1-HMI-PM-018-01` | A3 | If no other popups remain, the system shall shut off the radio. | `-016` ER5 | **本包新補** |
| `SWE1-HMI-PM-018-02` | A1 | If the user interacts with the FOTA popup, the system shall stay awake until the user has not interacted with  | `-017` ER2 |  |
| `SWE1-HMI-PM-018-02` | A2 | The maximum time the system can stay awake due to these popups is 10 minutes. | `-017` ER3 |  |
| `SWE1-HMI-PM-018-03` | A1 | For Priority 1 (FOTA update available): If the user accepts the FOTA popup, the system shall start the update  | `-018` ER2／ER3 |  |
| `SWE1-HMI-PM-018-03` | A2 | If the user schedules an update time or dismisses the update, the system shall display FOTA via Wi-Fi / Charge | `-019` ＋ `-020`（聯集） |  |
| `SWE1-HMI-PM-018-04` | A1 | For Priority 2 (FOTA via Wi-Fi configuration): If the user chooses to configure Wi-Fi, the system shall displa | `-021` ER1／ER2 |  |
| `SWE1-HMI-PM-018-04` | A2 | If the user chooses to dismiss the Wi-Fi configuration popup, the system shall display Charge Now (if applicab | `-022` ER1／ER2 |  |
| `SWE1-HMI-PM-018-05` | A1 | For Priority 3 (XEV key off popups: Charge Now/Summary, Preconditioning): If the user dismisses any XEV key of | `-023` ER1／ER2／ER3 |  |
| `SWE1-HMI-PM-022-02` | A1 | When the user presses the power button to change to On state, the system shall display the disclaimer screen ( | `-008` ER2／ER3（**主句**） | **其例外 `unless certain phone call scenarios …` 未涵蓋 —— `DR-PMH8` Q8** |

**斷言合計 = 42；未涵蓋（本 leaf）= 2**

### 2.1 停止條件 7 之核驗 —— **已知四處全數出現**

| 已知處 | 於表中之位置 |
|---|---|
| `-016` | `-018-01` **A2／A3**（本包補為 ER4／ER5） |
| `-026` | `-001-02` A1 之「中斷」與「進入免責」（本包補為 ER2／ER4） |
| `-008` | `-022-02` A1 之例外（未涵蓋，Q8） |
| `-025` | `-001-01` **A1**（未涵蓋，A-PMH30） |

**四處皆在 → 本表之切分未漏 → 停止條件 7 未觸發。**

### 2.2 ⚠ 表中另查出**二處先前未知**

| # | 處 | 性質 |
|---|---|---|
| 1 | **`-003` A2**（`No timeout is provided for Maserati applications`） | **037 於兩個 leaf 重複同一行為之第二例** —— 其行為由 `-004` 驗到而該條掛 `-001-05`。**登記為 A-PMH30 之第二例** |
| 2 | `-012` A3（`Sounds will sync amongst all supported vehicle displays`） | **已知**（A-PMH23），惟本表首次使其成為一個**逐斷言之未涵蓋項**而非散文中之備註 |

> **`-001-01` A1 與 `-003` A2 二者之性質須分辨**：
> **其行為皆有 TC 驗到，只是該 TC 掛在另一個 leaf。**
> **二者之別在於追溯，不在於覆蓋。** 依 R-PMH133 於其本 leaf 記 `未涵蓋`，
> **未補 TC**（其為重複驗證）、**未改 leaf 指派**（037 為權威）、**未提異議**（步驟 4 明令）。

---

## 3. 步驟 3 —— 「素材不足」類判斷之回溯重判

**母體之界定**：掃四批之 `reasoning`，取含
`不造值`／`素材不足`／`無法確定`／`破句`／`未給`／`未言`／`未載`／`規格未` 之陳述
—— **25 項**。

**逐項對照 037 之 DESC，翻案 2 項**：

| # | 處 | 原陳述 | DESC 之逐字 | 判 |
|---|---|---|---|---|
| 1 | **`-016`** | 「權威文本於逾時處為破句，其秒數無法確定」 | `within **the 60-second timeout defined in the pop-up list**, the system shall **close the popup**. If no other popups remain, the system shall **shut off the radio**.` | **翻案**（34 包已查出，本包補斷言） |
| 2 | **`-003`** | 「規格未載逾時之秒數，亦**未言逾時等同 Accept**」（13 包 §4.4 之更正） | `or wait for timeout (**which automatically equals Accept**)` | **翻案 —— 本包新查出** |

**其餘 23 項不翻**，其前提於 DESC 側同樣成立（逐項已查）。舉其要者：

| 處 | 未斷言者 | DESC 側 |
|---|---|---|
| `-011` | 設定之所在路徑 | DESC = `SSND 2)` 逐字，**同樣未給路徑** |
| `-013` | 「一日」之起算點 | DESC = `SSND 2.2)` 逐字，**同樣未定義** |
| `-015` | 音量之單位／容差 | DESC = `SSND 3)` 逐字 |
| `-021` | `configuration is complete` 之秒數 | DESC 同樣未給 |
| `-033` | `applicable` 之判準 | DESC 同樣未言 |
| `-036`／`-037` | `sync` 之允差、`refer to logic` 所指 | DESC = `SU7.)` 逐字 |
| **`-008`** | `certain phone call scenarios` 之內容 | **DESC 於同處亦未列舉** → 非 SYS1 側之偏差，**上游本身未定義** → Q8 |

### 3.1 ⚠ `-003` 之翻案，其性質與 A-PMH25 不同

A-PMH25 之成因為 **SYS1 匯出之破句**（同一句話在兩份文件中不一樣）。
**`-003` 之成因為 037 之 DESC 增寫了 PDF 所無之語義**
（`which automatically equals Accept` 於 PDF `SU1.)` 中**不存在**）。

**故 R-PMH133 之分工在此更為要緊**：
**DESC 決定要驗什麼** —— 即使該語義是 037 自己加的。

**`-003` 之修正不在步驟 4 之七處內，且其動到 batch 1** ——
**已於其 `reasoning` 具名並保留原文（R-PMH44），本包未改。**

> **13 包當時之「更正」（不斷言其等同 Accept）在當時是對的** ——
> 其所據為 PDF。**其在今日不對，是因為判準換了來源。**

---

## 4. 步驟 4 —— 七處修正

| # | 處置 | 實作 |
|---|---|---|
| 1 | `-016` 補三斷言 | proc／ER 由 4 增為 **6:6**；新增 ER4（60 秒逾時後 popup 關閉）、ER5（無其他 popup 則 radio 關機）。**A-PMH25 → `RESOLVED`** |
| 2 | `-026` 補二斷言 | proc／ER 由 4 增為 **6:6**；新增 ER2（動畫被中斷）、ER4（其後顯示免責畫面） |
| 3 | `-032` 改計次基準 | `CAN BUS wake-up` 為計次基準（PC3／ER1），**`ignition cycle` 降為 PC2 之前提** |
| 4 | `-025` **不改** | 登記 **A-PMH30**（只記現象） |
| 5 | `-008` **不改** | **`DR-PMH8` 增 Q8** |
| 6 | batch 2 六條 | **只補具名**：各具名其限定所對之該一個 ER（下表），**不重做** |
| 7 | `-026`／`-033`／`-034` | `reasoning` 補引 **R-PMH131**，其「不斷言輪替順序」自此為裁定而非暫置 |

### 4.1 batch 2 六條之具名（R-PMH126 之形式要求）

| tc | 其限定所對之斷言 |
|---|---|
| `-009` | ER3 `The start-up sound starts when the driver door is closed` |
| `-010` | ER4 `The goodbye sound starts at the start of the animation` |
| `-012` | ER3 `The sound was played on both occasions` |
| `-013` | ER4 `The sound was played once and not on the second occasion` |
| `-014` | ER3 `No start-up sound is played when the driver door is closed`（負向） |
| `-015` | ER3 `The start-up sound is played and its volume level is recorded` |

**六條之陳述皆為真**（34 包 §7.1 已逐條實查），**故只補具名**。

### 4.2 三處修正後之全文

#### `NR1L-DisclaimerScreen-016` — Head unit stays awake at ignition off to display the pending pop-up

- **leaf**：`SWE1-HMI-PM-018-01`

**pre_conditions**

```
1. No phone call or projection call is active
2. Power Accessory Delay is set to 0 seconds
3. At least one pop-up from the ignition off list is pending
```

**test_procedure**

```
1. Turn the ignition off and record the head unit power state
2. Read the display and record the pop-up shown
3. Do not interact with the pop-up and record the awake duration
4. Read the pop-up state after the 60-second timeout expires
5. Read the radio power state when no other pop-ups remain
6. Compare the recorded duration with the stated maximum
```

**expected_result**

```
1. The head unit stays awake when the ignition is turned off
2. The pending pop-up is displayed
3. The head unit does not power off while the pop-up is being displayed
4. The pop-up is closed after the 60-second timeout defined in the pop-up list
5. The radio shuts off when no other pop-ups remain
6. The head unit stays awake for no longer than 2.5 minutes
```

#### `NR1L-DisclaimerScreen-026` — Splash screens are presented when the ignition is turned on during the animation

- **leaf**：`SWE1-HMI-PM-001-02`

**pre_conditions**

```
1. Start-up animation and splash screen are supported on this vehicle
2. The driver door is open and the ignition is off
```

**test_procedure**

```
1. Do not press the Power Off or Screen Off hard key
2. Close the driver door and turn the ignition on during the animation
3. Read the display and record whether the animation continues
4. Read the display and record each splash screen and its duration
5. Read the display after the splash screens
6. Check that the splash screens are presented with a 1.5 second timeout
```

**expected_result**

```
1. No Power Off or Screen Off hard key press occurs
2. The ignition is turned on while the animation is playing
3. The animation is interrupted
4. The splash screens are presented
5. The disclaimer screen is displayed after the splash screens
6. Each splash screen times out after 1.5 seconds
```

#### `NR1L-DisclaimerScreen-032` — Animation is played only once while the ignition cycle has not changed

- **leaf**：`SWE1-HMI-PM-008-01`

**pre_conditions**

```
1. Start-up animation is supported on this vehicle
2. The ignition cycle has not changed since the animation was last played
3. The animation has already been played once in this CAN BUS wake-up
```

**test_procedure**

```
1. Reopen and close the driver door in the same CAN BUS wake-up
2. Check that the animation is not played a second time
```

**expected_result**

```
1. The driver door is closed again in the same CAN BUS wake-up
2. The animation is not played a second time
```


---

## 5. 步驟 5 —— 全批重跑（**依 R-PMH135 記為「繫於 R-PMH133」，非重做**）

```
batch01 32/32   batch02 32/32   batch03 32/32   batch04 32/32
--limit-must-hit → 通過      --final-step-must-hit → 通過
verdict_form → 0 failure     check_granularity --self-test → 通過
```

**本次修正繫於 R-PMH133（DESC 為斷言完整性之權威）與 R-PMH134 之維度三（單位）** ——
**依 R-PMH135 不計入 R-PMH120 之輪數上限。**

**其意義之分辨**（R-PMH135 明令）：
**本次是判準變了，不是做錯了** —— `-016` 之不斷言在 30 包當時合於當時之判準（SYS1 為權威文本），
`-003` 之不斷言在 13 包當時合於當時之判準（PDF 為來源）。

---

## 6. 步驟 6 —— `DR-PMH8` 之 Q8

**8 問 ＋ 首段更正句**，SHA256 **`41926e3de87df5c4`**，**狀態 `DRAFT`、`SENT` 欄留空**。

Q8 逐字抄自下放包，未改一字。

---

## 7. 步驟 7 —— `PENDING-ON-DR`（14 筆）

新增第 14 筆：`-008` 之例外未處理，繫於 `DR-PMH8` Q8，第 (3) 欄逐值列出。
**其註記明**：037 之 DESC 於同處亦未列舉 —— 非 SYS1 側之偏差，而是上游本身未定義。

---

## 8. 檢查總表

**新增檢查程式 0、新增檢查項 0**；apparatus 維持凍結。
**未註冊 must-hit 而標「未實測」者 = 4**（不變）。

**追溯維度自本包起封閉為三項**（R-PMH134）：leaf 指派／斷言涵蓋／單位。

---

## 9. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（8 問）** | 否 —— **其載 R-PMH112 之更正，未發出期間該不符持續存在** |

---

## 10. 本包是否仍有該驗而未驗者 —— **有**

1. **回溯重判之母體是我用七個關鍵詞掃出來的（25 項）。**
   **「以素材不足為由而未斷言」不一定用這七個詞寫** ——
   有些判斷根本沒有留下句子（**沒寫的，掃不到**）。
   **本步之偽陰無法量測，其限度於此具名。**
2. **`-003` 之翻案指出一件比 A-PMH25 更麻煩的事**：
   **037 之 DESC 會增寫 PDF 所無之語義。**
   本包只查了「未斷言」之側；**反向之側未查** ——
   **有多少 TC 斷言了 DESC 所無之內容？** 本包未做該方向之比對。
3. **`-016`／`-026` 之補斷言是我寫的文字，未經人讀。**
   本包新增五條 ER 與五個步驟。**其形態與前四批被判產出面不通過者相同。**
4. **A-PMH30 之二處我判為「追溯之事而非覆蓋之事」** ——
   **若交付要求「每 leaf 之每一斷言於該 leaf 上皆有 TC」，該判斷即不成立**，
   二處須補。**其要求為何，未定。**
5. **`-012` A3（告別音之跨螢幕同步）自 29 包登記為 A-PMH23 至今未動** ——
   本表使其成為一個逐斷言之未涵蓋項，**其處置仍待 `DR-PMH8` Q3**。
6. **維度封閉（R-PMH134）之三項，其第 (2) 項「斷言涵蓋」無任何檢查程式承載** ——
   本包之涵蓋表是一次人讀之產物。**下一批（batch 5／6）產出時，
   沒有東西會自動再做一次這張表。**

---

## 11. 建議之 commit（**未執行**）

```
feat(power_moding): package 35 — DESC assertion coverage closed, retro re-judgement, traceability dimensions frozen
```

pathspec（**19 路徑** —— **含 34 包**，其異動仍在工作區）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DATA_REQUESTS.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/data/layer3_sections.tsv
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/34_leaf_realign.md
features/power_moding/docs/handoff/34a_flowchart_and_cutoff.md
features/power_moding/docs/handoff/35_desc_closing_pass.md
features/power_moding/docs/upstream/34_leaf_realign.md
features/power_moding/docs/upstream/35_desc_closing_pass.md
features/power_moding/generated/batch01.json
features/power_moding/generated/batch02.json
features/power_moding/generated/batch03.json
features/power_moding/generated/batch04.json
features/power_moding/scripts/gen_batch01.py
features/power_moding/scripts/gen_batch02.py
features/power_moding/scripts/gen_batch03.py
features/power_moding/scripts/gen_batch04.py
```

### 11.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| 停止條件 | **7／8／9 皆未觸發** |
| apparatus | **維持凍結**；**追溯維度自本包起封閉為三項**（R-PMH134） |
| 輪數 | 本次修正**繫於 R-PMH133**，依 R-PMH135 **不計入 batch 3／4 之二輪上限** |
| 未改而具名者 | `-003`（batch 1，翻案待裁）／`-025`／`-003` A2（A-PMH30）／`-008`（Q8）／`-012` A3（A-PMH23） |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT`（8 問） |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
