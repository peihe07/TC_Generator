# NR1L-RVCHMI-098 — SWE1-RVC-147

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.8.4`（來源列 `NRL-188184`）

## test_item 上半（verbatim，SYS1 逐字）

> Same behavior applies when accessing from cargo cam

## reasoning

§34.8.4 之 `Same behavior` 指同節 §34.8.1～§34.8.3 之**未連線**行為，故以 cargo 視角為起點重驗 `-096` 之結果。與 `-091`（§34.6.3，逐字全等）之分工：後者之父題為 `Accessing Aux Cameras – Backup and Cargo Cam`（已連線），本列之父題為 `Accessing AUX – Cameras Not Connected`（未連線）；兩列之父節與來源列皆不同（**R-CAM10**）。`Digital_CHMSL_Camera_Prsnt`（Cargo）只存在於 Atl-Hi 三本 → **R-CAM18(b)** Atl-Mi 三欄 `0`。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
6. No AUX camera is connected
7. The cargo camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the AUX camera soft control in the cargo camera view
2. Read the HU display and check the screen colour and the message text
```

## expected_result

```
1. The AUX camera soft control registers the selection
2. The AUX 1 screen is a blue screen and reads "camera system unavailable"
```
