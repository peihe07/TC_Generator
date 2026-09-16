# NR1L-RVC-033 — SWE-CAM-020

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1603`（來源列 `SYS-RA-VF551_V33-227`）

## test_item 上半（verbatim，SYS2 逐字）

> IF TTM module is present (CAN Node 63 (TTM) = Present): when the value of the BED_EXTENDER.BedExtenderSts =(equal) "Active" OR BED_EXTENDER.IncompleteBedExtenderSts =(equal) "True", LTM doesn't show the RVC image and overlaps the message "Camera Not in position" (see LTM HMI specification document)

## reasoning

驗證目標為 SYS-RA-VF551_V33-227 之第二支條件「IncompleteBedExtenderSts = True」，與 NR1L-RVC-032 為 OR 之兩支，依 §8.3 決策表各出一列。DBC 缺件與 CameraEventHal 狀態同 -032（DR-CAM-f、A-CA29）。

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
1. Send CAN: BED_EXTENDER.IncompleteBedExtenderSts = PENDING (PENDING: DR-CAM-f raw value and VAL label for True)
2. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
3. Read the HU display and check that no camera image is displayed and that the "Camera Not in position" message is shown
```

## expected_result

```
1. The incomplete bed extender status is reported as True
2. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent
3. No camera image is displayed and the "Camera Not in position" message is overlaid on the screen
```
