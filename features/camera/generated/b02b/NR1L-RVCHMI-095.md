# NR1L-RVCHMI-095 — SWE1-RVC-144

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.8.1`（來源列 `NRL-188181`）

## test_item 上半（verbatim，SYS1 逐字）

> Pressing the AUX button will always take the user to the AUX 1 screen

## reasoning

§34.8 之父題逐字為 `Accessing AUX – Cameras Not Connected`（`NRL-188180`），故前提為**未連線**。本列驗 `always` 於該情境下仍成立（即使無相機，仍落 AUX 1 畫面）——其畫面內容由 `-096`（§34.8.2）承接。與 `-088`（§34.4.3）之分工見該列 reasoning（已連線 vs 未連線）。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

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
3. Read the HU display and check that the AUX 1 screen is displayed
```

## expected_result

```
1. The App Drawer is displayed
2. The AUX button registers the press
3. The AUX 1 screen is displayed
```
