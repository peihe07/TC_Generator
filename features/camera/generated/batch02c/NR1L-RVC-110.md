# NR1L-RVC-110 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_1646`（來源列 `SYS-RA-VF551_V33-443`）

## test_item 上半（verbatim，SYS2 逐字）

> If the LTM_OperationalModeSts.Info=="Ignition_On" OR LTM_OperationalModeSts.Info=="Ignition_On_EngOn", LTM does not receive the messages BED_EXTENDER for a time greater than a threshold calibrated "TIME_W_RVC" LTM must: use the last known valid of BED_EXTENDER.BedExtenderSts and BED_EXTENDER.IncompleteBedExtenderSts signal.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-443` 之「BED_EXTENDER 逾時時，LTM 沿用 `BedExtenderSts`／`IncompleteBedExtenderSts` 之最後有效值」。**`BED_EXTENDER` 不在四本 DBC**（A-CA29／DR-CAM-f），raw 與 VAL label 標 PENDING。**逾時門檻 `TIME_W_RVC` ＝ 2,5 sec**（V33 §1.14.1 `-515` 名／`-516` 值／`-519` 單位），故以「停送逾 2,5 s」表達；停送不需知 raw，本列因而較 `-109` 可執行。兩列與 `NR1L-RVC-032`／`-033`（抑制影像）之分工：後者驗 BedExtender **有效值**之效果，本二列驗其**失效／逾時**之回退策略（§8.2.1）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-f the BED_EXTENDER message is not present in the four DBC files in forms
4. LTM_OperationalModeSts.Info = "Ignition_On"
5. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Stop transmitting the BED_EXTENDER message for more than 2,5 s
2. Read the HU display and check the rear view camera image
```

## expected_result

```
1. The BED_EXTENDER message is no longer received for more than 2,5 s
2. The rear view camera image keeps behaving according to the bed extender values that were valid before step 1
```
