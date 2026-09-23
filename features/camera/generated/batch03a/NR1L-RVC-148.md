# NR1L-RVC-148 — SWE-CAM-010

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2476`（來源列 `SYS-RA-VF551_V42-326`）

## test_item 上半（verbatim，SYS2 逐字）

> LTM shall send: - vehicleUpdate_1.VC_WHL_BASE_LENGTH equal to "Length_3" IF the PROXI parameter Wheelbase is equal to "Long_3800_4050B"

## reasoning

驗證目標為 `SYS-RA-VF551_V42-326` 之 `Length_3` 分支。上半為摘句（§4.3.1）：原句 **73 token** 逾 50，刪其餘四個對映列後為 **17 token**，為原句之保序子序列，`LTM shall send:` 之主句與本分支之 PROXI 值與 LVDS 值皆保留。**本列為 CAM-10 審閱 §一-4 所令之補列** —— 查表對映之每一項為規格明定之獨立輸出，§8.3 之等價類不適用（任一項錯即漏網，§7）；`V42-326` 之五個對映因而全覆蓋，`-145`／`-146` 保留，本列與 `-147`～`-149` 補足其餘三項。PROXI 值取 `Promaster_ATL_MI` row 327 之列舉逐字（`3 = Long 3800 - 4050 B`）。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Wheelbase = 3 (Long 3800 - 4050 B)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_WHL_BASE_LENGTH and check that it is Length_3
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_WHL_BASE_LENGTH = Length_3 is sent over LVDS
```
