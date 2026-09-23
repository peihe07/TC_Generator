# NR1L-RVC-047 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781647`（來源列 `SYS-RA-CAM-082`）

## test_item 上半（verbatim，SYS2 逐字）

> When the user presses the X on the top right corner of the HU screen, the HU shall receive the internal signal RVC IMAGE OFF and shall close the image of the rear area of the vehicle.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-082`（ObjectID 4781647，Rear Camera 節）之「按下右上角 X → HU 收到內部訊號 RVC IMAGE OFF → 關閉後方影像」。**內部訊號 `RVC IMAGE OFF` 不可觀察** —— `forms/` 四本 DBC 全文字面掃描 `RVC IMAGE` 零命中，其為 HU 內部事件，依 §6 以其後果（影像關閉）判定；寫法同 `NR1L-RVC-036` 之 `CHMC IMAGE ON`。**與 `NR1L-RVC-006`（pilot02，手動關閉）之分工**：`-006` 之錨為 `SYS-RA-VF551_V2-549`，承接列為 `SWE-CAM-016`；本列之錨 `CAM-082` 承接列為 `SWE-CAM-001`（R-CAM10），二者為不同來源之同型行為，各自承接、不互相委派。前提取 Manual Display Mode —— 自動模式下退出由排檔決定，X 鍵之疊加另見 `NR1L-RVC-021`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. The rear view camera image is displayed in Manual Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the top right corner of the HU display
2. Read the HU display and check that the rear view camera image is closed
```

## expected_result

```
1. The "X" exit button registers the press
2. The rear view camera image is closed and the HU returns to the previous screen
```
