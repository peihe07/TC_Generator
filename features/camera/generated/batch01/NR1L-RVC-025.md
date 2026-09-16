# NR1L-RVC-025 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`CFTS092-4781637`（來源列 `SYS-RA-CAM-072`）

## test_item 上半（verbatim，SYS2 逐字）

> When the HU receives the $RVC_SK_PRSNT$ = [Present] the HU shall activate the virtual Rear View Camera button for user select-ability.

## reasoning

驗證目標為 CFTS092 SYS-RA-CAM-072（ObjectID 4781637）之「$RVC_SK_PRSNT$ = [Present] 時啟用虛擬 Rear View Camera 鍵」。錨取 Rear Camera 節（R-CAM12）。$RVC_SK_PRSNT$ 為設定／參數標記，其車輛組態對應為 PROXI Rear_View_Camera = 1 (Present)（五平台 byte 86 bit 0 實測），故以該 PROXI 行表達前提。缺件側（Absent）不在本 Test Set 之範圍，屬 Configuration（SWE-CAM-002／-005）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the App Drawer and check that "Rear View Camera" is present and selectable
```

## expected_result

```
1. The App Drawer is displayed
2. The "Rear View Camera" entry is present in the App Drawer and can be selected
```
