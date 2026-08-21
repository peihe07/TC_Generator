# 下放包 16 附件 E：PM 逐列改寫 rows 53–65（逐字可貼）

規則同附件 A–D。本批適用之新增裁決：
- `Ignition Pre Off` = VAL_ **10**（`Ignition_Off` = 2）；
  完整列舉見 `transition_values_from_source.md` §一
- rows 62／63 之 Input 欄已明載目標值，逐字取用（A-PM09 撤銷文件 §2）
- `Front_Panel_OnOff.Req`、`VPLastStatus`、`Rear_View_Camera`、
  `Rear_Camera_Enable.Info`、`Audio_Data_Exchange.Info`、
  `Auto_SwitchOn_Setting.Req`、`Timeout1`、`Response_Wait_Time`
  於 DBC 查無對應 → 保留原名、不加 `$`，PROC 明寫應觀察之值

⚠ **A-PM11**：row 54 之 PRE 原文作 `"Not_Active "`（尾隨空格）、
`Brand_Configuration _2`（底線前空格）；改寫統一為
`Not_Active`／`Brand_Configuration_2`。

---
## row 53
```
PRE:
1. An LTM High Radio is present in the bench configuration
2. Auto_SwitchOn_Setting.Req is Active
3. Timeout1 is 00 MIN
4. Phone_Call.Info is Not_Active
5. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
```
註：轉態值依 CFTS009-4941466（`Ignition Pre Off` OR `Ignition Off`），
本列取 `Ignition_Off`；另一分支由 row 63 承載。

---
## row 54
```
PRE:
1. An LTM High Radio is present in the bench configuration
2. Auto_SwitchOn_Setting.Req is Not_Active
3. Timeout1 is a value other than 00 MIN
4. Brand_Configuration_2 is a value other than Jeep
5. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
3. Read the active audio source and check that the source active before the transition is maintained

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
3. The audio source active before the transition is maintained
```

---
## row 55
```
PRE:
1. The TLM is in Full-Operation state
2. $STATUS_BH_BCM1.OperationalModeSts$ = 10 (Ignition_Pre_Off)
3. Phone_Call.Info is Active
4. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
2. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active)
3. Read RemStartFail and check that it is True

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is sent
2. The signal $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active) is registered without a bus error
3. RemStartFail is True
```
註：PRE 3 依 CFTS009-4941468（`RemStartFail="True"` 之前提為
`Phone_Call.Info == "Active"`）補入，原列未載。

---
## row 56
```
PRE:
1. The TLM is in Full-Operation state
2. Phone_Call.Info is Not_Active
3. LIN and CAN tool is available on HU

PROC:
1. Drive Front_Panel_OnOff.Req from Not_Pressed to Pressed
2. Read VPLastStatus and check that it is OFF
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)

ER:
1. The Front_Panel_OnOff.Req press transition is registered
2. VPLastStatus is OFF
3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
```

---
## row 57
```
PRE:
1. The TLM is in Full-Operation state
2. Phone_Call.Info is Not_Active
3. LIN and CAN tool is available on HU

PROC:
1. Send the signal $CLIMATIC_PANEL.Radio_btn0$ = 0 (Not_Pressed)
2. Send the signal $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed)
3. Read VPLastStatus and check that it is OFF
4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)

ER:
1. The signal $CLIMATIC_PANEL.Radio_btn0$ = 0 (Not_Pressed) is sent
2. The signal $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is registered without a bus error
3. VPLastStatus is OFF
4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
```

---
## row 58
```
PRE:
1. The TLM is in Full-Operation state
2. Phone_Call.Info is Not_Active
3. Rear_View_Camera is Present
4. The Rear Camera is not active
5. LIN and CAN tool is available on HU

PROC:
1. Drive Front_Panel_OnOff.Req from Not_Pressed to Pressed
2. Read VPLastStatus and check that it is OFF
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)

ER:
1. The Front_Panel_OnOff.Req press transition is registered
2. VPLastStatus is OFF
3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
```

---
## row 59
```
PRE:
1. The TLM is in Full-Operation state
2. Phone_Call.Info is Not_Active
3. Rear_View_Camera is Present
4. The Rear Camera is not active
5. LIN and CAN tool is available on HU

PROC:
1. Send the signal $CLIMATIC_PANEL.Radio_btn0$ = 0 (Not_Pressed)
2. Send the signal $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed)
3. Read VPLastStatus and check that it is OFF
4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)

ER:
1. The signal $CLIMATIC_PANEL.Radio_btn0$ = 0 (Not_Pressed) is sent
2. The signal $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is registered without a bus error
3. VPLastStatus is OFF
4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
```

---
## row 60
```
PRE:
1. The TLM is in Full-Operation state
2. Rear_View_Camera is Present
3. The Rear Camera is not active
4. LIN and CAN tool is available on HU

PROC:
1. Make the Rear Camera become active
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
3. Read the TLM screen and check that the rear view camera images are shown
4. Read Rear_Camera_Enable.Info and check that it is True

ER:
1. The Rear Camera becomes active
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
3. The rear view camera images are shown on the TLM screen
4. Rear_Camera_Enable.Info is True
```

---
## row 61
```
PRE:
1. The TLM is in Full-Operation state
2. Rear_View_Camera is Present
3. The Rear Camera is active
4. LIN and CAN tool is available on HU

PROC:
1. Make the Rear Camera become inactive
2. Read the TLM screen and check that the rear view camera images are no longer shown
3. Read the active audio source and check that it is the last active source

ER:
1. The Rear Camera becomes inactive
2. The rear view camera images are no longer shown on the TLM screen
3. The last active source is restored as the active audio source
```
⚠ 原 ER 2 附「according to Audio_Data_Exchange.Info and
Phone_Call.Info values」；該二值之判定規則未見於來源明載，
未寫入判準。若需，標 `PENDING`。

---
## row 62 — Input 內聯（值來自 Input 欄逐字）
```
PRE:
1. The TLM is in Idle state
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
```

---
## row 63 — Input 內聯（Ignition Pre Off = VAL_ 10）
```
PRE:
1. The TLM is in Idle state
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 10 (Ignition_Pre_Off)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)

ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = 10 (Ignition_Pre_Off) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
```

---
## row 64
```
PRE:
1. The TLM is in Idle state
2. Rear_View_Camera is Present
3. Rear_Camera_Enable.Info is True
4. LIN and CAN tool is available on HU

PROC:
1. Drive Front_Panel_OnOff.Req from Not_Pressed to Pressed
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is still 3 (Idle)
3. Read the TLM screen and check that no Splash Screen is shown

ER:
1. The Front_Panel_OnOff.Req press transition is received
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
3. No Splash Screen is shown on the TLM screen
```

---
## row 65
```
PRE:
1. The TLM is in Idle state
2. Rear_Camera_Enable.Info is False
3. LIN and CAN tool is available on HU

PROC:
1. Drive Front_Panel_OnOff.Req from Not_Pressed to Pressed
2. Read the TLM screen and check that a Splash Screen is shown
3. Read VPLastStatus and check that it is ON
4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)

ER:
1. The Front_Panel_OnOff.Req press transition is registered
2. A Splash Screen is shown on the TLM screen for Response_Wait_Time
3. VPLastStatus is ON
4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
```
⚠ `Response_Wait_Time` 之秒數未見於來源，維持符號名，未填數值。
