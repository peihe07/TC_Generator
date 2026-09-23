# NR1L-RVCHMI-184 — SWE1-RVC-039

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_9.2.3`（來源列 `NRL-142649`）

## test_item 上半（verbatim，SYS1 逐字）

> RVCF2.3) Display “Camera Out of Position” message for any event related to other diagnosable events which places the camera out of normal positions

## reasoning

§9.2.3 之訊息 `“Camera Out of Position”` 為來源逐字，惟**彈窗表查無** ——掃描字串 `out of position`／`not in position` 於 `forms/Pop Up List HMI R1 (26PI).xlsx` 全欄 **0 命中**（本輪重測，與 `popup_texts.tsv` 首兩列之既有記載一致）→ **`PENDING: DR-CAM-h`**（該條之第 (1) 項即此）。ER 仍以來源之逐字書寫，待 DR 結後確認其最終文字。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in R
4. The camera has been moved out of its normal position
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display and check the message text
2. Return the camera to its normal position and read the HU display
```

## expected_result

```
1. PENDING: DR-CAM-h the display reads "Camera Out of Position"; that string is not in the R1 HMI pop-up list
2. The rear view camera image is displayed again once the camera is back in position
```
