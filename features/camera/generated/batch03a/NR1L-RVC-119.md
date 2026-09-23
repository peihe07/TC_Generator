# NR1L-RVC-119 — SWE-CAM-008

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1728`（來源列 `SYS-RA-VF551_V2-450`）

## test_item 上半（verbatim，SYS2 逐字）

> a. When IPC_VEHICLE_SETUP.DynamicGrid is missing OR until received during wake up, the HU shall set LVDS gridZoomRequest.DynamicGridRQSts = Default.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-450` 之「`IPC_VEHICLE_SETUP.DynamicGrid` 缺席，或喚醒期間尚未收到時，HU 送 `DynamicGridRQSts = Default`」。「缺席」以**停送該訊息**表達（Pre-Condition 4），「喚醒期間尚未收到」以開機後之讀取表達 ——二者於本列同時成立，為來源之 `OR` 兩支之交集，一次觀察即可判（§5.7）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字為來源之子句編號 `a.`；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
4. IPC_VEHICLE_SETUP is not transmitted on the bus
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
2. Read gridZoomRequest.DynamicGridRQSts and check that it is Default
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
2. gridZoomRequest.DynamicGridRQSts = Default is sent over LVDS
```
