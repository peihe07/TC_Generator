# NR1L-RVCHMI-182 — SWE1-RVC-037

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_9.2.1`（來源列 `NRL-142647`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCF2.1) Display “Camera System Unavailable” error message screen for any event that prevents the camera feed from being displayed

## reasoning

§9.2.1 之 `any event that prevents the camera feed` —— 取 **LVDS 影像鏈路中斷**為該事件之實例（A 本 `NR1L-RVC-196` 等五列已用同一手段，`bench_verify.md` 有其治具項）。訊息逐字取 `PU0169`（module `Rearview Camera`，文字欄 `Camera System Unavailable`）；`PU0170` 為同訊息之含 `<X>` 版本（B01b `-038` 已引其 X 位置）。與 `-183`（§9.2.2）之分工：後者之條件為 `blue screen condition`（**畫面型態**），本列為 `prevents the camera feed`（**成因**）；兩列之來源列不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in R
4. The LVDS video link between the RVCM and the HU has been disconnected
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display and check the message text
2. Reconnect the LVDS video link and read the HU display
```

## expected_result

```
1. The display reads "Camera System Unavailable" (PU0169 of the R1 HMI pop-up list)
2. The rear view camera image is displayed again once the feed is restored
```
