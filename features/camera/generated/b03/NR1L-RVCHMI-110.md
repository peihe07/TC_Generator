# NR1L-RVCHMI-110 — SWE1-RVC-103-01

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.1.1`（來源列 `NRL-188110`）

## test_item 上半（verbatim，SYS1 逐字）

> Manipulate the image (zoom/pan, rotate image, mirror image) -The pan functionality will be a drag/ swipe to pan

## reasoning

§28.7.1 之父句逐字為 `From the Wireless AUX camera video feed, the user can:`（`NRL-188109`），故前提取無線 AUX 視角。本列取 §28.7.1.1 之 pan 一支（`-The pan functionality will be a drag/ swipe to pan`）；zoom 一支由 `-111` 承接。rotate／mirror 之操作入口在 §28.7.2（`-114`～`-116`），本節只載其為可操作之項，不重複驗。

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
1. Drag across the camera image with one finger
2. Read the camera image and check that it has panned in the direction of the drag
```

## expected_result

```
1. The drag gesture is registered on the camera image
2. The camera image pans in the direction of the drag
```
