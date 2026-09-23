# NR1L-RVCHMI-071 — SWE1-RVC-081

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.5.2`（來源列 `NRL-188074`）

## test_item 上半（verbatim，SYS1 逐字）

> When a wireless aux camera is selected from any location, if the ‘Enable wireless cameras’ setting is OFF but no wireless projection session is active, the setting is automatically enabled.

## reasoning

§27.5.2 逐字。與 `-072`（§27.6.1，有投影 → 彈窗後才啟用）成一對：本列為**無投影**之靜默啟用分支。與 `-067`（§27.4.3）之分工：後者由**使用者直接操作該設定**觸發，本列由**選取無線相機**間接觸發；兩者之來源節與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. No wireless projection session is active
7. A wireless AUX camera is within range and powered on
```

## input_test_data

`NA`

## test_procedure

```
1. Select the wireless AUX camera entry from the Aux Cameras list
2. Read the HU display and check that no pop-up is displayed
3. Read the Aux Cameras list and check that "Enable Wireless Cameras" is now On
```

## expected_result

```
1. The wireless AUX camera entry registers the selection
2. No pop-up is displayed
3. The "Enable Wireless Cameras" setting is On
```
