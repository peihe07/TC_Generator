# NR1L-RVC-032 — SWE-CAM-020

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1603`（來源列 `SYS-RA-VF551_V33-227`）

## test_item 上半（verbatim，SYS2 逐字）

> IF TTM module is present (CAN Node 63 (TTM) = Present): when the value of the BED_EXTENDER.BedExtenderSts =(equal) "Active" OR BED_EXTENDER.IncompleteBedExtenderSts =(equal) "True", LTM doesn't show the RVC image and overlaps the message "Camera Not in position" (see LTM HMI specification document)

## reasoning

驗證目標為 SYS-RA-VF551_V33-227 之「BedExtenderSts = Active 時不顯示 RVC 影像並疊加 Camera Not in position 訊息」。**BED_EXTENDER 訊息不存在於 forms/ 之四本 DBC**（全文字面掃描：FDCAN8 僅有 Bed Lowering Mode 與 Flatbed 拖車名，其餘三本零命中），raw 值與 VAL label 依 R-13 標 PENDING: DR-CAM-f。CameraEventHal 表該三訊號皆 Harman = N／Not yet，依下放包 §3 仍依規格生成（CAN bench 可送），實作可能未接線之風險登 A-CA29。畫面文字 "Camera Not in position" 於 Pop Up List 查無（A-CA20／DR-CAM-h），以來源原文書寫。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The TTM module is present on the vehicle at CAN node 63
4. PENDING: DR-CAM-f the BED_EXTENDER message is not present in the four DBC files in forms
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BED_EXTENDER.BedExtenderSts = PENDING (PENDING: DR-CAM-f raw value and VAL label for Active)
2. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
3. Read the HU display and check that no camera image is displayed and that the "Camera Not in position" message is shown
```

## expected_result

```
1. The bed extender status is reported as Active
2. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent
3. No camera image is displayed and the "Camera Not in position" message is overlaid on the screen
```
