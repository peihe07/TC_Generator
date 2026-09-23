# NR1L-RVCHMI-058 — SWE1-RVC-067

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.6.3`（來源列 `NRL-188051`）

## test_item 上半（verbatim，SYS1 逐字）

> Camera app home page

## reasoning

§27.2.6.3 之 Description 逐字即 `Camera app home page`（4 token）。「Camera App」配備旗標六本 PROXI 零命中 → **DR-CAM-r**。與 `-057`（§27.2.6.2）之分工：兩者為同節列舉之兩個相異入口。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. A wired AUX camera is connected
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the AUX camera soft control on the Camera app home page
4. Read the HU display and check that the AUX 1 camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The AUX camera soft control registers the selection
4. The AUX 1 camera view is displayed
```
