# NR1L-RVC-221 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1761`（來源列 `SYS-RA-VF551_V2-503`）

## test_item 上半（verbatim，SYS2 逐字）

> b. Once the head unit exits the rear camera mode, the Head Unit shall process display updates to show current information.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-503` 之「離開相機模式後，HU 處理顯示更新以顯示現況」。`SYS-RA-VF551_V4-140` 與本列**逐字同句**，依同義列不另出 TC，plan 記 covered_by。**與 `NR1L-RVC-101`（`V2-509`，`SWE-CAM-003`）之分工**：`-509` 為 `c.` 子句「畫面**反映變化**並顯示現況」（結果面），本列為 `b.` 子句「**處理**顯示更新」（過程面）；兩來源分屬不同承接列，各出一 TC（R-CAM10）。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "Off"
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
2. Read the HU display and check the information shown on the restored display
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the rear camera image is closed
2. The restored display shows current information
```
