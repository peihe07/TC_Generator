# NR1L-RVCHMI-203 — SWE1-RVC-021

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5.1`（來源列 `NRL-142627`）

## test_item 上半（verbatim，SYS1 逐字）

> Gear = D and speed threshold is overcome or RVC timeout expired; ○ If the camera is activated above the speed threshold limit via the soft control (user input) it will remain on the screen for 10 seconds before disappearing

## reasoning

**補生成之由**：拆解審計 **CAM-22 §5 #3**（`confidence = M`）—— 母列 `NR1L-RVCHMI-033` 只驗「10 秒後消失」而未驗「10 秒前仍在」，單側無法分辨 10 秒與更短之窗。本列取 **9 秒**之下界，與 `-035`（§7.5.3 之 9／11 兩點）形制一致。門檻值見 **profile §9**；raw 206 ＝ 12.875 km/h 為門檻上方最近之可注入點（**A-CA30**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in D
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Press the camera soft button on the HU and record the timestamp
3. Read the HU display 9 seconds after the recorded timestamp and check that the RVC+PAM layout is still displayed
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent, which is above the threshold
2. The camera soft button registers the press and its timestamp is recorded
3. The RVC+PAM layout is still displayed 9 seconds after the press
```
