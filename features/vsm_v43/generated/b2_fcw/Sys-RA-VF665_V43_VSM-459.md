# Sys-RA-VF665_V43_VSM-459

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> WHEN TLM receives "IPC_VEHICLE_SETUP2.FSFCWPlusSetting " message THEN TLM updates the Forward Collision Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

## reasoning

驗證目標為 TLM 收到 IPC_VEHICLE_SETUP2.FSFCWPlusSetting 後其 Setting1 顯示隨之更新。關鍵情境條件為 NAFTA／LATAM 市場、選單項可見，且起始值與注入值相異（Off → Audio）以使更新可觀察。本列只述一個接收→更新之因果，一條足夠；注入值取 VAL_ 實值 1 (Audio) 為測試設計自由度（R-VL21(d)）。TLM_Vehicle_Setup_Menu.Info 為內部訊號不可讀，其效果面即規格同句所載之顯示更新，ER 觀察具名選單項（R-P353 白名單 (ii)）。

## TC 1 — FCW Setting1 display updated on reception of setting message

### test_item

```
WHEN TLM receives "IPC_VEHICLE_SETUP2.FSFCWPlusSetting " message THEN TLM updates the Forward Collision Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

(FCW Setting1 display updated on reception of setting message)
```

### pre_conditions

```
PROXI Country_Code = a country of NAFTA or LATAM market (according to Market Configuration Table)
The menu item "Forward Collision Warning Setting1" is displayed and shows "Off"
```

### input_test_data

`NA`

### test_procedure

```
1. Send the signal $IPC_VEHICLE_SETUP2.FSFCWPlusSetting$ = 1 (Audio)
2. Read the menu item "Forward Collision Warning Setting1" and check that it shows "Audio"
```

### expected_result

```
1. The signal $IPC_VEHICLE_SETUP2.FSFCWPlusSetting$ = 1 (Audio) is registered without a bus error
2. The menu item "Forward Collision Warning Setting1" shows "Audio"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-459`
- design_method：功能測試 (Functional based ; no specific technique)｜priority：P1｜split_flag：False
