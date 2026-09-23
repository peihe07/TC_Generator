# NR1L-RVC-171 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V3_P363_VF_614`（來源列 `SYS-RA-VF551_V3-282`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate BH-CAN STATUS_CCAN5.ShiftLeverPosition to LVDS vehicleUpdate_2.ShiftLeverPosition a) The Head Unit shall send LVDS vehicleUpdate_2.ShiftLeverPosition = [SNA] when BH-CAN STATUS_CCAN5.ShiftLeverPosition is missing.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-282` 主句之「HU 將 BH-CAN `STATUS_CCAN5.ShiftLeverPosition` gate 至 LVDS `vehicleUpdate_2.ShiftLeverPosition`」。供試值取 P363 DBC 之實測（`STATUS_CCAN5`）。依 R-CAM15(b)，V3 列只承 376。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
1. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 2 (R)
2. Read vehicleUpdate_2.ShiftLeverPosition and check that it reports the value sent in step 1
```

## expected_result

```
1. STATUS_CCAN5.ShiftLeverPosition = 2 (R) is sent
2. vehicleUpdate_2.ShiftLeverPosition reports the same value and is sent over LVDS
```
