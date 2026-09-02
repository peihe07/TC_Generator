# Sys-RA-VF665_V43_VSM-441

- **Test Group**：Vehicle Setup Management R1L TBM
- **Test Set**：Side Distance Warning
- **spec_section**：`1.11.1.1.5`（來源 segment_map）
- **Remarks**：Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1); UI names taken verbatim from spec 1.11.1.1.5 para 559, which names the Side Distance Warning "Setting" and "Chime Volume" menu items; HMI Settings List `Settings` r315B carries "Side Distance Warning" (Technical Reference VF230/665) and r316B "Side Distance Warning Volume" with options "Low / Medium / High " (Technical Reference CFTS019)

## test_item 上半（verbatim，SYSRA Description）

> IF "Side_Distance_Warning" PROXI parameter is equal to "Present" THEN TLM shall display the Side Distance Warning "Setting" and "Chime Volume" menu items and the user can perform setting.

## reasoning

驗證目標為組態為 Present 時，Setting 與 Chime Volume 兩個子選單項同時顯示且可設定。關鍵情境條件為 PROXI 參數等於 Present；本列一觸發二同時結果，依 §5.7 屬同一 TC，多階段 ER 涵蓋兩項。兩子項之個別設定行為分由 -443〜-445 與 -448〜-450 涵蓋（§8.2.1 委任）。子項名 "Setting"／"Chime Volume" 逐字取規格 para 559，父選單名以 HMI r315B 為錨。

## TC 1 — Side Distance Warning setting and chime volume menus shown when present

### test_item

```
IF "Side_Distance_Warning" PROXI parameter is equal to "Present" THEN TLM shall display the Side Distance Warning "Setting" and "Chime Volume" menu items and the user can perform setting.

(Side Distance Warning setting and chime volume menus shown when present)
```

### pre_conditions

```
PROXI Side_Distance_Warning = Present
The TLM is powered on and the vehicle setup menu is reachable
```

### input_test_data

`NA`

### test_procedure

```
1. Open the vehicle setup menu on the TLM display
2. Open "Side Distance Warning" and read the menu list
3. Check that "Setting" and "Chime Volume" are present
```

### expected_result

```
1. The vehicle setup menu is displayed
2. The menu item "Side Distance Warning" is displayed and opens
3. The menu items "Setting" and "Chime Volume" are displayed in the menu list
```

- specification_reference：`Vehicle_Setup_Management_by_VP-LTM_R1L_TBM_VF665_V43_R4_1.11.1.1.5
Sys-RA-VF665_V43_VSM-441`
- design_method：決策表 (Decision Table Testing)｜priority：P1｜split_flag：False｜distinguishing_axis：Side_Distance_Warning = Present
