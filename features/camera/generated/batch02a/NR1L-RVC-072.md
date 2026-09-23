# NR1L-RVC-072 — SWE-CAM-014

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_549`（來源列 `SYS-RA-VF551_V3-206`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall send PowerShutDownNotifcation.Power_Down = [True] over LVDS to the RVCM and the radio shall provide power to the RVCM over LVDS for Tpower regardless of the internal power modes of the radio when STATUS_BH_BCM2.CmdIgnSts = [IGN_LK] is received.

## reasoning

驗證目標為 `SYS-RA-VF551_V3-206` —— Atl-Mi 側之關機通知與 `Tpower` 供電保持。**本列為 `SWE-CAM-014` 唯一承接之來源** —— 其六個來源中，`V2-550`／`-553`／`V3-205` 依 R-CAM10 委派 `SWE-CAM-012`、`V42-216` 委派 `SWE-CAM-006`、`V2-582` 為 Out of Scope（R-CAM9），只 `V3-206` 為其獨有（下放包 §3「`-014` 只 `V3-206`」）。`Tpower = 5 sec` 之出處同 `NR1L-RVC-069`（V3 §1.14.1 `-583`／`-584`／`-587`）。與 `-069` 之差別只在平台與訊息名，惟兩本條文逐字相異（V3 將供電與通知寫在同一句、V2 分為 1./2. 兩項），依 R-CAM3 拆列而非 R-CAM3(e) 折行。**LVDS 之觀察不造命令**（升級條件 2 之處置）—— 交付語料 17 本之 `$ ` 命令行 275 條**無一條與 LVDS 相關**（`lvds`／`PowerShutDownNotifcation`／`vehicleUpdate` 三串零命中）；`sources/raw/*sysad*` 之 10 本 docx 亦零命中。故 ER 以 bus analyzer 之訊息名與值書寫，procedure 之觀察步依 §5.4 兩行式但第二行為 bus analyzer 之動作而非 shell 命令。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK)
2. Read the bus analyzer recording and check the PowerShutDownNotifcation message
3. Hold for 5 s and check the supply to the RVCM on the LVDS link
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK) is sent
2. PowerShutDownNotifcation.Power_Down = True is transmitted over LVDS to the RVCM
3. The HU keeps supplying power to the RVCM over LVDS for 5 s
```
