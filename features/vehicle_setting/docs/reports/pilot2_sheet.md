# pilot #2 —— review sheet（15 條）

依 `docs/handoff/48_review_round28.md` §3 之抽法產出，29 輪 W-84。

## 抽法（可複現）

母體：**68 條**（已生成 76 − 已 PASS 8）。

分層維度：**Layer 2（四層）× design_method（五類）**。
抽樣：**非空交叉格內各取其 reqid 最小者**；空格跳過。實測非空格 **12** → 恰 12 條，無須補足。

| Layer 2 ＼ design_method | Decision Table | Equivalence Partitioning | Functional Based | Negative / Invalid | State Transition |
|---|---:|---:|---:|---:|---:|
| Common Features | 2 | 1 | 10 | 2 | 18 |
| Heated Seat | — | — | — | — | 4 |
| Heated Steering Wheel | — | 1 | — | 1 | 9 |
| Vented Seat | — | 2 | — | 2 | 16 |

必檢 3（非抽樣）：`LeftFrontHeatedSeat-014`／`RightFrontHeatedSeat-031`（`dr15_exposed = yes`）、
`HeatedSteeringWheel-021`（`duplicate_of` 之一）。

**合計 15 條。**

---

## 1. `SWE1-VC-StopStartSystemBehavior-054`

| 欄 | 值 |
|---|---|
| batch | `batch10` |
| test_set | Common Features |
| design_method | Decision Table |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Engine off in stop mode retains the seat button state

**test_item**

```text
IF (STATUS_CCAN3.EngineSts == "Engine_Off" AND STATUS_CCAN3.ESS_ENG_ST != "ENS_DSBL")THEN- The HU shall retain the existing state and level of the Heated/Vented Seats or Heated Steering Wheel button(s)

(Engine off, stop-start not disabled)
```

**pre_conditions**

```text
1. PROXI Stop_And_Start_cfg = 1 (Present)
2. The Heated / Vented Seats screen is displayed
3. The ignition is in the Ignition On condition
4. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CCAN3.ESS_ENG_ST$ = 3 (ENS Running)
2. Activate the vented seat button and record its state and level
3. Send the signal $STATUS_CCAN3.EngineSts$ = 0 (Engine_Off) and check that the vented seat button state and level are the same as recorded in step 2
```

**expected_result**

```text
1. The signal $STATUS_CCAN3.ESS_ENG_ST$ = 3 (ENS Running) is registered without a bus error
2. The vented seat button is active and its state and level are recorded
3. The vented seat button state and level are the same as recorded in step 2
```

**specification_reference**

```text
CFTS044-4859504
```

**distinguishing_axis**

`trigger_state` —— 本列之 ESS_ENG_ST = 3 (ENS Running)（非 ENS disabled），期望狀態保留；-055 之 ESS_ENG_ST = 7 (ENS disabled)，期望按鍵灰階。

**來源條文逐字**

- `4859504`：This functionality is implemented if PROXI parameter $Stop_And_Start_cfg$ = [Present].During the Ignition Working Conditions:• Ignition On• Ignition On Engine OnIF (STATUS_CCAN3.EngineSts == “Engine_Off” AND STATUS_CCAN3.ESS_ENG_ST != “ENS_DSBL”)THEN- The HU shall retain the existing state and level of the Heated/Vented Seats or Heated Steering Wheel button(s);- The HU shall allow the vented seats buttons to be selectable, as defined in Section ‘Vented Seats’;- The HU shall allow the heated steering wheel buttons to be selectable, as defined in Section ‘Heated Steering Wheel’;

---

## 2. `SWE1-VC-SwitchLHD/RHDConfiguration-012`

| 欄 | 值 |
|---|---|
| batch | `batch08` |
| test_set | Common Features |
| design_method | Equivalence Partitioning |
| priority | P1 |
| dr15_exposed | **no**　驗證對象為畫面圖示狀態之不變，未斷言請求訊號之編碼；`DrvSeatHeating.Req` 為內部訊號，依 §8.7.5(d) 保留來源名不加 `$` |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Right-hand drive without labels leaves seat heating request unchanged

**test_item**

```text
Wherever there is no Driver or Passenger label for Heated and Vented seats, the $DriverSide$ signal value shall have no impact on the Heated and Vented seat switch behavior.

(Right-hand drive, no Driver or Passenger label)
```

**pre_conditions**

```text
1. The heated and vented seat switches carry no Driver or Passenger label
2. The Heated / Vented Seats screen is reachable from the Menu Bar
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Set PROXI Driver_Side = 0 (Left Side) and power cycle the HU
2. Drive DrvSeatHeating.Req to Requested by pressing the left front heated seat switch and record the resulting heated seat icon status
3. Set PROXI Driver_Side = 1 (Right Side) and power cycle the HU
4. Drive DrvSeatHeating.Req to Requested by pressing the left front heated seat switch and check that the resulting heated seat icon status is the same as recorded in step 2
```

**expected_result**

```text
1. The HU completes start-up with PROXI Driver_Side = 0 (Left Side)
2. The heated seat icon status is recorded
3. The HU completes start-up with PROXI Driver_Side = 1 (Right Side)
4. The heated seat icon status is the same as recorded in step 2
```

**specification_reference**

```text
CFTS044-4859508
```

**distinguishing_axis**

`trigger_state` —— 本列以 `DrvSeatHeating.Req` 之內部訊號路徑觸發、驗畫面圖示不變；batch01_v3 之 SwitchLHD/RHD-009 以 `$TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$` 之匯流排值為驗證對象。

**來源條文逐字**

- `4859508`：Wherever there is no Driver or Passenger label for Heated and Vented seats, the $DriverSide$ signal value shall have no impact on the Heated and Vented seat switch behavior. As an example, when $DriverSide$ = [Right Drive] and the customer selects DrvSeatHeating.Req in CFTS044-3023/1787/2585 or the left heated seat in CFTS044-2585, the HU shall send the on-change $FL_HS_RQ$= [Pressed] or TELEMATIC_CLIMATE_SETUP.FL_HS_Cmd_Tlm = [Pressed] or TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm depeding of the current status as defined in each section.

---

## 3. `SWE1-VC-HeatedSteeringWheelManagement-027`

| 欄 | 值 |
|---|---|
| batch | `batch03` |
| test_set | Common Features |
| design_method | Functional Based |
| priority | P2 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Right-hand drive mirrors the heated steering wheel icon to the right

**test_item**

```text
If $DriverSide$ = [Right Side], the HU shall mirror the location of the Heated Steering Wheel Icon, showing it in the right side of the Heated / Vented Seats screen.

(Right-hand drive icon placement)
```

**pre_conditions**

```text
1. The vehicle is equipped with a heated steering wheel
2. PROXI Driver_Side = 0 (Left Side)
3. The Heated / Vented Seats screen is displayed
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Read the position of the heated steering wheel icon on the Heated / Vented Seats screen and record it
2. Set PROXI Driver_Side = 1 (Right Side)
3. Power cycle the HU so that the configuration is applied
4. Open the Heated / Vented Seats screen and check that the heated steering wheel icon is on the opposite side from the position recorded in step 1
```

**expected_result**

```text
1. The position of the heated steering wheel icon is recorded
2. PROXI Driver_Side = 1 (Right Side) is accepted
3. The HU completes start-up
4. The heated steering wheel icon is shown on the right side of the Heated / Vented Seats screen, mirrored from the position recorded in step 1
```

**specification_reference**

```text
CFTS044-4858299
CFTS044-4859494
```

**distinguishing_axis**

`mode` —— 本列之觸發為 PROXI Driver_Side 之配置，驗證對象為加熱方向盤圖示之左右位置；其餘九列皆非圖示位置。

**來源條文逐字**

- `4858299`：When $DriverSide$ = [Right Side], the HU shall mirror the location of the Heated Steering Wheel Icon, showing it in the right side of the Heated / Vented Seats screen. 1.3.2.1.3.1 Left Front Heated Seat {4858300}
- `4859494`：When $DriverSide$ = [Right Side], the HU shall mirror the location of the Heated Steering Wheel Icon, showing it in the right side of the Heated / Vented Seats screen.

---

## 4. `SWE1-VC-LeftFrontHeatedSeat-008`

| 欄 | 值 |
|---|---|
| batch | `batch03` |
| test_set | Common Features |
| design_method | Negative / Invalid |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Left front heated seat ignores an invalid status value

**test_item**

```text
The HU shall ignore invalid $HeatedSeatFL$ signals, if received.

(Two-state vehicle, medium is invalid)
```

**pre_conditions**

```text
1. The vehicle is configured for two heated seat states, Off and Low and High
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CSWM.FL_HS_STATSts$ = 1 (Heated_seat_low)
2. Read the displayed state of the left front heated seat and record it
3. Send the signal $STATUS_CSWM.FL_HS_STATSts$ = 2 (Heated_seat_medium) and check that the displayed state of the left front heated seat is unchanged from the state recorded in step 2
```

**expected_result**

```text
1. The signal $STATUS_CSWM.FL_HS_STATSts$ = 1 (Heated_seat_low) is registered without a bus error
2. The left front heated seat is displayed as low and the state is recorded
3. The left front heated seat is still displayed as low, unchanged from the state recorded in step 2
```

**specification_reference**

```text
CFTS044-4858310
```

**distinguishing_axis**

`input_data` —— 本列送無效值 2 (Heated_seat_medium) 且期望顯示不變；-007 送有效值 3 (Heated_seat_high) 且期望顯示變更。

**來源條文逐字**

- `4858310`：The HU shall ignore invalid $HeatedSeatFL$ signals, if received.

---

## 5. `SWE1-VC-LeftFrontHeatedSeat-003`

| 欄 | 值 |
|---|---|
| batch | `batch03` |
| test_set | Common Features |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Left front heated seat shows off after wake-up until status arrives

**test_item**

```text
When the HU wakes up on the BH-CAN bus, the HU shall show the Front Left Heated Seat as off until it receives a status update on CAN.

(Wake-up before first status)
```

**pre_conditions**

```text
1. The vehicle is equipped with heated front seats
2. The HU is in a sleep state on the BH-CAN bus
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Wake the HU on the BH-CAN bus without sending any $STATUS_CSWM.FL_HS_STATSts$ frame
2. Open the Heated / Vented Seats screen and check that the left front heated seat is shown as off
```

**expected_result**

```text
1. The HU completes wake-up on the BH-CAN bus
2. The left front heated seat is shown as off
```

**specification_reference**

```text
CFTS044-4858302
```

**distinguishing_axis**

`trigger_state` —— 本列驗左前座椅於喚醒後、首次狀態更新前顯示為 off；-022 驗右前座椅於喚醒時狀態被設為 OFF。

**來源條文逐字**

- `4858302`：When the HU wakes up on the BH-CAN bus, the HU shall show the Front Left Heated Seat as off until it receives a status update on CAN.

---

## 6. `SWE1-VC-TwoStagesHeatedSeat-057`

| 欄 | 值 |
|---|---|
| batch | `batch05` |
| test_set | Heated Seat |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **no**　驗證目標為畫面狀態循環，未斷言請求訊號之編碼（44 包 §3） |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Heated seat icon cycles off to high to low to off

**test_item**

```text
WHEN the user press the heated seats icons on TLM.Display.GUI, the relative icons status shall follow the logic descibed below (off -> high -> low -> off)

(Two-stage icon cycle on repeated press)
```

**pre_conditions**

```text
1. The vehicle is configured for two heated seat states
2. The heated seat icon status is off
3. The ignition is in the Ignition On condition
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Press the heated seat icon and check that its status changes to high
2. Press the heated seat icon and check that its status changes to low
3. Press the heated seat icon and check that its status changes to off
```

**expected_result**

```text
1. The heated seat icon status is high
2. The heated seat icon status is low
3. The heated seat icon status is off
```

**specification_reference**

```text
CFTS044-4859379
```

**distinguishing_axis**

`trigger_state` —— 本列驗連續按壓下圖示狀態之循環（off→high→low→off），驗證對象為畫面圖示狀態；其餘各列皆非循環行為。

**來源條文逐字**

- `4859379`：During the Ignition Working Condition- Ignition Off- Ignition On- Ignition On Engine On- Ignition Pre OffWHEN the user press the heated seats icons on TLM.Display.GUI, the relative icons status shall follow the logic descibed below (off -&gt; high -&gt; low -&gt; off):

---

## 7. `SWE1-VC-HeatedSteeringWheelManagement-025`

| 欄 | 值 |
|---|---|
| batch | `batch11` |
| test_set | Heated Steering Wheel |
| design_method | Equivalence Partitioning |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Heated steering wheel control shown only when configured present

**test_item**

```text
The HU shall Monitor $Heated_Steering_Wheel$ to determine if the vehicle is equipped with a heated steering wheel and update the HMI.

(Configuration present versus absent)
```

**pre_conditions**

```text
1. PROXI Heated_Steering_Wheel = 0 (Absent)
2. The Heated / Vented Seats screen is reachable from the Menu Bar
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Power cycle the HU and read whether the heated steering wheel control is present on the Heated / Vented Seats screen, and record it
2. Set PROXI Heated_Steering_Wheel = 1 (Present)
3. Power cycle the HU so that the configuration is applied
4. Open the Heated / Vented Seats screen and check that the heated steering wheel control is present, unlike the state recorded in step 1
```

**expected_result**

```text
1. The heated steering wheel control is not present and the state is recorded
2. PROXI Heated_Steering_Wheel = 1 (Present) is accepted
3. The HU completes start-up
4. The heated steering wheel control is present on the Heated / Vented Seats screen
```

**specification_reference**

```text
CFTS044-4858296
CFTS044-4859492
```

**distinguishing_axis**

`mode` —— 本列之觸發為 PROXI 配置參數之有無（Absent → Present），驗證對象為控制項之存在與否；batch05 之 HeatedSteeringWheel-003 之觸發為喚醒事件，驗證對象為狀態值。

**來源條文逐字**

- `4858296`：The HU shall Monitor $Heated_Steering_Wheel$ to determine if the vehicle is equipped with a heated steering wheel and update the HMI.
- `4859492`：Following requirements are valid only if PROXI parameter Heated_Steering_Wheel == "Present".

---

## 8. `SWE1-VC-HeatedSteeringWheel-006`

| 欄 | 值 |
|---|---|
| batch | `batch04_v2` |
| test_set | Heated Steering Wheel |
| design_method | Negative / Invalid |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Heated steering wheel ignores an undefined status encoding

**test_item**

```text
The HU shall ignore invalid $HSW_Stat_2$ signals, if received.

(Encoding 4 is not defined in the baseline DBC)
```

**pre_conditions**

```text
1. The vehicle is equipped with a heated steering wheel
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CLIMATE8.Tri_Level_HSW_StatSts$ = 1 (Heated_steering_wheel_low)
2. Read the displayed state of the heated steering wheel and record it
3. Send the signal $STATUS_CLIMATE8.Tri_Level_HSW_StatSts$ = 4 and check that the displayed state of the heated steering wheel is unchanged from the state recorded in step 2
```

**expected_result**

```text
1. The signal $STATUS_CLIMATE8.Tri_Level_HSW_StatSts$ = 1 (Heated_steering_wheel_low) is registered without a bus error
2. The heated steering wheel is displayed as low and the state is recorded
3. The heated steering wheel is still displayed as low, unchanged from the state recorded in step 2
```

**specification_reference**

```text
CFTS044-4858519
```

**distinguishing_axis**

`input_data` —— 本列送 4，其在基線 DBC 之 VAL_ 表中未定義；LeftFrontVentedSeat-006 送 2 (Vented_seat_medium)，其為已定義編碼而於二階配置下無效。

**來源條文逐字**

- `4858519`：The HU shall ignore invalid $HSW_Stat_2$ signals, if received.

---

## 9. `SWE1-VC-HeatedSteeringWheel-003`

| 欄 | 值 |
|---|---|
| batch | `batch04_v2` |
| test_set | Heated Steering Wheel |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Heated steering wheel state set to off at wake-up

**test_item**

```text
When the HU wakes up on the BH-CAN bus, the HU shall set the heated steering wheel state to OFF.

(Wake-up initial state)
```

**pre_conditions**

```text
1. The vehicle is equipped with a heated steering wheel
2. The HU is in a sleep state on the BH-CAN bus
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CLIMATE8.Tri_Level_HSW_StatSts$ = 3 (Heated_steering_wheel_high) and put the HU into a sleep state on the BH-CAN bus
2. Wake the HU on the BH-CAN bus, open the Heated / Vented Seats screen and check that the heated steering wheel state is OFF
```

**expected_result**

```text
1. The HU enters a sleep state on the BH-CAN bus
2. The heated steering wheel state is OFF
```

**specification_reference**

```text
CFTS044-4858513
```

**distinguishing_axis**

`trigger_state` —— 本列之驗證對象為加熱方向盤於喚醒時之狀態；LeftFrontVentedSeat-003 之驗證對象為左前通風座椅。

**來源條文逐字**

- `4858513`：When the HU wakes up on the BH-CAN bus, the HU shall set the heated steering wheel state to OFF.

---

## 10. `SWE1-VC-LeftFrontVentedSeat-004`

| 欄 | 值 |
|---|---|
| batch | `batch10` |
| test_set | Vented Seat |
| design_method | Equivalence Partitioning |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Two state left front vented seat accepts its three valid values

**test_item**

```text
For vehicles with two states (i.e. LO and HI), the HU shall implement the following requirements:Valid values for the $VentedSeatFL$ are shown below. All other states shall be considered invalid by the HU.

(Two-state valid value enumeration)
```

**pre_conditions**

```text
1. The vehicle is configured for two vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CSWM.FL_VS_STATSts$ = 0 (Vented_seat_off) and check that the left front vented seat is displayed as off
2. Send the signal $STATUS_CSWM.FL_VS_STATSts$ = 1 (Vented_seat_low) and check that the left front vented seat is displayed as low
3. Send the signal $STATUS_CSWM.FL_VS_STATSts$ = 3 (Vented_seat_high) and check that the left front vented seat is displayed as high
```

**expected_result**

```text
1. The left front vented seat is displayed as off
2. The left front vented seat is displayed as low
3. The left front vented seat is displayed as high
```

**specification_reference**

```text
CFTS044-4858367
```

**distinguishing_axis**

`input_data` —— 本列逐一驗三個有效值皆被接受；batch04 之 LeftFrontVentedSeat-006 驗無效值被忽略。

**來源條文逐字**

- `4858367`：For vehicles with two states (i.e. LO and HI), the HU shall implement the following requirements:Valid values for the $VentedSeatFL$ are shown below. All other states shall be considered invalid by the HU. $VentedSeatFL$ = [Vented Seat Off / VS_OFF] $VentedSeatFL$ = [Vented Seat Low / VS_LO] $VentedSeatFL$ = [Vented Seat High / VS_HI]

---

## 11. `SWE1-VC-LeftFrontVentedSeat-006`

| 欄 | 值 |
|---|---|
| batch | `batch04_v2` |
| test_set | Vented Seat |
| design_method | Negative / Invalid |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Left front vented seat ignores an invalid status value

**test_item**

```text
The HU shall ignore invalid $VentedSeatFL$ signals, if received.

(Two-state vehicle, medium is invalid)
```

**pre_conditions**

```text
1. The vehicle is configured for two vented seat states, Off and Low and High
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CSWM.FL_VS_STATSts$ = 1 (Vented_seat_low)
2. Read the displayed state of the left front vented seat and record it
3. Send the signal $STATUS_CSWM.FL_VS_STATSts$ = 2 (Vented_seat_medium) and check that the displayed state of the left front vented seat is unchanged from the state recorded in step 2
```

**expected_result**

```text
1. The signal $STATUS_CSWM.FL_VS_STATSts$ = 1 (Vented_seat_low) is registered without a bus error
2. The left front vented seat is displayed as low and the state is recorded
3. The left front vented seat is still displayed as low, unchanged from the state recorded in step 2
```

**specification_reference**

```text
CFTS044-4858369
```

**distinguishing_axis**

`input_data` —— 本列送無效值 2 (Vented_seat_medium) 且期望顯示不變；-007 送有效值 3 (Vented_seat_high) 且期望顯示變更。

**來源條文逐字**

- `4858369`：The HU shall ignore invalid $VentedSeatFL$ signals, if received.

---

## 12. `SWE1-VC-LeftFrontVentedSeat-003`

| 欄 | 值 |
|---|---|
| batch | `batch04_v2` |
| test_set | Vented Seat |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Left front vented seat state set to off at wake-up

**test_item**

```text
When the HU wakes up on the BH-CAN bus, the HU shall set the LF vented seat state to OFF.

(Wake-up initial state)
```

**pre_conditions**

```text
1. The vehicle is equipped with vented front seats
2. The HU is in a sleep state on the BH-CAN bus
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CSWM.FL_VS_STATSts$ = 3 (Vented_seat_high) and put the HU into a sleep state on the BH-CAN bus
2. Wake the HU on the BH-CAN bus, open the Heated / Vented Seats screen and check that the left front vented seat state is OFF
```

**expected_result**

```text
1. The HU enters a sleep state on the BH-CAN bus
2. The left front vented seat state is OFF
```

**specification_reference**

```text
CFTS044-4858362
```

**distinguishing_axis**

`trigger_state` —— 本列驗左前通風座椅於喚醒時狀態被設為 OFF；HeatedSteeringWheel-003 驗加熱方向盤之同一時機。

**來源條文逐字**

- `4858362`：When the HU wakes up on the BH-CAN bus, the HU shall set the LF vented seat state to OFF.

---

## 13. `SWE1-VC-LeftFrontHeatedSeat-014`

| 欄 | 值 |
|---|---|
| batch | `batch03` |
| test_set | Common Features |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **yes** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Left front heated seat request returns to not pressed

**test_item**

```text
The HU shall follow this signal with an on change $FL_HS_RQ$ = [Not Pressed / HS_NOT_PSD] within a time period of <Tsend>.

(Release after a press)
```

**pre_conditions**

```text
1. The vehicle is equipped with heated front seats
2. The Heated / Vented Seats screen is displayed
3. BH-CAN is connected to the bus simulator with signal tracing enabled
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Read the signal $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ and check that it is 0 (Not_Pressed)
2. Press the left front heated seat switch on the Heated / Vented Seats screen
3. Read the signal $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ and check that it returns to 0 (Not_Pressed) within <Tsend>
```

**expected_result**

```text
1. The signal $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ reads 0 (Not_Pressed)
2. The signal $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ = 1 (Pressed) is registered without a bus error
3. The signal $TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm$ = 0 (Not_Pressed) is registered within <Tsend>
```

**specification_reference**

```text
CFTS044-4858320
```

**distinguishing_axis**

`timing` —— 本列驗按下後請求訊號於 <Tsend> 內回到 0 (Not_Pressed)；其餘各列皆非請求訊號之時序。

**來源條文逐字**

- `4858320`：The HU shall follow this signal with an on change $FL_HS_RQ$ = [Not Pressed / HS_NOT_PSD] within a time period of &lt;Tsend&gt;.

---

## 14. `SWE1-VC-RightFrontHeatedSeat-031`

| 欄 | 值 |
|---|---|
| batch | `batch04_v2` |
| test_set | Common Features |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **yes** |
| dr_dependent | - |
| duplicate_of | - |
| split_flag / split_reason | False / - |

**tc_title**

> Right front heated seat request returns to not pressed

**test_item**

```text
The HU shall follow this signal with an on change $FR_HS_RQ$ = [Not Pressed / HS_NOT_PSD] within a time period of <Tsend>.

(Release after a press)
```

**pre_conditions**

```text
1. The vehicle is equipped with heated front seats
2. The Heated / Vented Seats screen is displayed
3. BH-CAN is connected to the bus simulator with signal tracing enabled
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Read the signal $TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm$ and check that it is 0 (Not_Pressed)
2. Press the right front heated seat switch on the Heated / Vented Seats screen
3. Read the signal $TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm$ and check that it has returned to 0 (Not_Pressed)
```

**expected_result**

```text
1. The signal $TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm$ reads 0 (Not_Pressed)
2. The signal $TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm$ = 1 (Pressed) is registered without a bus error
3. The signal $TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm$ reads 0 (Not_Pressed)
```

**specification_reference**

```text
CFTS044-4858350
```

**distinguishing_axis**

`trigger_state` —— 本列之驗證對象為右前座椅之 $TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm$；batch03 之 LeftFrontHeatedSeat-014 為左前之 FL_HS_Tlm。

**來源條文逐字**

- `4858350`：The HU shall follow this signal with an on change $FR_HS_RQ$ = [Not Pressed / HS_NOT_PSD] within a time period of &lt;Tsend&gt;.

---

## 15. `SWE1-VC-HeatedSteeringWheel-021`

| 欄 | 值 |
|---|---|
| batch | `batch07` |
| test_set | Heated Steering Wheel |
| design_method | State Transition |
| priority | P1 |
| dr15_exposed | **no** |
| dr_dependent | - |
| duplicate_of | 1 |
| split_flag / split_reason | False / - |

**tc_title**

> Heated steering wheel turns on when status reports on

**test_item**

```text
When the HU receives a $HSW_Stat$ = [1h: On] signal, the HU shall change the stored status of the heated steering wheel to ON and change the display as specified by the HMI within a time period of <Tdisplay>.

(Status reports on, raw code form)
```

**pre_conditions**

```text
1. The vehicle is equipped with a heated steering wheel
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**

`NA`

**test_procedure**

```text
1. Send the signal $STATUS_CSWM.HSW_StatSts$ = 0 (OFF)
2. Read the displayed state of the heated steering wheel and record it
3. Send the signal $STATUS_CSWM.HSW_StatSts$ = 1 (ON) and check that the heated steering wheel is displayed as on
```

**expected_result**

```text
1. The signal $STATUS_CSWM.HSW_StatSts$ = 0 (OFF) is registered without a bus error
2. The heated steering wheel is displayed as off and the state is recorded
3. The heated steering wheel is displayed as on
```

**specification_reference**

```text
CFTS044-4858544
```

**distinguishing_axis**

`none` —— 與 batch06 之 HeatedSteeringWheel-015（row #1）嚴格等價 —— 觸發、結果、輸入、驗證對象全同，差別僅在來源條文之記法（`[1h: On]` vs `[On]`）。

**來源條文逐字**

- `4858544`：When the HU receives a $HSW_Stat$ = [1h: On] signal, the HU shall change the stored status of the heated steering wheel to ON and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.

---

