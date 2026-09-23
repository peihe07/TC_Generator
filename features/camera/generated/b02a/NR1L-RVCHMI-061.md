# NR1L-RVCHMI-061 — SWE1-RVC-071

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.3.4.1`（來源列 `NRL-188061`）

## test_item 上半（verbatim，SYS1 逐字）

> Camera connection process is locked out when vehicle is in motion.

## reasoning

§27.3.4.1 逐字。`in motion` 之速度值本節未載，取 **profile §9** 之 8 mph 門檻（raw 206 ＝ 12.875 km/h，門檻上方最近之可注入點）—— 該門檻為本 feature 全案所用之唯一速度標定，不另造。與 `-047`（§27.1.4）之分工：後者驗**設定清單**之 lockout，本列驗**連線流程**之 lockout；兩列之來源節與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
7. The vehicle is stationary
8. The Aux Cameras list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Select the control that adds a wireless camera
3. Read the HU display and check that the connection process does not start
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The add control does not register the selection
3. No add wireless camera pop-up is displayed
```
