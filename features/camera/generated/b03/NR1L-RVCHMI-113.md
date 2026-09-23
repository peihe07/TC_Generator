# NR1L-RVCHMI-113 — SWE1-RVC-104-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.1.2`（來源列 `NRL-188111`）

## test_item 上半（verbatim，SYS1 逐字）

> -Manipulated settings will latch(zoom/pan, rotate image 90 degrees, mirror image)

## reasoning

§28.7.1.2 之後半。`latch` 之可觀察定義取 H 本 **§21.5**（`Latching Views`）之同一用語 ——即設定於離開該視角後仍保持。以 zoom 一項驗之（三項之 latch 機制同一），verbatim 保留三項之逐字列舉。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. PROXI Rear_View_Camera = 1 (Present)
8. The wireless AUX camera view is displayed
9. The image has been zoomed in
```

## input_test_data

`NA`

## test_procedure

```
1. Switch to the rear view camera image
2. Switch back to the wireless AUX camera view
3. Read the camera image and check that the zoom is still applied
```

## expected_result

```
1. The rear view camera image is displayed
2. The wireless AUX camera view is displayed again
3. The zoom that was applied earlier is still in effect, which is the latching behaviour
```
