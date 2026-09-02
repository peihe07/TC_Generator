# Sys-RA-VF665_V43_VSM-467

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Forward Collision Warning
- **spec_section**：`1.11.1.1.6`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.6 (paras 580, 584, 601, 617); HMI Settings List `Settings` r9/r255 carries "Forward Collision Sensitivity*" with Technical Reference VF230/665 and options "Near , Med, Far", matching the spec values

## test_item 上半（verbatim，SYSRA Description）

> IF the user sets "FSCWPlus_Activation_Mode_Setting.Req" internal signals to "Med" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req " B-CAN signal equal to "Med" and sends this signal to IPC

## reasoning

驗證目標為使用者選定靈敏度後，TLM 送出 TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req 之對應值。關鍵情境條件為 Forward_Collision_Mitigation 組態成立且靈敏度選單項可達；設定動作走 UI 路徑（R-P375(b)），FSCWPlus_Activation_Mode_Setting.Req 之驅動面為規格 para 617 具名之選單項，並有 HMI Settings List r9／r255「Forward Collision Sensitivity*」（TR VF230/665、選項 Near , Med, Far）為錨（R-VL21(a)）。本列只述單一等級，一條足夠；Near 與 Far 為值域兩端故用 BVA、Med 用 EP。ER 用 is received 式（DUT 送出，R-VL21(e)）。

## TC 1 — FCW sensitivity request sent for med selection

### test_item

```
IF the user sets "FSCWPlus_Activation_Mode_Setting.Req" internal signals to "Med" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req " B-CAN signal equal to "Med" and sends this signal to IPC

(FCW sensitivity request sent for med selection)
```

### pre_conditions

```
PROXI Forward_Collision_Mitigation = Full Speed Forward Collision Warning with Mitigation
The menu item "Forward Collision Warning Sensitivity" is displayed and reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Select "Forward Collision Warning Sensitivity" = "Med" on the TLM display
2. Read the signal $TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req$ and check that it is 1 (Med)
```

### expected_result

```
1. The menu item "Forward Collision Warning Sensitivity" shows "Med"
2. The signal value $TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req$ = 1 (Med) is received
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.6
Sys-RA-VF665_V43_VSM-467`
- design_method：等價劃分 (Equivalence Partitioning, EP)｜priority：P1｜split_flag：False｜distinguishing_axis：sensitivity = Med
