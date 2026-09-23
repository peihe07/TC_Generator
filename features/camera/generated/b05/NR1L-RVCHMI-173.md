# NR1L-RVCHMI-173 — SWE1-RVC-026

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.2`（來源列 `NRL-142633`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC2) When the Head Unit (HU) transitions the display to any camera image, a message stating “Check Entire Surroundings” (PU0362) will be displayed for 5 seconds

## reasoning

§8.2 逐字載彈窗號 `(PU0362)` 與時限 `5 seconds`。實測 `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` r365 之 `PU0362`（module `Surround View Camera`）：文字欄逐字 `Check Entire Surroundings`（相符），**惟 Timeout 欄為 `10`**，與來源之 `5 seconds` **相左** → 依 **§4.3.1** 以 SYS1 為準，差異記於 `Remarks` 並登 **RDF-16**。`any camera image` 之 `any` 由本列（後視）與 B02a `-100`（§28.2.1，AUX）分別驗；兩列之來源本與承接列皆不同（**R-CAM10**）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: TRANSM_FD_4.ShiftLeverPosition (HDCC27, DT27) / STATUS_CCAN4.ReverseGearSts (637, 2261, 376)
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R) and record the timestamp
2. Read the HU display and check the message text
3. Read the HU display 4 seconds after the recorded timestamp and check that the message is still shown
4. Read the HU display 6 seconds after the recorded timestamp and check that the message is no longer shown
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent and the rear view camera image is displayed
2. The message reads "Check Entire Surroundings" (PU0362 of the R1 HMI pop-up list)
3. The message is still shown 4 seconds after the transition
4. The message is no longer shown 6 seconds after the transition
```

## remarks

SYS1 8.2 and 9.2 state 5 seconds; the Pop Up List Timeout column for PU0362 reads 10. ER follows SYS1. See RDF-16.
