# 下放包 16 附件 B：PM 逐列改寫 rows 21–30（逐字可貼）

規則同附件 A。訊號對照：
`TLM_Status.Info` ／ `$Telematic_Power$`（同一狀態之兩種寫法，
A-PM07）→ `$STATUS_TELEMATIC.PowerSts_Telematic$`
VAL_：0 Sleep／1 Standby／2 Timed／3 Idle／4 Full_Operation／
5 Logistic_On／6 Bench／7 Partial_Operation
`LTM_OperationalModeSts.Info` → `$STATUS_BH_BCM1.OperationalModeSts$`
VAL_：2 Ignition_Off／4 Ignition_On／5 Ignition_Pre_Start／
6 Ignition_Start／7 Ignition_Cranking／8 Ignition_On_EngOn

`Antitheft_Activation.Req`、`SwitchOff_Timeout_Setting.Req`、
`Auto_SwitchOn_Setting.Req`、`VPLastStatus`、`RemStartFail`
於 DBC 查無對應（12 包 §三），依 R-1 v3(d) 以 HMI／可觀察現象
書寫，**保留原名作為狀態名稱但不加 `$`**，並於 PROC 明寫應觀察之值。

---
## row 21 (NR1L-PowerManagement-012)
```
PRE:
1. Ignition state = Ignition_Off
2. The TLM is in Timed state
3. Timeout1 is configured to a value other than 00 min
4. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
2. Read the AMP functionality and check that it is available
3. Read the ICS functionality and check that it is available
4. Read the DTV functionality and check that it is available
5. Wait until Timeout1 has elapsed
6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is no longer 2 (Timed)

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
2. The AMP functionality is available
3. The ICS functionality is available
4. The DTV functionality is available
5. Timeout1 has elapsed
6. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ is no longer 2 (Timed)
```
⚠ Timeout1 之具體秒數未見於來源，未填數值；PRE 3 僅述其非 00 min，
與原 PC 語意一致。

---
## row 22 (NR1L-PowerManagement-013)
```
PRE:
1. The TLM is in Timed state
2. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
2. Attempt to open a Customer setting screen and check that it is rejected

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
2. The Customer setting screen is not opened
```

---
## row 23 (NR1L-PowerManagement-014) — 同 row 12 結構，狀態為 Timed
```
PRE:
1. The TLM is in Timed state
2. An SDCARD is inserted
3. A paired BT audio device is connected
4. An active phone call is available
5. LIN and CAN tool is available on HU

PROC:
1. Select SDCARD as the audio active source
2. Read the played audio source and check that it is the SDCARD
3. Select BT Music streaming as the audio active source
4. Read the played audio source and check that it is the BT Music streaming
5. Place a phone call
6. Read the played audio source and check that it is the phone call

ER:
1. The SDCARD is selected as the audio active source
2. The TLM plays the SDCARD as the audio active source
3. The BT Music streaming is selected as the audio active source
4. The TLM plays the BT Music streaming as the audio active source
5. The phone call is established
6. The TLM plays the phone call as the audio active source
```

---
## row 24 (NR1L-PowerManagement-015)
```
PRE:
1. The TLM is in Standby state
2. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)
2. Read the network state and check that the network is on
3. Read the TLM functionality and check that it is not available
4. Read the FPDM functionality and check that it is not available
5. Read the AMP functionality and check that it is not available
6. Read the ICS functionality and check that it is not available
7. Read the DTV functionality and check that it is not available

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
2. The network is on
3. The TLM functionality is not available
4. The FPDM functionality is not available
5. The AMP functionality is not available
6. The ICS functionality is not available
7. The DTV functionality is not available
```

---
## row 25 (NR1L-PowerManagement-016)
```
PRE:
1. Antitheft_Activation.Req is set to True
2. The TLM is about to enter Standby
3. LIN and CAN tool is available on HU

PROC:
1. Let the TLM enter Standby
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)
3. Read Antitheft_Activation.Req and check that it is False

ER:
1. The TLM enters Standby
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received
3. Antitheft_Activation.Req is False
```

---
## row 26 (NR1L-PowerManagement-017)
```
PRE:
1. The TLM is in Sleep state
2. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)
2. Read the network state and check that the network is off
3. Read the TLM functionality and check that it is not available
4. Read the FPDM functionality and check that it is not available
5. Read the AMP functionality and check that it is not available
6. Read the ICS functionality and check that it is not available
7. Read the DTV functionality and check that it is not available

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received
2. The network is off
3. The TLM functionality is not available
4. The FPDM functionality is not available
5. The AMP functionality is not available
6. The ICS functionality is not available
7. The DTV functionality is not available
```

---
## row 27 (NR1L-PowerManagement-018)
```
PRE:
1. Antitheft_Activation.Req is set to True
2. The TLM is about to enter Sleep
3. LIN and CAN tool is available on HU

PROC:
1. Let the TLM enter Sleep
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)
3. Read Antitheft_Activation.Req and check that it is False

ER:
1. The TLM enters Sleep
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received
3. Antitheft_Activation.Req is False
```

---
## row 28 (NR1L-PowerManagement-019)
```
PRE:
1. Ignition state = Ignition_Off
2. The Engineering Line is activated
3. LIN and CAN tool is available on HU

PROC:
1. Bring the TLM to the Bench state
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 6 (Bench)
3. Read the AMP state and check that it is on
4. Read the ICS state and check that it is on
5. Read the DTV state and check that it is on

ER:
1. The TLM reaches the Bench state
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 6 (Bench) is received
3. The AMP is on
4. The ICS is on
5. The DTV is on
```

---
## row 29 (NR1L-PowerManagement-020)
```
PRE:
1. Ignition state = Ignition_Off
2. The Engineering Line is activated
3. The TLM is in Bench state
4. LIN and CAN tool is available on HU

PROC:
1. Read the audio power amplifier state and check that it is on and not muted
2. Read the BoosterOUT state and check that it is on
3. Read the analog antenna supply and check that it is on
4. Read the digital antenna supply and check that it is on
5. Read the USB MCU state and check that it is on
6. Read the AUX MCU state and check that it is on

ER:
1. The audio power amplifier is on and not muted
2. The BoosterOUT is on
3. The analog antenna supply is on
4. The digital antenna supply is on
5. The USB MCU is on
6. The AUX MCU is on
```
⚠ 原 ER 3 附 `when present` 之條件語；USB／AUX MCU 之存在與否
屬配置條件，未見來源明載判準，未寫入 PRE。若需，標 `PENDING`。

---
## row 30 (NR1L-PowerManagement-021) — 一步六觀察點，拆為六步
```
PRE:
1. The unit carries the ex-factory configuration
2. LIN and CAN tool is available on HU

PROC:
1. Power up the TLM for the first time
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 0 (Sleep)
3. Read VPLastStatus and check that it is On
4. Read SwitchOff_Timeout_Setting.Req and check that it is 00 min
5. Read Auto_SwitchOn_Setting.Req and check that it is Recall_Last
6. Read Antitheft_Activation.Req and check that it is False
7. Read RemStartFail and check that it is False

ER:
1. The TLM is powered up for the first time
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 0 (Sleep) is received
3. VPLastStatus is On
4. SwitchOff_Timeout_Setting.Req is 00 min
5. Auto_SwitchOn_Setting.Req is Recall_Last
6. Antitheft_Activation.Req is False
7. RemStartFail is False
```
