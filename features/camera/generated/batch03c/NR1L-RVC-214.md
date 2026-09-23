# NR1L-RVC-214 — SWE-CAM-019

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V33_P226MCA_VF_1115`（來源列 `SYS-RA-VF551_V33-234`）

## test_item 上半（verbatim，SYS2 逐字）

> When the rear images are displayed on TLM_Display.GUI the setted brightness must be over 50%, in order to visualize better the images (refers to FMVSS 111 and according to ECE-REG46 regulations).

## reasoning

驗證目標為 `SYS-RA-VF551_V33-234` 之「rear 影像顯示於 `TLM_Display.GUI` 時，亮度須超過 50 %（FMVSS 111 與 ECE-REG46）」。**量測手段來源未載，不造工具**（§8.4.1）—— procedure 只寫 `Read the brightness … and check its level`，由人工以亮度治具量測；本列已列入 `bench_verify.md`。來源之 `setted` 為 SYS2 之拼寫，依逐字原則不更正。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read the brightness of the displayed rear image on the HU display and check its level
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear image is displayed
2. The brightness of the displayed rear image is over 50 %
```
