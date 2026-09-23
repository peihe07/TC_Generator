# NR1L-RVCHMI-066 — SWE1-RVC-076

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.2.2`（來源列 `NRL-188068`）

## test_item 上半（verbatim，SYS1 逐字）

> If the user presses no, the wireless projection session is maintained and wireless cameras are not enabled.

## reasoning

§27.4.2.2 逐字之兩個後果（保持投影 ＋ 不啟用）皆驗。與 `-065` 成一對正反例；兩列之來源列不同（`NRL-188067` vs `NRL-188068`），依 **R-CAM10** 不合併。

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
1. Select <No> on the pop-up
2. Read the HU display and check that the wireless projection session is still active
3. Read the Aux Cameras list and check that "Enable Wireless Cameras" is still Off
```

## expected_result

```
1. The <No> button registers the selection and the pop-up closes
2. The wireless projection session is still active
3. The "Enable Wireless Cameras" setting is still Off and no wireless camera entry is available
```
