# NR1L-RVC-197 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_931`（來源列 `SYS-RA-VF551_V2-212`）

## test_item 上半（verbatim，SYS2 逐字）

> When Ignition is On AND the head unit does not receive LVDS Video Signal and ADAS_LVDS_RRCamera_Cable signal, the Head Unit shall: - Set the DTC to True - Display HMI as defined in the "HMI camera Logic and Flow" document.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-212` 之「點火為 On 而 HU 未收到 LVDS Video Signal 與 `ADAS_LVDS_RRCamera_Cable` 時，設 DTC 並依 HMI 文件顯示畫面」。**畫面之具體內容轉指 `"HMI camera Logic and Flow"`** —— 該文件不在素材，ER 只判「顯示該文件所定義之失效畫面」而不比對字串（§8.4.2）。回復側由 `NR1L-RVC-198` 承接。**DTC 之識別碼無來源** —— 來源只寫「as defined in the DTC Criteria Matrix」／「as listed in the "TLM Diagnostic Requirement" document」，該兩份文件不在本 feature 之素材；ER 因而只判「有／無 DTC」而不指名碼值，缺碼標 `PENDING: DR-CAM-q`（本輪新開）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。

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
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
4. Read the HU display and check what it shows
```

## expected_result

```
1. Neither the LVDS Video Signal nor the ADAS_LVDS_RRCamera_Cable signal is received by the HU
2. The DTC is set to True
3. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
4. The HU shows the screen that the "HMI camera Logic and Flow" document defines for this failure
```
