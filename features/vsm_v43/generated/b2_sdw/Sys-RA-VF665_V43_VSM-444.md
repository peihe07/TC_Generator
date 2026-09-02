# Sys-RA-VF665_V43_VSM-444

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Side Distance Warning
- **spec_section**：`1.11.1.1.5`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.5 para 559, which names the Side Distance Warning "Setting" and "Chime Volume" menu items; HMI Settings List `Settings` r315B carries "Side Distance Warning" (Technical Reference VF230/665) and r316B "Side Distance Warning Volume" with options "Low / Medium / High " (Technical Reference CFTS019)

## test_item 上半（verbatim，SYSRA Description）

> IF the user sets "Sdw_Setting.Req" internal signals to "Sound" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.Sdw_Req" B-CAN signal equal to "Sound" and sends this signal to IPC

## reasoning

驗證目標為使用者於 Setting 選定該選項後，TLM 送出 TELEMATIC_VEHICLE_SETUP.Sdw_Req 之對應值。關鍵情境條件為 PROXI Side_Distance_Warning = Present 且子選單項可達；設定動作走 UI 路徑（R-P375(b)），因 Sdw_Setting.Req 為內部訊號而其驅動面即規格 para 559 具名之 "Setting" 子項（R-VL21(a)）。本列只述單一選項，一條足夠；同族其餘選項由各自之列涵蓋（§8.2.1）。ER 用 is received 式（DUT 送出，R-VL21(e)）；raw 與 label 逐字取 val_tables_v43.tsv。

## TC 1 — Side distance warning request sent for sound selection

### test_item

```
IF the user sets "Sdw_Setting.Req" internal signals to "Sound" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.Sdw_Req" B-CAN signal equal to "Sound" and sends this signal to IPC

(Side distance warning request sent for sound selection)
```

### pre_conditions

```
PROXI Side_Distance_Warning = Present
The menu item "Setting" under "Side Distance Warning" is displayed and reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Select "Setting" = "Sound" on the TLM display
2. Read the signal $TELEMATIC_VEHICLE_SETUP.Sdw_Req$ and check that it is 1 (Sound)
```

### expected_result

```
1. The menu item "Setting" shows "Sound"
2. The signal value $TELEMATIC_VEHICLE_SETUP.Sdw_Req$ = 1 (Sound) is received
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.5
Sys-RA-VF665_V43_VSM-444`
- design_method：等價劃分 (Equivalence Partitioning, EP)｜priority：P1｜split_flag：False｜distinguishing_axis：Setting option = Sound
