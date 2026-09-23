# NR1L-RVC-156 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_2035`（來源列 `SYS-RA-VF551_V2-457`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate FD-CAN8 TRANSM_FD_4.ShiftLeverPosition to LVDS vehicleUpdate_2.ShiftLeverPosition when Hybrid_Type != "Range Electric Paradigm Breaker" OR "Fuel Cell Electric Vehicle"

## reasoning

驗證目標為 `SYS-RA-VF551_V2-457` 之「`Hybrid_Type` 非 REPB／FCEV 時，HU 將 `TRANSM_FD_4.ShiftLeverPosition` gate 至 LVDS」。供試值取 `VAL_ 1450 … 2 "R"`（`TRANSM_FD_4`）。**hybrid 分支（`V2-455`／`-454`）不生成** —— `PT_SYSTEM_FD_1.ShiftLeverPosition_PT` 不可注入（A-CA15），plan 已記。**只勾 HDCC27** —— DT27 之同一行為其來源為 `V2-747`（`-158`），兩者之 hybrid 列舉相異（FCEV vs BEV）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read vehicleUpdate_2.ShiftLeverPosition and check that it reports the value sent in step 1
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. vehicleUpdate_2.ShiftLeverPosition reports the same value and is sent over LVDS
```
