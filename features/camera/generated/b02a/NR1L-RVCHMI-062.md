# NR1L-RVCHMI-062 — SWE1-RVC-072

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.3.5.1`（來源列 `NRL-188063`）

## test_item 上半（verbatim，SYS1 逐字）

> Head unit will authenticate the camera by passing WiFi network credentials via QR code scan per Cyber Security requirements

## reasoning

§27.3.5.1 之驗證點為**所傳遞之內容**（WiFi network credentials）及其結果（相機加入 HU 之網路）。逐字畫面取 `PU0857`（`Authenticating "[Insert Camera Name]" to Uconnect HotSpot`）與 `PU0454`（`Wireless Camera Connection Complete` / `Successfully connected to`）。`per Cyber Security requirements` 指向**外部規格**，依 §8.4.2 不測其內容。與 `-049`（§27.1.5.1）之分工：後者驗**方法**（token via QR code），本列驗**內容與結果**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless camera is connected
```

## input_test_data

`NA`

## test_procedure

```
1. Start the add wireless camera process from the Aux Cameras list
2. Complete the QR code scan with the wireless camera
3. Read the HU display and check that the camera has joined the head unit WiFi network
```

## expected_result

```
1. A QR code is presented on the HU display
2. The wireless camera scans the QR code and joins the head unit WiFi network
3. The HU shows that the camera is connected
```
