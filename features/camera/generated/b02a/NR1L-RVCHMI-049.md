# NR1L-RVCHMI-049 — SWE1-RVC-058

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.1.5.1`（來源列 `NRL-188034`）

## test_item 上半（verbatim，SYS1 逐字）

> The authentication method is via token pass through QR code.

## reasoning

§27.1.5.1 之 `token pass through QR code`。其流程之逐字畫面取 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 之 `PU0854`（`Add Aux Camera <insert camera number>` / `QR Code Setup Process`）與 `PU0857`（`Authenticating "[Insert Camera Name]" to Uconnect HotSpot`）。與 `-051`（§27.3.5.1）之分工：後者之條文載**傳遞之內容**（WiFi network credentials）與其依據（Cyber Security requirements），本列載**方法**（token via QR code）。

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
2. Read the HU display and check that a QR code is presented for the camera to scan
3. Complete the QR code scan with the wireless camera
4. Read the HU display and check that the camera is authenticated
```

## expected_result

```
1. The add wireless camera process starts
2. A QR code is presented on the HU display
3. The wireless camera scans the QR code
4. The HU shows that the camera is authenticated
```
