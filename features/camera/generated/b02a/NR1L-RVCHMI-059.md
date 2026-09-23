# NR1L-RVCHMI-059 — SWE1-RVC-068

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.6.4`（來源列 `NRL-188052`）

## test_item 上半（verbatim，SYS1 逐字）

> Selected View soft control will be highlighted

## reasoning

§27.2.6.4 與 §27.1.3（`-046`）**逐字同句**，惟所在之節不同：§27.1.3 在 `Feature Assumptions`（通則），§27.2.6.4 在 `Accessible from`（第二表面之控制列）。**依 R-CAM10 兩列之承接列不同，故不合併**；分工為：`-046` 驗 AUX 清單內之 highlight 隨選取移動，本列驗**相機視角內**（second surface）之 highlight。

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
1. Read the soft controls within the rear view camera image and check that the rear view soft control is highlighted
2. Select the AUX 1 soft control within the view
3. Read the soft controls within the AUX 1 view and check that the AUX 1 soft control is highlighted
```

## expected_result

```
1. The rear view soft control is highlighted within the rear view camera image
2. The AUX 1 camera view is displayed
3. The AUX 1 soft control is highlighted within the AUX 1 view
```
