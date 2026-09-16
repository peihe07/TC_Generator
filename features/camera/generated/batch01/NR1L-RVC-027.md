# NR1L-RVC-027 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P3｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_534`（來源列 `SYS-RA-VF551_V2-532`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall overlay Zoom soft button on Rear View Camera Image, Refer to Head Unit Zoom mode requirements.

## reasoning

驗證目標為 SYS-RA-VF551_V2-532 之「Head Unit 於 RVC 影像上疊加 Zoom 軟鍵」。Zoom 模式本身之行為該條逐字指向 Head Unit Zoom mode requirements（他文件），不在本 Test Set，本列只驗疊加之存在。V3-250／V4 之同義列依 R-CAM3(e) 不另拆。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Rear View Camera" in the App Drawer
3. Read the rear view camera image and check that the Zoom soft button is overlaid on it
```

## expected_result

```
1. The App Drawer is displayed
2. The rear view camera image is displayed in Manual Display Mode
3. The Zoom soft button is overlaid on the rear view camera image
```
