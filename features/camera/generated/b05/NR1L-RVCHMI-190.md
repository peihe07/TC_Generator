# NR1L-RVCHMI-190 — SWE1-RVC-005

- **Test Group**：Rear View Camera｜**Test Set**：PAM Integration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_6.4`（來源列 `NRL-142610`）

## test_item 上半（verbatim，SYS1 逐字）

> PAM4) Parksense indications in HU will be consistent with Parksense indications in Cluster

## reasoning

§6.4 之 `consistent` 須以**兩個不同之告警階**驗得，否則兩者恰好同為「無告警」亦算一致。與 `-189`（§6.3）之分工：後者驗**閃爍頻率**，本列驗**告警階之對應**。本列亦須同時觀察兩個顯示器，記入 `bench_verify.md`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI CVPAM_Presence = 1 (Present)
4. The RVC+PAM layout is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Place an obstacle at the far PAM alert distance and read both the HU and the cluster indications
2. Move the obstacle to the near PAM alert distance and read both the HU and the cluster indications
```

## expected_result

```
1. The HU and the cluster show the same PAM alert level at the far distance
2. The HU and the cluster show the same PAM alert level at the near distance
```
