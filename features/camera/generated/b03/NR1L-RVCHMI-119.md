# NR1L-RVCHMI-119 — SWE1-RVC-107

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.7.4`（來源列 `NRL-188114`）

## test_item 上半（verbatim，SYS1 逐字）

> Signal strength and battery be available on wireless aux views

## reasoning

§28.7.4 之 `views`（複數）須以兩個視角驗得，故前提佈兩台無線相機。與 `-102`（§28.2.3）之分工見該列 reasoning（時序 vs 恆可得）。與 B02b `-080`（§27.8.4，`below More AUX button`）之分工：後者驗其**位置**（More AUX 按鍵下方），本列驗其**於各無線視角皆可得**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. Two wireless AUX cameras are connected
7. The wireless AUX 1 camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the wireless AUX 1 view and check that the signal strength and the battery are shown
2. Switch to the wireless AUX 2 view
3. Read the wireless AUX 2 view and check that the signal strength and the battery are shown
```

## expected_result

```
1. The signal strength and the battery are shown on the wireless AUX 1 view
2. The wireless AUX 2 view is displayed
3. The signal strength and the battery are shown on the wireless AUX 2 view
```
