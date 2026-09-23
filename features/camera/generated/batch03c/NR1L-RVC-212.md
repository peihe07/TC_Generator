# NR1L-RVC-212 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_1996`（來源列 `SYS-RA-VF551_V42-593`）

## test_item 上半（verbatim，SYS2 逐字）

> Once the LTM receives the LVDS Video Signal, LTM shall: set the DTC to not present according to the "TLM Diagnostic Requirement" document. All related functionalities shall revert back to normal operation conditions

## reasoning

驗證目標為 `SYS-RA-VF551_V42-593` 之「收到 LVDS Video Signal 後將 DTC 設為 not present，相關功能回復正常」。與 `-211` 成失效／回復一對。「功能回復」之可判面取影像可再顯示（§6）。DTC 之讀取以散文書寫（profile §7.3）—— 全語料無 DTC 相關之命令句式可抄，**不造命令**。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The LVDS video link between the RVCM and the HU is disconnected
4. A specific DTC is set for the missing video
```

## input_test_data

`NA`

## test_procedure

```
1. Reconnect the LVDS video link between the RVCM and the HU
2. Read the DTC list with the diagnostic tool and check the DTC state
3. Send CAN: STATUS_CCAN5.ShiftLeverPosition = 2 (R)
4. Read the HU display and check that the rearview image is displayed
```

## expected_result

```
1. The LVDS Video Signal is received by the LTM again
2. The DTC is set to not present
3. STATUS_CCAN5.ShiftLeverPosition = 2 (R) is sent
4. The rearview image is displayed and all related functionalities operate normally
```
