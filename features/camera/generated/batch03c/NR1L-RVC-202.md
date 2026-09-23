# NR1L-RVC-202 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_2357`（來源列 `SYS-RA-VF551_V42-253`）

## test_item 上半（verbatim，SYS2 逐字）

> copy the ADAS_LVDS_RRCamera_Cable output video into Rear_Camera_Repetition.Data and display the rearview image.

## reasoning

驗證目標為 `SYS-RA-VF551_V42-253` 之「複製 cable 影像並顯示」。`SYS-RA-VF551_V42-271` 與本列**逐字同句**，依同義列不另出 TC，plan 記 covered_by。**與 `-201` 之分工**：`-201` 驗其**時限**（`RESPONSE_TIME`），本列驗其**發生**；兩來源不同、失效態不同（§8.2.1）。依 R-CAM15(c)，V42 列承 637。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rearview image is displayed
```

## expected_result

```
1. STATUS_CCAN5.ShiftLeverPosition = 2 (R) is sent
2. The rearview image is displayed
```
