# NR1L-RVC-092 — SWE-CAM-005

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V3_P363_VF_522`（來源列 `SYS-RA-VF551_V3-254`）

## test_item 上半（verbatim，SYS2 逐字）

> · The RVCM image resolution is 1280 x 800 pixels and refer to HMI and PDO for the aspect ratio.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-254` 之「RVCM 影像解析度為 1280 x 800 像素」。**解析度可判**（來源有原文值）；**格式面不可判** —— 下放包 §3 令「EVS HAL 支援之影像格式」亦為本列之驗證點，惟該資訊於 SYS2 全本查無（`-005` 之另一來源 `SYS-RA-VF617_V5-183` 屬 DR-CAM-a 缺件），037 之 Description 雖提及 `physical image format` 但 **037 不作 literal 來源**（RDF-04 之同理），故格式面標 `PENDING: DR-CAM-m`，不採 037 值。來源末之 `refer to HMI and PDO for the aspect ratio` 為轉指，PDO 不在素材，不入 ER（§8.4.2）。觀察手段沿 pilot02 `NR1L-RVC-002` 已用之 `dumpsys media.camera` 兩行式（§5.4）。依 R-CAM15(a)（V42／V33 無對應條文）承三個 Atl-Mi 平台。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-m the image formats supported by the EVS HAL are not sourced in SYS2
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read the camera stream properties and check the resolution
   $ adb shell dumpsys media.camera
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
2. The RVCM image resolution is 1280 x 800 pixels
```
