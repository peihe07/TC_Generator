# NR1L-RVCHMI-142 — SWE1-RVC-116

- **Test Group**：Rear View Camera｜**Test Set**：AUX Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_30.1.3`（來源列 `NRL-188130`）

## test_item 上半（verbatim，SYS1 逐字）

> The pop-up updates to show the confirmation screen above. User presses OK or‘X’to clear, else pop-up dismissed automatically after 5 seconds.

## reasoning

§30.1.3 逐字載**三**條清除路徑（`OK`／`‘X’`／`after 5 seconds` 自動），三者皆驗。`5 seconds` 為來源逐字，觀察點取 6 秒（＋1 秒為人工可達之窗，見 `bench_verify.md`）。`the confirmation screen above` 指該列之圖（`image159.png`），其內容不可抽，故 ER 只判彈窗之**出現與清除**，**不造其文字**（§8.4.1）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. A wired AUX camera is connected
3. The confirmation pop-up is displayed after "Make Favorite" was pressed
```

## input_test_data

`NA`

## test_procedure

```
1. Press OK on the confirmation pop-up
2. Read the HU display and check that the pop-up is cleared
3. Press "Make Favorite" again and press ‘X’ on the confirmation pop-up
4. Read the HU display and check that the pop-up is cleared
5. Press "Make Favorite" again and record the timestamp
6. Read the HU display 6 seconds after the recorded timestamp and check that the pop-up is cleared
```

## expected_result

```
1. OK registers the press
2. The confirmation pop-up is cleared
3. ‘X’ registers the press
4. The confirmation pop-up is cleared
5. The confirmation pop-up is displayed and its timestamp is recorded
6. The confirmation pop-up is cleared without any user input 6 seconds after it appeared
```
