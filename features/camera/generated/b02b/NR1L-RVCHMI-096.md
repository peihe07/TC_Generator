# NR1L-RVCHMI-096 — SWE1-RVC-145

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.8.2`（來源列 `NRL-188182`）

## test_item 上半（verbatim，SYS1 逐字）

> If AUX camera is not connected, display blue screen “camera system unavailable”

## reasoning

§34.8.2 逐字載畫面色（`blue screen`）與訊息（`“camera system unavailable”`），故 ER 直接取來源之逐字（**§4.3.1**），**不掛 DR-CAM-h**。`forms/Pop Up List HMI R1 (26PI).xlsx` 之 `Camera System Unavailable` 命中 6 筆，module 分別為 `Rearview Camera`（`PU0169`／`PU0170`）、`Interior Camera`（`PU0844`）、`Turn Signal Activated Blind Spot View`（`PU1103`）、`Trailer Surround View Camera`（`PU1240`／`PU1270`）—— **無 `Aux Camera` module 之條目**；惟本條之文字已由來源自載，不需彈窗表補足。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. No AUX camera is connected
6. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Press the AUX button in the App Drawer
3. Read the HU display and check the screen colour and the message text
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX button registers the press
3. The AUX 1 screen is a blue screen and reads "camera system unavailable"
```
