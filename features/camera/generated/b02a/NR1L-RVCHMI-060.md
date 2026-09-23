# NR1L-RVCHMI-060 — SWE1-RVC-070

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.3.3`（來源列 `NRL-188059`）

## test_item 上半（verbatim，SYS1 逐字）

> Pop-up Messages Please refer also to R1 HMI popup list for final text

## reasoning

§27.3.3 本身即「彈窗文字以 R1 HMI popup list 為準」之規定，故本列驗**一致性**而非某一彈窗之行為。取 `PU0459` 為樣本 —— 其 module 欄為 `Aux Camera`、文字欄逐字 `No camera connected. Camera unavailable. Make sure camera is ON and within range`（`forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁）。其餘 AUX 彈窗（`PU0450`～`PU0459`、`PU0854`～`PU0858`、`PU1517`～`PU1519`）之逐字於其對應之行為列驗，不在本列重複。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless camera is within range or powered on
7. The AUX camera list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the wireless AUX camera entry
2. Read the pop-up text on the HU display
```

## expected_result

```
1. The wireless AUX camera entry registers the selection
2. The pop-up reads "No camera connected. Camera unavailable. Make sure camera is ON and within range" (PU0459 of the R1 HMI pop-up list)
```
