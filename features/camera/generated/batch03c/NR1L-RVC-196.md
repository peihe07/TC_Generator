# NR1L-RVC-196 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1662`（來源列 `SYS-RA-VF551_V2-539`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall receive the following signals on LVDS: - ADAS_LVDS_RRCamera_Cable - systemStatus.ExternalErrorStatus - systemStatus.InternalErrorStatus - systemStatus.Communications_Timeout - systemStatus.ZoomViewRes

## reasoning

驗證目標為 `SYS-RA-VF551_V2-539` 之「HU 於 LVDS **接收**所列之訊號」——其為**清單完整性**之驗證點，比照 `NR1L-RVC-088`（`V2-538`，送出側）與 DECISIONS 6-26，**不拆列**。兩列之方向相反：`-088` 驗 HU → RVCM 之送出，本列驗 RVCM → HU 之接收。各訊號之值語意由其各自之來源承接（`systemStatus.*` → `-179`～`-194`；`ADAS_LVDS_RRCamera_Cable` → `-197`／`-198`）。**`systemStatus.*` 為 RVCM → HU 之 LVDS 訊號**（四本 DBC 零命中），其注入須 LVDS 模擬器；該能力之確認已在 `bench_verify.md`（DECISIONS 6-38 之同一項）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Record the LVDS link for at least one transmission cycle of each signal
2. Read the recording and check that each of the signals listed in the Test Item is present
```

## expected_result

```
1. The LVDS link is recorded
2. All the listed signals are received by the HU over LVDS
```
