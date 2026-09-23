# NR1L-RVC-209 — SWE-CAM-006

- **Test Group**：Rear View Camera｜**Test Set**：Video Pipeline
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：邊界值分析 (Boundary Value Analysis, BVA)
- **specification_reference**：`VF551_V42_P637MCA_VF_1777`（來源列 `SYS-RA-VF551_V42-216`）

## test_item 上半（verbatim，SYS2 逐字）

> LTM shall send PowerShutDownNotification.Power _Down equal to "False" to the RVCM over LVDS and provide power to the RVCM within Time_POWER LTM shall start to read ADAS_LVDS_RRCamera_Cable LTM shall start to read the Rear_Camera_DelayOff.Req

## reasoning

驗證目標為 `SYS-RA-VF551_V42-216` 之「送 `Power_Down = "False"`、於 `Time_POWER` 內供電、並開始讀取 `ADAS_LVDS_RRCamera_Cable`」。原句 34 token，未逾 50。**`Time_POWER` ＝ 500 ms**（V42 §1.14.1 `-739`／`-740`／`-743`）。**本列即 `SWE-CAM-012`／`-014` 之委派對象**（R-CAM10：`-006` 之 SWE ID 較小）——`NR1L-RVC-069`～`-072` 之 Atl-Hi／Atl-Mi 條文與本列之 637 條文各歸其本。LVDS 之觀察不造命令（profile §7.3）。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read the bus analyzer recording and check the PowerShutDownNotification message
3. Read the bus analyzer recording and check the time between step 1 and the supply to the RVCM
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
2. PowerShutDownNotification.Power_Down = False is sent over LVDS to the RVCM
3. The LTM supplies power to the RVCM within 500 ms of step 1
```
