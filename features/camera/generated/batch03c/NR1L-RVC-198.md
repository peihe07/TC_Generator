# NR1L-RVC-198 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1592`（來源列 `SYS-RA-VF551_V2-211`）

## test_item 上半（verbatim，SYS2 逐字）

> When Ignition is On AND the head unit receives LVDS Video Signal, the ETM shall: o heal the DTC. o RVCM and Head Unit functionalities revert back to operating conditions as per Functional Requirements.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-211` 之「點火為 On 且 HU 收到 LVDS Video Signal 時，治癒 DTC 並使功能回復」。與 `-197` 成失效／回復一對。「功能回復」之可判面取影像可再顯示（§6）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The LVDS video link between the RVCM and the HU is disconnected
4. A DTC is set for the missing video
```

## input_test_data

`NA`

## test_procedure

```
1. Reconnect the LVDS video link between the RVCM and the HU
2. Read the DTC list with the diagnostic tool and check the DTC state
3. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
4. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. The LVDS Video Signal is received by the HU again
2. The DTC is healed and is no longer present
3. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
4. The rear view camera image is displayed
```
