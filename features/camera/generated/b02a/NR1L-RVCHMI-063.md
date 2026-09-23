# NR1L-RVCHMI-063 — SWE1-RVC-073

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.1`（來源列 `NRL-188065`）

## test_item 上半（verbatim，SYS1 逐字）

> In order to enable wireless cameras, the user has to activate the ‘enable wireless cameras’ setting.

## reasoning

§27.4.1 逐字。設定名之大小寫取 §27.4.5 與 `PU1517`／`PU1518` 之 `Enable Wireless Cameras`（§27.4.1／§27.4.4 寫 `‘enable wireless cameras’`／`‘Enable wireless cameras’`，三處大小寫不一，取彈窗表之拼法）。路徑取 `HMI Settings List` `Settings` 分頁 row 464 `13. Camera` → row 474 `10. Aux Cameras`；**該設定本身不在設定表**（row 475 註 `See Head Unit Camera Systems Logic & Flow`），即由本節承載，故不掛 DR。設定句式依 canon §5.8(e) 寫 `Set "X" = "On"`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. No wireless projection session is active
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Set "Enable Wireless Cameras" = "On"
6. Read the Aux Cameras list and check that the wireless camera entries are now available
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Aux Cameras" list is displayed
5. The "Enable Wireless Cameras" setting is On
6. The wireless camera entries are available in the Aux Cameras list
```
