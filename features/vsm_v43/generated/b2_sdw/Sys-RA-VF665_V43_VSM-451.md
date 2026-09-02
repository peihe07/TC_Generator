# Sys-RA-VF665_V43_VSM-451

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Side Distance Warning
- **spec_section**：`1.11.1.1.5`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.5 para 559, which names the Side Distance Warning "Setting" and "Chime Volume" menu items; HMI Settings List `Settings` r315B carries "Side Distance Warning" (Technical Reference VF230/665) and r316B "Side Distance Warning Volume" with options "Low / Medium / High " (Technical Reference CFTS019)

## test_item 上半（verbatim，SYSRA Description）

> WHEN TLM receives "IPC_VEHICLE_SETUP.SdwChimeVolume" message THEN TLM updates the Side Distance Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

## reasoning

驗證目標為 TLM 收到 IPC_VEHICLE_SETUP.SdwChimeVolume 後，其 Chime Volume 顯示隨之更新。關鍵情境條件同 -446 但收訊弧不同，起始 Low → 注入 2 (High) 取值域兩端使更新最可觀察。本列與 -446 分列不併：訊號、選單項、值域三者皆不同（§8.2.1）。內部訊號與 ER 式之處置同 -446。

## TC 1 — Side distance warning display updated on reception of chime volume message

### test_item

```
WHEN TLM receives "IPC_VEHICLE_SETUP.SdwChimeVolume" message THEN TLM updates the Side Distance Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

(Side distance warning display updated on reception of chime volume message)
```

### pre_conditions

```
PROXI Side_Distance_Warning = Present
The menu item "Chime Volume" under "Side Distance Warning" is displayed and shows "Low"
```

### input_test_data

`NA`

### test_procedure

```
1. Send the signal $IPC_VEHICLE_SETUP.SdwChimeVolume$ = 2 (High)
2. Read the menu item "Chime Volume" and check that it shows "High"
```

### expected_result

```
1. The signal $IPC_VEHICLE_SETUP.SdwChimeVolume$ = 2 (High) is registered without a bus error
2. The menu item "Chime Volume" shows "High"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.5
Sys-RA-VF665_V43_VSM-451`
- design_method：功能測試 (Functional based ; no specific technique)｜priority：P1｜split_flag：False｜distinguishing_axis：reception arc = SdwChimeVolume
