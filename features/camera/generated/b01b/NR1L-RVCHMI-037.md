# NR1L-RVCHMI-037 — SWE1-RVC-023-03

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.5.3`（來源列 `NRL-142629`）

## test_item 上半（verbatim，SYS1 逐字）

> “X” soft control is pressed (PU0361). The user has the ability to press this soft control to close the camera at any time during the 10 seconds/speed threshold.

## reasoning

§7.5.3 之第三分支。verbatim 為該列 Description 之保序子序列 —— 刪去 `In ANY OTHER GEAR, the camera image will display an “X” in the upper right corner of the screen.` 一句（該句之位置驗證由 `-038` 承接，不重複）。`X` 之彈窗編號 `PU0361` 取 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁 —— 該列之 `Timeout` 欄為 `10`（與本條之 10 秒相符）、文字欄逐字 `A clear ‘X’ exit button is available in any gear.`；惟其 module 欄為 `Cargo Camera` 而非 RVC，記於 `remarks`（**profile §10** 第二類）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. The shift lever has just been moved from R to D
5. The rear view camera image is displayed during the delay
```

## input_test_data

`NA`

## test_procedure

```
1. Read the camera image and check that the "X" soft control is available
2. Press the "X" soft control
3. Read the HU display and check that the camera image is turned off
```

## expected_result

```
1. The "X" soft control is shown on the camera image
2. The "X" soft control registers the press
3. The camera image is turned off and the last known HU display is shown again
```

## remarks

Popup PU0361 is listed under the Cargo Camera module in the Pop Up List; SYS1 RVC+PAM 7.5.3 cites it for the rear view camera.
