# NR1L-RVCHMI-094 — SWE1-RVC-143-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.7.2`（來源列 `NRL-188179`）

## test_item 上半（verbatim，SYS1 逐字）

> Camera image must always be up while in REVERSE

## reasoning

§34.7.2 之後半。`always ... while in REVERSE` 之驗證重點為**無任何操作可使相機畫面消失**，故施以兩種退出嘗試（`X` 與硬鍵）皆不得離開相機。verbatim 為保序子序列（刪前半）。與 `-093` 之分工：前者驗 `X` 之**可用性與角色**，本列驗**相機畫面之不可中斷**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. A wired AUX camera is connected
7. The shift lever is in R
8. The AUX camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the <X> control in the AUX camera view
2. Read the HU display and check that a camera image is still displayed
3. Press the Radio hard key on the HU
4. Read the HU display and check that a camera image is still displayed
```

## expected_result

```
1. The <X> control registers the selection and the back-up camera view is shown
2. A camera image is still displayed while the gear is R
3. The Radio hard key registers the press
4. A camera image is still displayed while the gear is R
```
