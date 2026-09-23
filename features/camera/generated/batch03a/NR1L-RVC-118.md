# NR1L-RVC-118 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1046`（來源列 `SYS-RA-VF551_V2-451`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate the value of the FD-CAN8 IPC_VEHICLE_SETUP.DynamicGrid to LVDS gridZoomRequest.DynamicGridRQSts

## reasoning

驗證目標為 `SYS-RA-VF551_V2-451` 之「HU 將 FD-CAN8 `IPC_VEHICLE_SETUP.DynamicGrid` 之值 gate 至 LVDS `gridZoomRequest.DynamicGridRQSts`」。**CAN 側可逐字書寫**：`IPC_VEHICLE_SETUP`（`BO_ 1443`，`forms/PDT27_E2A_R1_FDCAN8.dbc`）之 `VAL_ … 0 "Dynamic Gridlines OFF" 1 "Dynamic Gridlines ON"`（§8.7.5(c)）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。本列驗 gating 之成立（值傳遞）；其兩個極端值之分支與 default／SNA 之規則分別由 `-119`～`-121` 與 Atl-Mi 之 `-124`～`-127` 承接。

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
2. gridZoomRequest.DynamicGridRQSts = ON is sent over LVDS to the RVCM
```
