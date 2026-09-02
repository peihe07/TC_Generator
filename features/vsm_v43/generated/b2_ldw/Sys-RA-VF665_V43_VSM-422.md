# Sys-RA-VF665_V43_VSM-422

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Lane Departure Warning
- **spec_section**：`1.11.1.1.3`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.3 paras 502 and 515, including the spec spellings "Lanse Sense" and the PROXI value "Leve 3"/"Leve 2" (R-6/R-13, filed to DR-VT2); HMI Settings List `Settings` r288B carries "Lane Departure Warning Sensitivity" (Technical Reference VF230/665, options "Early / Late")

## test_item 上半（verbatim，SYSRA Description）

> IF the user sets "LDW_Sensibility_Setting.Req" internal signals to "Late" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.LDW_Sensibility_Req" B-CAN signal equal to "Late" and sends this signal to IPC

## reasoning

驗證目標為使用者選定該選項後，TLM 送出對應 B-CAN 訊號之值。關鍵情境條件為該 PROXI 等級成立且選單項可達；設定動作走 UI 路徑（R-P375(b)），因 LDW_Sensibility_Setting.Req／LDW_Intensity_Setting.Req 為內部訊號，其驅動面即規格具名之選單項（R-VL21(a)）。本列只述單一選項，一條足夠；同族其餘選項由各自之列涵蓋（§8.2.1）。ER 用 is received 式（DUT 送出，R-VL21(e)）；raw 與 label 逐字取 val_tables_v43.tsv。

## TC 1 — Lanse Sense Warning 1 request sent for late selection

### test_item

```
IF the user sets "LDW_Sensibility_Setting.Req" internal signals to "Late" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP2.LDW_Sensibility_Req" B-CAN signal equal to "Late" and sends this signal to IPC

(Lanse Sense Warning 1 request sent for late selection)
```

### pre_conditions

```
PROXI Half_Torque_Sensibility = Leve 3
The menu item "Lanse Sense Warning 1" is displayed and reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Select "Lanse Sense Warning 1" = "Late" on the TLM display
2. Read the signal $TELEMATIC_VEHICLE_SETUP2.LDW_Sensibility_Req$ and check that it is 2 (Late)
```

### expected_result

```
1. The menu item "Lanse Sense Warning 1" shows "Late"
2. The signal value $TELEMATIC_VEHICLE_SETUP2.LDW_Sensibility_Req$ = 2 (Late) is received
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.3
Sys-RA-VF665_V43_VSM-422`
- design_method：邊界值分析 (Boundary Value Analysis, BVA)｜priority：P1｜split_flag：False｜distinguishing_axis：Warning 1 option = Late
