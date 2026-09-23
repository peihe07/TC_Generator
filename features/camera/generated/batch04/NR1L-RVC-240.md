# NR1L-RVC-240 — SWE-CAM-023

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V42_P637MCA_VF_2296`（來源列 `SYS-RA-VF551_V42-232`）

## test_item 上半（verbatim，SYS2 逐字）

> - IF the PROXI parameter Gear_Box_Type is equal to "MTX" AND the signal ENGINE1.ReverseGearSts becomes different from "Inserted" before T_INITDISPLAY, THEN the warning text shall be removed

## reasoning

驗證目標為 `SYS-RA-VF551_V42-232` 之「Gear_Box_Type 為 MTX 且排檔於 `T_INITDISPLAY` 之前離開 R 時，移除警示文字」。**`T_INITDISPLAY` ＝ 5,0 sec**（V42 §1.14.1 `-631`／`-632`／`-635`，profile §9），故步 2 寫 5 秒內。**觸發訊號之訊息名依 profile §7.2 以訊號名重掃** —— 來源寫 `ENGINE1`，該訊號於 637MCA 本命中 `STATUS_CCAN4`，procedure 因而以其書寫（同 `NR1L-RVC-175`／`-176` 之處置），verbatim 逐字不改（R-13）。警示文字本身之顯示由 `NR1L-RVC-056`（`V42-230`，`SWE-CAM-001`）承接，本列只驗其提前移除（§8.2.1）。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Gear_Box_Type = 1 (MTX)
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) less than 5 s after step 1
3. Read the HU display and check the warning text
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the warning text is overlaid
2. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent
3. The warning text is removed
```

## remarks

Source names the message ENGINE1; the DBC carries the signal in STATUS_CCAN4. See DR-CAM-f.
