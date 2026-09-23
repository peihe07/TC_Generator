# NR1L-RVCHMI-100 — SWE1-RVC-093

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.2.1`（來源列 `NRL-188092`）

## test_item 上半（verbatim，SYS1 逐字）

> When aux cam is accessed,“check entire surroundings message is shown for 5 seconds.

## reasoning

§28.2 之父題逐字為 `Accessing Aux Cameras no camera app`（`NRL-188091`），故前提不設 camera app。`5 seconds` 為來源逐字，以 4／6 秒兩點驗其起訖（±1 秒為人工可達之窗，見 `bench_verify.md`）。訊息文字 `Check Entire Surroundings` 於彈窗表命中 **5 筆**，module 分別為 `Surround View Camera`（`PU0362`／`PU0467`）、`Trailer Reverse Guidance`（`PU0446`）、`Rearview Camera with all features`（`PU0447`）、`Turn Signal Activated Blind Spot View`（`PU1102`）—— **無 `Aux Camera` module 之條目**；惟本條之文字與時限皆由來源自載，依 **§4.3.1** 取其逐字，**不掛 DR-CAM-h**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the AUX camera soft control in the App Drawer and record the timestamp
3. Read the HU display 4 seconds after the recorded timestamp and check that the message is still shown
4. Read the HU display 6 seconds after the recorded timestamp and check that the message is no longer shown
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX camera view is displayed and reads "Check Entire Surroundings"
3. The message is still shown 4 seconds after the view was opened
4. The message is no longer shown 6 seconds after the view was opened
```
