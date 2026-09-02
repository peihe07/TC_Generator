# Sys-RA-VF665_V43_VSM-434

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Lane Departure Warning
- **spec_section**：`1.11.1.1.4`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.4 paras 531 and 541, including the spec spellings "Lanse Sense Strenght" and the PROXI value "Leve 3"/"Leve 2" (R-6/R-13, filed to DR-VT2); HMI Settings List `Settings` r282B carries "Lane Departure Warning" (Technical Reference VF230/VF665, CFTS022)

## test_item 上半（verbatim，SYSRA Description）

> IF "Half_HMI_Setting" PROXI parameter is equal to "Leve 2" THEN TLM shall display the " Lanse Sense Strenght 2" menu item and the user can perform setting with the following options: Low, Med, High

## reasoning

驗證目標為該 PROXI 等級成立時，對應之選單項顯示且提供規格所列之選項集合。關鍵情境條件為 Half_Torque_Sensibility／Half_HMI_Setting 之值（入 Pre-Condition，R-P375(b)）；本列一觸發二同時結果（顯示＋選項集合），依 §5.7 屬同一 TC，一條足夠。選單項名與選項值逐字取規格（含其拼字瑕疵 Lanse／Strenght／Leve，R-6／R-13 保留）；各選項之送出行為由同族之列涵蓋（§8.2.1）。

## TC 1 — Lanse Sense Strenght 2 menu offers 3 options at half level 2

### test_item

```
IF "Half_HMI_Setting" PROXI parameter is equal to "Leve 2" THEN TLM shall display the " Lanse Sense Strenght 2" menu item and the user can perform setting with the following options: Low, Med, High

(Lanse Sense Strenght 2 menu offers 3 options at half level 2)
```

### pre_conditions

```
PROXI Half_HMI_Setting = Leve 2
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Read the menu list and check that "Lanse Sense Strenght 2" is present
3. Read the options offered by "Lanse Sense Strenght 2" and check that they are "Low", "Med", "High"
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Lanse Sense Strenght 2" is displayed in the menu list
3. The menu item "Lanse Sense Strenght 2" offers exactly the options "Low", "Med", "High"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.4
Sys-RA-VF665_V43_VSM-434`
- design_method：決策表 (Decision Table Testing)｜priority：P1｜split_flag：False｜distinguishing_axis：Half_HMI_Setting = Leve 2
