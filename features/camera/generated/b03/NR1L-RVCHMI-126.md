# NR1L-RVCHMI-126 — SWE1-RVC-127-03

- **Test Group**：Rear View Camera｜**Test Set**：Wireless Camera Pairing
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_33.1.2`（來源列 `NRL-188147`）

## test_item 上半（verbatim，SYS1 逐字）

> Pressing NO will maintain wireless projection session and stop the pairing process.

## reasoning

§33.1.2 之 NO 支，其兩個後果（保持投影、停止配對）皆驗。與 `-125` 成一對正反例；兩列之來源列同為 `NRL-188147` 而**驗證點相異**（同一列之兩個分支，依 §4.3.1 分列），故 `specification_reference` 相同。否定句式用 `check that no …`。

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
1. Select <No> on the pop-up
2. Read the HU display and check that the wireless projection session is still active
3. Read the HU display and check that no pairing process has started
```

## expected_result

```
1. The <No> button registers the selection and the pop-up closes
2. The wireless projection session is still active
3. No pairing process is started and no QR code is displayed
```
