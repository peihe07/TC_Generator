# NR1L-RVC-079 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_599`（來源列 `SYS-RA-VF551_V2-484`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall send vehicleUpdate_2.ZoomViewReq = Default when RVC display not active on the Radio: vehicleUpdate_1.TGW_CAMERA_DISP_STAT !=DISP_DIGITAL_RVC_CAMERA.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-484` 之「RVC 未於 Radio 顯示時送 `ZoomViewReq = Default`」。`SYS-RA-VF551_V3-270` 與本列**逐字同句**（Atl-Mi 本），依同義列不另出 TC；依 **R-CAM15(a)**（V42／V33 於本驗證點皆無對應條文），本列因而承全五車型，訊號名兩本相同（皆 LVDS `vehicleUpdate_2`），無 EE 分支。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

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
1. Press the "X" exit button on the top right corner of the HU display
2. Read vehicleUpdate_1.TGW_CAMERA_DISP_STAT and check that it is not DISP_DIGITAL_RVC_CAMERA
3. Read vehicleUpdate_2.ZoomViewReq and check that it is Default
```

## expected_result

```
1. The rear view camera image is closed
2. vehicleUpdate_1.TGW_CAMERA_DISP_STAT is not DISP_DIGITAL_RVC_CAMERA
3. vehicleUpdate_2.ZoomViewReq = Default is sent over LVDS
```
