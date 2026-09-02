# Sys-RA-VF665_V43_VSM-455

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> IF "Country_Code" PROXI parameter is equal to a country of NAFTA or LATAM market (according to Market Configuration Table) THEN TLM shall display the " Forward Collision Warning Setting1" menu item and the user can perform setting with the following options: Off, Audio, Audio_Brake

## reasoning

驗證目標為 NAFTA／LATAM 市場下 Setting1 選單項顯示且提供三個指定選項。關鍵情境條件為 Country_Code 屬該市場（依 Market Configuration Table），與 -460 之非該市場互為決策表之兩支。本列同時規定「顯示」與「選項集合」兩個可觀察結果，屬同一觸發，一條足夠（§5.7）。選項值逐字取規格 para 586；各選項之送出行為由 -456〜-458 分別涵蓋（§8.2.1）。

## TC 1 — FCW Setting1 offers three options in NAFTA and LATAM markets

### test_item

```
IF "Country_Code" PROXI parameter is equal to a country of NAFTA or LATAM market (according to Market Configuration Table) THEN TLM shall display the " Forward Collision Warning Setting1" menu item and the user can perform setting with the following options: Off, Audio, Audio_Brake

(FCW Setting1 offers three options in NAFTA and LATAM markets)
```

### pre_conditions

```
PROXI Forward_Collision_Mitigation = Full Speed Forward Collision Warning with Mitigation
PROXI Country_Code = a country of NAFTA or LATAM market (according to Market Configuration Table)
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Read the menu list and check that "Forward Collision Warning Setting1" is present
3. Read the options offered by "Forward Collision Warning Setting1" and check that they are "Off", "Audio" and "Audio_Brake"
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Forward Collision Warning Setting1" is displayed in the menu list
3. The menu item "Forward Collision Warning Setting1" offers exactly the options "Off", "Audio" and "Audio_Brake"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-455`
- design_method：決策表 (Decision Table Testing)｜priority：P1｜split_flag：False｜distinguishing_axis：Country_Code in NAFTA/LATAM
