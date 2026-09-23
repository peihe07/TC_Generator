# NR1L-RVC-054 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_507`（來源列 `SYS-RA-VF551_V3-251`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall implement a warning text overlay that displays the text, "Check Entire Surroundings" for five seconds in the upper center of the display per the HMI definition when Head Unit transition from non camera display to camera display.

## reasoning

驗證目標同 `NR1L-RVC-053` 而為 V3（376）之逐字條文。上半為摘句（§4.3.1）：原句 88 token，刪 `This warning text shall be …18 arc minutes.`（17 token）與 `a)` 子句（34 token），摘後 37 token；為原句之保序子序列，條件（自非相機畫面切入）與結果（疊加文字五秒）兩子句皆保留。`a)` 子句（顯示不足 5 秒即移除）由 `NR1L-RVC-055` 承接。**只勾 376** —— 637 之同義條文為 `SYS-RA-VF551_V42-230`（另出 `-056`）、2261 為 `V33-233`（文字相異，`-057`），三者不可折。排檔訊號依 Atl-Mi 側之 `STATUS_CCAN4.ReverseGearSts` （`NR1L-RVC-021` 之 CAN source 行已鎖定該對應）。

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
2. Read the upper center of the HU display within 5 s and check the warning text
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
2. The text "Check Entire Surroundings" is overlaid on the upper center of the display
```
