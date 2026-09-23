# NR1L-RVCHMI-091 — SWE1-RVC-141

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.6.3`（來源列 `NRL-188176`）

## test_item 上半（verbatim，SYS1 逐字）

> Same behavior applies when accessing from cargo cam

## reasoning

§34.6.3 之 `Same behavior` 指同節 §34.6.1／§34.6.2 與 §34.4.3 所載之行為（進入 AUX、`X` 不出現、恆落 Aux 1），故本列以 cargo 視角為起點重驗該組行為。與 `-098`（§34.8.4，逐字全等）之分工：後者之父題為 `Accessing AUX – Cameras Not Connected`，其 `Same behavior` 指**未連線**之行為；兩列之父節與來源列皆不同（**R-CAM10**）。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
7. Two wired AUX cameras are connected
8. The cargo camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the AUX camera soft control in the cargo camera view
2. Read the HU display and check that the Aux 1 screen is displayed
3. Read the Aux 1 screen and check that no <X> control is present when it was entered from the cargo camera view
```

## expected_result

```
1. The AUX camera soft control registers the selection
2. The Aux 1 screen is displayed
3. No <X> control is shown in the Aux 1 screen
```
