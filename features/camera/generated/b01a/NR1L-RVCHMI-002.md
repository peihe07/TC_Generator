# NR1L-RVCHMI-002 — SWE1-RVC-042

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.1.3`（來源列 `NRL-187334`）

## test_item 上半（verbatim，SYS1 逐字）

> Camera feed not available in OFF and ACC ignition states

## reasoning

驗證目標為 §6.1.3 之兩個點火態。raw 與 label 取 `PDT27_E2A_R1_BHCAN2.dbc` 之 `VAL_ … CmdIgnSts 1 "IGN_LK" 3 "ACC"`；來源寫 `OFF` 而 DBC 之 label 為 `IGN_LK`，依 **profile §10** 之第一類記於 `remarks`。兩態同屬一條且可觀察結果相同，不拆軸（**R-CAM3** 之拆軸判準為車型／品牌，非值）。兩 EE 皆勾且有 `Send CAN` 步 → 依 **R-CAM3(f)** 寫 CAN source 行。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 3 (ACC)
2. Read the HU display and check that the rear view camera image is not available
3. Send CAN: BCM_FD_10.CmdIgnSts = 1 (IGN_LK)
4. Read the HU display and check that the rear view camera image is not available
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 3 (ACC) is sent
2. The rear view camera image is not displayed
3. BCM_FD_10.CmdIgnSts = 1 (IGN_LK) is sent
4. The rear view camera image is not displayed
```

## remarks

Source names the OFF ignition state; the DBC label for that value is IGN_LK.
