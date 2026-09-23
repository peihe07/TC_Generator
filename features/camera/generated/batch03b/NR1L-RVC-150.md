# NR1L-RVC-150 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_616`（來源列 `SYS-RA-VF551_V2-461`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate FD-CAN8 BRAKE_FD_2.VehicleSpeedVSOSig to LVDS vehicleUpdate_2.VehicleSpeedVSOSig

## reasoning

驗證目標為 `SYS-RA-VF551_V2-461` 之「HU 將 FD-CAN8 `BRAKE_FD_2.VehicleSpeedVSOSig` gate 至 LVDS `vehicleUpdate_2.VehicleSpeedVSOSig`」。供試 raw 205 = 12.8125 km/h（factor (0.0625,0) "Km/h"，`BO_ 258`）。缺失側由 `NR1L-RVC-151` 承接。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h)
2. Read vehicleUpdate_2.VehicleSpeedVSOSig and check that it reports the value sent in step 1
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 205 (12.8125 km/h) is sent
2. vehicleUpdate_2.VehicleSpeedVSOSig reports the same value and is sent over LVDS
```
