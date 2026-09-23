# NR1L-RVC-080 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1574`（來源列 `SYS-RA-VF551_V2-519`）

## test_item 上半（verbatim，SYS2 逐字）

> When none of the camera views are displayed on the Radio, then the head unit shall transmit following signals: - TELEMATIC_FD_14.TGW_CAMERA_DISP_STAT = DISP_NON_CAMERA - vehicleUpdate_1.TGW_CAMERA_DISP_STAT = DISP_NON_CAMERA.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-519` 之「無任何相機畫面時，CAN 與 LVDS 兩側之 `TGW_CAMERA_DISP_STAT` 皆送 `DISP_NON_CAMERA`」。**`TELEMATIC_FD_14` 只存在於 `forms/PDT27_E2A_R1_FDCAN8.dbc`**（Atl-Hi 側；其餘三本零命中），故本列只勾 Atl-Hi；Atl-Mi 之對應由 `SYS-RA-VF551_V3-257`（`RADIO_B2`，`NR1L-RVC-083`／`-084`）承接。`SYS-RA-VF551_V4-126` 與本列逐字近同（V4 只列 `TELEMATIC_FD_14` 一項），依同義列不另出 TC，plan 記 covered_by。**raw 值實測可書寫** —— `TELEMATIC_FD_14`（`BO_ 1465`，FDCAN8）之 `VAL_ … 0 "DISP_NON_CAMERA" 1 "DISP_DIGITAL_RVC_CAMERA" 2 "DISP_ANALOG_RVC_CAMERA" …`，CAN 側依 §8.7.5(d)／R-1 寫 `<raw> (<label>)`；LVDS 側之 `vehicleUpdate_1` 非 CAN，無 raw 可書，維持來源 label 逐字（§8.7.5(f)）。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。R-CAM3(f)：本列無 `Send CAN` 步，不寫 CAN source 行。

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
2. Read TELEMATIC_FD_14.TGW_CAMERA_DISP_STAT and check that it is 0 (DISP_NON_CAMERA)
3. Read vehicleUpdate_1.TGW_CAMERA_DISP_STAT and check that it is DISP_NON_CAMERA
```

## expected_result

```
1. No camera view is displayed on the HU
2. TELEMATIC_FD_14.TGW_CAMERA_DISP_STAT = 0 (DISP_NON_CAMERA) is sent
3. vehicleUpdate_1.TGW_CAMERA_DISP_STAT = DISP_NON_CAMERA is sent over LVDS
```
