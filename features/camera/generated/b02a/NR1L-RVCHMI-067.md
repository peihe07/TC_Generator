# NR1L-RVCHMI-067 — SWE1-RVC-077

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.3`（來源列 `NRL-188069`）

## test_item 上半（verbatim，SYS1 逐字）

> If the setting is selected without any wireless projection session active, wireless cameras are activated without any popup displayed.

## reasoning

§27.4.3 為 §27.4.2 之補集分支（無投影時）。驗證重點在 `without any popup displayed` ——故 ER 明寫「無彈窗」。與 `-064`（§27.4.2）成一對：前者有投影 → 有彈窗，本列無投影 → 無彈窗。否定句式用 `check that no …`。

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
1. Set "Enable Wireless Cameras" = "On"
2. Read the HU display and check that no pop-up is displayed
3. Read the Aux Cameras list and check that the wireless camera entries are available
```

## expected_result

```
1. The "Enable Wireless Cameras" setting is On
2. No pop-up is displayed
3. The wireless camera entries are available in the Aux Cameras list
```
