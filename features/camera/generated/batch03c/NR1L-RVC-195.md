# NR1L-RVC-195 — SWE-CAM-004

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V42_P637MCA_VF_2132`（來源列 `SYS-RA-VF551_V42-595`）

## test_item 上半（verbatim，SYS2 逐字）

> IF LTM_OperationalModeSts.Info is equal to "Ignition_On" or "Ignition_On_Prplsn_On" AND the LTM does not receive the STATUS_BH_BCM1 message for a time greater than TIME_W_RVC, LTM shall: consider the signal STATUS_BH_BCM1.RHatchSts equal to "Closed" Set a specific DTC as long as the failure persists, according to the "TLM Diagnostic Requirement" document

## reasoning

驗證目標為 `SYS-RA-VF551_V42-595` 之「`STATUS_BH_BCM1` 逾 `TIME_W_RVC` 未收到時之回退與 DTC」。原句 49 token，未逾 50。**門檻值取 V42 之 `TIME_W_RVC` ＝ 2,5 sec**（V42 §1.14.1 `-667`／`-668`／`-671`）。`STATUS_BH_BCM1`（`BO_ 854`）於 637MCA 本實測存在。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. LTM_OperationalModeSts.Info = "Ignition_On"
4. PENDING: DR-CAM-q the specific DTC that the specification lists is not sourced
```

## input_test_data

`NA`

## test_procedure

```
1. Stop transmitting STATUS_BH_BCM1 on the bus
2. Hold for 2,5 s
3. Read the DTC list with the diagnostic tool and check the DTC state
```

## expected_result

```
1. STATUS_BH_BCM1 is no longer received by the LTM
2. The message is absent for 2,5 s
3. A specific DTC is set for the missing message
```
