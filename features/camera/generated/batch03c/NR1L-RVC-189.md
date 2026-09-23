# NR1L-RVC-189 — SWE-CAM-004

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V33_P226MCA_VF_351`（來源列 `SYS-RA-VF551_V33-429`）

## test_item 上半（verbatim，SYS2 逐字）

> If the LTM_OperationalModeSts.Info=="Ignition On" or LTM_OperationalModeSts.Info=="Ignition_On_EngOn", LTM receives the signal STATUS_CCAN3.VehicleSpeedVSOSigFailSts="Fail Present" for a time greater than a threshold calibrated "TIME_W_RVC" LTM must: Store an appropriate DTC according to the rules contained in the document aimed to validate the diagnosis.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-429` 之「`VehicleSpeedVSOSigFailSts = "Fail Present"` 持續逾門檻時設 DTC」。上半為摘句（§4.3.1）：原句 65 token 逾 50。**門檻值取 `TIME_W_RVC` ＝ 2,5 sec**（V33 §1.14.1 `-515`／`-516`／`-519`，profile §9）。`VehicleSpeedVSOSigFailSts` 於 P363／637MCA 兩本實測為 `32|1@0+ (1,0)` 之單位元旗標；**2261 之 DBC 不在素材**（DR-CAM-f 之範圍），raw `1` 依該兩本之位元語意書寫。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. LTM_OperationalModeSts.Info = "Ignition On"
4. PENDING: DR-CAM-q the DTC that the specification defines for the speed fail status is not sourced
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN3.VehicleSpeedVSOSigFailSts = 1 (Fail Present)
2. Hold for 2,5 s
3. Read the DTC list with the diagnostic tool and check the DTC state
```

## expected_result

```
1. STATUS_CCAN3.VehicleSpeedVSOSigFailSts = 1 (Fail Present) is sent
2. The signal is held for 2,5 s
3. A DTC is set for the speed fail status
```
