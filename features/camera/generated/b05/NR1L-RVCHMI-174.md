# NR1L-RVCHMI-174 — SWE1-RVC-027

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.3`（來源列 `NRL-142634`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC2.1) The banner will fade out towards the edges of the screen as to not cover any potential buttons on the screen, if present

## reasoning

§8.3 之 `as to not cover any potential buttons ... if present` 須有**一個實際存在之按鍵**方驗得，故前提取 D 檔 ＋ delay 開啟（依 §8.1，該情境下 `X` 存在，B01b `-038` 已驗其位置）。ER 末加「可選」一項 —— 未被遮蓋之判準不只是看得見，還須可操作。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. The shift lever is in D
5. The rear view camera image is displayed with the "X" exit button present
```

## input_test_data

`NA`

## test_procedure

```
1. Read the banner and check that it fades out towards the edges of the display
2. Read the "X" exit button and check that it is not covered by the banner
3. Select the "X" exit button
```

## expected_result

```
1. The banner fades out towards the edges of the display
2. The "X" exit button is fully visible and is not covered by the banner
3. The "X" exit button registers the selection
```
