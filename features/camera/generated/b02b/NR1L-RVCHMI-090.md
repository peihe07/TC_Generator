# NR1L-RVCHMI-090 — SWE1-RVC-140

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.6.2`（來源列 `NRL-188175`）

## test_item 上半（verbatim，SYS1 逐字）

> Below screen is also accessed when shifting to REVERSE, but <X> is not present

## reasoning

與 `-086`（§34.3.2）逐字全等，惟**父題不同** —— 本列之父為 §34.6 `Accessing Aux Cameras – Backup and Cargo Cam`（配置含 Cargo），`-086` 之父為 §34.3 `Accessing Aux Cameras – Backup Cam Only`。配置不同即前提不同（本列加 `Digital_CHMSL_Camera_Prsnt = 1`），故**不委派**。反之 §34.4.2 之父題與 §34.3 全等，故委派 `-086`（見上繳 §2-2）。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
7. A wired AUX camera is connected
8. The shift lever is in P
9. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the back-up camera view is displayed
3. Read the back-up camera view and check that no <X> control is present
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The back-up camera view is displayed
3. No <X> control is shown in the back-up camera view
```
