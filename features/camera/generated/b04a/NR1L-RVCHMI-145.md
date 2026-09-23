# NR1L-RVCHMI-145 — SWE1-RVC-119-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.6`（來源列 `NRL-188133`）

## test_item 上半（verbatim，SYS1 逐字）

> Once the user returns to the homepage, the favorites star will be shown inside the camera icon circle to signify that it is the favorite.

## reasoning

§30.1.6 載三個後果，三列各驗一個（`-145`～`-147`）。`the homepage` 即 camera app home page（§27.2.6.3 之逐字 hop label），故掛 **DR-CAM-r**。與 `-144`（§30.1.5）之分工：後者為**設定選單**之線項星號，本列為**首頁圖示**內之星號。

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
3. Read the AUX 1 camera icon and check that the favorites star is shown inside the icon circle
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The favorites star is shown inside the AUX 1 camera icon circle
```
