# 下放包 16 附件 D：PM 逐列改寫 rows 43–52（逐字可貼）

規則與訊號對照同附件 A–C。本批新增：
`Phone_Call.Info`／`SwitchOff_Timeout_Setting.Req`／`RemStartFail`／
`Brand_Configuration_2`／`Timeout1` 於 DBC 查無對應，依 R-1 v3(d)
保留原名（不加 `$`），並於 PROC 明寫應觀察之值。
`LTM_OperationalModeSts.Info` → `$STATUS_BH_BCM1.OperationalModeSts$`
（VAL_ 2 Ignition_Off／4 Ignition_On／…）。

⚠ **A-PM08 登記**：row 51 之 PRE 原文作 `Brand_Configuration _2`
（底線前多一空格）；改寫統一為 `Brand_Configuration_2`。

---
## row 43
```
PRE:
1. Ignition state = Ignition_Cranking
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation) is received
```

---
## row 44
```
PRE:
1. Ignition state = Ignition_On_EngOn
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation) is received
```

---
## row 45
```
PRE:
1. The TLM is in Partial_Operation state
2. The unit is equipped with AMP
3. The unit is equipped with ICS
4. The unit is equipped with DTV
5. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)
2. Read the AMP power state and check that it is off
3. Read the ICS power state and check that it is off
4. Read the DTV power state and check that it is off
5. Read the ANC audio output and check that it is active
6. Read the ACN audio output and check that it is active
7. Read the chime audio output and check that it is active

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation) is received
2. The AMP is off
3. The ICS is off
4. The DTV is off
5. The ANC audio output is active
6. The ACN audio output is active
7. The chime audio output is active
```

---
## row 46
```
PRE:
1. The TLM is in Partial_Operation state
2. LIN and CAN tool is available on HU

PROC:
1. Attempt an HMI interaction that does not change the TLM status and check that it is rejected
2. Attempt an HMI interaction that changes the TLM status and check that it is accepted
3. Read the TLM functionality state and check that the functionalities run in background

ER:
1. The HMI interaction that does not change the TLM status is rejected
2. The HMI interaction that changes the TLM status is accepted
3. The TLM functionalities run in background
```

---
## row 47
```
PRE:
1. The TLM is in Full-Operation state
2. Ignition state = Ignition_Off
3. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
2. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active)
3. Read RemStartFail and check that it is True

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is sent
2. The signal $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active) is registered without a bus error
3. RemStartFail is True
```

---
## row 48
```
PRE:
1. RemStartFail is True
2. Phone_Call.Info is Not_Active
3. LIN and CAN tool is available on HU

PROC:
1. Let the TLM evaluate the call state after the RemStartFail transition
2. Read Phone_Call.Info and check that it is Not_Active
3. Read RemStartFail and check that it is False

ER:
1. The TLM evaluates the call state
2. Phone_Call.Info is Not_Active
3. RemStartFail is False
```
⚠ 原 ER 2 僅載 `RemStartFail reads "False"`，未及 TLM_Status.Info；
原 PROC 2 列 `TLM_Status.Info` 為觀察對象但 ER 無對應，屬 proc／ER
不對齊（A-PM05 型）。改寫以 ER 為準，未保留 TLM_Status.Info 觀察點。

---
## row 49
```
PRE:
1. SwitchOff_Timeout_Setting.Req is 00 MIN
2. Timeout1 is 00 MIN
3. Phone_Call.Info is Not_Active
4. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
```
⚠ 原 PROC 1 `Let LTM_OperationalModeSts.Info transition occur` 未指明
轉往何值；依該列 PRE 情境（切換至關機流程）與 R-1 v3(d) 改為明確
送出 `= 2 (Ignition_Off)`。**此為分析層依情境所定，非來源明載**，
若與規格不符請於覆核時退回。

---
## row 50
```
PRE:
1. SwitchOff_Timeout_Setting.Req is 00 MIN
2. Timeout1 is 00 MIN
3. Phone_Call.Info is Active
4. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
3. Set Phone_Call.Info to Not_Active
4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is no longer 2 (Timed)

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
3. Phone_Call.Info is Not_Active
4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ is no longer 2 (Timed)
```
⚠ 原 ER 2 述「stays there until Phone_Call.Info becomes Not_Active」，
其驗證需一離開步驟；改寫據此補 PROC 3／4，未新增數值。

---
## row 51
```
PRE:
1. SwitchOff_Timeout_Setting.Req is a value other than 00 MIN
2. Timeout1 is a value other than 00 MIN
3. Brand_Configuration_2 is Jeep
4. Phone_Call.Info is Not_Active
5. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.DriverDoorSts$ = 1 (Open)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)

ER:
1. The signal $STATUS_BH_BCM1.DriverDoorSts$ = 1 (Open) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
```

---
## row 52
```
PRE:
1. SwitchOff_Timeout_Setting.Req is a value other than 00 MIN
2. Timeout1 is a value other than 00 MIN
3. Brand_Configuration_2 is a value other than Jeep
4. A tuner source is currently active
5. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
3. Read the active audio source and check that the tuner source is maintained

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
3. The tuner source is maintained as the active audio source
```
