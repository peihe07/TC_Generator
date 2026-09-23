# NR1L-RVC-084 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_563`（來源列 `SYS-RA-VF551_V3-257`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall transmit current display status using RADIO_B2.TGW_CAMERA_DISP_STAT. b) The head unit shall transmit RADIO_B2.TGW_CAMERA_DISP_STAT = [DISP_NON_CAMERA] AND vehicleUpdate_1.TGW_CAMERA_DISP_STAT = [DISP_NON_CAMERA] when none of the cameras are active on the Radio display (No camera display).

## reasoning

驗證目標為 `SYS-RA-VF551_V3-257` 之 `b)` 分支（無任何相機於 Radio 畫面啟用）。上半為摘句（§4.3.1）：原句 60 token 逾 50，刪另一分支之子句後為 38 token，為原句之保序子序列，主句（以 `RADIO_B2.TGW_CAMERA_DISP_STAT` 送現況）與本分支之條件／結果皆保留。**`RADIO_B2` 實測為 `BO_ 1282`**（P363 與 637MCA 兩本），其 `TGW_CAMERA_DISP_STAT` 之 `VAL_` 與 Atl-Hi 側同值域（`0 DISP_NON_CAMERA`／`1 DISP_DIGITAL_RVC_CAMERA`），CAN 側因而寫 `<raw> (<label>)`；依 **R-CAM15(a)**（V42／V33 於本驗證點無對應條文）本列承 637／2261／376 三平台。Atl-Hi 側之對應為 `TELEMATIC_FD_14`（`-080`／`-081`），訊息名與母體皆異，故拆列。LVDS 之 `vehicleUpdate_*`／`gridZoomRequest`／`PowerShutDownNotifcation` 非 CAN 訊號（四本 DBC 零命中），觀察以 bus analyzer 於 HU ↔ RVCM 之 LVDS 鏈路進行；**不造命令**（交付語料 17 本之 275 條 `$ ` 命令行中與 LVDS 相關者為 0，A-CA27 加註）。

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
2. Read RADIO_B2.TGW_CAMERA_DISP_STAT and check that it is 0 (DISP_NON_CAMERA)
3. Read vehicleUpdate_1.TGW_CAMERA_DISP_STAT and check that it is DISP_NON_CAMERA
```

## expected_result

```
1. The rear view camera image is closed
2. RADIO_B2.TGW_CAMERA_DISP_STAT = 0 (DISP_NON_CAMERA) is sent
3. vehicleUpdate_1.TGW_CAMERA_DISP_STAT = DISP_NON_CAMERA is sent over LVDS
```
