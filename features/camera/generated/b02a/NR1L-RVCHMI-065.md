# NR1L-RVCHMI-065 — SWE1-RVC-075

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.2.1`（來源列 `NRL-188067`）

## test_item 上半（verbatim，SYS1 逐字）

> If the user presses yes, wireless aux cameras are enabled and the wireless projection session is disconnected.

## reasoning

§27.4.2.1 逐字之兩個後果（啟用 ＋ 斷開投影）皆驗。`<Yes>` 之按鍵標籤取 `PU1518` 之按鈕欄逐字。與 `-066`（§27.4.2.2）成一對正反例。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
7. The PU1518 pop-up is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Select <Yes> on the pop-up
2. Read the Aux Cameras list and check that the wireless camera entries are available
3. Read the HU display and check that the wireless projection session has ended
```

## expected_result

```
1. The <Yes> button registers the selection and the pop-up closes
2. The "Enable Wireless Cameras" setting is On and the wireless camera entries are available
3. The wireless projection session is disconnected
```
