# NR1L-RVCHMI-048 — SWE1-RVC-057

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.5`（來源列 `NRL-188033`）

## test_item 上半（verbatim，SYS1 逐字）

> Wireless Aux Feature functionality will be limited to four (4) wireless MOPAR-provided cameras, connected via WiFi protocol.

## reasoning

§27.1.5 逐字載上限 `four (4)`。四台之佈建須實機，記入 `bench_verify.md`。`WiFi protocol` 之硬體前提取 §27.3.1.1～§27.3.1.3 逐字（觸控螢幕、WiFi hotspot 能力、MOPAR 相機）。無線 AUX 相機**無 PROXI 配備旗標** —— 掃描字串 `Wireless_Camera`／`Wireless_Aux`／`Aux_Camera`／`Hotspot` 於 `forms/proxi/` 六本**各 0 命中**；SYS1 以 §27.3.1.x 之硬體條件與 §27.4.1 之 `Enable Wireless Cameras` 設定為替代條件，故依 **R-CAM18(a)** 五款平台皆 `1`，不掛 DR（升級條件 §4-3 不成立）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. Four wireless MOPAR-provided cameras are already connected
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Select the control that adds a wireless camera
6. Read the HU display and check that a fifth wireless camera cannot be added
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Aux Cameras" list is displayed with the four connected wireless cameras
5. The add control is either not offered or does not start the add process
6. No fifth wireless camera is added
```
