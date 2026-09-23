# NR1L-RVC-048 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Additional Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781653`（來源列 `SYS-RA-CAM-088`）

## test_item 上半（verbatim，SYS2 逐字）

> The default setting for the Surround View camera shall be OFF.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-088`（ObjectID 4781653，**Surround View Camera 節**）之「Surround View 相機之預設設定為 OFF」。**Test Set 為 `Additional Cameras`**（R-CAM13(c)）—— 本列雖為 `SWE-CAM-001` 所引，其來源屬 SVC 節，依節別歸組；framework VIII.2 之四列供稿表已含本列。導航取 R-CAM8 之 `ENTER_CAMERA_SETTINGS` 三 hop（`HMI Settings List` `Settings` 分頁 row 464 `13. Camera`）；Surround View 之設定項見同分頁 row 465 `Surround View Camera Delay` 與 row 466 `Surround View Camera Guidelines`，**惟來源只講「預設為 OFF」而未指名哪一項**，ER 因而以「Surround View camera setting is off」書寫而不指定 label（§8.4.1 不自造）。「預設」以 factory default 之前提表達（Pre-Condition 3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. The HU has been restored to its factory default settings
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Read the "Camera" settings screen and check the default state of the Surround View camera setting
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" settings screen is displayed
4. The Surround View camera setting is off
```
