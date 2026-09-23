# NR1L-RVC-166 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_624`（來源列 `SYS-RA-VF551_V3-285`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI Steering_Ratio_Rack_Pinion_Type to LVDS vehicleUpdate_2.VC_Steering_Cfactor a) The Head Unit shall send LVDS vehicleUpdate_2.VC_Steering_Cfactor = [Type_1] when PROXI Steering_Ratio_Rack_Pinion_Type = [15.5].

## reasoning

驗證目標為 `SYS-RA-VF551_V3-285` 主句之 gating 於 **`[15.5]` 以外之值**仍成立。**來源只給一個對映**（`a)` 之 `[15.5]` → `[Type_1]`），其餘值之對照**無來源**；ER 因而只判「不為 `Type_1`」而不指定應為何值（§8.4.1 不自造）。本列與 `-165` 成一對，使 `a)` 之條件side與否定side皆有覆蓋。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Steering_Ratio_Rack_Pinion_Type is not 15.5
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_2.VC_Steering_Cfactor and check that it is not Type_1
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_2.VC_Steering_Cfactor is not Type_1 and is sent over LVDS
```
