# NR1L-RVCHMI-031 — SWE1-RVC-019-04

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.4`（來源列 `NRL-142625`）

## test_item 上半（verbatim，SYS1 逐字）

> Pushing the button both RVC & sensors shall be displayed.

## reasoning

§7.4 之末句。`both RVC & sensors` 之 sensors 即 PAM 感測區，故前提加 `CVPAM_Presence = 1`。本列為**手動活化**（按鍵），與 `-028`（自動活化之初始視角）分工。`CVPAM_Presence` 於 `Toro_ATL_MI` 0 命中 → **R-CAM18(b)** `Toro(2261)` 判 `0`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. The shift lever is in D
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the camera soft button on the HU
2. Read the HU display and check that the rear view camera image and the PAM sensor area are both displayed
```

## expected_result

```
1. The camera soft button registers the press
2. The rear view camera image and the PAM sensor area are both displayed
```
