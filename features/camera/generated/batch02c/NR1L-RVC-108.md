# NR1L-RVC-108 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1197`（來源列 `SYS-RA-VF551_V33-432`）

## test_item 上半（verbatim，SYS2 逐字）

> If LTM_OperationalModeSts.Info=="SNA" THEN LTM considers the last value of these signals for TIME_W_RVC2 time after TM stops the functionality.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-432` 之「`LTM_OperationalModeSts.Info = "SNA"` 時，LTM 於 `TIME_W_RVC2` 期間沿用該些訊號之最後值」。**`TIME_W_RVC2` ＝ 50 ms**（V33 §1.14.1 `SYS-RA-VF551_V33-587` 名／`-588` 值 `50`／`-591` 單位 `ms`；範圍 `[50;100]`、容差 `10`），故觀察窗寫 50 ms。`LTM_OperationalModeSts` 之 `CmdIgnSts` 對應仍為 DR-CAM-i 之範圍，SNA 之產生改以「停送該訊息」表達（訊號逾時即為 SNA，不需知其 raw）—— 此為規避 DR-CAM-i 之可執行寫法。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-i the CmdIgnSts value that corresponds to LTM_OperationalModeSts SNA is not sourced
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Stop transmitting LTM_OperationalModeSts so that its value becomes SNA
2. Read the HU display within 50 ms and check the rear view camera image
```

## expected_result

```
1. LTM_OperationalModeSts is no longer transmitted and its value becomes SNA
2. The rear view camera image is still displayed with the values it had before step 1
```
