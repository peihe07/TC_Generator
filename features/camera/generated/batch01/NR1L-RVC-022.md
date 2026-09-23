# NR1L-RVC-022 — SWE-CAM-015

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1442`（來源列 `SYS-RA-VF551_V2-533`）

## test_item 上半（verbatim，SYS2 逐字）

> When ShiftLeverPosition = R, button presses and other events shall not interrupt the Rear Camera Image.

## reasoning

驗證目標為 SYS-RA-VF551_V2-533 之 a) 子句「When ShiftLeverPosition = R, button presses and other events shall not interrupt the Rear Camera Image」。上半為該 a) 子句之摘句（15 RE_TOKEN），主句由 NR1L-RVC-021 承接。以 Menu Bar 之 "Apps" 鍵為按鍵事件之代表 —— 其為 §5.8 之固定入口，label 有 Menu Bar §4.1 naming table 為據。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed in Automatic Display Mode
4. The shift lever is in R
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. The press is registered but no screen change is applied over the camera image
2. The rear view camera image stays displayed without interruption
```
