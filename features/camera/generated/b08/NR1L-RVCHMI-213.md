# NR1L-RVCHMI-213 — SWE1-RVC-091

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.8.5`（來源列 `NRL-188087`）

## test_item 上半（verbatim，SYS1 逐字）

> For details about wireless cameras connection please refer to ‘Wireless cameras connection’ pages.

## reasoning

**R-CAM19(c) 追溯補齊**（CAM-26 §2）：§27.8.5 全文為交叉引用句（同 §27.7.3，A-CA36），標的為 §27.5／§27.6。本列之父 §27.8 為 `Accessing Aux Cameras – from Rear View Camera`（`NRL-188082`），故前提取 `Rear_View_Camera = 1` 與「後視影像顯示中」，入口取影像中之 `“More Aux”` 彈窗（§27.8.1，`NR1L-RVCHMI-077`）；行為取 **§27.6.1**（設定 OFF 且有投影時選取無線相機 → 彈窗），**被引列 TC `NR1L-RVCHMI-072`**，彈窗逐字沿其 `PU1518`（`forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁）。與 `-212` 之分工：兩列之父節（入口）與被引行為（§27.5.2 vs §27.6.1）皆不同。`-072` 自 `Aux Cameras` 清單選取，本列自 `More Aux` 彈窗選取（§27.6.1 之 `from any location`）。`Rear_View_Camera` 五本 PROXI 皆有（`HDCC27`／`DT27`／`637`／`2261`／`376`），R-CAM18(a) 五款全 `1`（同 `-077`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The head unit is a touchscreen radio
4. The head unit has WiFi hotspot capability
5. A MOPAR-provided wireless camera is available
6. The "Enable Wireless Cameras" setting is Off
7. A wireless projection session is active
8. A wireless AUX camera is within range and powered on
9. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "More Aux" button in the rear view camera image
2. Select the wireless AUX camera button in the pop-up
3. Read the pop-up text on the HU display
```

## expected_result

```
1. The "More Aux" button registers the press and a pop-up opens
2. The wireless AUX camera button registers the selection
3. The pop-up reads "Do you want to disconnect Apple CarPlay and enable Wireless Cameras? Apple CarPlay can be connected using the USB port when Wireless Cameras are enabled." with <Yes> and <No> (PU1518)
```
