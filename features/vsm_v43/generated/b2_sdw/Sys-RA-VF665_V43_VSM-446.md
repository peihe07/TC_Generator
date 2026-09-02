# Sys-RA-VF665_V43_VSM-446

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Side Distance Warning
- **spec_section**：`1.11.1.1.5`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.5 para 559, which names the Side Distance Warning "Setting" and "Chime Volume" menu items; HMI Settings List `Settings` r315B carries "Side Distance Warning" (Technical Reference VF230/665) and r316B "Side Distance Warning Volume" with options "Low / Medium / High " (Technical Reference CFTS019)

## test_item 上半（verbatim，SYSRA Description）

> WHEN TLM receives "IPC_VEHICLE_SETUP.Sdw" message THEN TLM updates the Side Distance Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

## reasoning

驗證目標為 TLM 收到 IPC_VEHICLE_SETUP.Sdw 後，其 Setting 顯示隨之更新。關鍵情境條件為組態 Present、選單項可見，且起始 Off 與注入 1 (Sound) 相異以使更新可觀察。本列與 -451 為兩條獨立收訊弧（Sdw 對 SdwChimeVolume），依 13 包 §二-2 分列不併（§8.2.1）。TLM_Vehicle_Setup_Menu.Info 為內部訊號不可讀，效果面即規格同句所載之顯示更新（R-P353 白名單 (ii)）；步驟 1 為測試員送出故 ER 用 bus-error 確認式（R-VL21(e)）。

## TC 1 — Side distance warning display updated on reception of setting message

### test_item

```
WHEN TLM receives "IPC_VEHICLE_SETUP.Sdw" message THEN TLM updates the Side Distance Warning information on its display through "TLM_Vehicle_Setup_Menu.Info" internal signal

(Side distance warning display updated on reception of setting message)
```

### pre_conditions

```
PROXI Side_Distance_Warning = Present
The menu item "Setting" under "Side Distance Warning" is displayed and shows "Off"
```

### input_test_data

`NA`

### test_procedure

```
1. Send the signal $IPC_VEHICLE_SETUP.Sdw$ = 1 (Sound)
2. Read the menu item "Setting" and check that it shows "Sound"
```

### expected_result

```
1. The signal $IPC_VEHICLE_SETUP.Sdw$ = 1 (Sound) is registered without a bus error
2. The menu item "Setting" shows "Sound"
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.5
Sys-RA-VF665_V43_VSM-446`
- design_method：功能測試 (Functional based ; no specific technique)｜priority：P1｜split_flag：False｜distinguishing_axis：reception arc = Sdw
