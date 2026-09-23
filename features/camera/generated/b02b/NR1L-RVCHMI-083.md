# NR1L-RVCHMI-083 — SWE1-RVC-131

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.1.3.1`（來源列 `NRL-188159`）

## test_item 上半（verbatim，SYS1 逐字）

> AUX cam will always be a selectable field

## reasoning

本列與 §27.2.3.1（`NR1L-RVCHMI-052`）**非逐字全等** —— 後者為 `**Wired** AUX cam will always be a selectable field`（9 token），本列無 `Wired` 一字（8 token）；R1 Low 本即只有有線，故不需該限定詞。§34 之章標題逐字為 **`R1 Low Wired AUX Cameras`**（`NRL-188152`），與 §27 之 `R1 High Wired &Wireless Auxiliary Cameras`（`NRL-188027`）成對 —— 兩章之差別為 **HU 等級**（R1 Low 只有有線 AUX；§27.3.1 逐字 `Technical hardware requirements – (R1 High only due to architecture)`）。HU 等級**無 PROXI 編碼** —— 掃描字串 `Radio_Type`／`Trim_Level`／`Head_Unit_Type`／`Infotainment_Level`／`R1_Low`／`Uconnect` 於六本各 0 命中，故依下放包 §2 **不以此判車型**，前提以散文書寫（profile §7.3）。`always` 之驗法同 `-052`（兩個檔位）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. A wired AUX camera is connected
6. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
7. The shift lever is in P
8. The AUX camera list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the AUX camera list and check that the AUX entry is selectable
2. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
3. Read the AUX camera list and check that the AUX entry is still selectable
```

## expected_result

```
1. The AUX entry is selectable while the gear is P
2. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
3. The AUX entry is still selectable while the gear is R
```
