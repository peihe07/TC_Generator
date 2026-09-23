# NR1L-RVC-163 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1925`（來源列 `SYS-RA-VF551_V2-442`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI PAM_Tuning_Set value to the LVDS signal: vehicleUpdate_2.PAM_Tuning_Set

## reasoning

驗證目標為 `SYS-RA-VF551_V2-442` 之「HU 將 PROXI `PAM_Tuning_Set` 之值 gate 至 LVDS `vehicleUpdate_2.PAM_Tuning_Set`」。PROXI byte 104 bit 0–2（`HDCC28_ATL_HI` row 460 實測 `1=Base`）。**PROXI 值 ↔ LVDS 值之對照表於 V2 本查無**，ER 只驗「該 LVDS 訊號反映該 PROXI 值」（同 `-136`／`-137`／`-091` 之處置，DECISIONS 6-25）；本參數無 Atl-Mi 對應條文。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI PAM_Tuning_Set = 1 (Base)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_2.PAM_Tuning_Set and check that it reports the PROXI value
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_2.PAM_Tuning_Set reports the PROXI value and is sent over LVDS
```
