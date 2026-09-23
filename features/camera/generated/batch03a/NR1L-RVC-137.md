# NR1L-RVC-137 — SWE-CAM-010

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1232`（來源列 `SYS-RA-VF551_V2-444`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI Wheelbase to LVDS vehicleUpdate_1.VC_WHL_BASE_LENGTH

## reasoning

驗證目標為 `SYS-RA-VF551_V2-444` 之「HU 將 PROXI `Wheelbase` 之值 gate 至 LVDS `vehicleUpdate_1.VC_WHL_BASE_LENGTH`」。PROXI byte 71 bit 4–7（`HDCC28_ATL_HI` row 322 實測）。**PROXI 值 ↔ LVDS 值之對照表於 SYS2 查無**，故 ER 只驗「該 LVDS 訊號反映該 PROXI 值」而不寫具體對映（同 `NR1L-RVC-091` 之處置，DECISIONS 6-25）。Atl-Mi 之對應：`Wheelbase` 由 `-139`／`-140`（V3）與 `-145`／`-146`（V42）承接，其來源**有**逐值對照故可寫具體值。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Wheelbase = 1 (Type_2 (144.5 inch / Crew Cab 5’7” Box))
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_WHL_BASE_LENGTH and check that it reports the PROXI value
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_WHL_BASE_LENGTH reports the PROXI value and is sent over LVDS
```
