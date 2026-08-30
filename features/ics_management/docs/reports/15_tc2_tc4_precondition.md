# 作業 D — TC 2／TC 4 之前提建立法（A-ICS91）｜2026-08-30

**界限**：只量不改。本作業未改任何步驟、ER、錨或佔位。

---

## §1 二條之全文逐字

### TC 2 — `Power hardkey pressed at Telematic Power full operation`（錨：`CFTS020-4819561`）

**pre_conditions**
```
1. The A&T System has exited SLEEP MODE
2. A CAN trace tool is connected and able to log the ICS button status messages
3. $Telematic_Power$ is in the "Full_Operation" state
4. The DCSD screen is in the "DCSD Screen ON" state
```
**input_test_data**：`NA`

**test_procedure**
```
1. Read the display status signal on the CAN trace and record it (signal name PENDING: DR-ICS8 <TGW_DISP_STAT CAN signal>)
2. Press the ICS "Power" button
3. Read the signal $CLIMATIC_PANEL.Radio_btn0$ and check that it is 1 (Pressed)
4. Read the display status signal on the CAN trace and check that it is the "DISP_OFF" value (signal name PENDING: DR-ICS8 <TGW_DISP_STAT CAN signal>)
5. Read the signal $RADIO_B3.RQ_DISP_INTS$ on the CAN trace and check that it is 0 (0 %)
6. Check that the HU screen is dark and shows no content
```
**expected_result**
```
1. The display status signal is recorded on the CAN trace (supporting observation)
2. The "Power" button enters the pressed state
3. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the CAN trace (supporting observation)
4. The display status signal reports the "DISP_OFF" value on the CAN trace (supporting observation)
5. The signal value $RADIO_B3.RQ_DISP_INTS$ = 0 (0 %) is observed on the CAN trace (supporting observation)
6. The HU screen is dark and shows no content
```

### TC 4 — `Power hardkey pressed at Telematic Power idle`（錨：`CFTS020-4819564`）

**pre_conditions**
```
1. The A&T System has exited SLEEP MODE
2. A CAN trace tool is connected and able to log the ICS button status messages
3. $Telematic_Power$ is in the "Idle" state
4. The HU is in the "HU Screen OFF" state
```
**input_test_data**：`NA`

**test_procedure**
```
1. Record the screen that was shown before the HU entered the "HU Screen OFF" state
2. Press the ICS "Power" button
3. Read the signal $CLIMATIC_PANEL.Radio_btn0$ and check that it is 1 (Pressed)
4. Read the display status signal on the CAN trace and check that it is the "DISP_NORMAL" value (signal name PENDING: DR-ICS8 <TGW_DISP_STAT CAN signal>)
5. Check that the screen shown is the same as the screen recorded in step 1
```
**expected_result**
```
1. The previously shown screen is recorded
2. The "Power" button enters the pressed state
3. The signal value $CLIMATIC_PANEL.Radio_btn0$ = 1 (Pressed) is observed on the CAN trace (supporting observation)
4. The display status signal reports the "DISP_NORMAL" value on the CAN trace (supporting observation)
5. The previous "HU Screen ON" screen is shown again
```

---

## §2 前提現行以何法建立 —— **第三種：根本未寫如何建立**

下放包所列三種可能：

| 可能 | 實測 |
|---|---|
| 以 CAN 輸入餵入（哪一步驟）| **否** —— 二條之 `test_procedure` 中，**無任何一步驟提及 `$Telematic_Power$`**（TC 2 六步、TC 4 五步，逐步核對）|
| 以 DUT 自身之電源模式／PROXI／其他設定建立 | **否** —— `pre_conditions` 未載任何建立方法；`input_test_data` 為 `NA` |
| **根本未寫如何建立** | **是** —— `$Telematic_Power$` 僅出現於 `pre_conditions` 第 3 項，且該項為狀態陳述（`is in the "Full_Operation" state`），**無對應之建立步驟** |

**`$Telematic_Power$` 於二條中之出現次數：各 1 次，皆在 `pre_conditions`。**

---

## §3 故 A-ICS91 之「餵不進去」**可能不是本二條之問題**

A-ICS91（源自 upstream-14 §3-5）之疑慮為：
於 Pei 所裁之 BHCAN2，本 DUT 是 `PowerSts_Telematic` 之**發送側**，
`ICS` 既非收方亦不在 `BU_` 內，故台架**無路在該匯流排上餵給 DUT 此前提值**。

**該疑慮預設了「前提是以 CAN 餵入建立的」。實測顯示：二條從未指定以任何方法建立該前提。**

因此：

- **若**該前提之建立法日後被指定為「以 CAN 餵入」→ A-ICS91 之疑慮成立，二條需改。
- **若**被指定為其他方法（電源模式操作、PROXI、台架序列、上游 ETM 之實際狀態）
  → A-ICS91 之疑慮**與本二條無關**，二條只是缺一項 Pre-Condition 之建立說明。
- **現況**：**未指定**，故二者皆未定。

**執行層不推定何者為真，亦不推定「未寫建立方法」本身是否為缺陷**
（IN §4.4 對 Pre-Condition 是否須附建立步驟之要求，本作業未查，列為未驗項）。

---

## §4 二條之錨 —— 【E28 未觸發】

| TC | 錨（逐字）| 該物件之主詞 |
|---|---|---|
| TC 2 | `CFTS020-4819561` | **HU** |
| TC 4 | `CFTS020-4819564` | **HU** |

`4819561` 逐字（節錄）：
> If $Telematic_Power$ = [Full_Operation] and the DCSD Screen is in the 'DCSD Screen ON' state ($DCSD_DISP_STAT$ = [ON]) and **the HU** determines that the ICS POWER hardkey should be responded to, then **the HU shall** immediately send $TG...

`4819564` 逐字：
> If $Telematic_Power$ = [Idle] and the ICS POWER hardkey is pressed **the HU shall** send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] and the HU shall return to the previous 'HU Screen ON' s...

**二條之錨皆非 `4819144`／`4820117`，且其主詞為 `HU`（本 DUT）而非 `ICS`（面板）→ E28 未觸發。**

**附帶查明**：`4819144`／`4820117`（主詞為 ICS 面板、內容為 Diagnostics 之啟閉）
**未被本線任何一條 TC 引為錨** —— 二者於 31 條之 `specification_reference` 中命中 **0**。
故 upstream-14 §3-3 引該二物件證明「規格說 ICS 接收 `$Telematic_Power$`」時，
**所引者並非本二條之錨**。此點 upstream-14 未區分，**於此具名更正**：
`$Telematic_Power$` 在本二條中的角色是**前提條件**（來自其錨 `4819561`／`4819564` 之條件子句），
不是「ICS 依其啟閉 Diagnostics」那條需求。

---

## §5 下放包未預料之事

1. **§4 附帶**：upstream-14 §3-3 以 `4819144`／`4820117` 論證，
   但該二物件**不是 TC 2／TC 4 之錨**，且未被任何 TC 引用。
   A-ICS91 之論據因此需要重新指認 —— 本二條之 `$Telematic_Power$` 來自 `4819561`／`4819564`
   之條件子句，其主詞為 HU。
2. **二條之 `$Telematic_Power$` 為裸符號**（`$Telematic_Power$`），
   非 IN §8.7.5(a) 之 `$MESSAGE.Signal$` 式 —— 與同檔中 `$CLIMATIC_PANEL.Radio_btn0$`
   之寫法不一致。**只列不改**（本包禁區）。
3. 二條之 `pre_conditions` 第 2 項為
   `A CAN trace tool is connected and able to log the ICS button status messages`
   —— 只提 **log**（讀），未提 **inject**（寫）。台架能力面本身即未涵蓋餵入。

## §6 已知局限

- 未查 IN §4.4 對 Pre-Condition 是否須附建立步驟之規定，故未判「未寫建立方法」是否為缺陷。
- 未查其餘 29 條之 Pre-Condition 是否同樣有「只陳述狀態、不寫建立法」之情形
  —— 若普遍如此，則本件非二條所獨有。
