# NR1L-RVC-067 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_2336`（來源列 `SYS-RA-VF551_V42-221`）

## test_item 上半（verbatim，SYS2 逐字）

> The user can select Rear_Camera_DelayOff.Req value equal to "ON" or "OFF".

## reasoning

驗證目標為 `SYS-RA-VF551_V42-221` 之「使用者可將 `Rear_Camera_DelayOff.Req` 選為 `"ON"` 或 `"OFF"`」—— 即該設定項之**可操作性**（兩值皆可選），非其生效行為（生效由 `NR1L-RVC-015`／`-016` 與 `-066` 承接，§8.2.1）。label 取 `HMI Settings List` `Settings` 分頁 row 467 之基礎 label `Rear View Camera Delay*`；`*` 不入 hop（R-CAM5(a)），依 `Brand-Specific Names` 取值 —— 637 之 `Brand_Configuration_2 = 11 (RAM)`（R-CAM5(c)′），RAM 欄之逐字 label 為 **`ParkView Backup Camera Delay`**（`features/camera/data/brand_labels.tsv` row 467，`Jeep / Chrysler / Ram / Dodge` 欄）。本列只勾 637，品牌分支單一，故 Pre-Condition 依 R-CAM5(e) 寫 Ram 而不另拆 sibling。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The vehicle brand is Ram (HDCC27, DT27, 637)
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Set "ParkView Backup Camera Delay" = "On"
5. Set "ParkView Backup Camera Delay" = "Off"
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" settings screen is displayed
4. The "ParkView Backup Camera Delay" setting is set to "On"
5. The "ParkView Backup Camera Delay" setting is set to "Off"
```
