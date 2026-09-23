# NR1L-RVCHMI-111 — SWE1-RVC-103-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.1.1`（來源列 `NRL-188110`）

## test_item 上半（verbatim，SYS1 逐字）

> Manipulate the image (zoom/pan, rotate image, mirror image) -The zoom functionality will be a pinch to zoom

## reasoning

§28.7.1.1 之 zoom 一支（`-The zoom functionality will be a pinch to zoom`）。`pinch to zoom` 之雙向（放大／縮小）皆驗 —— 單向不足以判該手勢已繫於 zoom。verbatim 為該列 Description 之保序子序列（刪 pan 一支，由 `-110` 承接）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. A wireless AUX camera is connected
7. The wireless AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Pinch outwards on the camera image with two fingers
2. Read the camera image and check that it has zoomed in
3. Pinch inwards on the camera image with two fingers
4. Read the camera image and check that it has zoomed out
```

## expected_result

```
1. The outward pinch gesture is registered on the camera image
2. The camera image zooms in
3. The inward pinch gesture is registered on the camera image
4. The camera image zooms out
```
