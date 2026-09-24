# NR1L-RVC-249 — SWE-CAM-025

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1603`（來源列 `SYS-RA-VF551_V33-227`）

## test_item 上半（verbatim，SYS2 逐字）

> IF TTM module is present (CAN Node 63 (TTM) = Present): when the value of the BED_EXTENDER.BedExtenderSts =(equal) "Active" OR BED_EXTENDER.IncompleteBedExtenderSts =(equal) "True", LTM doesn't show the RVC image and overlaps the message "Camera Not in position" (see LTM HMI specification document)

## reasoning

**R-CAM19 追溯補齊**（CAM-26 §2）：`SWE-CAM-025`（NormalCamera App，題名 `Bed Extender Interlock - Warning Overlay`）之唯一來源 `SYS-RA-VF551_V33-227` 與 `SWE-CAM-020` 共引 —— **同源 SWE-CAM-020**（其 TC 為 `NR1L-RVC-032`／`-033`；下放包 §2 寫「全委派 `-023`」與 `batch04_plan.tsv` 第 116 列不合，更正記 A-CA38）。依 **R-CAM19(b)**，驗證角度取本列 037 Description（`The NormalCamera App shall display a "Camera Not in position" warning overlay when the bed extender active state is received.`）—— App 側疊層於**影像已顯示中**收到 bed extender active 之反應；`-032`／`-033`（Daemon 側）為先置 bed extender 再入 R 檔之抑制，本列之觸發序相反（先 R 檔顯示影像、後送 `BedExtenderSts = Active`），故為狀態轉換。`IncompleteBedExtenderSts` 分支已由 `-033` 驗，本列不重複。`BED_EXTENDER` 訊息四本 DBC 皆無 → `PENDING: DR-CAM-f`（前提與賦值佔位沿 `-032`）；疊層文字 `Camera Not in position` 於 Pop Up List 0 命中 → ER 子項標 `PENDING: DR-CAM-h`（DECISIONS 6-9／A-CA20；B 本 `NR1L-RVCHMI-184` 之 `Camera Out of Position` 為同一警示之另一寫法）。影像之移除為來源逐字（`doesn't show the RVC image`），照寫。車型只勾 2261（V33 之錨 `P226MCA`，同母列）。

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
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Send CAN: BED_EXTENDER.BedExtenderSts = PENDING (Active)
a. PENDING: DR-CAM-f the raw value and VAL label for Active are not sourced
3. Read the HU display and check that the camera image is removed and that the warning overlay is shown
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
2. The bed extender status is reported as Active
3. The rear view camera image is no longer displayed and the warning overlay is shown
a. PENDING: DR-CAM-h the overlay reads "Camera Not in position"; that string is not in the R1 HMI pop-up list
```
