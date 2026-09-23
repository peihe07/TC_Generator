# NR1L-RVC-088 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1663`（來源列 `SYS-RA-VF551_V2-538`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall transmit the following signals on LVDS: - vehicleUpdate_2.VehicleSpeedVSOSig - vehicleUpdate_2.LwsAngle - vehicleUpdate_2.ShiftLeverPosition - vehicleUpdate_2.VC_Steering_Cfactor - vehicleUpdate_2.ZoomViewReq - vehicleUpdate_2.ASCM_Stat - vehicleUpdate_1.VC_VehLineRVCM - vehicleUpdate_1.NetCfg_ASCM - vehicleUpdate_1.TGW_CAMERA_DISP_STAT - gridZoomRequest.DynamicGridRQSts - PowerShutDownNotifcation.Power_Down - vehicleUpdate_1.VC_WHL_BASE_LENGTH - vehicleUpdate_1.VC_RR_DuallyPrsnt - vehicleUpdate_2.PAM_Tuning_Set

## reasoning

驗證目標為 `SYS-RA-VF551_V2-538` 之「HU 於 LVDS 送出所列之十四個訊號」——其為**清單完整性**之驗證點（表內該有的都在），非各訊號之值語意（值由各自之來源承接：`ZoomViewReq` → `-079`、`VC_VehLineRVCM` → `-073`～`-078`、`TGW_CAMERA_DISP_STAT` → `-080`／`-081`、`Power_Down` → `-069`／`-070`、`DynamicGridRQSts` → `SWE-CAM-008` 之 `gridZoomRequest` 線）。逐字之十四項已在 test_item 上半（39 token，未逾 50），ER 不重複列舉。只勾 Atl-Hi —— 來源為 V2 本且 Atl-Mi 三本無同型清單條文。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Record the LVDS link for at least one transmission cycle of each signal
2. Read the recording and check that each of the fourteen signals listed in the Test Item is present
```

## expected_result

```
1. The LVDS link is recorded
2. All fourteen listed signals are sent over LVDS by the HU
```
