# NR1L-RVCHMI-068 — SWE1-RVC-078

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.4.4`（來源列 `NRL-188070`）

## test_item 上半（verbatim，SYS1 逐字）

> The ‘Enable wireless cameras’ setting is dynamically updated.

## reasoning

§27.4.4 之 `dynamically updated` 指**不需重新進入該清單即反映現值**，故以「清單開著時由外部事件改變該設定」驗之。該外部事件取 §27.4.5 之投影插入（其彈窗 `PU1517` 文字逐字 `Wireless Cameras disabled.`），為本節內唯一載明會改變該設定之事件。與 `-069`（§27.4.5）之分工：後者驗**設定被關閉與其彈窗**，本列驗**清單之即時更新**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. The head unit is a touchscreen radio
3. The head unit has WiFi hotspot capability
4. A MOPAR-provided wireless camera is available
5. The "Enable Wireless Cameras" setting is On
6. No wireless projection session is active
7. The Aux Cameras list is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Start a wired projection session that takes screen focus
2. Read the Aux Cameras list and check that "Enable Wireless Cameras" now reads Off
3. End the projection session
4. Read the Aux Cameras list and check that "Enable Wireless Cameras" reflects the current state
```

## expected_result

```
1. The projection session takes screen focus and the "Wireless Cameras disabled." pop-up is displayed
2. The "Enable Wireless Cameras" setting reads Off without the list being reopened
3. The projection session ends
4. The "Enable Wireless Cameras" setting reflects the current state without the list being reopened
```
