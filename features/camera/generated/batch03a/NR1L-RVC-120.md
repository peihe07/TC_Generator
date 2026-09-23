# NR1L-RVC-120 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1666`（來源列 `SYS-RA-VF551_V2-477`）

## test_item 上半（verbatim，SYS2 逐字）

> · The HU shall never send gridZoomRequest.DynamicGridRQSts = [SNA] to RVCM.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-477` 之「HU 永不送 `DynamicGridRQSts = [SNA]` 給 RVCM」。**negative 之可判化**：`never` 無法以單點觀察證否，故 procedure 走過**會使 SNA 出現之三種情境**（兩個有效值 ＋ 來源訊息缺席），再以整段錄製檢查 SNA 未出現（§6）。`SYS-RA-VF551_V2-449`（`b.` 子句，逐字近同）為同一驗證點，依同義列不另出 TC，plan 記 covered_by。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
1. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 0 (Dynamic Gridlines OFF)
2. Send CAN: IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON)
3. Stop transmitting IPC_VEHICLE_SETUP
4. Read the whole recording of gridZoomRequest.DynamicGridRQSts and check that SNA never appears
```

## expected_result

```
1. IPC_VEHICLE_SETUP.DynamicGrid = 0 (Dynamic Gridlines OFF) is sent
2. IPC_VEHICLE_SETUP.DynamicGrid = 1 (Dynamic Gridlines ON) is sent
3. IPC_VEHICLE_SETUP is no longer transmitted
4. gridZoomRequest.DynamicGridRQSts is never sent as SNA in the whole recording
```
