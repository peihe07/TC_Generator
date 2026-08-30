# 作業 D — 31 條之 Pre-Condition 體例抽查（R-ICS48(f)）｜2026-08-30

**界限**：只量不改。本作業未改任何 TC（R-ICS48(f)）。

**判準**（下放包 §3 作業 D 之四類）：以 `test_procedure` 全文為對照，
取該前提項中之符號／引號值／專名，若其於步驟中出現則判「有建立步驟」；
環境／硬體前提以 IN §4.4 之 allowed types 判（工具連接、電源／睡眠狀態等）。

## §1 四類之實數

31 條之 pre_conditions 項目總數：105
  環境／硬體前提           58  (55%)
  狀態陳述、無建立步驟        42  (40%)
  狀態陳述、有建立步驟         5  (5%)

=== 逐項 ===

## §2 核心答案：**是全批體例，不是 TC 2／4 之個例**

「狀態陳述、無建立步驟」佔 **42／105（40%）**，分佈於全部七個批次，
非集中於 b03。TC 2／TC 4 之 `$Telematic_Power$` 前提只是其中二項。

依 **R-ICS47(d)**（IN §4.4 定 Pre-Condition 為起始狀態／環境且明禁寫入動作），
**該形態本身非缺陷** —— 40% 之比例與該裁定一致，並非批次品質問題。

「有建立步驟」僅 **5／105（5%）**，反而是少數；其存在不使其餘 42 項成為缺陷。

## §3 逐項明細

```
  [環境／硬體前提       ] b01 Stuck button held over 120 s         | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b01 Stuck button held over 120 s         | A diagnostic tool is connected to the vehicle
  [環境／硬體前提       ] b01 Stuck fault held until de-bounced no | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b01 Stuck fault held until de-bounced no | A diagnostic tool is connected to the vehicle
  [環境／硬體前提       ] b01 Stuck fault held until de-bounced no | A CAN trace tool is connected and able to log the button status messages sent by the HU
  [環境／硬體前提       ] b01 Button held exactly 120 s            | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b01 Button held exactly 120 s            | A diagnostic tool is connected to the vehicle
  [狀態陳述、無建立步驟    ] b01 Button held exactly 120 s            | No stuck button DTC is present in the DTC list
  [狀態陳述、無建立步驟    ] b01 VOLUME knob rotated clock-wise       | The HU is in HU Audio Mode ON mode
  [狀態陳述、無建立步驟    ] b01 VOLUME knob rotated clock-wise       | The current audio level is not at the maximum audio level
  [狀態陳述、無建立步驟    ] b01 VOLUME knob rotated counter clock-wi | The HU is in HU Audio Mode ON mode
  [狀態陳述、無建立步驟    ] b01 VOLUME knob rotated counter clock-wi | The current audio level is not at the minimum audio level
  [狀態陳述、無建立步驟    ] b01 Three detents rotated clock-wise     | The HU is in HU Audio Mode ON mode
  [狀態陳述、無建立步驟    ] b01 Three detents rotated clock-wise     | The current audio level is at least three levels below the maximum audio level (maximum 
  [狀態陳述、無建立步驟    ] b01 Three detents rotated clock-wise     | The detent counting time window of the ICS is 50 msec
  [環境／硬體前提       ] b02 Press ignored during stuck condition | The A&T System has exited SLEEP MODE
  [狀態陳述、無建立步驟    ] b02 Press ignored during stuck condition | The HU is in HU Audio Mode ON mode
  [環境／硬體前提       ] b02 Press ignored during stuck condition | A CAN trace tool is connected and able to log the ICS button status messages
  [環境／硬體前提       ] b02 Button responsive after release      | The A&T System has exited SLEEP MODE
  [狀態陳述、無建立步驟    ] b02 Button responsive after release      | The HU is in HU Audio Mode ON mode
  [環境／硬體前提       ] b02 Button responsive after release      | A CAN trace tool is connected and able to log the ICS button status messages
  [環境／硬體前提       ] b03 Power hardkey pressed while HU scree | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Power hardkey pressed while HU scree | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b03 Power hardkey pressed while HU scree | The HU is in the "HU Screen ON" state
  [狀態陳述、無建立步驟    ] b03 Power hardkey pressed while HU scree | The DCSD screen is in the "DCSD Screen ON" state
  [環境／硬體前提       ] b03 Power hardkey pressed at Telematic P | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Power hardkey pressed at Telematic P | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b03 Power hardkey pressed at Telematic P | $STATUS_TELEMATIC.PowerSts_Telematic$ is 4 (Full_Operation)
  [狀態陳述、無建立步驟    ] b03 Power hardkey pressed at Telematic P | The DCSD screen is in the "DCSD Screen ON" state
  [環境／硬體前提       ] b03 Power hardkey pressed while HU scree | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Power hardkey pressed while HU scree | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、有建立步驟    ] b03 Power hardkey pressed while HU scree | The HU is in the "HU Screen OFF" state and displays the completely black screen
  [環境／硬體前提       ] b03 Power hardkey pressed at Telematic P | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Power hardkey pressed at Telematic P | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b03 Power hardkey pressed at Telematic P | $STATUS_TELEMATIC.PowerSts_Telematic$ is 3 (Idle)
  [狀態陳述、有建立步驟    ] b03 Power hardkey pressed at Telematic P | The HU is in the "HU Screen OFF" state
  [環境／硬體前提       ] b03 Screen off hardkey starts the three  | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Screen off hardkey starts the three  | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b03 Screen off hardkey starts the three  | The HU is in the "HU Screen ON" state
  [狀態陳述、無建立步驟    ] b03 Screen off hardkey starts the three  | The DCSD screen is in the "DCSD Screen ON" state
  [環境／硬體前提       ] b03 Screen off hardkey pressed again wit | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Screen off hardkey pressed again wit | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b03 Screen off hardkey pressed again wit | The HU is in the "HU Screen ON" state
  [狀態陳述、無建立步驟    ] b03 Screen off hardkey pressed again wit | The DCSD screen is in the "DCSD Screen ON" state
  [環境／硬體前提       ] b03 Three second period completed after  | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Three second period completed after  | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b03 Three second period completed after  | The HU is in the "HU Screen ON" state
  [狀態陳述、無建立步驟    ] b03 Three second period completed after  | The DCSD screen is in the "DCSD Screen ON" state
  [環境／硬體前提       ] b03 Screen off hardkey pressed while HU  | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b03 Screen off hardkey pressed while HU  | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、有建立步驟    ] b03 Screen off hardkey pressed while HU  | The HU is in the "HU Screen OFF" state and displays the completely black screen
  [環境／硬體前提       ] b04 Knob 2 rotated clock-wise            | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Knob 2 rotated clock-wise            | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、無建立步驟    ] b04 Knob 2 rotated clock-wise            | The ICS knob 2 is not being rotated
  [狀態陳述、無建立步驟    ] b04 Knob 2 rotated clock-wise            | The no-change resend period of the ICS is 20 msec
  [環境／硬體前提       ] b04 Knob 2 rotated counter clock-wise    | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Knob 2 rotated counter clock-wise    | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、無建立步驟    ] b04 Knob 2 rotated counter clock-wise    | The ICS knob 2 is not being rotated
  [狀態陳述、無建立步驟    ] b04 Knob 2 rotated counter clock-wise    | The no-change resend period of the ICS is 20 msec
  [環境／硬體前提       ] b04 Knob 2 held stationary               | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Knob 2 held stationary               | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、無建立步驟    ] b04 Knob 2 held stationary               | The ICS knob 2 is not being rotated
  [環境／硬體前提       ] b04 Knob 2 no change sent periodically   | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Knob 2 no change sent periodically   | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、無建立步驟    ] b04 Knob 2 no change sent periodically   | The ICS knob 2 has just been rotated one detent position clock-wise
  [環境／硬體前提       ] b04 Three detents counted in one rotatio | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Three detents counted in one rotatio | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、無建立步驟    ] b04 Three detents counted in one rotatio | The ICS knob 2 is not being rotated
  [狀態陳述、無建立步驟    ] b04 Three detents counted in one rotatio | The detent counting time window of the ICS is 50 msec
  [環境／硬體前提       ] b04 Knob 2 signals acted on by the HU    | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Knob 2 signals acted on by the HU    | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、無建立步驟    ] b04 Knob 2 signals acted on by the HU    | The HU shows a screen for which a browse action is defined for knob 2 (screen identified
  [狀態陳述、無建立步驟    ] b04 Knob 2 signals acted on by the HU    | The ICS knob 2 is not being rotated
  [環境／硬體前提       ] b04 Enter button pressed                 | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b04 Enter button pressed                 | A CAN trace tool is connected and able to log the ICS knob and button status messages
  [狀態陳述、有建立步驟    ] b04 Enter button pressed                 | The HU shows a screen for which an Enter action is defined (screen identified per PENDIN
  [環境／硬體前提       ] b05 Knob 2 rotated on a scrollable scree | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b05 Knob 2 rotated on a scrollable scree | A CAN trace tool is connected and able to log the ICS knob status messages
  [狀態陳述、無建立步驟    ] b05 Knob 2 rotated on a scrollable scree | The HU shows a screen for which a scroll action is defined for knob 2 (screen identified
  [狀態陳述、無建立步驟    ] b05 Knob 2 rotated on a scrollable scree | The ICS knob 2 is not being rotated
  [環境／硬體前提       ] b05 Knob 2 rotated on a tuner source     | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b05 Knob 2 rotated on a tuner source     | A CAN trace tool is connected and able to log the ICS knob status messages
  [狀態陳述、無建立步驟    ] b05 Knob 2 rotated on a tuner source     | The HU is on a tuner source for which a tune action is defined for knob 2 (source identi
  [狀態陳述、無建立步驟    ] b05 Knob 2 rotated on a tuner source     | The ICS knob 2 is not being rotated
  [環境／硬體前提       ] b06 Mute hardkey pressed while audio unm | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b06 Mute hardkey pressed while audio unm | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b06 Mute hardkey pressed while audio unm | The HU is in HU Audio Mode ON mode with an entertainment audio source playing
  [狀態陳述、無建立步驟    ] b06 Mute hardkey pressed while audio unm | The entertainment audio source is not muted
  [環境／硬體前提       ] b06 Mute hardkey pressed while audio mut | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b06 Mute hardkey pressed while audio mut | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、無建立步驟    ] b06 Mute hardkey pressed while audio mut | The HU is in HU Audio Mode ON mode with an entertainment audio source playing
  [狀態陳述、無建立步驟    ] b06 Mute hardkey pressed while audio mut | The entertainment audio source is muted
  [環境／硬體前提       ] b07 Back button pressed                  | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b07 Back button pressed                  | A CAN trace tool is connected and able to log the ICS button status messages
  [狀態陳述、有建立步驟    ] b07 Back button pressed                  | The HU shows a screen for which a Back action is defined (screen identified per PENDING:
  [環境／硬體前提       ] b07 Two ICS buttons pressed at the same  | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b07 Two ICS buttons pressed at the same  | A CAN trace tool is connected and able to log the ICS button and knob status messages
  [狀態陳述、無建立步驟    ] b07 Two ICS buttons pressed at the same  | No ICS button is pressed
  [環境／硬體前提       ] b07 Button event change reported within  | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b07 Button event change reported within  | A CAN trace tool is connected and able to log the ICS button and knob status messages
  [狀態陳述、無建立步驟    ] b07 Button event change reported within  | No ICS button is pressed
  [環境／硬體前提       ] b07 Button event change reported within  | The CAN trace tool timestamps each received frame with a resolution of 1 msec or finer
  [環境／硬體前提       ] b07 Knob 1 status sent on BH-CAN         | The A&T System has exited SLEEP MODE
  [環境／硬體前提       ] b07 Knob 1 status sent on BH-CAN         | A CAN trace tool is connected and able to log the ICS button and knob status messages
  [狀態陳述、無建立步驟    ] b07 Knob 1 status sent on BH-CAN         | The ICS knob 1 is not being rotated
```

## §4 已知局限

- 「有建立步驟」之判定以字面比對為之（前提項中之符號／引號值／專名是否出現於步驟）；
  語意上等價但用詞不同者會被判為「無建立步驟」，故該類之 42 為**上限**。
- 未查 IN §4.4 之 allowed types 逐條清單，環境類之 58 係以關鍵詞判，屬近似。
- 本作業未判任何一項是否「應該」有建立步驟 —— 依 R-ICS47(d) 該問已由分析層裁定為非缺陷。
