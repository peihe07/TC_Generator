# NR1L-RVCHMI-103 — SWE1-RVC-096

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.2.4`（來源列 `NRL-188095`）

## test_item 上半（verbatim，SYS1 逐字）

> If user presses “X” the screen will return to the previous screen from which aux camera was accessed (X functions like back button)

## reasoning

§28.2.4 之 `(X functions like back button)` 為括號內之逐字說明，其可觀察形制即「回到**進入前**之畫面」，故前提明記進入來源為後視影像。與 B02b `-093`（§34.7.2 之 `unless acting as a back button within camera views`）之分工：後者之情境為 **R 檔中**（`X` 本不可用，只在相機視角間作返回鍵），本列為一般情境下之返回；兩列之來源本章與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A wired AUX camera is connected
4. The rear view camera image is displayed
5. The AUX camera view was opened from the rear view camera image
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" control in the AUX camera view
2. Read the HU display and check that the rear view camera image is shown again
```

## expected_result

```
1. The "X" control registers the press
2. The rear view camera image is shown again, which is the display from which the AUX camera was accessed
```
