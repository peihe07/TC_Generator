# NR1L-RVCHMI-195 — SWE1-RVC-046

- **Test Group**：Rear View Camera｜**Test Set**：Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.2.2.2`（來源列 `NRL-187342`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear View Camera Active Guidelines (on/off) – provides the user with the option to toggle between having dynamic guidelines or no guidelines Factory Default => ON

## reasoning

設定名與 HMI Settings List **row 468** 之 `Rear View Camera Active Guidelines*` 相符（`*` 依 **R-CAM5(a)** 不入 hop）。`toggle between having dynamic guidelines or no guidelines` 之兩態皆驗，並驗其 `Factory Default => ON`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU has been reset to its factory defaults
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Read the "Camera" list and check the state of "Rear View Camera Active Guidelines"
5. Set "Rear View Camera Active Guidelines" = "Off"
6. Read the rear view camera image and check the guidelines
7. Set "Rear View Camera Active Guidelines" = "On"
8. Read the rear view camera image and check the guidelines
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. "Rear View Camera Active Guidelines" is On, which is the factory default
5. The "Rear View Camera Active Guidelines" setting is Off
6. No guidelines are shown on the rear view camera image
7. The "Rear View Camera Active Guidelines" setting is On
8. The dynamic guidelines are shown on the rear view camera image
```
