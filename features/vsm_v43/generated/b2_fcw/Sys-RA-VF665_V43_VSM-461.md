# Sys-RA-VF665_V43_VSM-461

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> IF the user sets "FSCWPlus_Setting.Req" internal signals to "Off " THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req" B-CAN signal equal to "Off " and sends this signal to IPC

## reasoning

驗證目標為使用者於 Setting2 選定該選項後，TLM 送出 TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req 之對應值。關鍵情境條件為 Country_Code 屬 非 NAFTA／LATAM 市場且選單項可達；設定動作走 UI 路徑（R-P375(b)），因 FSCWPlus_Setting.Req 為內部訊號而其驅動面即規格 para 584／601 具名之選單項（R-VL21(a)）。本列只述單一選項之對應關係，一條足夠；同族其餘選項由各自之列涵蓋（§8.2.1）。ER 用 is received 式而非 bus-error 式，因送出方為 DUT（R-VL21(e)）；raw 值逐字取 val_tables_v43.tsv。

## TC 1 — FCW Setting2 request sent for off selection

### test_item

```
IF the user sets "FSCWPlus_Setting.Req" internal signals to "Off " THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req" B-CAN signal equal to "Off " and sends this signal to IPC

(FCW Setting2 request sent for off selection)
```

### pre_conditions

```
PROXI Country_Code = a country outside the NAFTA and LATAM markets (according to Market Configuration Table)
The menu item "Forward Collision Warning Setting2" is displayed and reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Select "Forward Collision Warning Setting2" = "Off" on the TLM display
2. Read the signal $TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req$ and check that it is 0 (Off)
```

### expected_result

```
1. The menu item "Forward Collision Warning Setting2" shows "Off"
2. The signal value $TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req$ = 0 (Off) is received
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-461`
- design_method：等價劃分 (Equivalence Partitioning, EP)｜priority：P1｜split_flag：False｜distinguishing_axis：Setting2 option = Off
