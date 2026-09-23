# NR1L-RVC-089 — SWE-CAM-002

- **Test Group**：Rear View Camera｜**Test Set**：Configuration
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_1455`（來源列 `SYS-RA-VF551_V3-258`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall transmit current display status using internal signal Rear_Camera_Enable.Info equal to FALSE when the rear camera is not being displayed. · The Head Unit shall transmit current display status using internal signal Rear_Camera_Enable.Info equal to TRUE when the rear camera is being displayed.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-258` 之 `Rear_Camera_Enable.Info = FALSE` 側（相機未顯示時）。**`Rear_Camera_Enable.Info` 為內部訊號**（來源自稱 `internal signal`；四本 DBC 零命中），不可於匯流排觀察，依 §6 以畫面之可判後果書寫 —— 兩列之差別在觸發與畫面結果，ER 第 2 項之措辭對應來源之 `transmit current display status … equal to FALSE when the rear camera is not being displayed`。兩來源句於同一列（`-258` 為兩句一列），依 §8.3 之狀態軸各出一 TC。依 R-CAM15(a)（V42／V33 無對應條文）承三個 Atl-Mi 平台。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. The shift lever is in P
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the top right corner of the HU display
2. Read the HU display and check the rear view camera image
```

## expected_result

```
1. The rear view camera image is closed
2. The HU reports its current display status as not being displayed
```
