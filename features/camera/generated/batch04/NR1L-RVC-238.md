# NR1L-RVC-238 — SWE-CAM-023

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1705`（來源列 `SYS-RA-VF551_V2-542`）

## test_item 上半（verbatim，SYS2 逐字）

> a. HU shall set HU_ZOOM.req = Not Pressed when Zoom In soft button is not pressed.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-542` 之「Zoom In 軟鍵未被按下時，HU 設 `HU_ZOOM.req = Not Pressed`」。**`HU_ZOOM.req` 為內部訊號**（`forms/` 四本 DBC 以 `HU_ZOOM` 掃描零命中），依 §6 以其可觀察之後果書寫 —— `SYS-RA-VF551_V2-486` 之 `d.`／`e.` 子句載明 `HU_ZOOM.req = Pressed` 對應 `vehicleUpdate_2.ZoomViewReq = Pressed`、預設為 `Not_Pressed`（`NR1L-RVC-134`／`-135`），故以該 LVDS 訊號為觀察面。**兩列之分列**：來源分別指 Zoom Out（`-540`）與 Zoom In（`-542`）兩個不同軟鍵，逐字相異故各出一 TC（§8.2.2）。LVDS 之觀察不造命令（profile §7.3）。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

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
1. Read vehicleUpdate_2.ZoomViewReq without pressing the Zoom In soft button
2. Read the recording and check the value that is sent
```

## expected_result

```
1. The LVDS link is recorded
2. vehicleUpdate_2.ZoomViewReq = Not_Pressed is sent over LVDS
```
