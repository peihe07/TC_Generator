# NR1L-RVCHMI-074 — SWE1-RVC-083

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.6.2`（來源列 `NRL-188077`）

## test_item 上半（verbatim，SYS1 逐字）

> The camera may be asleep and take up to a few seconds to activate. When this occurs, a message will show letting the customer know the camera is “connecting”

## reasoning

§27.6.2 與 §27.5.1（`NR1L-RVCHMI-070`）之條文**同型而非同句**（29 vs 47 token，前者無 `If the ‘Enable wireless cameras’ setting is ON, when a wireless aux camera is selected from any location` 之前置條件句）。**分工**：`-070` 為 §27.5 之情境（**無**投影，設定本即 ON），本列為 §27.6 之情境（**有**投影，經 `PU1518` 按 `<Yes>` 後）——兩者之父節（`NRL-188072` vs `NRL-188075`）與來源列皆不同，依 **R-CAM10** 不合併。`connecting` 之逐字文字查無 → **`PENDING: DR-CAM-h`**（已擴題，DECISIONS 6-60）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
7. A wireless AUX camera is connected and asleep
8. The PU1518 pop-up is displayed after the wireless AUX camera was selected
```

## input_test_data

`NA`

## test_procedure

```
1. Select <Yes> on the pop-up
2. Read the HU display and check that a message tells the customer the camera is connecting
3. Read the HU display and check that the wireless AUX camera view is displayed once it has activated
```

## expected_result

```
1. The <Yes> button registers the selection and the pop-up closes
2. PENDING: DR-CAM-h a message showing that the camera is "connecting" is displayed; its verbatim text is not in the R1 HMI pop-up list
3. The wireless AUX camera view is displayed
```
