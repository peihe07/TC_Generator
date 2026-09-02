# Sys-RA-VF665_V43_VSM-464

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> WHEN TLM receives "IPC_VEHICLE_SETUP2.FSFCWPlusSetting " message THEN TLM updates the Forward Collision Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

## reasoning

驗證目標為非 NAFTA／LATAM 市場下 Setting2 顯示隨接收訊號更新。關鍵情境條件同 -459 但市場分支相反，起始 Off → 注入 2 (Brake)（Brake 為本分支獨有之選項，可同時區別於 -459）。本列只述一個接收→更新之因果，一條足夠。內部訊號 TLM_Vehicle_Setup_Menu.Info 之處置同 -459。

## TC 1 — FCW Setting2 display updated on reception of setting message

### test_item

```
WHEN TLM receives "IPC_VEHICLE_SETUP2.FSFCWPlusSetting " message THEN TLM updates the Forward Collision Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

(FCW Setting2 display updated on reception of setting message)
```

### pre_conditions

```
PROXI Country_Code = a country outside the NAFTA and LATAM markets (according to Market Configuration Table)
The menu item "Forward Collision Warning Setting2" is displayed and shows "Off"
```

### input_test_data

`NA`

### test_procedure

```
1. Send the signal $IPC_VEHICLE_SETUP2.FSFCWPlusSetting$ = 2 (Brake)
2. Read the menu item "Forward Collision Warning Setting2" and check that it shows "Brake"
```

### expected_result

```
1. The signal $IPC_VEHICLE_SETUP2.FSFCWPlusSetting$ = 2 (Brake) is registered without a bus error
2. The menu item "Forward Collision Warning Setting2" shows "Brake"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-464`
- design_method：功能測試 (Functional based ; no specific technique)｜priority：P1｜split_flag：False
