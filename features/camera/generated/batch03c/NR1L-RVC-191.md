# NR1L-RVC-191 — SWE-CAM-004

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_1993`（來源列 `SYS-RA-VF551_V42-584`）

## test_item 上半（verbatim，SYS2 逐字）

> Once the systemStatus.InternalErrorStatus signal is set to "False", LTM shall: set the DTC to not present according to the "TLM Diagnostic Requirement" document.

## reasoning

驗證目標為 `SYS-RA-VF551_V42-584` 之 637 條文。**`SYS-RA-VF551_V42-590` 與本列逐字同句**（其節為 Communications 之清除側，句子卻寫 `InternalErrorStatus`）—— plan 記 covered_by 本列，**Communications 之清除側因而無條文可依，不造**（RDF-10）。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。**`systemStatus.*` 為 RVCM → HU 之 LVDS 訊號**（四本 DBC 零命中），其注入須 LVDS 模擬器；該能力之確認已在 `bench_verify.md`（DECISIONS 6-38 之同一項）。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. LTM_OperationalModeSts.Info = "Ignition_On"
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
5. The DTC for InternalErrorStatus is set
```

## input_test_data

`NA`

## test_procedure

```
1. Set the LVDS signal systemStatus.InternalErrorStatus = False
2. Read the DTC list with the diagnostic tool and check the DTC state
```

## expected_result

```
1. The LVDS signal systemStatus.InternalErrorStatus = False is received by the LTM
2. The DTC for InternalErrorStatus is set to not present
```
