# NR1L-RVC-224 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V3_P363_VF_520`（來源列 `SYS-RA-VF551_V3-255`）

## test_item 上半（verbatim，SYS2 逐字）

> · No display blanking or flicker shall occur while Head Unit is displaying RVC image and during the display transitions between RVC image and non camera modes.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-255` 之「顯示 RVC 影像期間與其切換之間，不得有畫面變黑或閃爍」。**Atl-Mi 本將兩性質寫成一句**（V2 分為 `-523` 閃爍／`-524` 變黑兩列，由 `NR1L-RVC-104`／`-105` 承接），故本列以一列兩情境承之，ER 四項（§5.7）。依 **R-CAM15(b)**：V42 於本驗證點無對應條文、V33 亦無，**惟 V4 有 `-121`／`-122`（HDCC27 之類比側）**，故 V3 列承其母體 376。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read the HU display while the rear view camera image is shown and check for blanking and flicker
3. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
4. Read the HU display during the transition back to the non-camera display and check for blanking and flicker
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
2. Neither blanking nor flicker occurs while the RVC image is displayed
3. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent and the rear view camera image is closed
4. Neither blanking nor flicker occurs during the transition between RVC and non camera modes
```
