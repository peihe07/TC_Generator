# NR1L-RVCHMI-014 — SWE1-RVC-052

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.10.1`（來源列 `NRL-187356`）

## test_item 上半（verbatim，SYS1 逐字）

> When equipped, the following camera features will have access via a soft control in the corner of each of the equipped camera views

## reasoning

驗證目標為 §6.10.1 之「每個已配備之相機 view 角落皆有互通之 soft control」。§6.10 母題逐字為 `Non Surround View Vehicles access to Cameras:`，故前提取 `Surround_View_Camera = 0`。H 本 **§12.10.1.3** 逐字載 `Camera view Soft controls in top corner are only present in vehicles that do not have “Enhanced Camera App”`，與本條一致，故本列不掛 DR-CAM-r（配備方向為**否**，由 §6.10 母題承載）。已配備之組合取 RVC ＋ FFCTL（PROXI 實測六本中五本有 byte 177；Toro 缺 → 判 0，**DR-CAM-l**），驗其雙向互通即足以判「each of the equipped camera views」。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 0 (Absent)
3. PROXI Rear_View_Camera = 1 (Present)
4. PROXI Forward_Facing_Camera = 1 (Present)
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the corner of the rear view camera image and check that the Forward Facing Camera soft control is present
2. Select the Forward Facing Camera soft control in the corner of the view
3. Read the corner of the Forward Facing Camera view and check that the Rear View soft control is present
```

## expected_result

```
1. The Forward Facing Camera soft control is shown in the corner of the rear view camera image
2. The Forward Facing Camera view is displayed
3. The Rear View soft control is shown in the corner of the Forward Facing Camera view
```
