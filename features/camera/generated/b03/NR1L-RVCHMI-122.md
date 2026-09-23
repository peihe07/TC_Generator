# NR1L-RVCHMI-122 — SWE1-RVC-108-03

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.8.1`（來源列 `NRL-188116`）

## test_item 上半（verbatim，SYS1 逐字）

> From the AUX camera video feed, however, access to the other AUX views is available via the more aux button on the view

## reasoning

§28.8.1 之第三支（`via the more aux button on the view`）。與 `-121` 成一對：同一目的（進入另一個 AUX 視角）之**兩個入口**，來源以 `or` 並列，可觀察路徑不同故分列。

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
1. Press the more aux button on the view
2. Read the list and check that the other AUX view is offered
3. Select the wireless AUX 2 entry
4. Read the HU display and check that the wireless AUX 2 view is displayed
```

## expected_result

```
1. The more aux button registers the press
2. The wireless AUX 2 entry is shown in the list
3. The wireless AUX 2 entry registers the selection
4. The wireless AUX 2 camera view is displayed
```
