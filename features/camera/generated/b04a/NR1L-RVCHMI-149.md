# NR1L-RVCHMI-149 — SWE1-RVC-121-01

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_31.1.2`（來源列 `NRL-188137`）

## test_item 上半（verbatim，SYS1 逐字）

> The pop-up updates to show a full QWERTY keyboard.

## reasoning

§31.1.2 載三個驗證點（鍵盤顯示、開始輸入即覆寫預設名、按 OK 確認），三列各驗一個。`full QWERTY` 為逐字；不驗個別按鍵之配置（Core HMI 之鍵盤規格為外部規格，§8.4.2）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The "Edit Name" soft control has been pressed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the pop-up and check that a full QWERTY keyboard is shown
2. Read the keyboard and check that the letter keys A to Z are all present
```

## expected_result

```
1. A full QWERTY keyboard is shown in the pop-up
2. The letter keys A to Z are all present, which is what makes the keyboard full
```
