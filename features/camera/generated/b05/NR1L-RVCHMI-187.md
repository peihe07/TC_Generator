# NR1L-RVCHMI-187 — SWE1-RVC-002-02

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.2.1`（來源列 `NRL-142607`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM2.1) the addition of a new functionality will add the associated visualization logic to the system

## reasoning

§6.2.1 之後半（`the addition of a new functionality will add the associated visualization logic`）。與 `-186` 之分工：後者驗**並存**（靜態），本列驗**加入即增其視覺**（動態）；與 `-185`（§6.2）之分工：該列驗**內容由 proxy 決定**（兩組態之內容不同），本列驗**增量之關聯性**（新增功能帶入其視覺邏輯）。

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
1. Read the RVC+PAM layout and check that only the rear PAM visualization is shown
2. Set PROXI PAM_Configuration = 1 (Front And Rear)
3. Read the RVC+PAM layout and check that the front PAM visualization has been added
```

## expected_result

```
1. Only the rear PAM visualization is shown
2. PROXI PAM_Configuration = 1 (Front And Rear) is applied
3. The front PAM visualization is now shown in addition to the rear one
```
