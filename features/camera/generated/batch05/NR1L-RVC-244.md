# NR1L-RVC-244 — SWE-CAM-019

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V33_P226MCA_VF_1115`（來源列 `SYS-RA-VF551_V33-234`）

## test_item 上半（verbatim，SYS2 逐字）

> When the rear images are displayed on TLM_Display.GUI the setted brightness must be over 50%, in order to visualize better the images

## reasoning

**補生成之由**：拆解審計 **CAM-23 §3 #3**（`confidence = M`）—— `over 50%` 之邊界未夾（母列 `NR1L-RVC-214` 只判「高於 50 %」而未取具體點）。本列取**上界之 on-point 51 %**。與 `-245`（49 %，下界之 off-point）成一對。亮度之量測須亮度計（母列本即列於 `bench_verify.md`，本對兩列同列）。車型只勾 2261 —— 同母列（V33 之錨 `P226MCA`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU display brightness is set to 51 %
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Measure the brightness of the displayed rear image on the HU display
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear image is displayed
2. The measured brightness is 51 %, which is over the 50 % required by the source
```
