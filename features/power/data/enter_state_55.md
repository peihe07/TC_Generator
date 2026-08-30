# `ENTER_<STATE>` 標準片段表（55 包 B2 / R-P354）

> ⚠ **已依 57 包 R-P363 與 58 包 R-P369(c) 更新**（原 55 包 B2 版）。
> 產生依據：CFTS009 文字層錨點 ＋ **`forms/PDT27_E2A_R1_BHCAN2.dbc`**（`46cb73f3…`）之 `VAL_` 列舉。
> 每一片段之末步為 R-P354(a) 所定之確認步，逐字：
> `Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is <raw> (<label>)`
> 套用方式見 R-P354(f)：Pre-Condition 保留 `The HU is in <State> state`，
> Procedure 第 1 步改為 `Apply ENTER_<STATE>`。

## 0. 訊號與 `VAL_` 之出處（R-P354(c) / R-7）

| 訊號 | DBC message | 出處 |
|---|---|---|
| `$STATUS_TELEMATIC.PowerSts_Telematic$` | `BO_ 1470 STATUS_TELEMATIC` | BHCAN2，`VAL_ 1470` |
| `$STATUS_BH_BCM1.OperationalModeSts$` | `BO_ 854 STATUS_BH_BCM1` | BHCAN2，`VAL_ 854` |
| `$STATUS_BH_BCM2.RemStActvSts$` | `BO_ 1132 STATUS_BH_BCM2` | BHCAN2，`VAL_ 1132` |
| `$STATUS_BH_BCM1.PowerModeSts$` | `BO_ 854 STATUS_BH_BCM1` | BHCAN2，`VAL_ 854` |

**判準 DBC**：`forms/PDT27_E2A_R1_BHCAN2.dbc`（sha256 `46cb73f3…`），
與 LID v1_78（`a01e1679…`）、FDCAN8（`2a86c4bf…`）同列 G0 參考資料庫段
（R-P365(c) / R-P368(e)）。**G0 現為 素材 9 / 9 ＋ 參考庫 3 / 3。**
R4 BHCAN 降為**旁證**（R-P368(e)），A-PW349 之遲登與 A-PW356 之未查併記。

### G254 —— 片段訊號複驗（R-P369(c)）

四個訊號在 **BHCAN2 與旁證 R4 之訊息 ID、訊息名、`VAL_` 表全部逐字相同**：

| 訊號 | BHCAN2 | R4（旁證）| FDCAN8 | B-1 衝突 |
|---|---|---|---|---|
| `PowerSts_Telematic` | `1470 STATUS_TELEMATIC` | 同 | `1427 TELEMATIC_FD_4` | **無** |
| `OperationalModeSts` | `854 STATUS_BH_BCM1` | 同 | `256 BCM_FD_2` | **無** |
| `RemStActvSts` | `1132 STATUS_BH_BCM2` | 同 | `256 BCM_FD_2` | **無** |
| `PowerModeSts` | `854 STATUS_BH_BCM1` | 同 | `1066 BCM_FD_9` | **無** |

**G254：六可用片段之每一 `$…$` 在 BHCAN2 皆有 `SG_`；B-1 衝突數 = 0。PASS。**
片段內容因此**一字未改**，僅出處由 R4 改註為 BHCAN2。

⚠ 惟 `ENTER_STANDBY` 之 `Timeout1` 來源 `$PwrAccDelayAct$`
**確為 B-1 衝突**（A-PW357）：LID r1458 解得 `BODY_CNTRL3.Comfort_Enable_Time`，
BHCAN2 無、R4 有、FDCAN8 之訊息名為 `BCM_FD_27`。
**60 包 R-P371 已裁乙**：採 `$BCM_FD_27.Comfort_Enable_Time$`，B-1 衝突處置完畢。
見 §3 `ENTER_STANDBY`。

### `VAL_ 1470 PowerSts_Telematic`（逐字）

`0 "Sleep"  1 "Standby"  2 "Timed"  3 "Idle"  4 "Full_Operation"  5 "Logistic_On"  6 "Bench"  7 "Partial_Operation"`

### `VAL_ 854 OperationalModeSts`（逐字，僅列本表所用者）

`2 "Ignition_Off"  3 "Ignition_Acc"  4 "Ignition_On"  10 "Ignition_Pre_Off"  15 "SNA"`

## 1. 狀態集與拼法 —— 依 R-P363 改依 `VAL_ 1470`

55 包 B2 所報之三處不合（A-PW350）已由 R-P363 裁定：

| 項 | 55 包所報 | **R-P363 之裁定** |
|---|---|---|
| 拼法 | `VAL_` 為 `Full_Operation`，R-P354 寫 `Full-Operation` | **`<STATE>` 集合 = `VAL_ 1470` 之列舉值，拼法逐字取 `VAL_`** |
| `Logistic_On`（raw 5）| 在 `VAL_` 而不在 R-P354 八態 | **入正表**，惟 TC 產出仍受 R-P349(a) / DR-PW11 阻斷 —— **片段可立、TC 不產** |
| `INIT` | 不在 `VAL_` | **依 R-13 保留規格原名**，標 `PENDING: DR-PW26 INIT 觀察量`；**不得以 `VAL_` 內語意相近之值代入** |

故本表之片段集為 **`VAL_ 1470` 之八值 ＋ 規格態 `INIT`，共九個**。

## 2. `$PowerMode$` 之對應 —— DR-PW26

CFTS009 §1.3.1.1 之 Body ON / Body OFF 以 **`$PowerMode$`** 定義：

- `4941027`：Body ON = `$PowerMode$` = `[IGN_ACC]` / `[IGN_OFF_ACC]` / `[IGN_RUN]`
- `4941028`：Body OFF = `$PowerMode$` = `[IGN_LK]` / `[IGN_OFF]` / `[IGN_START]` / `[undefined]` / `[SNA]`

`$PowerMode$` 於兩份 DBC **查無同名**；相近者為 `STATUS_BH_BCM1.OperationalModeSts`
（`VAL_ 854` 含 `Ignition_Acc` / `Ignition_On` / `Ignition_Off` / `SNA` 等，
與 `$PowerMode$` 之值域**語義相符而拼法不同**）。

**27 包（pm_29）已逕以 `$STATUS_BH_BCM1.OperationalModeSts$` 表 Body ON/OFF
而未登 DR** —— 該認定屬上游職權（§8.4.1），與 DR-PW21 為同一形態。
本表沿用該寫法（R-13 下正確、可撰寫），**並開 DR-PW26 請上游確認**。
確認前，各片段之 Body ON/OFF 驅動步標註 `(DR-PW26)`。

## 3. 九個片段

### `ENTER_FULL_OPERATION`

| | |
|---|---|
| 目標 `PowerSts_Telematic` | `4 (Full_Operation)` |
| 錨點 | `CFTS009-4941042`（進入條件）、`CFTS009-4941027`（Body ON 定義）、`CFTS009-4941362`（`$Telematic_Power$ = [Full_Operation]`）|

```
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 4 (Ignition_On)   (DR-PW26)
2. Press the HU Power button
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
```

`4941042` 之進入條件為析取式：Body ON ∧（無 Power Button ∨（有 Power Button ∧
（`VPLastStatus==ON` ∨ PWR button pressed ON ∨ Phone Call ACTIVE ∨ `RVC_Condition==True`）））。
第 2 步取 `PWR button pressed ON` 一支 —— **其餘三支為等價入口，
不逐一產出**（測 TC 若須指定入口，於該 TC 之 Remarks 記明所取之支）。

### `ENTER_IDLE`

| | |
|---|---|
| 目標 | `3 (Idle)` |
| 錨點 | `CFTS009-4941039`（Body ON ＋ 有 Power Button ＋ `$HUModeStatus$ = [RAD_OFF]`）、`CFTS009-4941027` |

```
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 4 (Ignition_On)   (DR-PW26)
2. Press the HU Power button to turn the audio off
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)
```

### `ENTER_TIMED`

| | |
|---|---|
| 目標 | `2 (Timed)` |
| 錨點 | `CFTS009-4941054`（Body OFF ＋ CAN 保持喚醒）、`CFTS009-4941028`（Body OFF 定義）、`CFTS009-4941055` / `CFTS009-4941056`（`Timeout1` 之定義與 `$PwrAccDelayAct$` 換算）|

```
1. Apply ENTER_FULL_OPERATION
2. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 10 (Ignition_Pre_Off)   (DR-PW26)
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
```

⚠ `4941055` / `4941056` 載「`Timeout1` 僅在 Radio 自 STANDBY 轉入 TIMED 時使用」。

**離開條件之訊號**（`4941059`：`$AccDelayAct$` becomes Not Active && Phone Call == Not active）
依 R-P371(b) 引 **`$BCM_FD_27.Comfort_Enable_Act$`**
（forms FDCAN8，`CM_` 註解 `Accessory Delay Active` 與 LID r29 `Function` 欄逐字同；
該列 `Atlantis High` 欄為 `N/A`，故段 2 走 FD 側）。
自 Full_Operation 進入 Timed 者不經 Timeout1；**若某 TC 所測者為
STANDBY → TIMED，須改用 `ENTER_STANDBY` ＋ Timeout1 觸發**，
其片段待該 TC 出現時另立（本表不預造）。

### `ENTER_STANDBY`

| | |
|---|---|
| 目標 | `1 (Standby)` |
| 錨點 | `CFTS009-4941037`（Body OFF 時收到 CAN 訊號則喚醒）、`CFTS009-4941028` |

```
1. Apply ENTER_TIMED
2. Wait until $BCM_FD_27.Comfort_Enable_Time$ (Timeout1) has elapsed with no phone call active
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)
```

⚠ 第 2 步之 `Timeout1` 值取自 `$PwrAccDelayAct$`（`4941055`：X = 該訊號十進位值 × 15 秒）。
**58 包三段鏈重解**（R-P368）：段 1 LID r1458 c1 `PwrAccDelayAct` 逐字命中
（`Function` = `Power accessory delay time`）→ 段 2 `BODY_CNTRL3.Comfort_Enable_Time`（`B-CAN`）
→ 段 3 **BHCAN2 無、旁證 R4 有、FDCAN8 有同名訊號惟訊息為 `BCM_FD_27`**（A-PW357）。

**60 包 R-P371 裁乙 —— B-1 衝突已處置**：採
**`$BCM_FD_27.Comfort_Enable_Time$`**（forms FDCAN8，接收節點 ETM/LTM，
`CM_` 註解與 LID r1458 `Function` 欄逐字同）。R4 之 `BODY_CNTRL3` 版
（接收 DDM/PDM）不採。第 2 步之 `Timeout1` 值改引該訊號：

```
2. Wait until $BCM_FD_27.Comfort_Enable_Time$ (Timeout1) has elapsed with no phone call active
```

⚠ 「規格名 = DBC 訊號」之最終認定屬上游（§8.4.1）；
DR-PW26 第 (4) 問已改為「確認」並附本條證據，**上游否認則回滾至 PENDING**（R-P371(c)）。

### `ENTER_SLEEP`

| | |
|---|---|
| 目標 | `0 (Sleep)` |
| 錨點 | `CFTS009-4941032`（Body OFF ＋ CAN 無匯流排活動）、`CFTS009-4941035`（`$Telematic_Power$ = [BO_Off_TGW_OFF]`、sleep indication）|

```
1. Apply ENTER_STANDBY
2. Stop all bus activity on Body CAN and let the network go to sleep
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)
```

⚠ 第 3 步與第 2 步相衝：CAN 進入 sleep 後**無法再以 CAN 讀取確認值**。
`4941035` 僅載 HU 送出 sleep indication flag，未載可於何處觀察最終態。
**本片段之確認步不可執行 —— 標 `PENDING: DR-PW26`（請上游指定 Sleep 態之觀察方法）。**

### `ENTER_PARTIAL_OPERATION`

| | |
|---|---|
| 目標 | `7 (Partial_Operation)` |
| 錨點 | `CFTS009-4941044` / `CFTS009-4941045`（`$RemoteStartActive$ = [Active]` → `$Telematic_Power$ = [TGW_PWR_REM]`）、`CFTS009-4941392`（`STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"`）|

```
1. Apply ENTER_STANDBY
2. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)
```

本片段之驅動訊號**全為 DBC 白名單類**，無 DR-PW26 依賴 ——
`4941392` 以 `STATUS_BH_BCM2.RemStActvSts` 逐字寫出，不經 `$RemoteStartActive$` 之別名。

### `ENTER_BENCH`

| | |
|---|---|
| 目標 | `6 (Bench)` |
| 錨點 | `CFTS009-4941061`（無 CAN 或 CAN 睡眠時，接上 EngineeringLine 硬線）|

```
1. Disconnect the Body CAN bus from the HU
2. Connect the hardwired Ignition Sense line (EngineeringLine) to the HU
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 6 (Bench)
```

⚠ 與 `ENTER_SLEEP` 同型之矛盾：第 1 步斷開 CAN，第 3 步需 CAN 讀值。
`4941061` 載「In this mode, the HU shall wake up on CAN and begin communication」——
**進入 Bench 後 HU 會自行喚醒 CAN**，故第 3 步在重新連接後可執行。
第 1 步改為「Let the Body CAN go to sleep」亦可（`4941061` 之二擇一條件）。
本片段**可執行**，惟第 1 步與第 3 步之間須有 CAN 重連，已於步驟中隱含 —— 標記為**待站④ 人審確認措辭**。

### `ENTER_INIT`

| | |
|---|---|
| 目標 | **無 `VAL_` 值**（見 §1）|
| 錨點 | `CFTS009-4941439` / `CFTS009-4941447` / `CFTS009-4941448`（電壓門檻與進出 INIT 之時序「refer to SIS」）、`CFTS009-4941449`（電池重接後回復設定）|

```
1. Disconnect the battery from the HU
2. Reconnect the battery
3. PENDING: DR-PW26 INIT 態之觀察方法（PowerSts_Telematic 無 INIT 值；
   電壓門檻與時序 CFTS009 載為「refer to SIS」，SIS 不在素材台帳內）
```

**本片段不可執行。** 三份錨點皆將門檻與時序外指至 SIS，
SIS 不在 G0 台帳之九份內，**不得自造**（R-P353 末段 / §I）。

### `ENTER_LOGISTIC_ON`（R-P363(b)：自附錄移入正表）

| | |
|---|---|
| 目標 | `5 (Logistic_On)` |
| 錨點 | `CFTS009-4941063`（`$PowerModeSts$ = [SHIP_MD or Logistic_Mode_ON]` → LOGISTICS MODE）、DR-PW21（`PowerModeSts_Telematic` 之歸屬）|

```
1. Send the signal $STATUS_BH_BCM1.PowerModeSts$ = 1 (Logistic_Mode_ON)   (DR-PW21)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 5 (Logistic_On)
```

依 DR-PW21 之未決狀態，第 1 步之訊號歸屬未確認。
**TC 不產（R-P349(a) / DR-PW11 阻斷），片段先立**（R-P363(b)）。
⚠ `$STATUS_BH_BCM1.PowerModeSts$` 之 `VAL_ 854` 於 BHCAN2 實查為
`0 Standard_Power / 1 Logistic_Mode_ON / 2 Logistic_Mode_PR / 3 LogisticModeON_and_EngineON`，
與 CFTS009-4941063 原文之二值逐字相符（僅 `ON`/`On` 大小寫）。

## 4. 可執行性總表（G246，依 R-P365(a) 之新期望值）

| 片段 | 驅動步 | 確認步 | 判定 |
|---|---|---|---|
| `ENTER_FULL_OPERATION` | 可（DR-PW26 待確認） | 可 | **可用** |
| `ENTER_IDLE` | 可（DR-PW26） | 可 | **可用** |
| `ENTER_TIMED` | 可（DR-PW26） | 可 | **可用** |
| `ENTER_STANDBY` | 可，`Timeout1` 引 `$BCM_FD_27.Comfort_Enable_Time$`（R-P371 裁乙）| 可 | **可用** |
| `ENTER_PARTIAL_OPERATION` | 可（無 DR 依賴） | 可 | **可用** |
| `ENTER_BENCH` | 可 | 可（須 CAN 重連） | **可用（措辭待站④）** |
| `ENTER_LOGISTIC_ON` | 可（DR-PW21 待確認） | 可 | **片段可用，TC 不產**（R-P349(a) / DR-PW11） |
| `ENTER_SLEEP` | 可 | **否** | **PENDING: DR-PW26 Sleep 觀察方法** |
| `ENTER_INIT` | 可 | **否** | **PENDING: DR-PW26 INIT 觀察量** |

**九個片段：七可用、二 PENDING。**

R-P365(a) 之 G246 新期望值為「可用片段 100% 解析 ＋ PENDING 片段逐條掛 DR-PW26
且其所涉列以 `PENDING: DR-PW26 <態>` 佔位」：

| G246 判準 | 實測 |
|---|---|
| 可用片段（7）之 `$…$` 全部在 BHCAN2 有 `SG_` | **7 / 7**（G254 同時驗畢，B-1 衝突 0）|
| PENDING 片段（2）逐條掛 DR-PW26 | **2 / 2**（`Sleep 觀察方法` / `INIT 觀察量`）|
| `operative` / `a … state` 殘留 | 待 B5 施作後量 |

**G246 前二項 PASS。** 第三項須待機器改寫（B5）後方可量，本包不報。

⚠ **`ENTER_SLEEP` 之矛盾寫入片段備註**（R-P363(d)）：
`4941032` 之進入條件為「CAN 無匯流排活動」，`4941035` 僅載 HU 送出 sleep
indication flag —— CAN 睡眠後無法再以 CAN 讀 `PowerSts_Telematic`。
DR-PW26 已問是否有非 CAN 觀察面（電流／LIN／log）。

## 5. lint 常數表同步

`ENTER_*` **九個**常數名、其目標 raw 值與 `VAL_` 標籤已列於 §3。
§1（R-P363）、§4（R-P365(a)）已裁，§0 之判準 DBC 已定（R-P368(e)），
`$PwrAccDelayAct$` 之 B-1 衝突亦已由 R-P371 裁乙處置。
**常數表無未定項，可寫**，隨 B5 一併落地（B5 依 R-P374(a) / K-2 甲續凍）。
