# NR1L-RVC-183 — SWE-CAM-004

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_927`（來源列 `SYS-RA-VF551_V2-215`）

## test_item 上半（verbatim，SYS2 逐字）

> · When Ignition is On AND the Head Unit receives the systemStatus.Communications_Timeout signal equal to True, the Head Unit shall: o Set the DTC as defined in the DTC Criteria Matrix

## reasoning

驗證目標為 `SYS-RA-VF551_V2-215` 之「`systemStatus.Communications_Timeout` 為 `True` 時，HU 設定 DTC」。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。**`systemStatus.*` 為 RVCM → HU 之 LVDS 訊號**（四本 DBC 零命中），其注入須 LVDS 模擬器；該能力之確認已在 `bench_verify.md`（DECISIONS 6-38 之同一項）。與其配對之清除側由 `NR1L-RVC-183` 之 sibling 承接（§8.3 每點一 TC）。設定側之前提取「尚未有該 DTC」、清除側取「該 DTC 已設」，兩者互為對方之後果。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
4. PENDING: DR-CAM-q the DTC that the DTC Criteria Matrix defines for Communications_Timeout is not sourced
```

## input_test_data

`NA`

## test_procedure

```
1. Set the LVDS signal systemStatus.Communications_Timeout = True
2. Read the DTC list with the diagnostic tool and check the DTC state
```

## expected_result

```
1. The LVDS signal systemStatus.Communications_Timeout = True is received by the HU
2. A DTC is set for Communications_Timeout
```
