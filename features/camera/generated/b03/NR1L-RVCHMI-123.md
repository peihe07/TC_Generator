# NR1L-RVCHMI-123 — SWE1-RVC-126

- **Test Group**：Rear View Camera｜**Test Set**：Wireless Camera Pairing
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_33.1.1`（來源列 `NRL-188146`）

## test_item 上半（verbatim，SYS1 逐字）

> If the ‘enable wireless cameras’ setting is not enabled, no wireless projection session is active and the user selects the ‘Add camera’ button, the setting is automatically enabled and the pairing process is started

## reasoning

§33 之父題逐字為 `Adding a New Wireless Camera (QR Code Method)`（`NRL-188144`），§33.1 為 `Connecting a New Wireless Camera – interaction with ’enable wireless cameras’ setting`。配對流程之逐字畫面取 **`PU0854`**（module `Aux Camera`，Timeout 欄 `60 seconds`）。`(please refer to next pages)` 為交叉引用之括號句，其標的即 §33.2（`-127`），**非全文交叉引用**，故本列仍出 TC（R-CAM16(c)(ii) 不適用）。與 B02a `-071`（§27.5.2）之分工：後者由**選取無線相機**觸發自動啟用，本列由 **`Add camera` 按鍵**觸發並另啟配對流程。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. No wireless projection session is active
7. The Aux Cameras list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select the 'Add camera' button
2. Read the Aux Cameras list and check that "Enable Wireless Cameras" is now On
3. Read the HU display and check that the pairing process has started
```

## expected_result

```
1. The 'Add camera' button registers the selection
2. The "Enable Wireless Cameras" setting is On and no pop-up was displayed
3. The pairing process starts and the display reads "Add Aux Camera <insert camera number>" with the QR Code Setup Process (PU0854)
```
