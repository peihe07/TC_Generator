# NR1L-RVCHMI-106 — SWE1-RVC-098-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.3.2`（來源列 `NRL-188098`）

## test_item 上半（verbatim，SYS1 逐字）

> The Same behavior applies when accessing via all methods, with or without camera app

## reasoning

§28.3.2 之末句（`with or without camera app`）。`-105` 已驗**無** camera app 之路徑（自 App Drawer 直接進），本列驗**有** camera app 之路徑（經 Camera app home page），兩者之可觀察結果須相同。`accessing via all methods` 之方法集取 §27.2.6 之 `Accessible from`（App Drawer／Camera app home page），不另造方法。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
3. A wired AUX camera other than AUX 1 is connected
4. Wired AUX 1 is not connected
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select the Camera app in the App Drawer
3. Press the AUX camera button on the Camera app home page
4. Read the HU display and check the screen colour, the message text and the offered option
```

## expected_result

```
1. The App Drawer is displayed
2. The Camera app home page is displayed
3. The AUX camera button registers the press
4. The display is a blue screen, reads "camera system unavailable" and offers "More AUX", which is the same behaviour as without the camera app
```
