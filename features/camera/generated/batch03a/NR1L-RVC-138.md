# NR1L-RVC-138 — SWE-CAM-010

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_630`（來源列 `SYS-RA-VF551_V2-445`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI CAN node 27 (ASM/ASCM) value to LVDS vehicleUpdate_1.NetCfg_ASCM

## reasoning

驗證目標為 `SYS-RA-VF551_V2-445` 之「HU 將 PROXI `CAN node 27 (ASM/ASCM)` 之值 gate 至 LVDS `vehicleUpdate_1.NetCfg_ASCM`」。**CAM-11 §2 查證結果**：`CAN node 27 (ASM/ASCM)` **確為 PROXI 表之參數名**（byte 29 bit 3）——`HDCC28_ATL_HI` 與 `DT28_ATL_HI` row 32 實測 `1=Present`、`HDCC27_initial` row 32 `0=Absent`；來源之措辭與 PROXI 表之參數名**逐字相符**。Pre-Condition 因而改寫為 `PROXI CAN node 27 (ASM/ASCM) = 1 (Present)`，**不需 PENDING**（CAM-10 審閱 §一-6 之退回已解）。**PROXI 值 ↔ LVDS 值之對照表於 SYS2 查無**，故 ER 只驗「該 LVDS 訊號反映該 PROXI 值」而不寫具體對映（同 `NR1L-RVC-091` 之處置，DECISIONS 6-25）。Atl-Mi 之對應：`Wheelbase` 由 `-139`／`-140`（V3）與 `-145`／`-146`（V42）承接，其來源**有**逐值對照故可寫具體值。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CAN node 27 (ASM/ASCM) = 1 (Present)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.NetCfg_ASCM and check that it reports the PROXI value
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.NetCfg_ASCM reports the PROXI value and is sent over LVDS
```
