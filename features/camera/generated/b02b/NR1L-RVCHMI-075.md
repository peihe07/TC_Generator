# NR1L-RVCHMI-075 — SWE1-RVC-084

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.7.1`（來源列 `NRL-188079`）

## test_item 上半（verbatim，SYS1 逐字）

> All Wired and Wireless Aux cameras will be accessible via the controls page and apps drawer

## reasoning

§27.7.1 之 `All Wired and Wireless` 為本列之驗證重點 —— 兩種 AUX 皆須在**兩個**入口出現，故四格皆驗。與 `-057`（§27.2.6.2，`Apps Drawer`）之分工：後者為 `Accessible from` 節之入口列舉（只驗 App Drawer 一個入口、不分有線無線），本列為 §27.7 之完整性要求。Controls 頁之進入路徑無逐字來源 → **DR-CAM-g**（其第 (1) 項）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wired AUX camera and a wireless AUX camera are both connected
7. The shift lever is in P
8. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g the entry path to the Controls screen is not sourced
2. Read the Controls screen and check that both the wired and the wireless AUX soft controls are present
3. Press "Apps" on Menu Bar to open App Drawer
4. Read the App Drawer and check that both the wired and the wireless AUX soft controls are present
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. The wired AUX and the wireless AUX soft controls are both shown on the Controls screen
3. The App Drawer is displayed
4. The wired AUX and the wireless AUX soft controls are both shown in the App Drawer
```
