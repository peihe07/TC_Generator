# NR1L-RVC-078 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2024`（來源列 `SYS-RA-VF551_V42-327`）

## test_item 上半（verbatim，SYS2 逐字）

> The LTM shall gate and send the signal vehicleUpdate_1.VC_VehLineRVCM equal to [VEH_637MCA] when PROXI Vehicle_Line_Configuration is equal to [637MCA].

## reasoning

驗證目標為 `SYS-RA-VF551_V42-327` 之 637 分支。PROXI 值為 `Promaster_ATL_MI` row 470 之逐格實測 `114 = 637MCA (72 Hex)`，**與來源之 `[637MCA]` 逐字相符**。依 R-CAM15(c)，V42 列承 637。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Vehicle_Line_Configuration = 114 (637MCA (72 Hex))
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_VehLineRVCM and check that it is VEH_637MCA
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_VehLineRVCM = VEH_637MCA is sent over LVDS
```
