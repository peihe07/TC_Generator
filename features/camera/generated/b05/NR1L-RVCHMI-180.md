# NR1L-RVCHMI-180 — SWE1-RVC-032

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.4.1`（來源列 `NRL-142639`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC3.1) The message/button overlaid execution should only be performed when there is no other option to fit every UI element on the screen.

## reasoning

§8.4.1 之 `only ... when there is no other option to fit` 之否定側須以**版面足夠大**之機型驗之，故前提取 `Radio_Display_Type = 7`（12 吋直式，byte 185 值域逐字 `7 = 12" 1200x1920`）——該尺寸為本表之最大者之一，最可能容得下全部元素。**本列之判為條件式**：若該機型仍疊層，即表示「無其他選項」之判斷不同，須回報而非判 FAIL；此點記入 `bench_verify.md`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Radio_Display_Type = 7 (12" 1200x1920)
4. The shift lever is in R
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the camera view and check where the UI elements are placed
2. Read the camera view and check that no element is overlaid on the camera image
```

## expected_result

```
1. The UI elements are placed outside the camera image because the display is large enough to fit them
2. No element is overlaid on the camera image
```
