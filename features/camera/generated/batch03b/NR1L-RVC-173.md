# NR1L-RVC-173 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V3_P363_VF_613`（來源列 `SYS-RA-VF551_V3-283`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate BH-CAN STATUS_CCAN4.ReverseGearSts to LVDS vehicleUpdate_2.ReverseGearSts a) The Head Unit shall send LVDS STATUS_CCAN4.ReverseGearSts = [SNA] when BH-CAN STATUS_CCAN4.ReverseGearSts is missing.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-283` 主句之「HU 將 BH-CAN `STATUS_CCAN4.ReverseGearSts` gate 至 LVDS `vehicleUpdate_2.ReverseGearSts`」。供試值取 P363 DBC 之實測（`STATUS_CCAN4`）。依 R-CAM15(b)，V3 列只承 376。**來源之 `a)` 子句標的誤植**（RDF-09）—— 寫 `send LVDS STATUS_CCAN4.ReverseGearSts = [SNA]`；主句之 `vehicleUpdate_2.ReverseGearSts` 為正確標的。verbatim 逐字不改，**ER 以主句之標的書寫**（CAM-09 審閱 §一-6）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read vehicleUpdate_2.ReverseGearSts and check that it reports the value sent in step 1
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent
2. vehicleUpdate_2.ReverseGearSts reports the same value and is sent over LVDS
```
