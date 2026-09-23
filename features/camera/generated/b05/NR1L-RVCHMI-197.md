# NR1L-RVCHMI-197 — SWE1-RVC-047-02

- **Test Group**：Rear View Camera｜**Test Set**：Camera Settings
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_HeadUnitCameraSystems_HMI_Logic_and_Flow_R1_SR24_Post_2A_v7_(February_10th,_2023)_6.2.2.3`（來源列 `NRL-187343`）

## test_item 上半（verbatim，SYS1 逐字）

> Note: User shall only have the ability to choose one type of guidelines at a time

## reasoning

§6.2.2.3 末之 `Note:` 一句。其可觀察形制為**開一即關另一**（互斥）——以 Active 開著時開 Fixed，驗 Active 自動關閉。verbatim 為該列 Description 之保序子序列（只取 `Note:` 一句，前段由 `-196` 承接）。本列跨兩個設定，故不設「出廠預設」之前提，改直接佈定兩者之初始態。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Active Guidelines" setting is On
4. The "Rear View Camera Fixed Guidelines" setting is Off
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Set "Rear View Camera Fixed Guidelines" = "On"
5. Read the "Camera" list and check the state of "Rear View Camera Active Guidelines"
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. The "Rear View Camera Fixed Guidelines" setting is On
5. The "Rear View Camera Active Guidelines" setting has changed to Off, which shows that only one type of guidelines can be chosen at a time
```
