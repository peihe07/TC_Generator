# NR1L-RVC-059 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V33_P226MCA_VF_1137`（來源列 `SYS-RA-VF551_V33-214`）

## test_item 上半（verbatim，SYS2 逐字）

> Consider Rear_Camera_Enable.Info="FALSE" as the init default value.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-214` 之「`Rear_Camera_Enable.Info="FALSE"` 為初始預設值」。**`Rear_Camera_Enable.Info` 為內部訊號**（`forms/` 四本 DBC 字面掃描零命中；`SYS-RA-VF551_V3-258` 亦自稱 `internal signal`），不可於匯流排觀察；依 §6 以其可判後果書寫 —— Enable 為 FALSE 即開機後不顯示影像。`SYS-RA-VF551_V33-215`（`RVC_ACTIVE=False` 之初值）與 `-217`（`DelayOff=Off`／`GridLines=On` 之初值）為同一驗證點（開機預設值）之其餘兩項；`-215` 明載「internal at this functionality」更不可觀察，二者依 plan 記 covered_by 本列，不另出 TC。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU has been restored to its factory default settings
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read the HU display and check that no rear view camera image is displayed
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
2. No rear view camera image is displayed
```
