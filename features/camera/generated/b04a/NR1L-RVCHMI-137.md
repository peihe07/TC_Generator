# NR1L-RVCHMI-137 — SWE1-RVC-112-04

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.2.2`（來源列 `NRL-188124`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Delete the selected camera from the system altogether

## reasoning

§29.2.2 之第四項。`from the system altogether` 之可觀察結果為「清單中不再列出」。確認彈窗逐字取 **`PU0456`**（module `Aux Camera`；觸發欄逐字 `Displayed when user selects "Delete Camera"`），其按鈕欄為 `<X>`／`<Yes>`／`<Nol>`（末者為來源之拼寫，`Nol`）；ER 依文字欄之 `<Yes>  <No>` 書寫，拼寫差異記於 `remarks`。**本項只見於無線側** —— §29.1.2（有線）之四項無 Delete，與 §34.9.3 之 `Note: Wired AUX cameras Cannot be deleted` 一致（該列屬 B04b）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. The individual AUX Cam settings pop-up for the wireless camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that "Delete Camera" is offered
2. Select "Delete Camera"
3. Read the confirmation pop-up text on the HU display
4. Select <Yes> on the confirmation pop-up
5. Read the Aux Cameras settings menu and check that the camera is no longer listed
```

## expected_result

```
1. "Delete Camera" is shown in the pop-up
2. "Delete Camera" registers the selection
3. The confirmation pop-up reads "Are you sure you want to delete [Insert Camera Name] from Uconnect?" with <Yes> and <No> (PU0456)
4. The <Yes> button registers the selection
5. The camera is no longer listed in the Aux Cameras settings menu
```

## remarks

Popup PU0456 button column spells the second option "Nol"; its message text reads "<Yes>  <No>". ER follows the message text.
