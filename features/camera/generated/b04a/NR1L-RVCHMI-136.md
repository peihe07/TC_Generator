# NR1L-RVCHMI-136 — SWE1-RVC-112-03

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_29.2.2`（來源列 `NRL-188124`）

## test_item 上半（verbatim，SYS1 逐字）

> From this pop-up the user can: -Add/Remove as a favorite

## reasoning

§29.2.2 之第三項。驗法同 `-130`（兩向皆須可得，以標籤翻轉驗之）；分工亦同（有線 vs 無線之彈窗）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. The wireless camera is not currently a favorite
8. The individual AUX Cam settings pop-up for the wireless camera is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that "Make Favorite" is offered
2. Select "Make Favorite"
3. Read the pop-up and check that the control now reads "Remove as favorite"
```

## expected_result

```
1. "Make Favorite" is shown in the pop-up
2. "Make Favorite" registers the selection
3. The control reads "Remove as favorite"
```
