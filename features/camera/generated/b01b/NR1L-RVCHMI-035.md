# NR1L-RVCHMI-035 — SWE1-RVC-023-01

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5.3`（來源列 `NRL-142629`）

## test_item 上半（verbatim，SYS1 逐字）

> When the vehicle is shifted from REVERSE to PARK or DRIVE/NEUTRAL (AGSM) ○ Camera image will stay displayed if Camera Delay Settings is on: ■ After 10 seconds, the camera image will be turned off. Timer will start immediately once the vehicle is shifted from REVERSE

## reasoning

§7.5.3 之第一分支。`After 10 seconds` 與 `Timer will start immediately once the vehicle is shifted from REVERSE` 皆為逐字；以 9 秒／11 秒兩點驗計時器之起點與長度（±1 秒為人工可達之觀察窗；更緊之窗須 bus analyzer，見 `bench_verify.md`）。退出檔位取 P（`PARK`，來源列舉之第一款）。verbatim 51 token 逾 §4.3.1 之 50 上限，刪 `or ANY OTHER GEAR (manual gearshift)` 一段（手排之列舉，與本列所取之 P 檔無涉）；該段末之 `;` 與 `gearshift` 黏字，依 CAM-11 之前例整體刪去，故 `(AGSM)` 後不留分號。刪後 45 token，保序子序列成立。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
5. The shift lever is in R
6. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P) and record the timestamp
2. Read the HU display 9 seconds after the recorded timestamp and check that the camera image is still displayed
3. Read the HU display 11 seconds after the recorded timestamp and check that the camera image is turned off
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and its timestamp is recorded
2. The camera image is still displayed 9 seconds after the shift out of REVERSE
3. The camera image is turned off 11 seconds after the shift out of REVERSE
```
