# NR1L-RVCHMI-072 — SWE1-RVC-082-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.6.1`（來源列 `NRL-188076`）

## test_item 上半（verbatim，SYS1 逐字）

> If the ‘Enable wireless cameras’ setting is OFF, and a wireless projection session is active, when a wireless aux camera is selected from any location, a popup is displayed.

## reasoning

§27.6.1 之前半（彈窗之出現）。同一個 `PU1518` —— 其觸發欄第二句逐字 `Also displayed If wireless projection is connected and user presses a wireless camera button to view a camera feed`，即本節之情境（§27.4.2 為其第一句之情境）。與 `-064`（§27.4.2）之分工：兩列之**觸發動作不同**（操作設定 vs 選取相機），來源列亦不同（`NRL-188066` vs `NRL-188076`），依 **R-CAM10** 不合併。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
7. A wireless AUX camera is within range and powered on
```

## input_test_data

`NA`

## test_procedure

```
1. Select the wireless AUX camera entry from the Aux Cameras list
2. Read the pop-up text on the HU display
```

## expected_result

```
1. The wireless AUX camera entry registers the selection
2. The pop-up reads "Do you want to disconnect Apple CarPlay and enable Wireless Cameras? Apple CarPlay can be connected using the USB port when Wireless Cameras are enabled." with <Yes> and <No> (PU1518)
```
