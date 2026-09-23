# NR1L-RVC-205 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2367`（來源列 `SYS-RA-VF551_V42-263`）

## test_item 上半（verbatim，SYS2 逐字）

> IF the signal LTM_OperationalModeSts.Info is equal to "Ignition ON" AND the signal RVC_ImageDefeat.Req is equal to "Pressed" TRANSM2.ShiftLeverPosition is different from "R" AND the PROXI parameter Gear_Box_Type is different from "MTX") THEN LTM shall stop to copy the ADAS_LVDS_RRCamera_Cable into Rear_Camera_Repetition.Data and not display the rearview image.

## reasoning

驗證目標為 `SYS-RA-VF551_V42-263` 之「點火為 ON 系、`RVC_ImageDefeat.Req = "Pressed"` 且排檔條件成立時，停止複製」。上半為摘句（§4.3.1）：原句 73 token 逾 50。`RVC_ImageDefeat.Req` 為內部訊號（四本 DBC 零命中），以 `"X"` 鍵之按下表達（沿 `NR1L-RVC-021`／`-047` 之既有寫法）。排檔條件所引之 `TRANSM2.ShiftLeverPosition` 仍標 `PENDING: DR-CAM-f` —— 本列之觸發為按鍵而非排檔，該前提只影響條件之完整性，不影響本列可執行。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-f the TRANSM2 message is not present in the four DBC files in forms
4. The rearview image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the top right corner of the HU display
2. Read the HU display and check that no rearview image is displayed
```

## expected_result

```
1. The "X" exit button registers the press and the internal RVC_ImageDefeat.Req becomes Pressed
2. No rearview image is displayed
```
