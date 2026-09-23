# NR1L-RVC-125 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_1046`（來源列 `SYS-RA-VF551_V3-284`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate BH-CAN IPC_VEHICLE_SETUP.DynamicGrid to LVDS gridZoomRequest.DynamicGridRQSts b) The Head Unit shall gate BH-CAN IPC_VEHICLE_SETUP.DynamicGrid = [Dynamic Gridlines ON] to LVDS gridZoomRequest.DynamicGridRQSts = [ON]

## reasoning

驗證目標為 `SYS-RA-VF551_V3-284` 之 `b)` 分支。上半為摘句（§4.3.1）：原句 78 token 逾 50，刪其餘三個子句後為 28 token，為原句之保序子序列，主句（gating 之宣告）與本分支之來源值與標的值皆保留。**CAN 側可逐字書寫**：376 之 `IPC_VEHICLE_SETUP` 為 `BO_ 1468`（`forms/P363_BH-CAN [07338]_3A_R2.dbc`），其 `VAL_` 與 Atl-Hi 之 `BO_ 1443` 同值域。依 **R-CAM15(b)**，V42（637）於本驗證點有對應條文（`V42-319`／`-320`），故 V3 列只承 376。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON)
2. Read gridZoomRequest.DynamicGridRQSts and check that it is ON
```

## expected_result

```
1. IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON) is sent
2. gridZoomRequest.DynamicGridRQSts = ON is sent over LVDS
```
