# Sys-RA-VF665_V43_VSM-460

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> IF "Country_Code"PROXI parameter is not equal to a country of NAFTA/LATAM market (according to Market Configuration Table) THEN TLM shall display the " Forward Collision Warning Setting2" menu item and the user can perform setting with the following options: Off, Brake, Audio_Brake

## reasoning

驗證目標為非 NAFTA／LATAM 市場下 Setting2 選單項顯示且提供三個指定選項。關鍵情境條件為 Country_Code 不屬該市場，為 -455 之對立支（決策表）。本列與 -455 之選項集合不同（Brake 取代 Audio），故非重複；一條足夠。選項值逐字取規格 para 603；送出行為由 -461〜-463 涵蓋（§8.2.1）。

## TC 1 — FCW Setting2 offers three options outside NAFTA and LATAM markets

### test_item

```
IF "Country_Code"PROXI parameter is not equal to a country of NAFTA/LATAM market (according to Market Configuration Table) THEN TLM shall display the " Forward Collision Warning Setting2" menu item and the user can perform setting with the following options: Off, Brake, Audio_Brake

(FCW Setting2 offers three options outside NAFTA and LATAM markets)
```

### pre_conditions

```
PROXI Forward_Collision_Mitigation = Full Speed Forward Collision Warning with Mitigation
PROXI Country_Code = a country outside the NAFTA and LATAM markets (according to Market Configuration Table)
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Read the menu list and check that "Forward Collision Warning Setting2" is present
3. Read the options offered by "Forward Collision Warning Setting2" and check that they are "Off", "Brake" and "Audio_Brake"
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Forward Collision Warning Setting2" is displayed in the menu list
3. The menu item "Forward Collision Warning Setting2" offers exactly the options "Off", "Brake" and "Audio_Brake"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-460`
- design_method：決策表 (Decision Table Testing)｜priority：P1｜split_flag：False｜distinguishing_axis：Country_Code outside NAFTA/LATAM
