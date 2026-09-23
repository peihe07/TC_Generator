# NR1L-RVC-075 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PDT27_VF_629`（來源列 `SYS-RA-VF551_V2-751`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate and send vehicleUpdate_1.VC_VehLineRVCM = VEH_DT when PROXI Vehicle_Line_Configuration = DT.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-751` 之 DT 分支。其 anchor 為 **`VF551_V2_PDT27_VF_629`**（V2 本之 `PDT27` 前綴列），與 `-073`／`-074` 之 `PHDCC27` 前綴同本不同平台 —— 只勾 DT27。`Vehicle_Line_Configuration` 為 PROXI byte 105 bit 0–7，各平台實測值：HDCC28 `130 = HDCC (82 Hex)`（row 465）、DT28 `124 = DT (7C hex)`（row 465）、Fastback `103 = 363 (67 Hex)`／清單另有 `111 = 376 (6F Hex)`（row 470）、Promaster `114 = 637MCA (72 Hex)`（row 470）。本列之來源未載 `Body_Types` 條件，故不寫該前提（§8.4.1）。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Vehicle_Line_Configuration = 124 (DT (7C hex))
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Cycle the ignition to RUN so that the HU reads the PROXI configuration
2. Read vehicleUpdate_1.VC_VehLineRVCM and check that it is VEH_DT
```

## expected_result

```
1. The HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_VehLineRVCM = VEH_DT is sent over LVDS
```
