# 上繳包 04 —— T10a–d 架構傾印、T11a–c Market Config、T-登

- 日期：2026-08-27
- 對應下放：**二包併呈**（下放包 06 §四 明文併入本檔）
  - `docs/handoff/05_arch_suspend.md`
    （SHA256 `9f50273a8b9587094b81351c1441aad7a7ccc2349a3f8c656e524fb0c5053208`，150 行）
  - `docs/handoff/06_market_config.md`
    （SHA256 `4116c0accdf8f4e28fc8f8b040aa054a0992c682f32a51a8da9fba71a5e5398e`，86 行）
- **結論：T10a–d、T11a–c、T-登 全數完成。本輪只量測與登記。**
- **未做**：改 profile、任何 TC、pilot、git、任何架構選擇（Q7 屬 Pei）、
  任何文件識別之判定（Q9 屬 Pei）。

---

## 0. 三件請你先看

1. **`$VC_Trans_Equipped$` 在綁定之二 DBC 完全沒有 CAN 路徑** ——
   r420 與 r421 兩列合計六個候選名，**全部不在**；且 r420 之 Atlantis 欄
   逐字為 `Not Applicable`。**Q7 無論裁哪個架構，這個訊號都施加不出來。** 見 §3.2。
2. **誤一（缺分頁名）之所以逃過檢查，是因為錯的那一列其訊號「查得到」** ——
   `LID CAN Mapping r43` 之 `ACV_FailType` 在二 DBC 皆在。
   **一個「存在性檢查」對它會亮綠燈。** 見 §4.1。
3. **我這輪自己也犯了一次抽取瑕疵並修掉** —— 初版把 LID 儲存格內以
   「空白＋單引號」串接之二個訊號名切成一個畸形字串，報出假的「不在」，
   **而該名我在 T9 已量到它在**。見 §5.1。

---

## 1. T10a–d 原始輸出

```
# T10a–d —— 原始輸出

素材：`features/vehicle_setting/inputs/Logical Identifiers and CAN Mapping v1_76.xlsx`（R-DD5 綁定件，未複製）

**架構帶取自各分頁 r2 之合併標題列，非硬編**：

- `CAN Mapping`：c0+ = LID Information；c5+ = Powernet；c10+ = CUSW；c15+ = Atlantis；c20+ = Compact；c25+ = Atlantis High；c30+ = Comments
- `Proxi & Configuration`：c0+ = LID Information；c5+ = Powernet；c10+ = CUSW；c15+ = Atlantis & Atlantis High；c20+ = Compact；c25+ = Comments

---

## T10a —— `$Speedometer$`

### `$Speedometer$` —— `LID CAN Mapping r1738`

| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|
|---|---|---|---|
| c0 | **LID Information** | Logical Identifier | `Speedometer` |
| c1 | **LID Information** | Function | `Vehicle speed` |
| c2 | **LID Information** | Object Text | `VehicleSpeedVSOSig` |
| c3 | **LID Information** | Arch Basis | `Pnet` |
| c4 | **LID Information** | Transfer Function (from other  | `CUSW⏎GW_C1.VEH_SPEED = STATUS_B_BSM.VehicleSpeed * ( 0.0625 / 0.0078125)⏎GW_C1.VEH_SPEED [65535] = STATUS_B_BSM.VehicleSpeedFailSts [1]⏎Atlantis⏎GW_C1.VEH_SPEED = STATUS_CCAN3.VehicleSpeedVSOSig * ( 0.0625 / 0.0078125)⏎GW_C1.VEH_SPEED [6553` |
| c5 | **Powernet** | Signal Name | `GW_C1.VEH_SPEED` |
| c6 | **Powernet** | CAN | `CAN-B` |
| c7 | **Powernet** | Format | `Powernet⏎16 bit signal          ⏎0 - +511.984375 km/h⏎resolution = 0.0078125 km/h` |
| c8 | **Powernet** | SNA | `FFFFh` |
| c9 | **Powernet** | VFs | `174⏎451⏎551⏎651⏎673⏎683⏎684` |
| c10 | **CUSW** | Signal Name | `STATUS_B_BSM.VehicleSpeed⏎STATUS_B_BSM.VehicleSpeedFailSts⏎⏎0r⏎⏎Vehicle_speed_odometer.Vehiclespeed` |
| c11 | **CUSW** | CAN | `CAN-B` |
| c12 | **CUSW** | Format | `CUSW⏎13 bit signal (VehicleSpeed)⏎0 - +512 km/h⏎resolution = 0.0625 kmh⏎⏎1 bit signal (VehicleSpeedFailSts)⏎0 = Fail_not_present⏎1 = Fail_present` |
| c13 | **CUSW** | SNA | `Fail_present` |
| c14 | **CUSW** | VFs | `174⏎451⏎551⏎651⏎657⏎673⏎684` |
| c15 | **Atlantis** | Signal Name | `STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.VehicleSpeedVSOSigFailSts` |
| c17 | **Atlantis** | Format | `ATLANTIS⏎13 bit signal⏎0 - 511.875 km/h⏎Resolution = 0.0625 kmh` |
| c19 | **Atlantis** | VFs | `174⏎176⏎451⏎651⏎665⏎673` |
| c20 | **Compact** | Signal Name | `VEHICLE_SPEED_ODOMETER.VehicleSpeed⏎VEHICLE_SPEED_ODOMETER.VehicleSpeedFailSts` |
| c21 | **Compact** | CAN | `CAN-B` |
| c22 | **Compact** | Format | `13 bit signal⏎0 - 512 km/h⏎Resolution = 0.0625 kmh⏎⏎1 bit signal ⏎0 = Fail_not_present⏎1 = Fail_present` |
| c23 | **Compact** | SNA | `Fail_present` |
| c25 | **Atlantis High** | Signal Name | `STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.VehicleSpeedVSOSigFailSts⏎⏎BRAKE_FD_2.VehicleSpeedVSOSig` |
| c26 | **Atlantis High** | CAN | `CAN-B⏎⏎⏎FD` |
| c27 | **Atlantis High** | Format | `ATLANTIS⏎13 bit signal⏎0 - 511.875 km/h⏎Resolution = 0.0625 kmh` |
| c29 | **Atlantis High** | VFs | `174⏎176⏎451⏎651⏎665⏎673` |
| c30 | **Comments** | Usage Comment | ` ` |

**非空欄 27 個**（該列全欄已列，未省略）

---

## T10b —— `$VC_Trans_Equipped$`（r420 **與** r421 兩列）與 `$PresentGear$`

> **兩列皆給全貌，何者為準由分析層裁**（T10b 明文）。

### `Proxi & Configuration` r420 —— `LID Proxi & Configuration r420`

| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|
|---|---|---|---|
| c0 | **LID Information** | Logical Identifier | `VC_Trans_Equipped` |
| c2 | **LID Information** | Object Text | `VC_Trans_Equipped` |
| c5 | **Powernet** | Signal Name | `VC_Trans_Equipped` |
| c6 | **Powernet** | CAN | `CAN-C` |
| c10 | **CUSW** | Signal Name | `Not Applicable` |
| c15 | **Atlantis & Atlantis High** | Signal Name | `Not Applicable` |

**非空欄 6 個**（該列全欄已列，未省略）

### `Proxi & Configuration` r421 —— `LID Proxi & Configuration r421`

| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|
|---|---|---|---|
| c0 | **LID Information** | Logical Identifier | `VC_Trans_Equipped` |
| c1 | **LID Information** | Function | `Transmission manual or automatic` |
| c2 | **LID Information** | Object Text | `VC_Trans_Equipped` |
| c3 | **LID Information** | Arch Basis | `Pnet` |
| c5 | **Powernet** | Signal Name | `VehCfg7.VC_Trans_Equipped` |
| c6 | **Powernet** | CAN | `CAN-B` |
| c7 | **Powernet** | Format | `Transmission equipped: 0 = Automatic & 1 = Manual` |
| c10 | **CUSW** | Signal Name | `Gear_Box_Type` |
| c15 | **Atlantis & Atlantis High** | Signal Name | `Gear_Box_Type` |

**非空欄 9 個**（該列全欄已列，未省略）

### `$PresentGear$` —— `LID CAN Mapping r1397`

| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|
|---|---|---|---|
| c0 | **LID Information** | Logical Identifier | `PresentGear` |
| c1 | **LID Information** | Function | `Current Gear` |
| c3 | **LID Information** | Arch Basis | `Pnet` |
| c4 | **LID Information** | Transfer Function (from other  | `See tables to right⏎Powernet 0-6 = CUSW 0-6⏎Powernet 7,8 = CUSW 7,8⏎Powernet 10 = CUSW 9⏎Powernet 11 = CUSW 10                                ⏎Powernet 13 = CUSW 12⏎Powernet 15 = CUSW 15` |
| c5 | **Powernet** | Signal Name | `GW_C1.Gr` |
| c6 | **Powernet** | CAN | `CAN-B` |
| c7 | **Powernet** | Format | `Powernet⏎4 bit signal⏎0=Current gear "N" (or ParkNeutral) / N⏎1=Current gear "1" / D1⏎2=Current gear "2" / D2⏎3=Current gear "3" / D3⏎4=Current gear "4 (62TE 4P)" / D4⏎5=Current gear "5 (RFE 4P, 62TE 4)" / D5⏎6=Current gear "6 (62TE 5)" / D` |
| c8 | **Powernet** | SNA | `Fh` |
| c9 | **Powernet** | VFs | `673⏎651` |
| c10 | **CUSW** | Signal Name | `GEARMOT3.ActualGear` |
| c11 | **CUSW** | CAN | `CAN-C` |
| c12 | **CUSW** | Format | `CUSW⏎4 bit signal⏎0 = NEUTRAL⏎1 = D1⏎2 = D2⏎3 = D3⏎4 = D4⏎5 = D5⏎6 = D6⏎7 = D7⏎8 = D8⏎9 = D9⏎10 = R⏎11 = R2⏎12 = P⏎15 = SNA` |
| c13 | **CUSW** | SNA | `Fh` |
| c15 | **Atlantis** | Signal Name | `ENGINE7.ActualGearGSI⏎TRANSM2.GearEngaged⏎TRANSM2.ShiftLeverPosition` |
| c17 | **Atlantis** | Format | `ATLANTIS⏎4 bit signal⏎0 = Neutral⏎1 = ForwardGear_1⏎2 = ForwardGear_2⏎3 = ForwardGear_3⏎4 = ForwardGear_4⏎5 = ForwardGear_5⏎6 = ForwardGear_6⏎7 = Reverse⏎8 = ForwardGear_7⏎9 = ForwardGear_8⏎10 = ForwardGear_9⏎15 = SNA` |
| c18 | **Atlantis** | SNA | `Fh` |
| c19 | **Atlantis** | VFs | `674` |
| c20 | **Compact** | Signal Name | `STATUS_B_TCM_MTA_DCTM.ActualGearForDisplay` |
| c21 | **Compact** | CAN | `CAN-B` |
| c25 | **Atlantis High** | Signal Name | `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT⏎VDCM_PWT2.GearEngagedForDisplay_VDCM` |
| c26 | **Atlantis High** | CAN | `FD` |
| c27 | **Atlantis High** | Format | `0 = Initialize⏎1 = Gear_1⏎2 = Gear_2⏎3 = Gear_3⏎4 = Gear_4⏎5 = Gear_5⏎6 = Gear_6⏎7 = Gear_7⏎8 = Gear_8⏎9 = Gear_9⏎12 = Park⏎13 = Neutral⏎14 = Reverse⏎15 = Drive⏎16 = Low⏎17 = Manual⏎18 = Sport_Mode⏎31 = SNA` |
| c30 | **Comments** | Usage Comment | `VDCM_PWT2.GearEngagedForDisplay_VDCM⏎This signal is used only for the M182BEV program. more information in M182BEV Specific Signals⏎TRANSM2.ShiftLeverPosition This signal is used only for the 332BEV program, more information in 332BEV Speci` |
| c31 | **Comments** | Primary CFTS Usage | `CFTS053` |
| c33 | **Comments** | Revision Comments  | `See V1.53 revision note (3)⏎` |

**非空欄 25 個**（該列全欄已列，未省略）

---

## T10d —— `Country_Code` 二分頁同號兩列

> 誤一之更正回填素材：`r43` 於二分頁各有一列且內容不同。

### `CAN Mapping` r43 —— `LID CAN Mapping r43`

| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|
|---|---|---|---|
| c0 | **LID Information** | Logical Identifier | `ACV_FailType` |
| c5 | **Powernet** | Signal Name | `FT_HVAC_ICS_STAT_M.ACV_FailType` |
| c6 | **Powernet** | CAN | `B` |
| c7 | **Powernet** | Format | `0=None⏎1-7 = Reserved` |
| c25 | **Atlantis High** | Signal Name | `STATUS_CLIMATE9.ACV_FailType⏎BCM_FD_26.ACV_FailType` |
| c26 | **Atlantis High** | CAN | `B⏎FD` |
| c27 | **Atlantis High** | Format | `0=None⏎1-7 = Reserved` |
| c30 | **Comments** | Usage Comment | `ECC shall use the CAN B signal.⏎TBM shall use the FD signal.` |
| c31 | **Comments** | Primary CFTS Usage | `CFTS041` |
| c33 | **Comments** | Revision Comments  | `• See V1.56 revision note (5)` |

**非空欄 10 個**（該列全欄已列，未省略）

### `Proxi & Configuration` r43 —— `LID Proxi & Configuration r43`

| 欄 | 架構帶 | 欄名（r3）| 值（逐字）|
|---|---|---|---|
| c0 | **LID Information** | Logical Identifier | `Country_Code` |
| c1 | **LID Information** | Function | `Country Code` |
| c2 | **LID Information** | Object Text | `Proxi_Country_Code` |
| c4 | **LID Information** | Transfer Function (from other  | `Refer to CUSW Proxi` |
| c5 | **Powernet** | Signal Name | `ECUCfg3.EC_AudTel1b-<DEST>` |
| c7 | **Powernet** | Format | `See latest version of 'CIP Market Configuration Table v*.xlsx', worksheet 'Market Configuration'.` |
| c8 | **Powernet** | SNA | ` ` |
| c10 | **CUSW** | Signal Name | `Car_Configuration_16.Country_Code` |
| c11 | **CUSW** | CAN | `PROXI` |
| c15 | **Atlantis & Atlantis High** | Signal Name | `Car_Configuration_16.Country_Code` |
| c16 | **Atlantis & Atlantis High** | CAN | `PROXI` |

**非空欄 11 個**（該列全欄已列，未省略）

---

## T10c —— 各架構名於綁定二 DBC 之存在性

綁定件：`PDT27_E2A_R4_BHCAN.dbc`（155 訊息）／`PDT27_E2A_R5_FDCAN8.dbc`（323 訊息）

| LID 來源 | 架構帶 | 訊號名（逐字）| 在／不在 | BO_（id）| 長度 | factor／offset | 單位 |
|---|---|---|---|---|---|---|---|
| $Speedometer$ | Powernet | `GW_C1.VEH_SPEED` | **不在** | — | — | — | — |
| $Speedometer$ | CUSW | `STATUS_B_BSM.VehicleSpeed` | **不在** | — | — | — | — |
| $Speedometer$ | CUSW | `STATUS_B_BSM.VehicleSpeedFailSts` | **不在** | — | — | — | — |
| $Speedometer$ | CUSW | `0r` | **非訊號名形態（未查）** | — | — | — | — |
| $Speedometer$ | CUSW | `Vehicle_speed_odometer.Vehiclespeed` | **不在** | — | — | — | — |
| $Speedometer$ | Atlantis | `STATUS_CCAN3.VehicleSpeedVSOSig` | **在**（`PDT27_E2A_R4_BHCAN.dbc`）| `STATUS_CCAN3`（994）| 13 bit | `0.0625`／`0` | `Km/h` |
| $Speedometer$ | Atlantis | `STATUS_CCAN3.VehicleSpeedVSOSigFailSts` | **不在** | — | — | — | — |
| $Speedometer$ | Compact | `VEHICLE_SPEED_ODOMETER.VehicleSpeed` | **不在** | — | — | — | — |
| $Speedometer$ | Compact | `VEHICLE_SPEED_ODOMETER.VehicleSpeedFailSts` | **不在** | — | — | — | — |
| $Speedometer$ | Atlantis High | `STATUS_CCAN3.VehicleSpeedVSOSig` | **在**（`PDT27_E2A_R4_BHCAN.dbc`）| `STATUS_CCAN3`（994）| 13 bit | `0.0625`／`0` | `Km/h` |
| $Speedometer$ | Atlantis High | `STATUS_CCAN3.VehicleSpeedVSOSigFailSts` | **不在** | — | — | — | — |
| $Speedometer$ | Atlantis High | `BRAKE_FD_2.VehicleSpeedVSOSig` | **在**（`PDT27_E2A_R5_FDCAN8.dbc`）| `BRAKE_FD_2`（258）| 13 bit | `0.0625`／`0` | `Km/h` |
| $VC_Trans_Equipped$ (r420) | Powernet | `VC_Trans_Equipped` | **不在** | — | — | — | — |
| $VC_Trans_Equipped$ (r420) | CUSW | `Not Applicable` | **非訊號名形態（未查）** | — | — | — | — |
| $VC_Trans_Equipped$ (r420) | Atlantis & Atlantis High | `Not Applicable` | **非訊號名形態（未查）** | — | — | — | — |
| $VC_Trans_Equipped$ (r421) | Powernet | `VehCfg7.VC_Trans_Equipped` | **不在** | — | — | — | — |
| $VC_Trans_Equipped$ (r421) | CUSW | `Gear_Box_Type` | **不在** | — | — | — | — |
| $VC_Trans_Equipped$ (r421) | Atlantis & Atlantis High | `Gear_Box_Type` | **不在** | — | — | — | — |
| $PresentGear$ | Powernet | `GW_C1.Gr` | **不在** | — | — | — | — |
| $PresentGear$ | CUSW | `GEARMOT3.ActualGear` | **不在** | — | — | — | — |
| $PresentGear$ | Atlantis | `ENGINE7.ActualGearGSI` | **不在** | — | — | — | — |
| $PresentGear$ | Atlantis | `TRANSM2.GearEngaged` | **不在** | — | — | — | — |
| $PresentGear$ | Atlantis | `TRANSM2.ShiftLeverPosition` | **不在** | — | — | — | — |
| $PresentGear$ | Compact | `STATUS_B_TCM_MTA_DCTM.ActualGearForDisplay` | **不在** | — | — | — | — |
| $PresentGear$ | Atlantis High | `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT` | **在**（`PDT27_E2A_R5_FDCAN8.dbc`）| `PT_SYSTEM_FD_1`（263）| 5 bit | `1`／`0` | `` |
| $PresentGear$ | Atlantis High | `VDCM_PWT2.GearEngagedForDisplay_VDCM` | **不在** | — | — | — | — |
| $Country_Code$ (CAN Mapping r43) | Powernet | `FT_HVAC_ICS_STAT_M.ACV_FailType` | **不在** | — | — | — | — |
| $Country_Code$ (CAN Mapping r43) | Atlantis High | `STATUS_CLIMATE9.ACV_FailType` | **在**（`PDT27_E2A_R4_BHCAN.dbc`）| `STATUS_CLIMATE9`（1441）| 3 bit | `1`／`0` | `` |
| $Country_Code$ (CAN Mapping r43) | Atlantis High | `BCM_FD_26.ACV_FailType` | **在**（`PDT27_E2A_R5_FDCAN8.dbc`）| `BCM_FD_26`（1435）| 3 bit | `1`／`0` | `` |
| $Country_Code$ (Proxi & Configuration r43) | Powernet | `ECUCfg3.EC_AudTel1b-<DEST>` | **非訊號名形態（未查）** | — | — | — | — |
| $Country_Code$ (Proxi & Configuration r43) | CUSW | `Car_Configuration_16.Country_Code` | **不在** | — | — | — | — |
| $Country_Code$ (Proxi & Configuration r43) | Atlantis & Atlantis High | `Car_Configuration_16.Country_Code` | **不在** | — | — | — | — |

**不在者 22 筆**（照實列，未代換）：
- $Speedometer$ ／ Powernet ／ `GW_C1.VEH_SPEED`
- $Speedometer$ ／ CUSW ／ `STATUS_B_BSM.VehicleSpeed`
- $Speedometer$ ／ CUSW ／ `STATUS_B_BSM.VehicleSpeedFailSts`
- $Speedometer$ ／ CUSW ／ `Vehicle_speed_odometer.Vehiclespeed`
- $Speedometer$ ／ Atlantis ／ `STATUS_CCAN3.VehicleSpeedVSOSigFailSts`
- $Speedometer$ ／ Compact ／ `VEHICLE_SPEED_ODOMETER.VehicleSpeed`
- $Speedometer$ ／ Compact ／ `VEHICLE_SPEED_ODOMETER.VehicleSpeedFailSts`
- $Speedometer$ ／ Atlantis High ／ `STATUS_CCAN3.VehicleSpeedVSOSigFailSts`
- $VC_Trans_Equipped$ (r420) ／ Powernet ／ `VC_Trans_Equipped`
- $VC_Trans_Equipped$ (r421) ／ Powernet ／ `VehCfg7.VC_Trans_Equipped`
- $VC_Trans_Equipped$ (r421) ／ CUSW ／ `Gear_Box_Type`
- $VC_Trans_Equipped$ (r421) ／ Atlantis & Atlantis High ／ `Gear_Box_Type`
- $PresentGear$ ／ Powernet ／ `GW_C1.Gr`
- $PresentGear$ ／ CUSW ／ `GEARMOT3.ActualGear`
- $PresentGear$ ／ Atlantis ／ `ENGINE7.ActualGearGSI`
- $PresentGear$ ／ Atlantis ／ `TRANSM2.GearEngaged`
- $PresentGear$ ／ Atlantis ／ `TRANSM2.ShiftLeverPosition`
- $PresentGear$ ／ Compact ／ `STATUS_B_TCM_MTA_DCTM.ActualGearForDisplay`
- $PresentGear$ ／ Atlantis High ／ `VDCM_PWT2.GearEngagedForDisplay_VDCM`
- $Country_Code$ (CAN Mapping r43) ／ Powernet ／ `FT_HVAC_ICS_STAT_M.ACV_FailType`
- $Country_Code$ (Proxi & Configuration r43) ／ CUSW ／ `Car_Configuration_16.Country_Code`
- $Country_Code$ (Proxi & Configuration r43) ／ Atlantis & Atlantis High ／ `Car_Configuration_16.Country_Code`

**非訊號名形態 4 筆**（未查，與「查無」分開列）：
- $Speedometer$ ／ CUSW ／ `0r`
- $VC_Trans_Equipped$ (r420) ／ CUSW ／ `Not Applicable`
- $VC_Trans_Equipped$ (r420) ／ Atlantis & Atlantis High ／ `Not Applicable`
- $Country_Code$ (Proxi & Configuration r43) ／ Powernet ／ `ECUCfg3.EC_AudTel1b-<DEST>`

### `VAL_` 列舉逐字（查得者）

- `PDT27_E2A_R4_BHCAN.dbc` `STATUS_CCAN3`.`VehicleSpeedVSOSig` (msg 994)：`8191 "SNA"`
- `PDT27_E2A_R5_FDCAN8.dbc` `BRAKE_FD_2`.`VehicleSpeedVSOSig` (msg 258)：`8191 "SNA"`
- `PDT27_E2A_R5_FDCAN8.dbc` `PT_SYSTEM_FD_1`.`GearEngagedForDisplay_PT` (msg 263)：`0 "Initialize" 1 "Gear_1st" 2 "Gear_2nd" 3 "Gear_3rd" 4 "Gear_4th" 5 "Gear_5th" 6 "Gear_6th" 7 "Gear_7th" 8 "Gear_8th" 9 "Gear_9th" 12 "Park" 13 "Neutral" 14 "Reverse" 15 "Drive" 16 "Low" 17 "Manual" 18 "Sport_Mode" 31 "SNA"`
- `PDT27_E2A_R4_BHCAN.dbc` `STATUS_CLIMATE9`.`ACV_FailType` (msg 1441)：`0 "None"`
- `PDT27_E2A_R5_FDCAN8.dbc` `BCM_FD_26`.`ACV_FailType` (msg 1435)：`0 "None"`
```

---

## 2. T10a／T10d —— 誤一之更正素材

### 2.1 `LID CAN Mapping r1738`（`$Speedometer$`）

架構帶取自該分頁 **r2 之合併標題列**（非硬編）：
`c0+ LID Information／c5+ Powernet／c10+ CUSW／c15+ Atlantis／c20+ Compact／
c25+ Atlantis High／c30+ Comments`。

**profile §3 取的是 c5（Powernet）之 `GW_C1.VEH_SPEED`。**

### 2.2 `Country_Code` 之同號二列（誤一之核心）

| 位置 | `Logical Identifier` |
|---|---|
| `LID CAN Mapping r43` | **`ACV_FailType`** |
| `LID Proxi & Configuration r43` | **`Country_Code`** |

**「LID r43」四字無法區分二者** —— §1.1 之拘束
（一律書 `LID {分頁名} r{n}`）本輪已全程遵行。

---

## 3. T10b／T10c —— 兩列全貌與存在性

### 3.1 r420 與 r421 —— **兩列皆給，未判何者為準**

| 位置 | `Logical Identifier` | 各帶之 `Signal Name` |
|---|---|---|
| `LID Proxi & Configuration r420` | **`VC_Trans_Equipped`** | Powernet `VC_Trans_Equipped`；CUSW `Not Applicable`；**Atlantis & Atlantis High `Not Applicable`** |
| `LID Proxi & Configuration r421` | （見傾印）| Powernet `VehCfg7.VC_Trans_Equipped`；CUSW `Gear_Box_Type`；Atlantis & Atlantis High `Gear_Box_Type` |

**執行層不判何者為準**（T10b 明文）。二列全欄傾印見 §1。

### 3.2 ⚠ 存在性結果：`$VC_Trans_Equipped$` 六個候選**全不在**

| 訊號 | 在二 DBC 內者 |
|---|---|
| **`$Speedometer$`** | `STATUS_CCAN3.VehicleSpeedVSOSig`（**Atlantis／Atlantis High** 欄；`R4_BHCAN` `STATUS_CCAN3`(994)，13 bit、factor `0.0625`、offset `0`、單位 **`Km/h`**）<br>`BRAKE_FD_2.VehicleSpeedVSOSig`（**Atlantis High**；`R5_FDCAN8` `BRAKE_FD_2`(258)，同編碼） |
| **`$PresentGear$`** | `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT`（**Atlantis High**；`R5_FDCAN8`(263)，5 bit、factor `1`、offset `0`） |
| **`$VC_Trans_Equipped$`** | **無**（r420 三候選 ＋ r421 三候選，全部不在）|
| `$Country_Code$`（`Proxi & Configuration r43`）| **無** —— `Car_Configuration_16.Country_Code` 為 **PROXI 側**，非 CAN，**此為預期狀態，不登異常** |

**不在者 22 筆、非訊號名形態 4 筆**（後者如 `Not Applicable`、
`ECUCfg3.EC_AudTel1b-<DEST>`），二類**分開列**，見 §1。

> **`$VC_Trans_Equipped$` 之後果**：Q7 裁 Powernet 或 ATLANTIS 皆無解 ——
> 前者 `VehCfg7.*` 不在，後者逐字 `Not Applicable`。
> **這一項不是架構選擇能解的**，其施加路徑須另尋（PROXI？診斷？）或另登 DR。
> **本輪不提案** —— 量測到此為止。

### 3.3 `VAL_` 列舉（查得者，逐字）

見 §1 之末段。`VehicleSpeedVSOSig` 與 `GearEngagedForDisplay_PT` 於二 DBC
皆**無 `VAL_` 列舉**（前者為連續量、後者之檔位對照未以 `VAL_` 表示）。

---

## 4. T-登

| 項 | 結果 |
|---|---|
| **A-DD4** | 已登入 `ANOMALIES.md`，**§二 全文逐字**（`in` 比對相符）；另附本輪之遵行紀錄 |
| **DR-DD3** | 已建條目，狀態 **DRAFTED**；標的具名 `CIP Market Configuration Table v*.xlsx`，含指名來源之逐字與三項實測依據 |
| **DR-DD1** | 已加註「與 DR-DD3 為二個獨立阻斷，不可互抵」 |

### 4.1 ⚠ 誤一為何逃得過檢查 —— 值得記

`LID CAN Mapping r43` 之 `ACV_FailType`，其 Atlantis High 欄之
`STATUS_CLIMATE9.ACV_FailType`／`BCM_FD_26.ACV_FailType`
**在二 DBC 皆查得**（3 bit、factor 1）。

**即：若當初對 profile §3 之 `LID r43` 做「該訊號在不在 DBC」之檢查，
它會亮綠燈** —— 因為指錯的那一列，其訊號恰好存在。

**存在性檢查抓不到「指錯列」。** 能抓到它的只有
「回頭核對該列之 `Logical Identifier` 是否為所欲之名」——
而那正是本輪 T10d 所做的事。

### 4.2 A-DD4 之遵行

**本輪之寫入全在 `features/driver_distraction/` 私有路徑**
（`ANOMALIES.md`／`DATA_REQUESTS.md`／`docs/upstream/`／`scripts/`），
**未觸及 `docs/runtime/`、`docs/fw036/`、`forms/`、`scripts/`（repo 根）**
—— 故 §二 之三項拘束於本輪**無適用對象**，非「已遵行」而是「未觸發」。

已於 `ANOMALIES.md` 之 A-DD4 條目下如實記明，並記上一輪對
`docs/runtime/profiles/…` 之動作為 **`git add` 既有檔案、未改內容一字**。

---

## 4A. T11a–c —— Market Configuration Table

### 4A.1 T11a —— 綁定

```
forms/SR24 R1 Market Configuration Table v1.6.xlsx
file  : Microsoft Excel 2007+      magic : 504b030414000000
sha256: 7e865d557e42c8b00fbb92ed58ae4e94bb1d561c5fdf01c6af32a70821fe7dc9
bytes : 274,486
```

入 `feature.yaml` `reference.market_config`，**綁 `forms/` 之原件、
未複製入 `inputs/`**（同 R-DD5 之理），**sha256 自實體檔重算**。

**未入 `fingerprint.prompt_sources`** —— 其為**值域參照**，非生成語料。

### 4A.2 T11b —— 獨立重讀複核：**六欄值全數相符**

**未抄下放包之數字**：欄以**表頭字串**定位（非依其欄號）、
HK 之列以 `Destination Country` 全表搜（非依 r97）。

| 欄（Excel）| 表頭（逐字）| 實測值 | 下放包 §1.1 | 判 |
|---|---|---|---|---|
| **H** | `Destination Country` | `HONG KONG` | 同 | ✅ |
| **P** | `Region (Ref-only for FGA Default Regional Settings)` | `APAC` | 同 | ✅ |
| **Q** | `Value in <Dest> Signal - Hex` | `5B` | 同 | ✅ |
| **R** | `Value in <Dest> Signal - Decimal` | `91` | 同 | ✅ |
| **S** | `PROXI3 <Country_Code>Signal - Decimal` | **`91`** | 同 | ✅ |
| **BF** | `Navigation Driver Distraction Lockout Disabled (Y=Yes, N=No)` | `N` | 同 | ✅ |

#### (a) 欄號之表述差異 —— **不是錯**

下放包書 c8／c16／c17／c18／c19／c58；我書 c7／c15／c16／c17／c18／c57。
**逐欄以 Excel 欄名對照，二者指同一欄**（c7 = 第 8 欄 = `H`）——
**下放包為 1-based、本包為 0-based**。**同一欄，二種計數起點。**

> 記明以免日後被讀成「欄號不符」。**引用時宜書 Excel 欄名**（`H`／`S`／`BF`），
> 其無起點歧義 —— 同 §1.1 之「LID 須標分頁名」之理。

#### (b) 二個計數各差 1 —— **一次對上，成因為 `WORLD`**

| 量 | 下放包 | 我實測 |
|---|---|---|
| 具數值 `Country_Code` 之列 | 223 | **224** |
| `BF` 欄之 `N` | 58 | **59** |
| `BF` 欄之 `Y` | 165 | 165 ✅ |

**`r226 = WORLD`，其 `Country_Code = 0`、`BF = N`。**
排除該列後：**224−1 = 223、59−1 = 58** —— **二者同時對上**。

**即下放包之計數排除了 `WORLD`（非目的地國）。** 該排除合理，
惟**未於下放包書明** —— 記於此，使二組數字可對帳。

#### (c) 含 `HONG` 者實為二列，另一列是註腳

| 列 | 內容 |
|---|---|
| **r97** | `HONG KONG` —— 資料列 |
| r249 | `17 - For Hong Kong, Macau, and Taiwan R1L will use Language Set 3 and R1H will use Language Set 2.` —— **註腳文字落在 `Destination Country` 欄**，其餘五欄皆空 |

**下放包只提 r97，正確** —— r249 非資料列。
記明是因為**若以「含 HONG」搜列，會得到二列** —— 下一個人不必再判一次。

### 4A.3 T11c —— MACAU／TAIWAN／CHINA（**僅備查**）

| 列 | `Destination Country` | `Country_Code`（S）| Hex（Q）| Region（P）|
|---|---|---|---|---|
| r54 | `CHINA MAINLAND` | **16** | `10` | APAC |
| r125 | `MACAU` | **117** | `75` | APAC |
| r201 | `TAIWAN` | **190** | `BE` | APAC |

**本表僅備查，本輪不用於任何 TC。**

### 4A.4 ⚠ `BF` 欄（`c58`）之界線 —— 我未使用它

下放包 §1.2 記其分布並明文「**TC 不得引用該欄、不得以其為 Pre-Condition**，
亦不得以『HK=N 而 LATAM=Y』推論 A-DD1 之歸屬」。

**本輪之遵行**：
- 該欄之值**只出現於本節之對帳表**（因 §1.2 之計數需複核）
- **未寫入 `feature.yaml`、未寫入任何 TC、未用於任何推論**
- **A-DD1 之狀態未因本輪而改變** —— 仍待 DR-DD1

> 我複核了 LATAM 五國之 `BF` 皆為 `Y`（r16 Argentina 211／r36 Brazil 15／
> r53 Chile 45／r55 Colombia 47／r163 Peru 154）—— **該複核是為了對帳 §1.2
> 之計數，不是為了推論**。二者之別在於：對帳之後我沒有從它得出任何結論。

---

## 4B. T-登（下放包 06）

**DR-DD3 狀態改 `ANSWERED-PENDING-CONFIRM`**：標的已到位、值已查得（`91`），
**識別待 Q9**。條目內附六欄複核表與二分支處置
（Q9 = 是 → RESOLVED；否／不確定 → 值取 `91` 標 `[ASSUMPTION A-DD5]`，續開）。

**「與 DR-DD1 不可互抵」之註記維持**，並加一句：
**DR-DD3 之值到位不使 DR-DD1 得解**。

---

## 5. 獨立自評

### 5.1 我自己犯了一次抽取瑕疵，修掉了

初版 `collect_names()` 只以換行切多名。**實測 LID `CAN Mapping r1738`
之 Atlantis 欄以「空白 ＋ 單引號」串接二名**
（`STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.…FailSts`），
故被切成一個畸形字串，報出 **`STATUS_CCAN3.VehicleSpeedVSOSig …` 不在**。

**而 T9 已量到該名在 `R4_BHCAN` 內** —— 二次量測互相矛盾，
是這一點讓我回去看切法，而不是相信新的那次。

修正：另切單引號，並加 `NAME_RE` 把「不是訊號名形態」者
（`Not Applicable`、`0r` 之類殘片）**與真正之「查無」分開列** ——
**否則二者混在一起，讀表者會把工具的殘片當成上游的缺件。**

### 5.2 §3.2 那個結論我差點寫成建議

`$VC_Trans_Equipped$` 六個候選全不在，我第一個念頭是寫
「建議改由 PROXI 施加」。**沒寫** —— 那是提案，而本輪明文只量測。
**且我並未量測 PROXI 是否真有該參數**，寫了就是憑印象給方向。

### 5.3 T11b 我先定位再讀值，順序是刻意的

拘束要求「獨立重讀，不得抄下放包數字」。**若我按下放包給的 c8／c19 去讀，
讀到的會是別的欄**（0-based 之下 c8 是 `I`、c19 是 `T`）——
**然後值不符，我會報「複核不符」，而那是假的**。

先以**表頭字串**定位、再以 `Destination Country` **全表搜** HK 之列，
才使「值相符」與「欄號表述不同」二件事分得開。

### 5.4 `WORLD` 那一列我原本要寫成「下放包計數有誤」

二個計數各差 1，第一個念頭是報二筆不符。**先去找有沒有單一列能同時解釋二者**
—— `WORLD`（`Country_Code = 0`、`BF = N`）一列同時吃掉二個差。

**「差 1」與「排除了某一列」是兩種東西**，前者是錯，後者是判準差異。
不去找那一列，就會把後者報成前者。

### 5.5 r420／r421 我沒有比較

T10b 明文「何者為準由分析層裁」。二列傾印並列，**我連「r420 之
`Logical Identifier` 恰為 `VC_Trans_Equipped`」這件事都只陳述、不推論**
—— 那看起來像決定性證據，但 r421 之 Powernet 欄寫著
`VehCfg7.VC_Trans_Equipped`，同樣像。**兩個都像，就是該裁不該猜。**

---

## 6. 未結 DR

| DR | 狀態 | 阻斷範圍 |
|---|---|---|
| **DR-DD1** | DRAFTED（待發送）| `-025`~`-028` 凍結 |
| **DR-DD2** | DRAFTED（待發送）| 不阻斷；`$PARK_BRK_EGD$` 之名待定 |
| **DR-DD3** | DRAFTED（待發送）| `-017`~`-028` 之 `Country_Code` 值 |

**三筆皆未發送。DR-DD1 與 DR-DD3 不可互抵，須分別追。**

---

## 7. 量測條件揭露（R-G8）

- **架構帶自各分頁 r2 之合併標題列讀取**，非硬編猜測；欄名取 r3。
- **LID 之列號一律書 `LID {分頁名} r{n}`**（§1.1 拘束），本輪全文遵行。
- **存在性查核以 `BO_` 名 ＋ `SG_` 名雙鍵比對**；裸名者以 `SG_` 名全表比對。
  母體為 `R4_BHCAN` 155 訊息 ＋ `R5_FDCAN8` 323 訊息。
- **「不在」與「非訊號名形態」分開計**（22／4）——
  後者未查，**不得讀作查無**。
- **本輪只讀 LID 之二分頁**（`CAN Mapping`、`Proxi & Configuration`）。
  該檔另有 12 個 `* Specific Signals` 分頁（`Atlantis Low`／`M240`／
  `BSEGMENT`／`332BEV`／`M182BEV`／`250MCA`／`965`／`ALFAMCA`／`637MCA`／
  `356MCA` 等）**未掃** —— **若 `$VC_Trans_Equipped$` 另載於其中，本輪看不到**。
  此為 §3.2 之結論之已知邊界。
- **未量測 PROXI 是否含 `VC_Trans_Equipped`** —— 見 §5.2。
- **`VAL_` 之「無」為否定性判斷**，其母體為二 DBC 之全部 `VAL_` 行。
