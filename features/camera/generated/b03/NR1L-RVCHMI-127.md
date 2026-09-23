# NR1L-RVCHMI-127 — SWE1-RVC-128

- **Test Group**：Rear View Camera｜**Test Set**：Wireless Camera Pairing
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_33.2.1`（來源列 `NRL-188149`）

## test_item 上半（verbatim，SYS1 逐字）

> Function not available while vehicle in drive

## reasoning

§33.2 之父題逐字為 `Connecting a New Wireless Camera – QR Code (success)`（`NRL-188148`）。`in drive` 之速度值本條未載，取 **profile §9** 之 8 mph 門檻（raw 206 ＝ 12.875 km/h，門檻上方最近之可注入點）—— 與 B02a `-061`（§27.3.4.1，`Camera connection process is locked out when vehicle is in motion`）同一判準。**兩列之分工**：`-061` 之條件為 `in motion`（§27.3.4 `Lock out conditions / Requirements`），本列之條件為 `in drive`（§33.2，配對流程之成功路徑上），來源章與承接列皆不同（**R-CAM10**）；兩者之可佈狀態相同，故 ER 一致。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. CAN source: BRAKE_FD_2.VehicleSpeedVSOSig (HDCC27, DT27) / STATUS_CCAN3.VehicleSpeedVSOSig (637, 2261, 376)
7. The shift lever is in D
8. The Aux Cameras list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h)
2. Select the 'Add camera' button
3. Read the HU display and check that no pairing process starts
```

## expected_result

```
1. BRAKE_FD_2.VehicleSpeedVSOSig = 206 (12.875 km/h) is sent
2. The 'Add camera' button does not register the selection
3. No pairing process is started and no QR code is displayed
```
