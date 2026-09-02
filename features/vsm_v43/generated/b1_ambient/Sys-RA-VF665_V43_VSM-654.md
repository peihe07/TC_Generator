# Sys-RA-VF665_V43_VSM-654

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Interior Ambient Lighting
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); raw 2 = VAL_ Level_3 per data/val_tables_v43.tsv

## test_item 上半（verbatim，SYSRA Description）

> IF the user sets "Ambient_Lighting_level_Setting.Req" equal to "Level_3 " THEN TLM shal set "TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req" B-CAN signal equal to "Level_ 3 " and sends this signal to IPC

## reasoning

驗證目標為使用者於 TLM 選定 Level_3 後，TLM 送出 TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req 之對應值。關鍵情境條件為兩個 PROXI 皆成立且選單項可達；設定動作走 UI 路徑（R-P375(b)），因為 Ambient_Lighting_level_Setting.Req 為內部訊號、其驅動面即規格具名之選單項（R-VL21(a)），非臆造亦無須 PENDING。本列只述單一等級之對應關係，一條即足；其餘六級由 -652〜-658 之各列分別涵蓋（§8.2.1）。ER 用 is received 式而非 bus-error 式，因送出方為 DUT（TLM）而非測試員（R-VL21(e)）。

## TC 1 — Ambient lighting level 3 request sent on user selection

### test_item

```
IF the user sets "Ambient_Lighting_level_Setting.Req" equal to "Level_3 " THEN TLM shal set "TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req" B-CAN signal equal to "Level_ 3 " and sends this signal to IPC

(Ambient lighting level 3 request sent on user selection)
```

### pre_conditions

```
PROXI Ambient_Lighting_Function = Present
PROXI Ambient_Dimmer_Switch = absent
The menu item "Interior Ambient Lights Level" is displayed and reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Select "Interior Ambient Lights Level" = "Level_3" on the TLM display
2. Read the signal $TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req$ and check that it is 2 (Level_3)
```

### expected_result

```
1. The menu item "Interior Ambient Lights Level" shows "Level_3"
2. The signal value $TELEMATIC_VEHICLE_SETUP.AmbientLightingLevel_Req$ = 2 (Level_3) is received
```

- specification_reference：`Sys-RA-VF665_V43_VSM-654`
- design_method：等價劃分 (Equivalence Partitioning, EP)｜priority：P2｜split_flag：False｜distinguishing_axis：selected ambient lighting level = Level_3
