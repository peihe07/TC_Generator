# NR1L-RVC-101 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1753`（來源列 `SYS-RA-VF551_V2-509`）

## test_item 上半（verbatim，SYS2 逐字）

> c. After exiting rear camera mode, the Head Unit display shall reflect the changes and show current information.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-509` 之 `c.` 子句「離開相機模式後，畫面反映其間之變化並顯示現況」。與 `NR1L-RVC-098` 之分工：`-491` 驗「切回非相機」之發生，本列驗「切回後之內容為現況」——後者之失效態是切回後顯示過期畫面，前者不會 FAIL（§8.2.1）。同節之 `b.` 子句（`-510`：處理顯示更新）為同一行為之過程面，不另出 TC。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫（來源之子句編號 `a.`／`c.`）；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

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
2. The restored display shows current information and not the state it had before the camera was displayed
```
