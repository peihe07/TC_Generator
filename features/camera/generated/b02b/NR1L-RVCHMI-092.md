# NR1L-RVCHMI-092 — SWE1-RVC-142

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.7.1`（來源列 `NRL-188178`）

## test_item 上半（verbatim，SYS1 逐字）

> DT and HDCC programs with SVC and Camera app will not have access to AUX cameras via the left corner of views

## reasoning

**來源逐字點名平台** `DT and HDCC programs` —— 故 `Vehicle Model` 只勾 `HDCC27`／`DT27`，依 **R-CAM3**（來源直接載平台）而非 R-CAM18(b)。驗否定側之外亦驗替代入口仍在（Camera app），同 `-076` 之理。本條與 §34.10.3（`DT and HDCC programs with SVC and Camera app will not have access to AUX cameras via the left corner of views`）逐字同句，惟後者屬 `AUX Camera Settings` 組，不在本批。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. PENDING: DR-CAM-r the equipment flag for the "Camera App" feature is not sourced
4. A wired AUX camera is connected
5. The Vehicle Surround View is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the left corner of the Vehicle Surround View and check that no AUX camera soft control is present
2. Press "Apps" on Menu Bar to open App Drawer
3. Select the Camera app in the App Drawer
4. Read the Camera app home page and check that the AUX camera soft control is present
```

## expected_result

```
1. No AUX camera soft control is shown in the left corner of the Vehicle Surround View
2. The App Drawer is displayed
3. The Camera app home page is displayed
4. The AUX camera soft control is shown on the Camera app home page
```
