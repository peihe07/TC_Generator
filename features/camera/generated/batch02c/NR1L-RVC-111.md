# NR1L-RVC-111 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V4_PHDCC27_VF_1917`（來源列 `SYS-RA-VF551_V4-095`）

## test_item 上半（verbatim，SYS2 逐字）

> In this VF ShiftLeverPosition shall be set to TRANSM_FD_4.ShiftLeverPosition when Hybrid_Type != "Range Electric Paradigm Breaker" OR "Fuel Cell Electric Vehicle"

## reasoning

驗證目標為 `SYS-RA-VF551_V4-095` 之「非 REPB／FCEV 之 hybrid 型別時，`ShiftLeverPosition` 取自 `TRANSM_FD_4.ShiftLeverPosition`」。`SYS-RA-VF551_V4-105` 與本列逐字同句，依同義列不另出 TC，plan 記 covered_by。**相反側（`-096`／`-106`：REPB／FCEV 取 `PT_SYSTEM_FD_1.ShiftLeverPosition_PT`）不生成** ——該訊號不可注入（A-CA15，同 batch01 之 `V2-552`），plan 已記為唯二之「不生成」。「取自該訊號」之可判後果即注入該訊號後相機依其動作。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Hybrid_Type is not "Range Electric Paradigm Breaker" and not "Fuel Cell Electric Vehicle"
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The rear view camera image is displayed, which shows that the HU took the gear position from TRANSM_FD_4
```
