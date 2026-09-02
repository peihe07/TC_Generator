# Sys-RA-VF665_V43_VSM-661

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Interior Ambient Lighting
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); ELSE branch; the two negative cases are read from the -651 conjunction, not added scope - see section K

## test_item 上半（verbatim，SYSRA Description）

> THEN TLM shall not display the Ambient Light Level menu item and the user can not perform any setting.

## reasoning

驗證目標為 -651 之條件不成立時，Interior Ambient Lights Level 選單項不顯示且無法設定。關鍵情境條件為 ELSE 分支，即 (Function = Present AND Dimmer = absent) 之否定。切分依據為 §8.2.2：該合取式之兩個條件可各自獨立不成立，兩種失敗情境互不涵蓋，故出兩條，各驗一個否定支；此為對 -651 之負向配對（§7）。規格之 ELSE 未逐一列舉否定支，兩支係由 -651 之合取條件依德摩根律讀出，非新增情境；若上游認為應合為一條，已列 §K 交裁。

## TC 1 — Ambient Lights Level menu hidden when function absent

### test_item

```
THEN TLM shall not display the Ambient Light Level menu item and the user can not perform any setting.

(Ambient Lights Level menu hidden when function absent)
```

### pre_conditions

```
PROXI Ambient_Lighting_Function = absent
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Read the menu list and check that "Interior Ambient Lights Level" is absent
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Interior Ambient Lights Level" is not displayed in the menu list
```

- specification_reference：`Sys-RA-VF665_V43_VSM-661`
- design_method：負向測試 (Negative / Invalid)｜priority：P2｜split_flag：True｜split_reason：ELSE branch of the -651 conjunction; the two PROXI conditions fail independently (IN 8.2.2)｜distinguishing_axis：Ambient_Lighting_Function = absent

## TC 2 — Ambient Lights Level menu hidden when dimmer switch present

### test_item

```
THEN TLM shall not display the Ambient Light Level menu item and the user can not perform any setting.

(Ambient Lights Level menu hidden when dimmer switch present)
```

### pre_conditions

```
PROXI Ambient_Lighting_Function = Present
PROXI Ambient_Dimmer_Switch = Present
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Read the menu list and check that "Interior Ambient Lights Level" is absent
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Interior Ambient Lights Level" is not displayed in the menu list
```

- specification_reference：`Sys-RA-VF665_V43_VSM-661`
- design_method：負向測試 (Negative / Invalid)｜priority：P2｜split_flag：True｜split_reason：ELSE branch of the -651 conjunction; the two PROXI conditions fail independently (IN 8.2.2)｜distinguishing_axis：Ambient_Dimmer_Switch = Present
