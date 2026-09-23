# NR1L-RVCHMI-070 — SWE1-RVC-080

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.5.1`（來源列 `NRL-188073`）

## test_item 上半（verbatim，SYS1 逐字）

> If the ‘Enable wireless cameras’ setting is ON, when a wireless aux camera is selected from any location, the camera may be asleep and take up to a few seconds to activate. When this occurs, a message will show letting the customer know the camera is “connecting”.

## reasoning

§27.5.1 逐字載 `a message will show letting the customer know the camera is “connecting”`，惟該訊息之逐字文字**查無** —— `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁中 module 為 `Camera`／`Aux Camera` 之列，其訊息欄含 `connect` 者 15 筆，**無一為 `connecting` 之狀態訊息**（皆為 Add／Authenticating／Connection Complete／Connection ERROR／Delete 等流程畫面）→ **`PENDING: DR-CAM-h`**（依下放包 §2 之規定）。`take up to a few seconds` 無數值，不造時限，ER 只判訊息之出現與後續之活化。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless projection session is active
7. A wireless AUX camera is connected and asleep
```

## input_test_data

`NA`

## test_procedure

```
1. Select the wireless AUX camera entry from the Aux Cameras list
2. Read the HU display and check that a message tells the customer the camera is connecting
3. Read the HU display and check that the wireless AUX camera view is displayed once it has activated
```

## expected_result

```
1. The wireless AUX camera entry registers the selection
2. PENDING: DR-CAM-h a message showing that the camera is "connecting" is displayed; its verbatim text is not in the R1 HMI pop-up list
3. The wireless AUX camera view is displayed
```
