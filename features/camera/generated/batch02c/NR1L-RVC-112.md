# NR1L-RVC-112 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V4_PHDCC27_VF_1573`（來源列 `SYS-RA-VF551_V4-117`）

## test_item 上半（verbatim，SYS2 逐字）

> - The warning text shall follow ISO font 15008 and have size greater than 18 arc minutes.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-117` 之「警示文字須遵 ISO font 15008 且字高大於 18 arc minutes」。**ER 以來源數值逐字書寫**（下放包 §2 所令）；**量測手段來源未載，不造工具**（§8.4.1）——procedure 只寫 `Read … and check its font and its size`，由人工以字高治具量測。警示文字本身之顯示由 `NR1L-RVC-053`（V2-531，Atl-Hi `Check Entire Surroundings`）承接，本列只驗其字型與字高（§8.2.1）。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`。

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
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the warning text overlaid on the upper center of the display and check its font and its size
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the warning text is overlaid
2. The warning text follows ISO font 15008 and its size is greater than 18 arc minutes
```
