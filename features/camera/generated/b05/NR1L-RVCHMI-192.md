# NR1L-RVCHMI-192 — SWE1-RVC-035

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.8`（來源列 `NRL-142643`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC7) The PAM graphic will be based on the current vehicle and be provided on PDO graphical releases.

## reasoning

§8.8 之 `based on the current vehicle` 為可觀察（車輛輪廓與感測區），`be provided on PDO graphical releases` 為**交付管道**之陳述（PDO 為圖資釋出流程），非 HMI 行為，**不造其判準**（§8.4.1）。與 `-193`（§11.1）之分工：後者驗**隨 proxy 適配**（兩組態之差異），本列驗**與本車相符**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. PROXI PAM_Configuration = 0 (Rear)
5. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the PAM graphic and check the vehicle outline it draws
2. Read the PAM graphic and check which sensor zones it draws
```

## expected_result

```
1. The vehicle outline in the PAM graphic is the outline of the vehicle under test
2. The sensor zones in the PAM graphic are the rear zones only
```
