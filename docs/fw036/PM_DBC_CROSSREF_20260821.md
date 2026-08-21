# DBC 對照表：Power Management（M3 用，2026-08-21）

量測條件：解析 Pei 提供之兩份 DBC —— `PDT27_E2A_R4_BHCAN.dbc`
（BH-CAN，155 messages／883 signals）與 `PDT27_E2A_R5_FDCAN8.dbc`
（FD-CAN8，323 messages／1755 signals）。兩者網段名不同，
判為**平行網段**，非版本先後（沿既有判準）。
比對對象：PM 0820 工作簿四欄之訊號 token，distinct 點記法 20 個、
`$..$` 22 個。比對方式：精確名稱比對＋子字串模糊回查（去底線、
不分大小寫）。

## A. DBC 查得（6 個 token，可直接填三件組）

| 工作簿 token | Signal | Message | Segment |
|---|---|---|---|
| STATUS_BH_BCM2.RemStActvSts | RemStActvSts | STATUS_BH_BCM2 | BH-CAN |
| STATUS_LIN.Batt_ST_Crit | Batt_ST_Crit | STATUS_LIN | BH-CAN |
| STATUS_BH_BCM1.DriverDoorSts | DriverDoorSts | STATUS_BH_BCM1 | BH-CAN |
| STATUS_LIN.PN14_LS_Actv | PN14_LS_Actv | STATUS_LIN | BH-CAN |
| STATUS_LIN.PN14_LS_Lvl7 | PN14_LS_Lvl7 | STATUS_LIN | BH-CAN |
| CLIMATIC_PANEL.Radio_Btn0 | **Radio_btn0**（見註） | CLIMATIC_PANEL | BH-CAN |

註：DBC 之實際拼寫為 `Radio_btn0`（小寫 b），工作簿寫
`Radio_Btn0`。以 DBC 為準改為 `Radio_btn0`；此為大小寫漂移，
非新訊號。同 message 另有 Radio_btn1–4、Radio_Knob1/2_DIR/VAL。

## B. DBC 查無（14 個 token）—— 非 CAN 訊號，屬內部訊號層

TLM_Status.Info(177)、Phone_Call.Info(41)、
Antitheft_Activation.Req(39)、Auto_SwitchOn_Setting.Req(34)、
Antitheft_Result.Info(25)、LTM_OperationalModeSts.Info(20)、
SwitchOff_Timeout_Setting.Req(16)、Front_Panel_OnOff.Req(13)、
Rear_Camera_Enable.Info(11)、SwitchOffSetting.Req(5)、
PhoneCall.Info(5)、TLM_Display.GUI(2) 等。

精確與模糊比對皆零命中 → **判為 §8.7.5 之「內部訊號」層
（`X.Info` / `X.Req` / `X.GUI`），非 CAN 訊號**，不需三件組、
不需網段。此判定與其命名形態一致（`.Info`／`.Req`／`.GUI`
為內部訊號後綴，CAN 訊號無此後綴）。

**不得**因查無 DBC 而標 PENDING —— 查無在此屬正確結果，
非缺件。

## C. `$..$` PROXI 參數（22 個）

僅 `Radio_Theme` 一個同名出現於 DBC。其餘 21 個不在 DBC，
符合 PROXI 參數之預期。`$Radio_Theme$` 之同名為巧合，
工作簿用法為 PROXI，維持 `$X$` 記法不改。

## D. 對 M3 之結論

105 列訊號斷言之修法：
- 6 個 CAN token → 補足三件組 `<Signal> in <MESSAGE> on BH-CAN`
- 14 個內部 token → 維持 `X.Info`／`X.Req` 記法，僅需與
  `$..$` 分層清楚（43 列同行雙制之改寫重點在此）
- `$..$` → 不動
- 全部 105 列**無一需要標 PENDING**；DR 不新增

## E. 未決

FD-CAN8 之 1755 signals 於 PM 工作簿零命中。PM 功能是否確實
不涉 FD-CAN8，或係工作簿漏寫該網段訊號 —— 本次不擴大範圍
（§8.4.2），登記為 A-PM01 供後續覆核。
