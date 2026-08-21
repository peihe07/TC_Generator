# R-11 + PM 改寫樣本（2026-08-21，Pei 覆核意見）

Pei 指示三項：一觀察點一步驟／須寫出應觀察之值／Input Test Data
不得放內容。實測：26 行一步多觀察點、**215 行 Read 未寫應觀察值**、
101 列 Input 仍有內容（參數列舉 61／其他 31／訊號值 9）。

## R-11 條文

```
(a) 一個觀察點一個步驟。一步驟不得讀取或檢查 2 個以上訊號、
    參數或狀態；多個觀察對象逐一拆為獨立步驟，ER 逐一對應。
(b) 觀察步驟須寫出應觀察之值：
    `Read the signal $MESSAGE.Signal$ and check that it is <raw> (<label>)`
    非訊號之狀態亦須寫出判準，不得只寫 `Read the X state`。
(c) Input Test Data 一律 `NA`。其內容依性質全數移入：
    起始狀態 → Pre-Condition；驅動值／列舉值 → Procedure 逐值成步；
    判定值 → Expected Result。移動而非刪除。
```

## 樣本一：row 10（內部訊號可觀察化 + 拆步 + 補值）

**現況**
```
pre : 1. A LIN and CAN simulation tool is connected
      The ignition working condition is Ignition On          ← 無編號
      TLM_Status.Info and $Telematic_Power$ read "Full-Operation"  ← 無編號
proc: 1. Read TLM_Status.Info and the TLM power indication          ← 2 觀察點、無值
      2. Read the TLM, AMP, ICS and DTV functionality availability to check that all are available  ← 4 觀察點
er  : 1. The TLM is ON
      2. All TLM, AMP, ICS and DTV functionalities are available
```
**改寫**
```
pre : 1. Ignition state = Ignition_On
      2. A LIN and CAN simulation tool is connected
      3. CAN tool is available on HU
input: NA
proc: 1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
      2. Read the TLM audio output state and check that audio output is active
      3. Read the AMP functionality and check that it is available
      4. Read the ICS functionality and check that it is available
      5. Read the DTV functionality and check that it is available
er  : 1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
      2. The TLM audio output is active
      3. The AMP functionality is available
      4. The ICS functionality is available
      5. The DTV functionality is available
```

## 樣本二：row 11（Input 內聯，四個列舉值逐值成步）

**現況**
```
input: Ignition working conditions: Ignition Pre_Start, Ignition Start,
       Ignition Cranking, Ignition On Engine On
proc : 1. Apply each ignition working condition listed in Input Test Data in turn
       2. Read TLM_Status.Info after each one to check that Full-Operation is kept
```
**改寫**（`OperationalModeSts` 之 VAL_ 恰含此四值：5／6／7／8）
```
input: NA
proc : 1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 5 (Ignition_Pre_Start)
       2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
       3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 6 (Ignition_Start)
       4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
       5. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 7 (Ignition_Cranking)
       6. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
       7. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 8 (Ignition_On_EngOn)
       8. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
er   : 1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 5 (Ignition_Pre_Start) is received
       2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
       3. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 6 (Ignition_Start) is received
       4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
       5. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 7 (Ignition_Cranking) is received
       6. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
       7. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 8 (Ignition_On_EngOn) is received
       8. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
```

## 樣本三：row 12（Pre-Condition 多條件拆行）

**現況** `An SDCARD, a paired BT audio device and an active phone call are available`（一行三條件）
**改寫**
```
pre : 1. Ignition state = Ignition_On and TLM is in Full-Operation
      2. An SDCARD is inserted
      3. A paired BT audio device is connected
      4. An active phone call is in progress
      5. CAN tool is available on HU
```

## 樣本四：row 34（非訊號型 Input 內聯）

**現況** `input: CarPlay request: audio control and video control` ／
`proc 1. Let the CarPlay Device issue the request listed in Input Test Data`
**改寫**
```
input: NA
proc : 1. Let the CarPlay Device issue an audio control request
       2. Read the TLM audio control state and check that the request is accepted
       3. Let the CarPlay Device issue a video control request
       4. Read the TLM video control state and check that the request is accepted
```

## 待 Pei 確認

四樣本之格式若無誤，分析層即以此展開全 283 列改寫；
`PowerSts_Telematic` 一項涵蓋 177 次、`OperationalModeSts` 20 次，
其餘 11 種內部訊號依 12 包 §三走 HMI 可觀察現象或 PENDING。
