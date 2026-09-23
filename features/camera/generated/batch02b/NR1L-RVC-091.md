# NR1L-RVC-091 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_1792`（來源列 `SYS-RA-VF551_V42-322`）

## test_item 上半（verbatim，SYS2 逐字）

> Gear_Box_Type to vehicleUpdate_1.VC_Trans_Equipped

## reasoning

驗證目標為 `SYS-RA-VF551_V42-322` 之「`Gear_Box_Type` gating 至 `vehicleUpdate_1.VC_Trans_Equipped`」。**來源僅三 token、無等式**（逐字即 `Gear_Box_Type to vehicleUpdate_1.VC_Trans_Equipped`），故 ER 只驗「該 LVDS 訊號反映該 PROXI 值」而不寫具體對映 —— **PROXI 值 ↔ LVDS 值之對照表於 SYS2 查無**，不自造（§8.4.1）。供試值取 `Promaster_ATL_MI` row 447 之實測 `Gear_Box_Type = 1`，其列舉首項為 `1 = MTX`（同列 `I` 欄）。依 R-CAM15(c)，V42 列承 637。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Gear_Box_Type = 1 (MTX)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_Trans_Equipped and check that it reports the PROXI Gear_Box_Type value
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_Trans_Equipped reports the PROXI Gear_Box_Type value and is sent over LVDS
```
