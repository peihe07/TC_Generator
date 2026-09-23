# NR1L-RVC-127 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V3_P363_VF_1046`（來源列 `SYS-RA-VF551_V3-284`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall gate BH-CAN IPC_VEHICLE_SETUP.DynamicGrid to LVDS gridZoomRequest.DynamicGridRQSts d) The Head Unit shall never send LVDS gridZoomRequest.DynamicGridRQSts = [SNA] to RVCM.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-284` 之 `d)` 分支（Atl-Mi 之 never-SNA 規則），與 Atl-Hi 之 `NR1L-RVC-120`（`V2-477`）同型而本不同。摘句 78 → 24 token。negative 之可判化同 `-120`。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

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
