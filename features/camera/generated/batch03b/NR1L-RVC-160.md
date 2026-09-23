# NR1L-RVC-160 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_613`（來源列 `SYS-RA-VF551_V2-453`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate FD-CAN8 ASCM_FD_2.ASCM_Stat to LVDS vehicleUpdate_2.ASCM_Stat

## reasoning

驗證目標為 `SYS-RA-VF551_V2-453` 之「HU 將 FD-CAN8 `ASCM_FD_2.ASCM_Stat` gate 至 LVDS」。供試值取 `VAL_ 1445 ASCM_Stat … 2 "PARK"`（`ASCM_FD_2`，FDCAN8）。該訊號之存在前提為 PROXI `CAN node 27 (ASM/ASCM) = 1 (Present)`（見 `NR1L-RVC-138`）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
1. Send CAN: ASCM_FD_2.ASCM_Stat = 2 (PARK)
2. Read vehicleUpdate_2.ASCM_Stat and check that it reports the value sent in step 1
```

## expected_result

```
1. ASCM_FD_2.ASCM_Stat = 2 (PARK) is sent
2. vehicleUpdate_2.ASCM_Stat reports the same value and is sent over LVDS
```
