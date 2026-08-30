# `FUNC_STATE_<STATE>` 標準片段（66 包 / R-P387(b)）

> 來源：**`CFTS009-4941453`** —— 規格自帶之狀態表，逐字解析（13 列 × 9 欄）。
> A1 家族（`<X> functionality is (not) available`）之代理量**直接取該表該態之列**，
> 不另造（R-P387(b)）。`PowerSts_Telematic` 之 raw 值取 `VAL_ 1470`（forms BHCAN2）。

> ⚠ **BoosterOUT／天線供電為 (v) 類電氣量測**（R-P387(a)）。
> 其 **ON/OFF 位準值規格未載**（`4941453` 之該欄逐字為
> `ON Refer to {CFTS024} …` / `ON Refer to {VF654} …`），二文件在 G0 台帳外，
> 故該子項一律 **`PENDING: DR-PW27`**，**不得自造位準**（R-P387(a) / §I）。

> ⚠ **星號註腳之定義不在 `4941453` 段內**，而在相鄰之獨立錨點
> （`4941454` / `4941455` = `(*)`；`4941457` = `(**)`；`4941459` = `(***)`）。
> **註腳改變 ER** —— 例如 `Idle` 之 Display 為 `OFF (*)`，而 `(*)` 明載
> Splash Screen 仍顯示，故**不得寫成「畫面全暗」**。已逐格併入。

> ⚠ **`4941453` 有二列 `Full-Operation` 與二列 `Timed`**（音源清單不同：
> 後者多 `SDCARD, BT Music streaming or Phone Call`）—— 本表取其**聯集**，
> 差異記於各該節，**不擇一**（§8.4.1）。

## `FUNC_STATE_FULL_OPERATION`　（`4941453` 之 `Full-Operation` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `TLM plays the audio active source (Tuner, USB, AUX_IN, etc)` | (iii) The audio active source is playing on the HU speakers |
| Audio Power amplifier | `ON (Not muted)` | (iii) The amplifier output is present on the HU speakers |
| Display / Illumination | `ON DCSD follows behavior related to intensity and display st` | (ii) The HU display is on |
| BoosterOUT | `ON` | (v) Measure the voltage at the BoosterOUT output and check that it is the ON level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `ON Refer to {CFTS024} for further details about Antenna powe` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `ON Refer to {VF654} for further details about Antenna power ` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `ON (if present) Refer to {VF652} for further details about U` | (iii) A USB device inserted on the bench is enumerated and can be played |
| MCU (AUX) | `ON (if present) Refer to {VF652} for further details about A` | (iii) The AUX input plays on the HU speakers |

## `FUNC_STATE_IDLE`　（`4941453` 之 `Idle` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `ON (Muted) (***)` | (iii) The amplifier is on and the audio output is muted，**惟 `(***)`（CFTS009-4941459）例外**：with exception of Advanced Driving Assistance System requests |
| Display / Illumination | `OFF (*) DCSD follows behavior related to intensity and displ` | (ii) The HU display is off，**惟 `(*)`（CFTS009-4941454 / CFTS009-4941455）例外**：with exception of: Front_Panel_OnOff.Req icon (i.e. TLM Power button); Splash Screen visualization; HMI Antitheft Screens —— 該例外項須逐一驗其仍可顯示 |
| BoosterOUT | `ON` | (v) Measure the voltage at the BoosterOUT output and check that it is the ON level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `ON Refer to {CFTS024} for further details about Antenna powe` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `ON Refer to {VF654} for further details about Antenna power ` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_PARTIAL_OPERATION`　（`4941453` 之 `Partial Operation` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF(**) DCSD follows behavior related to intensity and displ` | (ii) The HU display is off，**惟 `(**)`（CFTS009-4941457）例外**：with exception of HMI Antitheft Screens —— 該例外項須逐一驗其仍可顯示 |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `ON Refer to {CFTS024} for further details about Antenna powe` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `ON Refer to {VF654} for further details about Antenna power ` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_TIMED`　（`4941453` 之 `Timed` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `TLM plays the audio active source (Tuner, USB, AUX_IN, etc)` | (iii) The audio active source is playing on the HU speakers |
| Audio Power amplifier | `ON (Not muted)` | (iii) The amplifier output is present on the HU speakers |
| Display / Illumination | `ON DCSD follows behavior related to intensity and display st` | (ii) The HU display is on |
| BoosterOUT | `ON` | (v) Measure the voltage at the BoosterOUT output and check that it is the ON level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `ON Refer to {CFTS024} for further details about Antenna powe` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `ON Refer to {VF654} for further details about Antenna power ` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `ON (if present) Refer to {VF652} for further details about U` | (iii) A USB device inserted on the bench is enumerated and can be played |
| MCU (AUX) | `ON (if present) Refer to {VF652} for further details about A` | (iii) The AUX input plays on the HU speakers |

## `FUNC_STATE_STANDBY`　（`4941453` 之 `Standby` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF (**) DCSD follows behavior related to intensity and disp` | (ii) The HU display is off，**惟 `(**)`（CFTS009-4941457）例外**：with exception of HMI Antitheft Screens —— 該例外項須逐一驗其仍可顯示 |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `OFF Refer to {CFTS024} for further details about Antenna pow` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `OFF Refer to {VF654} for further details about Antenna power` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_SLEEP`　（`4941453` 之 `Sleep` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF (**) DCSD powered off, screen off, no backlight` | (ii) The HU display is off，**惟 `(**)`（CFTS009-4941457）例外**：with exception of HMI Antitheft Screens —— 該例外項須逐一驗其仍可顯示 |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `OFF Refer to {CFTS024} for further details about Antenna pow` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `OFF Refer to {VF654} for further details about Antenna power` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_BENCH`　（`4941453` 之 `Bench` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 6 (Bench)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `LTM plays the audio active source (Tuner, USB, AUX_IN or Pho` | (iii) The audio active source is playing on the HU speakers |
| Audio Power amplifier | `ON (Not muted)` | (iii) The amplifier output is present on the HU speakers |
| Display / Illumination | `ON DCSD follows behavior related to intensity and display st` | (ii) The HU display is on |
| BoosterOUT | `ON` | (v) Measure the voltage at the BoosterOUT output and check that it is the ON level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `ON Refer to {CFTS024} for further details about Antenna powe` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `ON Refer to {VF654} for further details about Antenna power ` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the ON level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `ON (if present) Refer to {VF652} for further details about U` | (iii) A USB device inserted on the bench is enumerated and can be played |
| MCU (AUX) | `ON (if present) Refer to {VF652} for further details about A` | (iii) The AUX input plays on the HU speakers |

## `FUNC_STATE_LOGISTIC_IDLE`　（`4941453` 之 `Logistic Idle` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 5 (Logistic_On)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF DCSD powered off, screen off, no backlight` | (ii) The HU display is off |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `OFF` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `OFF` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_LOGISTIC_STANDBY`　（`4941453` 之 `Logistic Standby` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 5 (Logistic_On)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF DCSD powered off, screen off, no backlight` | (ii) The HU display is off |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `OFF` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `OFF` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_LOGISTIC_SLEEP`　（`4941453` 之 `Logistic Sleep` 列）

- **態確認 (i)**：`Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 5 (Logistic_On)`

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF DCSD powered off, screen off, no backlight` | (ii) The HU display is off |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `OFF` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `OFF` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## `FUNC_STATE_INIT`　（`4941453` 之 `Init` 列）

- **態確認**：`Init` 不在 `VAL_ 1470` 之列舉內 → **PENDING: DR-PW26**（同 `ENTER_INIT`，R-P363(c)）

| 欄（`4941453`）| 原值逐字 | ER 子項 |
|---|---|---|
| Source | `OFF (None)` | (iii) No audio source is playing on the HU speakers |
| Audio Power amplifier | `OFF` | (iii) No amplifier output is present on the HU speakers |
| Display / Illumination | `OFF DCSD powered off, screen off, no backlight` | (ii) The HU display is off |
| BoosterOUT | `OFF` | (v) Measure the voltage at the BoosterOUT output and check that it is the OFF level  —— PENDING: DR-PW27 BoosterOUT 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Analog tuner | `OFF` | (v) Measure the voltage at the analog tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 analog tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| Antenna / Digital tuner | `OFF` | (v) Measure the voltage at the digital tuner antenna supply output and check that it is the OFF level  —— PENDING: DR-PW27 digital tuner antenna supply 位準值（CFTS024 / VF654 在台帳外） |
| MCU (USB) | `OFF` | (iii) A USB device inserted on the bench is not enumerated |
| MCU (AUX) | `OFF` | (iii) The AUX input does not play on the HU speakers |

## 重複列

`4941453` 中重複出現之態：Full-Operation、Timed。
二列之差在 `Source` 欄之音源清單（後者多 `SDCARD, BT Music streaming or Phone Call`），
其餘八欄逐字相同。本表取聯集，**差異不擇一**。

## 產出 11 個片段

`FUNC_STATE_FULL_OPERATION`、`FUNC_STATE_IDLE`、`FUNC_STATE_PARTIAL_OPERATION`、`FUNC_STATE_TIMED`、`FUNC_STATE_STANDBY`、`FUNC_STATE_SLEEP`、`FUNC_STATE_BENCH`、`FUNC_STATE_LOGISTIC_IDLE`、`FUNC_STATE_LOGISTIC_STANDBY`、`FUNC_STATE_LOGISTIC_SLEEP`、`FUNC_STATE_INIT`
