# NR1L-RVC-170 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_615`（來源列 `SYS-RA-VF551_V3-281`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate BH-CAN STATUS_CCAN5.LWSAngle to LVDS STATUS_CCAN5.LWSAngle a) The Head Unit shall send LVDS vehicleUpdate_2.LwsAngle = [SNA] when BH-CAN STATUS_CCAN3.VehicleSpeedVSOSig is missing.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-281` 之 `a)` 子句（缺失 → `SNA`）。「訊號缺失」以**停送該 CAN 訊息**表達（下放包 §3）—— 逾時門檻之值於來源未載，**不造**（§8.4.1），ER 只判 SNA 之出現而不判其時限。**來源之主句標的誤植**（RDF-08）—— 寫 `to LVDS STATUS_CCAN5.LWSAngle`（即來源訊號自身）；其 `a)` 子句作 `vehicleUpdate_2.LwsAngle` 為正確標的。verbatim 逐字不改，**ER 以 `a)` 子句之正確標的書寫**（CAM-09 審閱 §一-6）。其 `a)` 子句之**條件訊號**亦寫 `STATUS_CCAN3.VehicleSpeedVSOSig is missing`（與主句不同訊號），本包判為第二處誤植，缺失側之 procedure 以**主句之訊號**（`STATUS_CCAN5`）停送，已於 RDF-08 具名。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。【CAM-12 §2】**procedure 改依來源逐字** —— `a)` 子句之條件為 `when BH-CAN STATUS_CCAN3.VehicleSpeedVSOSig is missing`，CAM-11 判其為誤植而改停送 `STATUS_CCAN5`，違 §8.1／§8.4.1「TC 依來源逐字，不得以判讀代換觸發」（CAM-11 審閱 §二-2）。本輪改回停送 **`STATUS_CCAN3`**。該疑似誤植仍登 RDF-08，工作簿 `Remarks` 具名。**`STATUS_CCAN5` 缺失 → `LwsAngle = SNA` 之行為無逐字來源，不生成**，待 RDF-08 回覆。

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
2. Read vehicleUpdate_2.LwsAngle and check that it is SNA
```

## expected_result

```
1. STATUS_CCAN3 is no longer received by the HU
2. vehicleUpdate_2.LwsAngle = SNA is sent over LVDS
```

## remarks

Condition per source text; suspected typo, see RDF-08
