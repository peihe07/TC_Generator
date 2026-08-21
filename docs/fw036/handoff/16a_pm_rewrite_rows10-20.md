# 下放包 16 附件 A：PM 逐列改寫 rows 10–20（示範批，逐字可貼）

規則依據：R-1 v3（訊號 `$MESSAGE.Signal$` + 值 + DBC VAL_ 標籤）、
R-9（PC 一條件一行一編號、工具行置末）、R-11（一觀察點一步驟、
須寫出應觀察之值、Input 一律 NA）、R-12(a)（`<工具> is available on HU`）。
訊號對照：`TLM_Status.Info` → `$STATUS_TELEMATIC.PowerSts_Telematic$`
（VAL_ 0 Sleep／1 Standby／2 Timed／3 Idle／4 Full_Operation／
5 Logistic_On／6 Bench／7 Partial_Operation）；
`LTM_OperationalModeSts.Info` → `$STATUS_BH_BCM1.OperationalModeSts$`
（4 Ignition_On／5 Ignition_Pre_Start／6 Ignition_Start／
7 Ignition_Cranking／8 Ignition_On_EngOn）。
`$Telematic_Power$` 為 PROXI 以外之電源狀態指涉，逐列一併改為
`$STATUS_TELEMATIC.PowerSts_Telematic$`（與 TLM_Status.Info 同一對象，
A-PM07 登記：二者於原本並列出現 129 行，實為同一狀態之兩種寫法）。

各列以三段呈現：`PRE:` `PROC:` `ER:`；`INPUT:` 一律 `NA` 不重列。
**逐字取代整欄**，不得部分套用。

---
## row 10 (NR1L-PowerManagement-001)
```
PRE:
1. Ignition state = Ignition_On
2. The TLM is in Full-Operation state
3. LIN and CAN tool is available on HU

PROC:
1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
2. Read the TLM audio output state and check that audio output is active
3. Read the AMP functionality and check that it is available
4. Read the ICS functionality and check that it is available
5. Read the DTV functionality and check that it is available

ER:
1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
2. The TLM audio output is active
3. The AMP functionality is available
4. The ICS functionality is available
5. The DTV functionality is available
```

---
## row 11 (NR1L-PowerManagement-002) — Input 內聯，四值逐值成步
```
PRE:
1. The TLM is in Full-Operation state
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 5 (Ignition_Pre_Start)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 6 (Ignition_Start)
4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
5. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 7 (Ignition_Cranking)
6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
7. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 8 (Ignition_On_EngOn)
8. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)

ER:
1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 5 (Ignition_Pre_Start) is received without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
3. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 6 (Ignition_Start) is received without a bus error
4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
5. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 7 (Ignition_Cranking) is received without a bus error
6. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
7. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 8 (Ignition_On_EngOn) is received without a bus error
8. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
```

---
## row 12 (NR1L-PowerManagement-003) — PC 三條件拆行
```
PRE:
1. The TLM is in Full-Operation state
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
## row 13 (NR1L-PowerManagement-004)
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

---
## row 14 (NR1L-PowerManagement-005)
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
## row 15 (NR1L-PowerManagement-006)
```
PRE:
1. The TLM is in Idle state
2. LIN and CAN tool is available on HU

PROC:
1. Request the rear view camera images
2. Read the TLM display and check that the rear view camera images are shown

ER:
1. The rear view camera image request is registered without a bus error
2. The rear view camera images are shown on the TLM display
```

---
## row 16 (NR1L-PowerManagement-007)
```
PRE:
1. The TLM is in Idle state
2. LIN and CAN tool is available on HU

PROC:
1. Attempt a user setting on the TLM and check that it is rejected
2. Attempt an HMI interaction other than the TLM Power button and check that it is rejected
3. Press the TLM Power button and check that the press is accepted

ER:
1. The user setting is rejected
2. The HMI interaction other than the TLM Power button is rejected
3. The TLM Power button press is accepted
```

---
## row 17 (NR1L-PowerManagement-008)
```
PRE:
1. Ignition state = Ignition_On
2. LIN and CAN tool is available on HU

PROC:
1. Send CAN: STATUS_BH_BCM2.RemStActvSts = 1 (Remote Start Active)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 7 (Partial_Operation)
3. Read the AMP state and check that it is off
4. Read the ICS state and check that it is off
5. Read the DTV state and check that it is off

ER:
1. The signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 7 (Partial_Operation) is received
3. The AMP is off
4. The ICS is off
5. The DTV is off
```
⚠ step 1 之現行寫法 `Send CAN: …` 係 R-1 v2 產物；依 R-1 v3
改為 `Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)`。
上表 PROC 1 已為 v2 式，**應改用 v3 式**，ER 1 已為 v3 式。

---
## row 18 (NR1L-PowerManagement-009) — PC 三條件拆行
```
PRE:
1. The TLM is in Partial_Operation state
2. The unit is equipped with ANC
3. The unit is equipped with ACN
4. The unit is equipped with chimes
5. LIN and CAN tool is available on HU

PROC:
1. Read the ANC audio output and check that it is active
2. Read the ACN audio output and check that it is active
3. Read the chime audio output and check that it is active

ER:
1. The ANC audio output is active
2. The ACN audio output is active
3. The chime audio output is active
```

---
## row 19 (NR1L-PowerManagement-010)
```
PRE:
1. The TLM is in Partial_Operation state
2. LIN and CAN tool is available on HU

PROC:
1. Attempt an HMI interaction that does not change the TLM status and check that it is rejected
2. Attempt an HMI interaction that changes the TLM status and check that it is accepted

ER:
1. The HMI interaction that does not change the TLM status is rejected
2. The HMI interaction that changes the TLM status is accepted
```

---
## row 20 (NR1L-PowerManagement-011)
```
PRE:
1. The TLM is in an operative state
2. LIN and CAN tool is available on HU

PROC:
1. Attempt to bring the HU into stolen vehicle mode
2. Read the HU mode and check that it is not stolen vehicle mode

ER:
1. The attempt to enter stolen vehicle mode is rejected
2. The HU mode is not stolen vehicle mode
```

---
## 本批未決事項（不得自行填補）

- row 15／16／19／20 之「rejected／accepted」判準未見於來源；
  沿用原 ER 語意改寫，未新增數值。若需具體判準，標
  `PENDING: DR-{n}` 由分析層補。
- row 18 之 ANC／ACN／chimes 是否有對應 CAN 訊號未查證，
  暫以音訊輸出可觀察現象書寫。
- spec_reference 欄**本批不動**（A-PM06 凍結）。
