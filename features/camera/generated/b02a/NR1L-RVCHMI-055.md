# NR1L-RVCHMI-055 — SWE1-RVC-064

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Access
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_27.2.5.1`（來源列 `NRL-188047`）

## test_item 上半（verbatim，SYS1 逐字）

> HMI BP V-3: Push Button Control

## reasoning

§27.2.5.1 為 `Soft Controls Requirements:` 節下之一句，指向 **HMI Behaviour Pattern V-3**（`Push Button Control`）—— 該 pattern 之定義在 Core HMI 之行為樣式表，屬**外部規格**，依 canon **§8.4.2**（R-CAM13(b)）不測其內容；本列只驗該控制項**是 push button 型**：按下不觸發、放開才觸發（push button 與 toggle／latch 之可觀察差別）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The shift lever is in P
4. The AUX camera soft controls are displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press and hold the AUX 1 soft control without releasing
2. Read the HU display and check that the AUX 1 view has not yet been activated
3. Release the AUX 1 soft control
4. Read the HU display and check that the AUX 1 view is displayed
```

## expected_result

```
1. The AUX 1 soft control shows its pressed state
2. The AUX 1 view is not yet displayed while the control is held
3. The AUX 1 soft control is released
4. The AUX 1 view is displayed
```
