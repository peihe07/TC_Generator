# pilot #5＋#6 合併 sheet（W-156，54 輪）

依 `docs/handoff/82_generation_done.md` §4。**母體：本輪起未經任何人工關卡者。**

## 1. 母體之構成

| 批 | 條 | 說明 |
|---|---|---|
| `batch01_v7.json` | 3 | 50 輪 W-143 之拆分產出 |
| `batch02_v5.json` | 2 | 50 輪 W-143 之拆分產出 |
| `batch06_v6.json` | 2 | 50 輪 W-143 之拆分產出 |
| `batch20.json` | 12 | 50 輪 A 型補寫 |
| `batch21_probe.json` | 7 | 52 輪 probe 修正 |
| `batch22.json` | 12 | 52 輪 E 型放量 |
| `batch23.json` | 47 | 53 輪生成收尾 |
| **合計** | **85** | 與 82 包 §4 所載之 85 相符 |

## 2. 分層維度之非單值驗證（先驗，A-VS142 之教訓）

| 維度 | 相異值 | 判 |
|---|---|---|
| `test_set` | 4 —— `Common Features`、`Heated Seat`、`Heated Steering Wheel`、`Vented Seat` | **非單值**，可分層 |
| `screen_pending` | 2 —— `no`、`yes` | **非單值**，可分層 |

**升級條件「分層維度於本母體為單值」未命中。**

## 3. 交叉格矩陣

| `test_set` \ `screen_pending` | `no` | `yes` | 小計 |
|---|---|---|---|
| `Common Features` | 21 | 2 | **23** |
| `Heated Seat` | 23 | 8 | **31** |
| `Heated Steering Wheel` | 7 | 4 | **11** |
| `Vented Seat` | 18 | 2 | **20** |
| **小計** | **69** | **16** | **85** |

**八格中非空者即分層抽樣之取樣格**；空格不取（其非抽樣之遺漏，而是該組合於母體不存在）。

## 4. 形態分布（必檢之涵蓋依據）

| 形態 | 條 | 必檢涵蓋 |
|---|---|---|
| `A 型（命令）` | 2 | — |
| `A 型（早批）` | 3 | — |
| `D 型（送出）` | 11 | ✅ |
| `E 型（早批）` | 12 | — |
| `F 型（啟用／停用）` | 1 | — |
| `F 型（早批）` | 3 | — |
| `G2 值域宣告 ＋ 其餘為無效` | 9 | ✅ |
| `G3 推進系統未啟動 → 灰階` | 5 | ✅ |
| `G4 Stop-Start 未配備 → 灰階` | 4 | ✅ |
| `G5 follow-up 訊號` | 7 | ✅ |
| `G6 DriverSide 之條件` | 2 | ✅ |
| `G6 PowerMode 之條件` | 3 | ✅ |
| `G7 配置訊號 → 按鍵` | 2 | ✅ |
| `G8 引擎運轉 → 允許啟用` | 1 | ✅ |
| `未標形態（早批）` | 20 | ✅ |

## 5. 抽樣 18 條（必檢 10 ＋ 分層 8）

### 1. [必檢] `SWE1-VC-HeatedSteeringWheel-004` — Invalid heated steering wheel status value is ignored

**抽樣理由**：必檢：G 型子形態 `G2 值域宣告 ＋ 其餘為無效` 之代表（該形態共 9 條）
**形態**：`G2 值域宣告 ＋ 其餘為無效`　**批**：`batch23.json`

**來源條文（逐字）**

```
For vehicles with dual states (i.e. OFF and HI) when $Heated_Steering_Levels$ = [1_Level], the HU shall implement the following requirements:Valid values for the $HSW_Stat$ are shown below. All other states shall be considered invalid by the HU. $HSW_StatS = [Heated steering wheel off / OFF] $HSW_StatS = [Heated steering wheel on / ON]
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-004` |
| Test Set | Heated Steering Wheel |
| TC Title | Invalid heated steering wheel status value is ignored |
| Test Item | For vehicles with dual states (i.e. OFF and HI) when $Heated_Steering_Levels$ = [1_Level], the HU shall implement the following requirements:Valid values for the $HSW_Stat$ are shown below. All other states shall be considered invalid by the HU. $HSW_StatS = [Heated steering wheel off / OFF] $HSW_StatS = [Heated steering wheel on / ON]<br><br>(Value outside the declared valid set) |
| Pre-Conditions | 1. The vehicle is equipped with the heated steering wheel<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CSWM.HSW_STATSts = 0 (OFF) and record the displayed state as Display_valid<br>2. Send CAN: STATUS_CSWM.HSW_STATSts = a value outside the declared valid set<br>3. Read the displayed state of the heated steering wheel and check that it is unchanged from Display_valid |
| Expected Result | 1. STATUS_CSWM.HSW_STATSts = 0 (OFF) is sent；Display_valid is recorded<br>2. PENDING: DR-18<br>3. The heated steering wheel display is unchanged from Display_valid |
| Specification Reference | CFTS044-4858516 |
| Design Method | 負向測試 (Negative / Invalid) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent | DR-18 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-18 —— 該訊號 0–3 皆已定義，無效碼之定義待覆 |
| Reasoning | P1：主要功能邏輯；**G2 值域宣告 ＋ 其餘為無效** —— 條文列 `HSW_Stat` 之合法值集並逐字宣告「All other states shall be considered invalid by the HU」——**其可測內容即「非合法值不改變顯示」**，而該訊號為 2 bit、其 0–3 四碼**皆已定義** —— **無未用碼可注入**；依 §8.4.1 不得造值，故該步驟之 ER 依 R-VS71 寫 `PENDING: DR-18`（無效碼之定義待覆） |

### 2. [必檢] `SWE1-VC-HeatedSteeringWheel-008` — Heated steering wheel greyed out when propulsion is not active

**抽樣理由**：必檢：G 型子形態 `G3 推進系統未啟動 → 灰階` 之代表（該形態共 5 條）
**形態**：`G3 推進系統未啟動 → 灰階`　**批**：`batch23.json`

**來源條文（逐字）**

```
If $Hybrid_Type$ = [[PHEV] OR [BEV] OR [HEV] OR [REPB] OR [FCEV]] &amp;&amp; $PrplsnSysAtv$ = [Not Active], the heated steering wheel switch, shall be shown as greyed-out, per the HMI.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-008` |
| Test Set | Heated Steering Wheel |
| TC Title | Heated steering wheel greyed out when propulsion is not active |
| Test Item | If $Hybrid_Type$ = [[PHEV] OR [BEV] OR [HEV] OR [REPB] OR [FCEV]] &amp;&amp; $PrplsnSysAtv$ = [Not Active], the heated steering wheel switch, shall be shown as greyed-out, per the HMI.<br><br>(Propulsion inactive on an electrified vehicle) |
| Pre-Conditions | 1. The vehicle is an electrified vehicle<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Set PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle)<br>2. Send CAN: HYBRID_POWERTRAIN1.PropulsionSystemActive = 1 (Active)<br>3. Send CAN: HYBRID_POWERTRAIN1.PropulsionSystemActive = 0 (Not_Active) and check that the heated steering wheel switch is greyed out |
| Expected Result | 1. PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle) is accepted<br>2. HYBRID_POWERTRAIN1.PropulsionSystemActive = 1 (Active) is sent<br>3. The heated steering wheel switch is greyed out |
| Specification Reference | CFTS044-4858522 |
| Design Method | 決策表 (Decision Table Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | no |
| Remarks |  |
| Reasoning | P1：主要功能邏輯；**G3 推進系統未啟動 → 灰階** —— 條文之條件為 `$PrplsnSysAtv$ = [Not Active] && $Hybrid_Type$ = [[PHEV] OR [BEV] …]` 之**合取** —— 二者皆須成立，故 procedure 先設 Hybrid_Type 再切 PrplsnSysAtv。`$PrplsnSysAtv$` 取 LID 之 `HYBRID_POWERTRAIN1.PropulsionSystemActive` |

### 3. [必檢] `SWE1-VC-LeftFrontHeatedSeat-010` — Left front heated seat greyed out when the engine is not running

**抽樣理由**：必檢：G 型子形態 `G4 Stop-Start 未配備 → 灰階` 之代表（該形態共 4 條）
**形態**：`G4 Stop-Start 未配備 → 灰階`　**批**：`batch23.json`

**來源條文（逐字）**

```
For vehicles not equipped with the Stop-Start feature, when the vehicle engine is not running ($EngRun_Stat$ &lt;&gt; [IDLE_STBL//UNLIMITED//LIMITED//RUN]  &amp;&amp; $Hybrid_Type$ &lt;&gt; [[PHEV] OR [BEV] OR [HEV] OR [REPB] OR [FCEV]]), the left front heated seat switch, shall be shown as greyed-out, per the HMI.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-LeftFrontHeatedSeat-010` |
| Test Set | Heated Seat |
| TC Title | Left front heated seat greyed out when the engine is not running |
| Test Item | For vehicles not equipped with the Stop-Start feature, when the vehicle engine is not running ($EngRun_Stat$ &lt;&gt; [IDLE_STBL//UNLIMITED//LIMITED//RUN]  &amp;&amp; $Hybrid_Type$ &lt;&gt; [[PHEV] OR [BEV] OR [HEV] OR [REPB] OR [FCEV]]), the left front heated seat switch, shall be shown as greyed-out, per the HMI.<br><br>(Engine not running on a vehicle without stop-start) |
| Pre-Conditions | 1. The vehicle is not equipped with the Stop-Start feature<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Set PROXI Stop_And_Start_cfg = 0 (Absent)<br>2. Send CAN: STATUS_CCAN3.EngineSts = 2 (Engine_On)<br>3. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off) and check that the left front heated seat switch is greyed out |
| Expected Result | 1. PROXI Stop_And_Start_cfg = 0 (Absent) is accepted<br>2. STATUS_CCAN3.EngineSts = 2 (Engine_On) is sent<br>3. PENDING: DR-19 |
| Specification Reference | CFTS044-4858316 |
| Design Method | 決策表 (Decision Table Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent | DR-19 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-19 —— `$EngRun_Stat$` 之四值待覆 |
| Reasoning | P1：主要功能邏輯；**G4 Stop-Start 未配備 → 灰階** —— 條文之條件為 `$EngRun_Stat$ <> [IDLE_STBL//UNLIMITED//LIMITED//RUN]`；該四值於 LID 與 DBC 皆無對應（**DR-19 之標的**），依 R-VS71 該步驟之 ER 寫 `PENDING: DR-19`、前置步驟照寫 |

### 4. [必檢] `SWE1-VC-HeatedSteeringWheel-013` — Request returns to not pressed after the press

**抽樣理由**：必檢：G 型子形態 `G5 follow-up 訊號` 之代表（該形態共 7 條）
**形態**：`G5 follow-up 訊號`　**批**：`batch23.json`

**來源條文（逐字）**

```
The HU shall follow this signal with an on change $HSW_RQ_TGW$ = [NOT Pressed / NOT_PSD] within a time period of &lt;Tsend&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-013` |
| Test Set | Heated Steering Wheel |
| TC Title | Request returns to not pressed after the press |
| Test Item | The HU shall follow this signal with an on change $HSW_RQ_TGW$ = [NOT Pressed / NOT_PSD] within a time period of &lt;Tsend&gt;.<br><br>(On-change follow-up after release) |
| Pre-Conditions | 1. The vehicle is equipped with the heated steering wheel<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator with signal tracing enabled |
| Input Test Data | NA |
| Test Procedure | 1. Start a bus trace on CAN-B that captures the frames carrying TELEMATIC_VEHICLE_SETUP3.HSW_Tlm<br>2. Press and release the heated steering wheel control<br>3. Read the CAN-B trace and check that TELEMATIC_VEHICLE_SETUP3.HSW_Tlm = 0 (Not_Pressed) is transmitted after the release |
| Expected Result | 1. The bus trace is running and is capturing the frames carrying TELEMATIC_VEHICLE_SETUP3.HSW_Tlm<br>2. The heated steering wheel control registers the press and the release<br>3. TELEMATIC_VEHICLE_SETUP3.HSW_Tlm = 0 (Not_Pressed) is sent |
| Specification Reference | CFTS044-4858532 |
| Design Method | 狀態轉換 (State Transition Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | no |
| Remarks | BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆，ER 只寫可觀察終態 |
| Reasoning | P1：主要功能邏輯；**G5 follow-up 訊號** —— 條文逐字「shall follow this signal with an on change … = [Not Pressed …] within <Tsend>」——**其驗證目標為釋放後之回歸值**，非按壓本身。`HSW_RQ_TGW` 依 R-VS67′ 取 `Atlantis High` 之 `TELEMATIC_VEHICLE_SETUP3.HSW_Tlm` |

### 5. [必檢] `SWE1-VC-SwitchLHD/RHDConfiguration-010` — Right hand drive modifies the seat control layout

**抽樣理由**：必檢：G 型子形態 `G6 DriverSide 之條件` 之代表（該形態共 2 條）
**形態**：`G6 DriverSide 之條件`　**批**：`batch23.json`

**來源條文（逐字）**

```
When $DriverSide$ = [Right hand drive] the HMI shall be modified as defined by HMI requirements.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-SwitchLHD/RHDConfiguration-010` |
| Test Set | Common Features |
| TC Title | Right hand drive modifies the seat control layout |
| Test Item | When $DriverSide$ = [Right hand drive] the HMI shall be modified as defined by HMI requirements.<br><br>(Right hand drive configuration) |
| Pre-Conditions | 1. The HU is in the Full-Operation state<br>2. The Heated / Vented Seats screen is displayed |
| Input Test Data | NA |
| Test Procedure | 1. Set PROXI Driver_Side = 0 (Left Side) and record the seat control layout as Layout_LHD<br>2. Set PROXI Driver_Side = 1 (Right Side)<br>3. Power cycle the HU and check that the seat control layout differs from Layout_LHD |
| Expected Result | 1. PROXI Driver_Side = 0 (Left Side) is accepted；Layout_LHD is recorded<br>2. PROXI Driver_Side = 1 (Right Side) is accepted<br>3. PENDING: DR-5-B |
| Specification Reference | CFTS044-4858560 |
| Design Method | 等價劃分 (Equivalence Partitioning, EP) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | yes |
| Remarks | BLOCKED: DR-5-B —— 右駕版面之具體定義待 HMI requirements |
| Reasoning | P1：主要功能邏輯；**G6 DriverSide 之條件** —— 條文逐字「the HMI shall be modified as defined by HMI requirements」——**其所指之 HMI requirements 不在本 feature 之範圍**（§8.4.2），故只驗「有無變更」，其具體版面依 R-VS59(4) 標 PENDING |

### 6. [必檢] `SWE1-VC-ThirdRowHeadrestDump-029` — Headrest dump softkey greyed out at the stated power mode

**抽樣理由**：必檢：G 型子形態 `G6 PowerMode 之條件` 之代表（該形態共 3 條）
**形態**：`G6 PowerMode 之條件`　**批**：`batch23.json`

**來源條文（逐字）**

```
The HU shall grey-out the Third Row Headrest Dump Softkey button when the $PowerMode$ = [Ignition start / IGN_START].
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-ThirdRowHeadrestDump-029` |
| Test Set | Common Features |
| TC Title | Headrest dump softkey greyed out at the stated power mode |
| Test Item | The HU shall grey-out the Third Row Headrest Dump Softkey button when the $PowerMode$ = [Ignition start / IGN_START].<br><br>(Power mode condition) |
| Pre-Conditions | 1. The vehicle is equipped with third row head restraints<br>2. The Controls screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)<br>2. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 5 (START)<br>3. Read the "Headrest Dump" softkey button and check that it is greyed out |
| Expected Result | 1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent<br>2. PENDING: DR-21<br>3. The "Headrest Dump" softkey button is greyed out |
| Specification Reference | CFTS044-4858991 |
| Design Method | 狀態轉換 (State Transition Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent | DR-21 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-21 —— `$PowerMode$` 之 `IGN_START`／`IGN_OFF_ACC` 待覆 |
| Reasoning | P1：主要功能邏輯；**G6 PowerMode 之條件** —— 條文之 `$PowerMode$` 值為 `IGN_START` —— 其於 LID 之 `STATUS_BH_BCM2.CmdIgnSts` 值域中**無逐字對應**（**DR-21 之標的**），依 R-VS71 該步驟之 ER 寫 `PENDING: DR-21`、其餘照寫 |

### 7. [必檢] `SWE1-VC-ScreenOFF-048` — Screen Off button activated when configured present

**抽樣理由**：必檢：G 型子形態 `G7 配置訊號 → 按鍵` 之代表（該形態共 2 條）
**形態**：`G7 配置訊號 → 按鍵`　**批**：`batch23.json`

**來源條文（逐字）**

```
When the HU receives $DSP_SK_PRSNT$ = [Present], the HU shall activate the virtual Screen Off button for user select-ability.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-ScreenOFF-048` |
| Test Set | Common Features |
| TC Title | Screen Off button activated when configured present |
| Test Item | When the HU receives $DSP_SK_PRSNT$ = [Present], the HU shall activate the virtual Screen Off button for user select-ability.<br><br>(Configuration present versus absent) |
| Pre-Conditions | 1. The HU is in the Full-Operation state<br>2. The Controls screen is displayed |
| Input Test Data | NA |
| Test Procedure | 1. Set PROXI DSP_SK_PRSNT = 0 (Absent) and record whether the "Screen Off" button is present as Button_absent<br>2. Set PROXI DSP_SK_PRSNT = 1 (Present)<br>3. Power cycle the HU and check that the "Screen Off" button is activated for user selection |
| Expected Result | 1. PROXI DSP_SK_PRSNT = 0 (Absent) is accepted；Button_absent is recorded<br>2. PENDING: DR-22<br>3. The "Screen Off" button is activated for user selection |
| Specification Reference | CFTS044-4859105 |
| Design Method | 等價劃分 (Equivalence Partitioning, EP) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent | DR-22 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-22 —— `DSP_SK_PRSNT` 之值域待覆 |
| Reasoning | P1：主要功能邏輯；**G7 配置訊號 → 按鍵** —— 條文之觸發為**配置訊號**（`DSP_SK_PRSNT = [Present]`），非狀態訊號 —— 其於 LID **無列**（`VC_HdRstPrsnt` 為 **DR-22 之 token 級標的**），依 R-VS71 該步驟之 ER 寫 `PENDING: DR-22`、其餘照寫 |

### 8. [必檢] `SWE1-VC-Stop-StartSystem-006` — Engine running allows the seat and wheel switches

**抽樣理由**：必檢：G 型子形態 `G8 引擎運轉 → 允許啟用` 之代表（該形態共 1 條）
**形態**：`G8 引擎運轉 → 允許啟用`　**批**：`batch23.json`

**來源條文（逐字）**

```
IF ($EngRun_Stat$ = [IDLE_STBL//UNLIMITED//LIMITED//RUN])THEN- The HU shall allow activation of the heated and vented seats and the heated steering wheel switches.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-Stop-StartSystem-006` |
| Test Set | Common Features |
| TC Title | Engine running allows the seat and wheel switches |
| Test Item | IF ($EngRun_Stat$ = [IDLE_STBL//UNLIMITED//LIMITED//RUN])THEN- The HU shall allow activation of the heated and vented seats and the heated steering wheel switches.<br><br>(Engine running condition) |
| Pre-Conditions | 1. The vehicle is equipped with the Stop-Start feature<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off)<br>2. Send CAN: STATUS_CCAN3.EngineSts = 2 (Engine_On)<br>3. Read the heated seat switch and check that it can be activated |
| Expected Result | 1. STATUS_CCAN3.EngineSts = 0 (Engine_Off) is sent<br>2. PENDING: DR-19<br>3. The heated seat switch can be activated |
| Specification Reference | CFTS044-4858555 |
| Design Method | 決策表 (Decision Table Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent | DR-19 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-19 —— `$EngRun_Stat$` 之四值待覆 |
| Reasoning | P1：主要功能邏輯；**G8 引擎運轉 → 允許啟用** —— 條文之條件 `$EngRun_Stat$ = [IDLE_STBL//UNLIMITED//LIMITED//RUN]` 之四值於 LID 與 DBC 皆無對應（**DR-19 之標的**），依 R-VS71 該步驟寫 `PENDING: DR-19` |

### 9. [必檢] `SWE1-VC-HeatedSteeringWheel-013` — Heated steering wheel press sends the request signal

**抽樣理由**：必檢：D 型 `PENDING: DR-15` 之形態（80 包 §1 之改寫，共 10 條）
**形態**：`D 型（送出）`　**批**：`batch23.json`

**來源條文（逐字）**

```
The HU shall follow this signal with an on change $HSW_RQ_TGW$ = [NOT Pressed / NOT_PSD] within a time period of &lt;Tsend&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-013` |
| Test Set | Heated Steering Wheel |
| TC Title | Heated steering wheel press sends the request signal |
| Test Item | The HU shall follow this signal with an on change $HSW_RQ_TGW$ = [NOT Pressed / NOT_PSD] within a time period of &lt;Tsend&gt;.<br><br>(Press sends the on-change request) |
| Pre-Conditions | 1. The vehicle is equipped with the heated steering wheel<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator with signal tracing enabled |
| Input Test Data | NA |
| Test Procedure | 1. Start a bus trace on CAN-B that captures the frames carrying TELEMATIC_VEHICLE_SETUP3.HSW_Tlm<br>2. Press the heated steering wheel icon<br>3. Read the CAN-B trace and check that the value sent on TELEMATIC_VEHICLE_SETUP3.HSW_Tlm is the one specified for the current state |
| Expected Result | 1. The bus trace is running and is capturing the frames carrying TELEMATIC_VEHICLE_SETUP3.HSW_Tlm<br>2. The heated steering wheel icon registers the press<br>3. PENDING: DR-15 |
| Specification Reference | CFTS044-4858532 |
| Design Method | 功能測試 (Functional based ; no specific technique) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | yes |
| DR Dependent | DR-15 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-15 —— 請求訊號之編碼待覆；BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆 |
| Reasoning | P1：主要功能邏輯；**D 型（送出）** —— 觸發為使用者按壓、標的為匯流排上之送出值。**其送出值為 DR-15 之 token 級標的**，於來源無逐字對應 —— 依 R-VS71 該步驟之 ER 寫 `PENDING: DR-15`、前置步驟照寫。**不以「有送出」代替「送出正確之值」**（80 包 §1，A-VS157） |

### 10. [必檢] `SWE1-VC-HeatedSteeringWheel-014` — Heated steering wheel request depends on current status

**抽樣理由**：必檢：D 型 `PENDING: DR-15` 之形態（80 包 §1 之改寫，共 10 條）
**形態**：`未標形態（早批）`　**批**：`batch21_probe.json`

**來源條文（逐字）**

```
When the HU determines that the Customer has selected to change the status of the Heated Steering Wheel, the HU shall send an on change $HSW_RQ_TGW$ depending on the current status of $HSW_Stat_2$. The signal value to be sent is detailed belowCurrent status of $HSW_Stat_2$ Signal to be sentHigh $HSW_RQ_TGW$ = [Medium]Medium $HSW_RQ_TGW$ = [Low]Low $HSW_RQ_TGW$ = [Off]Off $HSW_RQ_TGW$ = [High]
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-014` |
| Test Set | Heated Steering Wheel |
| TC Title | Heated steering wheel request depends on current status |
| Test Item | When the HU determines that the Customer has selected to change the status of the Heated Steering Wheel, the HU shall send an on change $HSW_RQ_TGW$ depending on the current status of $HSW_Stat_2$. The signal value to be sent is detailed belowCurrent status of $HSW_Stat_2$ Signal to be sentHigh $HSW_RQ_TGW$ = [Medium]Medium $HSW_RQ_TGW$ = [Low]Low $HSW_RQ_TGW$ = [Off]Off $HSW_RQ_TGW$ = [High]<br><br>(Request value follows the current status) |
| Pre-Conditions | 1. The vehicle is equipped with a heated steering wheel<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator with signal tracing enabled |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 3 (Heated_steering_wheel_high)<br>2. Press the heated steering wheel icon on the Heated / Vented Seats screen<br>3. Read the CAN-B trace and check that the request signal sent for the current status is as specified by the truth table |
| Expected Result | 1. STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 3 (Heated_steering_wheel_high) is sent<br>2. The heated steering wheel icon registers the press<br>3. PENDING: DR-15 |
| Specification Reference | CFTS044-4858537 |
| Design Method | 決策表 (Decision Table Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | yes |
| DR Dependent | DR-15 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-15 —— 真值表之逐狀態送出值待覆；其覆前本條只驗前置狀態之設定，送出值不驗 |
| Reasoning | P1：主要功能邏輯；本條文之表（`Current status … Signal to be sent`）為真值表，**其驗證目標即「送出之值是否對應當前狀態」** —— 該值為 **DR-15 之 token 級標的**，於來源亦無逐字對應，故依 **R-VS71** 該處寫 `PENDING: DR-15`、前置步驟照寫。**初版以 `HSW_Tlm = 1 (Pressed)` 為 ER 者為 false pass** —— 設 off 得 Pressed、設 high 亦得 Pressed，HU 送錯階數亦通過（80 包 §1） |

### 11. [分層] `SWE1-VC-ThirdRowHeadrestDump-027` — Headrest Dump softkey reachable from the Rear View Camera screen — head restraint

**抽樣理由**：分層：`Common Features` × `screen_pending = no`（該格 21 條，取排序中位）
**形態**：`未標形態（早批）`　**批**：`batch02_v5.json`

**來源條文（逐字）**

```
The Third Row Headrest Dump Softkey button will also be accessible from the Rear View Camera screen, if applicable.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-ThirdRowHeadrestDump-027` |
| Test Set | Common Features |
| TC Title | Headrest Dump softkey reachable from the Rear View Camera screen — head restraint |
| Test Item | The Third Row Headrest Dump softkey shall also be accessible from the Rear View Camera screen, when supported.<br><br>(Entry path: Rear View Camera screen) |
| Pre-Conditions | 1. The vehicle is equipped with the third row head restraint dump feature<br>2. PROXI Rear_View_Camera = 1 (Present)<br>3. The HU is on the home screen |
| Input Test Data | NA |
| Test Procedure | 1. Open the Rear View Camera screen from the Menu Bar<br>2. Check that the "Headrest Dump" softkey button is displayed on the Rear View Camera screen |
| Expected Result | 1. The Rear View Camera screen is displayed<br>2. The "Headrest Dump" softkey button is displayed |
| Specification Reference | CFTS044-4858988 |
| Design Method | 功能測試 (Functional based ; no specific technique) |
| Priority | P1 |
| Split Flag | True |
| Split Reason | §8.2.2 不同控制實體 → 拆；本條之實體為 head restraint（原條涵蓋 rear camera、head restraint） |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | no |
| Remarks |  |
| Reasoning | P1：主要功能邏輯 |

### 12. [分層] `SWE1-VC-SwitchLHD/RHDConfiguration-013` — Right hand drive modifies the seat control layout

**抽樣理由**：分層：`Common Features` × `screen_pending = yes`（該格 2 條，取排序中位）
**形態**：`G6 DriverSide 之條件`　**批**：`batch23.json`

**來源條文（逐字）**

```
When $DriverSide$ = [Right hand drive] the HMI shall be modified as defined by HMI requirements.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-SwitchLHD/RHDConfiguration-013` |
| Test Set | Common Features |
| TC Title | Right hand drive modifies the seat control layout |
| Test Item | When $DriverSide$ = [Right hand drive] the HMI shall be modified as defined by HMI requirements.<br><br>(Right hand drive configuration) |
| Pre-Conditions | 1. The HU is in the Full-Operation state<br>2. The Heated / Vented Seats screen is displayed |
| Input Test Data | NA |
| Test Procedure | 1. Set PROXI Driver_Side = 0 (Left Side) and record the seat control layout as Layout_LHD<br>2. Set PROXI Driver_Side = 1 (Right Side)<br>3. Power cycle the HU and check that the seat control layout differs from Layout_LHD |
| Expected Result | 1. PROXI Driver_Side = 0 (Left Side) is accepted；Layout_LHD is recorded<br>2. PROXI Driver_Side = 1 (Right Side) is accepted<br>3. PENDING: DR-5-B |
| Specification Reference | CFTS044-4859509 |
| Design Method | 等價劃分 (Equivalence Partitioning, EP) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | yes |
| Remarks | BLOCKED: DR-5-B —— 右駕版面之具體定義待 HMI requirements |
| Reasoning | P1：主要功能邏輯；**G6 DriverSide 之條件** —— 條文逐字「the HMI shall be modified as defined by HMI requirements」——**其所指之 HMI requirements 不在本 feature 之範圍**（§8.4.2），故只驗「有無變更」，其具體版面依 R-VS59(4) 標 PENDING |

### 13. [分層] `SWE1-VC-RightFrontHeatedSeat-024` — Invalid heated seat status value is ignored

**抽樣理由**：分層：`Heated Seat` × `screen_pending = no`（該格 23 條，取排序中位）
**形態**：`G2 值域宣告 ＋ 其餘為無效`　**批**：`batch23.json`

**來源條文（逐字）**

```
For vehicles with three states (i.e. LO, MEDIUM, and HI), the HU shall implement the following requirements:Valid values for the $HeatedSeatFR$ are shown below. All other states shall be considered invalid by the HU. $HeatedSeatFR$ = [Heated Seat Off / HS_OFF] $HeatedSeatFR$ = [Heated Seat Low / HS_LO] $HeatedSeatFR$ = [Heated Seat Medium / HS_MED] $HeatedSeatFR$ = [Heated Seat High / HS_HI]
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-RightFrontHeatedSeat-024` |
| Test Set | Heated Seat |
| TC Title | Invalid heated seat status value is ignored |
| Test Item | For vehicles with three states (i.e. LO, MEDIUM, and HI), the HU shall implement the following requirements:Valid values for the $HeatedSeatFR$ are shown below. All other states shall be considered invalid by the HU. $HeatedSeatFR$ = [Heated Seat Off / HS_OFF] $HeatedSeatFR$ = [Heated Seat Low / HS_LO] $HeatedSeatFR$ = [Heated Seat Medium / HS_MED] $HeatedSeatFR$ = [Heated Seat High / HS_HI]<br><br>(Value outside the declared valid set) |
| Pre-Conditions | 1. The vehicle is equipped with the heated seat<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off) and record the displayed state as Display_valid<br>2. Send CAN: STATUS_CSWM.FR_HS_STATSts = a value outside the declared valid set<br>3. Read the displayed state of the heated seat and check that it is unchanged from Display_valid |
| Expected Result | 1. STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off) is sent；Display_valid is recorded<br>2. PENDING: DR-18<br>3. The heated seat display is unchanged from Display_valid |
| Specification Reference | CFTS044-4858338 |
| Design Method | 負向測試 (Negative / Invalid) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent | DR-18 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-18 —— 該訊號 0–3 皆已定義，無效碼之定義待覆 |
| Reasoning | P1：主要功能邏輯；**G2 值域宣告 ＋ 其餘為無效** —— 條文列 `HeatedSeatFR` 之合法值集並逐字宣告「All other states shall be considered invalid by the HU」——**其可測內容即「非合法值不改變顯示」**，而該訊號為 2 bit、其 0–3 四碼**皆已定義** —— **無未用碼可注入**；依 §8.4.1 不得造值，故該步驟之 ER 依 R-VS71 寫 `PENDING: DR-18`（無效碼之定義待覆） |

### 14. [分層] `SWE1-VC-RightFrontHeatedSeat-033` — Right front heated seat display follows status off

**抽樣理由**：分層：`Heated Seat` × `screen_pending = yes`（該格 8 條，取排序中位）
**形態**：`E 型（早批）`　**批**：`batch22.json`

**來源條文（逐字）**

```
When the HU receives a $HeatedSeatFR$ = [Heated Seat Off / HS_OFF] signal, the HU shall change the stored status of the RF heated seat and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-RightFrontHeatedSeat-033` |
| Test Set | Heated Seat |
| TC Title | Right front heated seat display follows status off |
| Test Item | When the HU receives a $HeatedSeatFR$ = [Heated Seat Off / HS_OFF] signal, the HU shall change the stored status of the RF heated seat and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.<br><br>(Status transition to off) |
| Pre-Conditions | 1. The vehicle is equipped with the seat function under test<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CSWM.FR_HS_STATSts = 3 (Heated_seat_high) and record the right front heated seat display state as Right_display_before<br>2. Send CAN: STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off)<br>3. Read the displayed state of the right front heated seat and check that it changes from Right_display_before |
| Expected Result | 1. STATUS_CSWM.FR_HS_STATSts = 3 (Heated_seat_high) is sent；Right_display_before is recorded<br>2. STATUS_CSWM.FR_HS_STATSts = 0 (Heated_seat_off) is sent<br>3. The right front heated seat display changes from Right_display_before |
| Specification Reference | CFTS044-4858356 |
| Design Method | 狀態轉換 (State Transition Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | yes |
| Remarks | BLOCKED: DR-5-B —— 變更後之顯示樣式待 TLM HMI Document；BLOCKED: DR-24′ —— `<Tdisplay>` 之上限值待覆 |
| Reasoning | P1：主要功能邏輯；**E 型 —— 觸發為收到狀態訊號**（`When the HU receives a … signal`），標的為顯示之變更。其具體樣式待 TLM HMI Document，依 R-VS59(4) 寫最弱斷言 |

### 15. [分層] `SWE1-VC-HeatedSteeringWheel-012` — Heated steering wheel press sends the request signal

**抽樣理由**：分層：`Heated Steering Wheel` × `screen_pending = no`（該格 7 條，取排序中位）
**形態**：`A 型（早批）`　**批**：`batch21_probe.json`

**來源條文（逐字）**

```
When the customer selects to change the state of the heated steering wheel, the HU shall send an on-change $HSW_RQ_TGW$ = [Pressed / PSD] signal to the CSWM within &lt;Tsend&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-012` |
| Test Set | Heated Steering Wheel |
| TC Title | Heated steering wheel press sends the request signal |
| Test Item | When the customer selects to change the state of the heated steering wheel, the HU shall send an on-change $HSW_RQ_TGW$ = [Pressed / PSD] signal to the CSWM within &lt;Tsend&gt;.<br><br>(Press sends the on-change request) |
| Pre-Conditions | 1. The vehicle is equipped with a heated steering wheel<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator with signal tracing enabled |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 0 (Heated_steering_wheel_off)<br>2. Press the heated steering wheel icon on the Heated / Vented Seats screen<br>3. Read the CAN-B trace and check that TELEMATIC_VEHICLE_SETUP3.HSW_Tlm = 1 (Pressed) is transmitted |
| Expected Result | 1. STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 0 (Heated_steering_wheel_off) is sent<br>2. The heated steering wheel icon registers the press<br>3. TELEMATIC_VEHICLE_SETUP3.HSW_Tlm = 1 (Pressed) is sent |
| Specification Reference | CFTS044-4858531 |
| Design Method | 功能測試 (Functional based ; no specific technique) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | yes |
| DR Dependent | DR-15 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-15 —— 請求訊號之編碼待覆；BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆，ER 只寫可觀察終態 |
| Reasoning | P1：主要功能邏輯；**D 型之觸發為使用者按壓**（條文 `the customer selects to change the state`），與 A 型之 `IF <狀態值> THEN` 不同。`HSW_RQ_TGW` 為 DR-15 之 token 級標的，依 R-VS71 照寫；其時限 `<Tsend>` 依 42 包之處置以 remarks 標 BLOCKED |

### 16. [分層] `SWE1-VC-HeatedSteeringWheel-019` — Heated steering wheel display follows status medium

**抽樣理由**：分層：`Heated Steering Wheel` × `screen_pending = yes`（該格 4 條，取排序中位）
**形態**：`E 型（早批）`　**批**：`batch22.json`

**來源條文（逐字）**

```
When the HU receives a $HSW_Stat_2$ = [Heated steering wheel medium / HSW_MED] signal, the HU shall change the stored status of the heated steering wheel to MED and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-HeatedSteeringWheel-019` |
| Test Set | Heated Steering Wheel |
| TC Title | Heated steering wheel display follows status medium |
| Test Item | When the HU receives a $HSW_Stat_2$ = [Heated steering wheel medium / HSW_MED] signal, the HU shall change the stored status of the heated steering wheel to MED and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.<br><br>(Status transition to medium) |
| Pre-Conditions | 1. The vehicle is equipped with a heated steering wheel<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 0 (Heated_steering_wheel_off) and record the heated steering wheel display state as Heated_display_before<br>2. Send CAN: STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 2 (Heated_steering_wheel_medium)<br>3. Read the displayed state of the heated steering wheel and check that it changes from Heated_display_before |
| Expected Result | 1. STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 0 (Heated_steering_wheel_off) is sent；Heated_display_before is recorded<br>2. STATUS_CLIMATE8.Tri_Level_HSW_StatSts = 2 (Heated_steering_wheel_medium) is sent<br>3. The heated steering wheel display changes from Heated_display_before |
| Specification Reference | CFTS044-4858542 |
| Design Method | 狀態轉換 (State Transition Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | yes |
| Remarks | BLOCKED: DR-5-B —— 變更後之顯示樣式待 TLM HMI Document；BLOCKED: DR-24′ —— `<Tdisplay>` 之上限值待覆 |
| Reasoning | P1：主要功能邏輯；**E 型 —— 觸發為收到狀態訊號**（`When the HU receives a … signal`），標的為顯示之變更。其具體樣式待 TLM HMI Document，依 R-VS59(4) 寫最弱斷言 |

### 17. [分層] `SWE1-VC-RightFrontVentedSeat-028` — Right front vented seat press sends the request signal

**抽樣理由**：分層：`Vented Seat` × `screen_pending = no`（該格 18 條，取排序中位）
**形態**：`D 型（送出）`　**批**：`batch23.json`

**來源條文（逐字）**

```
When the customer selects to change the state of the RF vented seat, the HU shall send an on-change $FR_VS_RQ_TGW$ = [Vented Seat Pressed / VS_PSD] signal to the CSWM within &lt;Tsend&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-RightFrontVentedSeat-028` |
| Test Set | Vented Seat |
| TC Title | Right front vented seat press sends the request signal |
| Test Item | When the customer selects to change the state of the RF vented seat, the HU shall send an on-change $FR_VS_RQ_TGW$ = [Vented Seat Pressed / VS_PSD] signal to the CSWM within &lt;Tsend&gt;.<br><br>(Press sends the on-change request) |
| Pre-Conditions | 1. The vehicle is equipped with the right front vented seat<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator with signal tracing enabled |
| Input Test Data | NA |
| Test Procedure | 1. Start a bus trace on CAN-B that captures the frames carrying TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm<br>2. Press the right front vented seat icon<br>3. Read the CAN-B trace and check that the value sent on TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm is the one specified for the current state |
| Expected Result | 1. The bus trace is running and is capturing the frames carrying TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm<br>2. The right front vented seat icon registers the press<br>3. PENDING: DR-15 |
| Specification Reference | CFTS044-4858410 |
| Design Method | 功能測試 (Functional based ; no specific technique) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | yes |
| DR Dependent | DR-15 |
| Screen Pending | no |
| Remarks | BLOCKED: DR-15 —— 請求訊號之編碼待覆；BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆 |
| Reasoning | P1：主要功能邏輯；**D 型（送出）** —— 觸發為使用者按壓、標的為匯流排上之送出值。**其送出值為 DR-15 之 token 級標的**，於來源無逐字對應 —— 依 R-VS71 該步驟之 ER 寫 `PENDING: DR-15`、前置步驟照寫。**不以「有送出」代替「送出正確之值」**（80 包 §1，A-VS157） |

### 18. [分層] `SWE1-VC-RightFrontVentedSeat-033` — Right front vented seat display follows status medium

**抽樣理由**：分層：`Vented Seat` × `screen_pending = yes`（該格 2 條，取排序中位）
**形態**：`E 型（早批）`　**批**：`batch22.json`

**來源條文（逐字）**

```
When the HU receives an $VentedSeatFR$ = [Vented seat medium / VS_MED] signal, the HU shall change the stored status of the RF vented seat and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.
```

| 欄 | 內容 |
|---|---|
| Leaf ID | `SWE1-VC-RightFrontVentedSeat-033` |
| Test Set | Vented Seat |
| TC Title | Right front vented seat display follows status medium |
| Test Item | When the HU receives an $VentedSeatFR$ = [Vented seat medium / VS_MED] signal, the HU shall change the stored status of the RF vented seat and change the display as specified by the HMI within a time period of &lt;Tdisplay&gt;.<br><br>(Status transition to medium) |
| Pre-Conditions | 1. The vehicle is equipped with the seat function under test<br>2. The Heated / Vented Seats screen is displayed<br>3. CAN-B is connected to the bus simulator |
| Input Test Data | NA |
| Test Procedure | 1. Send CAN: STATUS_CSWM.FR_VS_STATSts = 0 (Vented_seat_off) and record the right front vented seat display state as Right_display_before<br>2. Send CAN: STATUS_CSWM.FR_VS_STATSts = 2 (Vented_seat_medium)<br>3. Read the displayed state of the right front vented seat and check that it changes from Right_display_before |
| Expected Result | 1. STATUS_CSWM.FR_VS_STATSts = 0 (Vented_seat_off) is sent；Right_display_before is recorded<br>2. STATUS_CSWM.FR_VS_STATSts = 2 (Vented_seat_medium) is sent<br>3. The right front vented seat display changes from Right_display_before |
| Specification Reference | CFTS044-4858419 |
| Design Method | 狀態轉換 (State Transition Testing) |
| Priority | P1 |
| Split Flag | False |
| Split Reason |  |
| DR-15 Exposed | no |
| DR Dependent |  |
| Screen Pending | yes |
| Remarks | BLOCKED: DR-5-B —— 變更後之顯示樣式待 TLM HMI Document；BLOCKED: DR-24′ —— `<Tdisplay>` 之上限值待覆 |
| Reasoning | P1：主要功能邏輯；**E 型 —— 觸發為收到狀態訊號**（`When the HU receives a … signal`），標的為顯示之變更。其具體樣式待 TLM HMI Document，依 R-VS59(4) 寫最弱斷言 |
