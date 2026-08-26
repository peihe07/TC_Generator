# 上繳包 33 —— `ops-01`：88 → 排除 36 → 52 條候選 → 14 軸 → 13 條 TC

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/33_ops01_scoped.md`
- **33 包於 34 包落檔時尚未執行**；依 34 包 §2.1 之指示，兩包合併執行，
  本上繳與 `34_closeout.md` 同輪產出
- 停止條件 91／92／93 皆未觸發

---

## 一、R-G39 之抄錄核對表

## 抄錄核對表 — 33_ops01_scoped.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| — | R-G39 | `docs/fw036/RULINGS_LEDGER.md` | 630 | `a1fdf3176b5a6fb3` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **59** 個，與各下放包原檔逐字元比對 **全數相符**（59 vs 59）。

---

## 二、排除表（88 → 52），逐條具名理由

# 排除 36 條 → 保留 **52** 條
  E2: 27
  E1: 6
  E3: 3

# 排除表（逐條具名理由）
| 條 | 類 | §章節 | 理由 |
|---|---|---|---|
| {4819642} | E1 | 1.8.2.1.2.1 | 已被 pilot-01／rvc-01 引為 specification_reference |
| {4819645} | E1 | 1.8.2.1.2.1 | 已被 pilot-01／rvc-01 引為 specification_reference |
| {4819652} | E1 | 1.8.2.1.3.1 | 已被 pilot-01／rvc-01 引為 specification_reference |
| {4819668} | E1 | 1.8.2.1.4.1 | 已被 pilot-01／rvc-01 引為 specification_reference |
| {4819671} | E1 | 1.8.2.1.4.1 | 已被 pilot-01／rvc-01 引為 specification_reference |
| {4820265} | E1 | 1.11.2.1.3.1 | 已被 pilot-01／rvc-01 引為 specification_reference |
| {4819632} | E2 | 1.8.2.1.1 | 主題逐字為 Display Hot（004／005 之材料） |
| {4819635} | E2 | 1.8.2.1.1.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4819641} | E2 | 1.8.2.1.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4819651} | E2 | 1.8.2.1.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4819654} | E2 | 1.8.2.1.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4819667} | E2 | 1.8.2.1.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820250} | E2 | 1.11.2.1.1 | 主題逐字為 Display Hot（004／005 之材料） |
| {4820252} | E2 | 1.11.2.1.1.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820257} | E2 | 1.11.2.1.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820258} | E2 | 1.11.2.1.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820260} | E2 | 1.11.2.1.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820264} | E2 | 1.11.2.1.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820266} | E2 | 1.11.2.1.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820275} | E2 | 1.11.2.1.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820276} | E2 | 1.11.2.1.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4820278} | E2 | 1.11.2.1.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821017} | E2 | 1.15.3.1 | 主題逐字為 Display Hot（004／005 之材料） |
| {4821020} | E2 | 1.15.3.1.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821026} | E2 | 1.15.3.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821027} | E2 | 1.15.3.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821030} | E2 | 1.15.3.2.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821036} | E2 | 1.15.3.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821037} | E2 | 1.15.3.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821039} | E2 | 1.15.3.3.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821052} | E2 | 1.15.3.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821053} | E2 | 1.15.3.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4821056} | E2 | 1.15.3.4.1 | 主題逐字為 Rear View Camera（007／008 之材料） |
| {4819253} | E3 | 1.4.1.2.3 | B29 偽陽性：`wake` 命中而非 Sleep/Wake 主題 |
| {4819710} | E3 | 1.8.2.2 | B29 偽陽性：`wake` 命中而非 Sleep/Wake 主題 |
| {4820824} | E3 | 1.15.2.2 | B29 偽陽性：`wake` 命中而非 Sleep/Wake 主題 |

# 保留之 52 條

**排除 36 條**：E1 已被兩批引用 **6**、E2 主題為 Display Hot／RVC **27**、
E3 `wake` 偽陽性 **3**。**保留 52 條**（停止條件 92 未觸發 —— 逐條皆具名理由）。

E2 之 27 條為 004／005／007／008 之**未用材料，不丟棄**（見 §五）。

---

## 三、行為軸表（R-G39 第二段）

**14 軸**（001 八軸、002 四軸、003 二軸），**軸數未逾 20**（停止條件 91 未觸發）。
其中一軸於 34 包之機器檢查階段移除（見上繳 34 §2.2），**實產 13 條**。

| # | leaf | 行為軸 | 所據條文 | 章別 |
|---|---|---|---|---|
| 1 | 001 | Screen ON 態之週期狀態回報 | `{4820255}` | 行為 |
| 2 | 001 | 請求關閉且強度歸零 → 送 `[OFF]` | `{4819722}` | 行為 |
| 3 | 001 | 請求關閉而強度非零 → 顯示 TOUCH 提示 | `{4820262}` | 行為 |
| 4 | 001 | SCREEN OFF 硬鍵 | `{4820193}`／`{4820194}` | 行為 |
| 5 | 001 | POWER 硬鍵 | `{4820187}`／`{4820189}` | 行為 |
| 6 | 001 | 螢幕關閉軟鍵 | `{4820827}` | 行為 |
| 7 | 001 | 顯示狀態收到不合理值（已有合理值前態） | `{4819353}` | **診斷** |
| 8 | 001 | 顯示狀態收到不合理值（無合理值前態） | `{4819353}` | **診斷** |
| 9 | 002 | 觸控 TOUCH 提示畫面 → 送觸控事件 | `{4820268}` | 行為 |
| 10 | 002 | TOUCH 提示畫面逾時 | `{4820271}` | 行為 |
| 11 | 002 | 提示畫面顯示中收到關閉請求 | `{4820272}` | 行為 |
| ~~12~~ | ~~002~~ | ~~喚醒後不合理強度值 → 沿用上一合理值~~ | ~~`{4819347}`~~ | **34 輪移除，見上繳 34 §2.2** |
| 13 | 003 | Pre Splash／Pre Disclaimer 期間之狀態回報 | `{4820248}` | 行為 |
| 14 | 003 | Splash／Disclaimer 期間之狀態回報 | `{4820249}` | 行為 |

**停止條件 90（診斷章與行為章混入同一 TC 之同一軸）未觸發** ——
軸 7／8 之 `specification_reference` 只引 `{4819353}`（診斷章），
其餘只引行為章，**無一 TC 跨章**。

### 3.1 架構副本之取捨

52 條中多組為逐字相同之架構副本（§1.8.x／§1.11.x／§1.15.x）。
本批一律引 **§1.11.x**（`ICS and DCSD` 之 Atlantis High 章）之副本；
`{4819722}`（`§1.8.2.3.1`，`[Radio:R1M, R1H] [EE:Atlantis High]`）與
`{4819353}`（`§1.4.3.2`，`[EE:All]`）於 §1.11.x 無副本，各引其原處。

### 3.2 T1c —— 逐條拼法判定（R-DM48／A-DM35 條款層級）

| 拼法 | 條文 | 判定 |
|---|---|---|
| 短拼法 `= [ON]` | `{4820255}` | **得寫 raw** → `1 (ON)` |
| 短拼法 `= [OFF]` | `{4819722}` | **得寫 raw** → `0 (OFF)` |
| 長拼法 `= [DISP_OFF]`／`[DISP_NORMAL]`（`$TGW_DISP_STAT$`） | 多條 | **不得寫 raw**（DR-DM9(b)）→ ER 驗畫面／背光 |
| `[0% Intensity]`（`$RQ_DISP_INTS$`） | 多條 | **不得寫 raw**（非列舉值）→ ER 驗「請求強度為零」 |
| 整數 5／6（`$DCSD_DISP_STAT$` 之不合理值） | `{4819353}` | **非值標籤** —— 逐字寫入 procedure 之注入動作；**ER 不寫賦值**（34 輪修正） |

---

## 四、`ops-01` 之十欄全文

### #1 — `SWE1-DM-001`　Display in screen on state → on status reported

`spec_ref` CFTS020-4820255　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Periodic status in the on state — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen ON state
2. The requested display intensity is a non-zero value

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 1 (ON)
2. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ again after one minute and check that it is 1 (ON)

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 1 (ON) is received
2. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 1 (ON) is received

```
### #2 — `SWE1-DM-001`　Screen off requested → off status reported

`spec_ref` CFTS020-4819722　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Entry to the off state — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen ON state
2. The requested display intensity is a non-zero value

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Request the display off state on the HU and set the requested display intensity to zero
3. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 0 (OFF)

[expected_result]
1. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 1 (ON) is received
2. The DCSD Display leaves the DCSD Screen ON state
3. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 0 (OFF) is received

```
### #3 — `SWE1-DM-001`　Screen off with intensity retained → touch prompt shown

`spec_ref` CFTS020-4820262　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` True

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Off request while the intensity stays non-zero — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen ON state
2. The requested display intensity is a non-zero value

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Request the display off state on the HU while the requested display intensity stays non-zero
3. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The DCSD Display shows the normal screen
2. The DCSD Display leaves the DCSD Screen ON state
3. The DCSD Display shows the TOUCH SCREEN TO TURN ON screen

```

`split_reason`：§8.3 之輸入軸：同一「請求關閉」之動作，依 $RQ_DISP_INTS$ 是否為零而分歧 —— 零則進 OFF 態（`{4819722}`），非零則顯示 TOUCH SCREEN TO TURN ON（`{4820262}`）。兩者之失效可獨立發生

### #4 — `SWE1-DM-001`　Screen off hardkey pressed → touch prompt shown

`spec_ref` CFTS020-4820193 / CFTS020-4820194　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Hardkey entry to the off state — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The HU is in the HU Screen ON state
2. The requested display intensity is a non-zero value

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Press the SCREEN OFF hardkey
3. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The DCSD Display shows the normal screen
2. The HU accepts the SCREEN OFF hardkey press
3. The DCSD Display shows the TOUCH SCREEN TO TURN ON screen

```
### #5 — `SWE1-DM-001`　Power hardkey pressed → screen state request issued

`spec_ref` CFTS020-4820187 / CFTS020-4820189　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Power hardkey path — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The HU is in the HU Screen ON state
2. The telematic power state is full operation

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Press the POWER hardkey
3. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The DCSD Display shows the normal screen
2. The HU determines whether to accept the POWER hardkey press
3. The DCSD Display leaves the normal screen

```
### #6 — `SWE1-DM-001`　Screen off button pressed → display turned off

`spec_ref` CFTS020-4820827　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Soft button entry to the off state — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The DCSD Display is in the DCSD Screen ON state
2. The screen off button is present on the display

[input_test_data]
NA

[test_procedure]
1. Read the backlight state of the DCSD Display and record it
2. Press the screen off button on the DCSD Display
3. Read the backlight state of the DCSD Display and record it

[expected_result]
1. The backlight is on
2. The screen off button press is accepted
3. The backlight is off

```
### #7 — `SWE1-DM-001`　Implausible display status received → last valid value kept

`spec_ref` CFTS020-4819353　`design_method` 等價類劃分 (Equivalence Partitioning)　`priority` P1　`functional_safety` NA　`split_flag` True

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Fault tolerance of the status input — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The HU has received a plausible display status value since the last exit from sleep mode
2. The last plausible display status value received was 1 (ON)

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the HU and record it
2. Send the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ with the value 5
3. Read the screen shown on the HU and record it

[expected_result]
1. The HU shows the screen matching the last plausible display status
2. The HU does not change the screen shown
3. The HU shows the same screen as recorded in step 1

```

`split_reason`：§8.3 之輸入軸：不合理值之處置與正常值之處置為兩條獨立路徑。值 5 逐字取自 `{4819353}` 之 `values 5 or 6`，**未自 DBC 推導、未補齊區間**（32 包 §2.3 第 1 項）

### #8 — `SWE1-DM-001`　No valid display status since wake-up → on assumed

`spec_ref` CFTS020-4819353　`design_method` 邊界值分析 (Boundary Value Analysis, BVA)　`priority` P1　`functional_safety` NA　`split_flag` True

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Fault tolerance with no prior value — the DISPLAY_ON and DISPLAY_OFF naming is deferred)

[pre_conditions]
1. The HU has not received any plausible display status value since the last exit from sleep mode

[input_test_data]
NA

[test_procedure]
1. Send the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ with the value 6
2. Read the screen shown on the HU and record it

[expected_result]
1. The HU does not change the screen shown on account of the received value
2. The HU shows the screen it shows for the on state

```

`split_reason`：§8.3 之邊界軸：`{4819353}` 分兩種前態 —— 已收過合理值者沿用，未收過者用預設。本條驗後者。值 6 逐字取自該條之 `values 5 or 6`

### #9 — `SWE1-DM-002`　Touch on the prompt screen → touch event sent

`spec_ref` CFTS020-4820268　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall transition display state from DISPLAY_OFF to DISPLAY_ON when valid touch coordinates are received from DCSD.The software shall restore previous display brightness and active HMI context after wake-up event handling.

(Wake-up trigger on the prompt screen — the DISPLAY_ON and DISPLAY_OFF naming and the brightness context are deferred)

[pre_conditions]
1. The DCSD Display is showing the TOUCH SCREEN TO TURN ON screen

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Touch the DCSD Display
3. Read the touch event sent by the DCSD and record it

[expected_result]
1. The DCSD Display shows the TOUCH SCREEN TO TURN ON screen
2. The touch is registered by the DCSD
3. The DCSD sends the touch event to the HU

```
### #10 — `SWE1-DM-002`　Prompt screen times out → display turned off

`spec_ref` CFTS020-4820271　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall transition display state from DISPLAY_OFF to DISPLAY_ON when valid touch coordinates are received from DCSD.The software shall restore previous display brightness and active HMI context after wake-up event handling.

(Timeout path of the prompt screen — the DISPLAY_ON and DISPLAY_OFF naming and the brightness context are deferred)

[pre_conditions]
1. The DCSD Display is showing the TOUCH SCREEN TO TURN ON screen
2. The DCSD Display is not touched for the whole of this test

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Read the screen shown on the DCSD Display after the prompt screen times out
3. Read the requested display intensity and record it

[expected_result]
1. The DCSD Display shows the TOUCH SCREEN TO TURN ON screen
2. The DCSD Display leaves the TOUCH SCREEN TO TURN ON screen
3. The requested display intensity is zero

```
### #11 — `SWE1-DM-002`　Off request while prompt shown → prompt screen left

`spec_ref` CFTS020-4820272　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall transition display state from DISPLAY_OFF to DISPLAY_ON when valid touch coordinates are received from DCSD.The software shall restore previous display brightness and active HMI context after wake-up event handling.

(Arbitration while the prompt is up — the DISPLAY_ON and DISPLAY_OFF naming and the brightness context are deferred)

[pre_conditions]
1. The DCSD Display is showing the TOUCH SCREEN TO TURN ON screen

[input_test_data]
NA

[test_procedure]
1. Read the screen shown on the DCSD Display and record it
2. Request the display off state on the HU and set the requested display intensity to zero
3. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The DCSD Display shows the TOUCH SCREEN TO TURN ON screen
2. The DCSD receives the off request
3. The DCSD Display leaves the TOUCH SCREEN TO TURN ON screen

```
### #12 — `SWE1-DM-003`　Startup before splash → display status reported

`spec_ref` CFTS020-4820248　`design_method` 狀態轉換 (State Transition Testing)　`priority` P2　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall support Splash Screen handling during system startup and sleep-to-wakeup transition sequence.The software shall resume normal HMI operation after Splash timeout completion or operational state transition completion.

(Pre splash period of the startup sequence — the splash timing and the DISPLAY_ON and DISPLAY_OFF naming are deferred)

[pre_conditions]
1. The vehicle is in the startup sequence before the splash screen period

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The DCSD reports its display status to the HU
2. The DCSD Display shows the screen sent by the HU for this period

```
### #13 — `SWE1-DM-003`　Splash period → display status reported

`spec_ref` CFTS020-4820249　`design_method` 狀態轉換 (State Transition Testing)　`priority` P2　`functional_safety` NA　`split_flag` False

```text
[test_item]
The Display Management software shall support Splash Screen handling during system startup and sleep-to-wakeup transition sequence.The software shall resume normal HMI operation after Splash timeout completion or operational state transition completion.

(Splash period of the startup sequence — the splash timing and the DISPLAY_ON and DISPLAY_OFF naming are deferred)

[pre_conditions]
1. The vehicle is in the startup sequence during the splash screen period

[input_test_data]
NA

[test_procedure]
1. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
2. Read the screen shown on the DCSD Display and record it

[expected_result]
1. The DCSD reports its display status to the HU
2. The DCSD Display shows the screen sent by the HU for this period

```
### `reasoning` 全文

```text
**兩段式界定（R-G39）**：第一段候選母體 —— 以三條 037 需求文之逐字內容導出九詞掃 CFTS_020，取 (B) 僅主題詞之界定得 **88 條**（33 包 §2.2 之裁定）；依 §2.3 三類排除 **36 條**（E1 已被兩批引用 6、E2 主題為 Display Hot／RVC 27、E3 `wake` 偽陽性 3），**保留 52 條**。第二段行為軸 —— 自 52 條歸納 **14 軸**（001 八軸、002 四軸、003 二軸），**其中一軸於檢查階段移除，實產 13 條**，一軸一 TC（§5.7），軸數未逾 20（停止條件 91 未觸發）。

**架構副本之取捨**：52 條中多組為逐字相同之架構副本（§1.8.x／§1.11.x／§1.15.x）。本批一律引 **§1.11.x**（`ICS and DCSD` 之 Atlantis High 章）之副本，其屬性行為 `[Radio:R1H, R1M, VP5R120] [EE Architecture:Atlantis High, PowerNet]`；惟 `{4819722}`（`§1.8.2.3.1 Screen Off Button`，`[Radio:R1M, R1H] [EE:Atlantis High]`）與 `{4819347}`／`{4819353}`（`§1.4.3.x`，`[EE:All]`）於 §1.11.x 無副本，各引其原處。

**逐條拼法判定（T1c；R-DM48／A-DM35 條款層級）**：
- 得寫 raw 者：`{4820255}` 之 `$DCSD_DISP_STAT$ = [ON]`（短拼法 → `1 (ON)`）、`{4819722}` 之 `= [OFF]`（短拼法 → `0 (OFF)`）。
- **不得寫 raw 者**：`$TGW_DISP_STAT$` 之 `[DISP_OFF]`／`[DISP_NORMAL]`（HU 側，DR-DM9(b) 未結）、`$RQ_DISP_INTS$` 之 `[0% Intensity]`（非列舉值）。此三者之 ER 一律改驗可觀察行為（畫面、背光、請求強度是否為零）。
- **不合理值之整數 5／6／201 為逐字取自條文之 CAN 值**，非值標籤，依 32 包 §2.3 第 1 項**逐字寫入、未自 DBC 推導、未補齊區間**（停止條件 88）。

**A15 之處置**：037 之 `DISPLAY_ON`／`DISPLAY_OFF`、DBC 之 `ON`／`OFF`、規格之 `[DISP_ON]`／`[DISP_OFF]` 三者兩兩逐字不等。依 R-DM48 不外推 —— 本批 ER 所寫之 `1 (ON)`／`0 (OFF)` **係依所引條款之短拼法逐字解得，非宣告其等同 037 之 `DISPLAY_ON`／`DISPLAY_OFF`**。該對應之未決以 deferred 承載（三 leaf 各一項，`blocking_dr: DR-DM8`），並依 R-G33 於各條括號下半指名。

**003 之限度**：`{4820248}`／`{4820249}` 之時段定義轉指 `{CFTS009-722}`（CFTS_009 未取得）。**故 003 之兩條只驗該時段內之狀態回報，不驗時長、不驗 `Splash timeout completion`**—— 後者為 037 之 003 逐字所要求者，已以 `splash timing` 之 deferred 指名（DR-DM1）。

**Sleep Mode 之前置為狀態（32 包 §2.3 第 3 項）**：四條不合理值 TC 之前置皆寫為「已／未收到過合理值」之**狀態**（`The HU has received…` / `has not received…`），非動作。停止條件 89 未觸發、55 未觸發。

**診斷章與行為章之分屬（停止條件 90）**：本批之 14 軸中，四軸取自**診斷章**（`§1.4.3.x` 之不合理值條文：#7／#8／#12），其餘取自**行為章**（`§1.8.x`／`§1.11.x`／`§1.15.2.3`）。**二者未編入同一 TC 之同一驗證軸** —— 每一 TC 之 `specification_reference` 只引單一章別。

**未用材料（R-G39 配套）**：52 條中未被任何軸取用者 **38 條**，其理由分四類 —— (i) 架構副本（同一本體之 §1.8.x／§1.15.x 版本，已由 §1.11.x 之副本承載）；(ii) **非 DCSD 標的**（FPDM `{4820012}`／`{4820014}`／`{4820017}`／`{4820019}`／`{4820020}`、CCDMF `{4819927}`、CCDMR `{4819944}` —— 037 八條之標的為 DCSD）；(iii) 非顯示狀態之不合理值（`PANEL_INTS` `{4819350}`、`CmdIgnStat` `{4819351}`、`$HUModeStatus$` `{4819355}`／`{4820159}`）；(iv) ICS 之 standby（`{4820147}`，標的為 ICS 模組）。逐條表見上繳 33 §五。

**Priority（§10.2）**：001／002 之十二條為 P1（major user-facing functionality）；003 之二條為 **P2** —— 037 之 003 其 `Priority` 欄逐字為 `Medium`，且本批只驗其時段內之狀態回報。`functional_safety` 十四條皆 `NA`（R-DM46：SYS3 之 `ASIL Level` 31/31 為 `QM`）。

**Design Method（§12）**：於步驟定稿後指派。十軸為狀態轉換；#7／#12 為等價類劃分（不合理值 vs 合理值之兩類）；#8 為邊界值分析（其標的為「未曾收到合理值」這一個前態邊界）。

**34 輪之修正（兩處）**：
(1) **原 #12 移除** —— 其 ER 須寫 `$RQ_DISP_INTS$ = 201` 之賦值，而該訊號之 DBC `VAL_` 只定義 `255 "SNA"`，**201 無標籤可解**（R-1 v3(a)／R-DM48）；且其訊息名 `RADIO_B3` 之採用受**停止條件 83** 禁止（30a §3.1「只登記不採用」）。**該行為軸併入 `brightness context` 之 deferred 項。**
(2) **#7／#8 之 ER 改為只驗可觀察行為** —— 原稿寫 `$DIS_CENTERSTACK.DCSD_DISP_STAT$ = 5`／`= 6`，而 5／6 **正因其無 `VAL_` 標籤才是不合理值**，寫成賦值即違 R-1 v3(a)。**注入動作留在 test_procedure（步驟得寫具體注入值），ER 只驗畫面不變。**
```

### `deferred` 陣列（R-DM53 四鍵）

```json
[
  {
    "leaf_id": "SWE1-DM-001",
    "token": "DISPLAY_ON and DISPLAY_OFF naming",
    "blocking_dr": "DR-DM8",
    "reason": "037 之 001 逐字用 `DISPLAY_ON`／`DISPLAY_OFF`；DBC `DCSD_DISP_STAT` 之 `VAL_` 為 `1 \"ON\"`／`0 \"OFF\"`；規格側另有別名 `[DISP_ON]`／`[DISP_OFF]`。三者兩兩逐字不等（A15），依 R-DM48 不外推。本批之 ER 所寫之 `1 (ON)`／`0 (OFF)` 係依所引條款之**短拼法**逐字解得（A-DM35 條款層級），**非**宣告其等同 037 之 `DISPLAY_ON`／`DISPLAY_OFF`"
  },
  {
    "leaf_id": "SWE1-DM-002",
    "token": "DISPLAY_ON and DISPLAY_OFF naming",
    "blocking_dr": "DR-DM8",
    "reason": "同 001"
  },
  {
    "leaf_id": "SWE1-DM-002",
    "token": "brightness context",
    "blocking_dr": "DR-DM8",
    "reason": "037 之 002 逐字要求 `restore previous display brightness and active HMI context`；CFTS_020 `{4819347}` 只規定不合理值時沿用上一合理值，**未載喚醒後之亮度還原序列**，亦未載 `active HMI context` 之定義。**34 輪另移除一條**：原 #12（不合理強度值 201 → 沿用上一合理值）其 ER 須寫 `$RQ_DISP_INTS$` 之賦值，而 (i) 該訊號之 `VAL_` 只定義 `255 \"SNA\"`，值 201 無標籤可解（R-1 v3(a)／R-DM48）；(ii) 其訊息名 `RADIO_B3` 之採用受停止條件 83 禁止（下放包 30a §3.1「只登記不採用」）。**該行為軸至此併入本 deferred 項。**"
  },
  {
    "leaf_id": "SWE1-DM-003",
    "token": "splash timing",
    "blocking_dr": "DR-DM1",
    "reason": "`{4820248}`／`{4820249}` 之時段定義一律轉指 `{CFTS009-722}`，CFTS_009 未取得。故本批之兩條只驗該時段內之狀態回報，**不驗時長、不驗 splash timeout completion**"
  },
  {
    "leaf_id": "SWE1-DM-003",
    "token": "DISPLAY_ON and DISPLAY_OFF naming",
    "blocking_dr": "DR-DM8",
    "reason": "同 001"
  }
]
```

---

## 五、未用材料表（R-G39 配套）

52 條候選中，**未被任何行為軸取用者 38 條**，逐類具名：

| 類 | 條數 | 條號 | 理由 |
|---|---:|---|---|
| (i) 架構副本 | 15 | `{4819638}`／`{4821023}`（＝`{4820255}`）、`{4819648}`／`{4821033}`（＝`{4820262}`）、`{4819657}`／`{4821042}`（＝`{4820268}`）、`{4819664}`／`{4821049}`（＝`{4820272}`）、`{4821047}`（＝`{4820271}`）、`{4819558}`（＝`{4820187}`）、`{4819560}`／`{4819572}`／`{4820189}`／`{4820194}` 之重複、`{4819571}`／`{4819573}` | 同一本體之 §1.8.x／§1.15.x 版本，已由 §1.11.x 之副本承載 |
| (ii) **非 DCSD 標的** | 7 | FPDM：`{4820012}`／`{4820014}`／`{4820017}`／`{4820019}`／`{4820020}`；CCDMF：`{4819927}`；CCDMR：`{4819944}` | **037 八條之標的為 DCSD**。此七條為 `[Radio:R1H][EE:Atlantis High]` 之專條，適用本車但**不屬本 feature 之 8 leaf** |
| (iii) 非顯示狀態之不合理值 | 6 | `{4819350}`（`PANEL_INTS`）、`{4819351}`（`CmdIgnStat`）、`{4819355}`／`{4820159}`（`$HUModeStatus$`）、`{4820157}`／`{4820373}`（`{4819353}` 之架構副本） | 其預設值非顯示狀態（`200 (100% Panel Intensity)`／`IGN_LK`／ICS 行為），不落 001–003 之主題 |
| (iv) ICS standby | 1 | `{4820147}` | 標的為 ICS 模組之 standby，非 DCSD 顯示狀態 |
| (v) 移除之軸 | 4 | `{4819347}`／`{4819348}`／`{4820152}`／`{4820368}` | 原軸 12 之材料，34 輪移除（見上繳 34 §2.2），併入 `brightness context` 之 deferred |
| (vi) Splash 其餘 | 5 | `{4819561}`、`{4819575}`、`{4820195}`、`{4820249}` 以外之 startup 條、`{4820827}` 之副本 | 其行為已由既有軸涵蓋（§5.7 一 TC 一驗證目標） |

> **(ii) 是本表最值得看的一列**：七條皆為 `[Radio:R1H][EE:Atlantis High]`
> 之**專條**，**適用本車**，惟其標的為 FPDM／CCDMF／CCDMR ——
> **037 之八條沒有涵蓋這三個顯示模組。** 該事實不屬本 feature 之缺陷
> （範圍由 037 界定），但交付面應知悉。

---

## 六、機器檢查（`ops-01` 單批）

```text
population: generated/ops-01.json, tcs = 14

--- tc_title（2–14 字）與相異 ---
  # 1 words= 9 :: Display in screen on state → on status reported
  # 2 words= 7 :: Screen off requested → off status reported
  # 3 words= 9 :: Screen off with intensity retained → touch prompt shown
  # 4 words= 8 :: Screen off hardkey pressed → touch prompt shown
  # 5 words= 8 :: Power hardkey pressed → screen state request issued
  # 6 words= 8 :: Screen off button pressed → display turned off
  # 7 words= 9 :: Implausible display status received → last valid value kept
  # 8 words= 9 :: No valid display status since wake-up → on assumed
  # 9 words= 9 :: Touch on the prompt screen → touch event sent
  #10 words= 8 :: Prompt screen times out → display turned off
  #11 words= 9 :: Off request while prompt shown → prompt screen left
  #12 words= 9 :: Implausible intensity after wake-up → last valid value kept
  #13 words= 7 :: Startup before splash → display status reported
  #14 words= 6 :: Splash period → display status reported
  distinct = 14 of 14

--- I-sibling：同 leaf 之括號下半逐字比對 ---
  SWE1-DM-001: 8 筆，逐字重複 = 0
  SWE1-DM-002: 4 筆，逐字重複 = 0
  SWE1-DM-003: 2 筆，逐字重複 = 0

--- test_item 上半 tokens（L 閾值 50）---
  #1=36  #2=36  #3=36  #4=36  #5=36  #6=36  #7=36  #8=36  #9=34  #10=34  #11=34  #12=34  #13=31  #14=31

--- Procedure ↔ ER 1:1 ---
  全部 1:1：PASS

--- 停止條件掃描 ---
  54（ER 未解析值標籤）= 0   55（PC 動作動詞）= 0
  60（CFTS013 門檻）= 0   73（引 CFTS013）= 0   83（30a 三標的）= 0

--- 89：Sleep Mode 前置是否為狀態 ---
  #7 1. The HU has received a plausible display status value since the last exit from sleep mode
  #8 1. The HU has not received any plausible display status value since the last exit from sleep mode
  #12 1. The DCSD has received a plausible intensity value since the last exit from sleep mode

--- 90：診斷章與行為章是否混入同一 TC ---
  混入者 = 0

--- 88：ER／步驟中之 CAN 值是否逐字取自條文 ---
  #7 值=['5']（條文：CFTS020-4819353）
  #8 值=['6']（條文：CFTS020-4819353）
  #12 值=['201']（條文：CFTS020-4819347）

--- 四欄行尾句號／方括號 ---
  行尾句號 = 0   方括號 = 0
```

雙向檢查（`check_disclosure.py`）**MISSING 0／STALE 0**。
全批合併之 lint 見上繳 34 §2.3。
