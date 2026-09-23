# NR1L-RVCHMI-073 — SWE1-RVC-082-02

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.6.1`（來源列 `NRL-188076`）

## test_item 上半（verbatim，SYS1 逐字）

> If the user presses ‘YES’ the setting is automatically enabled.

## reasoning

§27.6.1 之後半（`If the user presses ‘YES’ the setting is automatically enabled.`）。verbatim 為該列 Description 之保序子序列（刪前半之條件句，由 `-072` 承接）。與 `-065`（§27.4.2.1）之分工：後者由**操作設定**進入彈窗，其後果含「斷開投影」；本列由**選取相機**進入，其條文只載「設定自動啟用」，故 ER 不判斷開投影 ——**不把 §27.4.2.1 之後果搬到本列**（§8.4.1 不造來源未載之判準）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is Off
6. A wireless projection session is active
7. The PU1518 pop-up is displayed after a wireless AUX camera was selected
```

## input_test_data

`NA`

## test_procedure

```
1. Select <Yes> on the pop-up
2. Read the Aux Cameras list and check that "Enable Wireless Cameras" is now On
3. Read the HU display and check that the wireless AUX camera view is displayed
```

## expected_result

```
1. The <Yes> button registers the selection and the pop-up closes
2. The "Enable Wireless Cameras" setting is On
3. The wireless AUX camera view is displayed
```
