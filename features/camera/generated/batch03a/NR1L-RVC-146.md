# NR1L-RVC-146 — SWE-CAM-010

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2476`（來源列 `SYS-RA-VF551_V42-326`）

## test_item 上半（verbatim，SYS2 逐字）

> LTM shall send: - vehicleUpdate_1.VC_WHL_BASE_LENGTH equal to "Length_1" IF the PROXI parameter Wheelbase is equal to "Short_2950"

## reasoning

驗證目標為 `SYS-RA-VF551_V42-326` 之 `Length_1` 分支。上半為摘句（§4.3.1）：原句 **73 token** 逾 50，刪其餘四個對映列後為 **17 token**，為原句之保序子序列，`LTM shall send:` 之主句與本分支之 PROXI 值與 LVDS 值皆保留。**五個對映只生成兩列**（`Invalid` 與 `Short_2950`）—— 其餘三值（`Medium_3450_Absent`／`Long_3800_4050B`／`Extra_Long_4050L`）於 `Promaster_ATL_MI` row 327 之列舉雖有對應項，惟其為**同一判準之等價類**（查表對映），依 §8.3 取邊界（`Invalid`）與一個有效值即足；**若審閱要求全覆蓋則擴為五列**，於上繳包 §4 具名。PROXI 值取 `Promaster_ATL_MI` row 327 之列舉逐字。依 R-CAM15(c)，V42 列承 637。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. PROXI Wheelbase = 1 (short - 2950)
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Read vehicleUpdate_1.VC_WHL_BASE_LENGTH and check that it is Length_1
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up and reads the PROXI configuration
2. vehicleUpdate_1.VC_WHL_BASE_LENGTH = Length_1 is sent over LVDS
```
