# Sys-RA-VF665_V43_VSM-453

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); spec spells "Warinig"; test_item upper half keeps it verbatim (R-6/R-13), filed to DR-VT2; UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> IF "Forward_Collision_Mitigation" PROXI parameter is equal to "Full Speed Forward Collision Warning with Mitigation" THEN TLM shall display the "Forward Collision Warinig Setting" and "Forward Collision Warning Sensitivity" menu item and the user can perform setting.

## reasoning

驗證目標為 Forward_Collision_Mitigation 組態成立時，兩個 FCW 選單項同時顯示且可設定。關鍵情境條件為該 PROXI 參數等於「Full Speed Forward Collision Warning with Mitigation」，入 Pre-Condition（R-P375(b)）。本列一觸發二同時結果，依 §5.7 屬同一 TC，多階段 ER 涵蓋兩個選單項，故一條足夠。選單項名逐字取規格 para 580（含其拼字瑕疵 Warinig，R-6／R-13 保留），各選項之訊號效果由 -455〜-469 涵蓋（§8.2.1）。

## TC 1 — FCW setting and sensitivity menus shown when mitigation configured

### test_item

```
IF "Forward_Collision_Mitigation" PROXI parameter is equal to "Full Speed Forward Collision Warning with Mitigation" THEN TLM shall display the "Forward Collision Warinig Setting" and "Forward Collision Warning Sensitivity" menu item and the user can perform setting.

(FCW setting and sensitivity menus shown when mitigation configured)
```

### pre_conditions

```
PROXI Forward_Collision_Mitigation = Full Speed Forward Collision Warning with Mitigation
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Read the menu list and check that "Forward Collision Warinig Setting" is present
3. Read the menu list and check that "Forward Collision Warning Sensitivity" is present
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Forward Collision Warinig Setting" is displayed in the menu list
3. The menu item "Forward Collision Warning Sensitivity" is displayed in the menu list
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-453`
- design_method：決策表 (Decision Table Testing)｜priority：P1｜split_flag：False
