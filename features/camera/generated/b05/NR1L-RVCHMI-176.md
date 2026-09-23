# NR1L-RVCHMI-176 — SWE1-RVC-029

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.3.2`（來源列 `NRL-142636`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC2.3) When the Rear View Camera is turned off, the user is then returned to their last known HU state

## reasoning

§8.3.2 之 `last known HU state` 與 §8.1 之 `last known screen`（B01b `-039`）為**同一概念之兩處記載**，惟本列之觸發為**相機關閉**（檔位離開 R），`-039` 之觸發為**按 `X`**；兩列之來源列不同（`NRL-142636` vs `NRL-142631`），依 **R-CAM10** 不合併。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The Radio display was the last display shown before the camera image
5. The shift lever is in R
6. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
2. Read the HU display and check that the Radio display is shown again
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the rear view camera image is removed
2. The Radio display is shown again, which is the last known HU state
```
