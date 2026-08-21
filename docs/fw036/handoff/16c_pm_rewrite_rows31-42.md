# 下放包 16 附件 C：PM 逐列改寫 rows 31–42（逐字可貼）

規則與訊號對照同附件 A／B。本批新增對照：
`RemStActvSts` → `$STATUS_BH_BCM2.RemStActvSts$`
VAL_：0 Remote Start Not Active／1 Remote Start Active
`DriverDoorSts` → `$STATUS_BH_BCM1.DriverDoorSts$`　VAL_：0 Closed／1 Open

⚠ 本批 rows 41–44 之現行 `Send CAN: STATUS_BH_BCM2.RemStActvSts = 1 (…)`
為 R-1 v2 式，一律改 v3 式 `Send the signal $…$ = 1 (…)`。

---
## row 31
```
PRE:
1. The TLM is running normally
2. LIN and CAN tool is available on HU

PROC:
1. Disconnect the battery
2. Read the TLM state and check that it is the INIT state

ER:
1. The battery disconnection is registered
2. The TLM is in the INIT state
```

---
## row 32
```
PRE:
1. The TLM is in the INIT state after a battery disconnection
2. VPLastStatus held a known value before the disconnection
3. SwitchOffSetting.Req held a known value before the disconnection
4. Auto_SwitchOn_Setting.Req held a known value before the disconnection
5. LIN and CAN tool is available on HU

PROC:
1. Reconnect the battery and let the TLM exit the INIT state
2. Read VPLastStatus and check that it is the value held before the disconnection
3. Read SwitchOffSetting.Req and check that it is the value held before the disconnection
4. Read Auto_SwitchOn_Setting.Req and check that it is the value held before the disconnection
5. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)

ER:
1. The TLM exits the INIT state
2. VPLastStatus is the value held before the disconnection
3. SwitchOffSetting.Req is the value held before the disconnection
4. Auto_SwitchOn_Setting.Req is the value held before the disconnection
5. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received
```

---
## row 33
```
PRE:
1. The HU is in Idle state
2. A VR button is available on the bench
3. LIN and CAN tool is available on HU

PROC:
1. Press the VR button with a short press and release it
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)

ER:
1. The VR button short press is accepted
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
```

---
## row 34 — Input 內聯（兩項請求各自成步）
```
PRE:
1. The HU is in Full-Operation state
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
4. LIN and CAN tool is available on HU

PROC:
1. Let the CarPlay Device issue an audio control request
2. Let the CarPlay Device issue a video control request
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
4. Read the entertainment audio state and check that it is unmuted
5. Read the screen state and check that it is on

ER:
1. The audio control request is accepted
2. The video control request is accepted
3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
4. The entertainment audio is unmuted
5. The screen is on
```

---
## row 35 — Input 內聯（僅 audio control）
```
PRE:
1. The HU is in Full-Operation state
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
4. LIN and CAN tool is available on HU

PROC:
1. Let the CarPlay Device issue an audio control request only
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
3. Read the audio state and check that it is unmuted
4. Read the screen state and check that the Screen OFF function is activated

ER:
1. The audio control request is accepted
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
3. The audio is unmuted
4. The Screen OFF function is activated
```

---
## row 36 — Input 內聯（僅 video control）
```
PRE:
1. The HU is in Full-Operation state
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
4. LIN and CAN tool is available on HU

PROC:
1. Let the CarPlay Device issue a video control request only
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
3. Read the audio state and check that it is muted
4. Read the screen state and check that the Screen On function is activated

ER:
1. The video control request is accepted
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
3. The audio is muted
4. The Screen On function is activated
```

---
## row 37 — Input 內聯（兩者皆無）
```
PRE:
1. The HU is in Full-Operation state
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
4. LIN and CAN tool is available on HU

PROC:
1. Let the CarPlay Device issue a request with neither audio control nor video control
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)

ER:
1. The request is accepted and the HU leaves Full-Operation state
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
```

---
## row 38
```
PRE:
1. The HU is in Idle state
2. A VR button is available on the bench
3. LIN and CAN tool is available on HU

PROC:
1. Press the VR button with a long press and release it
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)

ER:
1. The VR button long press is accepted
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
```

---
## row 39
```
PRE:
1. VPLastStatus holds a known value
2. SwitchOffSetting.Req holds a known value
3. Auto_SwitchOn_Setting.Req holds a known value
4. The battery is disconnected
5. LIN and CAN tool is available on HU

PROC:
1. Reconnect the battery and let the voltage settle within its thresholds
2. Read the TLM state and check that it has left the INIT state
3. Read VPLastStatus and check that it is the value held before the disconnection
4. Read SwitchOffSetting.Req and check that it is the value held before the disconnection
5. Read Auto_SwitchOn_Setting.Req and check that it is the value held before the disconnection

ER:
1. The voltage settles within its thresholds
2. The TLM has left the INIT state
3. VPLastStatus is the value held before the disconnection
4. SwitchOffSetting.Req is the value held before the disconnection
5. Auto_SwitchOn_Setting.Req is the value held before the disconnection
```
⚠ 電壓門檻之具體值未見於來源，未填數值。

---
## row 40
```
PRE:
1. The battery has just been reconnected
2. LIN and CAN tool is available on HU

PROC:
1. Let the TLM exit the INIT state
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)

ER:
1. The TLM leaves the INIT state without an error being reported
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received
```

---
## row 41
```
PRE:
1. Ignition state = Ignition_On
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation) is received
```

---
## row 42
```
PRE:
1. Ignition state = Ignition_Pre_Start
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation) is received
```
