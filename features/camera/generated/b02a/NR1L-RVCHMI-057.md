# NR1L-RVCHMI-057 — SWE1-RVC-066

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.6.2`（來源列 `NRL-188050`）

## test_item 上半（verbatim，SYS1 逐字）

> Apps Drawer

## reasoning

§27.2.6.2 為 `Accessible from` 節（§27.2.6）下之入口列舉之一，Description 逐字即 `Apps Drawer`（2 token）。同節之 §27.2.6.3（`Camera app home page`）由 `-058` 承接。App Drawer 之進入句式沿 A 本 `NR1L-RVC-113`（**R-CAM1(b)**），故不掛 DR-CAM-g。H 本 §27.7.1 逐字 `All Wired and Wireless Aux cameras will be accessible via the controls page and apps drawer` 為同一入口之第二處記載（該列為 B02b 之 `SWE1-RVC-084`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the AUX camera soft control in the App Drawer
3. Read the HU display and check that the AUX 1 camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX camera soft control registers the selection
3. The AUX 1 camera view is displayed
```
