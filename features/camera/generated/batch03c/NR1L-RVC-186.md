# NR1L-RVC-186 — SWE-CAM-004

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_123`（來源列 `SYS-RA-VF551_V3-527`）

## test_item 上半（verbatim，SYS2 逐字）

> · If Head Unit receives the systemStatus.InternalErrorStatus signal equal to True the Head Unit shall: o Set a DTC Once the systemStatus.InternalErrorStatus signal is set to False, the Head Unit shall: o Clear the DTC

## reasoning

驗證目標為 `SYS-RA-VF551_V3-527` 之 Atl-Mi 條文。**與 Atl-Hi 之差別在條文結構** —— V2 將 set 與 clear 分為兩列（`-221`／`-220` 等），V3 **一句涵蓋兩側**，故本列以四步走完 True → False 之一輪（§5.7 同一驗證目標之多行 ER），不拆為兩列。依 **R-CAM15(b)**：V42 於同一驗證點有對應條文（`-583`～`-589`），V3 列只承 376。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。**`systemStatus.*` 為 RVCM → HU 之 LVDS 訊號**（四本 DBC 零命中），其注入須 LVDS 模擬器；該能力之確認已在 `bench_verify.md`（DECISIONS 6-38 之同一項）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
4. PENDING: DR-CAM-q the DTC that the specification defines for InternalErrorStatus is not sourced
```

## input_test_data

`NA`

## test_procedure

```
1. Set the LVDS signal systemStatus.InternalErrorStatus = True
2. Read the DTC list with the diagnostic tool and check the DTC state
3. Set the LVDS signal systemStatus.InternalErrorStatus = False
4. Read the DTC list with the diagnostic tool and check the DTC state
```

## expected_result

```
1. The LVDS signal systemStatus.InternalErrorStatus = True is received by the HU
2. A DTC is set for InternalErrorStatus
3. The LVDS signal systemStatus.InternalErrorStatus = False is received by the HU
4. The DTC for InternalErrorStatus is no longer present
```
