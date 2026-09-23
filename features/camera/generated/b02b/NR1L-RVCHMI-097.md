# NR1L-RVCHMI-097 — SWE1-RVC-146

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.8.3`（來源列 `NRL-188183`）

## test_item 上半（verbatim，SYS1 逐字）

> If AUX 2 connected, but AUX 1 not connected, system shall display blue screen “camera system unavailable” with customer option to select AUX 2

## reasoning

§34.8.3 為 §34.8.2 之分支（AUX 1 未連線但 AUX 2 已連線），其增量為 `with customer option to select AUX 2`。與 `-096` 之分工：後者驗**全未連線**之畫面，本列驗**部分連線**時之選項與其後果。H 本 §28.3.2 為同型條文（`with customer option to select More AUX`），屬 `Camera View Switching` 組，不在本批。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. AUX 2 is connected
6. AUX 1 is not connected
7. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Press the AUX button in the App Drawer
3. Read the HU display and check the screen colour, the message text and the offered option
4. Select the AUX 2 option
5. Read the HU display and check that the AUX 2 camera view is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX button registers the press
3. The AUX 1 screen is a blue screen, reads "camera system unavailable" and offers an option to select AUX 2
4. The AUX 2 option registers the selection
5. The AUX 2 camera view is displayed
```
