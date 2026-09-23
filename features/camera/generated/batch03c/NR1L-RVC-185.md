# NR1L-RVC-185 — SWE-CAM-004

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1821`（來源列 `SYS-RA-VF551_V2-205`）

## test_item 上半（verbatim，SYS2 逐字）

> When Ignition is On AND the gear status is no longer "SNA" the Head Unit shall: o heal the DTC. o RVCM and Head Unit functionalities revert back to operating conditions as per Functional Requirements.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-205` 之「點火為 On 且檔位不再為 SNA 時，HU 治癒（heal）該 DTC 並使功能回復」。`SYS-RA-VF551_V2-208` 與本列**逐字同句**（同本之另一節），依同義列不另出 TC，plan 記 covered_by。「檔位為 SNA」以**停送 `TRANSM_FD_4`** 表達（訊號逾時即 SNA，不需注入 raw 15）。點火之 On 態由 `The HU is in the Full-Operation state` 承載（profile §4.1）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. TRANSM_FD_4 is not transmitted on the bus so that the gear status is SNA
4. A DTC is set for the gear status
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 1 (P)
2. Read the DTC list with the diagnostic tool and check the DTC state
3. Read the HU display and check that the camera functions are available again
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 1 (P) is sent and the gear status is no longer SNA
2. The DTC is healed and is no longer present
3. The RVCM and Head Unit functionalities operate as per the Functional Requirements
```
