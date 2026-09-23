# NR1L-RVC-203 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2378`（來源列 `SYS-RA-VF551_V42-274`）

## test_item 上半（verbatim，SYS2 逐字）

> not copy the ADAS_LVDS_RRCamera_Cable output video into Rear_Camera_Repetition.Data and not display the rearview image.

## reasoning

驗證目標為 `SYS-RA-VF551_V42-274` 之「不複製 cable 影像、不顯示 rearview 影像」之側。與 `-202` 成正負一對（§8.3 每點一 TC）。依 R-CAM15(c)，V42 列承 637。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

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
1. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 1 (P)
2. Read the HU display and check that no rearview image is displayed
```

## expected_result

```
1. STATUS_CCAN5.ShiftLeverPosition = 1 (P) is sent
2. No rearview image is displayed
```
