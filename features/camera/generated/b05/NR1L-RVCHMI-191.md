# NR1L-RVCHMI-191 — SWE1-RVC-006

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.5`（來源列 `NRL-142611`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM5) Audible indications will follow Parksense logic and flow and will be provided for the Head Unit by the CAN

## reasoning

§6.5 之 `provided for the Head Unit by the CAN` 即本列之驗證點 —— 以 CAN 驅動並觀察 HU 出聲。raw 與 label 取 `Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc` 之 `VAL_ … PAMSystemSts 0 "OFF" 1 "ON_Active" 2 "ON_Inactive" 3 "ON_Disabled"`。`follow Parksense logic and flow` 轉指外部規格，依 §8.4.2 不測其內容。該列之兩個 `*` 註（`ARCs presence are subject to vehicle feature availability`／`Only applies if driving tube feature is present`）為圖之腳註，其圖不可抽，依 **DECISIONS 6-69** 不造其內容。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. CAN source: BCM_FD_12.PAMRequestSts (HDCC27, DT27) / STATUS_PAM.PAMSystemSts (637, 2261, 376)
5. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_PAM.PAMSystemSts = 1 (ON_Active)
2. Listen to the HU speakers and check that the PAM chime is produced
3. Send CAN: STATUS_PAM.PAMSystemSts = 0 (OFF)
4. Listen to the HU speakers and check that the PAM chime has stopped
```

## expected_result

```
1. STATUS_PAM.PAMSystemSts = 1 (ON_Active) is sent
2. The PAM chime is produced by the HU speakers
3. STATUS_PAM.PAMSystemSts = 0 (OFF) is sent
4. The PAM chime has stopped
```
