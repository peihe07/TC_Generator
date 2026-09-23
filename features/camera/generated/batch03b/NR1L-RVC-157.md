# NR1L-RVC-157 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_2036`（來源列 `SYS-RA-VF551_V2-456`）

## test_item 上半（verbatim，SYS2 逐字）

> a. The Head Unit sends LVDS vehicleUpdate_2.ShiftLeverPosition = SNA when FD-CAN8 TRANSM_FD_4.ShiftLeverPosition is missing and Hybrid_Type != "Range Electric Paradigm Breaker" OR "Fuel Cell Electric Vehicle".

## reasoning

驗證目標為 `SYS-RA-VF551_V2-456` 之缺失側（非 hybrid 分支），與 `-156` 成一對。「訊號缺失」以**停送該 CAN 訊息**表達（下放包 §3）—— 逾時門檻之值於來源未載，**不造**（§8.4.1），ER 只判 SNA 之出現而不判其時限。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字為來源之子句編號 `a.`；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

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
1. Stop transmitting TRANSM_FD_4 on the bus
2. Read vehicleUpdate_2.ShiftLeverPosition and check that it is SNA
```

## expected_result

```
1. TRANSM_FD_4 is no longer received by the HU
2. vehicleUpdate_2.ShiftLeverPosition = SNA is sent over LVDS
```
