# NR1L-RVCHMI-102 — SWE1-RVC-095

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.2.3`（來源列 `NRL-188094`）

## test_item 上半（verbatim，SYS1 逐字）

> After 5 seconds, the WiFi signal strength and battery level is shown for wireless cameras

## reasoning

§28.2.3 之 `After 5 seconds` 接續 §28.2.1 之訊息時限，故觀察點取 6 秒。逐字畫面取 **`PU0852`**（module `Aux Camera`；觸發欄逐字 `View when the Wireless Camera soft key is pressed.After The camera name is displayed and the WiFi signal strength and battery level is shown.`；文字欄 `<Insert Camera Name Here> <Battery><WiFi>`）。與 `-120`（§28.7.4，`Signal strength and battery be available on wireless aux views`）之分工：後者驗**該指示於無線 AUX 視角恆可得**，本列驗其**出現之時序**（訊息消失後）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the wireless AUX camera soft control in the App Drawer and record the timestamp
3. Read the HU display 6 seconds after the recorded timestamp and check that the WiFi signal strength and the battery level are shown
```

## expected_result

```
1. The App Drawer is displayed
2. The wireless AUX camera view is displayed
3. The camera name, the battery level and the WiFi signal strength are shown (PU0852)
```
