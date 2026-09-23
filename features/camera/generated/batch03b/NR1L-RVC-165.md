# NR1L-RVC-165 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_624`（來源列 `SYS-RA-VF551_V3-285`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI Steering_Ratio_Rack_Pinion_Type to LVDS vehicleUpdate_2.VC_Steering_Cfactor a) The Head Unit shall send LVDS vehicleUpdate_2.VC_Steering_Cfactor = [Type_1] when PROXI Steering_Ratio_Rack_Pinion_Type = [15.5].

## reasoning

驗證目標為 `SYS-RA-VF551_V3-285` 之 `a)` 分支（PROXI `[15.5]` → `[Type_1]`）。原句 26 token，未逾 50。PROXI 值依 §8.7.5(e) 取來源 label 逐字（該參數名於 Atl-Hi 三本 PROXI 掃描查無，376 本亦未逐格核出，故不寫 raw）。依 R-CAM15(b)，V3 列只承 376（Atl-Hi 之同一 gating 由 `-164` 承接）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Steering_Ratio_Rack_Pinion_Type = 15.5
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_2.VC_Steering_Cfactor and check that it is Type_1
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_2.VC_Steering_Cfactor = Type_1 is sent over LVDS
```
