# NR1L-RVC-175 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2020`（來源列 `SYS-RA-VF551_V42-308`）

## test_item 上半（verbatim，SYS2 逐字）

> - IF the LTM does not receive the signal TRANSM2.ShiftLeverPosition, LTM shall send LVDS vehicleUpdate_2.ShiftLeverPosition equal to "SNA".

## reasoning

驗證目標為 `SYS-RA-VF551_V42-308` 之「LTM 未收到 `TRANSM2` 時，LVDS 側送 `SNA`」。**`TRANSM2` 不在 `forms/` 四本 DBC**（A-CA23／DR-CAM-f）；停送之動作不需知其 raw，ER 仍可判。「訊號缺失」以**停送該 CAN 訊息**表達（下放包 §3）—— 逾時門檻之值於來源未載，**不造**（§8.4.1），ER 只判 SNA 之出現而不判其時限。依 R-CAM15(c)，V42 列承 637。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-f the TRANSM2 message is not present in the four DBC files in forms
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Stop transmitting TRANSM2 on the bus
2. Read vehicleUpdate_2.ShiftLeverPosition and check that it is SNA
```

## expected_result

```
1. TRANSM2 is no longer received by the LTM
2. vehicleUpdate_2.ShiftLeverPosition = SNA is sent over LVDS
```
