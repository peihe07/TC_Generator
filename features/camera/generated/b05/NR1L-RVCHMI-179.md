# NR1L-RVCHMI-179 — SWE1-RVC-031-02

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.4`（來源列 `NRL-142638`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC3) Any button or object overlaid on camera image is 60% transparency with +/- 5% variation.

## reasoning

§8.4 之後半。`60% transparency with +/- 5% variation` 逐字 → 容許區間 55–65%，故 ER 以區間書寫（**邊界值分析**）。透明度之量測須影像分析治具，記入 `bench_verify.md`。verbatim 為該列 Description 之保序子序列（刪前半句，由 `-178` 承接）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The "Rear View Camera Delay" setting is On
4. The shift lever is in D
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Measure the transparency of the "X" exit button overlaid on the camera image
2. Measure the transparency of the banner overlaid on the camera image
```

## expected_result

```
1. The transparency of the "X" exit button is between 55 percent and 65 percent
2. The transparency of the banner is between 55 percent and 65 percent
```
