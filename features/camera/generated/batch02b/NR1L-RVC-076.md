# NR1L-RVC-076 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_629`（來源列 `SYS-RA-VF551_V3-287`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI Vehicle_Line_Configuration to LVDS vehicleUpdate_1.VC_VehLineRVCM. a) The Head Unit shall send LVDS vehicleUpdate_1.VC_VehLineRVCM = [VEH_363] when PROXI Vehicle_Line_Configuration = [363]. b) The Head Unit shall send LVDS vehicleUpdate_1.VC_VehLineRVCM = [VEH_376] when PROXI Vehicle_Line_Configuration = [376].

## reasoning

驗證目標為 `SYS-RA-VF551_V3-287` 之 `a)` 分支。主句（gating 之宣告）與兩個子句同屬一列，兩分支之 PROXI 值不同、ER 不同，依 §8.3 各出一 TC（`a)` 由本列承接）。`Vehicle_Line_Configuration` 為 PROXI byte 105 bit 0–7，各平台實測值：HDCC28 `130 = HDCC (82 Hex)`（row 465）、DT28 `124 = DT (7C hex)`（row 465）、Fastback `103 = 363 (67 Hex)`／清單另有 `111 = 376 (6F Hex)`（row 470）、Promaster `114 = 637MCA (72 Hex)`（row 470）。**只勾 376** —— 依 **R-CAM15(b)**，V42（637）於同一驗證點有對應條文（`V42-327`，`NR1L-RVC-078`），V33（2261）無 `VC_VehLineRVCM` 之條文，故 V3 列只承其母體 376；`363` 為同本之另一車系值，不在本 feature 之七欄內，只作 PROXI 供試值出現。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Vehicle_Line_Configuration = 103 (363 (67 Hex))
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_VehLineRVCM and check that it is VEH_363
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_VehLineRVCM = VEH_363 is sent over LVDS
```
