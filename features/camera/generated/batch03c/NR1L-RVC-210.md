# NR1L-RVC-210 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_1836`（來源列 `SYS-RA-VF551_V42-219`）

## test_item 上半（verbatim，SYS2 逐字）

> send PowerShutDownNotification.Power _Down equal to "True" to the RVCM over LVDS. and it shall provide power to RVCM over LVDS for TPower time regardless of the internal power modes of the radio. stop to read the ADAS_LVDS_RRCamera_Cable

## reasoning

驗證目標為 `SYS-RA-VF551_V42-219` 之「送 `Power_Down = "True"`、於 `TPower` 期間持續供電、並停止讀取 cable」。上半為摘句（§4.3.1）：原句 57 token 逾 50。**`Tpower` ＝ 5 sec**（V42 §1.14.1 `SYS-RA-VF551_V42-703` 名／`-704` 值／`-707` 單位）——與 V2／V3 同值（profile §9）。`Hold for 5 s` 依 §8.7.5(f) 獨立成步。與 `-209` 成開機／關機一對。依 R-CAM15(c)，V42 列承 637。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK)
2. Read the bus analyzer recording and check the PowerShutDownNotification message
3. Hold for 5 s
4. Read the LVDS supply to the RVCM and check that it is still present
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK) is sent and the HU leaves the RUN power state
2. PowerShutDownNotification.Power_Down = True is sent over LVDS to the RVCM
3. The signal is held for 5 s
4. The LTM is still supplying power to the RVCM over LVDS
```
