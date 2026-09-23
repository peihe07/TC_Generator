# NR1L-RVCHMI-196 — SWE1-RVC-047-01

- **Test Group**：Rear View Camera｜**Test Set**：Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.2.2.3`（來源列 `NRL-187343`）

## test_item 上半（verbatim，SYS1 逐字）

> Rear View Camera Fixed Guidelines (on/off) – provides the user with the option to toggle between having fixed guidelines or no guidelines Factory Default => OFF

## reasoning

設定名與 HMI Settings List **row 469** 之 `Rear View Camera Fixed Guidelines` 相符（該列**無** `*`，與 row 467／468 不同）。本列驗其切換與出廠預設；該列之 `Note:` 一句（兩種輔助線不可並存）由 `-197` 承接。

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
4. Read the "Camera" list and check the state of "Rear View Camera Fixed Guidelines"
5. Set "Rear View Camera Fixed Guidelines" = "On"
6. Read the rear view camera image and check the guidelines
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. "Rear View Camera Fixed Guidelines" is Off, which is the factory default
5. The "Rear View Camera Fixed Guidelines" setting is On
6. The fixed guidelines are shown on the rear view camera image
```
