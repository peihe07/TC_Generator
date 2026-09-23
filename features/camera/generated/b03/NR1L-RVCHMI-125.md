# NR1L-RVCHMI-125 — SWE1-RVC-127-02

- **Test Group**：Rear View Camera｜**Test Set**：Wireless Camera Pairing
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_33.1.2`（來源列 `NRL-188147`）

## test_item 上半（verbatim，SYS1 逐字）

> Pressing YES will disconnect the wireless projection session and enable the wireless cameras and start the pairing process.

## reasoning

§33.1.2 之 YES 支，其三個後果（斷開投影、啟用設定、啟動配對）皆驗 —— 來源以 `and` 並列三者，缺一即未落地（**R-CAM13(a)**）。與 B02a `-065`（§27.4.2.1）之分工：後者之後果只有**兩個**（啟用、斷開），無配對流程；兩列之觸發按鍵（設定 vs `Add camera`）與來源列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
7. The PU1519 pop-up is displayed after the 'Add camera' button was selected
```

## input_test_data

`NA`

## test_procedure

```
1. Select <Yes> on the pop-up
2. Read the HU display and check that the wireless projection session has ended
3. Read the Aux Cameras list and check that "Enable Wireless Cameras" is now On
4. Read the HU display and check that the pairing process has started
```

## expected_result

```
1. The <Yes> button registers the selection and the pop-up closes
2. The wireless projection session is disconnected
3. The "Enable Wireless Cameras" setting is On
4. The pairing process starts and the QR Code Setup Process is displayed (PU0854)
```
