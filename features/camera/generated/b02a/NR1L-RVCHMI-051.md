# NR1L-RVCHMI-051 — SWE1-RVC-060

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.2.1`（來源列 `NRL-188040`）

## test_item 上半（verbatim，SYS1 逐字）

> Icons will exist for “AUX Cameras” in the camera views

## reasoning

§27.2.2.1 為 `Recommended Labels/Icons` 節下之一句；`“AUX Cameras”` 為逐字標籤。與 `-050`（§27.2.1.1）之分工：後者驗控制項**所在之表面**（second surface，兩個視角），本列驗**圖示之存在與可用**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A wired AUX camera is connected
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the rear view camera image and check that an "AUX Cameras" icon is present
2. Select the "AUX Cameras" icon
3. Read the HU display and check that an AUX camera view is displayed
```

## expected_result

```
1. The "AUX Cameras" icon is shown in the rear view camera image
2. The "AUX Cameras" icon registers the selection
3. An AUX camera view is displayed
```
