# NR1L-RVC-144 — SWE-CAM-010

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2203`（來源列 `SYS-RA-VF551_V42-323`）

## test_item 上半（verbatim，SYS2 逐字）

> LTM shall send: - vehicleUpdate_1.VC_Trans_Equipped equal to "Automatic" IF the PROXI parameter Gear_Box_Type is different from "MTX" - vehicleUpdate_1.VC_Trans_Equipped equal to "Manual" IF the PROXI parameter Gear_Box_Type is equal to "MTX"

## reasoning

驗證目標為 `SYS-RA-VF551_V42-323` 之 `Manual` 分支（31 token，未逾 50，兩分支共用上半）。PROXI `Gear_Box_Type` 為 byte 101 bit 0–2，`Promaster_ATL_MI` row 447 之列舉含 `1 = MTX`；`!= "MTX"` 之代表值取 Atl-Hi 兩本所載之 `4 = ATX`（`HDCC28_ATL_HI` row 442）。**與 `NR1L-RVC-091`（`V42-322`）之分工**：`-322` 只宣告 gating 之存在（3 token、無等式），本二列驗其**具體對映**（`V42-323` 有逐值條文）—— 兩來源不同、可判性亦不同。依 R-CAM15(c)，V42 列承 637。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
2. Read vehicleUpdate_1.VC_Trans_Equipped and check that it is Manual
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_Trans_Equipped = Manual is sent over LVDS
```
