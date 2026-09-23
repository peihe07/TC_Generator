# NR1L-RVCHMI-034 — SWE1-RVC-022

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5.2`（來源列 `NRL-142628`）

## test_item 上半（verbatim，SYS1 逐字）

> Gear != R and RVC timeout expired;

## reasoning

§7.5.2。`RVC timeout` 之值於本條未載，取同章 **§7.5.3** 之逐字 `After 10 seconds`（`Timer will start immediately once the vehicle is shifted from REVERSE`），並與 Pop Up List `PU0361` 之 timeout 欄 `10` 相符 —— 同一計時器之兩處記載，不另開 DR。`Rear View Camera Delay` 設為 On 以使計時器生效（§7.2.2／§7.5.3 之前提）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in R
6. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 4 (D) and record the timestamp
2. Read the HU display and check that the RVC+PAM layout is still displayed
3. Wait 10 seconds from the recorded timestamp
4. Read the HU display and check that the RVC+PAM layout is no longer displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 4 (D) is sent and its timestamp is recorded
2. The RVC+PAM layout remains displayed during the timeout
3. The 10 second interval elapses
4. The RVC+PAM layout is no longer displayed and the last known HU display is shown again
```
