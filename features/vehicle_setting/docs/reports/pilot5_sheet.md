# pilot #5 review sheet

執行層產出（W-148，51 輪）。依 78 包 §5 之抽樣。

## 1. 抽樣之交叉格矩陣

| 母體 | 條數 | 說明 |
|---|---:|---|
| 拆分產出（`split_flag = true`） | 7 | **必檢，不抽樣** —— 本 feature 首次出現之形態 |
| `batch20` | 12 | 分層母體 |

| `batch20` ＼ `impl_gap` | 有 | 無 |
|---|---:|---:|
| 條數 | 12 | 0 |

**必檢 7 ＋ 分層 8 ＝ 15 條。**

> `impl_gap` 之「無」格為 0 —— batch20 之 12 條全數帶 `impl_gap`
> （其命令訊號 `*_Cmd_Tlm` 皆不在基線 DBC）。
> **該維度於本母體為單值**，分層 8 條全自「有」格取（同 A-VS142 之形態）。

---

## 1. `SWE1-VC-Stop-StartSystem-002`

| 項 | 值 |
|---|---|
| 來源批次 | `batch01` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 heated seat（原條涵蓋 heated seat、vented seat、heated steering wheel） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4858549`：

> When the stop-start system is enabled the HU/CCDMR shall turn off the heated/vented seats and the heated steering wheel switch indicators based on the $EngRun_Stat$ signal and the $ESS_ENG_ST$ signal.

**十六欄全文**

**tc_title**：Stop mode turns the heated seat indicator off
**test_item**

```
If the stop-start system is enabled the HMI shall turn off the heated/vented seats and the heated steering wheel switch indicators based on the $EngRun_Stat$ signal and the $ESS_ENG_ST$ signal.

(Stop-start enabled, engine stopped)
```

**pre_conditions**

```
1. The vehicle is equipped with the Stop-Start system
2. The heated seat, vented seat and heated steering wheel switches are shown on the Climate screen
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 3 (ENS Running)
2. Send CAN: STATUS_CCAN3.EngineSts = 2 (Engine_On)
3. Activate the heated seat switches on the Climate screen
4. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 1 (ENS Stopped)
5. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off) and check that the heated seat switch indicators are turned off
```

**expected_result**

```
1. STATUS_CCAN3.ESS_ENG_ST = 3 (ENS Running) is sent
2. STATUS_CCAN3.EngineSts = 2 (Engine_On) is sent
3. the heated seat switch indicators are lit
4. STATUS_CCAN3.ESS_ENG_ST = 1 (ENS Stopped) is sent
5. the heated seat switch indicators are turned off
```

**specification_reference**：CFTS044-4858549
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 heated seat（原條涵蓋 heated seat、vented seat、heated steering wheel）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 2. `SWE1-VC-Stop-StartSystem-002`

| 項 | 值 |
|---|---|
| 來源批次 | `batch01` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 vented seat（原條涵蓋 heated seat、vented seat、heated steering wheel） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4858549`：

> When the stop-start system is enabled the HU/CCDMR shall turn off the heated/vented seats and the heated steering wheel switch indicators based on the $EngRun_Stat$ signal and the $ESS_ENG_ST$ signal.

**十六欄全文**

**tc_title**：Stop mode turns the vented seat indicator off
**test_item**

```
If the stop-start system is enabled the HMI shall turn off the heated/vented seats and the heated steering wheel switch indicators based on the $EngRun_Stat$ signal and the $ESS_ENG_ST$ signal.

(Stop-start enabled, engine stopped)
```

**pre_conditions**

```
1. The vehicle is equipped with the Stop-Start system
2. The heated seat, vented seat and heated steering wheel switches are shown on the Climate screen
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 3 (ENS Running)
2. Send CAN: STATUS_CCAN3.EngineSts = 2 (Engine_On)
3. Activate the vented seat switches on the Climate screen
4. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 1 (ENS Stopped)
5. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off) and check that the vented seat switch indicators are turned off
```

**expected_result**

```
1. STATUS_CCAN3.ESS_ENG_ST = 3 (ENS Running) is sent
2. STATUS_CCAN3.EngineSts = 2 (Engine_On) is sent
3. the vented seat switch indicators are lit
4. STATUS_CCAN3.ESS_ENG_ST = 1 (ENS Stopped) is sent
5. the vented seat switch indicators are turned off
```

**specification_reference**：CFTS044-4858549
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 vented seat（原條涵蓋 heated seat、vented seat、heated steering wheel）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 3. `SWE1-VC-Stop-StartSystem-002`

| 項 | 值 |
|---|---|
| 來源批次 | `batch01` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 heated steering wheel（原條涵蓋 heated seat、vented seat、heated steering wheel） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4858549`：

> When the stop-start system is enabled the HU/CCDMR shall turn off the heated/vented seats and the heated steering wheel switch indicators based on the $EngRun_Stat$ signal and the $ESS_ENG_ST$ signal.

**十六欄全文**

**tc_title**：Stop mode turns the heated steering wheel indicator off
**test_item**

```
If the stop-start system is enabled the HMI shall turn off the heated/vented seats and the heated steering wheel switch indicators based on the $EngRun_Stat$ signal and the $ESS_ENG_ST$ signal.

(Stop-start enabled, engine stopped)
```

**pre_conditions**

```
1. The vehicle is equipped with the Stop-Start system
2. The heated seat, vented seat and heated steering wheel switches are shown on the Climate screen
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 3 (ENS Running)
2. Send CAN: STATUS_CCAN3.EngineSts = 2 (Engine_On)
3. Activate the heated steering wheel switches on the Climate screen
4. Send CAN: STATUS_CCAN3.ESS_ENG_ST = 1 (ENS Stopped)
5. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off) and check that the heated steering wheel switch indicators are turned off
```

**expected_result**

```
1. STATUS_CCAN3.ESS_ENG_ST = 3 (ENS Running) is sent
2. STATUS_CCAN3.EngineSts = 2 (Engine_On) is sent
3. the heated steering wheel switch indicators are lit
4. STATUS_CCAN3.ESS_ENG_ST = 1 (ENS Stopped) is sent
5. the heated steering wheel switch indicators are turned off
```

**specification_reference**：CFTS044-4858549
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 heated steering wheel（原條涵蓋 heated seat、vented seat、heated steering wheel）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 4. `SWE1-VC-ThirdRowHeadrestDump-027`

| 項 | 值 |
|---|---|
| 來源批次 | `batch02` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 rear camera（原條涵蓋 rear camera、head restraint） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4858988`：

> The Third Row Headrest Dump Softkey button will also be accessible from the Rear View Camera screen, if applicable.

**十六欄全文**

**tc_title**：Headrest Dump softkey reachable from the Rear View Camera screen — rear camera
**test_item**

```
The Third Row Headrest Dump softkey shall also be accessible from the Rear View Camera screen, when supported.

(Entry path: Rear View Camera screen)
```

**pre_conditions**

```
1. The vehicle is equipped with the third row head restraint dump feature
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU is on the home screen
```

**input_test_data**：NA
**test_procedure**

```
1. Open the Rear View Camera screen from the Menu Bar
2. Check that the "" softkey button is displayed on the Rear View Camera screen
```

**expected_result**

```
1. The Rear View Camera screen is displayed
2. The "Headrest Dump" softkey button is displayed
```

**specification_reference**：CFTS044-4858988
**design_method**：功能測試 (Functional based ; no specific technique)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 rear camera（原條涵蓋 rear camera、head restraint）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 5. `SWE1-VC-ThirdRowHeadrestDump-027`

| 項 | 值 |
|---|---|
| 來源批次 | `batch02` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 head restraint（原條涵蓋 rear camera、head restraint） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4858988`：

> The Third Row Headrest Dump Softkey button will also be accessible from the Rear View Camera screen, if applicable.

**十六欄全文**

**tc_title**：Headrest Dump softkey reachable from the Rear View Camera screen — head restraint
**test_item**

```
The Third Row Headrest Dump softkey shall also be accessible from the Rear View Camera screen, when supported.

(Entry path: Rear View Camera screen)
```

**pre_conditions**

```
1. The vehicle is equipped with the third row head restraint dump feature
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU is on the home screen
```

**input_test_data**：NA
**test_procedure**

```
1. Open the Rear View Camera screen from the Menu Bar
2. Check that the "Headrest Dump" softkey button is displayed on the Rear View Camera screen
```

**expected_result**

```
1. The Rear View Camera screen is displayed
2. The "Headrest Dump" softkey button is displayed
```

**specification_reference**：CFTS044-4858988
**design_method**：功能測試 (Functional based ; no specific technique)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 head restraint（原條涵蓋 rear camera、head restraint）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 6. `SWE1-VC-ScreenOFF-052`

| 項 | 值 |
|---|---|
| 來源批次 | `batch06` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 touchscreen（原條涵蓋 touchscreen、audio） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4859110`：

> Display "on" or "off" status changes resulting from customer display button selections shall not alter any audio or video entertainment, information or signal warning/alert functions unless otherwise specified.
> 1.3.2.1.30 AQS (Air Quality Sensor) {4859111}

**十六欄全文**

**tc_title**：Display on off does not alter audio or video functions — touchscreen
**test_item**

```
Display "on" or "off" status changes resulting from customer display button selections shall not alter any audio or video entertainment, information or signal warning/alert functions unless otherwise specified.

(Audio continues across a display state change)
```

**pre_conditions**

```
1. Audio is playing from a media source
2. The touchscreen display is on
3. The Controls screen is displayed
```

**input_test_data**：NA
**test_procedure**

```
1. Read the audio playback state and the current track and record as Audio_track_initial
2. Press the "Screen Off" soft button and check that audio playback continues with Audio__initial
```

**expected_result**

```
1. Audio_track_initial is recorded as playing
2. The touchscreen display is off playback continues with Audio__initial
```

**specification_reference**：CFTS044-4859110
**design_method**：功能測試 (Functional based ; no specific technique)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 touchscreen（原條涵蓋 touchscreen、audio）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 7. `SWE1-VC-ScreenOFF-052`

| 項 | 值 |
|---|---|
| 來源批次 | `batch06` |
| 納入理由 | 必檢（拆分產出，首次出現之形態） |
| `split_flag` | True |
| `split_reason` | §8.2.2 不同控制實體 → 拆；本條之實體為 audio（原條涵蓋 touchscreen、audio） |
| `impl_gap` | （無） |
| `dr_dependent` | （無） |

**來源條文逐字**

`CFTS044-4859110`：

> Display "on" or "off" status changes resulting from customer display button selections shall not alter any audio or video entertainment, information or signal warning/alert functions unless otherwise specified.
> 1.3.2.1.30 AQS (Air Quality Sensor) {4859111}

**十六欄全文**

**tc_title**：Display on off does not alter audio or video functions — audio
**test_item**

```
Display "on" or "off" status changes resulting from customer display button selections shall not alter any audio or video entertainment, information or signal warning/alert functions unless otherwise specified.

(Audio continues across a display state change)
```

**pre_conditions**

```
1. Audio is playing from a media source
2. The touchscreen display is on
3. The Controls screen is displayed
```

**input_test_data**：NA
**test_procedure**

```
1. Read the audio playback state and the current track and record as Audio_track_initial
2. Press the "" soft button and check that audio playback continues with Audio_track_initial
```

**expected_result**

```
1. Audio_track_initial is recorded as playing
2. The touchscreen display is off and audio playback continues with Audio_track_initial
```

**specification_reference**：CFTS044-4859110
**design_method**：功能測試 (Functional based ; no specific technique)
**priority**：P1
**split_flag**：True
**split_reason**：§8.2.2 不同控制實體 → 拆；本條之實體為 audio（原條涵蓋 touchscreen、audio）
**dr_dependent**：
**impl_gap**：
**screen_pending**：no
**dr15_exposed**：no
**remarks**：

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 8. `SWE1-VC-ThreeStagesHeatedSeat-082`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859404`：

> IF ($HeatedSeatFL$ == "Heated_seat_high" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_mid".

**十六欄全文**

**tc_title**：Left front heated seat at high commands mid
**test_item**

```
IF ($HeatedSeatFL$ == "Heated_seat_high" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_mid".

(Three stage configuration, press request)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 3 (Heated_seat_high)
3. Press the left front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = Heated_seat_mid is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 3 (Heated_seat_high) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = Heated_seat_mid is sent
```

**specification_reference**：CFTS044-4859404
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 9. `SWE1-VC-ThreeStagesHeatedSeat-083`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859405`：

> IF ($HeatedSeatFL$ == "Heated_seat_mid" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_low".

**十六欄全文**

**tc_title**：Left front heated seat at mid commands low
**test_item**

```
IF ($HeatedSeatFL$ == "Heated_seat_mid" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_low".

(Three stage configuration, press request)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = Heated_seat_mid
3. Press the left front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 1 (Heated_seat_low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = Heated_seat_mid is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = 1 (Heated_seat_low) is sent
```

**specification_reference**：CFTS044-4859405
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 10. `SWE1-VC-ThreeStagesHeatedSeat-086`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859408`：

> IF ($HeatedSeatFR$ == "Heated_seat_high" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present" AND PsngrSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_mid".

**十六欄全文**

**tc_title**：Right front heated seat at high commands mid
**test_item**

```
IF ($HeatedSeatFR$ == "Heated_seat_high" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present" AND PsngrSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_mid".

(Three stage configuration, press request)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 3 (Heated_seat_high)
3. Press the right front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = Heated_seat_mid is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = 3 (Heated_seat_high) is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = Heated_seat_mid is sent
```

**specification_reference**：CFTS044-4859408
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 11. `SWE1-VC-ThreeStagesHeatedSeat-087`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859409`：

> IF ($HeatedSeatFR$ == "Heated_seat_mid" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present" AND PsngrSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_low".

**十六欄全文**

**tc_title**：Right front heated seat at mid commands low
**test_item**

```
IF ($HeatedSeatFR$ == "Heated_seat_mid" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present" AND PsngrSeatHeating.Req passes to "Requested" )THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_low".

(Three stage configuration, press request)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = Heated_seat_mid
3. Press the right front heated seat icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 1 (Heated_seat_low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = Heated_seat_mid is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = 1 (Heated_seat_low) is sent
```

**specification_reference**：CFTS044-4859409
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 12. `SWE1-VC-ThreeStagesHeatedSeat-092`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859416`：

> IF ($HeatedSeatFL$ passes to "Heated_seat_mid" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_mid"

**十六欄全文**

**tc_title**：Left front heated seat at mid commands mid
**test_item**

```
IF ($HeatedSeatFL$ passes to "Heated_seat_mid" AND STATUS_CSWM.FL_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = "Heated_seat_mid"

(Three stage configuration, status transition)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off)
3. Send CAN: STATUS_CSWM.FL_HS_STATSts = Heated_seat_mid without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = Heated_seat_mid is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_HS_STATSts = 0 (Heated_seat_off) is sent
3. TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm = Heated_seat_mid is sent
```

**specification_reference**：CFTS044-4859416
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 13. `SWE1-VC-ThreeStagesHeatedSeat-096`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859420`：

> IF ($HeatedSeatFR$ passes to "Heated_seat_mid" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_mid"

**十六欄全文**

**tc_title**：Right front heated seat at mid commands mid
**test_item**

```
IF ($HeatedSeatFR$ passes to "Heated_seat_mid" AND STATUS_CSWM.FR_HS_STATFailSts == "Fail_Not_Present")THENTLM shall set TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = "Heated_seat_mid"

(Three stage configuration, status transition)
```

**pre_conditions**

```
1. The vehicle is configured for three heated seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off)
3. Send CAN: STATUS_CSWM.FR_HS_STATSts = Heated_seat_mid without pressing any icon and check that TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = Heated_seat_mid is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FR_HS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off) is sent
3. TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm = Heated_seat_mid is sent
```

**specification_reference**：CFTS044-4859420
**design_method**：狀態轉換 (State Transition Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 14. `SWE1-VC-ThreeStagesVentedSeatsManagement-064`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859468`：

> IF ($VentedSeatFL$ == "Vented_seat_high" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_mid".

**十六欄全文**

**tc_title**：Left front vented seat at high commands mid
**test_item**

```
IF ($VentedSeatFL$ == "Vented_seat_high" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_mid".

(Three stage configuration, press request)
```

**pre_conditions**

```
1. The vehicle is configured for three vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = 3 (Vented_seat_high)
3. Press the left front vented seat icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = Vented_seat_mid is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = 3 (Vented_seat_high) is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = Vented_seat_mid is sent
```

**specification_reference**：CFTS044-4859468
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---

## 15. `SWE1-VC-ThreeStagesVentedSeatsManagement-065`

| 項 | 值 |
|---|---|
| 來源批次 | `batch20` |
| 納入理由 | 分層（batch20 × `impl_gap` 有） |
| `split_flag` | False |
| `split_reason` | （無） |
| `impl_gap` | TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm |
| `dr_dependent` | DR-18 |

**來源條文逐字**

`CFTS044-4859469`：

> IF ($VentedSeatFL$ == "Vented_seat_mid" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_low".

**十六欄全文**

**tc_title**：Left front vented seat at mid commands low
**test_item**

```
IF ($VentedSeatFL$ == "Vented_seat_mid" AND STATUS_CSWM.FL_VS_STATFailSts == "Fail_Not_Present" AND DrvSeatHeating.Req passes to "Requested")THENTLM shall set TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = "Vented_seat_low".

(Three stage configuration, press request)
```

**pre_conditions**

```
1. The vehicle is configured for three vented seat states
2. The Heated / Vented Seats screen is displayed
3. CAN-B is connected to the bus simulator
```

**input_test_data**：NA
**test_procedure**

```
1. Send CAN: STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present)
2. Send CAN: STATUS_CSWM.FL_VS_STATSts = Vented_seat_mid
3. Press the left front vented seat icon and check that TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 1 (Vented_Seat_Low) is transmitted
```

**expected_result**

```
1. STATUS_CSWM.FL_VS_STATFailSts = 0 (Fail_Not_Present) is sent
2. STATUS_CSWM.FL_VS_STATSts = Vented_seat_mid is sent
3. TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm = 1 (Vented_Seat_Low) is sent
```

**specification_reference**：CFTS044-4859469
**design_method**：決策表 (Decision Table Testing)
**priority**：P1
**split_flag**：False
**split_reason**：
**dr_dependent**：DR-18
**impl_gap**：TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm
**screen_pending**：no
**dr15_exposed**：no
**remarks**：BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；IMPL_GAP: TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm —— 依 R-VS66(a) 開 issue 予 RD

### 覆核欄（分析層填）

| 項 | 建議分類 | 理由 |
|---|---|---|
| 內容正確性 | | |
| 拆分之軸是否成立 | | |
| `impl_gap` 之標記 | | |

---
