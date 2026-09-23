# NR1L-RVC-140 — SWE-CAM-010

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_1102`（來源列 `SYS-RA-VF551_V3-286`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate PROXI Wheelbase to LVDS vehicleUpdate_1.VC_WHL_BASE_LENGTH a) The Head Unit shall send LVDS vehicleUpdate_1.VC_WHL_BASE_LENGTH= [Not_Used] when PROXI Wheelbase = [Invalid]. b) The Head Unit shall send LVDS vehicleUpdate_1.VC_WHL_BASE_LENGTH= [Length_1] when PROXI Wheelbase = [2532].

## reasoning

驗證目標為 `SYS-RA-VF551_V3-286` 之 `b)` 分支。原句 39 token，未逾 50，主句與兩個子句一併保留（兩分支之 TC 共用同一上半，以括號下半區分，形制同 batch01 之 `NR1L-RVC-017`／`-018`）。`Fastback_ATL_MI` row 327 之列舉 `1 = 2532mm` 與來源之 `[2532]` **逐字相符**。依 **R-CAM15(b)**，V42（637）於本驗證點有對應條文（`V42-326`），故 V3 列只承 376。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Wheelbase = 1 (2532mm)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_WHL_BASE_LENGTH and check that it is Length_1
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_WHL_BASE_LENGTH = Length_1 is sent over LVDS
```
