# NR1L-RVC-168 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_616`（來源列 `SYS-RA-VF551_V3-280`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate BH-CAN STATUS_CCAN3.VehicleSpeedVSOSig to LVDS vehicleUpdate_2.VehicleSpeedVSOSig a) The Head Unit shall send LVDS vehicleUpdate_2.VehicleSpeedVSOSig = [SNA] when BH-CAN STATUS_CCAN3.VehicleSpeedVSOSig is missing

## reasoning

驗證目標為 `SYS-RA-VF551_V3-280` 之 `a)` 子句（缺失 → `SNA`）。「訊號缺失」以**停送該 CAN 訊息**表達（下放包 §3）—— 逾時門檻之值於來源未載，**不造**（§8.4.1），ER 只判 SNA 之出現而不判其時限。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
1. Stop transmitting STATUS_CCAN3 on the bus
2. Read vehicleUpdate_2.VehicleSpeedVSOSig and check that it is SNA
```

## expected_result

```
1. STATUS_CCAN3 is no longer received by the HU
2. vehicleUpdate_2.VehicleSpeedVSOSig = SNA is sent over LVDS
```
