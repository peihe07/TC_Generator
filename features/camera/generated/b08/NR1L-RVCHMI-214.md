# NR1L-RVCHMI-214 — SWE1-RVC-102

- **Test Group**：Rear View Camera｜**Test Set**：Camera View Switching
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_28.6.1.2`（來源列 `NRL-188107`）

## test_item 上半（verbatim，SYS1 逐字）

> For details about wireless cameras connection please refer to ‘Wireless cameras connection’ pages

## reasoning

**R-CAM19(c) 追溯補齊**（CAM-26 §2）：§28.6.1.2 全文為交叉引用句（同 §27.7.3，A-CA36），標的為 §27.5／§27.6。本列之父 §28.6.1 為 `Top + Rear Automatic camera manual activation, shifted to Reverse, “R”`（`NRL-188105`），其父 §28.6 為 `UI – In Reverse with “Surround View and Camera App”`（`NRL-188104`）→ 前提取 `Surround_View_Camera = 1`、入口取 R 檔中之 `“More Cams”`（§28.6.1.1，`NR1L-RVCHMI-109`）。行為取 **§27.5.1**（設定 ON、相機休眠 → `connecting` 訊息），**被引列 TC `NR1L-RVCHMI-070`**；`connecting` 之逐字查無 → `PENDING: DR-CAM-h`（沿 `-070`）。與 `-212`／`-213` 之分工：三列之入口（App Drawer／More Aux／More Cams in R）與被引行為（§27.5.2／§27.6.1／§27.5.1）皆相異。`Surround_View_Camera` 於 `Toro_ATL_MI` 之 2019 本**不存在**（掃描字串 `Surround_View_Camera`，`forms/proxi/` 六本，openpyxl 全格掃描：HDCC27 兩本／DT27／637／376 各 1、**Toro 0**；DR-CAM-l）→ **R-CAM18(b)** `Toro(2261)` 判 `0`（同 `-109`）。CAN source 行依 R-CAM3(e)／(f)：本列同時勾兩 EE 且有 `Send CAN` 步。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The head unit is a touchscreen radio
5. The head unit has WiFi hotspot capability
6. A MOPAR-provided wireless camera is available
7. The "Enable Wireless Cameras" setting is On
8. No wireless projection session is active
9. A wireless AUX camera is connected and asleep
10. The shift lever is in P
11. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Press the "More Cams" button and select the wireless AUX camera view
3. Read the HU display and check that a message tells the customer the camera is connecting
4. Read the HU display and check that the wireless AUX camera view is displayed once it has activated
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the camera view is displayed
2. The wireless AUX camera view is selected from the pop-up
3. PENDING: DR-CAM-h a message showing that the camera is "connecting" is displayed; its verbatim text is not in the R1 HMI pop-up list
4. The wireless AUX camera view is displayed while the gear is still R
```
