# NR1L-RVC-164 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_624`（來源列 `SYS-RA-VF551_V2-448`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI Steering_Ratio_Rack_Pinion_Type to LVDS vehicleUpdate_2.VC_Steering_Cfactor

## reasoning

驗證目標為 `SYS-RA-VF551_V2-448` 之「HU 將 PROXI `Steering_Ratio_Rack_Pinion_Type` 之值 gate 至 LVDS `vehicleUpdate_2.VC_Steering_Cfactor`」。PROXI 表之參數名於 Atl-Hi 三本掃描查無（見上繳包 §3-3），Pre-Condition 依 §8.7.5(e) 以來源措辭逐字書寫。**PROXI 值 ↔ LVDS 值之對照表於 V2 本查無**，ER 只驗「該 LVDS 訊號反映該 PROXI 值」（同 `-136`／`-137`／`-091` 之處置，DECISIONS 6-25）；Atl-Mi 側之逐值對照由 `-165`／`-166`（`V3-285`）承接。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Steering_Ratio_Rack_Pinion_Type is configured
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_2.VC_Steering_Cfactor and check that it reports the PROXI value
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_2.VC_Steering_Cfactor reports the PROXI value and is sent over LVDS
```
