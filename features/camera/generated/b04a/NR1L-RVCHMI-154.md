# NR1L-RVCHMI-154 — SWE1-RVC-124

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.5`（來源列 `NRL-188140`）

## test_item 上半（verbatim，SYS1 逐字）

> The updated name also is reflected on the camera app homepage, in that camera’s soft button

## reasoning

§31.1.5 逐字。與 `-153`（§31.1.4）成一對：同一次改名於**兩處**之反映（設定選單線項 vs camera app 首頁軟鍵），來源列不同故分列（**R-CAM10**）。camera app 之配備旗標零命中 → **DR-CAM-r**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. A wired AUX camera is connected
4. The camera name has just been changed and confirmed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Read that camera's soft button on the Camera app home page
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. That camera's soft button reads the new name
```
