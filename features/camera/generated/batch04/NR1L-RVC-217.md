# NR1L-RVC-217 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1764`（來源列 `SYS-RA-VF551_V2-506`）

## test_item 上半（verbatim，SYS2 逐字）

> b. The head unit shall not interrupt the rear camera image.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-506` 之「HU 不中斷後方相機影像」。**章節脈絡**：V2 本 `VF章節` 欄於 `-499`～`-511` 區落後一組（DECISIONS 6-31 已裁），依該讀法本列屬 **Audio Mode OFF** 之脈絡。`SYS-RA-VF551_V4-137` 與本列**逐字同句**（V4 本），依同義列不另出 TC，plan 記 covered_by。**與 `NR1L-RVC-115`／`-116`（`SWE-CAM-003` 之 `V4-131`／`-138`）之分工**：後者驗該模式下**功能可用**，本列驗**影像不中斷**；兩者之來源與承接列皆不同（R-CAM10）。觸發取 Audio System Power 鍵 —— 其為 V2 §1.13.2.1.5／`-507` 所載之 Audio Mode 轉換條件。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU is in Audio Mode OFF
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the Audio System Power button on the HU
2. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. The Audio System Power button registers the press
2. The rear view camera image is not interrupted
```
