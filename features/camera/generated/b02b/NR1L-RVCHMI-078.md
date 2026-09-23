# NR1L-RVCHMI-078 — SWE1-RVC-088

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.8.2`（來源列 `NRL-188084`）

## test_item 上半（verbatim，SYS1 逐字）

> Selecting a new view takes you to the new view

## reasoning

§27.8.2 逐字。取 AUX 2（而非 AUX 1）為標的，以與「原本顯示之視角」相異，方驗得 `takes you to the new view`。與 `-077`（§27.8.1）之分工：後者驗**彈窗之開啟與內容**，本列驗**選取之後果**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. Two wired AUX cameras are connected
4. The rear view camera image is displayed
5. The "More Aux" pop-up is open
```

## input_test_data

`NA`

## test_procedure

```
1. Select the AUX 2 button in the pop-up
2. Read the HU display and check that the AUX 2 camera view is displayed
```

## expected_result

```
1. The AUX 2 button registers the selection and the pop-up closes
2. The AUX 2 camera view is displayed
```
