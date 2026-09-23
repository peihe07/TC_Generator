# NR1L-RVCHMI-147 — SWE1-RVC-119-03

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.6`（來源列 `NRL-188133`）

## test_item 上半（verbatim，SYS1 逐字）

> The rest of the cameras will be labeled : 2,3,4…etc.

## reasoning

§30.1.6 之第三個後果。`2,3,4…etc.` 之驗證須有**兩台以上非最愛**之相機方判得其序，故前提佈三台（一台最愛 ＋ 兩台非最愛）。`…etc.` 為開放式列舉，不造第四台之判準（§8.4.1）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. Three wired AUX cameras are connected
4. AUX 1 has been made favorite
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Read the camera icons and check the labels of the cameras that are not the favorite
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The cameras that are not the favorite are labeled 2 and 3 in order
```
