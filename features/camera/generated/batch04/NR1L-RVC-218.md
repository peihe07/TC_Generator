# NR1L-RVC-218 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1751`（來源列 `SYS-RA-VF551_V2-511`）

## test_item 上半（verbatim，SYS2 逐字）

> a. When the head unit executes entertainment and non-entertainment features, the Head Unit shall not interrupt the rear camera image display.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-511` 之「HU 執行娛樂與非娛樂功能時，不中斷後方相機影像顯示」。`SYS-RA-VF551_V4-132` 與本列**逐字同句**，依同義列不另出 TC，plan 記 covered_by。「執行功能」取 App Drawer 之開啟為代表 —— 其為 §5.3 已鎖定之 hop，且為疊加於影像之操作；與 `-215`～`-217`（Audio Mode 之轉換）之觸發不同，故分列。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. The App Drawer is displayed over the rear view camera image
2. The rear view camera image is not interrupted
```
