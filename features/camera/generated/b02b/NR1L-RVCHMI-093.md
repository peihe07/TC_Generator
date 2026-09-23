# NR1L-RVCHMI-093 — SWE1-RVC-143-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_34.7.2`（來源列 `NRL-188179`）

## test_item 上半（verbatim，SYS1 逐字）

> <X> not available in REVERSE, unless acting as a back button within camera views.

## reasoning

§34.7.2 之前半（例外條款）。`unless acting as a back button within camera views` 之可觀察形制為：按下後**回到前一個相機視角**（而非退出相機）。verbatim 為該列 Description 之保序子序列（刪後半，由 `-094` 承接）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is an R1 Low head unit
3. Only wired AUX cameras are fitted
4. No wireless AUX feature is offered
5. PROXI Rear_View_Camera = 1 (Present)
6. A wired AUX camera is connected
7. The shift lever is in R
8. The back-up camera view is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the back-up camera view and check that no <X> control is present
2. Select the AUX camera soft control within the view
3. Read the AUX camera view and check that an <X> control is present and acts as a back button
4. Select the <X> control
```

## expected_result

```
1. No <X> control is shown in the back-up camera view while the gear is R
2. The AUX camera view is displayed
3. An <X> control is shown in the AUX camera view
4. The back-up camera view is shown again, which shows that the <X> acted as a back button
```
