# NR1L-RVCHMI-208 — SWE1-RVC-103-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.1.1`（來源列 `NRL-188110`）

## test_item 上半（verbatim，SYS1 逐字）

> Manipulate the image (zoom/pan, rotate image, mirror image) -The zoom functionality will be a pinch to zoom

## reasoning

**補正之由**：**CAM-24 審閱 §一-1** —— canon **§8.3**（boundary 每點一 TC）與**§5.7**（不同觸發須拆）勝於本 feature 之既有前例；母列 `NR1L-RVCHMI-111` 原含多點／多觸發，已原地收斂為單點，本列承接其餘者。母列之 reasoning 已註本列之 ID。分析層記一筆：該形制經批次審閱而未抓（**A-CA37**）。`pinch to zoom` 之兩個方向為**兩個相異之觸發手勢**（向外／向內），依 **§5.7** 分列；母列留向外（zoom in），本列驗向內（zoom out）。前提加「影像已放大」—— 未放大時無從觀察縮小。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. The wireless AUX camera view is displayed
8. The image has been zoomed in
```

## input_test_data

`NA`

## test_procedure

```
1. Pinch inwards on the camera image with two fingers
2. Read the camera image and check that it has zoomed out
```

## expected_result

```
1. The inward pinch gesture is registered on the camera image
2. The camera image zooms out
```
