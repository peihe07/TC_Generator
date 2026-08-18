# B1 —— 反向涵蓋報告（R-P118）

> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。
> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。
> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。
> 產生指令：`python features/power/scripts/reverse_coverage.py`

## 現況（batch_001_power_down.json，17 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-071 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：001, 002, 003, 004

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | TLM boot requires following timings: After SplashScreen_Time the splash screen | 001 | 0.50 | 已覆蓋 | `cas`、`follow`、`nor`、`only`、`pas`、`requir`、`standby`、`statu`、`these`、`timing` |
| 2 | After StandardScreen_Time the standard screen is visualized on TLM screen | 004 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

### SWE-PM-072 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：005, 006

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Any event occurring during the boot must be recognized by TLM and then TLM has | 006 | 0.42 | **無對應** | `accord`、`behave`、`describ`、`occurr`、`par`、`proces`、`recogniz` |
| 2 | “TLM_Status.Info setting” while the boot is still completing | 005 | 0.50 | 已覆蓋 | `sett`、`tlm_status.info` |
| 3 | TLM must buffer the events and process them as soon as possible, depending on  | 006 | 0.60 | 已覆蓋 | `depend`、`proces`、`them`、`timing` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM_Status.Info`

### SWE-PM-073 —— 行為項 15，已覆蓋 13，無對應 **2**

TC：007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals ar | 007 | 0.81 | 已覆蓋 | `immediately`、`receiv`、`reduce` |
| 2 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 3 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 4 | ICS module shall power down | 007 | 1.00 | 已覆蓋 | （無） |
| 5 | Under fault condition of missing load shed signals on the CAN bus, the last va | 008 | 0.64 | 已覆蓋 | `fault`、`miss`、`under`、`used` |
| 6 | until load shed signal broadcast resumes | 011 | 1.00 | 已覆蓋 | （無） |
| 7 | If the load shed signals do not recover, the on-going load shed action shall b | 008 | 0.77 | 已覆蓋 | `do`、`on-go`、`recover` |
| 8 | The TLM shall transfer the call(not-Ecall/ACN call) to the head set in case a  | 012 | 0.60 | 已覆蓋 | `acn`、`case`、`not-ecall`、`transfer` |
| 9 | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_ | 009 | 0.72 | 已覆蓋 | `mimimize`、`off-tim`、`only`、`receiv`、`withdraw` |
| 10 | TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chim | 007 | 0.82 | 已覆蓋 | `immediately`、`reduce` |
| 11 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 12 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 13 | The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a | 012 | 0.60 | 已覆蓋 | `acn`、`case`、`not-ecall`、`transfer` |
| 14 | Unless defined otherwise, TLM shall stay in this state | 008 | 0.43 | **無對應** | `defin`、`otherwise`、`thi`、`unles` |
| 15 | until either voltage out of range conditions are satisfied or shall go back to | 010 | 0.43 | **無對應** | `back`、`becom`、`behavior`、`either`、`go`、`range`、`satisfi`、`voltage` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**合計**：行為項 **20**，已覆蓋 **17**，無對應 **3**。

---

## 驗證條件 —— 修補前（`b1_before16.json`，10 條 TC，R-P117 之三項缺口尚存）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-071 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：001, 002, 003, 004

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | TLM boot requires following timings: After SplashScreen_Time the splash screen | 001 | 0.50 | 已覆蓋 | `cas`、`follow`、`nor`、`only`、`pas`、`requir`、`standby`、`statu`、`these`、`timing` |
| 2 | After StandardScreen_Time the standard screen is visualized on TLM screen | 004 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

### SWE-PM-072 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：005, 006

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Any event occurring during the boot must be recognized by TLM and then TLM has | 006 | 0.42 | **無對應** | `accord`、`behave`、`describ`、`occurr`、`par`、`proces`、`recogniz` |
| 2 | “TLM_Status.Info setting” while the boot is still completing | 005 | 0.50 | 已覆蓋 | `sett`、`tlm_status.info` |
| 3 | TLM must buffer the events and process them as soon as possible, depending on  | 006 | 0.60 | 已覆蓋 | `depend`、`proces`、`them`、`timing` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM_Status.Info`

### SWE-PM-073 —— 行為項 15，已覆蓋 11，無對應 **4**

TC：007, 008, 009, 010

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals ar | 007 | 0.69 | 已覆蓋 | `alert`、`beep`、`immediately`、`receiv`、`reduce` |
| 2 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 3 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 4 | ICS module shall power down | 007 | 1.00 | 已覆蓋 | （無） |
| 5 | Under fault condition of missing load shed signals on the CAN bus, the last va | 008 | 0.64 | 已覆蓋 | `fault`、`miss`、`under`、`used` |
| 6 | until load shed signal broadcast resumes | 008 | 0.80 | 已覆蓋 | `resum` |
| 7 | If the load shed signals do not recover, the on-going load shed action shall b | 008 | 0.77 | 已覆蓋 | `do`、`on-go`、`recover` |
| 8 | The TLM shall transfer the call(not-Ecall/ACN call) to the head set in case a  | 009 | 0.40 | **無對應** | `call`、`case`、`continu`、`head`、`not-ecall`、`transfer` |
| 9 | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_ | 009 | 0.72 | 已覆蓋 | `mimimize`、`off-tim`、`only`、`receiv`、`withdraw` |
| 10 | TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chim | 007 | 0.64 | 已覆蓋 | `alert`、`beep`、`immediately`、`reduce` |
| 11 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 12 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 13 | The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a | 009 | 0.40 | **無對應** | `call`、`case`、`continu`、`head`、`not-ecall`、`transfer` |
| 14 | Unless defined otherwise, TLM shall stay in this state | 008 | 0.43 | **無對應** | `defin`、`otherwise`、`thi`、`unles` |
| 15 | until either voltage out of range conditions are satisfied or shall go back to | 010 | 0.43 | **無對應** | `back`、`becom`、`behavior`、`either`、`go`、`range`、`satisfi`、`voltage` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`BODY OFF-TIMED`

**合計**：行為項 **20**，已覆蓋 **15**，無對應 **5**。
