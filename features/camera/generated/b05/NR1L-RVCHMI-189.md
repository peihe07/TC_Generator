# NR1L-RVCHMI-189 — SWE1-RVC-004

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.3`（來源列 `NRL-142609`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM3) Flashing lines should have the same flash frequency as the IPC (refer to VF 179).

## reasoning

§6.3 轉指 **VF 179**（IPC 之規格）—— 該文件為**外部規格**，依 §8.4.2 不測其內容，故本列**不判絕對頻率值**，只判 HU 與 cluster **兩者相同**（來源之 `same ... as the IPC`）。該量測須同時錄兩個顯示器，記入 `bench_verify.md`。本列之 PAM 狀態由**實體障礙物**觸發（非 CAN 注入），故不寫 CAN source 行（**R-CAM3(f)**）。PAM 狀態之 CAN 對照（供 `-191` 用）：Atl-Hi 為 `BCM_FD_12.PAMRequestSts`（`PDT27_E2A_R1_FDCAN8.dbc`），Atl-Mi 為 `STATUS_PAM.PAMSystemSts`（`P363`／`637MCA` 兩本，`VAL_ 0 "OFF" 1 "ON_Active" 2 "ON_Inactive" 3 "ON_Disabled"`）—— 兩 EE 之訊號名不同，故寫 CAN source 行（**R-CAM3(f)**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. The RVC+PAM layout is displayed
5. An obstacle is within the PAM alert distance so that the lines flash
```

## input_test_data

`NA`

## test_procedure

```
1. Record the flash frequency of the PAM lines on the HU display
2. Record the flash frequency of the corresponding PAM indication on the cluster
3. Compare the two recorded frequencies
```

## expected_result

```
1. The flash frequency of the PAM lines on the HU is recorded
2. The flash frequency of the PAM indication on the cluster is recorded
3. The two recorded frequencies are the same
```
