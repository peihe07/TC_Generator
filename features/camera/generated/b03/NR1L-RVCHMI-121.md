# NR1L-RVCHMI-121 — SWE1-RVC-108-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.8.1`（來源列 `NRL-188116`）

## test_item 上半（verbatim，SYS1 逐字）

> From the AUX camera video feed, however, access to the other AUX views is available below the camera feed

## reasoning

§28.8.1 之第二支（`below the camera feed`）。該位置為 12 吋直式之特有排版，與 §28.7 之橫式（soft control 在視角內）相對。verbatim 為該列 Description 之保序子序列 —— 保留首片語 `From the AUX camera video feed,`（否則上半以小寫 `however,` 起首而命中 lint `J`，且 **profile §5.1 之豁免不適用** ——該豁免之要件為「上半與來源 `Description` 之**首 token** 相同」，本列非自首 token 起）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. PROXI Radio_Display_Type = 7 (12" 1200x1920)
7. Two wireless AUX cameras are connected
8. The wireless AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the area below the camera feed and check that the other AUX view is offered there
2. Select the wireless AUX 2 entry below the camera feed
3. Read the HU display and check that the wireless AUX 2 view is displayed
```

## expected_result

```
1. The wireless AUX 2 entry is shown below the camera feed
2. The wireless AUX 2 entry registers the selection
3. The wireless AUX 2 camera view is displayed
```
