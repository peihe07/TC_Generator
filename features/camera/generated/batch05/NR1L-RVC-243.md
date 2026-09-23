# NR1L-RVC-243 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_1164`（來源列 `SYS-RA-VF551_V42-226`）

## test_item 上半（verbatim，SYS2 逐字）

> copy the ADAS_LVDS_RRCamera_Cable output video into Rear_Camera_Repetition.Data.

## reasoning

**補生成之由**：拆解審計 **CAM-23 §3 #2**（`confidence = M`）—— `SYS-RA-VF551_V42-226` 之首句為**資料路徑之複製**（`copy the ADAS_LVDS_RRCamera_Cable output video into Rear_Camera_Repetition.Data.`），而母列 `NR1L-RVC-201` 只驗其後之 `RESPONSE_TIME` 時限。本列驗該複製本身。verbatim 取該首句（保序子序列之前段）。可觀察手段沿 A 本 `NR1L-RVC-058`／`-092` 之兩行式（`adb shell dumpsys media.camera`），其輸出是否足以判該資料路徑**須實機確認**，已記入 `bench_verify.md`。`Rear_Camera_Repetition.Data` 與 `ADAS_LVDS_RRCamera_Cable` 皆為來源之逐字內部名（§8.7.5(f)）。車型只勾 637 —— 同母列（V42 之錨 `P637MCA`，**R-CAM11** 平台對照）。**lint `J`（首字小寫）之豁免**：本列 test_item 上半**自來源 `Description` 之首 token 起**（`SYS-RA-VF551_V42-226` 全文即以小寫 `copy` 起首），符 **profile §5.1** 之豁免要件（CAM-19 之 6-65(a) 已明定該要件）；§4.3.1 之逐字忠實優先於版面規則。

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
1. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 2 (R)
2. Read the camera service status and check that the ADAS_LVDS_RRCamera_Cable output video is copied into Rear_Camera_Repetition.Data
   $ adb shell dumpsys media.camera
```

## expected_result

```
1. STATUS_CCAN5.ShiftLeverPosition = 2 (R) is sent and the rearview image is displayed
2. The Rear_Camera_Repetition.Data path is fed from the ADAS_LVDS_RRCamera_Cable output video
```
