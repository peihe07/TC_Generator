# NR1L-RVC-201 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V42_P637MCA_VF_1164`（來源列 `SYS-RA-VF551_V42-226`）

## test_item 上半（verbatim，SYS2 逐字）

> copy the ADAS_LVDS_RRCamera_Cable output video into Rear_Camera_Repetition.Data. -The rearview image shall be displayed on LTM_Display.GUI within RESPONSE_TIME since the signal TRANSM2.ShiftLeverPosition shifts to "R" when PROXI parameter Gear_Box_Type is different from "MTX"

## reasoning

驗證目標為 `SYS-RA-VF551_V42-226` 之「將 `ADAS_LVDS_RRCamera_Cable` 之輸出複製入 `Rear_Camera_Repetition.Data`，並於 `RESPONSE_TIME` 內顯示於 `LTM_Display.GUI`」。上半為摘句（§4.3.1）：原句 59 token 逾 50。**`RESPONSE_TIME` ＝ 2,0 sec**（V42 §1.14.1 `-679`／`-680`／`-683`）。**觸發訊號之訊息名依 profile §7.2 以訊號名重掃** —— 來源寫 `TRANSM2.ShiftLeverPosition`，`ShiftLeverPosition` 於 637MCA 本命中 `BO_ 998 STATUS_CCAN5`，procedure 因而以 `STATUS_CCAN5` 書寫（同 `NR1L-RVC-175` 之處置），verbatim 逐字不改。`Rear_Camera_Repetition.Data` 為內部資料（四本 DBC 零命中），以畫面之顯示為可判後果。依 R-CAM15(c)，V42 列承 637。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-f the TRANSM2 message is not present in the four DBC files in forms
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 2 (R)
2. Measure the time between step 1 and the moment the rearview image is fully displayed
```

## expected_result

```
1. STATUS_CCAN5.ShiftLeverPosition = 2 (R) is sent
2. The measured time is not greater than 2,0 s
```

## remarks

Source names the message TRANSM2; the DBC carries ShiftLeverPosition in STATUS_CCAN5 (BO_ 998). See DR-CAM-f.
