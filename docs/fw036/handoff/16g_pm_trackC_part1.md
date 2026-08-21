# 附件 G：軌 C 逐列改寫（1/2）rows 124–127、149、233、234、265–270

**軌 C 原則**：值一律取自 CFTS 原文，每列註明所據 object id
（Pei 裁定路線 c）。定位鏈：036 `Requirement or Design ID`
→ 037「SWE1 Requirements」`Source Requirement ID`
→ SYS2「Basic Report」→ CFTS object。

VAL_ 對照：`$STATUS_TELEMATIC.PowerSts_Telematic$`
0 Sleep／1 Standby／2 Timed／3 Idle／4 Full_Operation／
5 Logistic_On／6 Bench／7 Partial_Operation
`$STATUS_BH_BCM1.OperationalModeSts$`
2 Ignition_Off／4 Ignition_On／5 Ignition_Pre_Start／
6 Ignition_Start／7 Ignition_Cranking／8 Ignition_On_EngOn／
**10 Ignition_Pre_Off**

**Pei 裁定**：`PowerModeSts_Telematic` 一律改
`$STATUS_TELEMATIC.PowerSts_Telematic$`；`PowerModeSts` 不使用。

---
## row 124 — SWE-PM-041（Ignition_Off 分支）
來源：`CFTS009-4941410`（Ignition Pre Off, Ignition Off）／
`CFTS009-4941411`（TLM OFF with **Network on** → Standby）／
`CFTS009-4941412`（No TLM, FPDM, AMP, ICS, DTV available）
```
PRE:
1. The TLM is in an operative state
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)
3. Read the network state and check that the network is on
4. Read the TLM functionality and check that it is not available
5. Read the FPDM functionality and check that it is not available
6. Read the AMP functionality and check that it is not available
7. Read the ICS functionality and check that it is not available
8. Read the DTV functionality and check that it is not available

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
3. The network is on
4. The TLM functionality is not available
5. The FPDM functionality is not available
6. The AMP functionality is not available
7. The ICS functionality is not available
8. The DTV functionality is not available
```

---
## row 125 — SWE-PM-041（Ignition_Pre_Off 分支）
與 row 124 逐字相同，**僅 PROC 1 與 ER 1 之值改為
`= 10 (Ignition_Pre_Off)`**。
```
PROC 1: Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 10 (Ignition_Pre_Off)
ER   1: The signal $STATUS_BH_BCM1.OperationalModeSts$ = 10 (Ignition_Pre_Off) is registered without a bus error
```
（PROC 2–8、ER 2–8、PRE 全數同 row 124）

---
## row 126 — SWE-PM-042（Ignition_Off 分支）
來源：`CFTS009-4941416`／`CFTS009-4941417`（TLM OFF with
**Network off** → Sleep）／`CFTS009-4941418`
與 row 124 相同，**兩處差異**：
```
PROC 2: Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)
PROC 3: Read the network state and check that the network is off
ER   2: The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received
ER   3: The network is off
```
（其餘同 row 124）

---
## row 127 — SWE-PM-042（Ignition_Pre_Off 分支）
同 row 126，**PROC 1／ER 1 之值改 `= 10 (Ignition_Pre_Off)`**。

---
## row 149 — SWE-PM-053
來源：`CFTS009-4941668`「TLM has to read Brand_Configuration_2 PROXI
parameter in order to show the vehicle brand logo screen」
```
PRE:
1. Brand_Configuration_2 is set to a known vehicle brand value
2. LIN and CAN tool is available on HU

PROC:
1. Power up the TLM and let the brand logo screen be presented
2. Read the TLM screen and check that the brand logo screen is shown
3. Read the shown vehicle brand logo and check that it matches the Brand_Configuration_2 value

ER:
1. The brand logo screen is presented
2. The brand logo screen is shown on the TLM screen
3. The shown vehicle brand logo matches the Brand_Configuration_2 value
```

---
## row 233 — SWE-PM-091
來源：`CFTS009-4942105`「If the "Theme Mode" setting is set to "Day"
the HU shall use the Day theme」
```
PRE:
1. The HU is in Full-Operation state
2. HMI: "Theme Mode" is set to "Day"
3. LIN and CAN tool is available on HU

PROC:
1. Open the screen on which the theme is applied
2. Read the applied theme and check that it is the Day theme

ER:
1. The screen on which the theme is applied is shown
2. The HU uses the Day theme
```

---
## row 234 — SWE-PM-092
來源：`CFTS009-4942107`（同式，Night）
同 row 233，**PRE 2 改 `HMI: "Theme Mode" is set to "Night"`；
PROC 2 與 ER 2 之 `Day theme` 改 `Night theme`**。

---
## rows 265／266／267／268 — SWE-PM-103（四列同文）
來源：`CFTS009-4941364`（Ignition On／Pre_Start／Start／Cranking／
On Engine On 條件）／`CFTS009-4941365`「This status is related to
**TLM audio is OFF**. TLM shall allow only Splash Screen visualization
on its display. ICS functionalities are available. DTV shall be OFF」
→ 該狀態即 **Idle（3）**（與 rows 13／14 之 PRE 所載一致）
```
PRE:
1. The TLM is in Idle state
2. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)
2. Read the TLM audio output state and check that audio output is off
3. Read the TLM display and check that only the Splash Screen is shown

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
2. The TLM audio output is off
3. Only the Splash Screen is shown on the TLM display
```
⚠ **A-PM13**：本四列 PROC／ER 逐字相同，且與 row 13 同文，
合計 5 列驗證同一行為，屬 §10.6 strict equivalence 重複。
**拆併屬 Pei，本包照原列數各自寫入，不合併、不刪列。**

---
## row 269 — SWE-PM-103
來源同上（`CFTS009-4941365` 之後半：ICS available／DTV OFF）
```
PRE:
1. The TLM is in Idle state
2. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)
2. Read the ICS functionality and check that it is available
3. Read the DTV state and check that it is off

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
2. The ICS functionality is available
3. The DTV is off
```

---
## row 270 — SWE-PM-104
來源：`CFTS009-4941950`「The splash screen and disclaimer screen shall
be shown **the first time each bus cycle** the HU transitions to
**Timed or Full Operation** modes」
```
PRE:
1. The TLM is in Idle state
2. No transition to Timed or Full-Operation has occurred in the current bus cycle
3. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to Timed mode
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
3. Read the TLM screen and check that the splash screen is shown
4. Read the TLM screen and check that the disclaimer screen is shown after the splash screen

ER:
1. The HU reaches Timed mode
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
3. The splash screen is shown on the TLM screen
4. The disclaimer screen is shown on the TLM screen after the splash screen
```
⚠ 進入 Timed 之**觸發訊號原文未載**（4941950 僅述「transitions to
Timed」而未指定觸發來源）。PROC 1 保留 `Bring the HU to Timed mode`
之抽象動作，**不填推定之觸發訊號**（路線 c）。
若需具體觸發，標 `PENDING: DR-{n}`。
