# NR1L-RVCHMI-043 — SWE1-RVC-034

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.7`（來源列 `NRL-142642`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC6) When the vehicle is in accessory mode, the image shall not be displayed. RVC is an ignition fed module and thus relies on ignition to be in RUN state.

## reasoning

§8.7 兩句：前句為否定（accessory 態不顯示），後句給出其理由（RVC 為點火供電模組，依賴 RUN 態）。故本列以 ACC → RUN 之往返同時驗兩句 —— 只驗前句則後句之「relies on ignition to be in RUN state」無落地（**R-CAM13(a)**）。與 B01a `-002`（H 本 §6.1.3）之分工：後者為 HeadUnitCameraSystems 本之條文，驗 **OFF 與 ACC 兩態皆不可用**；本列為 RVC+PAM 本之條文，驗 **ACC 不顯示 ＋ 回 RUN 即恢復**，來源列與承接列皆不同。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. The shift lever is in R
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BCM_FD_10.CmdIgnSts = 3 (ACC)
2. Read the HU display and check that no camera image is displayed
3. Send CAN: BCM_FD_10.CmdIgnSts = 4 (RUN)
4. Read the HU display and check that the rear view camera image is displayed again
```

## expected_result

```
1. BCM_FD_10.CmdIgnSts = 3 (ACC) is sent
2. No camera image is displayed
3. BCM_FD_10.CmdIgnSts = 4 (RUN) is sent
4. The rear view camera image is displayed again
```
