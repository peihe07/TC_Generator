# NR1L-RVCHMI-047 — SWE1-RVC-056

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.4`（來源列 `NRL-188032`）

## test_item 上半（verbatim，SYS1 逐字）

> Feature will follow core head unit logic and flow regarding lockout conditions

## reasoning

§27.1.4 轉指 core head unit 之 lockout 條文 —— 該條文為**外部規格**，其內容依 canon **§8.4.2**（R-CAM13(b)）不測；本列只驗 AUX 側**受其支配**。可觀察之 lockout 形制取 `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` `Settings` 分頁 row 457 之逐字 `UNAVAILABLE WHILE VEHICLE IS IN MOTION:`。設定路徑取同表 row 464 `13. Camera` → row 474 `10. Aux Cameras`。與 `-050`（§27.3.4.1）之分工：後者驗**連線流程**之 lockout，本列驗**設定清單**之 lockout。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
4. The shift lever is in D
5. The vehicle is stationary
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Select "Aux Cameras"
5. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
6. Read the "Aux Cameras" list and check that no entry can be selected
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Aux Cameras" list is displayed
5. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
6. No entry in the "Aux Cameras" list can be selected while the vehicle is in motion
```
