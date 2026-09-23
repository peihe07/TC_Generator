# NR1L-RVC-199 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V3_P363_VF_931`（來源列 `SYS-RA-VF551_V3-533`）

## test_item 上半（verbatim，SYS2 逐字）

> If Head Unit does not receive the LVDS Video Signal, ADAS_LVDS_RRCamera_Cable the Head Unit shall: o Set the DTC to True. o Display appropriate HMI as defined in the "HMI camera Logic and Flow" document.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-533` 之 Atl-Mi 條文。上半為摘句（§4.3.1）：原句 69 token 逾 50。依 **R-CAM15(b)**：V42 於同一驗證點有對應條文（`-592`／`-593`），故 V3 列只承 376。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
4. PENDING: DR-CAM-q the DTC that the specification defines for the missing video is not sourced
```

## input_test_data

`NA`

## test_procedure

```
1. Disconnect the LVDS video link between the RVCM and the HU
2. Read the DTC list with the diagnostic tool and check the DTC state
3. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
4. Read the HU display and check what it shows
```

## expected_result

```
1. Neither the LVDS Video Signal nor the ADAS_LVDS_RRCamera_Cable signal is received by the HU
2. The DTC is set to True
3. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent
4. The HU shows the screen that the "HMI camera Logic and Flow" document defines for this failure
```
