# NR1L-RVC-057 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1142`（來源列 `SYS-RA-VF551_V33-233`）

## test_item 上半（verbatim，SYS2 逐字）

> LTM overlaps the related message on the RVC images ( "Check surroundings for safety" see LTM HMI specification document) for T_INITDISPLAY time, as indicated in "HMI System Technical Specification"

## reasoning

驗證目標為 `SYS-RA-VF551_V33-233` 之 2261 分支。**畫面文字與他平台相異** —— V2／V3／V42 為 `Check Entire Surroundings`，V33 為 `Check surroundings for safety`，逐字不同即不可折（§8.4.1 literal 各歸各源）。`T_INITDISPLAY` 之標定值為 **5,0 sec**（V33 §1.14.1 `SYS-RA-VF551_V33-479` 名／`-480` 值／`-483` 單位；V42 同值 `-631`／`-632`／`-635`），與 V2／V3 之 `for five seconds` 同數，ER 因而以 5 秒書寫。來源末之 `as indicated in "HMI System Technical Specification"` 為轉指，該文件未入本 feature 之素材；依 R-CAM13(b) 其為 037 所引之條文故生成，轉指之細節不入 ER（§8.4.2）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read the HU display within 5 s of the image appearing and check the message overlaid on the rear view camera image
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
2. The message "Check surroundings for safety" is overlaid on the rear view camera image for 5 s
```
