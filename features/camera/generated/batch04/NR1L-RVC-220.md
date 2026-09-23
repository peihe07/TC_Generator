# NR1L-RVC-220 — SWE-CAM-021

- **Test Group**：Rear View Camera｜**Test Set**：HMI Overlays
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1682`（來源列 `SYS-RA-VF551_V2-505`）

## test_item 上半（verbatim，SYS2 逐字）

> If the Head Unit Audio Mode is OFF, then the non-entertainment features shall be functional as per the Head Unit Audio Mode OFF behavior.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-505` 之 Audio Mode OFF 行為（V2 本）。**與 `NR1L-RVC-116` 之關係**：該列之來源為 `SYS-RA-VF551_V4-138`（**逐字同句但屬 V4 本**），承接列為 `SWE-CAM-003`；本列之來源屬 V2 本、承接列為 `SWE-CAM-021`。依 R-CAM10 兩者各歸其列，**不互相委派**（委派只在同一來源被多列共引時成立）。「依…之行為」為轉指，其細目在 Audio 線之規格，不展開（§8.4.2）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU is in Audio Mode OFF
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display and check that the non-entertainment features are functional
2. Read the HU display and check that the rear view camera image is not interrupted
```

## expected_result

```
1. The non-entertainment features are functional as per the Head Unit Audio Mode OFF behavior
2. The rear view camera image is not interrupted
```
