# NR1L-RVCHMI-146 — SWE1-RVC-119-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.6`（來源列 `NRL-188133`）

## test_item 上半（verbatim，SYS1 逐字）

> This camera icon will also be moved to the favorite filter for easy access.

## reasoning

§30.1.6 之第二個後果。`favorite filter` 為逐字；H 本 §19.1.2.3 逐字載 `When the Camera App is opened, the favorite camera filter will be the default filter page showing` —— 惟 **HU 章 18–22 為 B 本 230 列一列未引之範圍**（**A-CA12**），故只取其為用語佐證，不測其內容（§8.4.2）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. Two wired AUX cameras are connected
4. AUX 1 has been made favorite
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Select the favorite filter on the Camera app home page
4. Read the favorite filter and check that the AUX 1 camera icon is present there
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The favorite filter is displayed
4. The AUX 1 camera icon is shown in the favorite filter
```
