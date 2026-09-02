# Sys-RA-VF665_V43_VSM-449

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Side Distance Warning
- **spec_section**：`1.11.1.1.5`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.5 para 559, which names the Side Distance Warning "Setting" and "Chime Volume" menu items; HMI Settings List `Settings` r315B carries "Side Distance Warning" (Technical Reference VF230/665) and r316B "Side Distance Warning Volume" with options "Low / Medium / High " (Technical Reference CFTS019)

## test_item 上半（verbatim，SYSRA Description）

> IF the user sets "Sdw_Chime_Volume_Setting.Req" internal signals to "Medium" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req" B-CAN signal equal to "Medium" and sends this signal to IPC

## reasoning

驗證目標為使用者於 Chime Volume 選定該音量後，TLM 送出 TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req 之對應值。關鍵情境條件為 PROXI 為 Present 且子選單項可達；Sdw_Chime_Volume_Setting.Req 為內部訊號，其驅動面為規格 para 559 具名之 "Chime Volume" 子項，並有 HMI Settings List r316B 「Side Distance Warning Volume」（選項 Low / Medium / High ）為錨（R-VL21(a)）。本列只述單一音量，一條足夠；Low 與 High 為值域兩端故用 BVA、Medium 用 EP。ER 用 is received 式（DUT 送出，R-VL21(e)）。

## TC 1 — Side distance warning chime volume request sent for medium selection

### test_item

```
IF the user sets "Sdw_Chime_Volume_Setting.Req" internal signals to "Medium" THEN TLM shall set "TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req" B-CAN signal equal to "Medium" and sends this signal to IPC

(Side distance warning chime volume request sent for medium selection)
```

### pre_conditions

```
PROXI Side_Distance_Warning = Present
The menu item "Chime Volume" under "Side Distance Warning" is displayed and reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Select "Chime Volume" = "Medium" on the TLM display
2. Read the signal $TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req$ and check that it is 1 (Medium)
```

### expected_result

```
1. The menu item "Chime Volume" shows "Medium"
2. The signal value $TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req$ = 1 (Medium) is received
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.5
Sys-RA-VF665_V43_VSM-449`
- design_method：等價劃分 (Equivalence Partitioning, EP)｜priority：P1｜split_flag：False｜distinguishing_axis：Chime Volume option = Medium
