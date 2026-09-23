# NR1L-RVC-222 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1752`（來源列 `SYS-RA-VF551_V2-510`）

## test_item 上半（verbatim，SYS2 逐字）

> b. The Head Unit shall process display updates after the head unit exits rear camera mode.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-510` —— 與 `-221`（`V2-503`）為**不同節之同型 `b.` 子句**，逐字略異（`after the head unit exits` vs `Once the head unit exits`）。依 §8.2.2「一個 sub-id 可需數個 TC，不得反向合併」，兩個來源各出一 TC；其 procedure 相同係因兩節之觸發相同，差別在所屬節之脈絡（Audio Mode 之兩側）。`SYS-RA-VF551_V4-133` 為 `-022` 所承（`NR1L-RVC-227`），非本列之同義列。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

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
