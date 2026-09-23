# NR1L-RVCHMI-210 — SWE1-RVC-116

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.3`（來源列 `NRL-188130`）

## test_item 上半（verbatim，SYS1 逐字）

> The pop-up updates to show the confirmation screen above. else pop-up dismissed automatically after 5 seconds.

## reasoning

**補正之由**：**CAM-24 審閱 §一-1** —— canon **§8.3**（boundary 每點一 TC）與**§5.7**（不同觸發須拆）勝於本 feature 之既有前例；母列 `NR1L-RVCHMI-142` 原含多點／多觸發，已原地收斂為單點，本列承接其餘者。母列之 reasoning 已註本列之 ID。分析層記一筆：該形制經批次審閱而未抓（**A-CA37**）。§30.1.3 之第三條清除路徑（逾時自動）。**5 秒為 timeout 而非門檻**，故**不夾 4／6 兩點**（下放包 §2 明載此判），只取逾時後之觀察點 6 秒（＋1 秒為人工可達之窗，見 `bench_verify.md`）。verbatim 為該列 Description 之保序子序列（刪 `User presses OK or‘X’to clear,`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The confirmation pop-up is displayed after "Make Favorite" was pressed
4. The timestamp at which the pop-up appeared has been recorded
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display 6 seconds after the recorded timestamp without any user input
2. Read the HU display and check that no user input was needed to clear the pop-up
```

## expected_result

```
1. The confirmation pop-up is cleared 6 seconds after it appeared
2. The pop-up was cleared without any user input, which is the automatic dismissal
```
