# NR1L-RVC-236 — SWE-CAM-023

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1573`（來源列 `SYS-RA-VF551_V2-530`）

## test_item 上半（verbatim，SYS2 逐字）

> - The warning text shall follow ISO font 15008 and have size greater than 18 arc minutes.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-530` 之「警示文字遵 ISO font 15008 且字高大於 18 arc minutes」。本列之來源為條列式（`shall follow ISO font 15008 and have size`），與 `-235` 為**不同節之同型條文**，逐字相異故各出一 TC（§8.2.2）。**量測手段來源未載，不造工具**（§8.4.1）；本列與 `-235`／`-236` 一併列入 `bench_verify.md` 之字高治具項。與 `NR1L-RVC-112`（`V4-117`，`SWE-CAM-003`）之關係：來源不同本、承接列不同，各歸其列（R-CAM10）。

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
