# NR1L-RVCHMI-175 — SWE1-RVC-028

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.3.1`（來源列 `NRL-142635`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC2.2) The fade out banner will apply to any message/error that appears where “Check Entire Surroundings” appears

## reasoning

§8.3.1 之驗證點為**該淡出樣式適用於同位置之任何訊息**，故須以**非** Check Entire Surroundings 之訊息驗之；取 §9.2.1 之 `Camera System Unavailable`（`-182` 所驗）為該訊息。與 `-174`（§8.3）之分工：後者驗**該 banner 本身**之淡出與不遮蓋，本列驗**樣式之適用範圍**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. A camera fault has been injected so that an error message is shown
```

## input_test_data

`NA`

## test_procedure

```
1. Read the error message and check that it appears in the same position as the "Check Entire Surroundings" banner
2. Read the error message and check that it fades out towards the edges of the display
```

## expected_result

```
1. The error message appears in the same position as the Check Entire Surroundings banner
2. The error message fades out towards the edges of the display
```
